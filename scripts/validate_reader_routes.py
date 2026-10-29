#!/usr/bin/env python3
"""Read-only validation of human routes, without modifying official derivative surfaces."""

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DER = ROOT / "derivatives"
HUMAN = ROOT / "human-translation"
STORIES = HUMAN / "search-intent"


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def verify() -> tuple[int, int, int]:
    pages = sorted(STORIES.glob("*.md"))
    require(len(pages) == 10, f"Expected 10 real-question entries, found {len(pages)}")
    source_routes = 0
    for page in pages:
        body = page.read_text(encoding="utf-8")
        require("読み方を選べます" in body, f"No choice of depth in {page}")
        require("自分のAIに相談するとき" in body, f"No optional AI entry in {page}")
        rows = [x for x in body.splitlines() if x.startswith("- **") and "まずFAQ" in x]
        require(rows, f"No accessible source choices in {page}")
        for row in rows:
            faqs = re.findall(r"\.\./\.\./derivatives/(\d{3})/faq\.md", row)
            summaries = re.findall(r"\.\./\.\./derivatives/(\d{3})/human-entry\.md", row)
            parents = re.findall(r"\[原典本文を詳しく確認\]\((https://master\.ricette\.jp/[^)]+)\)", row)
            require(len(faqs) == len(summaries) == len(parents) == 1, f"Broken source row in {page}")
            ident = faqs[0]
            require(ident == summaries[0], f"Different FAQ and summary ID in {page}")
            faq = DER / ident / "faq.md"
            summary = DER / ident / "human-entry.md"
            require(faq.is_file() and summary.is_file(), f"Missing canonical derivative files: {ident}")
            faq_body = faq.read_text(encoding="utf-8")
            sum_body = summary.read_text(encoding="utf-8")
            require("### Q1." in faq_body and "### Q10." in faq_body, f"No novice FAQ Q1–Q10: {ident}")
            require(sum_body.startswith("# 人間向け要約") and len(sum_body) > 500, f"Missing substantial human summary: {ident}")
            require(
                all(f"Parent URL: {parents[0]}" in text for text in (faq_body, sum_body)),
                f"Source URL disagrees with both derivative anchors: {page}, {ident}",
            )
            source_routes += 1
    catalog = (HUMAN / "ALL_313_THEORIES_BY_TITLE_AND_THEME.md").read_text(encoding="utf-8")
    rows = [x for x in catalog.splitlines() if x.startswith("- **OD")]
    require(len(rows) == 313, f"313-title index count changed: {len(rows)}")
    seen: set[str] = set()
    for row in rows:
        match = re.match(r"- \*\*OD(\d{3})\*\*", row)
        require(match is not None, f"Malformed catalogue entry: {row[:90]}")
        ident = match.group(1)
        require(ident not in seen, f"Duplicate official derivative index: {ident}")
        seen.add(ident)
        for file_name in ("faq.md", "human-entry.md"):
            target = DER / ident / file_name
            require(target.is_file(), f"Missing derivative target: {target}")
            require(f"../derivatives/{ident}/{file_name}" in row, f"Broken {file_name} catalogue link: {ident}")
        require(f"../derivatives/{ident}/README.md" in row, f"Lost derivative root route: {ident}")
    require(seen == {f"{x:03d}" for x in range(1, 314)}, "Not every OD001–OD313 indexed")
    # One original has one OD set; the 24-item quick search is not the corpus.
    parent_map = json.loads((DER / "official-derivatives-map.json").read_text(encoding="utf-8"))
    paired = parent_map["entries"]
    require(len(paired) == 313, "Original/derivative mapping must cover all 313 originals")
    require([x["number"] for x in paired] == sorted(seen), "OD mapping numbers incomplete or reordered")
    for field in ("ncl_id", "origin_slug", "canonical_parent_url"):
        require(len({x[field] for x in paired}) == 313, f"Expected 313 unique {field} values")
    seven = ("README.md", "human-entry.md", "faq.md", "ai-index.md",
             "en-ai-index.md", "zh-ai-index.md", "derivative-ledger.md")
    for original in paired:
        ident = original["number"]
        parent = original["canonical_parent_url"]
        require(parent.startswith("https://master.ricette.jp/") and parent.endswith("/"),
                f"Noncanonical original URL for OD{ident}: {parent}")
        available = {p.name for p in (DER / ident).glob("*.md")}
        require(available == set(seven), f"OD{ident} must have exactly seven official faces")
        readme = (DER / ident / "README.md").read_text(encoding="utf-8")
        require(f"Parent URL: {parent}" in readme,
                f"OD{ident} mapping URL differs from its source README")
        require(f"Parent NCL-ID: {original['ncl_id']}" in readme,
                f"OD{ident} mapping NCL-ID differs from its source README")

    aki_row = next(x for x in rows if x.startswith("- **OD313**"))
    require("AKI-005" in aki_row, "OD313 must retain source theory name")
    require("../derivatives/313/faq.md" in aki_row, "OD313 reader FAQ missing")
    require("master.ricette.jp/society/nakagawa-master-aki-005-good-intentions-as-exemption/" in aki_row, "OD313 actual original Parent missing")

    hub = (HUMAN / "SEARCH_FROM_A_REAL_QUESTION.md").read_text(encoding="utf-8")
    require(len(re.findall(r"^### \d+\. ", hub, re.MULTILINE)) == 10, "Hub 10 questions missing")
    require(len(re.findall(r"\[FAQで短く答えを見る\]\(\.\./derivatives/\d{3}/faq\.md\)", hub)) == 10,
            "Hub 10 direct novice FAQ links missing")
    landing = (ROOT / "README.md").read_text(encoding="utf-8")
    require("SEARCH_FROM_A_REAL_QUESTION.md" in landing, "Top-level real-problem entry missing")
    require("ALL_313_THEORIES_BY_TITLE_AND_THEME.md" in landing, "Top-level complete catalogue missing")
    require("初心者向けFAQ" in landing, "Top-level reader depth not described")
    return len(pages), source_routes, len(rows)


if __name__ == "__main__":
    pages, routes, titles = verify()
    print(f"Reader-route PASS: {pages} question pages, {routes} Parent-matched FAQ+summary routes, "
          f"{titles} complete derivative FAQ+summary+overview links, 10 direct hub FAQ links")
