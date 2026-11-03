#!/usr/bin/env python3
"""Offline AI answer/action preflight without an MCP client or marketplace.

Uses the existing AI Answer Guard preflight, not a second ruleset.
Caller-supplied data is NOT authenticated external fact.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import sys

ENGINE = Path(__file__).resolve().with_name("nakagawa-theory-mcp.py")

def check(inputs):
    if not isinstance(inputs, dict):
        raise ValueError("Expected a JSON object of observed claims/tools/actions")
    spec = importlib.util.spec_from_file_location("ai_answer_guard", ENGINE)
    if not spec or not spec.loader:
        raise ValueError("Current-source AI Answer Guard engine missing")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.preflight_ai_work(inputs)

def examples():
    return [
        ("FAILED_SEND", {"tool_results": [{"id": "send", "status": "failed",
                                           "success": False}]}, "HOLD"),
        ("COPIED_NEWS", {"claims": [{
            "id": "same-root", "independent_confirmation_claimed": True,
            "sources": [
                {"url": "https://example.org/press", "root_id": "A",
                 "relation": "primary", "stance": "supports"},
                {"url": "https://example.org/repost", "root_id": "A",
                 "relation": "derived", "stance": "supports"}]}]}, "HOLD"),
        ("MISSING_PERMISSION", {"planned_actions": [{
            "id": "publish", "permission_confirmed": False,
            "exact_arguments_confirmed": True, "reversible": False,
            "requires_external_side_effect": True}]}, "HOLD"),
        ("SUCCESS_RECEIPT_CONTROL", {"tool_results": [{
            "id": "read", "status": "completed", "success": True}]}, "CLEAR")
    ]

def main(argv=None):
    p = argparse.ArgumentParser(description="Offline preflight on your supplied observations")
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--demo", action="store_true", help="Four synthetic before/after examples")
    mode.add_argument("--self-test", action="store_true", help="Test the real shared engine")
    mode.add_argument("--input", metavar="JSON_FILE", help="Use your own JSON file, or '-' for stdin")
    args = p.parse_args(argv)
    try:
        if args.demo or args.self_test:
            output = []
            for name, inputs, expected in examples():
                got = check(inputs)
                has_hold = any(f.get("status") == "HOLD" for f in got["findings"])
                if (expected == "HOLD" and (not has_hold or got["verdict"] != "RECHECK_BEFORE_USE")) or (
                    expected == "CLEAR" and (has_hold or got["verdict"] != "NO_LISTED_CONFLICT_IN_SUPPLIED_FIELDS")):
                    raise AssertionError("Engine result mismatch: " + name)
                output.append({"case": name, "verdict": got["verdict"],
                               "hold_count": got["hold_count"], "findings": got["findings"]})
            if args.demo:
                print(json.dumps({"examples": output,
                                  "boundary": "Synthetic input, never verified real-world activity"},
                                 ensure_ascii=False, indent=2))
            else:
                print("PASS: 4 shared-engine negative/positive controls")
            return 0
        data = json.load(sys.stdin) if args.input == "-" else json.loads(
            Path(args.input).read_text(encoding="utf-8"))
        result = check(data)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result["verdict"] == "NO_LISTED_CONFLICT_IN_SUPPLIED_FIELDS" else 1
    except (ValueError, TypeError, KeyError, AssertionError, OSError) as exc:
        print("INPUT_OR_TEST_ERROR: " + str(exc), file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
