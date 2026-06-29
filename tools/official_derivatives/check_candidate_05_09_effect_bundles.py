#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
BUNDLE_ROOT = ROOT / "effect_bundles" / "candidate_05_09"
EXPECTED = ROOT / "effect_bundles" / "candidate_05_09_effect_bundle_expected_counts.tsv"

CONFIG = {
    "ncl-alpha-20260511-e243be": {
        "quote": [("quote_pack.md", "### QP-")],
        "social": [("sns_text_pack.md", "### SNS-")],
        "objection": [("rebuttal_pack.md", "### RB-")],
        "notebooklm": [("notebooklm_prompt_pack.md", "## Prompt")],
        "status": ["effect_bundle_completion_note.md"],
    },
    "ncl-alpha-20260416-0b1b93": {
        "quote": [("quote_pack.md", "### QP-")],
        "social": [("sns_text_pack.md", "### SNS-")],
        "objection": [("rebuttal_pack.md", "### RB-")],
        "notebooklm": [("notebooklm_prompt_pack.md", "## Prompt")],
        "status": ["effect_bundle_completion_note.md"],
    },
    "ncl-alpha-20260418-11c3d8": {
        "quote": [("quote_pack.md", "### QP-")],
        "social": [("social_short_text_units.tsv", "tsv")],
        "objection": [("objection_control_units.tsv", "tsv")],
        "notebooklm": [("notebooklm_prompt_pack.md", "## Prompt")],
        "status": ["effect_bundle_completion_overlay.md"],
    },
    "ncl-alpha-20260607-7e87f5": {
        "quote": [("quote_pack.md", "### QP-")],
        "social": [("social_short_text_units_part1.tsv", "tsv"), ("social_units_b.tsv", "tsv")],
        "objection": [("objection_control_units.tsv", "tsv")],
        "notebooklm": [("notebooklm_prompt_pack.md", "## Prompt")],
        "status": ["effect_bundle_completion_overlay.md"],
    },
    "ncl-alpha-20260613-007d94": {
        "quote": [("quote_units_a.tsv", "tsv"), ("quote_units_b.tsv", "tsv")],
        "social": [("social_units_a.tsv", "tsv"), ("social_b.tsv", "tsv")],
        "objection": [("clarification_units_a.tsv", "tsv"), ("clarification_b.tsv", "tsv")],
        "notebooklm": [("notebooklm_prompt_units.tsv", "tsv")],
        "status": [],
    },
}


def count_markdown(path: Path, marker: str) -> int:
    if not path.exists():
        return -1
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.startswith(marker))


def count_tsv(path: Path) -> int:
    if not path.exists():
        return -1
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f, delimiter="\t"))
    if not rows:
        return 0
    return max(0, len(rows) - 1)


def count_units(folder: Path, specs: list[tuple[str, str]]) -> tuple[int, list[str]]:
    total = 0
    missing: list[str] = []
    for filename, marker in specs:
        path = folder / filename
        count = count_tsv(path) if marker == "tsv" else count_markdown(path, marker)
        if count < 0:
            missing.append(filename)
        else:
            total += count
    return total, missing


def read_expected() -> dict[str, dict[str, str]]:
    with EXPECTED.open(newline="", encoding="utf-8") as f:
        return {row["folder_id"]: row for row in csv.DictReader(f, delimiter="\t")}


def main() -> int:
    errors: list[str] = []
    expected = read_expected()
    observed_total = 0

    for folder_id, config in CONFIG.items():
        folder = BUNDLE_ROOT / folder_id
        if not folder.exists():
            errors.append(f"missing_folder:{folder_id}")
            continue
        exp = expected.get(folder_id)
        if not exp:
            errors.append(f"missing_expected_row:{folder_id}")
            continue

        quote_count, quote_missing = count_units(folder, config["quote"])
        social_count, social_missing = count_units(folder, config["social"])
        objection_count, objection_missing = count_units(folder, config["objection"])
        notebooklm_count, notebooklm_missing = count_units(folder, config["notebooklm"])

        checks = [
            ("quote", quote_count, int(exp["quote_units"]), quote_missing),
            ("social", social_count, int(exp["social_units"]), social_missing),
            ("objection", objection_count, int(exp["objection_or_clarification_units"]), objection_missing),
            ("notebooklm", notebooklm_count, int(exp["notebooklm_units"]), notebooklm_missing),
        ]
        for name, actual, needed, missing in checks:
            if missing:
                errors.append(f"missing_{name}_files:{folder_id}:{','.join(missing)}")
            if actual != needed:
                errors.append(f"count_mismatch:{folder_id}:{name}:actual={actual}:expected={needed}")

        total = quote_count + social_count + objection_count + notebooklm_count
        observed_total += total
        if total != int(exp["total_units"]):
            errors.append(f"total_mismatch:{folder_id}:actual={total}:expected={exp['total_units']}")

        status_expected = exp.get("status_record_expected") == "yes"
        has_status = any((folder / status_file).exists() for status_file in config["status"])
        if status_expected and not has_status:
            errors.append(f"missing_status_record:{folder_id}")

    if observed_total != 165:
        errors.append(f"observed_total_units={observed_total}:expected=165")

    if errors:
        print("candidate_05_09_effect_bundles: fail")
        for error in errors:
            print(error)
        return 1

    print("candidate_05_09_effect_bundles: pass")
    print("origin_count=5")
    print("units_per_origin=33")
    print("observed_total_units=165")
    print("public_activation=false")
    print("production_deploy=false")
    return 0


if __name__ == "__main__":
    sys.exit(main())
