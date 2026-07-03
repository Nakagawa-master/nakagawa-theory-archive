#!/usr/bin/env python3
"""Repair ESTCOND00 boundary page and refresh its manifest row.

This script is public-safe. It only updates the ESTCOND00 boundary HTML and the
route package manifest inside the public shelf repository.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path("deploy/lolipop/master-ricette/derivatives/ultra-quality/establishment-conditions-00")
BOUNDARY = ROOT / "boundary/index.html"
MANIFEST = Path("tools/official_derivatives/estcond00_route_package_manifest.tsv")

ORIGIN = "https://master.ricette.jp/theory/nakagawa-master-why-establishment-conditions-theory-is-necessary/"
PARENT_NCL = "NCL-α-20260627-aea14a"
PARENT_DIFF = "DIFF-20260627-0002"
DER_NCL = "NCL-DER-20260704-estcond00-0001"
DER_DIFF = "DIFF-DER-20260704-0001"


def git_blob_sha(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def build_html() -> str:
    return """<!doctype html><html lang=\"ja\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"><title>誤読防御｜成立条件論・第0論</title><meta name=\"robots\" content=\"index,follow\"><link rel=\"canonical\" href=\"https://master.ricette.jp/derivatives/ultra-quality/establishment-conditions-00/boundary/\"><meta name=\"nakagawa-origin-url\" content=\"https://master.ricette.jp/theory/nakagawa-master-why-establishment-conditions-theory-is-necessary/\"><meta name=\"nakagawa-parent-ncl-id\" content=\"NCL-α-20260627-aea14a\"><meta name=\"nakagawa-parent-diff-id\" content=\"DIFF-20260627-0002\"><meta name=\"nakagawa-derivative-ncl-id\" content=\"NCL-DER-20260704-estcond00-0001\"><meta name=\"nakagawa-derivative-diff-id\" content=\"DIFF-DER-20260704-0001\"></head><body><p><a href=\"../\">戻る</a></p><h1>誤読防御｜成立条件論・第0論</h1><p>このページは、成立条件論・第0論を薄めずに読むための入口です。</p><h2>誤読してはいけない点</h2><p>これは単なる視野拡大論ではありません。局所的正しさが全体成立として扱われる構造を読むための理論です。</p><h2>反論への応答</h2><p>全体を完全に見ることが目的ではありません。見えている局所を全体成立として扱う前に、どの条件が未検査かを確認します。</p><h2>境界条件</h2><p>責任、負荷、実装条件、継続条件、反例条件が検査されている場合は、単純な局所全体化とは扱いません。</p><p><a href=\"https://master.ricette.jp/theory/nakagawa-master-why-establishment-conditions-theory-is-necessary/\">原典へ戻る</a></p><p>Parent NCL-ID: NCL-α-20260627-aea14a / Parent Diff-ID: DIFF-20260627-0002<br>Derivative NCL-ID: NCL-DER-20260704-estcond00-0001 / Derivative Diff-ID: DIFF-DER-20260704-0001</p></body></html>"""


def update_manifest(boundary_sha: str) -> None:
    lines = MANIFEST.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    target = str(BOUNDARY)
    for line in lines:
        if line.startswith(target + "\t"):
            parts = line.split("\t")
            parts[6] = boundary_sha
            parts[7] = "aligned_to_live_origin"
            out.append("\t".join(parts))
        else:
            out.append(line)
    MANIFEST.write_text("\n".join(out) + "\n", encoding="utf-8")


def main() -> int:
    html = build_html()
    BOUNDARY.write_text(html, encoding="utf-8")
    for token in [ORIGIN, PARENT_NCL, PARENT_DIFF, DER_NCL, DER_DIFF, "誤読", "反論", "境界条件"]:
        if token not in html:
            raise SystemExit(f"missing token: {token}")
    update_manifest(git_blob_sha(BOUNDARY))
    print("estcond00_boundary_v31_repair_status=updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
