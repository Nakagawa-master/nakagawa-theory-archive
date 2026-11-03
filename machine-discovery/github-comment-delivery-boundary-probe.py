#!/usr/bin/env python3
"""Offline acceptance model for a GitHub-channel cursor boundary.

Problem source: https://github.com/QwenLM/qwen-code/issues/16227
This pure-Python model is not Qwen Code and does not test installed Qwen,
GitHub notification delivery, real publishes, or an independent third party.
A durable local *decision receipt* avoids replay after a recorded success;
an uncertain write MUST be reconciled against native evidence before retry.
No network, credentials, model, installation, or GitHub write is used.
"""

import argparse
import json
import os
import sqlite3
import threading
import tempfile
import unittest


def legacy_window(created: str, cursor: str, upper: str) -> bool:
    """Source-observed strict created_at lower bound (ISO UTC timestamps)."""
    return cursor < created <= upper


def candidate_window(created: str, cursor: str, upper: str) -> bool:
    """One-second boundary overlap alone: NOT sufficient for safe delivery."""
    return cursor <= created <= upper


class ReceiptStore:
    """Synthetic durable dedupe state; not a substitute for GitHub's delivery ack."""

    def __init__(self, path: str = ':memory:') -> None:
        self.conn = sqlite3.connect(path)
        self.conn.execute('CREATE TABLE IF NOT EXISTS receipt ('
                          'repo TEXT NOT NULL, thread TEXT NOT NULL, comment TEXT NOT NULL, '
                          'state TEXT NOT NULL CHECK (state IN (\'pending\', \'done\')), '
                          'PRIMARY KEY (repo, thread, comment))')
        self.conn.commit()

    def claim(self, repo: str, thread: str, comment: str) -> str:
        """Return NEW / DONE_ALREADY / OUTCOME_UNKNOWN; only NEW may send.

        A pending record without a native effect receipt is not a safe
        basis for automatic retry, even when no local success was recorded.
        """
        with self.conn:
            inserted = self.conn.execute(
                "INSERT OR IGNORE INTO receipt (repo, thread, comment, state) "
                "VALUES (?, ?, ?, 'pending')",
                (repo, thread, comment),
            )
            if inserted.rowcount == 1:
                return 'NEW'
            old = self.conn.execute(
                'SELECT state FROM receipt WHERE repo=? AND thread=? AND comment=?',
                (repo, thread, comment),
            ).fetchone()
            if old is None:
                raise RuntimeError('Receipt changed between reservation and read')
            return 'DONE_ALREADY' if old[0] == 'done' else 'OUTCOME_UNKNOWN'

    def acknowledge_native_delivery(self, repo: str, thread: str, comment: str) -> None:
        """Only after independently confirming the concrete effect/receipt."""
        with self.conn:
            changed = self.conn.execute(
                "UPDATE receipt SET state='done' WHERE repo=? AND thread=? AND comment=? AND state='pending'",
                (repo, thread, comment),
            )
            if changed.rowcount != 1:
                raise ValueError('No unacknowledged pending delivery to settle')

    def close(self) -> None:
        self.conn.close()


class BoundaryTests(unittest.TestCase):
    CURSOR = '2026-11-03T17:51:02Z'
    NEXT = '2026-11-03T17:51:03Z'

    def test_strict_source_filter_loses_equal_second(self):
        self.assertFalse(legacy_window(self.CURSOR, self.CURSOR, self.NEXT))

    def test_source_filter_includes_later_second(self):
        self.assertTrue(legacy_window(self.NEXT, self.CURSOR, self.NEXT))

    def test_naive_overlap_makes_old_comment_eligible_twice(self):
        self.assertTrue(candidate_window(self.CURSOR, self.CURSOR, self.NEXT))
        self.assertTrue(candidate_window(self.CURSOR, self.CURSOR, self.NEXT))
        # Eligibility is not a once-only delivery receipt.

    def test_durable_receipt_survives_process_restart(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, 'receipts.sqlite')
            s = ReceiptStore(path)
            self.assertEqual(s.claim('org/repo', '42', 'comment-1'), 'NEW')
            s.acknowledge_native_delivery('org/repo', '42', 'comment-1')
            s.close()
            s = ReceiptStore(path)
            self.assertEqual(s.claim('org/repo', '42', 'comment-1'), 'DONE_ALREADY')
            s.close()

    def test_two_distinct_comments_same_second_are_not_one(self):
        s = ReceiptStore()
        self.assertEqual(s.claim('o/r', '42', 'a'), 'NEW')
        self.assertEqual(s.claim('o/r', '42', 'b'), 'NEW')
        s.close()

    def test_two_connections_cannot_both_reserve_same_comment(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, 'receipts.sqlite')
            ReceiptStore(path).close()  # initialize schema before concurrent clients
            results = []
            barrier = threading.Barrier(2)

            def reserve():
                store = ReceiptStore(path)  # connections belong to their threads
                barrier.wait()
                results.append(store.claim('o/r', '42', 'a'))
                store.close()

            left = threading.Thread(target=reserve)
            right = threading.Thread(target=reserve)
            left.start()
            right.start()
            left.join()
            right.join()
            self.assertCountEqual(results, ['NEW', 'OUTCOME_UNKNOWN'])

    def test_crash_or_timeout_before_receipt_is_not_auto_retried(self):
        s = ReceiptStore()
        self.assertEqual(s.claim('o/r', '42', 'a'), 'NEW')
        self.assertEqual(s.claim('o/r', '42', 'a'), 'OUTCOME_UNKNOWN')
        s.close()

    def test_thread_scope_preserves_two_independent_receivers(self):
        s = ReceiptStore()
        self.assertEqual(s.claim('o/r', '41', 'same-local-id'), 'NEW')
        self.assertEqual(s.claim('o/r', '42', 'same-local-id'), 'NEW')
        s.close()

    def test_nonfit_older_second_is_not_backfill_by_default(self):
        earlier = '2026-11-03T17:51:01Z'
        self.assertFalse(candidate_window(earlier, self.CURSOR, self.NEXT))

    def test_done_without_pending_receipt_must_not_be_fabricated(self):
        s = ReceiptStore()
        with self.assertRaises(ValueError):
            s.acknowledge_native_delivery('o/r', '42', 'missing')
        s.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--sample', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(BoundaryTests)
        result = unittest.TextTestRunner(verbosity=1).run(suite)
        if not result.wasSuccessful():
            raise SystemExit(1)
        print(f'PASS_{result.testsRun}_LOCAL_BOUNDARY_MODEL_CHECKS; QWEN_INTEGRATION_NOT_RUN')
    elif args.sample:
        cursor, upper = BoundaryTests.CURSOR, BoundaryTests.NEXT
        ledger = ReceiptStore()
        decision = ledger.claim('org/repo', '42', 'boundary-comment')
        ledger.acknowledge_native_delivery('org/repo', '42', 'boundary-comment')
        later = ledger.claim('org/repo', '42', 'boundary-comment')
        ledger.close()
        print(json.dumps({
            'legacy_filter_at_cursor': legacy_window(cursor, cursor, upper),
            'candidate_filter_at_cursor': candidate_window(cursor, cursor, upper),
            'synthetic_first_claim': decision,
            'synthetic_replay_after_confirmed_receipt': later,
            'native_qwen_or_github_test': 'NOT_RUN',
            'caution': 'Pending/ambiguous real writes require native reconciliation',
        }, indent=2))
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
