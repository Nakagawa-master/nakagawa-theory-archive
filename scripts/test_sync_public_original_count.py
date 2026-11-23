#!/usr/bin/env python3
"""Offline regression: a newly published Parent changes every live derived count."""
import copy
import json
from pathlib import Path

import sync_public_original_count as counts


def main():
    entries = counts.get_entries()
    n, last = counts.get_count_and_last()
    assert len(entries) == n and int(entries[-1]["number"]) == last
    source = counts.MAP
    assert source.is_file()

    nav = counts.NAVIGATION.read_text(encoding="utf-8")
    index = counts.MACHINE_INDEX.read_text(encoding="utf-8")
    assert counts.sync_navigation(nav, n, last) == nav
    assert counts.sync_machine_index(index, entries) == index
    categories = counts.CATEGORIES.read_text(encoding="utf-8")
    assert counts.sync_categories(categories, entries) == categories

    # In memory only: no new "official" post, derivative or Git commit invented.
    candidate = copy.deepcopy(entries[-1])
    candidate.update({
        "number": f"{last + 1:03d}",
        "derivative_dir": f"derivatives/{last + 1:03d}",
        "ncl_id": f"SYNTHETIC-NOT-PUBLISHED-{last + 1}",
        "origin_slug": f"synthetic-not-published-{last + 1}",
        "canonical_parent_url": f"https://master.ricette.jp/synthetic-never-published-{last + 1}/",
        "title": f"Synthetic count-regression item {last + 1}",
    })
    simulated = entries + [candidate]
    follow_nav = counts.sync_navigation(nav, n + 1, last + 1)
    new_id = f"OD{last + 1:03d}"
    assert f"[{new_id}]({last + 1:03d}/)" in follow_nav
    assert follow_nav.count(f"[{new_id}](") == 1
    assert f"OD001–{new_id}の各9面" in follow_nav
    assert f"公式派生物{n + 1}件" in follow_nav

    follow_categories = counts.sync_categories(categories, simulated)
    assert f"OD001–{new_id}を" in follow_categories
    assert f"- 割当: {n + 1}件" in follow_categories
    assert f"[{new_id}]({last + 1:03d}/)" in follow_categories
    assert f"**{n + 1}件へ迷わず到達" in follow_categories
    assert "すべての公開原典はこのページと" in follow_categories
    follow_index = json.loads(counts.sync_machine_index(index, simulated))
    assert follow_index["coverage"]["expected_count"] == n + 1
    assert follow_index["coverage"]["indexed_count"] == n + 1
    assert follow_index["coverage"]["to"] == f"{last + 1:03d}"
    assert follow_index["original_derivative_pairing"]["published_original_articles"] == n + 1
    assert follow_index["original_derivative_pairing"]["total_derivative_markdown_pages"] == (n + 1) * len(counts.FACES)
    all_assigned = [v for cat in follow_index["categories"] for v in cat["members"]]
    assert len(all_assigned) == n + 1 and len(set(all_assigned)) == n + 1
    assert f"{last + 1:03d}" in next(
        cat["members"] for cat in follow_index["categories"] if cat["id"] == "cross_domain"
    )

    # A map is the only count authority: a duplicate OD in a navigation
    # cache must be rejected, not disguised as an extra published original.
    bad = json.loads(index)
    bad["categories"][0]["members"].append(bad["categories"][0]["members"][0])
    try:
        counts.sync_machine_index(json.dumps(bad, ensure_ascii=False), entries)
    except ValueError as exc:
        assert "duplicate/stale OD" in str(exc)
    else:
        raise AssertionError("Duplicate navigation membership was accepted")

    try:
        counts.sync_navigation(nav.replace("## 全件番号順", "## STALE"), n, last)
    except ValueError as exc:
        assert "numbered OD directory" in str(exc)
    else:
        raise AssertionError("Missing navigation section went unnoticed")

    print(f"PASS: one verified source: {n} published Parents; synthetic {n+1} propagates to full and thematic navigation, all machine counts and category coverage, with zero file writes")


if __name__ == "__main__":
    main()
