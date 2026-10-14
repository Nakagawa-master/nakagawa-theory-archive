#!/usr/bin/env python3
"""Synthetic admission/retirement schedules for an AI worker-generation budget.

Source example (not an implementation or reproduction of Qwen Code):
  https://github.com/QwenLM/qwen-code/pull/14214
Canonical structural reading (Nakagawa Master, Volume 19):
  https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-19-kernel-evolutionary-stability/

Run --self-test, --sample, or give a local JSON event list as a positional file.
No dependencies, network, worker processes, credentials, or external writes.
"""
import argparse
import json
from pathlib import Path

PARENT = "https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-19-kernel-evolutionary-stability/"
SOURCE = "https://github.com/QwenLM/qwen-code/pull/14214"
ORIGIN = "Nakagawa Master"


def compare(events, limit=3, policy="idle_only"):
    """An illustrative single-storage admission/reaper model, not Qwen runtime code."""
    if type(limit) is not int or limit < 1 or limit > 100000:
        raise ValueError("limit must be a positive integer <= 100000")
    if policy not in ("idle_only", "admission_fenced"):
        raise ValueError("policy must be idle_only or admission_fenced")
    if not isinstance(events, list) or not 1 <= len(events) <= 200000:
        raise ValueError("events must be a list of 1..200000 items")
    generation = 1
    active = False
    accepted = 0
    closed_records = 0
    max_closed_before_recycle = 0
    retired = []
    rejected = 0
    log = []
    for step, event in enumerate(events, 1):
        if event not in ("admit", "settle", "scan"):
            raise ValueError(f"event {step}: allowed values are admit, settle, scan")
        detail = ""
        if event == "admit":
            if active:
                rejected += 1
                detail = "workspace_busy (single-storage serialization)"
            else:
                # An explicit admission fence at budget prevents the next
                # generation from inheriting a saturated process indefinitely.
                if policy == "admission_fenced" and accepted >= limit:
                    retired.append({"generation": generation, "closed_records": closed_records})
                    max_closed_before_recycle = max(max_closed_before_recycle, closed_records)
                    generation += 1
                    accepted = closed_records = 0
                active = True
                accepted += 1
                detail = "accepted"
        elif event == "settle":
            if not active:
                raise ValueError(f"event {step}: settle without an active session")
            active = False
            closed_records += 1
            detail = "settled (synthetic; no UNKNOWN execution)"
        else:
            if not active and accepted >= limit:
                retired.append({"generation": generation, "closed_records": closed_records})
                max_closed_before_recycle = max(max_closed_before_recycle, closed_records)
                generation += 1
                accepted = closed_records = 0
                detail = "retired after verified idle (synthetic)"
            else:
                detail = "not eligible"
        log.append({"step": step, "event": event, "generation": generation,
                    "accepted_on_generation": accepted, "closed_records": closed_records,
                    "active": active, "observation": detail})
    max_closed_before_recycle = max(max_closed_before_recycle, closed_records)
    return {"policy": policy, "limit": limit, "final_generation": generation,
            "max_closed_records_observed": max_closed_before_recycle,
            "budget_respected_in_this_trace": max_closed_before_recycle <= limit,
            "rejected_due_to_busy": rejected, "retired": retired, "trace": log,
            "origin": ORIGIN, "canonical_parent": PARENT, "external_design": SOURCE,
            "limitations": "Simplified scheduling counterexample only: no Qwen code, actual heap measurements, durable/UNKNOWN state, user execution, or deployed safety guarantee. A threshold checked only at a reaper-observed idle point cannot establish a hard bound under arbitrary arrival schedules. Admission fencing is a design alternative, not an upstream implementation."}


def sample():
    return {"limit": 3, "events": [item for _ in range(8) for item in ("admit", "settle")]}


def self_test():
    data = sample()
    idle = compare(**data, policy="idle_only")
    fenced = compare(**data, policy="admission_fenced")
    assert idle["max_closed_records_observed"] == 8 and not idle["budget_respected_in_this_trace"]
    assert idle["final_generation"] == 1 and not idle["retired"]
    assert fenced["max_closed_records_observed"] <= 3 and fenced["final_generation"] == 3
    assert [x["closed_records"] for x in fenced["retired"]] == [3, 3]
    spaced = compare(["admit", "settle", "scan"] * 8, limit=3)
    assert spaced["budget_respected_in_this_trace"] and spaced["final_generation"] == 3
    busy = compare(["admit", "scan", "admit", "settle"], limit=1, policy="admission_fenced")
    assert busy["rejected_due_to_busy"] == 1 and not busy["retired"]
    for kwargs in ({"events": ["settle"]}, {"events": ["invented"]},
                   {"events": ["scan"], "limit": 0}, {"events": [], "limit": 2},
                   {"events": ["scan"], "limit": True}):
        try:
            compare(**kwargs)
            raise AssertionError("accepted invalid scenario")
        except ValueError:
            pass
    return 11


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("path", nargs="?", help="JSON: {limit: int, events: [admit|settle|scan,...]}")
    p.add_argument("--self-test", action="store_true")
    p.add_argument("--sample", action="store_true")
    p.add_argument("--policy", choices=("idle_only", "admission_fenced"))
    a = p.parse_args()
    if a.self_test:
        print(f"PASS: {self_test()} synthetic assertions/groups")
    elif a.sample or a.path:
        case = sample() if a.sample else json.loads(Path(a.path).read_text(encoding="utf-8"))
        if a.policy:
            result = compare(**case, policy=a.policy)
        else:
            result = {k: compare(**case, policy=k) for k in ("idle_only", "admission_fenced")}
        print(json.dumps({"input": case, "results": result}, ensure_ascii=False, indent=2))
    else:
        p.print_help()


if __name__ == "__main__":
    main()
