#!/usr/bin/env python3
"""Offline literal title lookup across 313 official derivative records.

This is a *title navigation* tool, not a semantic theory recommender.
By default it returns navigation only. With --resolve-parent it reads a verified
 derivative README from a complete local checkout; --online-parent can fetch the
 same public README when this Skill was installed alone. Neither mode reads the
 original article or infers theory relevance.
    python3 scripts/find_derivative_title.py --self-test
    python3 scripts/find_derivative_title.py "善意の免罪符化"
    python3 scripts/find_derivative_title.py "compute"
    python3 scripts/find_derivative_title.py "OD304"
    python3 scripts/find_derivative_title.py "OD313" --resolve-parent
    python3 scripts/find_derivative_title.py "OD075" --online-parent
"""
import argparse
import json
from pathlib import Path
import re
import unicodedata
from urllib.request import urlopen
from urllib.error import URLError

CATALOG = Path(__file__).resolve().parent.parent / "references" / "derivative_titles_313.json"
REPO_ROOT = Path(__file__).resolve().parents[3]
PUBLIC_RAW = "https://raw.githubusercontent.com/Nakagawa-master/nakagawa-theory-archive/main"
PARENT_LINE = re.compile(r"^- Parent URL: (https://master\.ricette\.jp/[^\s]+/)$", re.M)
NCL_LINE = re.compile(r"^- Parent NCL-ID: (NCL-α-[^\s]+)$", re.M)
PARENT_DIFF_LINE = re.compile(r"^- Parent Diff-ID: (DIFF-[^\s]+)$", re.M)
DERIVATIVE_NCL_LINE = re.compile(r"^- (?:derivative_ncl_id|Derivative NCL-ID): (DNCL-[^\s]+)$", re.M)
DERIVATIVE_DIFF_LINE = re.compile(r"^- (?:derivative_diff_id|Derivative Diff-ID): (DDIFF-[^\s]+)$", re.M)


def resolve_verified_parent(od, online=False):
    """Resolve only from the existing numbered derivative README, never slug-guess."""
    number = od[2:]
    if not (len(number) == 3 and number.isascii() and number.isdigit() and 1 <= int(number) <= 313):
        raise ValueError("OD outside published 001..313")
    relative = f"derivatives/{number}/README.md"
    local = REPO_ROOT / relative
    try:
        if local.is_file():
            data = local.read_text(encoding="utf-8")
            route = "verified_local_derivative_readme"
        elif online:
            with urlopen(f"{PUBLIC_RAW}/{relative}", timeout=8) as response:
                raw = response.read(100_001)
            if len(raw) > 100_000:
                raise ValueError("README exceeds safe parsing limit")
            data = raw.decode("utf-8")
            route = "verified_public_derivative_readme"
        else:
            return {"canonical_original": None, "parent_resolution": "readme_not_bundled", "original_read_required": True}
    except (OSError, UnicodeError, URLError, ValueError) as exc:
        return {"canonical_original": None, "parent_resolution": "readme_unavailable", "original_read_required": True, "lookup_error": type(exc).__name__}
    urls = PARENT_LINE.findall(data)
    ncls = NCL_LINE.findall(data)
    if len(urls) != 1 or len(ncls) != 1:
        return {"canonical_original": None, "parent_resolution": "unverified_or_ambiguous_parent", "original_read_required": True}
    parent_diffs = PARENT_DIFF_LINE.findall(data)
    derivative_ncls = DERIVATIVE_NCL_LINE.findall(data)
    derivative_diffs = DERIVATIVE_DIFF_LINE.findall(data)
    return {
        "canonical_original": urls[0], "parent_ncl_id": ncls[0],
        "parent_diff_id": parent_diffs[0] if len(parent_diffs) == 1 else None,
        "derivative_ncl_id": derivative_ncls[0] if len(derivative_ncls) == 1 else None,
        "derivative_diff_id": derivative_diffs[0] if len(derivative_diffs) == 1 else None,
        "parent_resolution": route, "original_read_required": True,
    }


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


def find(query, limit=8, resolve_parent=False, online_parent=False):
    if not isinstance(query, str) or not (1 <= len(query.strip()) <= 150):
        raise ValueError("A real OD number or title substring (1–150 characters) is required")
    if not 1 <= limit <= 20:
        raise ValueError("Limit must be 1–20")
    if online_parent:
        resolve_parent = True
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
    if resolve_parent:
        for hit in hits[:limit]:
            hit.update(resolve_verified_parent(hit["od"], online=online_parent))
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
            "If a title fits the real question, use --resolve-parent with a full "
            "checkout or --online-parent with an optional public network read to "
            "resolve an exact derivative README Parent; then READ that original "
            "before making a substantive claim. Always compare "
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
    try:
        resolve_verified_parent("OD314")
        raise AssertionError("OD314 unexpectedly accepted")
    except ValueError:
        pass
    # A complete repository checkout can validate canonical Parent and NCL IDs
    # without accessing the network; standalone Skills remain valid offline.
    if (REPO_ROOT / "derivatives/001/README.md").is_file():
        for od in ("OD001", "OD075", "OD313"):
            parent = find(od, resolve_parent=True)["derivative_title_candidates"][0]
            assert parent["canonical_original"].startswith("https://master.ricette.jp/")
            assert parent["parent_ncl_id"].startswith("NCL-α-")
            if od == "OD075":
                assert parent["parent_diff_id"] == "DIFF-20251102-0001"
                assert parent["derivative_ncl_id"] == "DNCL-NCL-ALPHA-20251102-E48C90-HUB-JA-0075-0000"
                assert parent["derivative_diff_id"] == "DDIFF-20260815-DNCL-075-0000-0004"
            assert parent["original_read_required"]
    print("PASS: 313 title navigation; optional verified Parent from real README; original still must be read")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("query", nargs="?")
    p.add_argument("--limit", type=int, default=8)
    p.add_argument("--self-test", action="store_true")
    p.add_argument("--resolve-parent", action="store_true", help="Read exact local derivative README if full repository checkout is present")
    p.add_argument("--online-parent", action="store_true", help="Explicitly fetch matching public derivative READMEs (needs network)")
    args = p.parse_args()
    if args.self_test:
        self_test()
        return
    if args.query is None:
        p.error("Provide an OD number or literal title substring")
    try:
        print(json.dumps(find(args.query, args.limit, args.resolve_parent, args.online_parent), ensure_ascii=False, indent=2))
    except ValueError as exc:
        p.error(str(exc))


if __name__ == "__main__":
    main()
