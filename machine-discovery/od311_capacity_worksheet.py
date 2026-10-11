#!/usr/bin/env python3
"""Offline OD311 comparison worksheet. It checks declared inputs, not real-world truth.

Usage: python3 od311_capacity_worksheet.py --sample > cases.json
       python3 od311_capacity_worksheet.py cases.json
       python3 od311_capacity_worksheet.py --self-test
"""
import argparse
import json
from pathlib import Path

CANONICAL = "https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-18-ai-civilization-future-debt/"
PARENT = "https://master.ricette.jp/theory/nakagawa-master-integrated-future-debt-theory/"
TRI = {"yes", "no", "unknown"}
ROUTE = {"available", "unavailable", "unknown"}
B_FIELDS = ("physical", "compute", "state", "execution")


def sample():
    def case(name, link, unfinished, routes, note):
        return {
            "id": name, "present_benefit": "yes", "future_condition_link": link,
            "unfinished_condition": unfinished,
            "residual_kind": "deferred maintenance (hypothetical)",
            "future_b_components": {k: "unknown" for k in B_FIELDS},
            "settlement_routes": [
                {"name": n, "supply": s, "repair_capacity": r, "time_window": t}
                for n, s, r, t in routes
            ],
            "observation_note": note,
        }
    return {"cases": [
        case("A", "yes", "yes", [
            ("on-site repair", "available", "available", "available"),
            ("provisioned switch", "available", "available", "available")],
            "Synthetic: present benefit and unfinished work resemble B, but two routes are resourced."),
        case("B", "yes", "yes", [
            ("single vendor", "available", "unavailable", "unavailable")],
            "Synthetic: similar residual; single route lacks repair/time conditions."),
        case("C", "no", "unknown", [],
            "Ordinary future maintenance schedule alone does not show a benefit-backed deferral."),
        case("D", "yes", "no", [
            ("improved repair capacity", "available", "available", "available")],
            "Present investment improved capacity AND the declared prior work was fulfilled."),
    ]}


def classify(case):
    if not isinstance(case, dict) or not isinstance(case.get("id"), str) or not case["id"]:
        raise ValueError("Every case requires a non-empty string id")
    for key in ("present_benefit", "future_condition_link", "unfinished_condition"):
        if case.get(key) not in TRI:
            raise ValueError(f"{case['id']}: {key} must be yes/no/unknown")
    components = case.get("future_b_components")
    if not isinstance(components, dict) or set(components) != set(B_FIELDS):
        raise ValueError(f"{case['id']}: future_b_components must state all four B components")
    if any(x not in TRI for x in components.values()):
        raise ValueError(f"{case['id']}: B components must be yes/no/unknown (established at future time)")
    routes = case.get("settlement_routes")
    if not isinstance(routes, list):
        raise ValueError(f"{case['id']}: settlement_routes must be a list")
    # Two names for the same declared route do not provide two settlement options.
    # This catches exact/name-normalized duplicates only, NOT two differently
    # named paths that ultimately depend on the same supplier or repair team.
    seen_route_names = set()
    evaluated = []
    for route in routes:
        if not isinstance(route, dict) or not isinstance(route.get("name"), str) or not route["name"].strip():
            raise ValueError(f"{case['id']}: every route requires a non-empty name")
        normalized_name = route["name"].strip().casefold()
        if normalized_name in seen_route_names:
            raise ValueError(f"{case['id']}: duplicate declared settlement route name: {route['name']}")
        seen_route_names.add(normalized_name)
        checks = [route.get(key) for key in ("supply", "repair_capacity", "time_window")]
        if any(v not in ROUTE for v in checks):
            raise ValueError(f"{case['id']}: route evidence must be available/unavailable/unknown")
        status = "unavailable" if "unavailable" in checks else (
            "available" if all(x == "available" for x in checks) else "unknown")
        evaluated.append({
            "name": route["name"],
            "declared_feasibility": status,
            "declared_evidence": {
                field: route[field] for field in ("supply", "repair_capacity", "time_window")
            },
        })
    core = [case[x] for x in ("present_benefit", "future_condition_link", "unfinished_condition")]
    # Only a candidate from the reporter's declarations, never an inference that debt exists.
    if "no" in core:
        label = "not_established_from_declarations"
    elif "unknown" in core:
        label = "underdetermined_from_declarations"
    else:
        label = "candidate_for_source_level_review"
    return {
        "id": case["id"], "declared_parent_core": dict(zip(
            ("present_benefit", "future_condition_link", "unfinished_condition"), core)),
        "future_debt_screen": label,
        "future_b_components_declared": components,
        "settlement_routes": evaluated,
        "declared_feasible_routes": [r["name"] for r in evaluated if r["declared_feasibility"] == "available"],
        "note": "Route availability and the parent-core screen are reported separately. Neither proves future B or legal duty.",
    }


