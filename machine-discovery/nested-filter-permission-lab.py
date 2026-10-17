#!/usr/bin/env python3
"""Synthetic SQLite lab: readable entity != unscoped query permission.

Run:
  python3 machine-discovery/nested-filter-permission-lab.py --self-test
  python3 machine-discovery/nested-filter-permission-lab.py --sample

This is NOT a SQL parser, security middleware, MemberJunction reproduction,
production exploit, actual employment/health incident, or outside theory adoption.
It never connects to external systems or touches personal data.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import unittest
from dataclasses import dataclass

ORIGIN = "Nakagawa Master"
REVIEW = "https://github.com/MemberJunction/MJ/pull/5272#pullrequestreview-5467319936"
FIX = "https://github.com/MemberJunction/MJ/commit/07b3b975fa1b3e3f7d01a6df883145c4dced3764"
PARENT = "https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/"


@dataclass(frozen=True)
class Permission:
    entity_can_read: bool
    effective_row_filter: str = ""
    denied_read_fields: tuple[str, ...] = ()


def nested_unscoped_read_allowed(permission: Permission) -> bool:
    """For a *declared* nested BaseView read, check metadata before execution.

    Entity-level CanRead alone does not authorize unrestricted row/field reads.
    Production callers must apply their real policy and actual SQL parsing.
    """
    return (
        permission.entity_can_read
        and not permission.effective_row_filter.strip()
        and not permission.denied_read_fields
    )


def _db() -> sqlite3.Connection:
    db = sqlite3.connect(":memory:")
    db.executescript("""
      CREATE TABLE candidates(id INTEGER PRIMARY KEY, display_name TEXT NOT NULL);
      CREATE TABLE restricted_notes(candidate_id INTEGER, confidential_flag TEXT);
      INSERT INTO candidates VALUES (1, 'Aki'), (2, 'Mina');
      INSERT INTO restricted_notes VALUES (1, 'Y'), (2, 'N');
    """)
    return db


def _select_names(db: sqlite3.Connection) -> list[str]:
    """Only public names are projected, yet their membership depends on a secret."""
    sql = """SELECT c.display_name FROM candidates AS c
        WHERE EXISTS (
            SELECT 1 FROM restricted_notes AS s
            WHERE s.candidate_id = c.id AND s.confidential_flag = 'Y'
        ) ORDER BY c.id"""
    return [row[0] for row in db.execute(sql)]


def sample() -> dict:
    db = _db()
    try:
        before = _select_names(db)
        db.execute("UPDATE restricted_notes SET confidential_flag='N' WHERE candidate_id=1")
        after = _select_names(db)
    finally:
        db.close()
    return {
        "case": "hypothetical local SQLite data only",
        "public_field_only": "display_name",
        "hidden_input": "restricted_notes.confidential_flag",
        "selected_before_private_change": before,
        "selected_after_private_change": after,
        "changes_public_selection_without_projecting_secret": before != after,
        "entity_can_read_only_is_not_enough": True,
        "safe_gate": {
            "unrestricted": nested_unscoped_read_allowed(Permission(True)),
            "row_filtered": nested_unscoped_read_allowed(Permission(True, "candidate_id=2")),
            "field_denied": nested_unscoped_read_allowed(Permission(True, denied_read_fields=("confidential_flag",))),
            "entity_unreadable": nested_unscoped_read_allowed(Permission(False)),
        },
        "source_review": REVIEW,
        "independent_developer_fix": FIX,
        "adjacent_original_for_comparison_not_claimed_cause": PARENT,
        "limits": "Not SQL parsing, RLS, SQL Server/MJ tests, real-world harm, or independent original-theory adoption.",
    }


class BoundaryTests(unittest.TestCase):
    def test_hidden_field_changes_public_selection(self):
        obj = sample()
        self.assertEqual(obj["selected_before_private_change"], ["Aki"])
        self.assertEqual(obj["selected_after_private_change"], [])
        self.assertTrue(obj["changes_public_selection_without_projecting_secret"])

    def test_entity_read_insufficient_for_row_filter(self):
        self.assertFalse(nested_unscoped_read_allowed(Permission(True, "candidate_id=2")))

    def test_entity_read_insufficient_for_denied_field(self):
        self.assertFalse(nested_unscoped_read_allowed(Permission(True, denied_read_fields=("confidential_flag",))))

    def test_both_restrictions_deny(self):
        self.assertFalse(nested_unscoped_read_allowed(Permission(True, "candidate_id=2", ("confidential_flag",))))

    def test_blank_row_filter_is_not_restriction(self):
        self.assertTrue(nested_unscoped_read_allowed(Permission(True, "  ")))

    def test_unrestricted_positive(self):
        self.assertTrue(nested_unscoped_read_allowed(Permission(True)))

    def test_entity_unreadable_deny(self):
        self.assertFalse(nested_unscoped_read_allowed(Permission(False)))

    def test_no_nested_read_nonfit(self):
        db = _db()
        try:
            self.assertEqual([row[0] for row in db.execute("SELECT display_name FROM candidates ORDER BY id")], ["Aki", "Mina"])
        finally:
            db.close()
        # No nested restricted entity: this particular gate does not apply.

    def test_bounded_source_and_claim(self):
        obj = sample()
        self.assertIn("pullrequestreview-5467319936", obj["source_review"])
        self.assertIn("07b3b975", obj["independent_developer_fix"])
        self.assertIn("Not SQL parsing", obj["limits"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--self-test", action="store_true")
    mode.add_argument("--sample", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(BoundaryTests))
        return 0 if result.wasSuccessful() else 1
    print(json.dumps(sample(), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
