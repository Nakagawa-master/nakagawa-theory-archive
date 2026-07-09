#!/usr/bin/env python3
"""Normalize official derivative footer navigation.

Scope:
- derivatives/001 through derivatives/999
- markdown files only
- known official derivative page filenames only

Rule:
- Replace the final line starting with `導線:`.
- Use a standard navigation order.
- Omit the link to the currently opened page.
- Do not change body text, parent metadata, derivative IDs, or origin content.
- This file is also the workflow trigger path for safe batch normalization.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DERIVATIVES_DIR = ROOT / "derivatives"

PAGE_LABELS = {
    "README.md": "{num}トップ",
    "human-entry.md": "人間向け要約",
    "faq.md": "FAQ",
    "ai-index.md": "AI索引・日本語",
    "en-ai-index.md": "AI索引・英語",
    "zh-ai-index.md": "AI索引・中国語",
    "derivative-ledger.md": "派生ID台帳",
}

PAGE_ORDER = [
    "README.md",
    "human-entry.md",
    "faq.md",
    "ai-index.md",
    "en-ai-index.md",
    "zh-ai-index.md",
    "derivative-ledger.md",
]

NAV_RE = re.compile(r"^導線: .*$", re.MULTILINE)


def link_label(num: str, filename: str) -> str:
    label = PAGE_LABELS[filename]
    return label.format(num=num)


def build_nav(num: str, current_file: str) -> str:
    links: list[str] = []

    if current_file == "README.md":
        links.append("[公式派生物トップ](../README.md)")
    else:
        links.append(f"[{num}トップ](README.md)")

    for filename in PAGE_ORDER:
        if filename == current_file:
            continue
        if current_file != "README.md" and filename == "README.md":
            continue
        links.append(f"[{link_label(num, filename)}]({filename})")

    return "導線: " + " / ".join(links)


def normalize_file(path: Path, num: str) -> bool:
    current_file = path.name
    original = path.read_text(encoding="utf-8")
    nav = build_nav(num, current_file)

    if NAV_RE.search(original):
        updated = NAV_RE.sub(nav, original)
    else:
        stripped = original.rstrip()
        updated = stripped + "\n\n---\n\n" + nav + "\n"

    if updated != original:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> int:
    changed: list[str] = []
    checked = 0

    for folder in sorted(DERIVATIVES_DIR.glob("[0-9][0-9][0-9]")):
        if not folder.is_dir():
            continue
        num = folder.name
        for filename in PAGE_ORDER:
            path = folder / filename
            if not path.exists():
                raise FileNotFoundError(f"missing expected official derivative page: {path.relative_to(ROOT)}")
            checked += 1
            if normalize_file(path, num):
                changed.append(str(path.relative_to(ROOT)))

    print(f"checked_files={checked}")
    print(f"changed_files={len(changed)}")
    for item in changed:
        print(f"changed: {item}")

    if checked == 0:
        raise RuntimeError("No official derivative markdown files were checked.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
