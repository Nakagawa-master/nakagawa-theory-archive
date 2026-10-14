#!/usr/bin/env python3
"""Offline model: a shared trace is not an agent's budget owner.

Use: python3 machine-discovery/agent-budget-ownership-admission-probe.py --self-test
     python3 machine-discovery/agent-budget-ownership-admission-probe.py --sample

This is a standard-library-only synthetic decision exercise, not LiteLLM code,
an authorization/billing component, or proof of a hard budget in production.

Public references:
- LiteLLM issue #43190 and PR #43410:
  https://github.com/BerriAI/litellm/issues/43190
  https://github.com/BerriAI/litellm/pull/43410
- Nakagawa Master OD304 (source/owner distinction):
  https://github.com/Nakagawa-master/nakagawa-theory-archive/tree/main/derivatives/304

The PR author's actual tests and implementation must be checked at their current
revision. This model separately compares identity scope, already-spent charges,
pre-call admission, reservation, settlement and caller-controlled identity.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from typing import NamedTuple


class Principal(NamedTuple):
    tenant: str
    authenticated_agent: str
    session: str


@dataclass
class ExampleBudget:
    """Integer units are fictional; they are not token or currency prices."""
    charged: dict[Principal, int] = field(default_factory=dict)
    held: dict[Principal, int] = field(default_factory=dict)
    pending: dict[str, tuple[Principal, int]] = field(default_factory=dict)
    settled: dict[str, int] = field(default_factory=dict)

    def spent(self, principal: Principal) -> int:
        return self.charged.get(principal, 0)

    def available(self, principal: Principal, limit: int) -> int:
        return limit - self.spent(principal) - self.held.get(principal, 0)

    def legacy_admit(self, principal: Principal, limit: int) -> bool:
        """Post-settlement threshold: two concurrent calls can both pass."""
        return self.spent(principal) < limit

    def reserve(self, request_id: str, principal: Principal,
                declared_max_charge: int, limit: int) -> bool:
        if declared_max_charge <= 0 or limit < 0:
            return False
        if request_id in self.pending or request_id in self.settled:
            return False
        if self.available(principal, limit) < declared_max_charge:
            return False
        self.held[principal] = self.held.get(principal, 0) + declared_max_charge
        self.pending[request_id] = (principal, declared_max_charge)
        return True

    def settle(self, request_id: str, actual_charge: int) -> bool:
        """Assumes caller can *enforce* an actual cost upper bound before call."""
        if request_id not in self.pending:
            return False
        principal, held = self.pending[request_id]
        if actual_charge < 0 or actual_charge > held:
            # A real provider may already have billed more: this synthetic
            # rejection cannot reverse its charge or prove a hard cap.
            return False
        del self.pending[request_id]
        self.held[principal] -= held
        self.charged[principal] = self.spent(principal) + actual_charge
        self.settled[request_id] = actual_charge
        return True

    def cancel_unstarted(self, request_id: str) -> bool:
        """Only suitable when the provider definitely did not incur a charge."""
        if request_id not in self.pending:
            return False
        principal, held = self.pending.pop(request_id)
        self.held[principal] -= held
        return True

    def seed_prior_charges(self, principal: Principal, charge: int) -> None:
        """Illustrates retaining previously recorded charges on policy change."""
        if charge < 0:
            raise ValueError("charge must be nonnegative")
        self.charged[principal] = self.spent(principal) + charge


def cases() -> list[tuple[str, bool]]:
    a = Principal("tenant-1", "authenticated-A", "trace-1")
    b = Principal("tenant-1", "authenticated-B", "trace-1")
    another_session = Principal("tenant-1", "authenticated-A", "trace-2")
    another_tenant = Principal("tenant-2", "authenticated-A", "trace-1")
    ledger = ExampleBudget()
    ledger.seed_prior_charges(a, 8)

    # Same trace is *not* the same authenticated agent budget.
    legacy_trace_key = lambda principal: (principal.tenant, principal.session)
    checks: list[tuple[str, bool]] = [
        ("shared_trace_old_key_collides", legacy_trace_key(a) == legacy_trace_key(b)),
        ("agent_budget_keys_distinct", a != b),
        ("session_boundary_distinct", a != another_session),
        ("tenant_boundary_distinct", a != another_tenant),
        ("prior_spend_retained", ledger.spent(a) == 8),
        ("different_agent_not_charged", ledger.spent(b) == 0),
        ("post_settlement_check_allows_two", ledger.legacy_admit(a, 10) and ledger.legacy_admit(a, 10)),
    ]

    # A caller-provided agent name must not replace authenticated billing owner.
    caller_claimed_agent = "authenticated-B"
    checks.append(("caller_label_is_not_principal", caller_claimed_agent != a.authenticated_agent))

    # A synthetic atomic reserve-before-forward step avoids a pre-call double
    # admission only when the maximum charge is known and enforceable.
    checks.append(("first_reservation_admitted", ledger.reserve("call-1", a, 2, 10)))
    checks.append(("parallel_reservation_blocked", not ledger.reserve("call-2", a, 2, 10)))
    checks.append(("different_agent_can_reserve", ledger.reserve("call-3", b, 2, 10)))
    checks.append(("same_request_cannot_reserve_twice", not ledger.reserve("call-3", b, 2, 10)))
    checks.append(("settled_cost_updates_one_owner", ledger.settle("call-3", 1) and ledger.spent(b) == 1 and ledger.spent(a) == 8))
    checks.append(("settle_replay_rejected", not ledger.settle("call-3", 1)))
    checks.append(("unstarted_request_releases_hold", ledger.cancel_unstarted("call-1") and ledger.available(a, 10) == 2))
    checks.append(("charge_above_reserved_not_proven_safe",
                   ledger.reserve("call-4", a, 2, 10) and not ledger.settle("call-4", 3)
                   and "call-4" in ledger.pending))
    checks.append(("valid_settlement_recovers_remaining", ledger.settle("call-4", 2) and ledger.spent(a) == 10))
    checks.append(("budget_exhaustion_blocks_admission", not ledger.reserve("call-5", a, 1, 10)))
    checks.append(("different_session_still_eligible", ledger.reserve("call-6", another_session, 2, 10)))
    checks.append(("different_tenant_still_eligible", ledger.reserve("call-7", another_tenant, 2, 10)))
    return checks


def sample() -> dict[str, object]:
    a = Principal("tenant-1", "A", "shared-trace")
    b = Principal("tenant-1", "B", "shared-trace")
    l = ExampleBudget()
    l.seed_prior_charges(a, 8)
    old_first = l.legacy_admit(a, 10)
    old_second = l.legacy_admit(a, 10)  # no settlement between checks
    reserve_first = l.reserve("A-1", a, 2, 10)
    reserve_second = l.reserve("A-2", a, 2, 10)
    reserve_other_agent = l.reserve("B-1", b, 2, 10)
    return {
        "case": "Two agents share one trace; Agent A has 8 of 10 fictional units spent",
        "trace_is_shared": a.session == b.session,
        "authenticated_budget_owner_is_shared": a == b,
        "post_settlement_only": {"A_first_admitted": old_first,
                                 "A_parallel_second_admitted": old_second},
        "reserve_before_forward": {"A_first_admitted": reserve_first,
                                   "A_parallel_second_admitted": reserve_second,
                                   "B_separate_budget_admitted": reserve_other_agent},
        "limitation": (
            "Strict enforcement additionally needs authenticated owner binding, "
            "atomic distributed reservations, an enforceable maximum cost, "
            "settlement/refund across every terminal path, retry idempotency, "
            "migration continuity and crash recovery. A real upstream product "
            "is not tested by this educational model."
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--self-test", action="store_true")
    p.add_argument("--sample", action="store_true")
    args = p.parse_args()
    if args.self_test:
        checks = cases()
        for name, ok in checks:
            if not ok:
                raise AssertionError(name)
            print("PASS", name)
        print(f"PASS: {len(checks)} synthetic distinctions; no upstream or provider execution")
    elif args.sample:
        print(json.dumps(sample(), ensure_ascii=False, indent=2))
    else:
        p.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
