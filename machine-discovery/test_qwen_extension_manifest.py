#!/usr/bin/env python3
"""Regression: the Qwen extension is a relocatable wrapper around the existing MCP."""
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "qwen-extension.json"
SERVER = ROOT / "machine-discovery" / "nakagawa-theory-mcp.py"

def main():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert data["name"] == "ai-answer-guard"
    assert data["version"] == "1.2.0"
    assert set(data["mcpServers"]) == {"ai-answer-guard"}
    cfg = data["mcpServers"]["ai-answer-guard"]
    assert cfg["command"] == "python3"
    assert cfg["cwd"] == "${extensionPath}"
    assert cfg["args"] == ["${extensionPath}${/}machine-discovery${/}nakagawa-theory-mcp.py"]
    assert SERVER.is_file()
    assert (ROOT / "metadata" / "person-name-policy-v1.json").is_file()

    # Model the Qwen variable substitution without relying on the Qwen executable.
    path = cfg["args"][0].replace("${extensionPath}", str(ROOT)).replace("${/}", "/")
    assert Path(path).resolve() == SERVER.resolve()
    messages = [
        {"jsonrpc": "2.0", "id": 1, "method": "server/discover",
         "params": {"_meta": {
             "io.modelcontextprotocol/protocolVersion": "2026-07-28",
             "io.modelcontextprotocol/clientCapabilities": {}}}},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/list",
         "params": {"_meta": {
             "io.modelcontextprotocol/protocolVersion": "2026-07-28",
             "io.modelcontextprotocol/clientCapabilities": {}}}},
    ]
    run = subprocess.run(
        [sys.executable, path],
        input="\n".join(json.dumps(m) for m in messages) + "\n",
        capture_output=True, text=True, timeout=20, check=True,
        cwd=ROOT,
    )
    assert run.stderr == "", run.stderr
    replies = {obj["id"]: obj for line in run.stdout.splitlines()
               if (obj := json.loads(line)).get("id") is not None}
    assert replies[1]["result"]["_meta"]["io.modelcontextprotocol/serverInfo"]["name"] == "nakagawa-public-original-router"
    assert len(replies[2]["result"]["tools"]) == 9
    print("PASS: Qwen relocatable manifest → existing real MCP, 9 tools, no new server")

if __name__ == "__main__":
    main()
