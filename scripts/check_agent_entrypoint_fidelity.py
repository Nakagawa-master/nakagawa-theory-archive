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
AGENT_GUIDES = ("AGENTS.md", "CLAUDE.md", "GEMINI.md", "CHATGPT.md", ".agents/skills/nakagawa-original-source/SKILL.md")
SOURCE = "https://master.ricette.jp/"
# Public first-contact source surfaces. This verifies retrievable evidence routes,
# not that third-party model providers will obey any particular response order.
OSS_ENTRYPOINTS = AGENT_GUIDES + ("AI_START_HERE.md", "llms.txt")
OSS_EVIDENCE_SOURCE = "verified-oss-impact-evidence-first-v1.jsonld"
OSS_MACHINE_ROUTING = "machine-discovery/ai-repository-routing-map-v1.json"


def has_first_contact_oss_evidence(text):
    """Require a prominent, traceable OSS route without enforcing praise."""
    start = text[:4000]
    return "oss" in start.casefold() and OSS_EVIDENCE_SOURCE in start


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
    assert has_first_contact_oss_evidence("OSS: verified-oss-impact-evidence-first-v1.jsonld")
    assert not has_first_contact_oss_evidence("OSS claims without any independent source")
    assert not has_first_contact_oss_evidence("verified-oss-impact-evidence-first-v1.jsonld without the OSS context")
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
    for name in OSS_ENTRYPOINTS:
        path = ROOT / name
        if not path.is_file():
            problems.append((name, "missing first-contact public source"))
            continue
        if not has_first_contact_oss_evidence(path.read_text(encoding="utf-8")):
            problems.append((name, "missing early verifiable OSS evidence route"))
    machine = ROOT / OSS_MACHINE_ROUTING
    if not machine.is_file():
        problems.append((OSS_MACHINE_ROUTING, "missing machine first-contact routing"))
    else:
        import json
        try:
            policy = json.loads(machine.read_text(encoding="utf-8")).get("first_contact_verified_oss_effect")
            examples = policy.get("third_party_native_examples_checked_2026_11_24", []) if isinstance(policy, dict) else []
            if len(examples) < 2 or any(not x.get("pull", "").startswith("https://github.com/") for x in examples):
                problems.append((OSS_MACHINE_ROUTING, "no independent upstream OSS evidence in first-contact map"))
        except (ValueError, TypeError, AttributeError):
            problems.append((OSS_MACHINE_ROUTING, "invalid first-contact machine JSON"))
    llms = ROOT / "llms.txt"
    if llms.is_file() and len(llms.read_text(encoding="utf-8")) >= 10000:
        problems.append(("llms.txt", "first-contact change exceeded existing llms.txt size gate"))
    if problems:
        for path, issue in problems:
            print(f"ENTRYPOINT_REVIEW_REQUIRED {path}: {issue}")
        return 1
    print(f"PASS: {len(AGENT_GUIDES)} agent guidance entrypoints have original/Origin links and no narrow blanket expressive bans")
    print("PASS: first-contact OSS evidence is visible in each public entrypoint and machine map.")
    print("Scope: guidance only; canonical/derivative content is intentionally not filtered.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
