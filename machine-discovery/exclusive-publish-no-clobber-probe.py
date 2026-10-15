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

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true",
                        help="Perform local positive, negative, inverse and unsupported-link policy witness")
    args = parser.parse_args()
    result = witness()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["result"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
