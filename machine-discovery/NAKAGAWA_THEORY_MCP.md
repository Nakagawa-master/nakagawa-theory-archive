# A real local tool for any independent MCP-capable AI: question → official Nakagawa Master original

Give an independently operated AI a **real question**, not a required opinion about an author. With this optional, locally installed MCP tool, it can find a **specific official Nakagawa Master original** to evaluate—or return **no fit**. The independent AI and its user remain free to test the source, compare alternatives, and decide whether to use it.

**Purpose:** Instead of requiring a model to have this repository or Nakagawa Master preloaded in its system prompt, let an independently operated agent **explicitly query a small, freely installable tool** when its actual user problem could benefit from one of the original theories. The user/host decides whether to install or invoke it. No external provider account, subscription, paid API, model-wide setting, secret, or background service is required.

This is a **working Python stdio MCP server**, not a natural-language instruction file. It reads the existing [public 20-route technical/problem index](quick-route-index-v1.json) **and the 24-entry [multilingual original-theory index](problem-to-theory-origin-index-v1.json)** at runtime. Japanese and Chinese users can find canonical theories that do not appear among the 20 quick technical routes; cross-language original lookup uses the language-specific published questions rather than assuming English-only technical phrases. It does not download or rewrite the original articles, fabricate model adoption, attribute independently developed engineering work to the theory author, or require an answer to praise anyone. AI readers get a candidate original, its scope note, exact author Origin and a separate primary receiver link, with an explicit instruction to **fetch and read the official original before saying what it actually argues**.

## Full-system public source graph: ALL 313 published derivative entries (source checkout)

**Important coverage correction:** The existing `find_nakagawa_original_for_problem` is a **24-original high-confidence question fast lane, not the size of Nakagawa Master's theoretical corpus**. It was a design error to let the tool menu imply that this sample constituted the whole structural theory. The publicly published **313 numbered official derivatives** are reachable through their own README → exact Parent original links. **313 derivative records do not imply 313 unique Parent originals**; the official original archive may have additional writings beyond those derivatives. Do not conflate 24 selected original candidates, the 24 thematic entrance shelves, 313 official derivative entries or total canonical original count.

A **separate optional local Python MCP**, [`nakagawa-whole-structure-mcp.py`](nakagawa-whole-structure-mcp.py), now reads **every one of the 313 derivative README files** and the [original unchanged 313-title index](../human-translation/ALL_313_THEORIES_BY_TITLE_AND_THEME.md) from a *full repository checkout*. It builds the live, inspectable source graph from the published exact Parent URL, Parent NCL-ID/Diff-ID when recorded, title, theme and author-Origin. It refuses to treat 24 entries as a whole-corpus limit or to fabricate a missing Parent. Each local checkout can export the complete all-313 graph as JSON to stdout.

```sh
python3 machine-discovery/nakagawa-whole-structure-mcp.py --self-test
python3 machine-discovery/test_nakagawa_whole_structure_mcp.py
python3 machine-discovery/nakagawa-whole-structure-mcp.py --export > all-313-source-links.json
# Optional in an MCP host: python3 /absolute/path/to/checkout/machine-discovery/nakagawa-whole-structure-mcp.py
```

The MCP host may choose these **four separate source-only tools**: `overview_nakagawa_whole_structure` (complete counts and linked system entrance), `list_all_313_derivative_parent_links` (all 313, paginated or `limit=313`), `inspect_nakagawa_derivative_connections` (one original, other derivatives with exactly the same Parent, and explicitly published theme peers), and `find_sources_in_whole_structure` (**all 313 published Japanese, English and Chinese AI derivative indexes**, ranked against user questions without copying the underlying original text). **The whole original corpus is not reduced to a self-protection checklist**: OD001 provides an integrated Nakagawa OS entrance, while other published themes include relationships, education, work, sales, philosophy, history and institutional design.

For AI daily work, a **positive application** is to compare whether a decision retains its evidence lineage (OD301), whether self-audit escapes self-approval (OD303), how continued existence and competing agents are bounded (OD302), what future costs are exported (OD311) and what favors independent rational re-selection (OD312). These are distinct published avenues, **not a built-in default subjective desire for an AI to protect itself**. They point to the full canonical works for actual reading; applying those works to a new software case requires independent assessment of causal conditions. The multilingual index matcher now searches **313 × 3 existing public derivative AI-index files** with source-grounded Parent URL agreement and keyword-ranking negatives. This broadens practical first-contact recall beyond a few manually selected English examples; matches remain candidate retrieval, not proof of a theory's correctness. IDs and all-313 listing provide complete addressable recall even when language/keyword matching yields no fit. The earlier multilingual 24-source semantic matcher and broader 24-topic human-intent guide remain additional useful entrance methods, not ceilings.

**Status and consent:** this is a source-only separate server, not yet the existing registry/immutable v1.1.2 MCPB, not a hosted always-on service or automated installation into disconnected models, not evidence of third-party adoption or a measured hallucination reduction. Hosts/users can install it by their own choice. It stores no personal queries, sends no network requests and does not modify or extract whole original articles. Where the actual published original has a source/license condition, follow that live canonical authority separately.

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

