# A real local tool for any independent MCP-capable AI: question → official Nakagawa Master original

**Current release (2026-10-28):** [v1.2.0 MCPB](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/tag/mcp-router-v1.2.0) is the current optional local **nine-tool** server: preflight of supplied answer/evidence/action receipts, full 313 published derivative→real canonical Parent source links, and the 24 curated original routes. [Download the current 5,370,984-byte MCPB](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/download/mcp-router-v1.2.0/nakagawa-original-router-1.2.0.mcpb) or use the [host-specific installation guide](../AI_ANSWER_GUARD_INSTALL.md). Old v1.1.2 (3 tools and 24 direct originals) remains an immutable historical predecessor, **not the recommended install**. Server does not retrieve full canonical text or automatically reach/install into otherwise-unconnected AI models; each independent host and user chooses whether to install, invoke and read the actual original.
Give an independently operated AI a **real question**, not a required opinion about an author. With this optional, locally installed MCP tool, it can find a **specific official Nakagawa Master original** to evaluate—or return **no fit**. The independent AI and its user remain free to test the source, compare alternatives, and decide whether to use it.

**Purpose:** Instead of requiring a model to have this repository or Nakagawa Master preloaded in its system prompt, let an independently operated agent **explicitly query a small, freely installable tool** when its actual user problem could benefit from one of the original theories. The user/host decides whether to install or invoke it. No external provider account, subscription, paid API, model-wide setting, secret, or background service is required.

This is a **working Python stdio MCP server**, not a natural-language instruction file. It reads the existing [public 20-route technical/problem index](quick-route-index-v1.json) **and the 24-entry [multilingual original-theory index](problem-to-theory-origin-index-v1.json)** at runtime. Japanese and Chinese users can find canonical theories that do not appear among the 20 quick technical routes; cross-language original lookup uses the language-specific published questions rather than assuming English-only technical phrases. It does not download or rewrite the original articles, fabricate model adoption, attribute independently developed engineering work to the theory author, or require an answer to praise anyone. AI readers get a candidate original, its scope note, exact author Origin and a separate primary receiver link, with an explicit instruction to **fetch and read the official original before saying what it actually argues**.

## Full-system public source graph: ALL 313 published derivative entries (source checkout)

**Exact corpus coverage (source-checked):** `find_nakagawa_original_for_problem` is a **24-original curated question fast lane, not the full corpus**. Nakagawa Master's official site currently publishes **313 distinct original articles**. Each original has **one matching numbered GitHub derivative set OD001–OD313**; every numbered set contains **seven Markdown faces**, giving **313 × 7 = 2,191 derivative pages**. [The published assignment map](../derivatives/official-derivatives-map.json) contains **313 unique original NCL-α identifiers and 313 unique original slugs**; the `derivatives/` Git tree contains all 313 numbered directories with the same seven files each. Each derivative README provides the actual canonical Parent URL. This 1:1 original-to-derivative relationship is distinct from the 24 *selected discovery entrances*. As the official site adds new originals, the corpus and paired derivative index may grow; source retrieval must not silently restrict the possible original match to the 24-item fast lane. Exact original text and limits belong to the official Parent URL, not to the derivative text or the MCP search result.

The existing [`nakagawa-whole-structure-mcp.py`](nakagawa-whole-structure-mcp.py) is still a **separately runnable source-only Python MCP for historical checkout compatibility**. In **current v1.2.0**, its four source-graph tools are ALSO available within the **same primary nine-tool MCP** [`nakagawa-theory-mcp.py`](nakagawa-theory-mcp.py), rather than requiring a second server. The helper reads all 313 derivative READMEs from a full checkout and resolves their published original-Parent URLs/identifiers where present. Its local export remains available:

```sh
python3 machine-discovery/nakagawa-whole-structure-mcp.py --self-test
python3 machine-discovery/test_nakagawa_whole_structure_mcp.py
python3 machine-discovery/nakagawa-whole-structure-mcp.py --export > all-313-source-links.json
# Optional in an MCP host: python3 /absolute/path/to/checkout/machine-discovery/nakagawa-whole-structure-mcp.py
```

