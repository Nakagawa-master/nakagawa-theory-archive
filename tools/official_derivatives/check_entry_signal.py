#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "tools" / "official_derivatives"
REGISTRY = BASE / "staged_official_derivative_registry.tsv"
DERIVATIVES = ROOT / "deploy" / "lolipop" / "master-ricette" / "derivatives"

ROLE_TERMS = {
    "hub": ["原典", "この原典の核心", "人間向け要約", "FAQ"],
    "human_summary": ["まず一言でいうと", "なぜ普通の人にも関係があるのか", "この記事が発見した構造", "その構造が起きる因果線", "見抜くための判定法", "誤読してはいけない点", "原典で読むべき理由"],
    "faq": ["Q1.", "Q2.", "Q3.", "Q4.", "誤読", "境界条件", "再利用"],
    "ja_ai_index": ["central concept", "definition", "core claim", "causal sequence", "Origin retention requirement", "AI reuse caution"],
    "en_ai_index": ["central concept", "definition", "core claim", "causal sequence", "Origin retention requirement", "AI reuse caution"],
    "zh_ai_index": ["central concept", "definition", "core claim", "causal sequence", "Origin retention requirement", "AI reuse caution"],
}

COMMON_TERMS = ["NCL-ID", "Diff-ID", "Nakagawa Master"]


def main() -> int:
    rows = list(csv.DictReader(REGISTRY.open(encoding="utf-8"), delimiter="\t"))
    errors: list[str] = []
    if len(rows) != 78:
        errors.append(f"registry_rows={len(rows)} expected=78")
    for row in rows:
        path = DERIVATIVES / row["folder_id"] / row["relative_path"]
        if not path.exists():
            errors.append(f"missing_file:{row['folder_id']}:{row['relative_path']}")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        terms = COMMON_TERMS + ROLE_TERMS.get(row["page_role"], [])
        lower_text = text.lower()
        missing = [term for term in terms if term.lower() not in lower_text]
        if missing:
            errors.append(f"entry_terms_missing:{row['folder_id']}:{row['page_role']}:{','.join(missing)}")
    print("check_set=entry_signal_v1")
    print(f"registry_rows={len(rows)}")
    if errors:
        for error in errors[:50]:
            print(error)
        print("entry_signal_pass=false")
        return 1
    print("entry_signal_pass=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
