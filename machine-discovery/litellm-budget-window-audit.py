#!/usr/bin/env python3
"""Offline comparison of matched LiteLLM budget-window spend aggregates.

No network, database, credentials or raw customer logs. The operator must FIRST
aggregate and verify that both figures use the same subject, budget period and
cutoff. A discrepancy is not proof of a specific root cause or fixed release.
"""
import argparse
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
import json
import re
from pathlib import Path
import sys

FIELDS = {"window_start_utc", "window_end_utc", "cutoff_utc",
          "same_subject_window_cutoff", "settled_and_flushed",
          "cap_usd", "spendlogs_total_usd", "window_stored_total_usd"}


class BadInput(ValueError):
    pass


def amount(obj, name):
    raw = obj[name]
    if not isinstance(raw, str) or not re.fullmatch(r"(?:0|[1-9][0-9]{0,11})(?:\.[0-9]{1,6})?", raw):
        raise BadInput(f"{name} must be a quoted nonnegative decimal (at most 12 integer and 6 fractional digits)")
    try:
        value = Decimal(raw)
    except InvalidOperation:
        raise BadInput(f"{name} is not a decimal") from None
    if not value.is_finite() or value < 0:
        raise BadInput(f"{name} must be finite and nonnegative")
    return value


def instant(raw, name):
    if not isinstance(raw, str) or not raw.endswith("Z"):
        raise BadInput(f"{name} must use UTC ISO-8601 ending Z")
    try:
        value = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        raise BadInput(f"{name} is not a valid timestamp") from None
    if value.tzinfo != timezone.utc:
        raise BadInput(f"{name} must use UTC")
    return value


def audit(obj):
    if not isinstance(obj, dict) or set(obj) != FIELDS:
        raise BadInput("expected exactly eight fields; no identifiers or raw logs")
    if not all(type(obj[name]) is bool for name in
               ("same_subject_window_cutoff", "settled_and_flushed")):
        raise BadInput("the two attestation fields must be booleans")
    start = instant(obj["window_start_utc"], "window_start_utc")
    end = instant(obj["window_end_utc"], "window_end_utc")
    cutoff = instant(obj["cutoff_utc"], "cutoff_utc")
    if not start < cutoff <= end:
        raise BadInput("require window_start_utc < cutoff_utc <= window_end_utc")
    cap = amount(obj, "cap_usd")
    logs = amount(obj, "spendlogs_total_usd")
    stored = amount(obj, "window_stored_total_usd")
    if not obj["same_subject_window_cutoff"] or not obj["settled_and_flushed"]:
        return {"status": "INCOMPARABLE_OR_UNSETTLED", "evidence_stage": "INSUFFICIENT",
                "gap_usd": None, "possible_enforcement_gap": None}
    delta = logs - stored
    if delta > 0:
        status = "WINDOW_UNDERCOUNT_IN_SUBMITTED_TOTALS"
    elif delta < 0:
        status = "WINDOW_OVERCOUNT_IN_SUBMITTED_TOTALS"
    else:
        status = "NO_DIFFERENCE_IN_SUBMITTED_TOTALS"
    return {"status": status, "evidence_stage": "OPERATOR_SUPPLIED_AGGREGATES",
            "gap_usd": format(delta, "f"),
            "possible_enforcement_gap": bool(logs > cap and stored < cap),
            "note": "Not proof of a bypass, installed fix, customer retest or root cause"}


def self_test():
    base = dict(window_start_utc="2026-10-26T00:00:00Z",
                window_end_utc="2026-11-02T00:00:00Z",
                cutoff_utc="2026-10-31T00:00:00Z",
                same_subject_window_cutoff=True, settled_and_flushed=True,
                cap_usd="200", spendlogs_total_usd="209.8900",
                window_stored_total_usd="193.8792")
    tests = 0
    def check(changes, expected, gap=None, flag=None):
        nonlocal tests
        obj = dict(base, **changes)
        got = audit(obj)
        assert got["status"] == expected, got
        if gap is not None:
            assert got["gap_usd"] == gap, got
        if flag is not None:
            assert got["possible_enforcement_gap"] is flag, got
        tests += 1
    check({}, "WINDOW_UNDERCOUNT_IN_SUBMITTED_TOTALS", "16.0108", True)
    check({"window_stored_total_usd": "209.8900"},
          "NO_DIFFERENCE_IN_SUBMITTED_TOTALS", "0.0000", False)
    check({"window_stored_total_usd": "210.0000"},
          "WINDOW_OVERCOUNT_IN_SUBMITTED_TOTALS", "-0.1100", False)
    check({"same_subject_window_cutoff": False}, "INCOMPARABLE_OR_UNSETTLED")
    check({"settled_and_flushed": False}, "INCOMPARABLE_OR_UNSETTLED")
    check({"cap_usd": "220"}, "WINDOW_UNDERCOUNT_IN_SUBMITTED_TOTALS", "16.0108", False)
    for changes in ({"cap_usd": "NaN"}, {"cap_usd": "1e1000000"}, {"cap_usd": True},
                    {"spendlogs_total_usd": "-1"},
                    {"cutoff_utc": "2026-11-04T00:00:00Z"},
                    {"same_subject_window_cutoff": "yes"}):
        try:
            audit(dict(base, **changes))
        except BadInput:
            tests += 1
        else:
            raise AssertionError(f"Accepted invalid fixture: {changes}")
    print(f"PASS_{tests}_OFFLINE_TESTS")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    exclusive = parser.add_mutually_exclusive_group(required=True)
    exclusive.add_argument("--audit", type=Path, metavar="MATCHED-AGGREGATES.json")
    exclusive.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    try:
        if args.audit.stat().st_size > 4000:
            raise BadInput("input is too large; only eight aggregate fields are accepted")
        obj = json.loads(args.audit.read_text(encoding="utf-8"))
        result = audit(obj)
    except (BadInput, OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "INVALID_INPUT", "error": str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["status"] == "INCOMPARABLE_OR_UNSETTLED":
        return 3
    return 0 if result["status"] == "NO_DIFFERENCE_IN_SUBMITTED_TOTALS" else 1


if __name__ == "__main__":
    sys.exit(main())
