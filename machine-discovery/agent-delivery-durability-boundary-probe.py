#!/usr/bin/env python3
"""Offline one-message AI-agent delivery boundary; no network or service writes.

This is a source-inspired *synthetic* interleaving model, not a Qwen Code test,
a demonstrated production loss, or independent original-theory adoption.
Run: python3 machine-discovery/agent-delivery-durability-boundary-probe.py --self-test
     python3 machine-discovery/agent-delivery-durability-boundary-probe.py --sample
     python3 machine-discovery/agent-delivery-durability-boundary-probe.py --input trace.json
Events: mailbox_mark_read, volatile_enqueue, append_requested, record_durable,
recorder_close, queue_discard, consumer_delivered. An append request or UI event
is NOT durable delivery; record_durable requires an independently observed
committed, rereadable receipt. A real system may use another persistence path.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

EVENTS = frozenset(("mailbox_mark_read", "volatile_enqueue", "append_requested",
                    "record_durable", "recorder_close", "queue_discard",
                    "consumer_delivered"))

def classify(trace: object) -> dict:
    if not isinstance(trace, dict) or trace.get("case_type") not in (None, "one_agent_message"):
        return {"verdict": "INVALID", "reason": "one_agent_message object required"}
    events = trace.get("events")
    if not isinstance(events, list) or not events or any(not isinstance(e, str) or e not in EVENTS for e in events):
        return {"verdict": "INVALID", "reason": "nonempty list of known event strings required"}
    if len(events) != len(set(events)):
        return {"verdict": "INVALID", "reason": "one-message trace cannot repeat lifecycle events"}
    pos = {e: i for i, e in enumerate(events)}
    at = lambda e: pos.get(e, 10**9)
    mark = "mailbox_mark_read" in pos
    durable = "record_durable" in pos
    delivered = "consumer_delivered" in pos
    discarded = "queue_discard" in pos
    closed = "recorder_close" in pos
    if durable and "append_requested" not in pos:
        return {"verdict": "INVALID", "reason": "durable receipt without append request provenance"}
    if durable and at("record_durable") < at("append_requested"):
        return {"verdict": "INVALID", "reason": "durable receipt preceded append request"}
    if durable and at("recorder_close") < at("record_durable"):
        return {"verdict": "INVALID", "reason": "post-close receipt needs a documented reopening contract"}
    if delivered and (not durable or at("consumer_delivered") < at("record_durable")):
        return {"verdict": "INVALID", "reason": "claimed delivery needs earlier independently proven durable evidence in this model"}
    if not mark:
        return {"verdict": "NOT_APPLICABLE", "reason": "mailbox was not acknowledged read"}
    if durable and (not discarded or at("record_durable") < at("queue_discard")):
        if at("mailbox_mark_read") < at("record_durable"):
            return {"verdict": "RECOVERED_BUT_EARLIER_CRASH_WINDOW",
                    "reason": "durable copy exists now, but a crash after mark-read and before receipt could lose it",
                    "delivered": delivered}
        return {"verdict": "SAFE_AT_CHECKPOINT", "reason": "receipt committed before mark-read and volatile discard", "delivered": delivered}
    if discarded:
        cause = ("recorder closed before attempted rescue" if closed and
                 at("recorder_close") < at("queue_discard") and
                 at("recorder_close") < at("record_durable")
                 else "volatile copy discarded before proven durable receipt")
        return {"verdict": "LOSS_WINDOW", "reason": cause, "proven_delivery": delivered}
    if closed and not durable:
        return {"verdict": "UNRESOLVED_AFTER_CLOSE", "reason": "marked read, recorder closed, durable receipt absent"}
    return {"verdict": "NOT_ESTABLISHED", "reason": "no observed durable handoff or discard yet"}

CASES = [
    ("close_before_rescue", ["mailbox_mark_read", "volatile_enqueue", "recorder_close", "append_requested", "queue_discard"], "LOSS_WINDOW"),
    ("fire_and_forget_append", ["mailbox_mark_read", "volatile_enqueue", "append_requested", "queue_discard"], "LOSS_WINDOW"),
    ("mark_read_then_overflow", ["mailbox_mark_read", "queue_discard"], "LOSS_WINDOW"),
    ("durable_before_close", ["append_requested", "record_durable", "mailbox_mark_read", "recorder_close", "queue_discard"], "SAFE_AT_CHECKPOINT"),
    ("durable_after_mark_before_close", ["mailbox_mark_read", "volatile_enqueue", "append_requested", "record_durable", "recorder_close", "queue_discard", "consumer_delivered"], "RECOVERED_BUT_EARLIER_CRASH_WINDOW"),
    ("close_without_discard", ["mailbox_mark_read", "recorder_close"], "UNRESOLVED_AFTER_CLOSE"),
    ("not_yet_completed", ["mailbox_mark_read", "volatile_enqueue"], "NOT_ESTABLISHED"),
    ("unread_mailbox", ["volatile_enqueue", "queue_discard"], "NOT_APPLICABLE"),
    ("not_proven_after_close", ["mailbox_mark_read", "append_requested", "recorder_close", "record_durable"], "INVALID"),
    ("unproven_consumption", ["mailbox_mark_read", "consumer_delivered"], "INVALID"),
]

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--self-test", action="store_true")
    g.add_argument("--sample", action="store_true")
    g.add_argument("--json", action="store_true")
    g.add_argument("--input", type=Path)
    args = p.parse_args()
    if args.self_test:
        for name, events, expected in CASES:
            got = classify({"case_type": "one_agent_message", "events": events})
            if got["verdict"] != expected:
                print(f"FAIL {name}: {got}", file=sys.stderr)
                return 1
        print(f"SELF_TEST_PASS: {len(CASES)} synthetic cases; no outside runtime run")
        return 0
    if args.sample:
        print(json.dumps({"case_type": "one_agent_message", "events": CASES[0][1]}, indent=2))
        return 0
    if args.json:
        print(json.dumps({name: classify({"case_type": "one_agent_message", "events": events})
                          for name, events, _ in CASES}, indent=2))
        return 0
    try:
        trace = json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as e:
        print(json.dumps({"verdict": "INVALID", "reason": f"cannot read trace: {type(e).__name__}"}))
        return 2
    result = classify(trace)
    print(json.dumps(result, indent=2))
    return 2 if result["verdict"] == "INVALID" else 1 if result["verdict"] in ("LOSS_WINDOW", "UNRESOLVED_AFTER_CLOSE") else 0

if __name__ == "__main__":
    raise SystemExit(main())