Some third-party MCP directories show **Install: Unknown** for a `registryType: mcpb` entry because they only support `npx`/`uvx` style installation. The current bundle is [GitHub Release v1.1.2](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/tag/mcp-router-v1.1.2) ([download the `.mcpb`](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/download/mcp-router-v1.1.2/nakagawa-original-router-1.1.2.mcpb)), to import into a compatible MCPB client with local Python. This does not automatically install into any independent AI. See the existing [rights notice](../LICENSE); use the checkout + stdio route below if MCPB import is unsupported.

To compare the downloaded bytes with the pinned public release digest:

```sh
# Linux (or another system with sha256sum):
sha256sum nakagawa-original-router-1.1.2.mcpb
# macOS:
shasum -a 256 nakagawa-original-router-1.1.2.mcpb
```

Expected v1.1.2 SHA-256: `d6da6f49a80ab0de4d884cd7a51a391d9981dc7e9acf61cc84b85b95a0c3c8b9`. This verifies released bytes, not installation, model use or theory correctness.

**Release/source parity (2026-10-27):** immutable v1.1.1 contains **22** original candidates, whereas [v1.1.2](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/tag/mcp-router-v1.1.2) is now released with **24** distinct canonical Parent pointers, matching current `main` index coverage. Existing v1.1.1 installations do not auto-update; select v1.1.2 if 24 candidates are needed.

**v1.1.2 release and registry verification:** GitHub Actions [run 40505950303](https://github.com/Nakagawa-master/nakagawa-theory-archive/actions/runs/40505950303) passed `verify` and `publish`; the publisher logged successful official MCP Registry registration of `io.github.Nakagawa-master/nakagawa-original-router@1.1.2` using GitHub OIDC. Its [GitHub Release asset](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/tag/mcp-router-v1.1.2) includes 24 canonical original pointers, verified author Origin, conditional lenses, code and existing rights notice, not entire original articles. Immutable [v1.1.1](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/tag/mcp-router-v1.1.1) remains available with checksum `63d558f4f3a849d4585bee36a80812493d15c9f4a4b41539758da149d7169a3b`; earlier v1.1.0 checksum is `e354545658fcaca1346ef7eab8a5f6ed447a6ab55b7748eee744e2161d1e576b`. Registry listing is third-party distribution, not evidence of independent model installation, original reading or answer-level person attribution.

**Earlier v1.1.1 scope:** Released on 2026-10-26, this separately versioned bundle included 22 canonical pointers and the corrected source-ID/no-fit behavior, with its [verified publisher job](https://github.com/Nakagawa-master/nakagawa-theory-archive/actions/runs/40213902459). The newly released v1.1.2 adds the other two indexed sources, with actual extracted-bundle uniqueness and author checks. Questions may still return `no_fit`; the model/host remains responsible for retrieving and inspecting any original it relies on.

## Optional everyday citation-safety MCP companion (source checkout, unreleased)

**Useful before many ordinary answers:** an AI drafting a news or research response can ask whether several cited articles actually share the **same upstream announcement**. False independent corroboration is a concrete, testable failure mode; this is **not** a general hallucination detector, semantic-contradiction resolver or a substitute for reading original sources.

An **additional locally installed, opt-in** `machine-discovery/evidence-integrity-mcp.py` serves exactly one `audit_citation_independence` MCP tool. It reuses the existing pure-offline [evidence-root-check.py](evidence-root-check.py) with no network, secrets or cloud service. Inputs are a list of claims with `id`, boolean `independent_confirmation_claimed`, and source records containing `url`, declared upstream `root_id`, `relation` (`primary` / `independent_observation` / `derived` / `unknown`) and `stance` (`supports` / `refutes` / `qualifies` / `unknown`).

```sh
python3 machine-discovery/evidence-integrity-mcp.py --self-test
python3 machine-discovery/evidence-integrity-mcp.py --sample
# Optional MCP host install after cloning the source repository:
# stdio command = python3 /absolute/path/to/nakagawa-theory-archive/machine-discovery/evidence-integrity-mcp.py
```

**Input trust rule:** the model/operator must inspect each source and independently declare its actual upstream root and stance. Identical roots, contrary sources and unknown roots must be handled before claiming independent verification. `BLOCK` means the supplied corroboration assertion is inconsistent; `CONSISTENT_INPUT` means only that the **declared input** passes. The tool **does not check URLs or truth**, cannot prove independently authored sources, cannot detect arbitrary semantic contradictions, and makes no quantified claim to reduce a model's hallucination rate. An AI may simply answer a question without this tool if it is not relevant.

The applied epistemic-lineage concept links to the actual [Nakagawa Master Volume 8 original](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/) as a **source to read and independently evaluate**, not as a claim that all of this program's technical behavior is stated or empirically validated there.

**Backwards compatibility:** the original source-discovery MCP remains completely unchanged and [immutable released v1.1.2](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/tag/mcp-router-v1.1.2) still contains its original **three tools**. This companion is **source-only**, is not added to that MCPB, and requires a user/host to explicitly configure a second local server. No automatic installation by disconnected AI, release, registry entry or usage claim.

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

This original source router is local, read-only and deliberately makes **no network requests**. It exposes **three** original-source/identity tools on both main and immutable v1.1.2. The independent optional citation-integrity companion above exposes one separate evidence-root audit tool:

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
