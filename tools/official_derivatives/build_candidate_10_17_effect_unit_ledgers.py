#!/usr/bin/env python3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUNDLE_DIR = ROOT / "effect_bundles"

QUEUE = ROOT / "next_10_queue_candidate_10_19.tsv"
EXPECTED = BUNDLE_DIR / "candidate_10_17_effect_bundle_expected_counts.tsv"

COMBINED = BUNDLE_DIR / "candidate_10_17_materialized_unit_ledger.tsv"
SPLIT_PATHS = {
    "quote": BUNDLE_DIR / "candidate_10_17_materialized_quote_units.tsv",
    "social": BUNDLE_DIR / "candidate_10_17_materialized_social_units.tsv",
    "clarification": BUNDLE_DIR / "candidate_10_17_materialized_clarification_units.tsv",
    "notebooklm": BUNDLE_DIR / "candidate_10_17_materialized_notebooklm_units.tsv",
}
SUMMARY = BUNDLE_DIR / "candidate_10_17_materialized_unit_summary.tsv"

UNIT_COUNT_FIELDS = {
    "quote": "quote_units",
    "social": "social_units",
    "clarification": "objection_or_clarification_units",
    "notebooklm": "notebooklm_units",
}

FIELDNAMES = [
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


def write_tsv(path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def make_unit_rows(queue_row, expected_row):
    rows = []
    boundary_note = (
        "staged only; no public activation; no FTP action; "
        "no sitemap action; no Search Console action; no index/follow conversion"
    )
    for unit_type, count_field in UNIT_COUNT_FIELDS.items():
        count = int(expected_row[count_field])
        for index in range(1, count + 1):
            rows.append({
                "batch_id": queue_row["batch_id"],
                "slot_id": queue_row["slot_id"],
                "folder_id": queue_row["folder_id"],
                "unit_type": unit_type,
                "unit_id": f"{queue_row['folder_id']}-{unit_type}-{index:02d}",
                "unit_index": str(index),
                "language": "ja",
                "parent_url": queue_row["parent_url"],
                "parent_title": queue_row["parent_title"],
                "parent_ncl_id": queue_row["parent_ncl_id"],
                "parent_diff_id": queue_row["parent_diff_id"],
                "canonical_url": queue_row["canonical_url"],
                "origin_author": "Nakagawa Master",
                "causal_line": queue_row["reason_for_inclusion"],
                "boundary_note": boundary_note,
                "misreading_guard": queue_row["risk_note"],
                "staged_state": "staged_only",
                "public_activation": "false",
                "production_deploy": "false",
            })
    return rows


def main():
    queue = [
        row for row in read_tsv(QUEUE)
        if row.get("selection_status") == "selected" and row.get("handoff_status") == "intake_ready"
    ]
    expected_by_folder = {row["folder_id"]: row for row in read_tsv(EXPECTED)}

    rows = []
    for queue_row in queue:
        folder_id = queue_row["folder_id"]
        expected_row = expected_by_folder.get(folder_id)
        if expected_row is None:
            raise SystemExit(f"missing expected count row for {folder_id}")
        rows.extend(make_unit_rows(queue_row, expected_row))

    write_tsv(COMBINED, rows, FIELDNAMES)

    for unit_type, path in SPLIT_PATHS.items():
        write_tsv(path, [row for row in rows if row["unit_type"] == unit_type], FIELDNAMES)

    summary_rows = []
    for unit_type, path in SPLIT_PATHS.items():
        unit_rows = [row for row in rows if row["unit_type"] == unit_type]
        summary_rows.append({
            "scope": f"candidate_10_17_{unit_type}",
            "origin_count": str(len({row["folder_id"] for row in unit_rows})),
            "unit_type": unit_type,
            "unit_count": str(len(unit_rows)),
            "state": "materialized",
            "public_activation": "false",
            "production_deploy": "false",
        })
    summary_rows.append({
        "scope": "candidate_10_17_materialized_total",
        "origin_count": str(len({row["folder_id"] for row in rows})),
        "unit_type": "all",
        "unit_count": str(len(rows)),
        "state": "materialized",
        "public_activation": "false",
        "production_deploy": "false",
    })
    write_tsv(
        SUMMARY,
        summary_rows,
        ["scope", "origin_count", "unit_type", "unit_count", "state", "public_activation", "production_deploy"],
    )

    print("candidate_10_17_materialized_unit_builder=ok")
    print(f"origin_count={len({row['folder_id'] for row in rows})}")
    print(f"materialized_unit_rows={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
