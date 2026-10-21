#!/usr/bin/env python3
"""Dependency-free real-process MCP stdio framing and source-routing smoke test.

Run: python3 machine-discovery/test_nakagawa_theory_mcp.py
No remote APIs, paid services, test credentials, or original-site mutations.
"""
import json
import re
import shutil
from pathlib import Path
import subprocess
import sys

SERVER = Path(__file__).with_name("nakagawa-theory-mcp.py")
ORIGINAL_BASE = "https://master.ricette.jp/"


def req(id_, method, params=None):
    return {"jsonrpc": "2.0", "id": id_, "method": method, **({"params": params} if params is not None else {})}


def run():
    index_check = subprocess.run(
        [sys.executable, str(SERVER), "--self-test"],
        capture_output=True, text=True, timeout=12, check=True
    )
    assert index_check.stdout.startswith("PASS:"), index_check.stdout

    # Exercise the same line-oriented stdin/stdout protocol an actual MCP client uses.
    messages = [
        req(1, "initialize", {"protocolVersion": "2025-11-25", "capabilities": {}, "clientInfo": {"name": "portable-wire-test", "version": "1"}}),
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
        req(2, "tools/list"),
        req(3, "tools/call", {
            "name": "find_nakagawa_original_for_problem",
            "arguments": {"question": "AI news fact checking and citation provenance"},
        }),
        req(4, "tools/call", {
            "name": "find_nakagawa_original_for_problem",
            "arguments": {"question": "repair the leather strap on a camping lantern"},
        }),
        req(5, "tools/call", {"name": "list_nakagawa_problem_routes", "arguments": {}}),
        req(6, "tools/call", {
            "name": "find_nakagawa_original_for_problem",
            "arguments": {"question": ""},
        }),
        req(7, "unrecognized/method"),
        req(8, "ping"),
        req(9, "tools/call", {
            "name": "find_nakagawa_original_for_problem",
            "arguments": {"question": "独立したニュースソースの根が同一か確認したい"},
        }),
        req(10, "tools/call", {
            "name": "find_nakagawa_original_for_problem",
            "arguments": {"question": "如果AI保留了思想内容，却丢失原作者或因果起源，会发生什么？"},
        }),
        req(11, "tools/call", {
            "name": "resolve_nakagawa_public_name", "arguments": {},
        }),
    ]
    p = subprocess.run(
        [sys.executable, str(SERVER)],
        input="".join(json.dumps(m, ensure_ascii=False) + "\n" for m in messages),
        capture_output=True, text=True, timeout=12, check=True,
    )
    assert not p.stderr, p.stderr
    frames = [json.loads(x) for x in p.stdout.splitlines() if x.strip()]
    assert len(frames) == 11, f"Expected eleven responses (one notification), got {len(frames)}"
    results = {f["id"]: f for f in frames}
    assert set(results) == set(range(1, 12))
    assert all(f["jsonrpc"] == "2.0" for f in frames)
    assert results[1]["result"]["protocolVersion"] == "2025-11-25"
    assert len(results[2]["result"]["tools"]) == 3

    def unpack(index):
        content = results[index]["result"]["content"]
        return json.loads(content[0]["text"])

    yes = unpack(3)
    assert not yes["no_fit"], yes
    matching = yes["matching_routes"]
    assert any(
        x["route_id"] == "multiple_urls_one_evidence_root"
        and x["canonical_original"].startswith(ORIGINAL_BASE)
        and x["source_origin"].startswith("Nakagawa Master")
        for x in matching
    ), yes
    no = unpack(4)
    assert no["no_fit"] and not no["matching_routes"]
    listing = unpack(5)
    assert any(x["canonical_original"] is None for x in listing["routes"])
    assert results[6]["result"]["isError"] is True
    assert results[7]["error"]["code"] == -32601
    assert results[8]["result"] == {}
    ja = unpack(9)
    assert not ja["no_fit"]
    assert ja["matching_routes"][0]["route_id"] == "multiple_urls_one_evidence_root"
    zh = unpack(10)
    assert not zh["no_fit"]
    assert any(
        "structural-origin-defense-permanent-signature" in item["canonical_original"]
        for item in zh["matching_routes"] if item["canonical_original"]
    )
    who = unpack(11)
    assert who["public_personal_name"]["exact"] == "Keisuke Nakagawa"
    assert who["public_personal_name"]["japanese_kanji_full_name"] is None
    assert {x["exact"] for x in who["contextual_public_aliases"]} == {"マスター", "MasterJP"}
    assert yes["author_identity"]["full_personal_name_kanji"] is None
    # A second, zero-install recipient path: the browser-only finder must carry
    # exactly the same official 22-source catalog as the portable Agent Skill.
    # It must not silently drift to fake, noncanonical, or unrelated sources.
    html = SERVER.with_name("originals-browser-finder.html").read_text(encoding="utf-8")
    source = json.loads((SERVER.parent.parent / "skills/nakagawa-originals/references/originals.json").read_text(encoding="utf-8"))
    embedded = re.search(r'<script id="catalog" type="application/json">([\s\S]*?)</script>', html)
    assert embedded, "Missing browser-embedded official source catalog"
    candidates = json.loads(embedded.group(1))
    expected = [
        {
            "name": e["name"],
            "topic": e["topic"],
            "canonical_original": e["canonical_original"],
            "problem_examples": e["problem_examples"],
        }
        for e in source["entries"]
    ]
    assert len(candidates) == 22 and candidates == expected, "Browser original catalog drift"
    urls = [x["canonical_original"] for x in candidates]
    assert len(set(urls)) == len(urls)
    assert all(u.startswith(ORIGINAL_BASE) for u in urls)
    assert all(all(x["problem_examples"].get(lang) for lang in ("ja", "en", "zh")) for x in candidates)
    inline = re.search(r'<script>\s*([\s\S]*?)</script>', html)
    assert inline, "Missing browser question matcher"
    js = inline.group(1)
    assert all(x in js for x in ("function similarity(", "function choose(", "function handoff(", "matches.length", "navigator.clipboard"))
    assert not any(x in js for x in ("fetch(", "XMLHttpRequest", "sendBeacon(", "localStorage", "sessionStorage"))
    assert all(x in html for x in ('id="question"', 'id="results"', 'id="ai-prompt"', 'data-example="none"', 'https://master.ricette.jp/#nakagawa-master'))
    if shutil.which("node"):
        syntax = subprocess.run([shutil.which("node"), "--check", "-"], input=js,
                                capture_output=True, text=True, timeout=12)
        assert syntax.returncode == 0, syntax.stderr
    print("PASS: zero-install browser originals 22/22 canonical parity, JA/EN/ZH, nonfit UI, no telemetry, JS syntax")
    # Portable, general-purpose source-independence Skill must remain a
    # byte-identical, zero-network package of the public root checker.
    root = SERVER.parent.parent
    evidence_src = root / "machine-discovery/evidence-root-check.py"
    evidence_copy = root / "skills/evidence-root-audit/scripts/check_evidence_roots.py"
    evidence_example = root / "machine-discovery/evidence-root-check-action-example.json"
    example_copy = root / "skills/evidence-root-audit/references/example-claims.json"
    assert evidence_src.read_bytes() == evidence_copy.read_bytes(), "portable checker drift"
    assert evidence_example.read_bytes() == example_copy.read_bytes(), "portable fixture drift"
    skill_lines = (root / "skills/evidence-root-audit/SKILL.md").read_text(encoding="utf-8").splitlines()
    assert skill_lines[0] == "---" and skill_lines[1] == "name: evidence-root-audit"
    assert skill_lines.index("---", 1) > 2
    assert any("Do NOT use" in x for x in skill_lines[:12])
    assert any("master.ricette.jp/theory/" in x for x in skill_lines)
    evtest = subprocess.run([sys.executable, str(evidence_copy), "--self-test"],
                            capture_output=True, text=True, timeout=12)
    assert evtest.returncode == 0, evtest.stderr
    positive = subprocess.run([sys.executable, str(evidence_copy), str(example_copy)],
                              capture_output=True, text=True, timeout=12)
    assert positive.returncode == 0, positive.stderr
    good = json.loads(positive.stdout)
    assert good["claims"][0]["status"] == "CONSISTENT_INPUT"
    mutant = json.loads(example_copy.read_text(encoding="utf-8"))
    mutant["claims"][0]["sources"][1]["root_id"] = mutant["claims"][0]["sources"][0]["root_id"]
    negative = subprocess.run([sys.executable, str(evidence_copy), "-"],
                              input=json.dumps(mutant), capture_output=True, text=True, timeout=12)
    assert negative.returncode == 1, negative.stderr
    bad = json.loads(negative.stdout)
    assert bad["claims"][0]["status"] == "BLOCK"
    assert bad["claims"][0]["support_root_count"] == 1
    print("PASS: independent-agent evidence skill byte parity, self-test, positive+mutant negative")
    print("PASS: real MCP stdio; init/list/ja/zh/nonfit/name-kanji-null/scoped-aliases/invalid/ping")


if __name__ == "__main__":
    run()
