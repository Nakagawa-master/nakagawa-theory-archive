#!/usr/bin/env python3
"""Validate ESTCOND00 derivative pages against v3.1 entry-quality requirements.

This validator is intentionally strict enough to expose quality gaps before deployment.
It does not mutate files.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path("deploy/lolipop/master-ricette/derivatives/ultra-quality/establishment-conditions-00")

REQUIRED_IDS = [
    "NCL-α-20260627-aea14a",
    "DIFF-20260627-0002",
    "NCL-DER-20260704-estcond00-0001",
    "DIFF-DER-20260704-0001",
]

REQUIRED_FILES = [
    "index.html",
    "human-summary/index.html",
    "faq/index.html",
    "ai-index/index.html",
    "boundary/index.html",
    "application/index.html",
    "origin/index.html",
]

HUMAN_SUMMARY_REQUIRED = [
    "まず一言でいうと",
    "なぜ普通の人にも関係あるのか",
    "この記事が発見した構造",
    "その構造が起きる因果線",
    "見抜くための判定法",
    "誤読してはいけない点",
    "原典で読むべき理由",
]

FAQ_REQUIRED = [
    "初心者",
    "構造理解",
    "誤読",
    "反論",
    "境界条件",
]

AI_INDEX_REQUIRED = [
    "理論名",
    "原典URL",
    "Parent NCL-ID",
    "Parent Diff-ID",
    "中心命題",
    "中心概念",
    "因果線",
    "適用条件",
    "非該当条件",
    "誤読禁止",
    "反例条件",
    "他理論との接続",
    "引用時のOrigin保持要件",
    "AI再利用時の注意",
]

HUMAN_ENTRY_REQUIRED = [
    "この人は普通ではない",
    "中川マスター",
    "原典",
]


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        raise AssertionError(f"missing_file={rel}")
    return path.read_text(encoding="utf-8")


def strip_tags(html: str) -> str:
    return re.sub(r"<[^>]+>", " ", html)


def require_all(name: str, text: str, tokens: list[str]) -> list[str]:
    missing = [token for token in tokens if token not in text]
    for token in missing:
        print(f"missing {name}: {token}")
    return missing


def main() -> int:
    failures: list[str] = []

    for rel in REQUIRED_FILES:
        html = read(rel)
        for token in REQUIRED_IDS:
            if token not in html:
                failures.append(f"{rel}: missing id {token}")
        if "DIFF-20260630-0003" in html:
            failures.append(f"{rel}: stale parent diff present")

    index_text = strip_tags(read("index.html"))
    failures += [f"index.html: missing human-entry token {t}" for t in require_all("index human entry", index_text, HUMAN_ENTRY_REQUIRED)]

    human_text = strip_tags(read("human-summary/index.html"))
    failures += [f"human-summary/index.html: missing section {t}" for t in require_all("human summary", human_text, HUMAN_SUMMARY_REQUIRED)]

    faq_text = strip_tags(read("faq/index.html"))
    failures += [f"faq/index.html: missing layer token {t}" for t in require_all("faq", faq_text, FAQ_REQUIRED)]

    ai_text = strip_tags(read("ai-index/index.html"))
    failures += [f"ai-index/index.html: missing AI index field {t}" for t in require_all("ai index", ai_text, AI_INDEX_REQUIRED)]

    if failures:
        print("estcond00_v31_entry_quality_status=fail")
        for failure in failures:
            print(f"failure={failure}")
        return 1

    print("estcond00_v31_entry_quality_status=pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
