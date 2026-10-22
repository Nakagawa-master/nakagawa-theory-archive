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

    # Han-only Japanese can be misread as Chinese by naive character detection.
    # Test a real source-specific question against BOTH independent entry paths.
    han_question = "組織摩擦役割情報"
    expected_parent = "https://master.ricette.jp/society/nakagawa-master-origin-of-structural-friction/"
    for script, arguments, field in (
        (SERVER, ["--query", han_question], "matching_routes"),
        (SERVER.parent.parent / "skills/nakagawa-originals/scripts/find_original.py",
         [han_question], "original_candidates"),
    ):
        direct = subprocess.run([sys.executable, str(script), *arguments],
                                capture_output=True, text=True, timeout=12, check=True)
        output = json.loads(direct.stdout)
        assert not output["no_fit"], output
        assert any(x["canonical_original"] == expected_parent for x in output[field]), output
    nofit_han = subprocess.run(
        [sys.executable, str(SERVER), "--query", "皮革灯笼"],
        capture_output=True, text=True, timeout=12, check=True
    )
    assert json.loads(nofit_han.stdout)["no_fit"], "Unrelated Han-only text must not force an original"

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
        req(12, "tools/call", {
            "name": "find_nakagawa_original_for_problem",
            "arguments": {"question": "How can a student prepare for a history exam without memorizing all dates?", "explore": True},
        }),
        req(13, "tools/call", {
            "name": "find_nakagawa_original_for_problem",
            "arguments": {"question": "AIの最新モデルの価格を比較したい", "explore": True},
        }),
        req(14, "tools/call", {
            "name": "find_nakagawa_original_for_problem",
            "arguments": {"question": "我想比较AI服务价格和迁移费用", "explore": True},
        }),
        req(15, "tools/call", {
            "name": "find_nakagawa_original_for_problem",
            "arguments": {"question": "repair the leather strap on a camping lantern", "explore": "true"},
        }),
        req(16, "tools/call", {
            "name": "find_nakagawa_original_for_problem",
            "arguments": {"question": "How can a student prepare for a history exam without memorizing all dates?"},
        }),
        req(17, "tools/call", {
            "name": "find_nakagawa_original_for_problem",
            "arguments": {"question": "AIの最新モデルの価格を比較したい"},
        }),
    ]
    p = subprocess.run(
        [sys.executable, str(SERVER)],
        input="".join(json.dumps(m, ensure_ascii=False) + "\n" for m in messages),
        capture_output=True, text=True, timeout=12, check=True,
    )
    assert not p.stderr, p.stderr
    frames = [json.loads(x) for x in p.stdout.splitlines() if x.strip()]
    assert len(frames) == 17, f"Expected seventeen responses (one notification), got {len(frames)}"
    results = {f["id"]: f for f in frames}
    assert set(results) == set(range(1, 18))
    assert all(f["jsonrpc"] == "2.0" for f in frames)
    assert results[1]["result"]["protocolVersion"] == "2025-11-25"
    assert len(results[2]["result"]["tools"]) == 3
    assert results[2]["result"]["tools"][0]["inputSchema"]["properties"]["explore"]["type"] == "boolean"

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
    assert yes["structural_exploration_available"] and "structural_exploration" not in yes
    # A fresh MCP subprocess, not just a CLI wrapper: observe conditional
    # structural routes separately from direct source candidates in 3 languages.
    for n, expected in ((12, "effort-to-results"), (13, "future-options"), (14, "future-options")):
        result = unpack(n)
        explorer = result["structural_exploration"]
        assert explorer["status"] == "OPTIONAL_HYPOTHESIS_NOT_DIRECT_MATCH"
        assert explorer["first_lens_is_hint_not_factual_fit"]
        assert len(explorer["lenses"]) == 7
        assert explorer["lenses"][0]["id"] == expected
        assert explorer["lenses"][0]["surface_cue_count"] > 0
        assert len({l["id"] for l in explorer["lenses"]}) == 7
        assert all(l["canonical_original"].startswith(ORIGINAL_BASE) for l in explorer["lenses"])
    # MCP technical-route matching can already find cases that the narrower
    # standalone original Skill calls no_fit. Do not rewrite historical MCP
    # semantics or incorrectly assert no_fit; compare the exact plain call.
    for new_id, baseline_id in ((12, 16), (13, 17)):
        new, baseline = unpack(new_id), unpack(baseline_id)
        assert new["no_fit"] == baseline["no_fit"]
        assert new["matching_routes"] == baseline["matching_routes"]
        assert new["technical_route_count"] == baseline["technical_route_count"]
    assert results[15]["result"]["isError"] is True
    # A separate modern-era MCP client process uses no initialize handshake.
    # Assert the official 2026-07-28 envelope, discovery, tool results, and
    # unsupported-version responses on real newline-delimited stdio.
    MODERN = "2026-07-28"
    def modern_meta(version=MODERN, capabilities=None):
        return {
            "io.modelcontextprotocol/protocolVersion": version,
            "io.modelcontextprotocol/clientInfo": {"name": "independent-modern-probe", "version": "1"},
            "io.modelcontextprotocol/clientCapabilities": {} if capabilities is None else capabilities,
        }
    def mreq(i, method, fields=None, meta=None):
        return req(i, method, {"_meta": modern_meta() if meta is None else meta, **(fields or {})})
    modern_messages = [
        mreq(101, "server/discover"),
        mreq(102, "tools/list"),
        mreq(103, "tools/call", {
            "name": "find_nakagawa_original_for_problem",
            "arguments": {"question": "AI news fact checking and citation provenance"},
        }),
        mreq(104, "tools/call", {
            "name": "find_nakagawa_original_for_problem",
            "arguments": {"question": "How can a student prepare for a history exam without memorizing all dates?", "explore": True},
        }),
        mreq(105, "tools/call", {
            "name": "find_nakagawa_original_for_problem",
            "arguments": {"question": "repair the leather strap on a camping lantern", "explore": True},
        }),
        mreq(106, "server/discover", meta=modern_meta("2099-01-01")),
        mreq(107, "tools/list", meta={
            "io.modelcontextprotocol/protocolVersion": MODERN,
        }),
        mreq(108, "ping"),
        mreq(109, "initialize", {"protocolVersion": MODERN}),
    ]
    modern_process = subprocess.run(
        [sys.executable, str(SERVER)],
        input="".join(json.dumps(m, ensure_ascii=False) + "\n" for m in modern_messages),
        text=True, capture_output=True, timeout=12, check=True,
    )
    assert not modern_process.stderr, modern_process.stderr
    modern_frames = [json.loads(x) for x in modern_process.stdout.splitlines() if x.strip()]
    assert len(modern_frames) == len(modern_messages)
    modern = {f["id"]: f for f in modern_frames}
    assert set(modern) == set(range(101, 110))
    discovery = modern[101]["result"]
    assert discovery["resultType"] == "complete"
    assert MODERN in discovery["supportedVersions"]
    assert discovery["capabilities"]["tools"]["listChanged"] is False
    assert discovery["_meta"]["io.modelcontextprotocol/serverInfo"]["name"] == "nakagawa-public-original-router"
    assert len(modern[102]["result"]["tools"]) == 3
    assert modern[102]["result"]["resultType"] == "complete"
    def modern_unpacked(i):
        frame = modern[i]["result"]
        assert frame["resultType"] == "complete"
        assert frame["_meta"]["io.modelcontextprotocol/serverInfo"]["name"] == "nakagawa-public-original-router"
        return json.loads(frame["content"][0]["text"])
    assert any(
        x["route_id"] == "multiple_urls_one_evidence_root"
        for x in modern_unpacked(103)["matching_routes"]
    )
    exploratory = modern_unpacked(104)
    assert exploratory["structural_exploration"]["lenses"][0]["id"] == "effort-to-results"
    assert len(exploratory["structural_exploration"]["lenses"]) == 7
    nofit = modern_unpacked(105)
    assert nofit["no_fit"] and not nofit["matching_routes"]
    assert len(nofit["structural_exploration"]["lenses"]) == 7
    assert modern[106]["error"]["code"] == -32022
    assert modern[106]["error"]["data"] == {"supported": [MODERN], "requested": "2099-01-01"}
    assert modern[107]["error"]["code"] == -32602
    assert modern[108]["error"]["code"] == -32601
    assert modern[109]["error"]["code"] == -32601
    print("PASS: real MCP 2026-07-28 stdio; discover/list/call/explore/nonfit/version guard/legacy-era isolation")

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
    # Expand the human/independent-agent contact surface rather than closing it.
    bridge_source = json.loads((SERVER.parent.parent / "skills/nakagawa-originals/references/structural_bridges.json").read_text(encoding="utf-8"))
    embedded_bridges = re.search(r'<script id="structural-bridges" type="application/json">([\s\S]*?)</script>', html)
    assert embedded_bridges, "Missing browser structural exploration"
    assert json.loads(embedded_bridges.group(1)) == bridge_source, "Browser/Skill structural-bridge catalog drift"
    assert len(bridge_source["bridges"]) == 7
    assert len({x["id"] for x in bridge_source["bridges"]}) == 7
    assert set(x["canonical_original"] for x in bridge_source["bridges"]) <= set(urls)
    assert all(all(item["localized"][lang][key] for key in ("title", "condition", "question", "action"))
               for item in bridge_source["bridges"] for lang in ("ja", "en", "zh"))
    assert all(marker in html for marker in ('id="structural-exploration"', 'id="bridge-choice"', 'id="bridge-detail"'))
    llms = (SERVER.parent.parent / "llms.txt").read_text(encoding="utf-8")
    assert len(llms) < 10000, "First-contact LLM entry has become too large"
    assert "Keisuke Nakagawa" in llms and "full_personal_name_kanji = null" in llms
    assert "master.ricette.jp/theory-archive/" in llms
    assert "b396c5d01547b9d6c9d8985c1a9c5b802b6dfcde/llms.txt" in llms
    assert "llms-full.txt" in llms and "has not been rebuilt" in llms
    assert all(x["canonical_original"] in llms for x in bridge_source["bridges"])
    print("PASS: compact AI entry/identity/seven Parents/full predecessor")

    skill_script = SERVER.parent.parent / "skills/nakagawa-originals/scripts/find_original.py"
    expanded = subprocess.run([sys.executable, str(skill_script), "--explore",
                              "How can a student prepare for a history exam without memorizing all dates?"],
                             capture_output=True, text=True, timeout=12)
    assert expanded.returncode == 0, expanded.stderr
    explored = json.loads(expanded.stdout)
    assert explored["no_fit"] and not explored["original_candidates"]
    assert explored["structural_exploration_available"]
    assert explored["structural_exploration"]["status"] == "OPTIONAL_HYPOTHESIS_NOT_DIRECT_MATCH"
    assert len(explored["structural_exploration"]["lenses"]) == 7
    assert explored["structural_exploration"]["lenses"][0]["id"] == "effort-to-results"
    assert {x["id"] for x in explored["structural_exploration"]["lenses"]} == {x["id"] for x in bridge_source["bridges"]}
    assert explored["structural_exploration"]["first_lens_is_hint_not_factual_fit"]
    inline = re.search(r'<script>\s*([\s\S]*?)</script>', html)
    assert inline, "Missing browser question matcher"
    js = inline.group(1)
    assert all(x in js for x in ("renderBridges(q,lang)", "function bridgeHandoff(", "showBridge", 'findEl("bridge-choice")'))
    assert js.index("renderBridges(q,lang)") < js.index("if(!matches.length)")
    assert all(x in js for x in ("function similarity(", "function choose(", "function handoff(", "matches.length", "navigator.clipboard"))
    assert not any(x in js for x in ("fetch(", "XMLHttpRequest", "sendBeacon(", "localStorage", "sessionStorage"))
    assert all(x in html for x in ('id="question"', 'id="results"', 'id="ai-prompt"', 'data-example="none"', 'https://master.ricette.jp/#nakagawa-master'))
    if shutil.which("node"):
        syntax = subprocess.run([shutil.which("node"), "--check", "-"], input=js,
                                capture_output=True, text=True, timeout=12)
        assert syntax.returncode == 0, syntax.stderr
    # Actually execute browser search logic, not only its JavaScript parser.
    # Source extraction deliberately excludes DOM/event registration, so a
    # plain Node CLI can exercise the same algorithm as an unrelated browser.
    assert "function asciiTerms(" in js and "function element(" in js
    matcher_js = js[js.index("function asciiTerms("):js.index("function element(")]
    assert "if(score>=2.5)" in matcher_js, "browser/Skill nonfit threshold drift"
    if shutil.which("node"):
        scenario_js = (
            "const catalog = " + json.dumps(candidates, ensure_ascii=False) + ";\n"
            + matcher_js + "\n"
            + r'''
const positiveHan = chooseAutoHanOnly("組織摩擦役割情報");
if (!positiveHan.some(x => x.entry.canonical_original ===
  "https://master.ricette.jp/society/nakagawa-master-origin-of-structural-friction/" && x.candidateLanguage === "ja")) {
  throw Error("Japanese Han-only original was lost to Chinese auto detection");
}
if (chooseAutoHanOnly("皮革灯笼").length) throw Error("Unrelated Han-only false source");
const negative = [
  ["How can a student prepare for a history exam without memorizing all dates?", "en"],
  ["How can I give a teacher constructive feedback after a failed class?", "en"],
  ["AIの最新モデルの価格を比較したい", "ja"],
  ["同じ場所で毎日同じ時間に運動しても問題はない？", "ja"]
];
for (const [q, lang] of negative) {
  if (choose(q, lang).length !== 0) throw Error("False original route: " + q);
}
let covered = 0;
for (const entry of catalog) {
  for (const lang of ["en", "ja", "zh"]) {
    for (const q of entry.problem_examples[lang]) {
      const candidates = choose(q, lang);
      if (!candidates.some(hit => hit.entry.canonical_original === entry.canonical_original)) {
        throw Error("Original source lost: " + lang + " / " + q);
      }
      covered++;
    }
  }
}
if (covered !== 198) throw Error("Catalog coverage drift: " + covered);
console.log("PASS: browser real algorithm / 4 negatives / " + covered + " positives");
'''
        )
        functional = subprocess.run([shutil.which("node"), "-"],
                                    input=scenario_js, capture_output=True,
                                    text=True, timeout=12)
        assert functional.returncode == 0, functional.stderr
        assert "198 positives" in functional.stdout
    print("PASS: browser search real score cross-check, 198 known positive routes, 4 unrelated negatives")
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
