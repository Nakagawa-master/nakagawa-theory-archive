#!/usr/bin/env python3
"""Check that public official derivative files do not expose internal operations metadata.

Public derivative pages are for readers and AI entry. Internal acquisition,
workflow, mirror, and status details belong in private reports or public
fulltext manifests, not in derivative README / FAQ / AI index pages.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DERIVATIVES = ROOT / "derivatives"
REPORT = ROOT / "derivatives" / "public-derivative-leakage-report.json"

FORBIDDEN = [
    "fulltext_status",
    "audit_bundle_status",
    "source_acquisition_method",
    "origin-fulltext/articles",
    "origin-fulltext-build-report",
    "mirror:",
    "Source mirror",
    "Source gate state",
    "pending_safe_rewrite",
    "recovered source record",
    "NCL-ID and Diff-ID pending recovery",
    "workflow",
    "GitHub Actions HTML経路",
]

ALLOWLIST_FILES = {
    "derivatives/public-derivative-leakage-report.json",
}


def main() -> int:
    failures = []
    for path in sorted(DERIVATIVES.glob("[0-9][0-9][0-9]/*.md")):
        rel = path.relative_to(ROOT).as_posix()
        if rel in ALLOWLIST_FILES:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        hits = [term for term in FORBIDDEN if term in text]
        if hits:
            failures.append({"path": rel, "hits": hits})
    REPORT.write_text(json.dumps({"failures": failures}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if failures:
        print(json.dumps({"failures": failures}, ensure_ascii=False, indent=2))
        return 1
    print("public derivative leakage check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
