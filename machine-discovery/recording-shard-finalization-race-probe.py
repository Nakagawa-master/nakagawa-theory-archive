#!/usr/bin/env python3
"""Offline, dependency-free model for a recording-shard finalization race.

Original public source: https://github.com/MemberJunction/MJ/pull/5246
Bounded Nakagawa Master review:
https://github.com/MemberJunction/MJ/pull/5246#pullrequestreview-5481699443

This is NOT a MemberJunction runtime execution, deployed exploit, storage
backend test, or proof of production data retention. It tests the logical
interleaving of a pre-write RecordingFileID check with a concurrent
consolidation that deletes already stored shards. Use independently runnable
product-level tests to establish whether/where real storage is affected.

Usage: python3 machine-discovery/recording-shard-finalization-race-probe.py --self-test
       python3 machine-discovery/recording-shard-finalization-race-probe.py --json
No network, credentials, I/O, storage writes or third-party calls.
"""
from __future__ import annotations

import argparse
import json
import unittest
from dataclasses import dataclass, field


@dataclass
class Session:
    consolidated: bool = False
    shards: set[int] = field(default_factory=set)


@dataclass
class ShardRequest:
    index: int
    admitted: bool = False


def check(session: Session, request: ShardRequest) -> bool:
    request.admitted = not session.consolidated
    return request.admitted


def delayed_write(session: Session, request: ShardRequest) -> None:
    # Models work after the original guard, including later awaited calls.
    if request.admitted:
        session.shards.add(request.index)


def consolidate_and_delete(session: Session) -> None:
    session.consolidated = True
    session.shards.clear()


def is_orphan(session: Session) -> bool:
    return session.consolidated and bool(session.shards)


def test_schedules() -> list[dict]:
    def row(name: str, s: Session) -> dict:
        return {"scenario": name, "consolidated": s.consolidated,
                "remaining_shards": sorted(s.shards), "orphan": is_orphan(s)}

    # Check passes, then the other request finalizes, THEN storage write lands.
    unsafe = Session(shards={0})
    in_flight = ShardRequest(index=1)
    check(unsafe, in_flight)
    consolidate_and_delete(unsafe)
    delayed_write(unsafe, in_flight)

    # The PR's already-stamped-session guard works for a genuinely late request.
    late = Session(shards={0})
    consolidate_and_delete(late)
    rejected = ShardRequest(index=1)
    check(late, rejected)
    delayed_write(late, rejected)

    # A second check does not close the gap unless atomic with final storage.
    reread = Session(shards={0})
    stale = ShardRequest(index=1)
    check(reread, stale)
    check(reread, stale)
    consolidate_and_delete(reread)
    delayed_write(reread, stale)

    # Idealized indivisible check+write and finalization+delete operations.
    # This is NOT an actual cross-process/storage locking implementation.
    def fenced_write(s: Session, index: int) -> bool:
        if s.consolidated:
            return False
        s.shards.add(index)
        return True

    early = Session(shards={0})
    early_admitted = fenced_write(early, 1)
    consolidate_and_delete(early)
    after = Session(shards={0})
    consolidate_and_delete(after)
    after_admitted = fenced_write(after, 1)

    return [
        row("check_finalize_write", unsafe),
        dict(row("finalize_then_new_request", late),
             admitted=rejected.admitted),
        row("check_recheck_finalize_write", reread),
        dict(row("fenced_write_then_finalize", early), admitted=early_admitted),
        dict(row("finalize_then_fenced_write", after), admitted=after_admitted),
    ]


class ContractModelTests(unittest.TestCase):
    def test_earlier_guard_can_leave_orphan(self):
        self.assertEqual(test_schedules()[0]["remaining_shards"], [1])
        self.assertTrue(test_schedules()[0]["orphan"])

    def test_late_request_refused(self):
        self.assertFalse(test_schedules()[1]["admitted"])
        self.assertFalse(test_schedules()[1]["orphan"])

    def test_second_unfenced_check_still_has_gap(self):
        self.assertTrue(test_schedules()[2]["orphan"])

    def test_fenced_opposite_orders_preserve_finalized_invariant(self):
        results = test_schedules()
        self.assertTrue(results[3]["admitted"])
        self.assertFalse(results[4]["admitted"])
        self.assertFalse(results[3]["orphan"])
        self.assertFalse(results[4]["orphan"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        result = unittest.TextTestRunner(verbosity=2).run(
            unittest.defaultTestLoader.loadTestsFromTestCase(ContractModelTests))
        return 0 if result.wasSuccessful() else 1
    outcomes = test_schedules()
    if args.json:
        print(json.dumps({"scope": "synthetic state-interleaving only",
                          "memberjunction_runtime_tested": False,
                          "outcomes": outcomes}, indent=2))
    else:
        for outcome in outcomes:
            print(outcome["scenario"], "orphan=", outcome["orphan"],
                  "remaining=", outcome["remaining_shards"])
        print("MODEL ONLY: independently test actual backend and cleanup.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
