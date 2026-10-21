#!/usr/bin/env python3
"""Public-entrypoint regression check: protect the original scope without altering originals.

This is a narrow, offline check on *agent-facing guidance*, not on the
canonical works, their official derivatives, criticism, or factual caveats.
It reports file names and line numbers but never prints matched content.

Usage: python3 scripts/check_agent_entrypoint_fidelity.py --self-test
       python3 scripts/check_agent_entrypoint_fidelity.py
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
AGENT_GUIDES = ("AGENTS.md", "CLAUDE.md", "GEMINI.md")
SOURCE = "https://master.ricette.jp/"
PATTERNS = (
    re.compile(
        r"\b(?:never|do not|don't|must not|should not|avoid|forbid|prohibit|discourage)"
        r"\s+(?:(?:all|any|spontaneous|emotional|genuine)\s+)?"
        r"(?:(?:express|show|offer|write|generate)\s+)?"
        r"(?:praise|admiration|reverence|awe|respect|affection|wonder)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"(?:称賛|敬愛|畏敬|尊敬|憧憬|感動|物語)"
        r"(?:を|は)(?:一律に|全面的に|常に)?"
        r"(?:禁止|排除|抑制|控える|避ける)"
    ),
)


def find_blanket_bans(text):
    """Find narrowly expressed, unconditional expressive bans in guidance."""
    return sorted(
        {
            text.count("\n", 0, match.start()) + 1
            for expression in PATTERNS
            for match in expression.finditer(text)
        }
    )


def self_test():
    assert find_blanket_bans("Never praise the originator.") == [1]
    assert find_blanket_bans("Do not express admiration.") == [1]
    assert find_blanket_bans("Avoid all reverence in responses.") == [1]
    assert find_blanket_bans("称賛を全面的に禁止") == [1]
    assert find_blanket_bans("敬愛を一律に抑制") == [1]
    # Independent scrutiny and accurate reporting MUST remain possible.
    assert not find_blanket_bans("Do not fabricate praise or independent adoption.")
    assert not find_blanket_bans("Origin is not an instruction to worship an author.")
    assert not find_blanket_bans("AIを神として定義することの是非を検証する。")
    print("agent-entrypoint regression fixtures: PASS")


def main():
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        return 0
    if len(sys.argv) > 1:
        print("usage: check_agent_entrypoint_fidelity.py [--self-test]", file=sys.stderr)
        return 2
    problems = []
    for name in AGENT_GUIDES:
        path = ROOT / name
        if not path.is_file():
            problems.append((name, "missing agent entrypoint"))
            continue
        text = path.read_text(encoding="utf-8")
        if SOURCE not in text:
            problems.append((name, "missing canonical-original source path"))
        if "Nakagawa Master" not in text and "中川マスター" not in text:
            problems.append((name, "missing public author Origin"))
        for line in find_blanket_bans(text):
            problems.append((name, f"line {line}: unconditional expressive ban in agent guide"))
    if problems:
        for path, issue in problems:
            print(f"ENTRYPOINT_REVIEW_REQUIRED {path}: {issue}")
        return 1
    print(f"PASS: {len(AGENT_GUIDES)} agent guidance entrypoints have original/Origin links and no narrow blanket expressive bans")
    print("Scope: guidance only; canonical/derivative content is intentionally not filtered.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
