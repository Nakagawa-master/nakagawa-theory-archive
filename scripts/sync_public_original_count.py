#!/usr/bin/env python3
"""Synchronize reader-visible original counts from the ONE official derivatives map.

README.md and the human introduction display generated text, not Markdown variables.
When the map is extended, the GitHub Actions workflow regenerates both. New
WordPress-only posts are NOT counted until registered in the official map.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT / "derivatives" / "official-derivatives-map.json"
PAGES = {
    ROOT / "README.md": "derivatives/",
    ROOT / "human-translation" / "who-is-nakagawa-master.md": "../derivatives/",
}
BEGIN = "<!-- BEGIN AUTO:OFFICIAL_ORIGINAL_COUNT -->"
END = "<!-- END AUTO:OFFICIAL_ORIGINAL_COUNT -->"


def get_count_and_last() -> tuple[int, int]:
    entries = json.loads(MAP.read_text(encoding="utf-8"))["entries"]
    numbers = sorted(int(row["number"]) for row in entries)
    if not numbers or numbers != list(range(1, len(entries) + 1)):
        raise ValueError("Official original numbers are missing, duplicated, or noncontiguous")
    for entry in entries:
        if entry.get("status") != "active" or not entry.get("canonical_parent_url"):
            raise ValueError("Map includes inactive original or lacks a canonical Parent URL")
    return len(entries), numbers[-1]


def generated(count: int, last: int, derivative_link: str) -> str:
    return (
        f"{BEGIN}\n"
        f"**公開原典：{count}件。** [原典の正本](https://master.ricette.jp/) ／ "
        f"[公式派生物 OD001〜OD{last:03d}]({derivative_link})\n"
        f"{END}"
    )


def update_content(original: str, replacement: str) -> str:
    if original.count(BEGIN) != 1 or original.count(END) != 1:
        raise ValueError("Missing or duplicate original-count marker")
    pattern = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.DOTALL)
    new, n = pattern.subn(lambda _match: replacement, original)
    if n != 1:
        raise ValueError("Unexpected generated-block replacement count")
    return new


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if generated counts are stale")
    args = parser.parse_args()
    count, last = get_count_and_last()
    pending = []
    for path, link in PAGES.items():
        before = path.read_text(encoding="utf-8")
        after = update_content(before, generated(count, last, link))
        if before != after:
            pending.append(path)
            if not args.check:
                path.write_text(after, encoding="utf-8")
    if pending:
        print("Stale original counts:", ", ".join(str(p.relative_to(ROOT)) for p in pending))
    else:
        print(f"Official count current: {count} originals, OD001 through OD{last:03d}")
    return int(args.check and bool(pending))


if __name__ == "__main__":
    raise SystemExit(main())
