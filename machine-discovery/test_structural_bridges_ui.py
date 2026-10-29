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
SOURCE_CATALOG = ROOT / "machine-discovery/problem-to-theory-origin-index-v1.json"
BRIDGES = ROOT / "skills/nakagawa-originals/references/structural_bridges.json"
SKILL = ROOT / "skills/nakagawa-originals/scripts/find_original.py"
SHAREABLE = ROOT / "human-translation/QUESTIONS_TO_STRUCTURE.md"

def main():
    html = HTML.read_text(encoding="utf-8")
    match = re.search(r'<script>\s*([\s\S]*?)</script>', html)
    assert match
    js = match.group(1)
    originals = json.loads(DIRECT.read_text(encoding="utf-8"))
    source = json.loads(SOURCE_CATALOG.read_text(encoding="utf-8"))
    embedded_tag = '<script id="catalog" type="application/json">'
    visible = json.loads(html.split(embedded_tag, 1)[1].split("</script>", 1)[0])
    assert len(visible) == len(source["entries"]) == 24
    by_url = {e["canonical_url"]: e for e in source["entries"]}
    assert len(by_url) == 24
    assert set(by_url) == {e["canonical_original"] for e in visible}
    for entry in visible:
        canonical = by_url[entry["canonical_original"]]
        assert entry["problem_examples"] == {
            "en": canonical["problem_phrases"],
            "ja": canonical["problem_phrases_ja"],
            "zh": canonical["problem_phrases_zh"],
        }, entry["canonical_original"]
    assert sum(len(e["problem_examples"][lang]) for e in visible
               for lang in ("en", "ja", "zh")) > 210

    bridges = json.loads(BRIDGES.read_text(encoding="utf-8"))
    embedded = json.loads(re.search(
        r'<script id="structural-bridges" type="application/json">([\s\S]*?)</script>', html).group(1))
    assert embedded == bridges
    official = {x["canonical_original"] for x in originals["entries"]}
    assert len(bridges["bridges"]) == 7
    assert all(x["canonical_original"] in official for x in bridges["bridges"])
    assert len({x["id"] for x in bridges["bridges"]}) == 7
    # A GitHub-readable, install-free human and ordinary-browsing-AI entry
    # must preserve all 21 exact localized conditional questions and 7 Parents.
    reader = SHAREABLE.read_text(encoding="utf-8")
    # Verify the seven conditional lenses *within each language's own section*.
    # The introductory human examples may legitimately cite the same Parents;
    # whole-file URL counts would reject useful examples despite intact lenses.
    section_headers = (
        ("ja", "## 日本語：日常の疑問を因果構造へ"),
        ("en", "## English: Go from a daily problem to a causal question"),
        ("zh", "## 中文：把日常问题变成可验证的结构问题"),
    )
    assert reader.count("\n### ") == 21
    for i, (lang, heading) in enumerate(section_headers):
        assert reader.count(heading) == 1
        scope = reader.split(heading, 1)[1]
        if i + 1 < len(section_headers):
            next_heading = section_headers[i + 1][1]
            assert next_heading in scope
            scope = scope.split(next_heading, 1)[0]
        assert scope.count("\n### ") == 7
        for item in bridges["bridges"]:
            assert scope.count(item["canonical_original"]) == 1
            view = item["localized"][lang]
            assert all(view[k] in scope for k in ("title", "condition", "question", "action"))
    for front in ("README.md", "AI_START_HERE.md", "llms.txt"):
        assert "QUESTIONS_TO_STRUCTURE.md" in (ROOT / front).read_text(encoding="utf-8")
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
        assert obj["structural_exploration"]["lenses"][0]["id"] == ("future-options" if lang == "ja" else "effort-to-results" if lang == "en" else "independent-evidence")
        assert len({x["id"] for x in obj["structural_exploration"]["lenses"]}) == 7
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
                  "status", "bridge-choice", "bridge-hint", "bridge-detail", "find",
                  "ai-prompt", "copy-status", "copy", "open-chatgpt", "share-ai",
                  "find-all-titles", "all-title-status", "all-title-results"]) elements[id] = node(id);
