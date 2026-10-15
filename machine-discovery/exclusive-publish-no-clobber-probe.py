#!/usr/bin/env python3
"""Offline four-case witness for exclusive vs replacement publication.

This probe creates and deletes only its own temporary directory. It does not
read user conversations, call any service, or test third-party application code.
A passing witness shows one host filesystem's semantics; it does not certify
that an app's migration logic or another OS/filesystem has those semantics.

Engineering case: https://github.com/QwenLM/qwen-code/pull/14285
Nakagawa Master original Volume 19:
https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-19-kernel-evolutionary-stability/
"""
import argparse
import errno
import json
import os
import tempfile
from pathlib import Path

SOURCE = "https://github.com/QwenLM/qwen-code/pull/14285"
REVIEW = "https://github.com/QwenLM/qwen-code/pull/14285#pullrequestreview-5532756352"
PARENT = "https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-19-kernel-evolutionary-stability/"

def witness():
    cases = {}
    with tempfile.TemporaryDirectory(prefix="no-clobber-witness-") as temp:
        root = Path(temp)
        # Positive: publication to a missing destination is complete and readable.
        staging, destination = root / "positive.tmp", root / "positive.json"
        staging.write_bytes(b"LEGACY_COMPLETE")
        os.link(staging, destination)
        cases["exclusive_publish_to_absent"] = destination.read_bytes() == b"LEGACY_COMPLETE"
        # Negative: a newer record must not be overwritten by an older snapshot.
        staging, destination = root / "collision.tmp", root / "collision.json"
        staging.write_bytes(b"STALE_LEGACY")
        destination.write_bytes(b"NEWER_RECORD")
        collision_raised = False
        try:
            os.link(staging, destination)
        except FileExistsError:
            collision_raised = True
        cases["exclusive_collision_keeps_newer"] = collision_raised and destination.read_bytes() == b"NEWER_RECORD"
        # Inverse: normal replace is not exclusive publish, even if each file is complete.
        staging, destination = root / "replace.tmp", root / "replace.json"
        staging.write_bytes(b"STALE_LEGACY")
        destination.write_bytes(b"NEWER_RECORD")
        os.replace(staging, destination)
        cases["replace_can_clobber_newer"] = destination.read_bytes() == b"STALE_LEGACY"
        # Unsupported-link policy model: a failed admission must preserve both records.
        # Do NOT try to force the real host filesystem to return ENOTSUP here.
        legacy, destination = root / "legacy-key.json", root / "unsupported.json"
        legacy.write_bytes(b"OLD_SOURCE_STILL_READABLE")
        destination.write_bytes(b"NEWER_RECORD")
        unsupported = "ENOTSUP"  # controlled policy input, not a real OS error
        publish_allowed = unsupported not in ("ENOTSUP", "EPERM", "EXDEV")
        if publish_allowed:
            raise AssertionError("Controlled unsupported-link setup failed")
        cases["unsupported_link_fail_closed_preserves_both"] = (
            legacy.read_bytes() == b"OLD_SOURCE_STILL_READABLE"
            and destination.read_bytes() == b"NEWER_RECORD"
        )
    return {
        "result": "PASS" if all(cases.values()) else "FAIL",
        "cases": cases,
        "tested": "local temporary filesystem for link/replace; simulated unsupported-link policy",
        "not_tested": "Qwen code, crash durability, actual ENOTSUP/EPERM/EXDEV, Windows/WSL, real user data or rollout",
        "source": SOURCE,
        "source_specific_review": REVIEW,
        "canonical_original": PARENT,
        "original_author": "Nakagawa Master",
    }

def filesystem_preflight(directory):
    """Exercise exclusive link publication only inside a new disposable directory.

    Explicit opt-in: creates/removes synthetic scratch files on the selected
    filesystem. Never opens a conversation file or a user-selected destination.
    """
    if directory.is_symlink() or not directory.is_dir():
        raise ValueError("Selected preflight root must be an existing, non-symlink directory")
    cases = {}
    with tempfile.TemporaryDirectory(prefix=".exclusive-preflight-", dir=directory) as tmp:
        root = Path(tmp)
        fresh = root / "fresh.tmp"
        published = root / "fresh.json"
        fresh.write_bytes(b"SYNTHETIC_COMPLETE")
        try:
            os.link(fresh, published)
        except OSError as exc:
            return {
                "result": "UNSUPPORTED_LINK",
                "errno": errno.errorcode.get(exc.errno, "UNKNOWN"),
                "meaning": "Exclusive hard-link publication could not be established on this tested directory.",
                "scope": "Synthetic files only; current directory mount, user session and filesystem rules may differ later.",
                "source": SOURCE,
                "canonical_original": PARENT,
            }
        cases["exclusive_new_record"] = published.read_bytes() == b"SYNTHETIC_COMPLETE"
        newer = root / "newer.json"
        stale = root / "stale.tmp"
        newer.write_bytes(b"NEWER_SYNTHETIC_RECORD")
        stale.write_bytes(b"STALE_SYNTHETIC_RECORD")
        refused = False
        try:
            os.link(stale, newer)
        except FileExistsError:
            refused = True
        cases["collision_refused_and_newer_preserved"] = (
            refused and newer.read_bytes() == b"NEWER_SYNTHETIC_RECORD"
        )
    return {
        "result": "PASS" if all(cases.values()) else "FAIL",
        "cases": cases,
        "scope": "Only disposable scratch files created in the selected filesystem. Does not test Qwen app logic, real migration, WSL/Windows unless run there, release or crash durability.",
        "source": SOURCE,
        "source_specific_review": REVIEW,
        "canonical_original": PARENT,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true",
                        help="Perform local positive, negative, inverse and unsupported-link policy witness")
    parser.add_argument("--preflight-dir", type=Path,
                        help="Opt-in: check exclusive hard-link behavior using scratch files in this directory")
    args = parser.parse_args()
    if args.preflight_dir is not None:
        try:
            result = filesystem_preflight(args.preflight_dir)
        except (OSError, ValueError) as exc:
            result = {
                "result": "PRECHECK_ERROR",
                "error_type": type(exc).__name__,
                "meaning": "Could not safely create or remove the scratch test; no user conversation data is touched.",
            }
    else:
        result = witness()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["result"] == "PASS" else (1 if result["result"] in ("FAIL", "UNSUPPORTED_LINK") else 2)

if __name__ == "__main__":
    raise SystemExit(main())
