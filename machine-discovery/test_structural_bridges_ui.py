#!/usr/bin/env python3
"""Execute production structural discovery UI in Node's minimal DOM simulator.

Public-only, offline, no browser install, network, telemetry or API key.
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "machine-discovery" / "originals-browser-finder.html"
DIRECT = ROOT / "skills/nakagawa-originals/references/originals.json"
BRIDGES = ROOT / "skills/nakagawa-originals/references/structural_bridges.json"
SKILL = ROOT / "skills/nakagawa-originals/scripts/find_original.py"

def main():
    html = HTML.read_text(encoding="utf-8")
    match = re.search(r'<script>\s*([\s\S]*?)</script>', html)
    assert match
    js = match.group(1)
    originals = json.loads(DIRECT.read_text(encoding="utf-8"))
    bridges = json.loads(BRIDGES.read_text(encoding="utf-8"))
    embedded = json.loads(re.search(
        r'<script id="structural-bridges" type="application/json">([\s\S]*?)</script>', html).group(1))
    assert embedded == bridges
    official = {x["canonical_original"] for x in originals["entries"]}
    assert len(bridges["bridges"]) == 7
    assert all(x["canonical_original"] in official for x in bridges["bridges"])
    assert len({x["id"] for x in bridges["bridges"]}) == 7
    for b in bridges["bridges"]:
        for lang in ("ja", "en", "zh"):
            assert all(b["localized"][lang][k] for k in ("title", "condition", "question", "action"))
    for lang, question in [
        ("en", "How can a student prepare for a history exam without memorizing all dates?"),
        ("ja", "AIの最新モデルの価格を比較したい"),
        ("zh", "我想规划一次城市旅行，该怎么做？")
    ]:
        result = subprocess.run([sys.executable, str(SKILL), "--explore", question],
                                capture_output=True, text=True, timeout=12)
        assert result.returncode == 0, result.stderr
        obj = json.loads(result.stdout)
        assert obj["language"] == lang
        assert len(obj["structural_exploration"]["lenses"]) == 7
        assert obj["structural_exploration"]["status"] == "OPTIONAL_HYPOTHESIS_NOT_DIRECT_MATCH"
        assert obj["structural_exploration"]["lenses"][0]["id"] == "independent-evidence"
    if not shutil.which("node"):
        print("PASS: Python structural exploration and source parity; Node UI runtime unavailable")
        return

    bootstrap = r'''
"use strict";
const elements = {};
function node(tag) {
  return {
    tag, value: "", textContent: "", hidden: false, children: [], listeners: {},
    append(...nodes) { this.children.push(...nodes); },
    replaceChildren(...nodes) { this.children = [...nodes]; },
    addEventListener(kind, cb) { this.listeners[kind] = cb; },
    get firstChild() { return this.children[0]; },
    focus() {}, select() {}, setAttribute() {},
  };
}
for (const id of ["catalog", "structural-bridges", "question", "language",
                  "results", "handoff", "structural-exploration",
                  "status", "bridge-choice", "bridge-detail", "find",
                  "ai-prompt", "copy-status", "copy"]) elements[id] = node(id);
elements["catalog"].textContent = ORIGINAL_CATALOG;
elements["structural-bridges"].textContent = BRIDGE_CATALOG;
globalThis.document = {
 getElementById: id => elements[id],
 createElement: node,
 querySelectorAll: () => []
};
// Node 22 already exposes a read-only navigator; the click test does not need a mock.
'''
    # Values are inserted as JS source string literals, never network calls.
    bootstrap = bootstrap.replace("ORIGINAL_CATALOG", json.dumps(json.dumps([
        {"name": e["name"], "topic": e["topic"],
         "canonical_original": e["canonical_original"],
         "problem_examples": e["problem_examples"]} for e in originals["entries"]
    ], ensure_ascii=False), ensure_ascii=False))
    bootstrap = bootstrap.replace("BRIDGE_CATALOG", json.dumps(json.dumps(bridges, ensure_ascii=False), ensure_ascii=False))
    checks = r'''
elements.question.value = "How can a student prepare for a history exam without memorizing all dates?";
elements.language.value = "en";
elements.find.listeners.click();
if (elements["structural-exploration"].hidden) throw Error("No-fit closed expansion");
if (elements.results.children.length) throw Error("False direct source match");
if (elements["bridge-choice"].children.length !== 8) throw Error("Missing seven choices");
elements["bridge-choice"].value = "independent-evidence";
elements["bridge-choice"].listeners.change();
const details = elements["bridge-detail"].children;
if (!details.some(x => x.tag === "a" && x.href.includes("epistemic-integrity")))
  throw Error("Official source missing from chosen structural route");
const actions = details.find(x => x.tag === "div");
if (!actions || !actions.children[0].listeners.click) throw Error("Missing AI handoff button");
actions.children[0].listeners.click();
const prompt = elements["ai-prompt"].value;
if (!prompt.includes("optional structural exploration") ||
    !prompt.includes("epistemic-integrity") ||
    !prompt.includes("How can a student prepare for a history exam"))
  throw Error("Structural expansion handoff lost hypothesis, real problem or Parent");
elements.question.value = "How can AI systems remain auditable and correctable without losing provenance?";
elements.find.listeners.click();
if (!elements.results.children.length) throw Error("Direct match lost");
if (elements["structural-exploration"].hidden) throw Error("Expansion disappeared after direct match");
console.log("PASS: production browser no-fit → 7 choices → chosen condition → Parent → AI prompt; direct match preserved");
'''
    run = subprocess.run(["node", "-"], input=bootstrap + "\n" + js + "\n" + checks,
                         capture_output=True, text=True, timeout=12)
    assert run.returncode == 0, run.stderr
    assert "direct match preserved" in run.stdout
    print(run.stdout.strip())
    print("PASS: 7 source-backed cross-domain conditions x 3 languages, no network")

if __name__ == "__main__":
    main()
