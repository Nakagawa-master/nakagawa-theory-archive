#!/usr/bin/env python3
"""Validate that the numbered public-impact cases precede the final conclusions.

Run before proposing or merging a change to the three REAL_WORLD_IMPACT pages.
This is a local, read-only check; it does not start GitHub Actions.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASE_HEADING = re.compile(r"^## ([1-9][0-9]*)[.] ", re.MULTILINE)

PAGES = {
    "REAL_WORLD_IMPACT.md": (
        "## このページから言えること／言えないこと",
        "## 自分で確認する方法",
        "## 関連する公開資料",
    ),
    "REAL_WORLD_IMPACT.en.md": (
        "## What this page supports — and what it does not",
        "## How to verify a case yourself",
        "## Related public material",
    ),
    "REAL_WORLD_IMPACT.zh.md": (
        "## 本页可以支持什么结论，以及不能支持什么结论",
        "## 怎样自行核验一个案例",
        "## 相关公开资料",
    ),
}


# The reader's first-screen count must change whenever the numbered cases change.
# Keep these bound to the three public introductions, not to an internal changelog.
FIRST_SCREEN_COUNTS = {
    "REAL_WORLD_IMPACT.md": r"^\*\*公開記録([0-9]+)件。\*\*",
    "REAL_WORLD_IMPACT.en.md": r"^\*\*([0-9]+) publicly documented cases\.\*\*",
    "REAL_WORLD_IMPACT.zh.md": r"^\*\*([0-9]+)项有公开记录的案例。\*\*",
}


def inspect_page(path: Path, footer_titles: tuple[str, ...]) -> int:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    headers = [(i, line) for i, line in enumerate(lines) if line.startswith("## ")]
    numbered = [
        (i, int(match.group(1)))
        for i, line in enumerate(lines)
        if (match := CASE_HEADING.match(line))
    ]
    nums = [n for _, n in numbered]
    if not nums or nums != list(range(1, len(nums) + 1)):
        raise ValueError(f"{path.name}: case numbering must be consecutive from 1 (got {nums})")

    footer_at = []
    for title in footer_titles:
        positions = [i for i, line in headers if line == title]
        if len(positions) != 1:
            raise ValueError(f"{path.name}: required closing heading must occur once: {title}")
        footer_at.append(positions[0])

    if not (numbered[-1][0] < footer_at[0] < footer_at[1] < footer_at[2]):
        raise ValueError(f"{path.name}: closing sections must follow the final numbered case")
    if any(i > footer_at[2] for i, _ in headers):
        raise ValueError(f"{path.name}: no ## section may appear after Related public material")

    return len(nums)


def main() -> int:
    try:
        counts = {
            filename: inspect_page(ROOT / filename, footers)
            for filename, footers in PAGES.items()
        }
        unique = set(counts.values())
        if len(unique) != 1:
            raise ValueError(f"language counts differ: {counts}")
        count = unique.pop()

        # A case-count increase must also update the immediately visible number
        # on every language page; the deeper JA overview and README are separate.
        for filename, first_screen_pattern in FIRST_SCREEN_COUNTS.items():
            intro = "\n".join(
                (ROOT / filename).read_text(encoding="utf-8").splitlines()[:8]
            )
            matches = list(re.finditer(first_screen_pattern, intro, re.MULTILINE))
            if len(matches) != 1 or int(matches[0].group(1)) != count:
                raise ValueError(
                    f"{filename}: first-screen case count must equal numbered cases ({count})"
                )

        ja = (ROOT / "REAL_WORLD_IMPACT.md").read_text(encoding="utf-8")
        snapshot = re.search(r"[*][*]([0-9]+)の番号付き外部作用事例[*][*]", ja)
        if not snapshot or int(snapshot.group(1)) != count:
            raise ValueError("Japanese overview case count differs from numbered headings")

        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        mentioned = re.search(r"には現在([0-9]+)の番号付き事例セクション", readme)
        if not mentioned or int(mentioned.group(1)) != count:
            raise ValueError("README case count differs from the three impact pages")

        # The same README paragraph also contains a human-facing caveat such as
        # "46件すべてが採用・リリース・運用まで進んだという意味ではありません".
        # Check that numerical statement too: otherwise a case-47 proposal can
        # pass this validator while still displaying 47 and 46 together.
        caveat_counts = [
            int(number)
            for number in re.findall(
                r"(?<![0-9])([0-9]+)件すべてが採用・リリース・運用まで進んだという意味ではありません",
                readme,
            )
        ]
        if any(number != count for number in caveat_counts):
            raise ValueError("README adoption caveat count differs from numbered impact cases")
    except (OSError, ValueError) as exc:
        print(f"Impact index order FAILED: {exc}", file=sys.stderr)
        return 1

    print(f"Impact index order PASS: 1–{count}, three languages, conclusions last, README aligned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
