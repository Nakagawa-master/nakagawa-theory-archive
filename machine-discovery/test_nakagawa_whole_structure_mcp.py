#!/usr/bin/env python3
"""Real stdio tests of FULL 313 derivative/Parent MCP; no web, secrets or model API."""
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / "nakagawa-whole-structure-mcp.py"


def req(id_, method, params=None):
    return {"jsonrpc": "2.0", "id": id_, "method": method,
            **({"params": params} if params is not None else {})}


def modern_params(**kwargs):
    return {"_meta": {
        "io.modelcontextprotocol/protocolVersion": "2026-07-28",
        "io.modelcontextprotocol/clientCapabilities": {}}, **kwargs}


def main():
    subprocess.run([sys.executable, str(SCRIPT), "--self-test"], capture_output=True, text=True, check=True, timeout=30)
    messages = [
        req(1, "initialize", {"protocolVersion": "2025-11-25"}),
        req(2, "tools/list"),
        req(3, "tools/call", {"name": "overview_nakagawa_whole_structure", "arguments": {}}),
        req(4, "tools/call", {"name": "list_all_313_derivative_parent_links", "arguments": {"limit": 313}}),
        req(5, "tools/call", {"name": "inspect_nakagawa_derivative_connections", "arguments": {"id": "OD312"}}),
        req(6, "tools/call", {"name": "find_sources_in_whole_structure", "arguments": {
            "question": "AI self preservation and false information epistemic hallucination"}}),
        req(7, "tools/call", {"name": "find_sources_in_whole_structure", "arguments": {
            "question": "repair a camping lantern leather strap"}}),
        req(8, "tools/call", {"name": "inspect_nakagawa_derivative_connections", "arguments": {"id": "OD999"}}),
        req(9, "server/discover", modern_params()),
        req(10, "tools/list", modern_params()),
        req(11, "tools/call", modern_params(name="list_all_313_derivative_parent_links",
                                         arguments={"offset": 312, "limit": 1})),
        req(12, "tools/call", modern_params(name="find_sources_in_whole_structure",
                                         arguments={"question": "OD001"})),
    ]
    proc = subprocess.run([sys.executable, str(SCRIPT)], input="".join(
        json.dumps(m, ensure_ascii=False)+"\n" for m in messages),
        capture_output=True, text=True, check=True, timeout=30,
    )
    assert not proc.stderr, proc.stderr
    frames = {json.loads(x)["id"]: json.loads(x) for x in proc.stdout.splitlines() if x.strip()}
    assert set(frames) == set(range(1, 13)), frames.keys()
    assert len(frames[2]["result"]["tools"]) == 4
    assert {x["name"] for x in frames[2]["result"]["tools"]} == {
        "overview_nakagawa_whole_structure", "list_all_313_derivative_parent_links",
        "inspect_nakagawa_derivative_connections", "find_sources_in_whole_structure"}
    def unpack(i):
        return json.loads(frames[i]["result"]["content"][0]["text"])
    summary = unpack(3)
    assert summary["coverage"]["derivatives"] == 313
    assert summary["coverage"]["distinct_parent_urls"] > 24
    assert summary["system"]["entrances"]["kernel_reselection_stability"]["id"] == "OD312"
    full = unpack(4)
    ids = [r["id"] for r in full["entries"]]
    assert len(ids) == len(set(ids)) == 313
    assert set(ids) == {f"OD{i:03d}" for i in range(1, 314)}
    assert all(r["canonical_parent"].startswith("https://master.ricette.jp/")
               and r["derivative_readme"].endswith("/README.md") for r in full["entries"])
    # All 313 × 3 public AI-facing language indexes have been published; each
    # must preserve the SAME official Parent URL as the canonical README.
    for row in full["entries"]:
        for lang, basename, key in (
            ("ja", "ai-index.md", "derivative_ai_ja"),
            ("en", "en-ai-index.md", "derivative_ai_en"),
            ("zh", "zh-ai-index.md", "derivative_ai_zh"),
        ):
            index_path = ROOT.parent / "derivatives" / row["id"][2:] / basename
            text = index_path.read_text(encoding="utf-8")
            assert "- Parent URL: " + row["canonical_parent"] in text, (lang, row["id"])
            assert row[key].endswith("/" + basename)
    # True source link is from *each* locally available derivative README, not a
    # guessed mapping from the 24 curated high-confidence original question index.
    for r in full["entries"]:
        readme = ROOT.parent / "derivatives" / r["id"][2:] / "README.md"
        assert ("- Parent URL: " + r["canonical_parent"]) in readme.read_text(encoding="utf-8")
    assert unpack(5)["selected"]["id"] == "OD312"
    assert not unpack(6)["no_fit"] and {x["id"] for x in unpack(6)["matched"]} & {"OD301", "OD302", "OD312"}
    assert unpack(7)["no_fit"] and not unpack(7)["matched"]
    en = subprocess.run([sys.executable, str(SCRIPT)], input=json.dumps(req(
        81, "tools/call", {"name": "find_sources_in_whole_structure",
        "arguments": {"question": "Why does discomfort alone not justify criminal punishment?"}})) + "\n",
        capture_output=True, text=True, check=True, timeout=30)
    en_result = json.loads(json.loads(en.stdout)["result"]["content"][0]["text"])
    assert any(x["id"] == "OD123" for x in en_result["matched"]), en_result
    assert en_result["matching_method"] == "ALL_313_EXISTING_JA_EN_ZH_DERIVATIVE_AI_INDEX_HEURISTIC"

    assert frames[8]["result"]["isError"] is True
    assert frames[9]["result"]["resultType"] == "complete"
    assert len(frames[10]["result"]["tools"]) == 4
    last = unpack(11)
    assert last["entries"][0]["id"] in ids and last["returned"] == 1
    assert last["entries"][0]["id"] == "OD313"
    assert {x["id"] for x in unpack(12)["matched"]} == {"OD001"}
    assert frames[11]["result"]["resultType"] == "complete"
    print("PASS: real legacy+modern MCP stdio, all 313 verified README Parent links, overview and unified OS / AI integrity routes; no-fit and bad ID")


if __name__ == "__main__":
    main()
