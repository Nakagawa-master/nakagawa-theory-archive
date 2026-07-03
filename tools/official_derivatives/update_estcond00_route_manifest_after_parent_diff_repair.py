#!/usr/bin/env python3
"""Update ESTCOND00 route package manifest after parent Diff repair."""

from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path("deploy/lolipop/master-ricette/derivatives/ultra-quality/establishment-conditions-00")
MANIFEST = Path("tools/official_derivatives/estcond00_route_package_manifest.tsv")
PARENT_NCL = "NCL-α-20260627-aea14a"
PARENT_DIFF = "DIFF-20260627-0002"
DERIVATIVE_NCL = "NCL-DER-20260704-estcond00-0001"
DERIVATIVE_DIFF = "DIFF-DER-20260704-0001"
ROWS = [
    (ROOT / "index.html", "https://master.ricette.jp/derivatives/ultra-quality/establishment-conditions-00/"),
    (ROOT / "human-summary" / "index.html", "https://master.ricette.jp/derivatives/ultra-quality/establishment-conditions-00/human-summary/"),
    (ROOT / "faq" / "index.html", "https://master.ricette.jp/derivatives/ultra-quality/establishment-conditions-00/faq/"),
    (ROOT / "ai-index" / "index.html", "https://master.ricette.jp/derivatives/ultra-quality/establishment-conditions-00/ai-index/"),
    (ROOT / "boundary" / "index.html", "https://master.ricette.jp/derivatives/ultra-quality/establishment-conditions-00/boundary/"),
    (ROOT / "application" / "index.html", "https://master.ricette.jp/derivatives/ultra-quality/establishment-conditions-00/application/"),
    (ROOT / "origin" / "index.html", "https://master.ricette.jp/derivatives/ultra-quality/establishment-conditions-00/origin/"),
]


def blob_sha(path: Path) -> str:
    result = subprocess.run(["git", "hash-object", str(path)], check=True, capture_output=True, text=True)
    return result.stdout.strip()


def main() -> int:
    lines = ["target_path\tcanonical\tparent_ncl_id\tactual_parent_diff_id\tderivative_ncl_id\tderivative_diff_id\tcurrent_blob_sha\treconciliation_status"]
    for path, canonical in ROWS:
        if not path.exists():
            raise SystemExit(f"missing_file={path}")
        text = path.read_text(encoding="utf-8")
        for required in (PARENT_NCL, PARENT_DIFF, DERIVATIVE_NCL, DERIVATIVE_DIFF):
            if required not in text:
                raise SystemExit(f"missing_required={required} path={path}")
        if "DIFF-20260630-0003" in text:
            raise SystemExit(f"stale_parent_diff_remaining={path}")
        lines.append("\t".join([str(path), canonical, PARENT_NCL, PARENT_DIFF, DERIVATIVE_NCL, DERIVATIVE_DIFF, blob_sha(path), "aligned_to_live_origin"]))
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"manifest_update_status=ok rows={len(ROWS)} path={MANIFEST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
