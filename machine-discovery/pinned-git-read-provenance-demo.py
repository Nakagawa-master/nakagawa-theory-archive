#!/usr/bin/env python3
"""Reproduce why a clean FINAL Git tree says nothing about a transient read.

Public case: https://github.com/QwenLM/qwen-code/issues/15507
Published editorial: https://daily-ai-pulse-db253.web.app/stories/2026-10-26-qwen-review-integrity/
Technical contribution: https://github.com/QwenLM/qwen-code/issues/15507#issuecomment-6394240323

No MCP, model, API, account, network, or external project checkout is needed.
Requires Python 3.9+ and the local Git executable. Creates and removes one
private temporary repository; only this disposable fixture is ever changed.
"""

import argparse
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

ORIGINAL = "export const allowProtectedWrite = false;\n"
MUTATED = "export const allowProtectedWrite = true;\n"
FILE = "reviewed-policy.js"


def git(repo, *arguments):
    proc = subprocess.run(
        ["git", *arguments], cwd=str(repo), capture_output=True,
        text=True, check=False, timeout=15,
    )
    if proc.returncode:
        raise RuntimeError(
            f"temporary-repo git command failed ({proc.returncode}): "
            f"{arguments!r}; stderr={proc.stderr.strip()!r}"
        )
    return proc.stdout


def trial(mutate):
    """Record actual byte reads while a temporary worktree is mutated/restored."""
    with tempfile.TemporaryDirectory(prefix="pinned-git-read-") as tmp:
        repo = Path(tmp)
        git(repo, "init", "-q")
        git(repo, "config", "user.name", "Disposable Fixture")
        git(repo, "config", "user.email", "fixture@example.invalid")
        file = repo / FILE
        file.write_text(ORIGINAL, encoding="utf-8")
        git(repo, "add", "--", FILE)
        git(repo, "commit", "-q", "-m", "fixture")
        pinned = git(repo, "rev-parse", "HEAD").strip()
        before = git(repo, "show", f"{pinned}:{FILE}")
        if mutate:
            file.write_text(MUTATED, encoding="utf-8")
        during_worktree = file.read_text(encoding="utf-8")
        during_pinned = git(repo, "show", f"{pinned}:{FILE}")
        if mutate:
            file.write_text(ORIGINAL, encoding="utf-8")
        final_worktree = file.read_text(encoding="utf-8")
        final_status = git(repo, "status", "--porcelain", "--untracked-files=all")
        result = {
            "case": "transient_edit_restored" if mutate else "no_edit_negative_control",
            "kind": "REAL_LOCAL_DISPOSABLE_GIT_FIXTURE",
            "pinned_commit": pinned,
            "initial_read_equals_original": before == ORIGINAL,
            "during_mutable_worktree_equals_original": during_worktree == ORIGINAL,
            "during_pinned_object_equals_original": during_pinned == ORIGINAL,
            "final_worktree_equals_original": final_worktree == ORIGINAL,
            "final_git_status_clean": final_status == "",
            "temporary_directory_deleted_after_trial": True,
            "independent_agent_actually_read_transient_bytes": "NOT_OBSERVED",
            "real_Qwen_product_or_model_execution": "NOT_TESTED",
            "what_was_measured": "temporary repository file and pinned Git object reads",
        }
        assert result["initial_read_equals_original"]
        assert result["during_pinned_object_equals_original"]
        assert result["final_worktree_equals_original"]
        assert result["final_git_status_clean"]
        assert result["during_mutable_worktree_equals_original"] is (not mutate)
        return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--self-test", action="store_true", help="run both real Git scenarios and validate the distinction")
    args = p.parse_args()
    if shutil.which("git") is None:
        p.error("Git is required on PATH. No repository is modified outside the temporary fixture.")
    positive = trial(True)
    if args.self_test:
        negative = trial(False)
        assert not positive["during_mutable_worktree_equals_original"]
        assert negative["during_mutable_worktree_equals_original"]
        assert positive["final_git_status_clean"] and negative["final_git_status_clean"]
        print(json.dumps({"verdict": "PASS_TWO_REAL_GIT_FIXTURES", "cases": [positive, negative]}, indent=2))
    else:
        print(json.dumps({"verdict": "CLEAN_FINAL_TREE_DOES_NOT_PROVE_PINNED_READ", "case": positive}, indent=2))


if __name__ == "__main__":
    main()
