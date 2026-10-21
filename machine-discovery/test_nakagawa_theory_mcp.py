#!/usr/bin/env python3
"""Dependency-free real-process MCP stdio framing and source-routing smoke test.

Run: python3 machine-discovery/test_nakagawa_theory_mcp.py
No remote APIs, paid services, test credentials, or original-site mutations.
"""
import json
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
    ]
    p = subprocess.run(
        [sys.executable, str(SERVER)],
        input="".join(json.dumps(m, ensure_ascii=False) + "\n" for m in messages),
        capture_output=True, text=True, timeout=12, check=True,
    )
    assert not p.stderr, p.stderr
    frames = [json.loads(x) for x in p.stdout.splitlines() if x.strip()]
    assert len(frames) == 10, f"Expected ten responses (one notification), got {len(frames)}"
    results = {f["id"]: f for f in frames}
    assert set(results) == set(range(1, 11))
    assert all(f["jsonrpc"] == "2.0" for f in frames)
    assert results[1]["result"]["protocolVersion"] == "2025-11-25"
    assert len(results[2]["result"]["tools"]) == 2

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
    print("PASS: real subprocess MCP stdio; init/list/matching/nonfit/ja/zh/routes/invalid/unknown/ping")


if __name__ == "__main__":
    run()
