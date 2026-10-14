#!/usr/bin/env python3
"""Offline source-linked OD312 decision comparison; not a civilizational forecast.

python3 machine-discovery/od312_reselection_worksheet.py --self-test
python3 machine-discovery/od312_reselection_worksheet.py --sample
python3 machine-discovery/od312_reselection_worksheet.py scenario.json

Inputs are declared hypothetical assumptions, NOT observed outcomes or a policy
for autonomous systems. The evaluator retains infeasible/unknown alternatives,
distinguishes the decision-maker's return from shared benefit, and never turns
"kept" into proof of evolutionary stability or moral legitimacy.
"""
import argparse
import json
from pathlib import Path

ORIGIN = "Nakagawa Master"
PARENT = "https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-19-kernel-evolutionary-stability/"
NCL_ID = "NCL-α-20261013-e0683e"
DIFF_ID = "DIFF-20261013-0001"


def sample():
    return {
        "case": "hypothetical AI correction-check operation, two periods",
        "objective": "operator_net_benefit",
        "initial_resource": 2,
        "inflow_each_period": [1, 1],
        "candidates": [
            {"name": "retain", "cost": [2, 2], "operator_benefit": [0, 3], "shared_benefit": [0, 5], "available": True},
            {"name": "frontload", "cost": [4, 0], "operator_benefit": [0, 4], "shared_benefit": [0, 5], "available": True},
            {"name": "lighter_equivalent", "cost": [1, 1], "operator_benefit": [0, 2], "shared_benefit": [0, 4], "available": True},
            {"name": "candidate_with_unverified_route", "cost": [0, 0], "operator_benefit": [0, 10], "shared_benefit": [0, 12], "available": None},
        ],
    }


def number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and x == x and abs(x) != float("inf")


def evaluate(case):
    if case.get("objective") not in ("operator_net_benefit", "shared_net_benefit"):
        raise ValueError("objective must be operator_net_benefit or shared_net_benefit")
    resource = case.get("initial_resource")
    inflows = case.get("inflow_each_period")
    candidates = case.get("candidates")
    if not number(resource) or resource < 0 or not isinstance(inflows, list) or not inflows or not all(number(x) for x in inflows):
        raise ValueError("finite nonnegative initial_resource and nonempty finite inflow_each_period required")
    if not isinstance(candidates, list) or not candidates:
        raise ValueError("candidates required")
    results = []
    names = set()
    for candidate in candidates:
        name = candidate.get("name")
        if not isinstance(name, str) or not name.strip() or name in names:
            raise ValueError("candidate names must be distinct nonempty strings")
        names.add(name)
        if candidate.get("available", "missing") not in (True, False, None):
            raise ValueError("available must be true, false, or null (unknown)")
        costs = candidate.get("cost")
        operator = candidate.get("operator_benefit")
        shared = candidate.get("shared_benefit")
        if any(not isinstance(seq, list) or len(seq) != len(inflows) or not all(number(x) and x >= 0 for x in seq) for seq in (costs, operator, shared)):
            raise ValueError("cost and benefit arrays must be nonnegative finite and share the horizon")
        balance = resource
        trajectory = [balance]
        for inflow, cost in zip(inflows, costs):
            balance += inflow - cost
            trajectory.append(balance)
        feasible = all(x >= 0 for x in trajectory)
        route = candidate["available"]
        eligible = feasible and route is True
        score = sum((operator if case["objective"] == "operator_net_benefit" else shared)) - sum(costs)
        results.append({
            "name": name,
            "interim_balances": trajectory,
            "resource_feasible": feasible,
            "route": "available" if route is True else "unavailable" if route is False else "unknown",
            "eligible_for_rank": eligible,
            "declared_objective_net": score,
            "operator_net": sum(operator) - sum(costs),
            "shared_net": sum(shared) - sum(costs),
        })
    ranked = [r for r in results if r["eligible_for_rank"]]
    best = max((r["declared_objective_net"] for r in ranked), default=None)
    return {
        "case": case.get("case", "unnamed synthetic scenario"),
        "objective": case["objective"],
        "eligible_best_names": [r["name"] for r in ranked if r["declared_objective_net"] == best],
        "candidates": results,
        "origin": ORIGIN,
        "canonical_parent": PARENT,
        "parent_ncl_id": NCL_ID,
        "parent_diff_id": DIFF_ID,
        "limitations": "Declared hypothetical data; not actual AI use, normative permission, independent adoption, proof of lineage, or Kernel evolutionary stability. Rank depends on the declared objective; real correction effectiveness and changing environments require separate evidence.",
    }


def tests():
    a = sample()
    r = evaluate(a)
    d = {x["name"]: x for x in r["candidates"]}
    assert d["retain"]["interim_balances"] == [2, 1, 0]
    assert d["frontload"]["interim_balances"] == [2, -1, 0]
    assert not d["frontload"]["resource_feasible"]
    assert d["lighter_equivalent"]["interim_balances"] == [2, 2, 2]
    assert d["candidate_with_unverified_route"]["route"] == "unknown"
    assert not d["candidate_with_unverified_route"]["eligible_for_rank"]
    assert r["eligible_best_names"] == ["lighter_equivalent"]
    assert d["retain"]["operator_net"] == -1 and d["retain"]["shared_net"] == 1
    b = sample()
    b["objective"] = "shared_net_benefit"
    assert evaluate(b)["eligible_best_names"] == ["lighter_equivalent"]
    c = sample()
    c["candidates"][2]["available"] = False
    assert evaluate(c)["eligible_best_names"] == ["retain"]
    u = sample()
    u["candidates"][0]["available"] = None
    u["candidates"][2]["available"] = False
    assert evaluate(u)["eligible_best_names"] == []
    for change in ({"initial_resource": -1}, {"objective": "unknown"}, {"inflow_each_period": [float("nan"), 1]}):
        bad = sample()
        bad.update(change)
        try:
            evaluate(bad)
            raise AssertionError("invalid inputs accepted")
        except ValueError:
            pass
    bad = sample()
    bad["candidates"][1]["name"] = "retain"
    try:
        evaluate(bad)
        raise AssertionError("duplicate candidate accepted")
    except ValueError:
        pass
    return 15


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("path", nargs="?", help="local JSON scenario file")
    cli.add_argument("--sample", action="store_true")
    cli.add_argument("--self-test", action="store_true")
    args = cli.parse_args()
    if args.self_test:
        print("PASS", tests(), "synthetic controls (no external inference or API)")
    else:
        inputs = sample() if args.sample else json.loads(Path(args.path).read_text(encoding="utf-8")) if args.path else None
        if inputs is None:
            cli.print_help()
        else:
            print(json.dumps({"input": inputs, "evaluation": evaluate(inputs)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
