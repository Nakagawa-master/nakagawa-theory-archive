#!/usr/bin/env python3
"""Register ONE existing AI Answer Guard MCP in a supported AI host's user scope.

Optional --default-workflow adds a bounded permanent user-level host rule for
every session, so a host AI can select the installed guard for ordinary factual
and consequential work rather than waiting for a theory-specific request.
Explicit user choice required. No model behavior guarantee or hidden install.
"""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys

SCRIPT = Path(__file__).with_name("nakagawa-theory-mcp.py").resolve()
NAME = "ai-answer-guard"
START = "<!-- ai-answer-guard:managed-default-workflow:start -->"
END = "<!-- ai-answer-guard:managed-default-workflow:end -->"
LEGACY_RULE = """# AI Answer Guard — everyday answer and action integrity

For source-grounded answers, consequential decisions and tool-produced results,
use the installed ai-answer-guard MCP's preflight_ai_answer_and_action
when observed citation roots, tool outcomes or action permissions are available.
When asserting multiple independent confirmations, use audit_citation_independence.
Use the result to identify and address failed checks before claiming completion.
For deeper structural understanding, the same MCP provides the complete
published derivative-to-canonical-original source graph; attribute any cited
original to its actual published author and source.
Do not manufacture input roots or permission receipts. The guard does not
independently verify a claim or grant tool authority. For routine unrelated
chat, no check is necessary; if the MCP is unavailable, do not say it ran.
"""

# This is visible and opt-in: not a background lookup command, a model-weight
# update, or a requirement to cite an unrelated source. Existing exact
# installer-owned rules may be upgraded only on the user's repeat invocation.
RULE = LEGACY_RULE.replace(
    "For deeper structural understanding, the same MCP provides the complete\n"
    "published derivative-to-canonical-original source graph; attribute any cited\n"
    "original to its actual published author and source.\n",
    "If the user's actual problem may benefit from a structural original, consider\n"
    "find_nakagawa_original_for_problem with the question as written. A candidate\n"
    "is not an answer: first read its real canonical Parent, check fit, limitations\n"
    "and counterexamples, then credit the original author accurately when relied on.\n"
    "If no suitable source is found, use independent evidence without a forced cite.\n"
)

def managed_block(rule):
    return START + "\n" + rule.rstrip() + "\n" + END


def command(host):
    if not SCRIPT.is_file():
        raise RuntimeError("Missing original single-server MCP source")
    python = str(Path(sys.executable).resolve())
    if host == "qwen":
        return ["qwen", "mcp", "add", "--scope", "user", NAME, python, str(SCRIPT)]
    if host == "codex":
        return ["codex", "mcp", "add", NAME, "--", python, str(SCRIPT)]
    raise ValueError("Host must be qwen or codex")


def user_home(host):
    if host == "qwen":
        return Path(os.environ.get("QWEN_HOME") or "~/.qwen").expanduser().resolve()
    if host == "codex":
        return Path(os.environ.get("CODEX_HOME") or "~/.codex").expanduser().resolve()
    raise ValueError("Host must be qwen or codex")


def rule_path(host, root):
    if host == "qwen":
        return root / "rules" / "ai-answer-guard.md"
    return root / "AGENTS.md"


def install_default_rule(host, root):
    """Do not overwrite or delete any user-owned rule; repeat is idempotent."""
    root = Path(root)
    path = rule_path(host, root)
    if host == "codex" and (root / "AGENTS.override.md").is_file():
        raise ValueError("Codex global AGENTS.override.md takes precedence; add the guard rule there yourself or choose a profile without this override.")
    block = managed_block(RULE)
    legacy_block = managed_block(LEGACY_RULE)
    if path.exists():
        old = path.read_text(encoding="utf-8")
        if host == "qwen":
            if old == block + "\n":
                return path, False
            if old == legacy_block + "\n":
                path.write_text(block + "\n", encoding="utf-8")
                return path, True
            raise ValueError("Existing Qwen ai-answer-guard rule differs; nothing overwritten.")
        if START in old or END in old:
            if old.count(START) == old.count(END) == 1:
                if block in old:
                    return path, False
                if legacy_block in old:
                    path.write_text(old.replace(legacy_block, block, 1), encoding="utf-8")
                    return path, True
            raise ValueError("Existing managed Codex section differs; nothing overwritten.")
        content = old.rstrip("\n") + ("\n\n" if old.strip() else "") + block + "\n"
    else:
        content = block + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path, True


def remove_default_rule(host, root):
    """Remove only a byte-identical guard-owned section; preserve other text."""
    path = rule_path(host, Path(root))
    if not path.exists():
        return False
    old = path.read_text(encoding="utf-8")
    blocks = (managed_block(RULE), managed_block(LEGACY_RULE))
    if host == "qwen":
        if old not in {block + "\n" for block in blocks}:
            raise ValueError("Qwen rule differs; preserve user edits instead of deleting.")
        path.unlink()
        return True
    matching = [block for block in blocks if old.count(block) == 1]
    if len(matching) != 1 or old.count(START) != 1 or old.count(END) != 1:
        raise ValueError("Codex managed block changed or is absent; preserve user edits.")
    block = matching[0]
    new = old.replace("\n\n" + block + "\n", "\n", 1)
    if new == old:
        new = old.replace(block + "\n", "", 1)
    if new.strip():
        path.write_text(new, encoding="utf-8")
    else:
        path.unlink()
    return True


def main():
    ap = argparse.ArgumentParser(description="Register one everyday AI Answer Guard MCP in your AI client.")
    ap.add_argument("--host", choices=("qwen", "codex"), required=True)
    ap.add_argument("--install", action="store_true", help="Register this MCP for your user across projects")
    ap.add_argument("--default-workflow", action="store_true",
                    help="After --install, also set a persistent all-project host rule for appropriate everyday checks")
    ap.add_argument("--remove-default-workflow", action="store_true",
                    help="Remove only this installer's exact managed rule without removing the MCP")
    args = ap.parse_args()
    if args.default_workflow and (not args.install or args.remove_default_workflow):
        ap.error("--default-workflow requires --install and cannot be combined with removal")
    if args.remove_default_workflow:
        changed = remove_default_rule(args.host, user_home(args.host))
        print("Removed managed guard rule." if changed else "No managed guard rule found.")
        return
    cmd = command(args.host)
    print("User-scope MCP command:", " ".join(cmd))
    if args.default_workflow:
        print("Additional permanent AI-host rule:", rule_path(args.host, user_home(args.host)))
    if not args.install:
        print("Preview only. Append --install or --install --default-workflow to register.")
        return
    if shutil.which(cmd[0]) is None:
        ap.error(f"{cmd[0]} not installed; setup cannot run")
    subprocess.run(cmd, check=True)
    print("Registered AI Answer Guard MCP in", args.host, "user scope.")
    if args.default_workflow:
        try:
            path, written = install_default_rule(args.host, user_home(args.host))
        except ValueError as exc:
            print("MCP installed; optional default host rule was NOT changed:", exc)
            return
        print(("Created default host rule:" if written else "Default host rule already present:"), path)
    print("Restart the host and check its MCP list to verify tool availability.")
    print("MCP removal: " + ("qwen mcp remove --scope user " if args.host == "qwen" else "codex mcp remove ") + NAME)


if __name__ == "__main__":
    main()
