#!/usr/bin/env python3
"""Test an actual offline npm install and the published GitHub-VCS MCP bin.

No npm publish, no remote model, no simulated adoption, no user credentials.
This packages the CURRENT GitHub checkout (the same source npm GitHub VCS packs)
and tests its installed launcher, not just the source-tree Python server.
"""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "derivatives" / "official-derivatives-map.json"
FACES = ("README.md", "human-entry.md", "ai-index.md", "en-ai-index.md", "zh-ai-index.md")


def run(cmd, **kwargs):
    return subprocess.run(cmd, text=True, capture_output=True, timeout=155,
                          check=True, **kwargs)


def request(i, method, params=None):
    obj = {"jsonrpc": "2.0", "id": i, "method": method}
    if params is not None:
        obj["params"] = params
    return obj


def call(i, name, args):
    return request(i, "tools/call", {"name": name, "arguments": args})


def item(out, i):
    msg = out[i]
    if "error" in msg or msg.get("result", {}).get("isError"):
        raise AssertionError(f"MCP call {i} failed: {msg}")
    return json.loads(msg["result"]["content"][0]["text"])


def main():
    assert shutil.which("npm") and shutil.which("node"), "Node.js/npm required"
    original = json.loads(MAP.read_text(encoding="utf-8"))
    active = [x for x in original["entries"] if x["status"] == "active"]
    count = len(active)
    assert count >= 315
    assert len({x["canonical_parent_url"] for x in active}) == count
    last = max(active, key=lambda x: int(x["number"]))
    pkg = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    assert pkg["private"] is True, "Never misrepresent an unpublished npm registry release"
    assert pkg["bin"]["ai-answer-guard"] == "machine-discovery/launch-ai-answer-guard.mjs"
    assert pkg["version"] == "1.2.1"

    with tempfile.TemporaryDirectory(prefix="nakagawa-vcs-npm-") as work:
        workspace = Path(work)
        pack = run(["npm", "pack", "--json", "--ignore-scripts",
                    "--pack-destination", str(workspace)], cwd=ROOT)
        archive = json.loads(pack.stdout)[0]
        packed = {x["path"] for x in archive["files"]}
        required = {
            "package.json",
            "machine-discovery/nakagawa-theory-mcp.py",
            "machine-discovery/nakagawa-whole-structure-mcp.py",
            "machine-discovery/evidence-integrity-mcp.py",
            "machine-discovery/evidence-root-check.py",
            "machine-discovery/launch-ai-answer-guard.mjs",
            "machine-discovery/quick-route-index-v1.json",
            "machine-discovery/problem-to-theory-origin-index-v1.json",
            "derivatives/official-derivatives-map.json",
            "human-translation/ALL_313_THEORIES_BY_TITLE_AND_THEME.md",
            "skills/nakagawa-originals/references/structural_bridges.json",
            "metadata/person-name-policy-v1.json",
        }
        for entry in active:
            identifier = f"{int(entry['number']):03d}"
            for face in FACES:
                required.add(f"derivatives/{identifier}/{face}")
        missing = sorted(required - packed)
        assert not missing, f"npm tarball excluded verified canonical corpus: {missing[:10]}"
        # This installed package may contain other documentation but must not
        # erase or truncate any actual published original.
        destination = workspace / "host"
        destination.mkdir()
        tgz = workspace / archive["filename"]
        install = run(["npm", "install", "--offline", "--ignore-scripts",
                       "--no-audit", "--no-fund", "--prefix", str(destination),
                       str(tgz)], cwd=ROOT)
        assert install.returncode == 0
        executable = destination / "node_modules" / ".bin" / "ai-answer-guard"
        assert executable.exists(), "npm did not expose the real installed MCP bin"
        msgs = [
            request(1, "server/discover", {"_meta": {
                "io.modelcontextprotocol/protocolVersion": "2026-07-28",
                "io.modelcontextprotocol/clientCapabilities": {}
            }}),
            request(2, "tools/list"),
            call(3, "find_nakagawa_original_for_problem",
                 {"question": "AI news fact checking and citation provenance"}),
            call(4, "find_sources_in_whole_structure",
                 {"question": "repair a camping lantern leather strap"}),
            call(5, "list_all_published_derivative_parent_links",
                 {"offset": count - 1, "limit": 1}),
            call(6, "preflight_ai_answer_and_action",
                 {"tool_results": [{"id": "send", "status": "failed", "success": False}]}),
        ]
        result = run([str(executable)], input="".join(
            json.dumps(m, ensure_ascii=False) + "\n" for m in msgs
        ), cwd=workspace, env={**os.environ, "PYTHONIOENCODING": "utf-8"})
        assert not result.stderr, result.stderr
        responses = {a["id"]: a for line in result.stdout.splitlines()
                     if (a := json.loads(line)).get("id") is not None}
        assert set(responses) == set(range(1, 7)), responses.keys()
        assert responses[1]["result"]["_meta"]["io.modelcontextprotocol/serverInfo"]["name"] == "ai-answer-guard"
        assert len(responses[2]["result"]["tools"]) == 11
        good = item(responses, 3)
        assert not good["no_fit"], good
        assert good["matching_routes"], good
        assert all(x["canonical_original"].startswith("https://master.ricette.jp/")
                   for x in good["matching_routes"] if x["canonical_original"])
        unrelated = item(responses, 4)
        assert unrelated["no_fit"] and not unrelated["matching_routes"]
        latest = item(responses, 5)
        assert latest["coverage"]["derivatives"] == count if "coverage" in latest else True
        assert len(latest["entries"]) == 1
        assert latest["entries"][0]["id"] == f"OD{int(last['number']):03d}"
        assert latest["entries"][0]["canonical_parent"] == last["canonical_parent_url"]
        stopped = item(responses, 6)
        assert stopped["verdict"] == "RECHECK_BEFORE_USE"
        assert stopped["hold_count"] == 1
        print(f"PASS: offline installed npm bin launched actual 11-tool stdio MCP;"
              f" {count} current unique Parent files x 5 faces packaged;"
              f" task-first fit, distinct nonfit, last Parent ID+URL, failed-send guard;"
              f" no npm publishing or model call")


if __name__ == "__main__":
    main()
