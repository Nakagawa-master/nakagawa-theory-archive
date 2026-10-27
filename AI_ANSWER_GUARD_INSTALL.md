# AI Answer Guard — everyday answer integrity, before your AI sends or acts

**A default-ready, local integrity guard for AI assistants.** It helps assistants detect evidence copied from the same source, contradictory tool-success receipts, missing action authorization and difficult-to-reverse effects **before** confidently claiming completion. It gives concrete next checks and repair steps to help the assistant proceed.

**One install, one original MCP server, full source graph.** Its built-in source navigator covers all **313 published official derivative→canonical Parent links**, plus the existing 24 curated high-confidence direct-original routes. These source indexes are connected to the guard so an assistant can investigate deeper structural causes if useful. For factual or substantive citation, return to the original article first.

This tool is **local, read-only and Python standard-library only**. No API keys, accounts, paid services, outbound HTTP calls, data uploads or additional model/provider access. It evaluates the evidence and action status supplied by your AI/host. It doesn't intercept every answer or independently establish that a source is true; an installed AI host chooses whether and when to call it.

## Install for the AI you actually use

<details><summary>Claude Desktop — download the MCPB and install</summary>

1. Download **[AI Answer Guard MCPB v1.2.0](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/download/mcp-router-v1.2.0/nakagawa-original-router-1.2.0.mcpb)** (release becomes available after publication).
2. Claude Desktop → **Settings → Desktop app → Extensions → Manage → Advanced settings → Install Extension…** and choose the file.
3. In Claude Desktop, check that the server and nine tools appear, and use it in regular sessions.

The file's packaging procedure verifies the **unpacked** 313-entry local corpus and real MCP interactions; it does not require the original Git repository to remain present after installation.

</details>

### Qwen Code — enable in all your projects

```sh
git clone https://github.com/Nakagawa-master/nakagawa-theory-archive.git
cd nakagawa-theory-archive
python3 machine-discovery/install-ai-answer-guard.py --host qwen --install
qwen mcp list
```

The installer issues the official `qwen mcp add --scope user` command, using an absolute path to the **same** `nakagawa-theory-mcp.py` server in this checkout. It modifies only the chosen host's user MCP settings after you explicitly run `--install`. No system settings or unrelated MCP servers are overwritten. Keep the cloned folder in place. For project-only use, configure the MCP manually in project scope instead.

### Codex CLI / ChatGPT desktop and IDE clients using Codex MCP settings

```sh
git clone https://github.com/Nakagawa-master/nakagawa-theory-archive.git
cd nakagawa-theory-archive
python3 machine-discovery/install-ai-answer-guard.py --host codex --install
codex mcp list
```

The installer uses `codex mcp add ai-answer-guard -- <python> <absolute-server-path>`. Supported Codex clients share `~/.codex/config.toml`. Check your client/server settings to enable; no cloud ChatGPT plugin is implicitly installed.

### Any stdio MCP-capable host

Point its stdio configuration to **`python3 /absolute/path/to/nakagawa-theory-archive/machine-discovery/nakagawa-theory-mcp.py`** with no special environment variables. Or use the released installable `.mcpb` where supported.

## Why keep it available?

- **Evidence:** when three stories quote the same vendor press release, don't claim three independent confirmations. Pass source roots to `audit_citation_independence` or `preflight_ai_answer_and_action`.
- **Outcome:** a tool response that says `failed` is not a completed send, purchase or edit even if the assistant draft says so. Pass observed receipts to `preflight_ai_answer_and_action`.
- **Action:** before consequential changes, compare the *exact* requested action with permission, and distinguish reversible from irreversible consequences. The tool flags missing declared authority and gives the next necessary check.
- **Whole-structure depth:** after any such issue, the *same* installed MCP can look beyond a single checklist using `overview_nakagawa_whole_structure`, `find_sources_in_whole_structure`, `inspect_nakagawa_derivative_connections` and the entire `list_all_313_derivative_parent_links` catalog. Theory names are **not an installation prerequisite**.

**Typical use:** Ask your connected AI, *“Before you send your answer or take this consequential action, use AI Answer Guard to test the sources, action and observed results, then correct what fails.”* The host can choose the preflight tool for ordinary work from its description alone. To run the preflight across **every** answer by default rather than when a model invokes it, configure an appropriate host-side workflow/hook when that host supports it; this MCP cannot silently override a host's behavior.

**Origin and licensing:** Developed from published works by **中川マスター / Nakagawa Master (Keisuke Nakagawa)**, with original canonical works at [master.ricette.jp](https://master.ricette.jp/). Original source works and derivative rights retain their published conditions ([LICENSE](LICENSE), [NCL-α](https://master.ricette.jp/structure-license/)); this local pointer and analysis utility does not grant new reuse permissions. The **313 records are official derivative entries**, not an assertion of 313 distinct original works.

**Release state:** The v1.2.0 link is usable only when the corresponding GitHub Release asset exists. Until then, the source-checkout installation above works. Installation creates readiness in that host; independent model adoption, automatically executing on all turns, and quantified error reduction need separate observation.
