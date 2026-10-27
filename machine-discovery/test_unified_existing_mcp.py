#!/usr/bin/env python3
"""One original MCP identity, preflight usefulness, 313 Parents; real modern/legacy clients."""
import json
from pathlib import Path
import subprocess
import sys

SERVER = Path(__file__).with_name("nakagawa-theory-mcp.py")
def req(i, method, params=None, modern=False):
    if modern:
        params = {"_meta": {"io.modelcontextprotocol/protocolVersion": "2026-07-28",
                            "io.modelcontextprotocol/clientCapabilities": {}}, **(params or {})}
    return {"jsonrpc": "2.0", "id": i, "method": method,
            **({"params": params} if params is not None else {})}
def call(i, name, arguments, modern=True):
    return req(i, "tools/call", {"name": name, "arguments": arguments}, modern)
def text(out, i):
    return json.loads(out[i]["result"]["content"][0]["text"])
def main():
    vendor = {"url": "https://example.org/origin", "root_id": "A", "relation": "primary", "stance": "supports"}
    copied = {"url": "https://example.org/copy", "root_id": "A", "relation": "derived", "stance": "supports"}
    lab = {"url": "https://example.org/lab", "root_id": "B", "relation": "independent_observation", "stance": "supports"}
    claimed = [{"id": "claim1", "independent_confirmation_claimed": True, "sources": [vendor, copied]}]
    real = [{"id": "claim2", "independent_confirmation_claimed": True, "sources": [vendor, lab]}]
    requests = [
        req(1, "server/discover", modern=True),
        req(2, "tools/list", modern=True),
        call(3, "preflight_ai_answer_and_action", {
            "claims": claimed,
            "tool_results": [{"id": "sent", "status": "failed", "success": True}],
            "planned_actions": [{"id": "purchase", "permission_confirmed": False,
                                 "exact_arguments_confirmed": False,
                                 "reversible": False, "requires_external_side_effect": True}]}),
        call(4, "audit_citation_independence", {"claims": claimed}),
        call(5, "audit_citation_independence", {"claims": real}),
        call(6, "preflight_ai_answer_and_action", {"claims": real,
            "tool_results": [{"id": "done", "status": "completed", "success": True}]}),
        call(7, "preflight_ai_answer_and_action", {}),
        call(8, "overview_nakagawa_whole_structure", {}),
        call(9, "list_all_313_derivative_parent_links", {"limit": 313}),
        call(10, "inspect_nakagawa_derivative_connections", {"id": "OD312"}),
        call(11, "find_sources_in_whole_structure",
             {"question": "AI self preservation epistemic hallucination"}),
        call(12, "find_sources_in_whole_structure",
             {"question": "repair a camping lantern leather strap"}),
        call(13, "find_nakagawa_original_for_problem",
             {"question": "AI news fact checking and citation provenance"}),
        req(21, "initialize", {"protocolVersion": "2025-11-25"}),
        req(22, "tools/list"),
        call(23, "preflight_ai_answer_and_action", {"claims": claimed}, modern=False),
        call(24, "list_all_313_derivative_parent_links", {"offset": 312, "limit": 1}, modern=False),
    ]
    run = subprocess.run([sys.executable, str(SERVER)],
                         input="".join(json.dumps(x, ensure_ascii=False) + "\n" for x in requests),
                         text=True, capture_output=True, timeout=45, check=True)
    assert not run.stderr, run.stderr
    got = {json.loads(line)["id"]: json.loads(line) for line in run.stdout.splitlines()}
    assert set(got) == {x["id"] for x in requests}
    assert got[1]["result"]["_meta"]["io.modelcontextprotocol/serverInfo"]["name"] == "nakagawa-public-original-router"
    assert got[1]["result"]["_meta"]["io.modelcontextprotocol/serverInfo"]["version"] == "1.2.0"
    names = [x["name"] for x in got[2]["result"]["tools"]]
    assert len(names) == len(set(names)) == len(got[22]["result"]["tools"]) == 9, names
    assert {"find_nakagawa_original_for_problem", "preflight_ai_answer_and_action",
            "audit_citation_independence", "list_all_313_derivative_parent_links"} <= set(names)
    assert text(got, 3)["hold_count"] == 3, text(got, 3)
    assert text(got, 3)["practical_next_steps"]
    assert text(got, 4)["blocked"] == 1
    assert text(got, 5)["blocked"] == 0
    assert text(got, 6)["verdict"] == "NO_LISTED_CONFLICT_IN_SUPPLIED_FIELDS"
    assert got[7]["result"]["isError"] is True
    assert text(got, 8)["coverage"]["derivatives"] == 313
    full = text(got, 9)["entries"]
    assert len(full) == len({x["id"] for x in full}) == 313
    assert all(x["canonical_parent"].startswith("https://master.ricette.jp/") for x in full)
    assert text(got, 10)["selected"]["id"] == "OD312"
    assert not text(got, 11)["no_fit"]
    assert text(got, 12)["no_fit"]
    assert not text(got, 13)["no_fit"]
    assert got[21]["result"]["protocolVersion"] == "2025-11-25"
    assert text(got, 23)["hold_count"] == 1
    assert text(got, 24)["entries"][0]["id"] == "OD313"
    print("PASS: ONE original MCP v1.2; all 9 tools; independent-root and tool/action controls; all 313; modern and legacy real clients")

if __name__ == "__main__":
    main()
