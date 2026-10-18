#!/usr/bin/env python3
"""Check synthetic agent-team UI traces for distinct peer messages versus bounded tool progress.

Source case: https://github.com/QwenLM/qwen-code/pull/13902#discussion_r4306135401
Original Nakagawa counterexample: https://github.com/QwenLM/qwen-code/pull/13902#discussion_r4305247350
This is a portable *observation comparator*, not a Qwen test, model-run proof,
proof of source theory adoption, or a claim about any actual user session.
Input schema: {"events": [event, ...], "rows": [row, ...]}; each event/row
has kind="message" with agent (recipient), sender, text or kind="tool"
with agent (actor), text. Capture observed UI rows with your own adapter.
All message instances remain distinct (including identical text/participants),
while this deliberately minimal model keeps the latest tool-progress row per agent.
Exit: 0 faithful, 1 discrepancy, 2 invalid input.
"""
import argparse
import json
import sys
from pathlib import Path


def signature(x):
    return (x["agent"], x["sender"], x["text"])


def assess(data):
    if not isinstance(data, dict) or not isinstance(data.get("events"), list) or not isinstance(data.get("rows"), list):
        return {"verdict": "INVALID", "reason": "events and rows arrays required"}
    events, rows = data["events"], data["rows"]
    if len(events) > 10000 or len(rows) > 10000:
        return {"verdict": "INVALID", "reason": "trace exceeds 10000 rows"}
    for i, x in enumerate(events + rows):
        if not isinstance(x, dict) or x.get("kind") not in ("message", "tool"):
            return {"verdict": "INVALID", "reason": f"item {i}: kind must be message/tool"}
        if not isinstance(x.get("agent"), str) or not x["agent"].strip() or not isinstance(x.get("text"), str):
            return {"verdict": "INVALID", "reason": f"item {i}: agent/text required"}
        if x["kind"] == "message" and (not isinstance(x.get("sender"), str) or not x["sender"].strip()):
            return {"verdict": "INVALID", "reason": f"item {i}: message sender required"}
    before = [signature(x) for x in events if x["kind"] == "message"]
    after = [signature(x) for x in rows if x["kind"] == "message"]
    if before != after:
        return {"verdict": "MESSAGE_EVENT_LOSS_OR_REORDER", "reason": "ordered peer-message instances differ; same sender and identical text still count as distinct events", "expected": len(before), "observed": len(after)}
    latest_tool = {}
    for x in events:
        if x["kind"] == "tool":
            latest_tool[x["agent"]] = x["text"]
    actual_tool = {}
    for x in rows:
        if x["kind"] == "tool":
            actual_tool.setdefault(x["agent"], []).append(x["text"])
    if set(actual_tool) != set(latest_tool):
        return {"verdict": "TOOL_PROGRESS_MISSING_OR_SPURIOUS", "reason": "tool-progress agent set differs"}
    for agent, latest in latest_tool.items():
        if actual_tool[agent] != [latest]:
            return {"verdict": "TOOL_PROGRESS_STALE_OR_UNBOUNDED", "reason": f"{agent}: expected only the latest tool-progress text"}
    return {"verdict": "FAITHFUL", "message_events": len(before), "latest_tool_agents": len(latest_tool)}


def self_test():
    t = lambda kind, agent="/root/checker", text="", sender="/root/writer": dict(kind=kind, agent=agent, text=text, **({"sender": sender} if kind == "message" else {}))
    s, a, b, e = t("tool", text="started read_file"), t("message", text="read auth"), t("message", text="read another file"), t("tool", text="finished read_file")
    base = [s, a, b, e]
    tests = [
      ("distinct same-sender messages plus bounded tool progress", {"events":base,"rows":[e,a,b]}, "FAITHFUL"),
      ("both same-sender messages lost to merge", {"events":base,"rows":[e,b]}, "MESSAGE_EVENT_LOSS_OR_REORDER"),
      ("tool row overwritten with message", {"events":base,"rows":[a,b]}, "TOOL_PROGRESS_MISSING_OR_SPURIOUS"),
      ("stale tool progress", {"events":base,"rows":[s,a,b]}, "TOOL_PROGRESS_STALE_OR_UNBOUNDED"),
      ("unbounded tool rows", {"events":base,"rows":[s,e,a,b]}, "TOOL_PROGRESS_STALE_OR_UNBOUNDED"),
      ("messages out of order", {"events":base,"rows":[e,b,a]}, "MESSAGE_EVENT_LOSS_OR_REORDER"),
      ("identical message text is still two events", {"events":[a,a],"rows":[a,a]}, "FAITHFUL"),
      ("identical message text lost", {"events":[a,a],"rows":[a]}, "MESSAGE_EVENT_LOSS_OR_REORDER"),
      ("distinct recipients preserved", {"events":[a,t("message",agent="/root/reviewer",text="read auth")],"rows":[a,t("message",agent="/root/reviewer",text="read auth")]}, "FAITHFUL"),
      ("different senders preserved", {"events":[a,t("message",text="read auth",sender="/root/leader")],"rows":[a,t("message",text="read auth",sender="/root/leader")]}, "FAITHFUL"),
      ("no fabricated messages", {"events":[],"rows":[a]}, "MESSAGE_EVENT_LOSS_OR_REORDER"),
      ("no tools", {"events":[a],"rows":[a]}, "FAITHFUL"),
      ("invalid missing sender", {"events":[{"kind":"message","agent":"x","text":"y"}],"rows":[]}, "INVALID"),
      ("invalid malformed input", {"events":[],"rows":"not a list"}, "INVALID"),
    ]
    for name, data, expected in tests:
        actual = assess(data)["verdict"]
        if actual != expected:
            print(f"FAIL {name}: expected={expected} actual={actual}", file=sys.stderr)
            return 1
    print(f"SELF_TEST_PASS: {len(tests)} synthetic positive/negative/invalid cases; no external runtime invoked")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--self-test", action="store_true")
    g.add_argument("--sample", action="store_true")
    g.add_argument("--input", type=Path)
    args = p.parse_args()
    if args.self_test:
        return self_test()
    if args.sample:
        events = [{"kind":"tool","agent":"/root/checker","text":"started read_file"},{"kind":"message","agent":"/root/checker","sender":"/root/writer","text":"review the auth module"},{"kind":"message","agent":"/root/checker","sender":"/root/writer","text":"check another file"},{"kind":"tool","agent":"/root/checker","text":"finished read_file"}]
        rows = [events[3],events[1],events[2]]
        print(json.dumps({"events":events,"rows":rows}, ensure_ascii=False, indent=2))
        return 0
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as e:
        print(json.dumps({"verdict":"INVALID","reason":type(e).__name__}))
        return 2
    result = assess(data)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if result["verdict"]=="INVALID" else (0 if result["verdict"]=="FAITHFUL" else 1)

if __name__ == "__main__":
    raise SystemExit(main())
