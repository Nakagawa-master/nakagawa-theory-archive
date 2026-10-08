#!/usr/bin/env python3
"""Offline evidence-root consistency check (non-canonical public reuse aid).

Input roots, relationships and stances are REVIEWER ASSERTIONS, not inferred facts.
This script checks whether a claim of independent corroboration is consistent
with those assertions. It cannot judge truth, quotation polarity, independence
in the world, or whether a source is trustworthy. No network calls/dependencies.
"""
import argparse
import json
import sys
from pathlib import Path

RELATIONS = {"primary", "independent_observation", "derived", "unknown"}
STANCES = {"supports", "refutes", "qualifies", "unknown"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def audit(payload):
    require(isinstance(payload, dict) and isinstance(payload.get("claims"), list),
            "top level must contain claims: [...]")
    reports = []
    for position, claim in enumerate(payload["claims"], 1):
        require(isinstance(claim, dict), f"claim {position} must be an object")
        claim_id = claim.get("id")
        require(isinstance(claim_id, str) and bool(claim_id.strip()),
                f"claim {position} needs an id")
        required = claim.get("independent_confirmation_claimed")
        require(type(required) is bool,
                f"{claim_id}: independent_confirmation_claimed must be true/false")
        sources = claim.get("sources")
        require(isinstance(sources, list), f"{claim_id}: sources must be an array")

        positive_roots = set()
        independent_positive_roots = set()
        refuting_roots = set()
        qualifications = 0
        unknown_roots = 0
        unresolved_refuters = 0
        url_to_root = {}
        errors = []
        for index, source in enumerate(sources, 1):
            prefix = f"{claim_id} source {index}"
            require(isinstance(source, dict), f"{prefix}: expected object")
            url, root = source.get("url"), source.get("root_id")
            relation, stance = source.get("relation"), source.get("stance")
            require(isinstance(url, str) and url.startswith(("https://", "http://")),
                    f"{prefix}: url must be http(s)")
            require(isinstance(relation, str) and relation in RELATIONS, f"{prefix}: bad relation")
            require(isinstance(stance, str) and stance in STANCES, f"{prefix}: bad stance")
            require(root is None or (isinstance(root, str) and bool(root.strip())),
                    f"{prefix}: root_id must be string or null")
            if url in url_to_root and url_to_root[url] != root:
                errors.append("same URL assigned incompatible upstream roots")
            url_to_root[url] = root
            if root is None or relation == "unknown":
                unknown_roots += 1
                if stance == "refutes":
                    unresolved_refuters += 1
                continue
            if stance == "supports":
                positive_roots.add(root)
                if relation == "independent_observation":
                    independent_positive_roots.add(root)
            elif stance == "refutes":
                refuting_roots.add(root)
            elif stance == "qualifies":
                qualifications += 1

        if required:
            if len(positive_roots) < 2:
                errors.append("independent confirmation claimed, but fewer than two supporting upstream roots")
            if not independent_positive_roots:
                errors.append("no source marked independently observed positive evidence")
            if refuting_roots or unresolved_refuters:
                errors.append("contrary source present (possibly unresolved); reconcile before claiming unqualified independent confirmation")
        if errors:
            status = "BLOCK"
        else:
            status = "CONSISTENT_INPUT"
        reports.append({
            "id": claim_id,
            "status": status,
            "independent_confirmation_claimed": required,
            "support_root_count": len(positive_roots),
            "independent_observation_root_count": len(independent_positive_roots),
            "refuting_root_count": len(refuting_roots),
            "unresolved_refuting_sources": unresolved_refuters,
            "qualifying_sources": qualifications,
            "source_records_without_known_root": unknown_roots,
            "issues": sorted(set(errors)),
        })
    return {
        "tool": "evidence-root-check-v1",
        "scope": "input consistency only; no truth or real-world source independence certification",
        "claims": reports,
        "blocked": sum(r["status"] == "BLOCK" for r in reports),
    }


SAMPLE = {
    "claims": [
        {
            "id": "one-vendor-release-reposted-three-times",
            "independent_confirmation_claimed": True,
            "sources": [
                {"url": "https://example.org/vendor", "root_id": "vendor-A", "relation": "primary", "stance": "supports"},
                {"url": "https://example.org/news-1", "root_id": "vendor-A", "relation": "derived", "stance": "supports"},
                {"url": "https://example.org/news-2", "root_id": "vendor-A", "relation": "derived", "stance": "supports"},
            ],
        },
        {
            "id": "vendor-plus-independent-test",
            "independent_confirmation_claimed": True,
            "sources": [
                {"url": "https://example.org/vendor", "root_id": "vendor-A", "relation": "primary", "stance": "supports"},
                {"url": "https://example.org/test", "root_id": "lab-B", "relation": "independent_observation", "stance": "supports"},
            ],
        },
    ]
}


def self_test():
    report = audit(SAMPLE)
    assert report["blocked"] == 1
    assert report["claims"][0]["support_root_count"] == 1
    assert report["claims"][0]["status"] == "BLOCK"
    assert report["claims"][1]["status"] == "CONSISTENT_INPUT"
    single = dict(SAMPLE["claims"][1])
    single["sources"] = [dict(s) for s in single["sources"]]
    single["sources"][1]["relation"] = "derived"
    assert audit({"claims": [single]})["blocked"] == 1
    contrary = dict(SAMPLE["claims"][1])
    contrary["sources"] = [*contrary["sources"], {
        "url": "https://example.org/refutation", "root_id": "lab-C",
        "relation": "independent_observation", "stance": "refutes",
    }]
    assert audit({"claims": [contrary]})["blocked"] == 1
    unresolved = dict(SAMPLE["claims"][1])
    unresolved["sources"] = [*unresolved["sources"], {
        "url": "https://example.org/untraced-refutation", "root_id": None,
        "relation": "unknown", "stance": "refutes",
    }]
    assert audit({"claims": [unresolved]})["blocked"] == 1
    no_claim = dict(SAMPLE["claims"][0])
    no_claim["independent_confirmation_claimed"] = False
    assert audit({"claims": [no_claim]})["blocked"] == 0
    try:
        audit({"claims": [{"id": "invalid", "sources": []}]})
    except ValueError:
        pass
    else:
        raise AssertionError("missing required boolean accepted")
    print("self-test: 7 PASS", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", help="input JSON file (use - for stdin)")
    parser.add_argument("--sample", action="store_true", help="print an input example")
    parser.add_argument("--self-test", action="store_true", help="run offline regression cases")
    args = parser.parse_args()
    if args.sample:
        print(json.dumps(SAMPLE, ensure_ascii=False, indent=2))
        return 0
    if args.self_test:
        self_test()
        return 0
    if not args.input:
        parser.error("supply input JSON path, - for stdin, --sample, or --self-test")
    try:
        content = sys.stdin.read() if args.input == "-" else Path(args.input).read_text(encoding="utf-8")
        report = audit(json.loads(content))
    except (ValueError, OSError, json.JSONDecodeError) as error:
        print(f"invalid input: {error}", file=sys.stderr)
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["blocked"] else 0


if __name__ == "__main__":
    sys.exit(main())
