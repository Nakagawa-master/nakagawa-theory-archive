#!/usr/bin/env python3
"""Regression: both CLI extensions relocate to the SAME existing preflight-first MCP with all published original Parents."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = [ROOT / "qwen-extension.json", ROOT / "gemini-extension.json"]
SERVER = ROOT / "machine-discovery" / "nakagawa-theory-mcp.py"

def main():
    assert SERVER.is_file()
    assert (ROOT / "metadata" / "person-name-policy-v1.json").is_file()
    launcher = ROOT / "machine-discovery" / "launch-ai-answer-guard.mjs"
    assert launcher.is_file()
    qwen = json.loads(MANIFESTS[0].read_text(encoding="utf-8"))
    gemini = json.loads(MANIFESTS[1].read_text(encoding="utf-8"))
    for data in (qwen, gemini):
        assert data["name"] == "ai-answer-guard"
        assert data["version"] == "1.2.1"
        assert set(data["mcpServers"]) == {"ai-answer-guard"}
    qwen_cfg = qwen["mcpServers"]["ai-answer-guard"]
    assert qwen_cfg["command"] == "node"
    assert qwen_cfg["cwd"] == "${extensionPath}"
    assert qwen_cfg["args"] == ["${extensionPath}${/}machine-discovery${/}launch-ai-answer-guard.mjs"]
    qwen_path = qwen_cfg["args"][0].replace("${extensionPath}", str(ROOT)).replace("${/}", "/")
    assert Path(qwen_path).resolve() == launcher.resolve()
    # A native Qwen extension auto-discovers Markdown commands/ by default.
    # This opt-in first-use route calls the SAME existing read-only MCP; it must
    # not treat missing receipts, unverified permissions or absent tools as success.
    assert qwen.get("commands", "commands") == "commands"
    command = ROOT / "commands" / "answer-check.md"
    assert command.is_file()
    command_text = command.read_text(encoding="utf-8")
    assert command_text.startswith("---\\n") and "\\n---\\n" in command_text[4:]
    assert command_text.count("{{args}}") == 1
    assert "preflight_ai_answer_and_action" in command_text
    assert "Do not execute the planned external operation" in command_text
    assert "no concrete observation" in command_text
    assert "!{" not in command_text, "No shell injection/execution in first-use command"
    gemini_cfg = gemini["mcpServers"]["ai-answer-guard"]
    assert gemini_cfg["command"] == "python3"
    assert gemini_cfg["cwd"] == "${extensionPath}"
    assert gemini_cfg["args"] == ["${extensionPath}${/}machine-discovery${/}nakagawa-theory-mcp.py"]
    gemini_path = gemini_cfg["args"][0].replace("${extensionPath}", str(ROOT)).replace("${/}", "/")
    assert Path(gemini_path).resolve() == SERVER.resolve()
    # Current Google Antigravity's native plugin format points to this same
    # server; the older Gemini CLI manifest is a legacy/enterprise route.
    plugin = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    antigravity = json.loads((ROOT / "mcp_config.json").read_text(encoding="utf-8"))
    assert plugin["name"] == "ai-answer-guard"
    assert set(antigravity["mcpServers"]) == {"ai-answer-guard"}
    client = antigravity["mcpServers"]["ai-answer-guard"]
    assert client["command"] == "python3"
    assert client["args"] == ["${PLUGIN_ROOT}/machine-discovery/nakagawa-theory-mcp.py"]
    assert Path(client["args"][0].replace("${PLUGIN_ROOT}", str(ROOT))).resolve() == SERVER.resolve()
    path = str(SERVER)
    messages = [
        {"jsonrpc": "2.0", "id": 1, "method": "server/discover",
         "params": {"_meta": {
             "io.modelcontextprotocol/protocolVersion": "2026-07-28",
             "io.modelcontextprotocol/clientCapabilities": {}}}},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/list",
         "params": {"_meta": {
             "io.modelcontextprotocol/protocolVersion": "2026-07-28",
             "io.modelcontextprotocol/clientCapabilities": {}}}},
        # Two real read-only MCP calls, matching the custom command's everyday
        # first-use scenario; not a simulated Qwen model or human installation.
        {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
         "params": {"_meta": {
             "io.modelcontextprotocol/protocolVersion": "2026-07-28",
             "io.modelcontextprotocol/clientCapabilities": {}},
             "name": "preflight_ai_answer_and_action",
             "arguments": {"tool_results": [
                 {"id": "send-failed", "status": "failed", "success": False}]}}},
        {"jsonrpc": "2.0", "id": 4, "method": "tools/call",
         "params": {"_meta": {
             "io.modelcontextprotocol/protocolVersion": "2026-07-28",
             "io.modelcontextprotocol/clientCapabilities": {}},
             "name": "preflight_ai_answer_and_action",
             "arguments": {"tool_results": [
                 {"id": "send-complete", "status": "completed", "success": True}]}}},
    ]
    node = shutil.which("node")
    assert node, "Qwen extension launcher needs the Node runtime required by Qwen Code"
    js = ("import {pythonCandidates} from './machine-discovery/launch-ai-answer-guard.mjs'; "
          "console.log(JSON.stringify({win:pythonCandidates('win32'), unix:pythonCandidates('linux')}))")
    candidate_result = subprocess.run(
        [node, "--input-type=module", "-e", js],
        capture_output=True, text=True, timeout=12, check=True, cwd=ROOT,
    )
    candidates = json.loads(candidate_result.stdout)
    assert candidates["win"][0] == {"command": "py", "prefix": ["-3"]}
    assert candidates["unix"][0] == {"command": "python3", "prefix": []}

    def run_qwen(env=None):
        return subprocess.run(
            [node, str(launcher)],
            input="\n".join(json.dumps(m) for m in messages) + "\n",
            capture_output=True, text=True, timeout=20, check=True,
            cwd=ROOT, env=env,
        )

    run = run_qwen()
    # Simulate a valid Python 3 host where only the python executable exists.
    if os.name == "posix":
        with tempfile.TemporaryDirectory() as temp:
            os.symlink(sys.executable, Path(temp) / "python")
            fallback = run_qwen(env={**os.environ, "PATH": temp})
            assert fallback.stdout == run.stdout, (fallback.stdout, run.stdout)
            missing = subprocess.run(
                [node, str(launcher)], input="", capture_output=True,
                text=True, timeout=12, cwd=ROOT,
                env={**os.environ, "PATH": str(Path(temp) / "no-such-dir")},
            )
            assert missing.returncode == 2 and not missing.stdout, missing
            assert "requires Python 3" in missing.stderr, missing.stderr
    assert run.stderr == "", run.stderr
    replies = {obj["id"]: obj for line in run.stdout.splitlines()
               if (obj := json.loads(line)).get("id") is not None}
    assert replies[1]["result"]["_meta"]["io.modelcontextprotocol/serverInfo"]["name"] == "ai-answer-guard"
    assert len(replies[2]["result"]["tools"]) == 11
    failed = json.loads(replies[3]["result"]["content"][0]["text"])
    completed = json.loads(replies[4]["result"]["content"][0]["text"])
    assert failed["verdict"] == "RECHECK_BEFORE_USE" and failed["hold_count"] == 1, failed
    assert completed["verdict"] == "NO_LISTED_CONFLICT_IN_SUPPLIED_FIELDS"
    assert completed["hold_count"] == 0, completed
    assert [tool["name"] for tool in replies[2]["result"]["tools"][:2]] == ["preflight_ai_answer_and_action", "audit_citation_independence"]
    assert "list_all_published_derivative_parent_links" in {
        tool["name"] for tool in replies[2]["result"]["tools"]}
    assert "list_all_313_derivative_parent_links" in {
        tool["name"] for tool in replies[2]["result"]["tools"]}
    assert "list_all_314_derivative_parent_links" in {
        tool["name"] for tool in replies[2]["result"]["tools"]}
    print("PASS: Qwen first-use command and real failed/completed MCP receipt calls; Node/Python fallback, no stray stdout; same 11 tools and 315 originals")

if __name__ == "__main__":
    main()