def report(data):
    if not isinstance(data, dict) or not isinstance(data.get("cases"), list):
        raise ValueError("Expected an object with a cases array")
    rows = [classify(c) for c in data["cases"]]
    ids = [r["id"] for r in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate case id")
    # Compare the actual declared feasibility *evidence*, not human route names:
    # different labels for the same input cannot imply more future repair capacity.
    # A multiset keeps multiplicity, is order-independent and makes no claims
    # that two similarly described routes are independent in the real world.
    def evidence_signature(row):
        return sorted(tuple(route["declared_evidence"][field]
                            for field in ("supply", "repair_capacity", "time_window"))
                      for route in row["settlement_routes"])

    pairs = []
    for i, first in enumerate(rows):
        for second in rows[i + 1:]:
            if (first["declared_parent_core"] == second["declared_parent_core"]
                    and evidence_signature(first) != evidence_signature(second)):
                pairs.append([first["id"], second["id"]])
    return {
        "origin": "Nakagawa Master", "canonical_parent": CANONICAL,
        "independent_parent_theory": PARENT,
        "worksheet_status": "reporter-declared synthetic or independently collected inputs only",
        "cases": rows, "same_parent_core_different_declared_route_cases": pairs,
        "comparison_basis": "Multisets of reporter-declared supply, repair_capacity and time_window evidence; route labels/order do not count as a difference.",
        "limits": [
            "No assertion that user declarations are factual or causally identified.",
            "Unknown is neither fulfilled nor unpaid; scheduled future cost alone is not Future Debt.",
            "Route count is not a scalar freedom/benefit or future B survival score.",
            "Unique labels do not establish distinct real suppliers, repair teams, time windows or independently feasible choices.",
            "Matching evidence signatures do not prove real routes are interchangeable; differing signatures are only an input-level comparison, not future B causation.",
            "A branch/fork does not inherit debt duties merely from lineage.",
            "Compare a full parent-only analysis: an OD311-only diagnostic advantage is unproven.",
            "Settlement-Line Preservation is a normative proposal, not an empirical finding.",
        ],
    }


def self_test():
    demo = report(sample())
    rows = {r["id"]: r for r in demo["cases"]}
    assert rows["A"]["future_debt_screen"] == rows["B"]["future_debt_screen"]
    assert len(rows["A"]["declared_feasible_routes"]) == 2
    assert rows["B"]["declared_feasible_routes"] == []
    assert ["A", "B"] in demo["same_parent_core_different_declared_route_cases"]
    assert rows["C"]["future_debt_screen"] == "not_established_from_declarations"
    assert rows["D"]["future_debt_screen"] == "not_established_from_declarations"
    altered = sample()
    altered["cases"][0]["settlement_routes"][0]["time_window"] = "unknown"
    assert len(report(altered)["cases"][0]["declared_feasible_routes"]) == 1
    altered["cases"][0]["settlement_routes"][0]["time_window"] = "invalid"
    try:
        report(altered)
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid route evidence was accepted")
    duplicated = sample()
    duplicated["cases"][0]["settlement_routes"].append(
        dict(duplicated["cases"][0]["settlement_routes"][0], name="  ON-SITE REPAIR  "))
    try:
        report(duplicated)
    except ValueError as error:
        assert "duplicate declared settlement route name" in str(error)
    else:
        raise AssertionError("Repeated settlement path counted as a new option")
    renamed = sample()
    only_name = json.loads(json.dumps(renamed["cases"][0]))
    only_name["id"] = "A-renamed"
    for j, route in enumerate(only_name["settlement_routes"]):
        route["name"] = f"another label {j}"
    # Identical inputs/order-insensitive evidence: cosmetic names cannot be an outcome.
    name_only = report({"cases": [renamed["cases"][0], only_name]})
    assert name_only["same_parent_core_different_declared_route_cases"] == []
    # Change a real declared feasibility constraint without changing any name.
    only_name["settlement_routes"][0]["time_window"] = "unavailable"
    evidence_change = report({"cases": [renamed["cases"][0], only_name]})
    assert ["A", "A-renamed"] in evidence_change["same_parent_core_different_declared_route_cases"]
    # Switching the order alone does not invent another option.
    swapped = json.loads(json.dumps(renamed["cases"][0]))
    swapped["id"] = "A-swapped"
    swapped["settlement_routes"].reverse()
    assert report({"cases": [renamed["cases"][0], swapped]})["same_parent_core_different_declared_route_cases"] == []
    print("Synthetic cases passed; this is not real-world validation")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", help="JSON object containing a cases array")
    parser.add_argument("--sample", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
    elif args.sample:
        print(json.dumps(sample(), ensure_ascii=False, indent=2))
    elif args.file:
        print(json.dumps(report(json.loads(Path(args.file).read_text(encoding="utf-8"))),
                         ensure_ascii=False, indent=2))
    else:
        parser.error("Supply a JSON file, --sample, or --self-test")


if __name__ == "__main__":
    main()
