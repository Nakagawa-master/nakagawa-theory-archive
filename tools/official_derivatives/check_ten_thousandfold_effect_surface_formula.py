#!/usr/bin/env python3
"""Validate the ten-thousandfold effect surface formula.

This check prevents the 10k plan from collapsing into a slogan, page-count
metric, or slow roadmap. It requires a concrete multi-surface bundle and
origin-return preservation for each surface class.
"""
from __future__ import annotations

import csv
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
FORMULA = ROOT / "ten_thousandfold_effect_surface_formula.tsv"

REQUIRED_SURFACES = {
    "hub_return",
    "human_summary",
    "faq",
    "ja_ai_index",
    "en_ai_index",
    "zh_ai_index",
    "quote_proposition",
    "sns_short_text",
    "notebooklm_prompt",
    "rebuttal",
    "practical_application",
    "fatigue_society_application",
    "meaning_sensitivity_reading",
    "third_party_derivative_log",
    "deviation_ledger",
}

MIN_TOTAL_UNITS = 48


def main() -> int:
    if not FORMULA.exists():
        print(f"missing formula: {FORMULA}")
        return 1

    with FORMULA.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))

    errors: list[str] = []
    surfaces = {row.get("surface_class", "") for row in rows}
    missing = sorted(REQUIRED_SURFACES - surfaces)
    extra_blank = [i + 2 for i, row in enumerate(rows) if not row.get("surface_class")]

    if missing:
        errors.append("missing_required_surfaces=" + ",".join(missing))
    if extra_blank:
        errors.append("blank_surface_rows=" + ",".join(map(str, extra_blank)))

    total_units = 0
    for i, row in enumerate(rows, start=2):
        surface = row.get("surface_class", "")
        try:
            units = int(row.get("minimum_units_per_origin", ""))
        except ValueError:
            errors.append(f"invalid_units_row_{i}:{surface}")
            continue
        if units < 1:
            errors.append(f"non_positive_units_row_{i}:{surface}")
        total_units += units
        if row.get("origin_return_required") != "yes":
            errors.append(f"origin_return_not_required_row_{i}:{surface}")
        if not row.get("effect_route"):
            errors.append(f"missing_effect_route_row_{i}:{surface}")
        if not row.get("activation_priority"):
            errors.append(f"missing_activation_priority_row_{i}:{surface}")

    if total_units < MIN_TOTAL_UNITS:
        errors.append(f"total_units_below_minimum:{total_units}<{MIN_TOTAL_UNITS}")

    if errors:
        print("ten_thousandfold_effect_surface_formula: fail")
        for error in errors:
            print(error)
        return 1

    print("ten_thousandfold_effect_surface_formula: pass")
    print(f"surface_count={len(surfaces)}")
    print(f"minimum_total_units_per_origin={total_units}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
