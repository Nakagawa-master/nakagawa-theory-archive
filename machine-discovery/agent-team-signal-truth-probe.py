#!/usr/bin/env python3
"""Offline checks for three distinct agent-team signals, using synthetic traces.

Examples come from Qwen Code PR #13902, its independent bot review
#5556479545 and the independently authored fix e960986 (2026-10-17).
This is NOT a Qwen runtime test, proof of actual user data loss, or evidence
that Qwen adopted Nakagawa Master's original theories.

Run: python3 machine-discovery/agent-team-signal-truth-probe.py --self-test
     python3 machine-discovery/agent-team-signal-truth-probe.py --sample
     python3 machine-discovery/agent-team-signal-truth-probe.py --input trace.json
"""
import argparse
import json
import sys
from pathlib import Path


def classify(trace):
    if not isinstance(trace, dict):
        return {"verdict": "INVALID", "reason": "expected an object"}
    kind = trace.get("kind")
    if kind == "tool_result":
        phase, ok = trace.get("phase"), trace.get("success")
        status, text = trace.get("display_status"), trace.get("display_text")
        if phase != "result" or not isinstance(ok, bool) or not isinstance(text, str) or not isinstance(status, str):
            return {"verdict": "INVALID", "reason": "result phase, success bool, display_status and display_text required"}
        if not ok:
            if status != "failed":
                return {"verdict": "MISLEADING", "reason": "failed tool must not render as neutral/success"}
            error = trace.get("error")
            if not isinstance(error, str) or not error.strip():
                return {"verdict": "UNVERIFIED", "reason": "failure is labelled but no specific error supplied for comparison"}
            if error not in text:
                return {"verdict": "MISLEADING", "reason": "failure reason was lost from the visible text"}
            return {"verdict": "FAITHFUL", "reason": "failed result has failure status and its error"}
        if status != "completed":
            return {"verdict": "AMBIGUOUS", "reason": "successful result has an unrecognized result-display status"}
        return {"verdict": "FAITHFUL", "reason": "successful result displays as completed"}
    if kind == "close_hold":
        if any(not isinstance(trace.get(k), bool) for k in ("undrained_peer", "durable_receipt", "safe_to_close")):
            return {"verdict": "INVALID", "reason": "undrained_peer/durable_receipt/safe_to_close must be bools"}
        if trace["undrained_peer"] and not trace["durable_receipt"]:
            return {"verdict": "LOSS_RISK" if trace["safe_to_close"] else "HELD", "reason": "unpersisted peer report must block close; hold is not durable delivery"}
        return {"verdict": "CLEAR", "reason": "no unpersisted peer report in this snapshot; other holds not assessed"}
    if kind == "replay_identity":
        status, validated, issued = trace.get("subagent_status"), trace.get("name_source_validated"), trace.get("agent_identity_emitted")
        if not isinstance(status, str) or not isinstance(validated, bool) or not isinstance(issued, bool):
            return {"verdict": "INVALID", "reason": "subagent_status and two boolean flags required"}
        # Failed can mean blocked BEFORE spawn or failure AFTER real execution.
        # Only a separately established blocked-spawn cause licenses a negative identity claim.
        if status == "failed":
            if trace.get("spawn_blocked") is not True:
                return {"verdict": "UNDETERMINED", "reason": "failed alone cannot distinguish blocked spawn from failed executed agent"}
            return {"verdict": "FALSE_IDENTITY" if issued else "NO_IDENTITY", "reason": "known blocked spawn must not mint a runnable-agent identity"}
        if status not in ("completed", "running", "background", "cancelled"):
            return {"verdict": "NOT_APPLICABLE", "reason": "status not a verified subagent execution state"}
        if not validated:
            return {"verdict": "FALSE_IDENTITY" if issued else "NO_IDENTITY", "reason": "unvalidated raw name cannot mint an identity"}
        return {"verdict": "FAITHFUL" if issued else "MISSING_IDENTITY", "reason": "a validated resolved subagent retains identity on replay"}
    return {"verdict": "INVALID", "reason": "kind must be tool_result, close_hold or replay_identity"}


