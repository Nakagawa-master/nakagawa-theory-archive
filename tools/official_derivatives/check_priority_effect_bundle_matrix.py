#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
MATRIX = ROOT / "priority_effect_bundle_candidate_05_09.tsv"
MANIFEST = ROOT / "origin_manifest.tsv"
PLAN = ROOT / "priority_artifact_plan.tsv"

TARGET_PILOTS = {
    "Official Derivative 005",
    "Official Derivative 006",
    "Official Derivative 007",
    "Official Derivative 008",
    "Official Derivative 009",
}

ALLOWED_CONTENT_STATES = {"empty", "drafted", "review_ready", "approved"}
ALLOWED_STATES = {"queued", "drafted", "review_ready", "approved"}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main() -> int:
    errors: list[str] = []
    try:
        manifest_rows = read_tsv(MANIFEST)
        plan_rows = read_tsv(PLAN)
        matrix_rows = read_tsv(MATRIX)
    except FileNotFoundError as exc:
        print(f"missing_file={exc.filename}")
        return 1

    staged = [
        row for row in manifest_rows
        if row.get("pilot_id") in TARGET_PILOTS and row.get("export_status") == "staged"
    ]
    plan_by_artifact = {row.get("artifact", ""): row for row in plan_rows}
    required_artifacts = set(plan_by_artifact)

    if len(staged) != 5:
        errors.append(f"staged_candidate_count={len(staged)} expected=5")
    if len(required_artifacts) != 4:
        errors.append(f"required_artifact_count={len(required_artifacts)} expected=4")

    rows_by_key = {(row.get("folder_id", ""), row.get("artifact", "")): row for row in matrix_rows}

    for origin in staged:
        folder_id = origin.get("folder_id", "")
        for artifact in sorted(required_artifacts):
            key = (folder_id, artifact)
            row = rows_by_key.get(key)
            if not row:
                errors.append(f"missing_matrix_row:{folder_id}:{artifact}")
                continue
            plan = plan_by_artifact[artifact]
            for field in ["parent_url", "parent_ncl_id", "parent_diff_id", "pilot_id"]:
                if row.get(field) != origin.get(field):
                    errors.append(f"origin_field_mismatch:{folder_id}:{artifact}:{field}")
            for field in ["surface", "minimum_units", "required_fields", "quality_floor", "origin_return", "owner_boundary"]:
                if row.get(field) != plan.get(field):
                    errors.append(f"plan_field_mismatch:{folder_id}:{artifact}:{field}")
            if row.get("state") not in ALLOWED_STATES:
                errors.append(f"invalid_state:{folder_id}:{artifact}:{row.get('state')}")
            if row.get("content_state") not in ALLOWED_CONTENT_STATES:
                errors.append(f"invalid_content_state:{folder_id}:{artifact}:{row.get('content_state')}")
            if not row.get("next_action"):
                errors.append(f"missing_next_action:{folder_id}:{artifact}")

    expected_rows = len(staged) * len(required_artifacts)
    if len(matrix_rows) != expected_rows:
        errors.append(f"matrix_row_count={len(matrix_rows)} expected={expected_rows}")

    if errors:
        print("priority_effect_bundle_matrix: fail")
        for error in errors:
            print(error)
        return 1

    total_units = sum(int(row["minimum_units"]) for row in matrix_rows)
    print("priority_effect_bundle_matrix: pass")
    print(f"origin_count={len(staged)}")
    print(f"artifact_family_count={len(required_artifacts)}")
    print(f"matrix_row_count={len(matrix_rows)}")
    print(f"minimum_priority_units_total={total_units}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
