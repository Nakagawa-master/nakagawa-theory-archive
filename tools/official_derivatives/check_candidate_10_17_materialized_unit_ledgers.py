#!/usr/bin/env python3
import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUNDLE_DIR = ROOT / "effect_bundles"

QUEUE = ROOT / "next_10_queue_candidate_10_19.tsv"
TARGETS = ROOT / "targets.tsv"
EXPECTED = BUNDLE_DIR / "candidate_10_17_effect_bundle_expected_counts.tsv"

COMBINED = BUNDLE_DIR / "candidate_10_17_materialized_unit_ledger.tsv"
SPLIT_PATHS = {
    "quote": BUNDLE_DIR / "candidate_10_17_materialized_quote_units.tsv",
    "social": BUNDLE_DIR / "candidate_10_17_materialized_social_units.tsv",
    "clarification": BUNDLE_DIR / "candidate_10_17_materialized_clarification_units.tsv",
    "notebooklm": BUNDLE_DIR / "candidate_10_17_materialized_notebooklm_units.tsv",
}
SUMMARY = BUNDLE_DIR / "candidate_10_17_materialized_unit_summary.tsv"

EXPECTED_TYPES = {
    "quote": 8,
    "social": 12,
    "clarification": 8,
    "notebooklm": 5,
}

REQUIRED_FIELDS = [
    "batch_id",
    "slot_id",
    "folder_id",
    "unit_type",
    "unit_id",
    "unit_index",
    "language",
    "parent_url",
    "parent_title",
    "parent_ncl_id",
    "parent_diff_id",
    "canonical_url",
    "origin_author",
    "causal_line",
    "boundary_note",
    "misreading_guard",
    "staged_state",
    "public_activation",
    "production_deploy",
]


def read_tsv(path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def row_key(row):
    return (row["folder_id"], row["unit_type"], row["unit_id"])


def main():
    errors = []
    for path in [COMBINED, SUMMARY, *SPLIT_PATHS.values()]:
        if not path.exists():
            errors.append("missing_file=" + str(path.relative_to(ROOT)))

    if errors:
        print("\n".join(errors))
        print("candidate_10_17_materialized_unit_ledger_pass=false")
        return 1

    rows = read_tsv(COMBINED)
    selected = {
        row["folder_id"]: row
        for row in read_tsv(QUEUE)
        if row.get("selection_status") == "selected" and row.get("handoff_status") == "intake_ready"
    }
    staged = {row["folder_id"] for row in read_tsv(TARGETS) if row.get("export_status") == "staged"}
    expected = {row["folder_id"]: row for row in read_tsv(EXPECTED)}
    summary = {row["scope"]: row for row in read_tsv(SUMMARY)}

    if len(selected) != 8:
        errors.append("selected_origin_count=" + str(len(selected)))
    if len(expected) != 8:
        errors.append("expected_origin_count=" + str(len(expected)))
    if len(rows) != 264:
        errors.append("combined_unit_rows=" + str(len(rows)))

    combined_keys = Counter(row_key(row) for row in rows)
    duplicate_keys = [key for key, count in combined_keys.items() if count != 1]
    if duplicate_keys:
        errors.append("duplicate_unit_keys=" + str(duplicate_keys[:5]))

    split_rows = []
    for unit_type, path in SPLIT_PATHS.items():
        unit_rows = read_tsv(path)
        split_rows.extend(unit_rows)
        if any(row.get("unit_type") != unit_type for row in unit_rows):
            errors.append("split_unit_type_mismatch=" + unit_type)
        expected_total = 8 * EXPECTED_TYPES[unit_type]
        if len(unit_rows) != expected_total:
            errors.append(f"{unit_type}_row_count={len(unit_rows)}")

    if Counter(row_key(row) for row in split_rows) != combined_keys:
        errors.append("split_combined_key_mismatch")

    folder_type_counts = defaultdict(Counter)
    folder_counts = Counter()
    for row in rows:
        missing = [field for field in REQUIRED_FIELDS if not row.get(field)]
        if missing:
            errors.append("missing_fields=" + row.get("unit_id", "unknown") + ":" + ",".join(missing))
            continue

        folder = row["folder_id"]
        unit_type = row["unit_type"]
        folder_type_counts[folder][unit_type] += 1
        folder_counts[folder] += 1

        if folder not in selected:
            errors.append("folder_not_selected=" + folder)
        if folder not in staged:
            errors.append("folder_not_staged=" + folder)
        if folder not in expected:
            errors.append("folder_not_expected=" + folder)

        queue_row = selected.get(folder, {})
        for field in ["parent_url", "parent_title", "parent_ncl_id", "parent_diff_id", "canonical_url"]:
            if row.get(field) != queue_row.get(field):
                errors.append(f"{field}_mismatch={row.get('unit_id')}")

        if row["parent_ncl_id"].startswith("NCL-") is False:
            errors.append("bad_parent_ncl_id=" + row["unit_id"])
        if row["parent_diff_id"].startswith("DIFF-") is False:
            errors.append("bad_parent_diff_id=" + row["unit_id"])
        if row["origin_author"] != "Nakagawa Master":
            errors.append("bad_origin_author=" + row["unit_id"])
        if row["staged_state"] != "staged_only":
            errors.append("bad_staged_state=" + row["unit_id"])
        if row["public_activation"] != "false":
            errors.append("bad_public_activation=" + row["unit_id"])
        if row["production_deploy"] != "false":
            errors.append("bad_production_deploy=" + row["unit_id"])
        if len(row["causal_line"]) < 20:
            errors.append("weak_causal_line=" + row["unit_id"])
        if "no " not in row["boundary_note"]:
            errors.append("weak_boundary_note=" + row["unit_id"])
        if row["misreading_guard"].strip().lower() in {"none", "n/a", "pending"}:
            errors.append("weak_misreading_guard=" + row["unit_id"])

    for folder, count in folder_counts.items():
        if count != 33:
            errors.append(f"folder_total_{folder}={count}")
        for unit_type, expected_count in EXPECTED_TYPES.items():
            actual = folder_type_counts[folder][unit_type]
            if actual != expected_count:
                errors.append(f"{folder}_{unit_type}={actual}")

    if summary.get("candidate_10_17_materialized_total", {}).get("unit_count") != "264":
        errors.append("summary_materialized_total")
    if summary.get("candidate_10_17_materialized_total", {}).get("state") != "materialized":
        errors.append("summary_materialized_state")
    if summary.get("candidate_10_17_materialized_total", {}).get("public_activation") != "false":
        errors.append("summary_public_activation")
    if summary.get("candidate_10_17_materialized_total", {}).get("production_deploy") != "false":
        errors.append("summary_production_deploy")

    print("check_set=candidate_10_17_materialized_unit_ledger_v1")
    print("origin_count=" + str(len(folder_counts)))
    print("combined_unit_rows=" + str(len(rows)))
    print("split_unit_rows=" + str(len(split_rows)))
    print("public_activation=false")
    print("production_deploy=false")
    if errors:
        print("\n".join(errors[:60]))
        print("candidate_10_17_materialized_unit_ledger_pass=false")
        return 1
    print("candidate_10_17_materialized_unit_ledger_pass=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