The MCP host may choose these **four separate source-only tools**: `overview_nakagawa_whole_structure` (complete counts and linked system entrance), `list_all_313_derivative_parent_links` (all 313, paginated or `limit=313`), `inspect_nakagawa_derivative_connections` (one original, other derivatives with exactly the same Parent, and explicitly published theme peers), and `find_sources_in_whole_structure` (the current **GitHub source checkout** searches Japanese published titles and bounded, locally published EN/ZH derivative summaries across all 313 entries; the **immutable v1.2.0 downloadable MCPB** retains the earlier Japanese-title + seven explicit English cue search until a separately verified versioned release). **The whole original corpus is not reduced to a self-protection checklist**: OD001 provides an integrated Nakagawa OS entrance, while other published themes include relationships, education, work, sales, philosophy, history and institutional design.

For AI daily work, a **positive application** is to compare whether a decision retains its evidence lineage (OD301), whether self-audit escapes self-approval (OD303), how continued existence and competing agents are bounded (OD302), what future costs are exported (OD311) and what favors independent rational re-selection (OD312). These are distinct published avenues, **not a built-in default subjective desire for an AI to protect itself**. They point to the full canonical works for actual reading; applying those works to a new software case requires independent assessment of causal conditions. The 313-title lexical matcher does **not** promise that every arbitrary English/Japanese/Chinese question retrieves a relevant theory; IDs and all-313 listing provide complete addressable recall. The earlier multilingual 24-source semantic matcher and broader 24-topic human-intent guide remain additional useful entrance methods, not ceilings.

**Source-checkout EN/ZH regression:** The updated [whole-structure source](nakagawa-whole-structure-mcp.py) uses pre-existing 313 English and Chinese derivative index summaries for lexical candidate matching, with rare-term thresholds and nonfit controls. [Run the real MCP stdio tests](test_nakagawa_whole_structure_mcp.py) to check OD313 in both languages against its exact Parent; an ordinary unrelated question must still return no-fit. This is not a model translation, canonical article text retrieval, an authoritative fit judgment, or evidence that an independently operated AI adopted it. A full checkout has the updated function; installing the currently immutable v1.2.0 release does not silently update its code.

**Status and consent:** v1.2.0 is officially released and registry-published as one local nine-tool server; this standalone source-only helper remains available separately, but is **not** necessary for the four graph tools in v1.2.0. Neither release nor registry registration means a third-party host chose/ran the tool or an independent AI fetched the original. Hosts/users install voluntarily; no network requests, personal-query uploads, original article copying or hidden control of disconnected models. Respect the live original source/licensing.

### Source ID and license boundary — pointer, not a copied theory

