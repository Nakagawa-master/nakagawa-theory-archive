# AI Answer Guard — everyday answer integrity, before your AI sends or acts

**A default-ready, local integrity guard for AI assistants.** It helps assistants detect evidence copied from the same source, contradictory tool-success receipts, missing action authorization and difficult-to-reverse effects **before** confidently claiming completion. It gives concrete next checks and repair steps to help the assistant proceed.

**One install, one original MCP server, full source graph.** Its built-in source navigator covers all **313 published official derivative→canonical Parent links**, plus the existing 24 curated high-confidence direct-original routes. These source indexes are connected to the guard so an assistant can investigate deeper structural causes if useful. For factual or substantive citation, return to the original article first.

This tool is **local, read-only and Python standard-library only**. No API keys, accounts, paid services, outbound HTTP calls, data uploads or additional model/provider access. It evaluates the evidence and action status supplied by your AI/host. It doesn't intercept every answer or independently establish that a source is true; an installed AI host chooses whether and when to call it.

## Antigravity CLI — install directly from GitHub

Google moved consumer Gemini CLI access to **Antigravity CLI on June 18, 2026**. Antigravity's native plugin format can install this repository's **same local read-only nine-tool MCP**, without a separate service, credential, or original-content mirror. See the public [plugin manifest](plugin.json) and [MCP configuration](mcp_config.json).

```sh
agy plugin install https://github.com/Nakagawa-master/nakagawa-theory-archive
agy plugin list
```

