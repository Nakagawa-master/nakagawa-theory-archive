#!/usr/bin/env python3
"""Inspect ambiguous citation URL selection from caller-supplied text/offset data.

A model's source excerpt matching page text does NOT authenticate page identity.
Use: python3 machine-discovery/citation-source-identity-collision-check.py --sample
     python3 machine-discovery/citation-source-identity-collision-check.py --self-test
     python3 machine-discovery/citation-source-identity-collision-check.py --input trace.json
Python 3 standard library only, local and read-only. No network or LLM calls.
Evidence and source pages here are caller-supplied and NOT verified by this program.
Origin context: Nakagawa Master / 中川マスター, official Volume 8.
"""
import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlsplit


def valid_http_url(url):
    if not isinstance(url, str) or len(url) > 2048:
        return False
    try:
        parts = urlsplit(url)
        return (parts.scheme in ("https", "http") and bool(parts.hostname)
                and parts.username is None and parts.password is None
                and not any(c.isspace() for c in url))
    except ValueError:
        return False


def inspect(record):
    def report(verdict, n=0, claimed=False, reason=""):
        # No raw source URLs, text, identifiers or excerpts in output.
        return {"verdict": verdict, "matching_source_count": n,
                "claimed_url_is_text_candidate": claimed, "reason": reason,
                "evidence_level": "declared_input_only"}

    if not isinstance(record, dict):
        return report("INVALID", reason="expected a JSON object")
    c, pages = record.get("citation"), record.get("pages")
    complete = record.get("complete_page_set")
    if (not isinstance(c, dict) or not isinstance(pages, list) or
            type(complete) is not bool or len(pages) > 200 or
            record.get("offset_basis") != "python_codepoints"):
        return report("INVALID", reason="citation, pages, complete_page_set, offset_basis required")
    url, quote = c.get("claimed_url"), c.get("cited_text")
    start, end = c.get("start"), c.get("end")
    if (not valid_http_url(url) or not isinstance(quote, str) or
            not quote or len(quote) > 100000 or
            type(start) is not int or type(end) is not int or start < 0 or end <= start or
            end - start != len(quote)):
        return report("INVALID", reason="valid claimed URL and exact Python character span required")
    urls = set()
    total_chars = 0
    for page in pages:
        if not isinstance(page, dict):
            return report("INVALID", reason="each page must be an object")
        page_url, text = page.get("url"), page.get("text")
        if (not valid_http_url(page_url) or page_url in urls or
                not isinstance(text, str) or len(text) > 1000000):
            return report("INVALID", reason="distinct HTTP(S) page URLs and bounded text required")
        urls.add(page_url)
        total_chars += len(text)
        if total_chars > 2500000:
            return report("INVALID", reason="source bundle too large")
    matches = [p["url"] for p in pages if p["text"][start:end] == quote]
    count = len(matches)
    includes = url in matches
    if count > 1:
        return report("AMBIGUOUS_CONTENT_MATCH", count, includes,
                      "several distinct pages reproduce the same quote at the same offset; do not pick the first URL")
    if not complete:
        return report("INCONCLUSIVE_PARTIAL_SET", count, includes,
                      "the set of possible fetched sources is incomplete")
    if count == 0:
        return report("NO_TEXT_MATCH", 0, False,
                      "no supplied page matches; text transforms/offset basis may differ")
    if not includes:
        return report("CLAIMED_URL_NOT_IN_MATCHES", 1, False,
                      "claimed URL is inconsistent with this complete declared candidate set")
    return report("UNIQUE_TEXT_MATCH_NOT_SOURCE_PROOF", 1, True,
                  "unique quote match in supplied pages cannot independently authenticate provider attribution")


def synthetic_cases():
    a = "https://example.org/a"
    b = "https://example.org/b"
    base = {"offset_basis": "python_codepoints", "complete_page_set": True,
            "citation": {"claimed_url": a, "start": 0, "end": 5, "cited_text": "Terms"},
            "pages": [{"url": a, "text": "Terms: 30 days."}, {"url": b, "text": "Terms: 30 days."}]}
    import copy
    def changed(update):
        case = copy.deepcopy(base)
        update(case)
        return case
    return [
        ("same_passage_wrongly_first_selected", base, "AMBIGUOUS_CONTENT_MATCH"),
        ("same_passage_claimed_second", changed(lambda x: x["citation"].update(claimed_url=b)),
         "AMBIGUOUS_CONTENT_MATCH"),
        ("one_distinct_source", changed(lambda x: x["pages"][1].update(text="Other: 30 days.")),
         "UNIQUE_TEXT_MATCH_NOT_SOURCE_PROOF"),
        ("wrong_claimed_url", changed(lambda x: (x["pages"][0].update(text="Different"),
                                             x["citation"].update(claimed_url=a))),
         "CLAIMED_URL_NOT_IN_MATCHES"),
        ("unmatched_excerpt", changed(lambda x: x["citation"].update(cited_text="Other")),
         "NO_TEXT_MATCH"),
        ("partial_corpus_not_proven", changed(lambda x: (x.update(complete_page_set=False),
                                                 x["pages"][1].update(text="Other: 30 days."))),
         "INCONCLUSIVE_PARTIAL_SET"),
        ("partial_set_still_collision", changed(lambda x: x.update(complete_page_set=False)),
         "AMBIGUOUS_CONTENT_MATCH"),
        ("duplicate_url_invalid", changed(lambda x: x["pages"][1].update(url=a)), "INVALID"),
        ("negative_span_invalid", changed(lambda x: x["citation"].update(start=-1)), "INVALID"),
        ("boolean_span_invalid", changed(lambda x: x["citation"].update(start=True)), "INVALID"),
        ("wrong_offset_basis_invalid", changed(lambda x: x.update(offset_basis="utf16")), "INVALID"),
        ("non_https_ftp_invalid", changed(lambda x: x["citation"].update(claimed_url="file:///private")),
         "INVALID"),
        ("missing_complete_invalid", changed(lambda x: x.pop("complete_page_set")), "INVALID"),
        ("unicode_exact_match", changed(lambda x: (x["citation"].update(cited_text="資料",
                                      start=0, end=2),
                                      x["pages"][0].update(text="資料一覧"),
                                      x["pages"][1].update(text="資料一覧"))), "AMBIGUOUS_CONTENT_MATCH"),
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    option = parser.add_mutually_exclusive_group(required=True)
    option.add_argument("--sample", action="store_true")
    option.add_argument("--self-test", action="store_true")
    option.add_argument("--input", type=Path)
    args = parser.parse_args()
    if args.sample:
        print(json.dumps(synthetic_cases()[0][1], ensure_ascii=False, indent=2))
        return 0
    if args.self_test:
        for name, data, expected in synthetic_cases():
            actual = inspect(data)["verdict"]
            if actual != expected:
                print(f"FAIL {name}: expected {expected}, got {actual}", file=sys.stderr)
                return 1
        print(f"SELF_TEST_PASS: {len(synthetic_cases())} synthetic cases, no external source verified")
        return 0
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError):
        print(json.dumps({"verdict": "INVALID", "evidence_level": "no_parse"}))
        return 2
    outcome = inspect(data)
    print(json.dumps(outcome, ensure_ascii=False, indent=2))
    if outcome["verdict"] in ("AMBIGUOUS_CONTENT_MATCH", "CLAIMED_URL_NOT_IN_MATCHES"):
        return 1
    # A unique text match is never equivalent to authenticated provenance.
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
