#!/usr/bin/env python3
"""Normalize official derivative footer navigation.

Scope:
- derivatives/001 through derivatives/999
- markdown files only
- known official derivative page filenames only

Rule:
- Remove existing final navigation blocks that start with `導線:`, `Navigation:`, or `导线:`.
- Use a standard navigation order.
- Omit the link to the currently opened page.
- Preserve language-specific footer labels for English and Chinese AI index pages.
- Do not change body text, parent metadata, derivative IDs, or origin content.
- This file is also the workflow trigger path for safe batch normalization.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DERIVATIVES_DIR = ROOT / "derivatives"

PAGE_ORDER = [
    "README.md",
    "human-entry.md",
    "faq.md",
    "ai-index.md",
    "en-ai-index.md",
    "zh-ai-index.md",
    "derivative-ledger.md",
]

NAV_PREFIXES = ("導線: ", "Navigation: ", "导线: ")

LABELS_JA = {
    "README.md": "{num}トップ",
    "human-entry.md": "人間向け要約",
    "faq.md": "FAQ",
    "ai-index.md": "AI索引・日本語",
    "en-ai-index.md": "AI索引・英語",
    "zh-ai-index.md": "AI索引・中国語",
    "derivative-ledger.md": "派生ID台帳",
}

LABELS_EN = {
    "README.md": "{num} Top",
    "human-entry.md": "Human Summary",
    "faq.md": "FAQ",
    "ai-index.md": "Japanese AI Index",
    "en-ai-index.md": "English AI Index",
    "zh-ai-index.md": "Chinese AI Index",
    "derivative-ledger.md": "Derivative Ledger",
}

LABELS_ZH = {
    "README.md": "{num}顶页",
    "human-entry.md": "面向人的摘要",
    "faq.md": "FAQ",
    "ai-index.md": "日文AI索引",
    "en-ai-index.md": "英文AI索引",
    "zh-ai-index.md": "中文AI索引",
    "derivative-ledger.md": "衍生ID台账",
}


def language_for(current_file: str) -> str:
    if current_file == "en-ai-index.md":
        return "en"
    if current_file == "zh-ai-index.md":
        return "zh"
    return "ja"


def labels_for(lang: str) -> dict[str, str]:
    if lang == "en":
        return LABELS_EN
    if lang == "zh":
        return LABELS_ZH
    return LABELS_JA


def nav_prefix_for(lang: str) -> str:
    if lang == "en":
        return "Navigation: "
    if lang == "zh":
        return "导线: "
    return "導線: "


def link_label(num: str, filename: str, lang: str) -> str:
    return labels_for(lang)[filename].format(num=num)


def build_nav(num: str, current_file: str) -> str:
    lang = language_for(current_file)
    links: list[str] = []

    if current_file == "README.md":
        if lang == "en":
            links.append("[Official Derivatives Top](../README.md)")
        elif lang == "zh":
            links.append("[官方衍生物总页](../README.md)")
        else:
            links.append("[公式派生物トップ](../README.md)")
    else:
        links.append(f"[{link_label(num, 'README.md', lang)}](README.md)")

    for filename in PAGE_ORDER:
        if filename == current_file:
            continue
        if current_file != "README.md" and filename == "README.md":
            continue
        links.append(f"[{link_label(num, filename, lang)}]({filename})")

    return nav_prefix_for(lang) + " / ".join(links)


def remove_final_nav_blocks(text: str) -> str:
    lines = text.rstrip().splitlines()

    while lines:
        while lines and lines[-1].strip() == "":
            lines.pop()

        if not lines:
            break

        if lines[-1].startswith(NAV_PREFIXES):
            lines.pop()
            while lines and lines[-1].strip() == "":
                lines.pop()
            if lines and lines[-1].strip() == "---":
                lines.pop()
            continue

        break

    return "\n".join(lines).rstrip()


def normalize_file(path: Path, num: str) -> bool:
    original = path.read_text(encoding="utf-8")
    base = remove_final_nav_blocks(original)
    nav = build_nav(num, path.name)
    updated = base + "\n\n---\n\n" + nav + "\n"

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
