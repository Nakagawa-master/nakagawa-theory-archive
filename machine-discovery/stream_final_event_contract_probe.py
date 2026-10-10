#!/usr/bin/env python3
"""Offline evidence checker for an AI agent's FINAL streamed tool-call contract.

All inputs are provided by the operator; this tool neither connects to an LLM nor
proves that the trace is authentic. Run on synthetic or redacted observations.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

EXAMPLE = {
    "case": "synthetic-two-tools-one-committed",
    "outcome": "completed",
    "events": [
        {"stage": "provisional", "tool_calls": ["A", "B"]},
        {"stage": "committed", "tool_calls": ["A"]},
    ],
    "final_response_tool_calls": ["A"],
    "executed_tool_calls": ["A"],
}


def tool_ids(value: object, field: str) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(v, str) or not v.strip() for v in value):
        raise ValueError(f"{field} must be a list of nonempty tool-call identifiers")
    if len(set(value)) != len(value):
        raise ValueError(f"{field} must identify distinct call occurrences (use distinct IDs)")
    return value


def check(trace: object) -> dict[str, object]:
    if not isinstance(trace, dict):
        raise ValueError("trace must be a JSON object")
    outcome = trace.get("outcome")
    if outcome not in ("completed", "validation_error", "early_stopped"):
        raise ValueError("outcome must be completed, validation_error or early_stopped")
    events = trace.get("events")
    if not isinstance(events, list):
        raise ValueError("events must be a list")
    committed = []
    for i, event in enumerate(events):
        if not isinstance(event, dict) or event.get("stage") not in ("provisional", "committed"):
            raise ValueError(f"events[{i}] must have stage provisional or committed")
        ids = tool_ids(event.get("tool_calls"), f"events[{i}].tool_calls")
        if event["stage"] == "committed":
            committed.append((i, ids))
    if len(committed) > 1:
        return {"result": "FAIL", "reason": "Multiple committed final events: check final-event ownership"}
    if committed and committed[0][0] != len(events) - 1:
        return {"result": "FAIL", "reason": "A provisional event follows the committed final event"}
    final = tool_ids(trace.get("final_response_tool_calls"), "final_response_tool_calls")
    executed = tool_ids(trace.get("executed_tool_calls"), "executed_tool_calls")
    if outcome == "early_stopped":
        if committed:
            return {"result": "FAIL", "reason": "An early-stopped stream was presented as a committed final event"}
        return {"result": "NOT_ASSESSED", "reason": "Partial stream: final validation and upstream close/aclose require separate evidence"}
    if outcome == "validation_error":
        if committed:
            return {"result": "FAIL", "reason": "A rejected final response was already emitted as a committed event"}
        if executed:
            return {"result": "FAIL", "reason": "Tool execution occurred despite final validation error"}
        return {"result": "PASS", "reason": "No committed event or execution after validation error (trace claim only)"}
    if not committed:
        return {"result": "FAIL", "reason": "Completed run lacks a captured committed final event"}
    emitted = committed[0][1]
    if emitted != final or final != executed:
        return {"result": "FAIL", "reason": "Event-time committed calls, validated final response and execution differ", "committed": emitted, "final": final, "executed": executed}
    return {"result": "PASS", "reason": "Committed event agrees with validated final response and next-step executed calls (trace claim only)", "calls": emitted}


def self_test() -> None:
    def run(outcome: str, events: list[dict], final: list[str], executed: list[str]) -> str:
        return str(check({"outcome": outcome, "events": events, "final_response_tool_calls": final, "executed_tool_calls": executed})["result"])
    provisional = {"stage": "provisional", "tool_calls": ["A", "B"]}
    good = {"stage": "committed", "tool_calls": ["A"]}
    bad = {"stage": "committed", "tool_calls": ["A", "B"]}
    assert run("completed", [provisional, good], ["A"], ["A"]) == "PASS"
    assert run("completed", [provisional, bad], ["A"], ["A"]) == "FAIL"
    assert run("completed", [provisional, good], ["A"], ["A", "B"]) == "FAIL"
    assert run("completed", [provisional], ["A"], ["A"]) == "FAIL"
    assert run("validation_error", [provisional], [], []) == "PASS"
    assert run("validation_error", [bad], [], []) == "FAIL"
    assert run("validation_error", [provisional], [], ["A"]) == "FAIL"
    assert run("early_stopped", [provisional], [], []) == "NOT_ASSESSED"
    assert run("early_stopped", [good], ["A"], []) == "FAIL"
    try:
        check({"outcome": "completed", "events": [good], "final_response_tool_calls": ["A", "A"], "executed_tool_calls": ["A"]})
    except ValueError:
        pass
    else:
        raise AssertionError("Duplicate call IDs must be rejected")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("trace", nargs="?", type=Path, help="JSON trace captured at actual event emission and next-step execution")
    p.add_argument("--sample", action="store_true", help="Print a synthetic example JSON trace")
    p.add_argument("--self-test", action="store_true", help="Run deterministic positive/negative and malformed-case checks")
    args = p.parse_args()
    if args.self_test:
        self_test()
        print("Self-test PASS: 10 bounded contracts")
        return 0
    if args.sample:
        print(json.dumps(EXAMPLE, ensure_ascii=False, indent=2))
        return 0
    if args.trace is None:
        p.error("pass a JSON trace, --sample, or --self-test")
    try:
        result = check(json.loads(args.trace.read_text(encoding="utf-8")))
    except (OSError, ValueError, json.JSONDecodeError) as e:
        print(json.dumps({"result": "INVALID_INPUT", "reason": str(e)}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False))
    return {"PASS": 0, "FAIL": 1, "NOT_ASSESSED": 3}[str(result["result"])]


if __name__ == "__main__":
    raise SystemExit(main())
