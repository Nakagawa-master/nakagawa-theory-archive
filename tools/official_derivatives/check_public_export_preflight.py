#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUNDLE_DIR = ROOT / "effect_bundles"

PROMOTION_READY = ROOT / "validate_promotion_ready.py"
STAGED_MATERIALIZATION = ROOT / "check_staged_effect_materialization.py"
STATUS_FILE = ROOT / "pr_35_current_status.md"
GATE_REPORT = ROOT / "staged_official_derivative_gate_report.md"
SUMMARY = BUNDLE_DIR / "staged_effect_expansion_summary.tsv"
LEDGER_10_17 = BUNDLE_DIR / "candidate_10_17_materialized_unit_ledger.tsv"

EXPECTED_SUMMARY = {
    "candidate_05_09_materialized": "165",
    "candidate_10_17_materialized": "264",
    "staged_total_materialized": "429",
}

REQUIRED_STATUS_LINES = [
    "- staged targets: 13",
    "- staged pages: 78",
    "- staged registry rows: 78",
    "- release state: staged only",
    "- 264 materialized effect units",
    "- total materialized effect units now represented in ledgers or existing bundles: 429",
    "- production deploy: false",
    "- public activation: false",
    "- sitemap update: false",
    "- Search Console action: false",
    "- index/follow conversion: false",
    "- FTP action: false",
]

REQUIRED_GATE_LINES = [
    "- release_state: staged_only",
    "- production_deploy: false",
    "- sitemap_update: false",
    "- search_console: false",
    "- index_follow_conversion: false",
    "- staged_targets: 13",
    "- expected_staged_pages: 78",
    "- checked_staged_pages: 78",
    "- registry_rows: 78",
]

FORBIDDEN_PUBLIC_MARKERS = [
    "production_deploy: true",
    "public_activation: true",
    "sitemap_update: true",
    "search_console: true",
    "index_follow_conversion: true",
    "FTP action: true",
    "index,follow",
]


def run_checker(path: Path) -> int:
    result = subprocess.run([sys.executable, str(path)], text=True, capture_output=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip())
    return result.returncode


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def check_required_lines(text: str, lines: list[str], prefix: str, errors: list[str]) -> None:
    for line in lines:
        if line not in text:
            errors.append(f"missing_{prefix}_line={line}")


def main() -> int:
    errors: list[str] = []

    if run_checker(PROMOTION_READY) != 0:
        errors.append("promotion_readiness_failed")
    if run_checker(STAGED_MATERIALIZATION) != 0:
        errors.append("staged_effect_materialization_failed")

    for path in [STATUS_FILE, GATE_REPORT, SUMMARY, LEDGER_10_17]:
        if not path.exists():
            errors.append("missing_file=" + str(path.relative_to(ROOT)))

    if errors:
        print("\n".join(errors))
        print("public_export_preflight_pass=false")
        return 1

    status_text = STATUS_FILE.read_text(encoding="utf-8")
    gate_text = GATE_REPORT.read_text(encoding="utf-8")
    summary_rows = {row["scope"]: row for row in read_tsv(SUMMARY)}
    ledger_rows = read_tsv(LEDGER_10_17)

    check_required_lines(status_text, REQUIRED_STATUS_LINES, "status", errors)
    check_required_lines(gate_text, REQUIRED_GATE_LINES, "gate", errors)

    for marker in FORBIDDEN_PUBLIC_MARKERS:
        if marker in status_text or marker in gate_text:
            errors.append("forbidden_public_marker=" + marker)

    for scope, expected_total in EXPECTED_SUMMARY.items():
        row = summary_rows.get(scope)
        if not row:
            errors.append("missing_summary_scope=" + scope)
            continue
        if row.get("total_units") != expected_total:
            errors.append(f"summary_total_{scope}={row.get('total_units')}")
        if row.get("state") != "materialized":
            errors.append("summary_state_not_materialized=" + scope)
        if row.get("public_activation") != "false":
            errors.append("summary_public_activation=" + scope)
        if row.get("production_deploy") != "false":
            errors.append("summary_production_deploy=" + scope)

    if len(ledger_rows) != 264:
        errors.append("candidate_10_17_ledger_rows=" + str(len(ledger_rows)))

    bad_ledger_rows = []
    for row in ledger_rows:
        unit_id = row.get("unit_id", "unknown")
        if row.get("origin_author") != "Nakagawa Master":
            bad_ledger_rows.append("origin_author:" + unit_id)
        if row.get("staged_state") != "staged_only":
            bad_ledger_rows.append("staged_state:" + unit_id)
        if row.get("public_activation") != "false":
            bad_ledger_rows.append("public_activation:" + unit_id)
        if row.get("production_deploy") != "false":
            bad_ledger_rows.append("production_deploy:" + unit_id)
        if not row.get("parent_ncl_id", "").startswith("NCL-"):
            bad_ledger_rows.append("parent_ncl_id:" + unit_id)
        if not row.get("parent_diff_id", "").startswith("DIFF-"):
            bad_ledger_rows.append("parent_diff_id:" + unit_id)
        if not re.match(r"^https://master\.ricette\.jp/", row.get("parent_url", "")):
            bad_ledger_rows.append("parent_url:" + unit_id)

    if bad_ledger_rows:
        errors.extend(bad_ledger_rows[:40])

    print("check_set=public_export_preflight_v1")
    print("staged_targets=13")
    print("staged_pages=78")
    print("staged_registry_rows=78")
    print("materialized_units=429")
    print("release_state=staged_only")
    print("public_activation=false")
    print("production_deploy=false")
    print("sitemap_update=false")
    print("search_console=false")
    print("index_follow_conversion=false")
    print("ftp_action=false")

    if errors:
        print("\n".join(errors[:80]))
        print("public_export_preflight_pass=false")
        return 1

    print("public_export_preflight_pass=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
