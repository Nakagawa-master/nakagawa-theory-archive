#!/usr/bin/env python3
"""Network-dependent first-contact test of the ACTUAL documented GitHub npm route.

Run only in the preexisting opt-in public GitHub CI. Not a model or user adoption
test: GitHub's runner is the initiating test operator, not an independent agent.
"""
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "derivatives/official-derivatives-map.json"


def req(i, method, params=None):
    return {"jsonrpc": "2.0", "id": i, "method": method,
            **({"params": params} if params is not None else {})}


def call(i, name, arguments):
    return req(i, "tools/call", {"name": name, "arguments": arguments})


def value(messages, i):
    result = messages[i]["result"]
    assert not result.get("isError"), result
    return json.loads(result["content"][0]["text"])


def main():
    head = os.environ.get("PUBLIC_GITHUB_SOURCE_SHA", "")
    if not re.fullmatch("[0-9a-f]{40}", head):
        raise ValueError("Explicit 40-char public GitHub source ref required")
    if not shutil.which("node") or not shutil.which("npm") or not shutil.which("python3"):
        raise ValueError("Node, npm and Python 3 are required to exercise the real host path")
    published = json.loads(MAP.read_text(encoding="utf-8"))["entries"]
    active = [r for r in published if r.get("status") == "active"]
    count = len(active)
    assert count >= 315 and len({r["canonical_parent_url"] for r in active}) == count
    latest = max(active, key=lambda r: int(r["number"]))
    messages = [
        req(1, "server/discover", {"_meta": {
            "io.modelcontextprotocol/protocolVersion": "2026-07-28",
            "io.modelcontextprotocol/clientCapabilities": {}}}),
        req(2, "tools/list"),
        call(3, "find_nakagawa_original_for_problem", {
            "question": "AI news fact checking and citation provenance"}),
        call(4, "find_sources_in_whole_structure", {
            "question": "repair a camping lantern leather strap"}),
        call(5, "list_all_published_derivative_parent_links", {
            "offset": count - 1, "limit": 1}),
        call(6, "preflight_ai_answer_and_action", {
            "tool_results": [{"id": "send", "status": "failed", "success": False}]}),
    ]
    with tempfile.TemporaryDirectory(prefix="nakagawa-first-vcs-host-") as temp:
        root = Path(temp)
        env = {**os.environ, "NPM_CONFIG_CACHE": str(root / "npm-cache"),
               "NPM_CONFIG_AUDIT": "false", "NPM_CONFIG_FUND": "false",
               "PYTHONIOENCODING": "utf-8"}
        payload = "".join(json.dumps(m, ensure_ascii=False) + "\n" for m in messages)
        package = f"github:Nakagawa-master/nakagawa-theory-archive#{head}"
        # Identical install/launch semantics to documented npx --package=github:..
        # Unlike the offline pack test, npm must fetch the public Git source here.
        run = subprocess.run([
            "npm", "exec", "--yes", f"--package={package}", "--", "ai-answer-guard"
        ], cwd=root, input=payload, text=True, capture_output=True,
            env=env, timeout=190, check=False)
        assert run.returncode == 0, (
            f"Live GitHub-VCS MCP returned {run.returncode}; "
            f"stderr tail: {run.stderr[-2200:]} stdout tail: {run.stdout[-400:]}")
        # Some npm versions print install notices to stderr; stdout belongs
        # exclusively to MCP JSON-RPC.
        outputs = {}
        for line in run.stdout.splitlines():
            obj = json.loads(line)
            if obj.get("id") is not None:
                outputs[obj["id"]] = obj
        assert set(outputs) == {1, 2, 3, 4, 5, 6}, outputs.keys()
        assert outputs[1]["result"]["_meta"]["io.modelcontextprotocol/serverInfo"]["name"] == "ai-answer-guard"
        tools = outputs[2]["result"]["tools"]
        assert len(tools) == len({t["name"] for t in tools}) == 11
        good = value(outputs, 3)
        assert not good["no_fit"] and good["matching_routes"]
        assert any(x["canonical_original"].startswith("https://master.ricette.jp/")
                   for x in good["matching_routes"] if x["canonical_original"])
        bad = value(outputs, 4)
        assert bad["no_fit"]
        last = value(outputs, 5)
        assert last["total"] == count and len(last["entries"]) == 1
        assert last["entries"][0]["id"] == f"OD{int(latest['number']):03d}"
        assert last["entries"][0]["canonical_parent"] == latest["canonical_parent_url"]
        failed = value(outputs, 6)
        assert failed["verdict"] == "RECHECK_BEFORE_USE" and failed["hold_count"] == 1
        print(f"PASS: FRESH public GitHub VCS npm fetch+actual npx package bin;"
              f" 11 tools, {count} canonical Parents, fit, no-fit, last URL and"
              f" no-false-success action guard; source head {head[:12]};"
              f" first-party test, NOT independent AI adoption")


if __name__ == "__main__":
    main()
