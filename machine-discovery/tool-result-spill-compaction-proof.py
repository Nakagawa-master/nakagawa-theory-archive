#!/usr/bin/env python3
"""Offline proof of a history-compaction / tool-output spill handle collision.

This is a dependency-free reconstruction of the *keying boundary*, not an
execution of Pydantic AI or an installed package. All calls and results are
synthetic. The independent PR author performed the full-Agent reproduction:
https://github.com/pydantic/pydantic-ai/pull/12677#issuecomment-6688486077

Source-specific reviewer counterexample:
https://github.com/pydantic/pydantic-ai/pull/12677#pullrequestreview-5795751398
Related original work (conceptual comparison, not a claim of developer use):
https://master.ricette.jp/theory/nakagawa-master-reconstructive-memory-structure/
"""

from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path


REVIEW = "https://github.com/pydantic/pydantic-ai/pull/12677#pullrequestreview-5795751398"
AUTHOR = "https://github.com/pydantic/pydantic-ai/pull/12677#issuecomment-6688486077"
ORIGINAL = "https://master.ricette.jp/theory/nakagawa-master-reconstructive-memory-structure/"


def historical_history_key(run: str, call: str, prior_visible_count: int) -> str:
    """Illustrate the earlier history-count key, with its zero-count spelling."""
    occurrence = f"{prior_visible_count}/" if prior_visible_count else ""
    return f"{run}/{occurrence}{call}.0"


def durable_step_key(run: str, step: int, call: str) -> str:
    """Illustrate the independent author's replacement key (run/step/call)."""
    return f"{run}/{step}/{call}.0"


def _write(root: Path, handle: str, payload: bytes) -> None:
    target = root / handle
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(payload)


def run_probes() -> dict[str, object]:
    first, second = b"FIRST independent tool result\n", b"SECOND independent tool result\n"
    with tempfile.TemporaryDirectory(prefix="spill-handle-probe-") as tmp:
        root = Path(tmp)
        # Negative: a history-count key works until compression removes call_0
        # from the visible messages. The second response reuses call_0, even
        # though it is a different real call with different bytes.
        before = historical_history_key("run", "call_0", 0)
        without_compaction = historical_history_key("run", "call_0", 1)
        after_compaction = historical_history_key("run", "call_0", 0)
        assert without_compaction != before
        assert after_compaction == before
        _write(root, before, first)
        _write(root, after_compaction, second)
        assert (root / before).read_bytes() == second
        assert list((root / "run").rglob("*.0")) == [root / before]

        # Positive: the model-request step survives a history rewrite and
        # identifies the separately issued call, independently of which earlier
        # messages remain visible.
        fixed_root = root / "fixed"
        old_handle = durable_step_key("run", 1, "call_0")
        new_handle = durable_step_key("run", 3, "call_0")
        _write(fixed_root, old_handle, first)
        _write(fixed_root, new_handle, second)
        assert old_handle != new_handle
        assert (fixed_root / old_handle).read_bytes() == first
        assert (fixed_root / new_handle).read_bytes() == second

        # Non-fit control: distinct call IDs do not collide in this scenario,
        # even under the earlier history-count key after compaction.
        other_id = historical_history_key("run", "call_9", 0)
        assert other_id != before
        _write(root, other_id, second)
        assert (root / before).read_bytes() == second
        assert (root / other_id).read_bytes() == second

        return {
            "fixture": "synthetic history-count versus durable-step spill paths",
            "old_without_compaction_distinct": before != without_compaction,
            "old_after_compaction_overwrites_first": before == after_compaction,
            "new_after_compaction_keeps_both_results": True,
            "distinct_tool_ids_do_not_collide": other_id != before,
            "historical_paths": [before, after_compaction],
            "corrected_paths": [old_handle, new_handle],
            "sources": {"review": REVIEW, "independent_author_reproduction": AUTHOR, "conceptual_original": ORIGINAL},
            "limit": "This script tests the keying invariant only; the PR author, not this fixture, ran the real Agent and compaction integration. No installed-user, merge or release claim.",
        }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="machine-readable results for independent checking")
    args = parser.parse_args()
    checks = run_probes()
    if args.json:
        print(json.dumps(checks, ensure_ascii=False, indent=2))
    else:
        print("PASS: history-count key is distinct without compression")
        print("FAILURE REPRODUCED: after compression the older key is reused and its bytes overwritten")
        print("PASS: run-step key preserves both results despite compression")
        print("PASS: different tool IDs are a non-collision control")
        print(f"Reviewer: {REVIEW}")
        print(f"Independent author's real-Agent confirmation: {AUTHOR}")
        print("This offline fixture is not a Pydantic AI integration test or proof of release.")


if __name__ == "__main__":
    main()
