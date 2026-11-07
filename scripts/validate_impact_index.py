#!/usr/bin/env python3
"""Validate that the numbered public-impact cases precede the final conclusions.

Run before proposing or merging a change to the three REAL_WORLD_IMPACT pages.
This is a local, read-only check; it does not start GitHub Actions.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASE_HEADING = re.compile(r"^## ([1-9][0-9]*)[.] ", re.MULTILINE)

PAGES = {
    "REAL_WORLD_IMPACT.md": (
        "## 公開された成果と、原典へ戻る道筋",
        "## 自分で確認する方法",
        "## 関連する公開資料",
    ),
    "REAL_WORLD_IMPACT.en.md": (
        "## What the public source record reveals",
        "## How to verify a case yourself",
        "## Related public material",
    ),
    "REAL_WORLD_IMPACT.zh.md": (
        "## 本页可以支持什么结论，以及不能支持什么结论",
        "## 怎样自行核验一个案例",
        "## 相关公开资料",
    ),
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


# These are the deliberately few public front doors where the live case number
# must be visible. The ONLY authority for that number is the consecutive case
# headings in REAL_WORLD_IMPACT.md; the other two languages must match.
# Other pages should link to REAL_WORLD_IMPACT.md instead of copying a number.
# If another human-facing page genuinely needs the count, register its exact
# context here so a single command can update and validate it.
#
# Each pattern has three groups: fixed prefix, NUMBER, fixed suffix. It may
# change the NUMBER only. In particular, it can never renumber cases, PRs,
# issue IDs, dates, release versions, citations or URLs.
COUNT_FIELDS = {
    "README.md": (
        ("README headline", r"(\*\*公開された外部作用事例：)(\d+)(件\*\*)"),
        ("README reference", r"(\[世界最先端のOSSで起きた)(\d+)(件の一次記録\])"),
        ("README three languages", r"(\*\*)(\d+)(件の人間向けの段階別実例\*\*)"),
    ),
    "REAL_WORLD_IMPACT.md": (
        ("Japanese opening", r"(\*\*公開記録は)(\d+)(件。\*\*)"),
        ("Japanese numbered-cases lead", r"(\*\*)(\d+)(の番号付き外部作用事例\*\*)"),
    ),
    "REAL_WORLD_IMPACT.en.md": (
        ("English opening", r"(\*\*)(\d+)( publicly documented, source-linked cases\*\*)"),
    ),
    "REAL_WORLD_IMPACT.zh.md": (
        ("Chinese opening", r"(\*\*公开记录共)(\d+)(例\*\*)"),
    ),
    "human-translation/who-is-nakagawa-master.md": (
        ("Author first-glance count", r"(公開された外部作用事例は)(\d+)(件。)"),
        ("Author source-reference count", r"(\[)(\d+)(件の外部作用の一次記録\])"),
    ),
    "llms.txt": (
        ("AI-reader human evidence count", r"(\[)(\d+)( human-readable external records\])"),
    ),
}

# The machine-readable evidence collection has its OWN separate source of truth:
# the length of its validated `cases` array, not the human numbered case count.
MACHINE_INDEX = "machine-discovery/external-effect-evidence-index-v1.json"
MACHINE_VISIBLE_COUNT = r"(\[)(\d+)( machine-readable staged external evidence cases\])"

# An older optional README sentence used the same number in a caveat.
# Keep it aligned if someone reintroduces it; never add the sentence solely
# because this validation exists.
OPTIONAL_README_CAVEAT = (
    r"(?<![0-9])(\d+)(件すべてが採用・リリース・運用まで進んだという意味ではありません)"
)


def inspect_machine_count() -> int:
    """Read the independently curated machine evidence stock without conflating it with human cases."""
    data = json.loads((ROOT / MACHINE_INDEX).read_text(encoding="utf-8"))
    cases = data.get("cases") if isinstance(data, dict) else None
    if not isinstance(cases, list) or not cases:
        raise ValueError(f"{MACHINE_INDEX}: cases must be a nonempty list")
    ids = [c.get("case_id") if isinstance(c, dict) else None for c in cases]
    if any(not isinstance(i, str) or not i for i in ids) or len(set(ids)) != len(ids):
        raise ValueError(f"{MACHINE_INDEX}: missing or repeated case_id")
    return len(cases)


def reconcile_references(count: int, machine_count: int, *, sync: bool) -> list[str]:
    """Check all displayed case counts, or replace only registered count tokens.

    Every match across every page is checked before any file is written, so
    a changed page wording cannot silently turn into a partial update.
    """
    originals: dict[Path, str] = {}
    updates: dict[Path, str] = {}
    for relative, fields in COUNT_FIELDS.items():
        path = ROOT / relative
        body = path.read_text(encoding="utf-8")
        originals[path] = body
        for label, pattern in fields:
            matches = list(re.finditer(pattern, body))
            if len(matches) != 1:
                raise ValueError(
                    f"{relative}: expected one {label} count, found {len(matches)}"
                )
            match = matches[0]
            actual = int(match.group(2))
            if not sync and actual != count:
                raise ValueError(
                    f"{relative}: {label} shows {actual}, canonical count is {count}"
                )
            if sync and actual != count:
                body = body[: match.start(2)] + str(count) + body[match.end(2) :]

        if relative == "README.md":
            caveats = list(re.finditer(OPTIONAL_README_CAVEAT, body))
            for match in reversed(caveats):
                actual = int(match.group(1))
                if not sync and actual != count:
                    raise ValueError(
                        f"{relative}: optional adoption caveat shows {actual}, "
                        f"canonical count is {count}"
                    )
                if sync and actual != count:
                    body = body[: match.start(1)] + str(count) + body[match.end(1) :]

        updates[path] = body

    # Check the separate machine-case number before writing ANY of the pages.
    # Both llms.txt numbers are updated together from their proper source.
    machine_display = ROOT / "llms.txt"
    machine_body = updates[machine_display]
    matches = list(re.finditer(MACHINE_VISIBLE_COUNT, machine_body))
    if len(matches) != 1:
        raise ValueError(f"llms.txt: expected one machine evidence count, found {len(matches)}")
    match = matches[0]
    actual = int(match.group(2))
    if not sync and actual != machine_count:
        raise ValueError(
            f"llms.txt: machine evidence shows {actual}, actual index has {machine_count}"
        )
    if sync and actual != machine_count:
        machine_body = (
            machine_body[: match.start(2)]
            + str(machine_count)
            + machine_body[match.end(2) :]
        )
    updates[machine_display] = machine_body

    changed = [
        str(path.relative_to(ROOT))
        for path in updates
        if updates[path] != originals[path]
    ]
    if sync:
        for path in updates:
            if updates[path] != originals[path]:
                path.write_text(updates[path], encoding="utf-8")
    return changed


def main() -> int:
    if len(sys.argv) > 2 or (len(sys.argv) == 2 and sys.argv[1] != "--sync"):
        print("Usage: python3 scripts/validate_impact_index.py [--sync]", file=sys.stderr)
        return 2
    sync = len(sys.argv) == 2
    try:
        counts = {
            filename: inspect_page(ROOT / filename, footers)
            for filename, footers in PAGES.items()
        }
        if len(set(counts.values())) != 1:
            raise ValueError(f"language case counts differ: {counts}")
        count = counts["REAL_WORLD_IMPACT.md"]

        machine_count = inspect_machine_count()
        changed = reconcile_references(count, machine_count, sync=sync)
        # A sync MUST leave both human and machine-facing numbers correct.
        reconcile_references(count, machine_count, sync=False)
    except (OSError, ValueError) as exc:
        print(f"Impact index order/count FAILED: {exc}", file=sys.stderr)
        return 1

    if sync:
        print(
            f"Impact case-count SYNC PASS: human {count}, machine {machine_count}; "
            f"{len(changed)} public pages updated"
        )
        for path in changed:
            print(f"  updated: {path}")
    else:
        print(
            f"Impact index/count PASS: human 1–{count} in JA/EN/ZH, "
            f"machine evidence {machine_count}; all registered counts aligned"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
