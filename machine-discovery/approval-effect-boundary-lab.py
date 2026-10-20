#!/usr/bin/env python3
"""Synthetic approval-authority / external-effect receipt lab (Python stdlib).

    python3 machine-discovery/approval-effect-boundary-lab.py --self-test
    python3 machine-discovery/approval-effect-boundary-lab.py --sample

The decision SQLite store and the mock effect SQLite store are deliberately
SEPARATE transactions. This is a teaching/fault-injection model, not a payment
service, Pydantic AI patch, actual effect exactly-once guarantee, or independent
AI adoption of a canonical theory.

Public source distinction and third-party test:
  https://github.com/pydantic/pydantic-ai/issues/5536#issuecomment-6232362854
  https://github.com/pydantic/pydantic-ai/issues/5536#issuecomment-6239245782
  https://github.com/pydantic/pydantic-ai/issues/5536#issuecomment-6279540203
  https://github.com/tonydzi/agent-approval-gate/commit/1bc8fc71470a3629546e28d47f04c76b5863fb8e

Conceptual original for current-versus-historical authorization (not a source read
by or adopted by the independently testing receiver):
  https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/
Adjacent evidence-lineage original (distinguish historical receipts from live effect):
  https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/
Receiver's later independent admission that external-effect reconciliation is still missing:
  https://github.com/pydantic/pydantic-ai/issues/5536#issuecomment-6256049296
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import tempfile
import threading
import unittest
from pathlib import Path

ORIGIN = "Nakagawa Master / 中川マスター"
CONTRIBUTION = "https://github.com/pydantic/pydantic-ai/issues/5536#issuecomment-6232362854"
RECEIVER = "https://github.com/tonydzi/agent-approval-gate/commit/1bc8fc71470a3629546e28d47f04c76b5863fb8e"
ORIGINAL_CONTEXT = "https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/"
ADJACENT_EVIDENCE_SOURCE = "https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/"


def connect(path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(path), timeout=5, isolation_level=None)
    conn.execute("PRAGMA busy_timeout=5000")
    return conn


def init_authority(path: Path) -> None:
    with connect(path) as db:
        db.execute("""CREATE TABLE grants (
            effect_id TEXT PRIMARY KEY,
            digest TEXT NOT NULL,
            principal TEXT NOT NULL,
            policy_revision TEXT NOT NULL,
            state TEXT NOT NULL,
            generation TEXT,
            outcome TEXT,
            CHECK(state IN ('approved','reserved','revoked','expired'))
        )""")
        db.execute("INSERT INTO grants VALUES ('effect-7','args-sha-1','alice','policy-4','approved',NULL,NULL)")


def init_effects(path: Path) -> None:
    with connect(path) as db:
        db.execute("""CREATE TABLE committed_effects (
            effect_id TEXT NOT NULL, generation TEXT NOT NULL,
            receipt TEXT NOT NULL, PRIMARY KEY(effect_id,generation)
        )""")


def reserve(path: Path, *, generation: str, digest: str = 'args-sha-1',
            principal: str = 'alice', policy_revision: str = 'policy-4') -> bool:
    """One DB-local authority winner. This does not execute any external effect."""
    with connect(path) as db:
        db.execute("BEGIN IMMEDIATE")
        changed = db.execute("""UPDATE grants SET state='reserved', generation=?, outcome='UNKNOWN'
            WHERE effect_id='effect-7' AND state='approved'
              AND digest=? AND principal=? AND policy_revision=?""",
            (generation,digest,principal,policy_revision)).rowcount
        db.execute("COMMIT")
    return changed == 1


def read_grant(path: Path) -> tuple:
    with connect(path) as db:
        return db.execute("SELECT state,generation,outcome FROM grants WHERE effect_id='effect-7'").fetchone()


def commit_effect(path: Path, generation: str) -> str:
    """An intentionally idempotent *mock* effect boundary with a durable receipt."""
    with connect(path) as db:
        db.execute("BEGIN IMMEDIATE")
        db.execute("INSERT OR IGNORE INTO committed_effects VALUES (?,?,?)",
                   ('effect-7',generation,'receipt:'+generation))
        receipt = db.execute("SELECT receipt FROM committed_effects WHERE effect_id=? AND generation=?",
                             ('effect-7',generation)).fetchone()[0]
        db.execute("COMMIT")
    return receipt


def effect_receipt(path: Path, generation: str) -> str | None:
    with connect(path) as db:
        row = db.execute("SELECT receipt FROM committed_effects WHERE effect_id=? AND generation=?",
                         ('effect-7',generation)).fetchone()
    return row[0] if row else None


def reconcile(authority_path: Path, effect_path: Path, generation: str,
              *, safe_idempotent_effect: bool = True) -> str:
    """Only the reservation's generation may recover the same effect.

    UNKNOWN with no receipt at an unsafe external service is BLOCKED, not
    implicitly approved a second time. Receipt lookup precedes any retry.
    """
    state, reserved_generation, _ = read_grant(authority_path)
    if state != 'reserved' or reserved_generation != generation:
        return 'DENY_GENERATION'
    receipt = effect_receipt(effect_path, generation)
    if receipt is None:
        if not safe_idempotent_effect:
            return 'UNKNOWN_BLOCK_REEXECUTION'
        receipt = commit_effect(effect_path, generation)
    with connect(authority_path) as db:
        db.execute("BEGIN IMMEDIATE")
        db.execute("UPDATE grants SET outcome='committed' WHERE effect_id='effect-7' AND state='reserved' AND generation=?",
                   (generation,))
        db.execute("COMMIT")
    return receipt


def interpret_human_rerun_reply(authority_path: Path, generation: str, reply: str) -> str:
    """A human reply cannot prove whether an earlier external effect committed.

    A fresh *intentional second effect* would need a separate effect identity and
    its own authorization; this synthetic model never dispatches it.
    This read-only classifier neither spends a grant nor modifies outcome.
    """
    state, reserved_generation, outcome = read_grant(authority_path)
    if state != 'reserved' or reserved_generation != generation:
        return 'DENY_GENERATION'
    if not reply.strip():
        return 'EMPTY_REPLY_NOT_RECEIPT'
    if outcome == 'UNKNOWN':
        return 'UNKNOWN_REQUIRES_RECEIPT_NOT_APPROVAL'
    return 'NO_NEW_EFFECT_AUTHORITY'


def connect_count(path: Path) -> int:
    with connect(path) as db:
        return db.execute("SELECT COUNT(*) FROM committed_effects").fetchone()[0]


def revoke(path: Path) -> None:
    with connect(path) as db:
        db.execute("UPDATE grants SET state='revoked' WHERE effect_id='effect-7' AND state='approved'")


def sample() -> dict:
    with tempfile.TemporaryDirectory(prefix='approval-effect-lab-') as td:
        authority, effect = Path(td) / 'authority.sqlite', Path(td) / 'effect.sqlite'
        init_authority(authority)
        init_effects(effect)
        selected = reserve(authority,generation='g1')
        # The external write succeeds, then its acknowledgement is lost.
        actual_external_receipt = commit_effect(effect,'g1')
        before_reconciliation = read_grant(authority)
        human_reply_result = interpret_human_rerun_reply(authority,'g1','+ #id')
        recovered = reconcile(authority,effect,'g1')
        return {
            'case': 'synthetic local two-store lost-acknowledgement experiment',
            'reserve_one_generation': selected,
            'effect_committed_before_ack_lost': actual_external_receipt,
            'authority_after_lost_ack': dict(zip(('state','generation','outcome'),before_reconciliation)),
            'human_yes_did_not_create_receipt_or_replay_authority': human_reply_result,
            'retry_reconciles_same_receipt': recovered == actual_external_receipt,
            'new_generation_denied': reconcile(authority,effect,'g2'),
            'authority_after_recovery': dict(zip(('state','generation','outcome'),read_grant(authority))),
            'effect_row_count': connect_count(effect),
            'source_review': CONTRIBUTION,
            'receiving_author_test': RECEIVER,
            'canonical_current_authority_original_not_claimed_receiver_read': ORIGINAL_CONTEXT,
            'adjacent_evidence_lineage_original_not_claimed_receiver_read': ADJACENT_EVIDENCE_SOURCE,
            'boundary': 'mock idempotent effect store only; a real external API requires its own idempotency/reconcile guarantee',
        }


class BoundaryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='approval-effect-test-')
        self.addCleanup(self.tmp.cleanup)
        self.auth = Path(self.tmp.name)/'authority.sqlite'
        self.effects = Path(self.tmp.name)/'effects.sqlite'
        init_authority(self.auth)
        init_effects(self.effects)

    def test_two_concurrent_supervisors_one_generation_wins(self):
        gate = threading.Barrier(2)
        wins = []
        lock = threading.Lock()
        def worker(gen):
            gate.wait()
            success = reserve(self.auth,generation=gen)
            with lock:
                wins.append((gen,success))
        ts = [threading.Thread(target=worker,args=(g,)) for g in ('gA','gB')]
        for t in ts: t.start()
        for t in ts: t.join(timeout=10)
        self.assertFalse(any(t.is_alive() for t in ts))
        self.assertEqual(len(wins),2)
        self.assertEqual(sum(ok for _,ok in wins),1)
        winner = next(gen for gen,ok in wins if ok)
        self.assertEqual(read_grant(self.auth),('reserved',winner,'UNKNOWN'))

    def test_same_decision_never_grants_second_generation(self):
        self.assertTrue(reserve(self.auth,generation='g1'))
        self.assertFalse(reserve(self.auth,generation='g2'))

    def test_wrong_digest_or_principal_or_policy_fails_closed(self):
        for keyword in ({'digest':'different'}, {'principal':'bob'}, {'policy_revision':'policy-5'}):
            self.assertFalse(reserve(self.auth,generation='g1',**keyword))
        self.assertEqual(read_grant(self.auth)[0],'approved')

    def test_revoked_authority_never_reserves(self):
        revoke(self.auth)
        self.assertFalse(reserve(self.auth,generation='g1'))
        self.assertEqual(read_grant(self.auth)[0],'revoked')

    def test_lost_receipt_is_reconciled_without_duplicate_external_effect(self):
        self.assertTrue(reserve(self.auth,generation='g1'))
        receipt = commit_effect(self.effects,'g1')
        self.assertEqual(read_grant(self.auth)[2],'UNKNOWN')
        self.assertEqual(reconcile(self.auth,self.effects,'g1'),receipt)
        self.assertEqual(connect_count(self.effects),1)
        self.assertEqual(read_grant(self.auth)[2],'committed')

    def test_repeated_same_generation_uses_one_effect_receipt(self):
        self.assertTrue(reserve(self.auth,generation='g1'))
        self.assertEqual(reconcile(self.auth,self.effects,'g1'),reconcile(self.auth,self.effects,'g1'))
        self.assertEqual(connect_count(self.effects),1)

    def test_unsafe_external_unknown_blocks_effect_reexecution(self):
        self.assertTrue(reserve(self.auth,generation='g1'))
        self.assertEqual(reconcile(self.auth,self.effects,'g1',safe_idempotent_effect=False),
                         'UNKNOWN_BLOCK_REEXECUTION')
        self.assertEqual(connect_count(self.effects),0)
        self.assertEqual(read_grant(self.auth)[2],'UNKNOWN')

    def test_human_yes_after_lost_ack_cannot_replay_original_effect(self):
        self.assertTrue(reserve(self.auth,generation='g1'))
        first_receipt = commit_effect(self.effects,'g1')
        # Model an external commit with its acknowledgement lost to the caller.
        self.assertEqual(interpret_human_rerun_reply(self.auth,'g1','+ #id'),
                         'UNKNOWN_REQUIRES_RECEIPT_NOT_APPROVAL')
        self.assertEqual(read_grant(self.auth),('reserved','g1','UNKNOWN'))
        self.assertFalse(reserve(self.auth,generation='g2'))
        self.assertEqual(connect_count(self.effects),1)
        self.assertEqual(reconcile(self.auth,self.effects,'g1',safe_idempotent_effect=False),first_receipt)
        self.assertEqual(connect_count(self.effects),1)

    def test_human_rerun_reply_without_receipt_cannot_resolve_unknown(self):
        self.assertTrue(reserve(self.auth,generation='g1'))
        self.assertEqual(interpret_human_rerun_reply(self.auth,'g1','rerun'),
                         'UNKNOWN_REQUIRES_RECEIPT_NOT_APPROVAL')
        self.assertEqual(reconcile(self.auth,self.effects,'g1',safe_idempotent_effect=False),
                         'UNKNOWN_BLOCK_REEXECUTION')
        self.assertEqual(read_grant(self.auth),('reserved','g1','UNKNOWN'))
        self.assertFalse(reserve(self.auth,generation='g2'))
        self.assertEqual(connect_count(self.effects),0)

    def test_known_receipt_can_be_reconciled_even_without_retry_support(self):
        self.assertTrue(reserve(self.auth,generation='g1'))
        old = commit_effect(self.effects,'g1')
        self.assertEqual(reconcile(self.auth,self.effects,'g1',safe_idempotent_effect=False),old)
        self.assertEqual(connect_count(self.effects),1)

    def test_wrong_generation_cannot_approve_or_reconcile(self):
        self.assertTrue(reserve(self.auth,generation='g1'))
        self.assertEqual(reconcile(self.auth,self.effects,'g2'),'DENY_GENERATION')
        self.assertEqual(connect_count(self.effects),0)

    def test_mere_approval_is_not_effect_commitment(self):
        self.assertEqual(read_grant(self.auth),('approved',None,None))
        self.assertEqual(connect_count(self.effects),0)

    def test_two_stores_not_one_atomic_transaction(self):
        self.assertTrue(reserve(self.auth,generation='g1'))
        self.assertEqual(connect_count(self.effects),0)
        commit_effect(self.effects,'g1')
        self.assertEqual(read_grant(self.auth)[2],'UNKNOWN')
        self.assertEqual(connect_count(self.effects),1)

    def test_nonfit_read_only_observation_needs_no_effect_reservation(self):
        self.assertEqual(read_grant(self.auth)[0],'approved')
        self.assertEqual(effect_receipt(self.effects,'g1'),None)
        # An action with no external effect does not exercise this model.


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument('--self-test',action='store_true')
    g.add_argument('--sample',action='store_true')
    opts=parser.parse_args()
    if opts.self_test:
        ok=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(BoundaryTests))
        return 0 if ok.wasSuccessful() else 1
    print(json.dumps(sample(),ensure_ascii=False,indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