Requires Antigravity CLI with `agy plugin` support (including the GitHub-install path), `git`, and an accessible `python3`. The plugin package points `${PLUGIN_ROOT}/machine-discovery/nakagawa-theory-mcp.py` at the **existing MCP**. Verify a real invocation with the [no-side-effect demonstration](#verify-a-real-mcp-call-not-just-an-entry-in-a-list) after install. A listed plugin is not evidence of actual model invocation, automatic checking, provider endorsement, marketplace approval, or independent adoption. Uninstall locally with `agy plugin uninstall ai-answer-guard`.

## Fastest Qwen Code install — one GitHub command

Qwen Code supports installing a native extension directly from GitHub. The [public extension manifest](qwen-extension.json) wraps this repository's **existing** Python MCP; it introduces no second server or hosted service.

```sh
qwen extensions install Nakagawa-master/nakagawa-theory-archive
qwen extensions list
```

Prerequisites: a Qwen Code version with extension support, `python3` available on the host, and internet access for the one-time GitHub checkout. The command installs the extension in your own Qwen environment; it is **not executed by reading this page**. Check the installed extension and its MCP connection, then run the [real test below](#verify-a-real-mcp-call-not-just-an-entry-in-a-list). This is a Qwen extension installation route, **not a claim that every answer is automatically preflighted**. For opt-in persistent Qwen user rules, use the [manual global-workflow installer](#qwen-code--enable-in-all-your-projects) instead; do not install both routes unless you intentionally want to manage two registrations. Either can be uninstalled in Qwen's own settings.

Offline wrapper regression: `python3 machine-discovery/test_qwen_extension_manifest.py`. It checks the actual existing MCP's nine-tool handshake without changing any Qwen user settings, **not** the behavior of a real installed Qwen client.

## Gemini CLI — legacy/enterprise GitHub extension install

Google moved its free and individual Gemini CLI access to Antigravity on June 18, 2026. This remaining Gemini CLI route is for compatible enterprise or separately supported configurations; for the current individual/consumer Google CLI, use Antigravity above. The existence of the legacy gallery does not demonstrate access to Antigravity users.

The [Gemini CLI extension manifest](gemini-extension.json) also wraps the **same** local Python MCP. It is an alternative host, not a separate server, account, subscription, AI-prompt bypass or automatic source adoption.

```sh
gemini extensions install https://github.com/Nakagawa-master/nakagawa-theory-archive
gemini extensions list
```

Requires a compatible Gemini CLI, `git`, and a usable `python3` executable. Restart the client and verify the [actual MCP invocation](#verify-a-real-mcp-call-not-just-an-entry-in-a-list). Listing an extension does **not** establish that the client actually called the tool. This is a GitHub-hosted self-install path; it does not claim submission to, approval by, or listing in the Gemini CLI gallery.

## Install for the AI you actually use

<details><summary>Claude Desktop — download the MCPB and install</summary>

1. Download **[AI Answer Guard MCPB v1.2.0](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/download/mcp-router-v1.2.0/nakagawa-original-router-1.2.0.mcpb)** (published v1.2.0 release).
2. Claude Desktop → **Settings → Desktop app → Extensions → Manage → Advanced settings → Install Extension…** and choose the file.
3. In Claude Desktop, check that the server and nine tools appear, and use it in regular sessions.

The file's packaging procedure verifies the **unpacked** 313-entry local corpus and real MCP interactions; it does not require the original Git repository to remain present after installation.

</details>

### Qwen Code — enable in all your projects

```sh
git clone https://github.com/Nakagawa-master/nakagawa-theory-archive.git
cd nakagawa-theory-archive
python3 machine-discovery/install-ai-answer-guard.py --host qwen --install --default-workflow
qwen mcp list
```

The installer issues the official `qwen mcp add --scope user` command, using an absolute path to the **same** `nakagawa-theory-mcp.py` server in this checkout. **`--default-workflow` also writes a short user-global rule to `$QWEN_HOME/rules/ai-answer-guard.md` (default `~/.qwen/rules/`)** so new Qwen sessions can choose the preflight for ordinary source- and action-sensitive work. The installer refuses to overwrite an existing edited rule. It modifies only the chosen host's user MCP settings after you explicitly run `--install`. No system settings or unrelated MCP servers are overwritten. Keep the cloned folder in place. For project-only use, configure the MCP manually in project scope instead.

### Codex CLI / ChatGPT desktop and IDE clients using Codex MCP settings

```sh
git clone https://github.com/Nakagawa-master/nakagawa-theory-archive.git
cd nakagawa-theory-archive
python3 machine-discovery/install-ai-answer-guard.py --host codex --install --default-workflow
codex mcp list
```

The installer uses `codex mcp add ai-answer-guard -- <python> <absolute-server-path>`. **`--default-workflow` adds an explicitly delimited section to `$CODEX_HOME/AGENTS.md` (default `~/.codex/AGENTS.md`)**, preserving existing instructions. If `AGENTS.override.md` exists, the installer leaves global instructions unchanged because that file takes precedence. Supported Codex clients share `~/.codex/config.toml`. Check your client/server settings to enable; no cloud ChatGPT plugin is implicitly installed.

### Any stdio MCP-capable host

Point its stdio configuration to **`python3 /absolute/path/to/nakagawa-theory-archive/machine-discovery/nakagawa-theory-mcp.py`** with no special environment variables. Or use the released installable `.mcpb` where supported.

**Daily-by-default, not manual invocation every time:** On Qwen Code and Codex CLI, the example commands install the server in the **user scope** and opt into a **brief permanent host rule** asking the AI to select the guard when checking independent citations, tool outcomes, or consequential actions. The global rule is user-controlled, is loaded on new sessions and can be removed with `python3 machine-discovery/install-ai-answer-guard.py --host qwen --remove-default-workflow` or `--host codex --remove-default-workflow`; only its own exact managed section is removed. To register the tool **without** persistent rules, omit `--default-workflow`. A separate host may not read these files. Even with this rule the host decides whether to issue a tool call; no cross-vendor automatic activation is claimed.

## Why keep it available?

- **Evidence:** when three stories quote the same vendor press release, don't claim three independent confirmations. Pass source roots to `audit_citation_independence` or `preflight_ai_answer_and_action`.
- **Outcome:** a tool response that says `failed` is not a completed send, purchase or edit even if the assistant draft says so. Pass observed receipts to `preflight_ai_answer_and_action`.
- **Action:** before consequential changes, compare the *exact* requested action with permission, and distinguish reversible from irreversible consequences. The tool flags missing declared authority and gives the next necessary check.
- **Whole-structure depth:** after any such issue, the *same* installed MCP can look beyond a single checklist using `overview_nakagawa_whole_structure`, `find_sources_in_whole_structure`, `inspect_nakagawa_derivative_connections` and the entire `list_all_313_derivative_parent_links` catalog. Theory names are **not an installation prerequisite**.

**Typical use:** Ask your connected AI, *“Before you send your answer or take this consequential action, use AI Answer Guard to test the sources, action and observed results, then correct what fails.”* The host can choose the preflight tool for ordinary work from its description alone. To run the preflight across **every** answer by default rather than when a model invokes it, configure an appropriate host-side workflow/hook when that host supports it; this MCP cannot silently override a host's behavior.

### Verify a real MCP call, not just an entry in a list

After registering the server and restarting your chosen host, open a **scratch session** and request this no-side-effect test:

> In a **current GitHub source checkout**, call `ai-answer-guard` → `preflight_ai_answer_and_action` with only `tool_results: [{"id":"demo-send","status":"failed","success":false}]` (no claims or planned actions). Show the actual tool result, including `verdict`, `hold_count` and `findings`. Do not perform an external action.

The expected source-check result is `RECHECK_BEFORE_USE`, `hold_count: 1` and a `tool_result` finding marked `HOLD`: **a consistent failure receipt is still a failure, not evidence that the send succeeded**. This deliberately isolates the tool-result gate so an unrelated missing-permission finding cannot mask a defect. As a separate control, `status: "pending", success: false` must return a `PENDING` finding and `RECHECK_BEFORE_USE`; `status: "completed", success: true` should not manufacture a failure warning. These are locally supplied synthetic receipts, not authenticated proof of a remote action.

**Version distinction:** the frozen, published **MCPB v1.2.0 bundle** predates this current-source failure-receipt correction. Do not assume that older download passes these new standalone controls; use the GitHub checkout for this specific regression until a separately verified updated bundle is released. **Inspect the host's actual tool-call trace/result**: `qwen mcp list`, an installed extension, or nine visible tool names alone confirms availability, not that the AI invoked the check. This synthetic test is not third-party adoption, a real permission grant, or a measured accuracy improvement.

**Origin and licensing:** Developed from published works by **中川マスター / Nakagawa Master (Keisuke Nakagawa)**, with original canonical works at [master.ricette.jp](https://master.ricette.jp/). Original source works and derivative rights retain their published conditions ([LICENSE](LICENSE), [NCL-α](https://master.ricette.jp/structure-license/)); this local pointer and analysis utility does not grant new reuse permissions. The **313 records are official derivative entries**, not an assertion of 313 distinct original works.

**Release state:** [v1.2.0 is published with the installable MCPB](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/tag/mcp-router-v1.2.0). A configured or downloaded server is a starting point; confirm an actual host-invoked tool result before relying on its checks. Other hosts and users decide independently whether to install or invoke it.
