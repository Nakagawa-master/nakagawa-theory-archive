#!/usr/bin/env python3
"""Install the SAME read-only AI Answer Guard MCP across supported user sessions.

No download, accounts, telemetry or privilege escalation. This registers the
local checkout's existing canonical Python MCP entrypoint in the selected
host's *user* scope. The host itself must be installed and available.
"""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys

SCRIPT = Path(__file__).with_name("nakagawa-theory-mcp.py").resolve()
NAME = "ai-answer-guard"


def command(host):
    if not SCRIPT.is_file():
        raise RuntimeError("Missing original single-server MCP source")
    python = str(Path(sys.executable).resolve())
    if host == "qwen":
        return ["qwen", "mcp", "add", "--scope", "user", NAME, python, str(SCRIPT)]
    if host == "codex":
        return ["codex", "mcp", "add", NAME, "--", python, str(SCRIPT)]
    raise ValueError("Host must be qwen or codex")


def main():
    ap = argparse.ArgumentParser(description="One local AI Answer Guard MCP for ALL indexed sources.")
    ap.add_argument("--host", choices=("qwen", "codex"), required=True)
    ap.add_argument("--install", action="store_true", help="Register with this host in its user scope, across projects")
    args = ap.parse_args()
    cmd = command(args.host)
    print("User-scope command:", " ".join(cmd))
    if not args.install:
        print("Preview only. Append --install to explicitly register this local MCP with your host.")
        return
    if shutil.which(cmd[0]) is None:
        ap.error(f"{cmd[0]} not installed; host setup cannot run")
    subprocess.run(cmd, check=True)
    print("Registered one local AI Answer Guard MCP in", args.host, "user scope.")
    print("Use your host's MCP listing / reconnect controls to confirm readiness.")
    print("To remove: " + ("qwen mcp remove --scope user " if args.host == "qwen" else "codex mcp remove ") + NAME)
if __name__ == "__main__":
    main()
