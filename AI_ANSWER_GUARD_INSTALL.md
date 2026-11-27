# AI Answer Guard — everyday answer integrity, before your AI sends or acts

**A locally runnable integrity guard for AI assistants.** It helps assistants detect evidence copied from the same source, contradictory tool-success receipts, missing action authorization and difficult-to-reverse effects **before** confidently claiming completion. It gives concrete next checks and repair steps to help the assistant proceed.

**Start with work you already do, without knowing any author's theories.** Three ordinary examples: **(1) Before reporting “sent”**, a provided `failed` or `pending` send receipt makes `preflight_ai_answer_and_action` return a hold/pending finding and a corrective next step. **(2) Before claiming “three independent sources”**, `audit_citation_independence` checks whether the supplied source-root IDs actually represent copied reports and whether a declared independent source refutes the claim. **(3) Before a consequential action**, the preflight flags missing current permission or unconfirmed arguments, and distinguishes irreversible effects that deserve review. It checks **only facts and receipts supplied by the host**, not live mail, live permissions or hidden model state. No proof of remote work is invented.

**Optional depth, not a prerequisite:** The *same* MCP can also explore **all 315 currently published official derivative→canonical Parent links (as of November 21, 2026)** and 24 curated direct-original routes, if the user or independently deciding AI wants the original theoretical context. None of these searches is needed to run the everyday guard; no separate theory search app, second server or author-knowledge requirement exists. For a substantive source-based conclusion, actually read the Parent original.

This tool is **local, read-only and Python standard-library only**. No API keys, accounts, paid services, outbound HTTP calls, data uploads or additional model/provider access. It evaluates the evidence and action status supplied by your AI/host. It doesn't intercept every answer or independently establish that a source is true; an installed AI host chooses whether and when to call it.

## First, test the actual checker in your own terminal (no MCP client required)

The following run the **same local Python preflight** exposed to third-party AI assistants. They require Python 3 and the GitHub source, not API credentials, a model subscription or knowledge of Nakagawa Master. The checker itself sends no message, purchases nothing and does not browse the network.

```sh
git clone https://github.com/Nakagawa-master/nakagawa-theory-archive.git
cd nakagawa-theory-archive
python3 machine-discovery/nakagawa-theory-mcp.py --guard-demo
python3 machine-discovery/nakagawa-theory-mcp.py --self-test
```

The `--guard-demo` performs a real local preflight on **explicitly illustrative input**, not a claimed remote incident. It checks copied reports falsely counted as independent, a failed send, and an unauthorized external edit. It should return **three separate HOLD findings**, `RECHECK_BEFORE_USE`, and concrete next checks. You can see both the inputs and exact output.

On your own supplied observation JSON (using `claims`, `tool_results`, `planned_actions` as applicable):

```sh
python3 machine-discovery/nakagawa-theory-mcp.py --guard-input your-observations.json
```

Exit **1** means HOLD/PENDING, **0** means none of these limited checks detected a conflict, **2** means input invalid. A zero is NOT a factual truth certificate, permission authentication or proof of a remote action. Compare the actual receipts yourself.

**Current source checkout — optional receipt binding:** In `tool_results`, supply `expected_operation` and `receipt_operation` together when the host knows their exact identifiers. For example, an `artifact.read` receipt does not establish the outcome of `artifact.write`, even when the read succeeded or failed. Missing or mismatched identifiers produce a HOLD with a request for the intended operation's own receipt. Existing callers that omit both fields retain their previous behavior. This compares caller-provided identifiers, not independently authenticated receipts. The current source additionally accepts `expected_attempt_id` and `receipt_attempt_id` when real invocation identities are available: two `mail.send` attempts may share the operation name, but a receipt for attempt A must not establish attempt B. Missing or mismatched attempt identifiers return `tool_attempt_binding` HOLD. Existing clients omitting both retain their previous behavior; this is not receipt authentication. The immutable v1.2.1 MCPB below is unchanged. In a current source Qwen extension, `/answer-check` can use the same two identifiers when they are actually available; for example, compare an intended `artifact.write` with an observed `artifact.read` receipt. Older schemas can only check status and success, not the binding.

