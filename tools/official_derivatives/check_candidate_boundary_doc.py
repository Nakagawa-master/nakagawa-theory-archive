#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "tools" / "official_derivatives" / "release_candidate_boundary.md"

REQUIRED = [
    "staged origins: 13",
    "staged pages: 78",
    "staged registry rows: 78",
    "materialized effect units: 429",
    "release state: staged only",
    "Official derivative generation check",
    "Official derivative preflight check",
    "entry signal check",
    "production deploy",
    "FTP action",
    "sitemap update",
    "Search Console action",
]


def main() -> int:
    if not DOC.exists():
        print("candidate_boundary_doc_exists=false")
        return 1
    text = DOC.read_text(encoding="utf-8")
    missing = [item for item in REQUIRED if item not in text]
    print("check_set=candidate_boundary_doc_v1")
    if missing:
        for item in missing:
            print(f"missing={item}")
        print("candidate_boundary_doc_pass=false")
        return 1
    print("candidate_boundary_doc_pass=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