// Guard against any network access until the optional 313-title button is clicked.
globalThis.fetch = () => { throw Error("Unexpected browser GET without explicit title-search click"); };
elements["share-ai"].hidden = true; // Reflect production [hidden] when native share is unavailable.
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
    bootstrap = bootstrap.replace("ORIGINAL_CATALOG", json.dumps(json.dumps(visible, ensure_ascii=False), ensure_ascii=False))
    bootstrap = bootstrap.replace("BRIDGE_CATALOG", json.dumps(json.dumps(bridges, ensure_ascii=False), ensure_ascii=False))
    checks = r'''
// The 24 offline search path is independently usable without static-313 GET.
if(!elements["find-all-titles"].listeners.click) throw Error("Optional 313-title click handler missing");
if(elements["all-title-results"].children.length) throw Error("Title search ran before click");
// Newly indexed risk questions previously unreachable in the HTML browser.
const riskCases = [
 ["How could an AI shutdown or containment action increase catastrophic risk by destroying another agent's only viable recovery resources?", "en", "09-self-preservation-mutual-existence-conflict"],
 ["高风险AI智能体被停止或撤销许可后重启，若旧的人类批准迟到，如何阻止其重新生效？", "zh", "nakagawa-master-goi-no-kioku"],
 ["AI制御や倫理審査が失敗したとき、事故報告を異議・救済・制度変更へ実際につなげるには？", "ja", "07-ai-civilization-institutional-loop"]
];
for (const [q, lang, source] of riskCases) {
 const hits = choose(q, lang);
 if (!hits.some(x => x.entry.canonical_original.includes(source)))
   throw Error("Missing new canonical Parent for "+lang+": "+source);
}
elements.question.value = "How can a student prepare for a history exam without memorizing all dates?";
elements.language.value = "en";
elements.find.listeners.click();
if (elements["structural-exploration"].hidden) throw Error("No-fit closed expansion");
if (elements.results.children.length) throw Error("False direct source match");
if (elements["bridge-choice"].children.length !== 8) throw Error("Missing seven choices");
if (elements["bridge-choice"].value !== "effort-to-results") throw Error("Context did not activate the study lens");
if (!elements["bridge-hint"].textContent.includes("問いの表現")) throw Error("Context hint not displayed");
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
// Opt-in ChatGPT takes the current edited source-bound draft, not an old template.
// This minimal DOM never opens an external window or sends a message.
const handoffDraft = elements["ai-prompt"].value;
const open = elements["open-chatgpt"];
if (!open.listeners.click) throw Error("Missing optional AI opening control");
open.listeners.click({currentTarget:open, preventDefault(){throw Error("Unexpected handoff block");}});
if (open.href !== "https://chatgpt.com/?q=" + encodeURIComponent(handoffDraft))
  throw Error("User-edited original-linked question was not handed off correctly");
if (elements["share-ai"].hidden !== true || !elements["share-ai"].listeners.click)
  throw Error("Native share opt-in not hidden on unsupported runtimes");
elements["ai-prompt"].value = "private".repeat(2000);
let blockedLong = false;
open.listeners.click({currentTarget:open, preventDefault(){blockedLong = true;}});
if (!blockedLong) throw Error("Oversize URL should fall back to copying");
elements["ai-prompt"].value = handoffDraft;
elements.question.value = "How can AI systems remain auditable and correctable without losing provenance?";
elements.find.listeners.click();
if (!elements.results.children.length) throw Error("Direct match lost");
if (elements["structural-exploration"].hidden) throw Error("Expansion disappeared after direct match");
// The semantic contact surface activates a conditional lens, without
// dropping any other lens or overwriting a user's actual question.
const contexts = [
  ["How can I give a teacher constructive feedback after a failed class?", "en", "verifiable-authority"],
  ["AIの最新モデルの価格を比較したい", "ja", "future-options"],
  ["同じ場所で毎日同じ時間に運動しても問題はない？", "ja", "effort-to-results"],
  ["我想比较AI服务价格和迁移费用", "zh", "future-options"]
];
for(const [q, lang, expected] of contexts){
 elements.question.value=q;elements.language.value=lang;elements.find.listeners.click();
 if(elements["bridge-choice"].value!==expected)throw Error("Wrong surfaced lens: "+q+" => "+elements["bridge-choice"].value);
 if(elements["bridge-choice"].children.length!==8)throw Error("Lost an alternative lens: "+q);
 const links=elements["bridge-detail"].children.filter(x=>x.tag==="a");
 if(links.length!==1||!links[0].href.startsWith("https://master.ricette.jp/"))throw Error("No canonical parent: "+q);
}
elements.question.value="repair the leather strap on a camping lantern";elements.language.value="en";
elements.find.listeners.click();
if (elements["bridge-choice"].value !== "" || elements["bridge-choice"].children.length !== 8) 
  throw Error("Noncontext prompt must keep all open choices without forced selection");
if (!elements["bridge-hint"].textContent.includes("7経路")) throw Error("Noncontext options not advertised");
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
