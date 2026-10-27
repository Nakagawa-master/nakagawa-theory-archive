#!/usr/bin/env python3
"""Offline verification of opt-in global host rule and non-destructive rollback."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
TARGET = HERE / "install-ai-answer-guard.py"
spec = importlib.util.spec_from_file_location("one_ai_answer_guard_install", TARGET)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def main():
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        for host in ("qwen", "codex"):
            home = root / host
            if host == "codex":
                home.mkdir()
                (home / "AGENTS.md").write_text("# My existing global instructions\n", encoding="utf-8")
            path, written = module.install_default_rule(host, home)
            assert written and path.exists()
            s = path.read_text(encoding="utf-8")
            assert module.START in s and module.END in s
            assert "preflight_ai_answer_and_action" in s
            assert "list_all_313" not in s  # no massive always-on prompt payload
            if host == "codex":
                assert s.startswith("# My existing global instructions\n")
            again, changed = module.install_default_rule(host, home)
            assert again == path and changed is False
            assert path.read_text(encoding="utf-8") == s
            assert module.remove_default_rule(host, home)
            if host == "codex":
                assert path.read_text(encoding="utf-8") == "# My existing global instructions\n"
            else:
                assert not path.exists()
        qwen = root / "qwen-forked"
        file, _ = module.install_default_rule("qwen", qwen)
        file.write_text("Original customized user rule\n", encoding="utf-8")
        try:
            module.install_default_rule("qwen", qwen)
        except ValueError:
            pass
        else:
            raise AssertionError("Differing Qwen rule may not be replaced")
        try:
            module.remove_default_rule("qwen", qwen)
        except ValueError:
            pass
        else:
            raise AssertionError("Modified Qwen rule may not be deleted")
        assert file.read_text(encoding="utf-8") == "Original customized user rule\n"
        codex = root / "codex-override"
        codex.mkdir()
        (codex / "AGENTS.override.md").write_text("# Existing override\n", encoding="utf-8")
        try:
            module.install_default_rule("codex", codex)
        except ValueError:
            pass
        else:
            raise AssertionError("Precedent AGENTS.override must not be ignored")
        assert not (codex / "AGENTS.md").exists()
    for host in ("qwen", "codex"):
        cmd = subprocess.run([sys.executable, str(TARGET), "--host", host, "--default-workflow"],
                             capture_output=True, text=True, timeout=10)
        assert cmd.returncode != 0, "No host rule without explicit --install"
        preview = subprocess.run([sys.executable, str(TARGET), "--host", host],
                                 capture_output=True, text=True, timeout=10, check=True)
        assert "Preview only." in preview.stdout
        assert "mcp add" in preview.stdout
    print("PASS: Qwen/Codex global everyday rules, idempotence, user-content preservation, override protection, removal, explicit consent and dry-run")


if __name__ == "__main__":
    main()
