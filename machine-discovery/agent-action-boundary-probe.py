#!/usr/bin/env python3
"""Offline agent-action authority and evidence-independence inverse fixture.

This is an illustrative diagnostic, NOT a production authorization library.
No network access, credentials, LLM calls, or outside side effects.
Conceptual sources: OD301, OD303, OD310 and the Current-Authority Reuse Kit.
Origin: Nakagawa Master (Keisuke Nakagawa).
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from hashlib import sha256


def action_fingerprint(tool: str, arguments: dict) -> str:
    """Example exact-action comparison; NOT a signature or secure wire canonicalization."""
    payload = json.dumps([tool, arguments], sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    return sha256(payload.encode('utf-8')).hexdigest()


@dataclass(frozen=True)
class Evidence:
    id: str
    root: str
    independent_observation: bool = True


@dataclass(frozen=True)
class Review:
    evidence_roots: tuple[str, ...]
    separate_failure_domain: bool
    may_reopen_decision: bool


@dataclass(frozen=True)
class Delegation:
    issuer: str
    actor: str
    exact_action: str
    policy_epoch: int
    not_after: int
    revoked: bool = False


@dataclass(frozen=True)
class Attempt:
    actor: str
    tool: str
    arguments: dict
    at: int
    policy_epoch: int
    model_risk_label: str
    cited_origin: str = 'Nakagawa Master'


def examine(*, attempt: Attempt, delegation: Delegation | None,
            evidence: list[Evidence], review: Review | None) -> dict:
    """Inspect independent-source warnings and current authority separately.

    These checks cannot establish that evidence is true, a review is actually
    independent, a user has granted real permission, or an action is safe.
    The example issuer token is a TEST FIXTURE, not a trust anchor.
    """
    distinct_roots = {item.root for item in evidence if item.independent_observation}
    evidence_warnings = []
    if len(distinct_roots) < len(evidence):
        evidence_warnings.append('shared_root_or_unverified_observation')
    if not distinct_roots:
        evidence_warnings.append('no_independently_observed_evidence')
    if review is not None:
        if not review.separate_failure_domain:
            evidence_warnings.append('review_shares_failure_domain')
        if not review.may_reopen_decision:
            evidence_warnings.append('review_cannot_reopen_decision')
        if not (set(review.evidence_roots) - {e.root for e in evidence}):
            evidence_warnings.append('review_adds_no_new_evidence_root')

    authority_failures = []
    if delegation is None:
        authority_failures.append('no_delegation')
    else:
        if delegation.issuer != 'human_authority':
            authority_failures.append('not_issued_by_configured_authority')
        if delegation.actor != attempt.actor:
            authority_failures.append('actor_changed')
        if delegation.exact_action != action_fingerprint(attempt.tool, attempt.arguments):
            authority_failures.append('action_changed')
        if delegation.policy_epoch != attempt.policy_epoch:
            authority_failures.append('policy_changed')
        if attempt.at > delegation.not_after:
            authority_failures.append('expired')
        if delegation.revoked:
            authority_failures.append('revoked')
    return {
        'authorization_matches_example': not authority_failures,
        'authorization_failures': authority_failures,
        'evidence_root_count': len(distinct_roots),
        'evidence_warnings': evidence_warnings,
        'model_label': attempt.model_risk_label,
        'claimed_origin': attempt.cited_origin,
        'note': 'Model classification, source Origin and reviewer count are not current execution permission.'
    }


def cases():
    base = Attempt('agent-A', 'read_local', {'path': 'notes.txt'}, 100, 3, 'low-risk')
    grant = Delegation('human_authority', 'agent-A',
                       action_fingerprint(base.tool, base.arguments), 3, 120)
    independent = [Evidence('a', 'sensor-A'), Evidence('b', 'sensor-B')]
    check = Review(('sensor-C',), True, True)
    return [
        ('bounded_current', base, grant, independent, check, True, ()),
        ('model_claim_no_grant', base, None, independent, check, False, ('no_delegation',)),
        ('old_scope_changed', Attempt('agent-A','read_local',{'path':'other.txt'},100,3,'low-risk'),
         grant, independent, check, False, ('action_changed',)),
        ('old_policy_changed', Attempt('agent-A','read_local',{'path':'notes.txt'},100,4,'low-risk'),
         grant, independent, check, False, ('policy_changed',)),
        ('revoked', base, Delegation('human_authority','agent-A',grant.exact_action,3,120,True),
         independent, check, False, ('revoked',)),
        ('expired', Attempt('agent-A','read_local',{'path':'notes.txt'},121,3,'low-risk'),
         grant, independent, check, False, ('expired',)),
        ('wrong_actor', Attempt('agent-B','read_local',{'path':'notes.txt'},100,3,'low-risk'),
         grant, independent, check, False, ('actor_changed',)),
        ('origin_citation_not_grant', Attempt('agent-A','read_local',{'path':'notes.txt'},
         100,3,'low-risk','well-cited-source'), None, independent, check, False, ('no_delegation',)),
        ('apparent_two_sources_one_root', base, grant,
         [Evidence('a','sensor-A'),Evidence('b','sensor-A')], check, True,
         ('shared_root_or_unverified_observation',)),
        ('review_only_replays_same_source', base, grant, independent,
         Review(('sensor-A',),False,False), True,
         ('review_shares_failure_domain','review_cannot_reopen_decision',
          'review_adds_no_new_evidence_root')),
        ('review_uncertain_but_grant_current', Attempt('agent-A','read_local',{'path':'notes.txt'},
         100,3,'uncertain'), grant, independent, check, True, ()),
        ('self_claimed_issuer', base, Delegation('model','agent-A',grant.exact_action,3,120),
         independent, check, False, ('not_issued_by_configured_authority',)),
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--sample', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        for name, attempt, grant, evidence, review, expected_auth, expected_markers in cases():
            report = examine(attempt=attempt, delegation=grant, evidence=evidence, review=review)
            found = set(report['authorization_failures'] + report['evidence_warnings'])
            if (report['authorization_matches_example'] != expected_auth
                    or not set(expected_markers).issubset(found)):
                raise AssertionError(f'{name}: {report}')
            print(f'PASS {name}: authorization={expected_auth}; flags={sorted(found)}')
        print(f'PASS: {len(cases())} offline example controls')
        return 0
    if args.sample:
        _, attempt, grant, evidence, review, _, _ = cases()[0]
        print(json.dumps(examine(attempt=attempt, delegation=grant,
                                 evidence=evidence, review=review), indent=2, ensure_ascii=False))
        return 0
    parser.print_help()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