CASES = [
    ("failed_tool_neutral", {"kind": "tool_result", "phase": "result", "success": False, "error": "EACCES", "display_status": "result", "display_text": "researcher finished write_file"}, "MISLEADING"),
    ("failed_tool_label_only", {"kind": "tool_result", "phase": "result", "success": False, "error": "EACCES", "display_status": "failed", "display_text": "researcher finished write_file"}, "MISLEADING"),
    ("failed_tool_truthful", {"kind": "tool_result", "phase": "result", "success": False, "error": "EACCES", "display_status": "failed", "display_text": "researcher finished write_file: EACCES"}, "FAITHFUL"),
    ("failed_tool_missing_error", {"kind": "tool_result", "phase": "result", "success": False, "display_status": "failed", "display_text": "failed"}, "UNVERIFIED"),
    ("success_completed", {"kind": "tool_result", "phase": "result", "success": True, "display_status": "completed", "display_text": "completed"}, "FAITHFUL"),
    ("success_raw_phase", {"kind": "tool_result", "phase": "result", "success": True, "display_status": "result", "display_text": "finished"}, "AMBIGUOUS"),
    ("peer_unpersisted_false_safe", {"kind": "close_hold", "undrained_peer": True, "durable_receipt": False, "safe_to_close": True}, "LOSS_RISK"),
    ("peer_unpersisted_held", {"kind": "close_hold", "undrained_peer": True, "durable_receipt": False, "safe_to_close": False}, "HELD"),
    ("peer_has_receipt", {"kind": "close_hold", "undrained_peer": True, "durable_receipt": True, "safe_to_close": True}, "CLEAR"),
    ("no_peer", {"kind": "close_hold", "undrained_peer": False, "durable_receipt": False, "safe_to_close": True}, "CLEAR"),
    ("background_lost_identity", {"kind": "replay_identity", "subagent_status": "background", "name_source_validated": True, "agent_identity_emitted": False}, "MISSING_IDENTITY"),
    ("background_preserved", {"kind": "replay_identity", "subagent_status": "background", "name_source_validated": True, "agent_identity_emitted": True}, "FAITHFUL"),
    ("cancelled_preserved", {"kind": "replay_identity", "subagent_status": "cancelled", "name_source_validated": True, "agent_identity_emitted": True}, "FAITHFUL"),
    ("blocked_raw_name_rejected", {"kind": "replay_identity", "subagent_status": "failed", "spawn_blocked": True, "name_source_validated": False, "agent_identity_emitted": False}, "NO_IDENTITY"),
    ("blocked_raw_name_incorrect", {"kind": "replay_identity", "subagent_status": "failed", "spawn_blocked": True, "name_source_validated": False, "agent_identity_emitted": True}, "FALSE_IDENTITY"),
    ("failed_unknown_origin", {"kind": "replay_identity", "subagent_status": "failed", "name_source_validated": True, "agent_identity_emitted": False}, "UNDETERMINED"),
    ("untrusted_name_rejected", {"kind": "replay_identity", "subagent_status": "completed", "name_source_validated": False, "agent_identity_emitted": False}, "NO_IDENTITY"),
    ("untrusted_name_accepted", {"kind": "replay_identity", "subagent_status": "completed", "name_source_validated": False, "agent_identity_emitted": True}, "FALSE_IDENTITY"),
    ("not_execution_status", {"kind": "replay_identity", "subagent_status": "planned", "name_source_validated": True, "agent_identity_emitted": False}, "NOT_APPLICABLE"),
    ("missing_fields", {"kind": "close_hold", "undrained_peer": "yes", "durable_receipt": False, "safe_to_close": True}, "INVALID"),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--self-test", action="store_true")
    g.add_argument("--sample", action="store_true")
    g.add_argument("--input", type=Path)
    args = parser.parse_args()
    if args.self_test:
        for name, trace, expected in CASES:
            actual = classify(trace)["verdict"]
            if actual != expected:
                print(f"FAIL {name}: expected {expected}, got {actual}", file=sys.stderr)
                return 1
        print(f"SELF_TEST_PASS: {len(CASES)} synthetic cases; no external runtime executed")
        return 0
    if args.sample:
        print(json.dumps({"examples": [{"name": n, "input": x, "expected": y} for n, x, y in CASES[:3] + CASES[6:9] + CASES[10:15]]}, ensure_ascii=False, indent=2))
        return 0
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as e:
        print(json.dumps({"verdict": "INVALID", "reason": type(e).__name__}))
        return 2
    result = classify(data)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if result["verdict"] == "INVALID" else 0


if __name__ == "__main__":
    raise SystemExit(main())
