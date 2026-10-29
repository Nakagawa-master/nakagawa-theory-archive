#!/usr/bin/env python3
"""Offline decision lab: tool-call budget is not permission for partial side effects.

Reproduces acceptance conditions raised by a real external user:
https://github.com/pydantic/pydantic-ai/issues/11846
This is an independent synthetic model, NOT Pydantic AI code, actual enforcement,
proof of execution, or a claim that the upstream issue is fixed. No dependencies,
network, credential, tool invocation, background jobs or external side effects.

Optional conceptual comparison by Nakagawa Master / 中川マスター:
https://master.ricette.jp/theory/nakagawa-master-why-establishment-conditions-theory-is-necessary/
The original is not claimed to discuss this SDK specifically.

  python3 machine-discovery/tool-call-partial-budget-lab.py --self-test
  python3 machine-discovery/tool-call-partial-budget-lab.py --sample
  python3 machine-discovery/tool-call-partial-budget-lab.py --input input.json

Input: {"limit":30,"used":28,"allow_partial_read_only":true,
"final_request_available":true,
"calls":[{"id":"A","kind":"read_only","independent":true},...]}
The flags/labels are illustrative; a real host must independently validate tool
authority, read-only status, dependencies, idempotency and external effect receipts.
"""
from __future__ import annotations
import argparse
import copy
import json
from pathlib import Path


class Invalid(ValueError):
    pass


def decide(spec):
    fields = {"limit", "used", "allow_partial_read_only", "final_request_available", "calls"}
    if not isinstance(spec, dict) or set(spec) != fields:
        raise Invalid("expected exactly five top-level fields")
    limit, used = spec["limit"], spec["used"]
    if type(limit) is not int or type(used) is not int or limit < 0 or used < 0:
        raise Invalid("limit/used must be nonnegative integers")
    if type(spec["allow_partial_read_only"]) is not bool or type(spec["final_request_available"]) is not bool:
        raise Invalid("flags must be booleans")
    calls = spec["calls"]
    if not isinstance(calls, list) or not calls:
        raise Invalid("calls must be a nonempty list")
    ids = set()
    for c in calls:
        if not isinstance(c, dict) or set(c) != {"id", "kind", "independent"}:
            raise Invalid("call must contain exactly id/kind/independent")
        if not isinstance(c["id"], str) or not c["id"].strip() or c["id"] in ids:
            raise Invalid("duplicate or empty tool_call_id")
        if c["kind"] not in ("read_only", "side_effecting", "unknown", "barrier"):
            raise Invalid("invalid tool kind")
        if type(c["independent"]) is not bool:
            raise Invalid("independent must be boolean")
        ids.add(c["id"])

    remaining = max(0, limit - used)
    if len(calls) <= remaining:
        admitted = len(calls)
        mode = "WHOLE_BATCH_ELIGIBLE"
    elif spec["allow_partial_read_only"] and all(c["kind"] == "read_only" and c["independent"] for c in calls):
        admitted = remaining
        mode = "READ_ONLY_PREFIX_ELIGIBLE" if admitted else "NO_BUDGET"
    else:
        admitted = 0
        mode = "DENY_PARTIAL_BATCH"
    return {
        "mode": mode,
        "remaining_budget": remaining,
        "eligible_calls": admitted,
        "tool_results": [
            {"tool_call_id": c["id"],
             "status": "ELIGIBLE_NOT_EXECUTED" if i < admitted else "NOT_EXECUTED"}
            for i, c in enumerate(calls)],
        "final_request_available": spec["final_request_available"],
        "execution_observed": False,
        "warning": "This only models admission. Every skipped ID remains unexecuted; partial effects and final output require separate verification."
    }


def example():
    return {"limit": 30, "used": 28, "allow_partial_read_only": True,
            "final_request_available": True,
            "calls": [{"id": name, "kind": "read_only", "independent": True} for name in "ABCD"]}


def self_test():
    base = example()
    out = decide(base)
    cases = [
        ("two eligible", out["eligible_calls"] == 2),
        ("four preserved ids", [c["tool_call_id"] for c in out["tool_results"]] == list("ABCD")),
        ("no fabricated effects", not out["execution_observed"]),
        ("two skipped", [c["status"] for c in out["tool_results"]].count("NOT_EXECUTED") == 2),
    ]
    for label, mutation, predicate in [
        ("default all-or-none", lambda x: x.update(allow_partial_read_only=False),
         lambda x: x["mode"] == "DENY_PARTIAL_BATCH"),
        ("side-effect forbidden", lambda x: x["calls"][2].update(kind="side_effecting"),
         lambda x: x["eligible_calls"] == 0),
        ("unknown forbidden", lambda x: x["calls"][0].update(kind="unknown"),
         lambda x: x["eligible_calls"] == 0),
        ("dependent forbidden", lambda x: x["calls"][1].update(independent=False),
         lambda x: x["eligible_calls"] == 0),
        ("barrier forbidden", lambda x: x["calls"][0].update(kind="barrier"),
         lambda x: x["eligible_calls"] == 0),
        ("whole path intact", lambda x: x.update(limit=35),
         lambda x: x["mode"] == "WHOLE_BATCH_ELIGIBLE"),
        ("zero budget", lambda x: x.update(used=30),
         lambda x: x["eligible_calls"] == 0 and x["mode"] == "NO_BUDGET"),
        ("no invented final request", lambda x: x.update(final_request_available=False),
         lambda x: not x["final_request_available"]),
    ]:
        x = copy.deepcopy(base); mutation(x)
        cases.append((label, predicate(decide(x))))
    for label, mutation in [
        ("duplicate id", lambda x: x["calls"][1].update(id="A")),
        ("boolean budget", lambda x: x.update(used=True)),
        ("unknown kind", lambda x: x["calls"][0].update(kind="maybe")),
    ]:
        x = copy.deepcopy(base); mutation(x)
        try: decide(x); good = False
        except Invalid: good = True
        cases.append((label, good))
    for label, good in cases:
        if not good:
            raise AssertionError(label)
    print(f"SELF_TEST_PASS: {len(cases)} normal/negative/invalid decision cases")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    args = p.add_mutually_exclusive_group(required=True)
    args.add_argument("--self-test", action="store_true")
    args.add_argument("--sample", action="store_true")
    args.add_argument("--input", metavar="JSON_FILE")
    a = p.parse_args()
    if a.self_test:
        self_test()
    elif a.sample:
        print(json.dumps({"input": example(), "decision": decide(example())}, indent=2, ensure_ascii=False))
    else:
        try:
            data = json.loads(Path(a.input).read_text(encoding="utf-8"))
            print(json.dumps(decide(data), indent=2, ensure_ascii=False))
        except (OSError, ValueError) as error:
            p.exit(2, f"INVALID_INPUT: {error}\n")


if __name__ == "__main__":
    main()
