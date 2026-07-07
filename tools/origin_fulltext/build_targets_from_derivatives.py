#!/usr/bin/env python3
"""Expand origin-fulltext targets from existing official derivative files.

This script scans derivatives/*/README.md and extracts parent origin metadata.
It preserves manually listed incident targets, then adds parent origins from all
published derivatives. This makes the AI-readable fulltext mirror follow the
public derivative set without owner hand-carrying.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[2]
DERIVATIVES = ROOT / "derivatives"
TARGETS = ROOT / "origin-fulltext" / "origin-fulltext-targets.json"


def slug_from_url(url: str) -> str:
    return url.rstrip("/").split("/")[-1]


def extract(patterns: List[str], text: str) -> str:
    for pattern in patterns:
        m = re.search(pattern, text, flags=re.M)
        if m:
            return m.group(1).strip()
    return ""


def target_from_readme(num: str, readme: Path) -> Dict[str, str] | None:
    text = readme.read_text(encoding="utf-8", errors="ignore")
    url = extract([
        r"Parent URL[:：]\s*(https?://\S+)",
        r"親原典URL[:：]\s*(https?://\S+)",
        r"- Parent URL[:：]\s*(https?://\S+)",
    ], text)
    if not url:
        return None
    title = extract([
        r"- タイトル[:：]\s*(.+)",
        r"Parent title[:：]\s*(.+)",
        r"タイトル[:：]\s*(.+)",
    ], text) or f"Official Derivative {num} parent"
    ncl = extract([r"Parent NCL-ID[:：]\s*(\S+)", r"親NCL-ID[:：]\s*(\S+)"], text)
    diff = extract([r"Parent Diff-ID[:：]\s*(\S+)", r"親Diff-ID[:：]\s*(\S+)"], text)
    slug = slug_from_url(url)
    return {
        "slug": slug,
        "title": title,
        "canonical_url": url,
        "priority": f"official_derivative_parent_{num}",
        "status": "candidate_for_fulltext_mirror",
        "parent_ncl_id_hint": ncl,
        "parent_diff_id_hint": diff,
    }


def main() -> int:
    existing: List[Dict[str, str]] = []
    if TARGETS.exists():
        existing = json.loads(TARGETS.read_text(encoding="utf-8"))
    by_slug: Dict[str, Dict[str, str]] = {item.get("slug", ""): item for item in existing if item.get("slug")}
    for path in sorted(DERIVATIVES.glob("[0-9][0-9][0-9]/README.md")):
        num = path.parent.name
        target = target_from_readme(num, path)
        if not target:
            continue
        if target["slug"] not in by_slug:
            by_slug[target["slug"]] = target
        else:
            merged = dict(by_slug[target["slug"]])
            merged.update({k: v for k, v in target.items() if v})
            by_slug[target["slug"]] = merged
    out = sorted(by_slug.values(), key=lambda x: (x.get("priority", ""), x.get("slug", "")))
    TARGETS.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(out)} targets to {TARGETS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
