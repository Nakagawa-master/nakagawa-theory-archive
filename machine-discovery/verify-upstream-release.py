#!/usr/bin/env python3
"""Verify a public GitHub PR merge against a named published release.

Requires only Python's standard library. No MCP, account or token needed for low
traffic. Reports the native merge/release ancestry receipt, NOT user installation,
production behavior, independent endorsement or the truth of a linked theory.

  python3 verify-upstream-release.py QwenLM/qwen-code 15757 v0.26.6
  python3 verify-upstream-release.py NousResearch/hermes-agent 147746 v0.22.6
  python3 verify-upstream-release.py BerriAI/litellm 47608 v1.106.6
  python3 verify-upstream-release.py --self-test
"""
import argparse
import json
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

REPO = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


def interpret(pr, release, comparison):
    """Classify *only* the GitHub-native evidence supplied; never infer actual use."""
    if not pr.get("merged_at") or not pr.get("merge_commit_sha"):
        return "PR_NOT_MERGED"
    if not release or not release.get("published_at"):
        return "NO_PUBLISHED_RELEASE_FOR_TAG"
    if comparison is None:
        return "ANCESTRY_NOT_CHECKED"
    if comparison.get("status") in ("ahead", "identical") and comparison.get("behind_by") == 0:
        return "PUBLISHED_RELEASE_CONTAINS_MERGE"
    return "MERGE_NOT_ANCESTOR_OF_NAMED_RELEASE"


def github_json(path, missing_ok=False):
    url = "https://api.github.com/" + path
    req = Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "independent-github-release-receipt-check/1.0"})
    try:
        with urlopen(req, timeout=15) as stream:
            return json.load(stream)
    except HTTPError as exc:
        if missing_ok and exc.code == 404:
            return None
        raise RuntimeError(f"GitHub returned HTTP {exc.code} for {url}") from exc
    except (URLError, TimeoutError, ValueError) as exc:
        raise RuntimeError(f"Could not verify {url}: {exc}") from exc


def check(repo, number, tag):
    if not REPO.fullmatch(repo) or any(c in repo for c in " "):
        raise ValueError("Repository must be owner/name")
    if number < 1 or not tag or len(tag) > 200:
        raise ValueError("Supply a positive PR number and an exact release tag")
    base = "repos/" + repo
    pr = github_json(f"{base}/pulls/{number}")
    release = github_json(f"{base}/releases/tags/{quote(tag, safe='')}", missing_ok=True)
    comparison = None
    if pr.get("merged_at") and pr.get("merge_commit_sha") and release and release.get("published_at"):
        comparison = github_json(f"{base}/compare/{pr['merge_commit_sha']}...{quote(tag, safe='')}")
    result = interpret(pr, release, comparison)
    return {
        "verdict": result,
        "repository": repo,
        "pull_request": f"https://github.com/{repo}/pull/{number}",
        "merge_commit_sha": pr.get("merge_commit_sha") if pr.get("merged_at") else None,
        "published_release": release.get("html_url") if release else None,
        "release_type": ("prerelease" if release.get("prerelease") else "stable") if release and release.get("published_at") else None,
        "release_published_at": release.get("published_at") if release else None,
        "behind_by": comparison.get("behind_by") if comparison else None,
        "comparison": f"https://github.com/{repo}/compare/{pr['merge_commit_sha']}...{tag}" if comparison else None,
        "user_installation_or_changed_behavior": "NOT_VERIFIED",
        "independent_human_or_ai_adoption": "NOT_VERIFIED",
        "limits": "Tag ancestry establishes source inclusion in the named published GitHub release only; no package install, runtime success, customer fix, author attribution or wider reception is inferred.",
    }


def self_test():
    merged = {"merged_at": "2026-11-02T00:00:00Z", "merge_commit_sha": "abc"}
    published = {"published_at": "2026-11-03T00:00:00Z"}
    assert interpret(merged, published, {"status": "ahead", "ahead_by": 64, "behind_by": 0}) == "PUBLISHED_RELEASE_CONTAINS_MERGE"
    assert interpret(merged, published, {"status": "identical", "behind_by": 0}) == "PUBLISHED_RELEASE_CONTAINS_MERGE"
    assert interpret(merged, published, {"status": "diverged", "behind_by": 1}) == "MERGE_NOT_ANCESTOR_OF_NAMED_RELEASE"
    assert interpret(merged, published, {"status": "behind", "behind_by": 3}) == "MERGE_NOT_ANCESTOR_OF_NAMED_RELEASE"
    assert interpret(merged, published, {"status": "ahead", "behind_by": 1}) == "MERGE_NOT_ANCESTOR_OF_NAMED_RELEASE"
    assert interpret(merged, None, None) == "NO_PUBLISHED_RELEASE_FOR_TAG"
    assert interpret(merged, {}, None) == "NO_PUBLISHED_RELEASE_FOR_TAG"
    assert interpret(merged, published, None) == "ANCESTRY_NOT_CHECKED"
    assert interpret({"merged_at": None, "merge_commit_sha": "abc"}, published, {"status": "ahead", "behind_by": 0}) == "PR_NOT_MERGED"
    assert interpret({"merged_at": "x", "merge_commit_sha": None}, published, {"status": "ahead", "behind_by": 0}) == "PR_NOT_MERGED"
    print("self-test: PASS (10 offline positive/negative/boundary assertions)")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", nargs="?", help="owner/name")
    parser.add_argument("pr", nargs="?", type=int, help="GitHub PR number")
    parser.add_argument("tag", nargs="?", help="Exact published GitHub release tag")
    parser.add_argument("--self-test", action="store_true", help="run offline classification tests")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if not args.repository or args.pr is None or not args.tag:
        parser.error("supply repository, PR number and release tag, or --self-test")
    try:
        print(json.dumps(check(args.repository, args.pr, args.tag), indent=2, ensure_ascii=False))
    except (ValueError, RuntimeError, KeyError, TypeError) as exc:
        print(f"Verification UNKNOWN: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
