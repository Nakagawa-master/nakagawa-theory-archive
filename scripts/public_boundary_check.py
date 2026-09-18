#!/usr/bin/env python3
"""Fail if public files contain terms that strongly indicate private operating-state leakage.

This validator is intentionally conservative. It does not encode or reveal private objectives.
It only blocks public-facing markers that should never be needed in this repository.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_DIRS = {".git"}
TEXT_SUFFIXES = {
    ".md", ".txt", ".json", ".jsonld", ".yml", ".yaml", ".py", ".toml", ".cff"
}

# Public-safe generic leakage markers. Keep this list about *classification*,
# not about private objective contents.
FORBIDDEN = [
    re.compile(r"\bprivate[_ -]?kpi\b", re.I),
    re.compile(r"\binternal[_ -]?objective\b", re.I),
    re.compile(r"\binternal[_ -]?priority\b", re.I),
    re.compile(r"\binternal[_ -]?roadmap\b", re.I),
    re.compile(r"\bprivate[_ -]?roadmap\b", re.I),
    re.compile(r"\bprivate[_ -]?strategy\b", re.I),
    re.compile(r"\bhidden[_ -]?goal\b", re.I),
    re.compile(r"\bprogram[_ -]?state\b", re.I),
    re.compile(r"\bexecution[_ -]?cursor\b", re.I),
    re.compile(r"\bcurrent[_ -]?priority\b", re.I),
    re.compile(r"\bdecisive[_ -]?gaps\b", re.I),
    re.compile(r"\badoption[_ -]?credit\b", re.I),
    re.compile(r"\bcompletion[_ -]?guard\b", re.I),
    re.compile(r"\bowner[_ -]?instruction\b", re.I),
    re.compile(r"\bbrain[_ -]?vault\b", re.I),
]

# Files that document this validator/policy can mention generic classification words.
ALLOW = {
    "PUBLIC_SAFE_BOUNDARY.md",
    "scripts/public_boundary_check.py",
}

def iter_files():
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        rel = p.relative_to(ROOT).as_posix()
        if rel in ALLOW:
            continue
        if p.suffix.lower() in TEXT_SUFFIXES or p.name in {"README", "LICENSE"}:
            yield p, rel

def main() -> int:
    failures = []
    for p, rel in iter_files():
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for rx in FORBIDDEN:
            for m in rx.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                failures.append((rel, line, m.group(0)))
    if failures:
        print("Public-safe boundary check FAILED:")
        for rel, line, token in failures:
            print(f"- {rel}:{line}: {token}")
        return 1
    print("Public-safe boundary check passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
