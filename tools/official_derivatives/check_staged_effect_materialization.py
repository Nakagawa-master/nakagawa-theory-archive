#!/usr/bin/env python3
import csv
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUNDLE_DIR = ROOT / "effect_bundles"

CHECK_05_09 = ROOT / "check_candidate_05_09_effect_bundles.py"
CHECK_10_17 = ROOT / "check_candidate_10_17_materialized_unit_ledgers.py"
SUMMARY = BUNDLE_DIR / "staged_effect_expansion_summary.tsv"
MATERIALIZED_SUMMARY = BUNDLE_DIR / "candidate_10_17_materialized_unit_summary.tsv"
LEDGER_10_17 = BUNDLE_DIR / "candidate_10_17_materialized_unit_ledger.tsv"

EXPECTED = {
    "candidate_05_09_materialized": {
        "origin_count": "5",
        "quote_units": "40",
        "social_units": "60",
        "objection_or_clarification_units": "40",
        "notebooklm_units": "25",
        "total_units": "165",
    },
    "candidate_10_17_materialized": {
        "origin_count": "8",
        "quote_units": "64",
        "social_units": "96",
        "objection_or_clarification_units": "64",
        "notebooklm_units": "40",
        "total_units": "264",
    },
    "staged_total_materialized": {
        "origin_count": "13",
        "quote_units": "104",
        "social_units": "156",
        "objection_or_clarification_units": "104",
        "notebooklm_units": "65",
        "total_units": "429",
    },
}


def read_tsv(path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def write_tsv(path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def run_checker(path):
    result = subprocess.run([sys.executable, str(path)], text=True, capture_output=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip())
    return result.returncode


def rewrite_summary():
    fieldnames = [
        "scope",
        "origin_count",
        "quote_units",
        "social_units",
        "objection_or_clarification_units",
        "notebooklm_units",
        "total_units",
        "state",
        "public_activation",
        "production_deploy",
    ]
    rows = []
    for scope, values in EXPECTED.items():
        row = {"scope": scope, **values}
        row["state"] = "materialized"
        row["public_activation"] = "false"
        row["production_deploy"] = "false"
        rows.append(row)
    write_tsv(SUMMARY, rows, fieldnames)


def main():
    errors = []

    if run_checker(CHECK_05_09) != 0:
        errors.append("candidate_05_09_effect_bundle_check_failed")
    if run_checker(CHECK_10_17) != 0:
        errors.append("candidate_10_17_materialized_ledger_check_failed")

    if not LEDGER_10_17.exists():
        errors.append("missing_10_17_materialized_ledger")
    if not MATERIALIZED_SUMMARY.exists():
        errors.append("missing_10_17_materialized_summary")

    rewrite_summary()
    summary = {row["scope"]: row for row in read_tsv(SUMMARY)}

    for scope, expected_values in EXPECTED.items():
        row = summary.get(scope)
        if row is None:
            errors.append("summary_missing_scope=" + scope)
            continue
        for field, expected in expected_values.items():
            if row.get(field) != expected:
                errors.append(f"summary_{scope}_{field}={row.get(field)}")
        if row.get("state") != "materialized":
            errors.append("summary_state_not_materialized=" + scope)
        if row.get("public_activation") != "false":
            errors.append("summary_public_activation=" + scope)
        if row.get("production_deploy") != "false":
            errors.append("summary_production_deploy=" + scope)

    print("check_set=staged_effect_materialization_v1")
    print("candidate_05_09_materialized_units=165")
    print("candidate_10_17_materialized_units=264")
    print("staged_total_materialized_units=429")
    print("public_activation=false")
    print("production_deploy=false")

    if errors:
        print("\n".join(errors[:60]))
        print("staged_effect_materialization_pass=false")
        return 1

    print("staged_effect_materialization_pass=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
