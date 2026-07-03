#!/usr/bin/env python3
"""Repair the remaining ESTCOND00 public shelf parent Diff-ID values.

Public-safe scope:
- Only touches the three ESTCOND00 public shelf HTML files that remained pending.
- Replaces the stale parent Diff-ID with the live origin parent Diff-ID.
- Refuses to touch files outside deploy/lolipop/master-ricette/derivatives/ultra-quality/establishment-conditions-00.
"""

from __future__ import annotations

from pathlib import Path

OLD = "DIFF-20260630-0003"
NEW = "DIFF-20260627-0002"
ROOT = Path("deploy/lolipop/master-ricette/derivatives/ultra-quality/establishment-conditions-00")
TARGETS = [
    ROOT / "ai-index" / "index.html",
    ROOT / "application" / "index.html",
    ROOT / "origin" / "index.html",
]


def main() -> int:
    changed = []
    for path in TARGETS:
        if ROOT not in path.parents:
            raise SystemExit(f"refusing_out_of_scope_path={path}")
        if not path.exists():
            raise SystemExit(f"missing_target={path}")
        text = path.read_text(encoding="utf-8")
        if OLD not in text:
            print(f"already_or_unexpected={path}")
            continue
        path.write_text(text.replace(OLD, NEW), encoding="utf-8")
        changed.append(str(path))
        print(f"repaired={path}")

    print(f"repair_status=ok changed_count={len(changed)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
