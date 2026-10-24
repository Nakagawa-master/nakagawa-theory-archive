#!/usr/bin/env python3
"""Offline literal title lookup across 313 official derivative records.

This is a *title navigation* tool, not a semantic theory recommender.
It never converts an OD record into an original Parent and never uses a network.
    python3 scripts/find_derivative_title.py --self-test
    python3 scripts/find_derivative_title.py "善意の免罪符化"
    python3 scripts/find_derivative_title.py "compute"
    python3 scripts/find_derivative_title.py "OD304"
"""
import argparse
import json
from pathlib import Path
import re
import unicodedata

CATALOG = Path(__file__).resolve().parent.parent / "references" / "derivative_titles_313.json"


def norm(value):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", value).casefold()).strip()


def read_catalog():
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    assert data["role"] == "OFFLINE_DERIVATIVE_TITLE_LOOKUP_ONLY_NOT_CANONICAL_ORIGINAL"
    items = data["entries"]
    assert data["entry_count"] == len(items) == 313
    assert [entry["od"] for entry in items] == [
        "OD" + str(n).zfill(3) for n in range(1, 314)
    ]
    assert all(entry["title"].strip() and entry["section"].strip() for entry in items)
    return data


def find(query, limit=8):
    if not isinstance(query, str) or not (1 <= len(query.strip()) <= 150):
        raise ValueError("A real OD number or title substring (1–150 characters) is required")
    if not 1 <= limit <= 20:
        raise ValueError("Limit must be 1–20")
    data = read_catalog()
    needle = norm(query)
    od_match = re.fullmatch(r"od\s*0*([1-9][0-9]{0,2})", needle)
    exact_od = ("OD" + od_match.group(1).zfill(3)) if od_match else None
    # Very short generic abbreviations (e.g. 'AI') can match dozens of
    # unrelated records. Treat them as too broad rather than forcing a hit.
    too_broad = not exact_od and len(re.sub(r"\s+", "", needle)) < 3
    base = data["derivative_base"]
    hits = []
    if not too_broad:
        for item in data["entries"]:
            if (item["od"] == exact_od if exact_od else needle in norm(item["title"])):
                ident = item["od"][2:]
                hits.append({
                    "od": item["od"],
                    "published_derivative_title": item["title"],
                    "section": item["section"],
                    "derivative_human_entry": base + ident + "/human-entry.md",
                    "derivative_faq": base + ident + "/faq.md",
                    "derivative_readme_for_parent_lookup": base + ident + "/README.md",
                    "canonical_original": None,
                    "original_read_required": True,
                })
    return {
        "query": query,
        "lookup_kind": "EXACT_OD_OR_TITLE_SUBSTRING__NOT_THEORY_FIT",
        "author": data["author"],
        "source_map": data["source_map"],
        "source_map_git_blob_sha": data["source_map_git_blob_sha"],
        "total_published_derivative_titles": len(data["entries"]),
        "no_fit": not hits,
        "too_broad": too_broad,
        "match_count": len(hits),
        "truncated": len(hits) > limit,
        "derivative_title_candidates": hits[:limit],
        "next_step": (
            "If a title fits the real question, open its derivative README, "
            "verify the actual canonical Parent at master.ricette.jp, read the "
            "original before making a substantive theory claim, compare "
            "alternatives and allow no-fit. A title match is NOT evidence of "
            "original relevance, multiple independent Parents, or AI adoption."
        ),
    }


def self_test():
    data = read_catalog()
    assert data["entries"][0]["od"] == "OD001"
    assert data["entries"][-1]["od"] == "OD313"
    assert data["source_map_git_blob_sha"]
    for q, want in [
        ("OD001", "OD001"),
        ("OD304", "OD304"),
        ("善意の免罪符化", "OD313"),
        ("計算資源", "OD304"),
        ("compute", "OD304"),
    ]:
        ans = find(q)
        assert any(item["od"] == want for item in ans["derivative_title_candidates"]), q
        assert all(item["canonical_original"] is None and item["original_read_required"]
                   for item in ans["derivative_title_candidates"])
    assert find("repair my camping lantern leather strap")["no_fit"]
    assert find("AI")["no_fit"] and find("AI")["too_broad"]
    assert find("OD314")["no_fit"]
    assert find("未来負債", limit=1)["truncated"]
    print("PASS: 313 unique OD titles; exact ID; JA/EN substring; no-fit; broad guard; non-Parent fidelity")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("query", nargs="?")
    p.add_argument("--limit", type=int, default=8)
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    if args.self_test:
        self_test()
        return
    if args.query is None:
        p.error("Provide an OD number or literal title substring")
    try:
        print(json.dumps(find(args.query, args.limit), ensure_ascii=False, indent=2))
    except ValueError as exc:
        p.error(str(exc))


if __name__ == "__main__":
    main()