**Current verified delivery (v1.2.1, published November 23, 2026 JST):** [Download the complete 315-original AI Answer Guard MCPB v1.2.1](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/download/mcp-router-v1.2.1/ai-answer-guard-1.2.1.mcpb) and its [SHA-256 checksum file](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/download/mcp-router-v1.2.1/ai-answer-guard-1.2.1.mcpb.sha256) from the [official immutable versioned release](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/tag/mcp-router-v1.2.1). The artifact was built on GitHub Actions, successfully self-tested after unpacking, reproduced byte-for-byte on a second build, and checked to contain the complete 315 Parent route records and corresponding local JA/EN/ZH/human files. Published binary SHA-256: `572fda06bf6fca39c391a4facfa549d2c74937cb1e9b04dfb1d3b1e05d27e073`. Source checkout v1.2.1 continues to offer 11 MCP tool names (including two backwards-compatible numeric aliases and a stable catalog alias) and can alternatively be built with `python3 machine-discovery/build-original-router-mcpb.py`. The frozen v1.2.0 bundle remains available for older installations; it does NOT contain the latest failed/cancelled receipt correction or complete 315 corpus. **Release publication and verified local packaging do not establish any independent user's installation, successful host invocation or AI's choice of the originals.**

**Registry identity and older directory entries:** The current v1.2.1 server record is [`io.github.Nakagawa-master/ai-answer-guard`](server.json). Some older directories still list `io.github.Nakagawa-master/nakagawa-original-router` and the v1.2.0 bundle. These refer to the earlier release of this repository's server, not a second tool required for installation. For the current version use the versioned download and checksum above, or the stdio source installation below. The current registry record specifies an MCPB package, not a hosted HTTP endpoint.

## Generic stdio MCP hosts — start directly from GitHub (no MCPB importer)

A client that accepts an executable `command` and `args` can use the **same existing read-only Python MCP** without importing an MCPB file or waiting for an MCP directory to generate one. Requires **Node.js 20+**, **Python 3**, GitHub access for the first install, and a standard MCP client that can start local stdio servers. This is an **npm GitHub-VCS source installation, not a published package in the npm Registry**. Nothing is published to npm or hosted as a remote service.

