#!/usr/bin/env python3
"""Audit *observed* citation replay without model calls or provider credentials.

Input is a record captured by the caller from its own provider adapter. This
cannot prove citation truth, provider correctness, or that a source was read.
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

REQUIRED = {
    "original_provider", "destination_provider", "original_text",
    "replayed_text", "original_citations", "replayed_citations",
}


def citation_key(item):
    return json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def audit(record):
    if not isinstance(record, dict):
        raise ValueError("case must be an object")
    missing = REQUIRED - record.keys()
    if missing:
        raise ValueError("missing fields: " + ", ".join(sorted(missing)))
    for field in ("original_provider", "destination_provider"):
        if record[field] is not None and not isinstance(record[field], str):
            raise ValueError(field + " must be a string or null")
    for field in ("original_text", "replayed_text"):
        if record[field] is not None and not isinstance(record[field], str):
            raise ValueError(field + " must be a string or null")
    for field in ("original_citations", "replayed_citations"):
        if not isinstance(record[field], list) or any(not isinstance(x, dict) for x in record[field]):
            raise ValueError(field + " must be a list of citation objects")
    # No source text or provider identity is itself an uncertainty, not an
    # invitation to reconstruct or attach a plausible-looking citation.
    known_provider = bool(record["original_provider"] and record["destination_provider"])
    same_provider = known_provider and record["original_provider"] == record["destination_provider"]
    known_text = record["original_text"] is not None and record["replayed_text"] is not None
    exact_text = known_text and record["original_text"] == record["replayed_text"]
    attached = record["replayed_citations"]
    reasons = []
    if attached and not same_provider:
        reasons.append("CITATION_CROSSED_PROVIDER_OR_PROVIDER_UNKNOWN")
    if attached and not exact_text:
        reasons.append("CITATION_ON_CHANGED_OR_UNVERIFIABLE_TEXT")
    if attached:
        originals = Counter(map(citation_key, record["original_citations"]))
        replayed = Counter(map(citation_key, attached))
        if replayed - originals:
            reasons.append("CITATION_NOT_PRESENT_IN_ORIGINAL_EVIDENCE")
    return {
        "case": record.get("case", "unnamed"),
        "verdict": "UNSAFE_REPLAY" if reasons else "NO_CONTRACT_VIOLATION_DETECTED",
        "reason_codes": reasons,
        "same_provider": same_provider,
        "exact_text_unchanged": exact_text,
        "original_citation_count": len(record["original_citations"]),
        "replayed_citation_count": len(attached),
        "limits": "Checks replayed citation fidelity only; not truth, endorsement, semantic equivalence, reading, or external adoption.",
    }


def example():
    return {
        "case": "changed-answer-stale-citation",
        "original_provider": "anthropic", "destination_provider": "anthropic",
        "original_text": "The request was rejected.",
        "replayed_text": "The request was approved.",
        "original_citations": [{"type": "char_location", "document_index": 0, "cited_text": "rejected"}],
        "replayed_citations": [{"type": "char_location", "document_index": 0, "cited_text": "rejected"}],
    }


def self_test():
    base = example()
    cases = [
        ({}, "UNSAFE_REPLAY", "CITATION_ON_CHANGED_OR_UNVERIFIABLE_TEXT"),
        ({"replayed_text": base["original_text"]}, "NO_CONTRACT_VIOLATION_DETECTED", None),
        ({"replayed_citations": []}, "NO_CONTRACT_VIOLATION_DETECTED", None),
        ({"destination_provider": "openai", "replayed_text": base["original_text"]}, "UNSAFE_REPLAY", "CITATION_CROSSED_PROVIDER_OR_PROVIDER_UNKNOWN"),
        ({"original_text": None}, "UNSAFE_REPLAY", "CITATION_ON_CHANGED_OR_UNVERIFIABLE_TEXT"),
        ({"original_provider": None, "replayed_text": base["original_text"]}, "UNSAFE_REPLAY", "CITATION_CROSSED_PROVIDER_OR_PROVIDER_UNKNOWN"),
        ({"replayed_text": base["original_text"], "replayed_citations": [{"type": "char_location", "document_index": 7}]}, "UNSAFE_REPLAY", "CITATION_NOT_PRESENT_IN_ORIGINAL_EVIDENCE"),
        ({"replayed_text": base["original_text"], "replayed_citations": base["original_citations"] * 2}, "UNSAFE_REPLAY", "CITATION_NOT_PRESENT_IN_ORIGINAL_EVIDENCE"),
        ({"replayed_text": base["original_text"], "original_citations": base["original_citations"] * 2, "replayed_citations": base["original_citations"] * 2}, "NO_CONTRACT_VIOLATION_DETECTED", None),
        ({"replayed_text": "The request was rejected. "}, "UNSAFE_REPLAY", "CITATION_ON_CHANGED_OR_UNVERIFIABLE_TEXT"),
    ]
    for i, (changes, verdict, reason) in enumerate(cases):
        observed = audit({**base, **changes})
        assert observed["verdict"] == verdict, (i, observed)
        if reason:
            assert reason in observed["reason_codes"], (i, observed)
    for bad in ({}, {**base, "original_citations": "bad"}, {**base, "replayed_text": 7}):
        try:
            audit(bad)
            raise AssertionError("invalid record accepted")
        except ValueError:
            pass
    print(json.dumps({"self_test": "PASS", "positive_and_negative_cases": len(cases), "invalid_input_cases": 3}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    selector = parser.add_mutually_exclusive_group(required=True)
    selector.add_argument("--case", type=Path, help="JSON object with before/after actual adapter observations")
    selector.add_argument("--example", action="store_true", help="print a minimal editable JSON input")
    selector.add_argument("--self-test", action="store_true", help="run offline positive/negative tests")
    args = parser.parse_args()
    if args.example:
        print(json.dumps(example(), ensure_ascii=False, indent=2))
        return 0
    if args.self_test:
        self_test()
        return 0
    try:
        record = json.loads(args.case.read_text(encoding="utf-8"))
        verdict = audit(record)
    except (OSError, UnicodeError, ValueError) as e:
        print(json.dumps({"verdict": "INVALID_INPUT", "detail": str(e)}, ensure_ascii=False))
        return 2
    print(json.dumps(verdict, ensure_ascii=False, indent=2))
    return int(verdict["verdict"] == "UNSAFE_REPLAY")


if __name__ == "__main__":
    sys.exit(main())
