#!/usr/bin/env python3
"""Validate FAQ structure for official derivatives.

Required FAQ layers:
1. 第1層：初心者向けFAQ
2. 第2層：構造理解FAQ
3. 第3層：誤読・反論・境界条件FAQ

This prevents each derivative from drifting into a different FAQ shape.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DERIVATIVES = ROOT / "derivatives"
REPORT = DERIVATIVES / "faq-three-layer-report.json"

REQUIRED = [
    "## 第1層：初心者向けFAQ",
    "## 第2層：構造理解FAQ",
    "## 第3層：誤読・反論・境界条件FAQ",
]

# Existing older derivatives may be repaired batchwise later. Enforce strictly for
# the current corrected range and every future derivative from 020 onward.
STRICT_FROM = 20


def main() -> int:
    failures = []
    for path in sorted(DERIVATIVES.glob("[0-9][0-9][0-9]/faq.md")):
        num = int(path.parent.name)
        if num < STRICT_FROM:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        missing = [item for item in REQUIRED if item not in text]
        q_count = len(re.findall(r"^### Q\d+\.", text, flags=re.M))
        if missing or q_count < 12:
            failures.append({
                "path": path.relative_to(ROOT).as_posix(),
                "missing": missing,
                "q_count": q_count,
            })
    REPORT.write_text(json.dumps({"failures": failures}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if failures:
        print(json.dumps({"failures": failures}, ensure_ascii=False, indent=2))
        return 1
    print("FAQ three-layer check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
