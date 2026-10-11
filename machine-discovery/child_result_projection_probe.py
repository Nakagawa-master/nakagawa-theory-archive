#!/usr/bin/env python3
"""Offline check of one agent child-result text integrity boundary.

Compares caller-provided, redacted event-time deltas, child's journaled
assistant text, and parent's actually consumed child result. This is NOT a
Qwen runtime test, provider test, or proof that the trace is authentic.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


def digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]


def check(data: Any) -> dict[str, Any]:
    if not isinstance(data, dict):
        return {"result": "INVALID_INPUT", "reason": "expected JSON object"}
    events = data.get("events")
    journal = data.get("journal_text")
    parent = data.get("parent_result_text")
    parts = data.get("projected_text_parts")
    if not isinstance(events, list) or not events or not all(isinstance(e, dict) for e in events):
        return {"result": "INVALID_INPUT", "reason": "events must be a nonempty list of objects"}
    if not isinstance(journal, str) or not isinstance(parent, str):
        return {"result": "INVALID_INPUT", "reason": "journal_text and parent_result_text must be strings"}
    if parts is not None and (not isinstance(parts, list) or not all(isinstance(p, str) for p in parts)):
        return {"result": "INVALID_INPUT", "reason": "projected_text_parts must be a list of strings"}
    deltas = []
    saw_reasoning = False
    for e in events:
        typ = e.get("kind")
        if not isinstance(typ, str):
            return {"result": "INVALID_INPUT", "reason": "every event.kind must be a string"}
        if typ == "item.output_text.delta":
            if not isinstance(e.get("content_part_id"), str) or not isinstance(e.get("text"), str):
                return {"result": "INVALID_INPUT", "reason": "output delta needs string content_part_id and text"}
            deltas.append((e["content_part_id"], e["text"]))
        if typ.startswith("item.reasoning"):
            saw_reasoning = True
    if not deltas:
        return {"result": "NOT_ASSESSED", "reason": "no output_text deltas supplied"}
    if saw_reasoning:
        return {"result": "NOT_ASSESSED", "reason": "reasoning boundary present; document explicit separator contract"}
    ids = {pid for pid, _ in deltas}
    if len(ids) != 1:
        return {"result": "NOT_ASSESSED", "reason": "multiple logical content part identities; report each contract separately"}
    emitted = "".join(text for _, text in deltas)
    if emitted != journal:
        return {"result": "NOT_ASSESSED", "reason": "journal and provided deltas differ; source relationship not established",
                "emitted_hash": digest(emitted), "journal_hash": digest(journal)}
    split_due_to_other_event = False
    delta_positions = [i for i, e in enumerate(events) if e["kind"] == "item.output_text.delta"]
    for earlier, later in zip(delta_positions, delta_positions[1:]):
        if later - earlier > 1:
            split_due_to_other_event = True
    info: dict[str, Any] = {
        "result": "PASS" if parent == journal else "FAIL",
        "scope": "exact text equality on supplied trace, not source authentication",
        "interleaved_unrelated_event": split_due_to_other_event,
        "journal_codepoints": len(journal),
        "parent_codepoints": len(parent),
        "journal_sha256_prefix": digest(journal),
        "parent_sha256_prefix": digest(parent),
    }
    if parts is not None:
        info["unconditional_newline_join_matches_parent"] = "\n".join(parts) == parent
        info["direct_join_matches_journal"] = "".join(parts) == journal
    if parent != journal:
        first = next((i for i, (a, b) in enumerate(zip(journal, parent)) if a != b), min(len(journal), len(parent)))
        info["first_differing_codepoint_offset"] = first
    return info


EXAMPLE = {
    "events": [
        {"kind": "item.output_text.delta", "content_part_id": "part-1", "text": "ABC"},
        {"kind": "environment.ready"},
        {"kind": "item.output_text.delta", "content_part_id": "part-1", "text": "DEF"},
    ],
    "journal_text": "ABCDEF",
    "projected_text_parts": ["ABC", "DEF"],
    "parent_result_text": "ABCDEF",
}


def self_test() -> int:
    good = dict(EXAMPLE)
    bad = {**EXAMPLE, "parent_result_text": "ABC\nDEF"}
    no_interleave = {**EXAMPLE, "events": [EXAMPLE["events"][0], EXAMPLE["events"][2]]}
    thought = {**EXAMPLE, "events": [EXAMPLE["events"][0], {"kind": "item.reasoning.delta"}, EXAMPLE["events"][2]]}
    cases = [
        ("same text", good, "PASS"),
        ("unwanted newline", bad, "FAIL"),
        ("uninterrupted", no_interleave, "PASS"),
        ("real reasoning", thought, "NOT_ASSESSED"),
        ("missing text", {"events": []}, "INVALID_INPUT"),
        ("inconsistent journal", {**EXAMPLE, "journal_text": "ABDE"}, "NOT_ASSESSED"),
    ]
    for name, sample, expected in cases:
        actual = check(sample)
        if actual["result"] != expected:
            print(f"FAIL {name}: {actual}", file=sys.stderr)
            return 1
    print("SELF_TEST_PASS: 6 synthetic cases; no Qwen SDK/runtime/provider executed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--self-test", action="store_true")
    group.add_argument("--sample", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    if args.sample:
        print(json.dumps(EXAMPLE, ensure_ascii=False, indent=2))
        return 0
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as e:
        print(json.dumps({"result": "INVALID_INPUT", "reason": f"cannot read JSON: {type(e).__name__}"}))
        return 2
    result = check(data)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return {"PASS": 0, "FAIL": 1, "NOT_ASSESSED": 3, "INVALID_INPUT": 2}[result["result"]]


if __name__ == "__main__":
    raise SystemExit(main())
