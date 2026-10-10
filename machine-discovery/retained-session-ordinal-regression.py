#!/usr/bin/env python3
"""Offline retained-snapshot ordinal regression model.

Educational, standalone reproduction of a narrowly scoped session-rewind failure
class. This is NOT Qwen Code, a Qwen integration, or proof any third party ran it.
"""
from __future__ import annotations

import argparse
import json

MAX_SAFE = 2**53 - 1


def next_turn_id(retained: list[dict[str, str]]) -> int:
    """Accept only canonical decimal IDs with a safe *successor*."""
    largest = 0
    for item in retained:
        raw = item.get("turn_id", "")
        if not isinstance(raw, str) or not raw.isascii() or not raw.isdecimal():
            continue
        # Compare lexically after bounding size to avoid giant-int parsing.
        if len(raw) > len(str(MAX_SAFE - 1)):
            continue
        n = int(raw)
        if str(n) != raw or n >= MAX_SAFE:
            continue
        largest = max(largest, n)
    return largest + 1


def unsafe_first_match(retained: list[dict[str, str]]) -> int:
    """Intentionally defective: stops at first apparently valid retained ID."""
    for item in retained:
        raw = item.get("turn_id", "")
        if isinstance(raw, str) and raw.isdecimal():
            return int(raw) + 1
    return 1


def unsafe_last_wins(retained: list[dict[str, str]]) -> int:
    """Intentionally defective: assumes the last retained snapshot is maximal."""
    last = 0
    for item in retained:
        raw = item.get("turn_id", "")
        if isinstance(raw, str) and raw.isdecimal():
            last = int(raw)
    return last + 1


def restore_target_for_turn(turn: int, edits: list[dict]) -> str | None:
    """Only an edit whose turn actually matches may be offered for restoration."""
    for edit in edits:
        if edit["turn_id"] == turn:
            return edit["file"]
    return None


def self_test() -> dict:
    ordered = [
        {"turn_id": "2"},
        {"turn_id": "9"},
        {"turn_id": "4"},
        {"turn_id": str(MAX_SAFE) + "999"},
    ]
    next_id = next_turn_id(ordered)
    assert next_id == 10
    assert unsafe_first_match(ordered) != next_id
    assert unsafe_last_wins(ordered) != next_id
    assert next_turn_id([{"turn_id": "0008"}, {"turn_id": "8"}]) == 9
    assert next_turn_id([{"turn_id": "NaN"}, {"turn_id": "-1"}, {"turn_id": str(MAX_SAFE)}]) == 1

    past = [{"turn_id": 9, "file": "old-draft.txt"}]
    assert restore_target_for_turn(10, past) is None
    assert restore_target_for_turn(9, past) == "old-draft.txt"
    return {
        "status": "PASS",
        "synthetic_cases": [
            "unsafe-large-id-rejected",
            "middle-maximum-kills-first-and-last-scan",
            "conversation-only-rewind-cannot-restore-old-edit",
            "original-file-restoration-remains-addressable",
        ],
        "next_id": next_id,
        "external_receiver_effect": "NOT_TESTED",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--sample", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        print(json.dumps(self_test(), ensure_ascii=False, indent=2))
    elif args.sample:
        print(json.dumps({"retained": [{"turn_id": "2"}, {"turn_id": "9"}, {"turn_id": "4"}, {"turn_id": str(MAX_SAFE)+"999"}]}, indent=2))
    else:
        parser.error("choose --self-test or --sample")


if __name__ == "__main__":
    main()