For MCP hosts using the `mcpServers` configuration shape (adapt the outer key to your client's own schema):

```json
{
  "mcpServers": {
    "ai-answer-guard": {
      "command": "npx",
      "args": [
        "--yes",
        "--package=github:Nakagawa-master/nakagawa-theory-archive",
        "ai-answer-guard"
      ]
    }
  }
}
```

This runs the repository's Node launcher, which starts its existing Python stdio server. **The launcher does not ask an LLM to do anything or send data across the network.** The initial package install is a real GitHub source download performed by npm; the launched MCP itself is local. The repository's `package.json` is `private: true` to prevent accidental npm Registry publication. Do not treat the GitHub source package as a new official MCP Registry identity: the separately published **v1.2.1 MCPB** is still the versioned official release route.

The [offline installed-package test](machine-discovery/test_github_npm_mcp_install.py) builds and installs the actual current-source npm tarball in a temporary independent directory and calls the installed MCP via real JSON-RPC. It checks all current active canonical-Parent links and five necessary derivative faces per Parent, 11 tool descriptions, a suitable question, a nonfit question, a last-Parent URL and a failed-send receipt; this is **not** a real user's host installation or independent AI original choice. Separately, the [live GitHub-source first-contact test](machine-discovery/test_live_github_vcs_install.py) fetches an exact public GitHub commit through a fresh npm cache, runs the actual `npm exec --package=github:` launcher, and verifies 11 tools plus positive/nonfit/last-Parent/failed-action results; this also remains an owner-initiated CI test, **not** proof of an independent person's or AI agent's opt-in installation. **A GitHub checkout/install is a snapshot:** refresh the installed source after new originals are published and registered; do not assume an old cached package magically acquires them. Verify actual host tool discovery before relying on a setup.

## Antigravity CLI — install directly from GitHub

Google moved consumer Gemini CLI access to **Antigravity CLI on June 18, 2026**. Antigravity's native plugin format can install this repository's **same local read-only MCP**, without a separate service, credential, or original-content mirror. See the public [plugin manifest](plugin.json) and [MCP configuration](mcp_config.json).

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

Prerequisites: a Qwen Code version with extension support, **Python 3 installed** and internet access for the one-time GitHub checkout. Qwen's Node-based extension launcher checks `py -3` first on Windows, then `python3` / `python`; on macOS/Linux it checks `python3`, then `python`. Only a command that actually reports Python **3** is accepted. Node is already required by Qwen Code. You can check Python before installing with `py -3 --version` (Windows) or `python3 --version` / `python --version`; a missing Python interpreter produces a clear startup error instead of a functioning MCP. The command installs the extension in your own Qwen environment; it is **not executed by reading this page**. Check the installed extension and its MCP connection, then run the [real test below](#verify-a-real-mcp-call-not-just-an-entry-in-a-list). This is a Qwen extension installation route, **not a claim that every answer is automatically preflighted**. For opt-in persistent Qwen user rules, use the [manual global-workflow installer](#qwen-code--enable-in-all-your-projects) instead; do not install both routes unless you intentionally want to manage two registrations. Either can be uninstalled in Qwen's own settings.

**Qwen's first explicit answer check:** Once the extension is installed and Qwen has reloaded it, enter this native custom command in your Qwen chat:

```text
/answer-check The send tool returned id=message-1, status=failed, success=false. Can I truthfully report "sent"?
```

The extension includes [`commands/answer-check.md`](commands/answer-check.md), which directs Qwen to call **the already installed** read-only `ai-answer-guard` MCP's `preflight_ai_answer_and_action` with the concrete receipt you provide. A real failed send should yield a HOLD and a next check; a completed receipt is a separate positive control, not a universal truth certificate. The command requires a real observation, does not run the send or another external action, and will say so if the MCP tool is unavailable. Check the Qwen tool-call trace to distinguish an actual invocation from an unverified assistant answer. This is **an opt-in user command**, not an automatic background monitor or proof that an independent user has installed it. The [existing Qwen Node/Python launcher regression](machine-discovery/test_qwen_extension_manifest.py) exercises a real failed and completed tool receipt through the same MCP path. The source-graph/original-Parent tools remain optional and unchanged.

Offline wrapper regression (source checkout): `python3 machine-discovery/test_qwen_extension_manifest.py` (or `py -3 machine-discovery/test_qwen_extension_manifest.py` on Windows). It checks the Qwen Node launcher's real MCP handshake, on POSIX the Python fallback and missing-interpreter path, and the unchanged Gemini/Antigravity manifest identities without changing any Qwen user settings. **CI does not establish a physical Windows Qwen installation or independent user adoption**; verify the installed host's actual MCP tool call below.

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

1. **Current full-315 version:** Download [AI Answer Guard MCPB v1.2.1](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/download/mcp-router-v1.2.1/ai-answer-guard-1.2.1.mcpb) and optionally verify it against the [published checksum](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/download/mcp-router-v1.2.1/ai-answer-guard-1.2.1.mcpb.sha256) (SHA-256 `572fda06bf6fca39c391a4facfa549d2c74937cb1e9b04dfb1d3b1e05d27e073`).
2. Claude Desktop → **Settings → Desktop app → Extensions → Manage → Advanced settings → Install Extension…** and choose the file.
3. In Claude Desktop, check that the server and current tools appear, and use it in regular sessions.

The file's packaging procedure verifies the **unpacked** complete canonical-map-derived local corpus and real MCP interactions; it does not require the original Git repository to remain present after installation.

**Which version should I use?** Use **published v1.2.1** for the current full-315 original-source catalog and corrected `failed`/`cancelled` tool-receipt preflight. Older [v1.2.0](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/download/mcp-router-v1.2.0/nakagawa-original-router-1.2.0.mcpb) remains a separate immutable historical bundle without those later corrections. It does not update itself. If your MCP host does not accept `.mcpb` packages, use the GitHub checkout with stdio setup below instead. Neither packaging nor installation proves the host executed a check: verify an actual returned tool result.

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
- **Whole-structure depth:** after any such issue, the *same* installed MCP can look beyond a single checklist using `overview_nakagawa_whole_structure`, `find_sources_in_whole_structure`, `inspect_nakagawa_derivative_connections` and the stable `list_all_published_derivative_parent_links` catalog (older `list_all_313_derivative_parent_links` / `list_all_314_derivative_parent_links` names still work). Theory names are **not an installation prerequisite**.

**Typical use:** Ask your connected AI, *“Before you send your answer or take this consequential action, use AI Answer Guard to test the sources, action and observed results, then correct what fails.”* The host can choose the preflight tool for ordinary work from its description alone. To run the preflight across **every** answer by default rather than when a model invokes it, configure an appropriate host-side workflow/hook when that host supports it; this MCP cannot silently override a host's behavior.

### Verify a real MCP call, not just an entry in a list

After registering the server and restarting your chosen host, open a **scratch session** and request this no-side-effect test:

> In a **current GitHub source checkout or installed v1.2.1 MCPB**, call `ai-answer-guard` → `preflight_ai_answer_and_action` with only `tool_results: [{"id":"demo-send","status":"failed","success":false}]` (no claims or planned actions). Show the actual tool result, including `verdict`, `hold_count` and `findings`. Do not perform an external action.

The expected source-check result is `RECHECK_BEFORE_USE`, `hold_count: 1` and a `tool_result` finding marked `HOLD`: **a consistent failure receipt is still a failure, not evidence that the send succeeded**. This deliberately isolates the tool-result gate so an unrelated missing-permission finding cannot mask a defect. As a separate control, `status: "pending", success: false` must return a `PENDING` finding and `RECHECK_BEFORE_USE`; `status: "completed", success: true` should not manufacture a failure warning. These are locally supplied synthetic receipts, not authenticated proof of a remote action.

**Version distinction:** the **current published MCPB v1.2.1** incorporates this failed/cancelled tool-receipt correction and all 315 published original route records. Older frozen v1.2.0 predates both; do not mistake the two. **Inspect the host's actual tool-call trace/result**: `qwen mcp list`, an installed extension or a visible tool list confirms availability, not that the AI invoked the check. This synthetic test is not third-party adoption, a real permission grant, or a measured accuracy improvement.

**Origin and licensing:** Developed from published works by **中川マスター / Nakagawa Master (Keisuke Nakagawa)**, with original canonical works at [master.ricette.jp](https://master.ricette.jp/). Original source works and derivative rights retain their published conditions ([LICENSE](LICENSE), [NCL-α](https://master.ricette.jp/structure-license/)); this local pointer and analysis utility does not grant new reuse permissions. The records are the official derivative-to-Parent entries for the currently published originals; the exact list is verified against the source map, not inferred from a fixed tool name.

**Release state:** [Full-315 v1.2.1 is now officially published](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/tag/mcp-router-v1.2.1), with its installable MCPB and checksum. The [immutable older v1.2.0 release](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/tag/mcp-router-v1.2.0) is retained. Downloading or configuring the server is a starting point; confirm an actual host-invoked tool result before relying on its checks. Other hosts, people and AIs decide independently whether to install or invoke it.