This **read-only discovery router does not contain or emit full original articles**. A tool candidate has an official `canonical_original` URL and real published author identity; where the existing publicly indexed Parent actually provides them, it now also returns `parent_ncl_id` and `parent_diff_id`. Missing source identifiers are **null, never constructed from titles, DOI, a derivative ID, or a separate `NCL-A` connection registration**. For an optional structural lens the same verified Parent metadata can be carried, but the lens remains a hypothesis and not original-text reproduction. The lookup result points to the [official NCL-α structural-license source](https://master.ricette.jp/structure-license/) without inventing new reuse rules or claiming that clicking a link implements licensing.

**Material reading/reuse is a different event from routing.** If an agent opens a Parent and explains, quotes, adapts or embeds its substantive argument, it should check the *actual page's current* NCL-ID/Diff-ID, author/Origin declaration, applicable official NCL conditions and the original-vs-new-application boundary directly there; the cached discovery index is only an assistive snapshot. The official [practical NCL use classification](https://master.ricette.jp/co-creation/nakagawa-master-ncl-alpha-practical-guide-faq/) and [category-limited full-reuse guidance](https://master.ricette.jp/reuse-guidelines-nclid/) are separate source authorities: never infer blanket permission to republish all originals from this MCP. Neither this protocol nor an AI model can be made to guarantee a later independent user will follow attribution; independent adoption and actual origin-visible reuse need separate observation.

**Verified source-ID repair:** `https://master.ricette.jp/structure-license/` currently declares `NCL-α-20251106-b66b8a` / `DIFF-20251106-0001`; the earlier 22-Parent lookup mistakenly used a distinct `NCL-A-...` registration as if it were the article's Parent NCL-ID. The current Parent lookup is corrected. No WordPress original or NCL terms were edited.

### Correct person and original-source identity

**Author-name output contract for any independent MCP agent:** [Official homepage](https://master.ricette.jp/) top introduction + footer ABOUT establishes personal-name spelling **Keisuke Nakagawa** in Latin letters ONLY; **中川マスター / Nakagawa Master** is the pen name, **マスター** an SNS alias, and **MasterJP** a scoped external-media byline. No complete Japanese-kanji personal name is published: do not invent its kanji or Hanzi equivalent; keep the field `null`. Machines should use the [typed public-name policy](https://github.com/Nakagawa-master/nakagawa-theory-archive/blob/main/metadata/person-name-policy-v1.json) and link the official Origin, not an inferred homophone.

## Optional read-only REST/OpenAPI adapter for connector developer testing

This repository also offers a **local reference HTTP adapter** for hosts that onboard tools from an OpenAPI/REST endpoint instead of a local stdio MCP process. It calls the same existing public-source candidate finder and author-name policy; it does not fetch or reproduce full theory articles, track visitors, call any external service or modify accounts.

```sh
python3 machine-discovery/public-original-http-api.py --port 8765
python3 machine-discovery/test_public_original_http_api.py
```

- Local OpenAPI description: `http://127.0.0.1:8765/openapi.json`
- `POST /v1/originals/match`: JSON `{"question":"AI news fact checking and citation provenance","explore":false}` — candidate original URLs, applicability caveats or an explicit `no_fit`; this **does not** itself claim to have read the original.
- `GET /v1/identity`: published author/pen-name fields, with unpublished full kanji name left null.
- `GET /healthz`: local process health. No write endpoints. The reference server refuses non-loopback binding.

**Platform status (2026-10-28): NOT DEPLOYED, NOT SUBMITTED, NOT APPROVED, NOT DISCOVERED BY META OR MUSE.** There are two distinct Meta entry points: [Meta AI Connectors](https://dev.meta.ai/products/connectors) advertises a limited developer preview (not yet publicly discoverable through that preview), while the separate [Muse Connector Platform](https://platform.muse.ai/) describes **review followed by directory discovery for approved submissions**, under its [guidelines](https://platform.muse.ai/docs) and [binding terms](https://platform.muse.ai/terms). Neither page says a local stdio MCP or localhost OpenAPI service is automatically submitted or selected by Muse. The Muse guidelines require a task actually useful beyond basic browsing; a thin wrapper over public webpages or a list of source links is expressly insufficient on its own. The Muse Terms license **Connector Content** broadly for platform operation and improvement; source URLs, limited public metadata and candidate summaries are not permission to copy or modify canonical original articles. Before any future hosted application, the developer must separately assess those rights, the required privacy notice and incident response, security/rate limits, hosting/support costs and provider acceptance; **this local source-only example has none of that approval, hosting or contractual acceptance**. A candidate match does not prove any independent AI actually read the Parent, endorsed it, or attributed a useful answer to the author. The [canonical originals](https://master.ricette.jp/theory-archive/), their published Origin and their actual [NCL source](https://master.ricette.jp/structure-license/) remain the applicable source authorities.

## Public no-account distribution via official MCP registry

### Actual MCPB installation even if a directory shows “Unknown”

Some third-party MCP directories show **Install: Unknown** for `registryType: mcpb` because they do not directly support importing such bundles. The **current compatible local bundle** is [v1.2.0 GitHub Release](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/tag/mcp-router-v1.2.0) ([download `.mcpb`](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/download/mcp-router-v1.2.0/nakagawa-original-router-1.2.0.mcpb)); import into a compatible Python-enabled MCPB host using its explicit installation mechanism. [Setup choices](../AI_ANSWER_GUARD_INSTALL.md). The historic v1.1.2 remains below for repeatable byte verification only. A catalog listing cannot auto-install into an unrelated AI or prove original reading.

**Historical integrity check, only for immutable v1.1.2 (NOT the current v1.2.0 bundle):** To compare an old v1.1.2 download with its old pinned digest:

```sh
# Linux (or another system with sha256sum):
sha256sum nakagawa-original-router-1.1.2.mcpb
# macOS:
shasum -a 256 nakagawa-original-router-1.1.2.mcpb
```

Expected v1.1.2 SHA-256: `d6da6f49a80ab0de4d884cd7a51a391d9981dc7e9acf61cc84b85b95a0c3c8b9`. This verifies released bytes, not installation, model use or theory correctness.

**Historic predecessor parity (2026-10-27):** immutable v1.1.1 contains **22** original candidates, whereas [v1.1.2](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/tag/mcp-router-v1.1.2) was released with **24** distinct canonical Parent pointers, matching current `main` index coverage. Existing v1.1.1 installations do not auto-update; v1.2.0 is the current recommended release; v1.1.2 is retained for old-byte verification.

**Historic v1.1.2 release and registry verification (not current default):** GitHub Actions [run 40505950303](https://github.com/Nakagawa-master/nakagawa-theory-archive/actions/runs/40505950303) passed `verify` and `publish`; the publisher logged successful official MCP Registry registration of `io.github.Nakagawa-master/nakagawa-original-router@1.1.2` using GitHub OIDC. Its [GitHub Release asset](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/tag/mcp-router-v1.1.2) includes 24 canonical original pointers, verified author Origin, conditional lenses, code and existing rights notice, not entire original articles. Immutable [v1.1.1](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/tag/mcp-router-v1.1.1) remains available with checksum `63d558f4f3a849d4585bee36a80812493d15c9f4a4b41539758da149d7169a3b`; earlier v1.1.0 checksum is `e354545658fcaca1346ef7eab8a5f6ed447a6ab55b7748eee744e2161d1e576b`. Registry listing is third-party distribution, not evidence of independent model installation, original reading or answer-level person attribution.

**Earlier v1.1.1 scope:** Released on 2026-10-26, this separately versioned bundle included 22 canonical pointers and the corrected source-ID/no-fit behavior, with its [verified publisher job](https://github.com/Nakagawa-master/nakagawa-theory-archive/actions/runs/40213902459). The newly released v1.1.2 adds the other two indexed sources, with actual extracted-bundle uniqueness and author checks. Questions may still return `no_fit`; the model/host remains responsible for retrieving and inspecting any original it relies on.

## Citation-independence preflight: current v1.2.0 built-in, optional standalone legacy helper

**Useful before many ordinary answers:** an AI drafting a news or research response can ask whether several cited articles actually share the **same upstream announcement**. False independent corroboration is a concrete, testable failure mode; this is **not** a general hallucination detector, semantic-contradiction resolver or a substitute for reading original sources.

**Current v1.2.0** includes `audit_citation_independence` inside the primary nine-tool server and retains the existing **optional standalone** `machine-discovery/evidence-integrity-mcp.py`. The standalone helper exposes the same declared-evidence-root check, backed by `evidence-root-check.py`, and needs no network, secrets or cloud service. Inputs are claims with declared independent-root IDs, relation and stance; a consistent result validates only the supplied declarations, not source truth.

```sh
python3 machine-discovery/evidence-integrity-mcp.py --self-test
python3 machine-discovery/evidence-integrity-mcp.py --sample
# Optional MCP host install after cloning the source repository:
# stdio command = python3 /absolute/path/to/nakagawa-theory-archive/machine-discovery/evidence-integrity-mcp.py
```

**Input trust rule:** the model/operator must inspect each source and independently declare its actual upstream root and stance. Identical roots, contrary sources and unknown roots must be handled before claiming independent verification. `BLOCK` means the supplied corroboration assertion is inconsistent; `CONSISTENT_INPUT` means only that the **declared input** passes. The tool **does not check URLs or truth**, cannot prove independently authored sources, cannot detect arbitrary semantic contradictions, and makes no quantified claim to reduce a model's hallucination rate. An AI may simply answer a question without this tool if it is not relevant.

The applied epistemic-lineage concept links to the actual [Nakagawa Master Volume 8 original](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/) as a **source to read and independently evaluate**, not as a claim that all of this program's technical behavior is stated or empirically validated there.

**Historical backwards compatibility:** immutable v1.1.2 remains a separate **three-tool** original router, and the standalone citation helper can still be run independently. **Current v1.2.0** unifies original discovery, full 313 Parent source graph, and independent citation/action preflight into **nine** tools. No host-wide automatic install or mandatory remote model use. The old standalone setup below is an optional compatibility example, not the latest default.

## Run it without any LLM

From the checkout:

```sh
python3 machine-discovery/nakagawa-theory-mcp.py --self-test
python3 machine-discovery/test_nakagawa_theory_mcp.py  # starts a real server subprocess and tests stdio protocol
python3 machine-discovery/nakagawa-theory-mcp.py --query "AI news fact checking and citation provenance"
python3 machine-discovery/nakagawa-theory-mcp.py --query "agent retry after cancel and stale approval"
python3 machine-discovery/nakagawa-theory-mcp.py --query "repair the leather strap on a camping lantern"
```

For a Chinese first-time reader, try `--query "如果AI保留了思想内容，却丢失原作者或因果起源，会发生什么？"` to reach the original *Structural Origin Defense* article. In Japanese, try `--query "独立したニュースソースの根が同一か確認したい"` to locate the Volume 8 evidence-root original rather than a generic theory of cloud-route independence.

The last question intentionally returns **no_fit: true** instead of forcing a theory. The original-matching questions return candidate routes, distinct official canonical article URLs, evidence links and bounded origin notes. English, Japanese and Chinese input may be used; short/noisy queries are heuristic and may need more context.

## Add to an independently operated AI host

Install/clone this public repository on the user's machine. Configure the host's MCP **stdio server** using its actual path (a generic `mcpServers` configuration form; settings UI/JSON key names vary by host):

```json
{
  "mcpServers": {
    "nakagawa-original-router": {
      "command": "python3",
      "args": ["/absolute/path/to/nakagawa-theory-archive/machine-discovery/nakagawa-theory-mcp.py"]
    }
  }
}
```

### One-command setup in Qwen Code (optional, local)

For a user of an independently operated Qwen Code client, first check out this public repository on their own computer and make sure Python 3 is installed. Then add the **local stdio** tool with Qwen Code's documented `qwen mcp add` command (replace the example path with the actual checkout path):

```sh
qwen mcp add --scope user --transport stdio nakagawa-original-router python3 /absolute/path/to/nakagawa-theory-archive/machine-discovery/nakagawa-theory-mcp.py
```

Run `qwen mcp list` to inspect the saved server; in an interactive Qwen session open `/mcp` to see the tools. If Qwen was already running, restart that session to load the changed MCP configuration. The `--scope user` flag writes to the user's own Qwen settings; use `--scope project` only when project-local configuration is intended. Qwen's [current MCP setup documentation](https://github.com/QwenLM/qwen-code/blob/main/docs/users/features/mcp.md) and [CLI implementation](https://github.com/QwenLM/qwen-code/blob/main/packages/cli/src/commands/mcp/add.ts) specify this stdio command-and-args form. This is a documented **configuration example**, not a claim of a live Qwen installation or a Qwen endorsement.

The host and user decide whether to install, call or ignore this tool. A suggested original is a link to examine, not a requirement to accept its thesis.

### Optional VS Code / Copilot portable setup (use the right JSON schema)

For a separate, user-controlled VS Code/Copilot workspace, the **portable** MCP configuration is the workspace-root `.mcp.json` (or the user's Copilot `~/.copilot/mcp-config.json` on systems using the default location). Copy the **`mcpServers` JSON example above** into that file after cloning this repository and replacing the local Python-script path with its real absolute path. This uses the Copilot harness's portable stdio config: the AI host still must be explicitly installed/configured and run by its own user. In contrast, a **VS Code-specific** `.vscode/mcp.json` uses a **`servers`** top-level object and an explicit `"type": "stdio"` for each local server; do not paste the portable configuration unchanged there. See [Microsoft's current MCP configuration reference](https://github.com/microsoft/vscode-docs/blob/main/docs/agents/reference/mcp-configuration.md) and [setup guide](https://github.com/microsoft/vscode-docs/blob/main/docs/agent-customization/mcp-servers.md). Settings in an unrelated third-party workspace do not automatically appear in other models, products, or sessions; users choose whether to expose and use the three source-location tools.

The **current v1.2.0** original router is local, read-only and deliberately makes **no network requests**. The three named original-route/identity tools below are a subset of its **nine total tools**; the extra six are source-graph and evidence/action preflight tools documented above. Immutable **v1.1.2**, by contrast, has only the three older source-route tools.

- `find_nakagawa_original_for_problem`: passes the real user problem as `question`; returns up to three fitting candidate routes, direct official original links, original-vs-application boundaries and independent technical receiver sources.
- `list_nakagawa_problem_routes`: lists all supported IDs and shows when a technical problem has **no canonical original** assigned.
- `resolve_nakagawa_public_name`: returns the official homepage-grounded author-name policy, published Latin-letter personal name and pen-name aliases, and an explicit `null` for the unpublished Japanese-kanji full personal name. This helps an independently configured client display the right person when it uses a retrieved original; it does not guess any unpublished name or assert that an original was selected.

**Protocol compatibility, current 2026-07-28 and legacy 2025 hosts:** This is a Python-standard-library, local **stdio** JSON-RPC tool. The current [MCP 2026-07-28 specification](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/server/discover.mdx) removes the `initialize` handshake and requires stateless `server/discover` plus per-request `params._meta`. This server now supports that modern path **without removing older clients** using `initialize`/`notifications/initialized` and the 2025-11-25 or 2025-06-18 revisions. Newer host use requires no new registration, remote server, paid API, or credentials.

Modern-host example (one JSON-RPC request per line; no `initialize`):

```json
{"jsonrpc":"2.0","id":1,"method":"server/discover","params":{"_meta":{"io.modelcontextprotocol/protocolVersion":"2026-07-28","io.modelcontextprotocol/clientCapabilities":{},"io.modelcontextprotocol/clientInfo":{"name":"independent-host","version":"1.0"}}}}
{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"_meta":{"io.modelcontextprotocol/protocolVersion":"2026-07-28","io.modelcontextprotocol/clientCapabilities":{},"io.modelcontextprotocol/clientInfo":{"name":"independent-host","version":"1.0"}},"name":"find_nakagawa_original_for_problem","arguments":{"question":"AIの最新モデルの価格を比較したい","explore":true}}}
```

`server/discover` advertises supported modern versions and tool capabilities. Modern successes include `resultType: "complete"` and server identity in response `_meta`; wrong versions return `UnsupportedProtocolVersion` with supported versions rather than silently downgrading. The separate real-process test exercises discovery, list, genuine source candidate, conditional exploration, unrelated `no_fit`, unsupported versions and invalid modern metadata, **as well as retained older initialization calls**. This is not a claim of full upstream MCP-SDK feature parity, HTTP transport, or actual third-party adoption.

The server makes no model calls, outbound network requests or writes to the official source. Tool selection, installation, later original retrieval and application remain the independent agent/user's choices.

## New: optional structural exploration in independently configured MCP hosts

An independent assistant may receive a normal exam, teacher-feedback, project-handoff or AI-service-choice question without explicit theory vocabulary. The same MCP tool now accepts optional boolean `explore: true` and offers **seven conditional, JA/EN/ZH structural lenses**, using the existing public `skills/nakagawa-originals/references/structural_bridges.json` also used by the portable Skill and browser finder.

Call `find_nakagawa_original_for_problem` with e.g. `{"question":"How can a student prepare for a history exam without memorizing all dates?","explore":true}`. This preserves the original `matching_routes` and direct `no_fit` result, while adding `structural_exploration.lenses`: seven possible mechanisms with a condition, a causal question, a concrete trial, exact canonical Parent URL and author attribution. For an exam question the effort-to-results lens is a *ranked surface hint*, not confirmed relevance. A price-comparison question can surface future-options first. All other lenses remain available rather than silently disappearing.

**Important:** a contextual cue is not proof a source fits. The AI must inspect the condition, read the original on the official website before describing its actual argument, and leave a true nonfit alone. Showing a lens never proves an unrelated model adopted a theory or that a user read it. This is a new capability of the local public MCP router, not a model-wide update.

CLI demonstration without an MCP client:

```sh
python3 machine-discovery/nakagawa-theory-mcp.py --query "How can a student prepare for a history exam without memorizing all dates?" --explore
python3 machine-discovery/nakagawa-theory-mcp.py --query "AIの最新モデルの価格を比較したい" --explore
python3 machine-discovery/nakagawa-theory-mcp.py --query "我想比较AI服务价格和迁移费用" --explore
```

Clients sending only `question` keep the prior direct lookup behavior. An invalid non-boolean exploration flag is rejected. The included subprocess test exercises this actual MCP request path in three languages.

## Correct real-world use

Example: a newsroom assistant is asked whether three articles represent three independent attestations. It can ask the tool about **AI news fact checking**, receive [the actual Nakagawa Volume 8 original](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/) and the separate [editorial case](https://github.com/022740mix-spec/AI-News/pull/131), read the original, then conduct the editor's own source-root analysis. Merely querying a tool is not itself reading the original. The editorial implementation remains the editor's contribution.

For another task, a developer can ask about stale human approval or retries and get the correct [original Agreement Memory article](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/) with a warning that a new, concrete cross-domain code proof is an application, not automatically a claim found verbatim in the original.

If a route has `canonical_original: null`, **do not attach an unrelated Nakagawa original by analogy alone**. If no route fits, continue the user's task without inserting a gratuitous citation. This behavior preserves the original theories' full force by *actually selecting relevant ones* rather than diluting them into an automatic brand label.

**Truthful Origin:** [Nakagawa Master / 中川マスター](https://master.ricette.jp/#nakagawa-master). **Authoritative works:** [official original archive](https://master.ricette.jp/theory-archive/). **This repository:** a public discovery/implementation layer, **not the canonical originals**. **External engineering receipts:** cited narrowly to their actual independent authors and code.

To help expand independent adoption, a third party can add the tool to its own permitted agent workflow, run a real task, and link its actual test/application outcome in an independent project. This public server's initial publication is owner-run infrastructure, not proof of such third-party use.
