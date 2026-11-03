#!/usr/bin/env python3
"""Offline AI ranking eligibility-before-cap regression (non-canonical public aid).
Original source: https://github.com/ai-pipestream/turboembed/issues/1285
Independent receiving fix: https://github.com/ai-pipestream/turboembed/pull/1330

python3 machine-discovery/eligible-before-cap-probe.py --self-test
python3 machine-discovery/eligible-before-cap-probe.py --sample
python3 machine-discovery/eligible-before-cap-probe.py claims.json

This is a deterministic ordering simulation, NOT a live NLI/model/user test.
No dependencies, network, MCP, tokens, or credentials.
"""
import argparse
import json
import sys
from pathlib import Path

SAMPLE = {
    "max_pairs": 1, "pair_token_budget": 12, "pair_special_tokens": 3,
    "ranked_candidates": [
        {"id": "over-budget", "rank": 2, "tokens_left": 9, "tokens_right": 9},
        {"id": "eligible", "rank": 1, "tokens_left": 3, "tokens_right": 3},
    ],
}


def natural(value, key):
    if type(value) is not int or value < 0:
        raise ValueError(key + " must be an integer >= 0")
    return value


def analyze(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be a JSON object")
    cap = natural(data.get("max_pairs"), "max_pairs")
    limit = natural(data.get("pair_token_budget"), "pair_token_budget")
    special = natural(data.get("pair_special_tokens"), "pair_special_tokens")
    items = data.get("ranked_candidates")
    if not isinstance(items, list):
        raise ValueError("ranked_candidates must be a JSON array")
    unique = set()
    rows = []
    for pos, c in enumerate(items):
        if not isinstance(c, dict):
            raise ValueError("candidate must be an object")
        ident = c.get("id")
        if not isinstance(ident, str) or not ident.strip() or ident in unique:
            raise ValueError("candidate id must be unique and nonempty")
        unique.add(ident)
        rows.append((ident, natural(c.get("rank"), "rank"), pos,
                     natural(c.get("tokens_left"), "tokens_left") +
                     natural(c.get("tokens_right"), "tokens_right") + special))
    ranked = sorted(rows, key=lambda v: (-v[1], v[2]))
    before = [v[0] for v in ranked[:cap] if v[3] <= limit]
    after = [v[0] for v in ranked if v[3] <= limit][:cap]
    hidden = [v for v in after if v not in before]
    return {
        "verdict": "ELIGIBLE_CANDIDATES_HIDDEN_BY_OLD_ORDER" if hidden else "NO_LOSS_IN_THIS_FIXTURE",
        "old_cap_then_filter": before,
        "correct_filter_then_cap": after,
        "previously_hidden": hidden,
        "original_source": "https://github.com/ai-pipestream/turboembed/issues/1285",
        "receiver_implemented_fix": "https://github.com/ai-pipestream/turboembed/pull/1330",
        "evidence_limit": "Counts and ranks are provided inputs. This synthetic order check does not establish installed user behavior, model correctness, independent adoption or whole-theory endorsement.",
    }


def self_test():
    assert analyze(SAMPLE)["previously_hidden"] == ["eligible"]
    assert analyze(dict(SAMPLE, max_pairs=0))["previously_hidden"] == []
    assert analyze(dict(SAMPLE, ranked_candidates=[SAMPLE["ranked_candidates"][0]]))["previously_hidden"] == []
    exact = dict(SAMPLE, ranked_candidates=[
        {"id": "exact", "rank": 1, "tokens_left": 4, "tokens_right": 5}])
    assert analyze(exact)["correct_filter_then_cap"] == ["exact"]
    assert analyze(dict(exact, pair_token_budget=11))["correct_filter_then_cap"] == []
    tied = dict(SAMPLE, ranked_candidates=[
        {"id": "first", "rank": 1, "tokens_left": 1, "tokens_right": 1},
        {"id": "second", "rank": 1, "tokens_left": 1, "tokens_right": 1}])
    assert analyze(tied)["correct_filter_then_cap"] == ["first"]
    two = dict(SAMPLE, max_pairs=2, ranked_candidates=[
        {"id": "bad1", "rank": 4, "tokens_left": 9, "tokens_right": 9},
        {"id": "bad2", "rank": 3, "tokens_left": 9, "tokens_right": 9},
        {"id": "good1", "rank": 2, "tokens_left": 1, "tokens_right": 1},
        {"id": "good2", "rank": 1, "tokens_left": 2, "tokens_right": 2}])
    assert analyze(two)["previously_hidden"] == ["good1", "good2"]
    for invalid in (True, None, -1, 1.1):
        try:
            analyze(dict(SAMPLE, max_pairs=invalid))
        except ValueError:
            pass
        else:
            raise AssertionError("invalid cap accepted")
    print("self-test PASS: loss, zero cap, all-ineligible, exact edge, boundary fail, ties, multiple lost, malformed inputs", file=sys.stderr)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", nargs="?", help="JSON file or - to read stdin")
    p.add_argument("--sample", action="store_true")
    p.add_argument("--self-test", action="store_true")
    a = p.parse_args()
    if a.self_test:
        self_test()
        return 0
    if a.sample:
        print(json.dumps(SAMPLE, indent=2))
        return 0
    if not a.input:
        p.error("provide a JSON fixture or --sample or --self-test")
    try:
        data = sys.stdin.read() if a.input == "-" else Path(a.input).read_text(encoding="utf-8")
        result = analyze(json.loads(data))
    except (ValueError, OSError, json.JSONDecodeError) as e:
        print("INVALID INPUT: " + str(e), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
