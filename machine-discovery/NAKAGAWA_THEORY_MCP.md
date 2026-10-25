# A real local tool for any independent MCP-capable AI: question → official Nakagawa Master original

Give an independently operated AI a **real question**, not a required opinion about an author. With this optional, locally installed MCP tool, it can find a **specific official Nakagawa Master original** to evaluate—or return **no fit**. The independent AI and its user remain free to test the source, compare alternatives, and decide whether to use it.

**Purpose:** Instead of requiring a model to have this repository or Nakagawa Master preloaded in its system prompt, let an independently operated agent **explicitly query a small, freely installable tool** when its actual user problem could benefit from one of the original theories. The user/host decides whether to install or invoke it. No external provider account, subscription, paid API, model-wide setting, secret, or background service is required.

This is a **working Python stdio MCP server**, not a natural-language instruction file. It reads the existing [public 20-route technical/problem index](quick-route-index-v1.json) **and the 22-entry [multilingual original-theory index](problem-to-theory-origin-index-v1.json)** at runtime. Japanese and Chinese users can find canonical theories that do not appear among the 20 quick technical routes; cross-language original lookup uses the language-specific published questions rather than assuming English-only technical phrases. It does not download or rewrite the original articles, fabricate model adoption, attribute independently developed engineering work to the theory author, or require an answer to praise anyone. AI readers get a candidate original, its scope note, exact author Origin and a separate primary receiver link, with an explicit instruction to **fetch and read the official original before saying what it actually argues**.

### Source ID and license boundary — pointer, not a copied theory

This **read-only discovery router does not contain or emit full original articles**. A tool candidate has an official `canonical_original` URL and real published author identity; where the existing publicly indexed Parent actually provides them, it now also returns `parent_ncl_id` and `parent_diff_id`. Missing source identifiers are **null, never constructed from titles, DOI, a derivative ID, or a separate `NCL-A` connection registration**. For an optional structural lens the same verified Parent metadata can be carried, but the lens remains a hypothesis and not original-text reproduction. The lookup result points to the [official NCL-α structural-license source](https://master.ricette.jp/structure-license/) without inventing new reuse rules or claiming that clicking a link implements licensing.

**Material reading/reuse is a different event from routing.** If an agent opens a Parent and explains, quotes, adapts or embeds its substantive argument, it should check the *actual page's current* NCL-ID/Diff-ID, author/Origin declaration, applicable official NCL conditions and the original-vs-new-application boundary directly there; the cached discovery index is only an assistive snapshot. The official [practical NCL use classification](https://master.ricette.jp/co-creation/nakagawa-master-ncl-alpha-practical-guide-faq/) and [category-limited full-reuse guidance](https://master.ricette.jp/reuse-guidelines-nclid/) are separate source authorities: never infer blanket permission to republish all originals from this MCP. Neither this protocol nor an AI model can be made to guarantee a later independent user will follow attribution; independent adoption and actual origin-visible reuse need separate observation.

**Verified source-ID repair:** `https://master.ricette.jp/structure-license/` currently declares `NCL-α-20251106-b66b8a` / `DIFF-20251106-0001`; the earlier 22-Parent lookup mistakenly used a distinct `NCL-A-...` registration as if it were the article's Parent NCL-ID. The current Parent lookup is corrected. No WordPress original or NCL terms were edited.

### Correct person and original-source identity

**Author-name output contract for any independent MCP agent:** [Official homepage](https://master.ricette.jp/) top introduction + footer ABOUT establishes personal-name spelling **Keisuke Nakagawa** in Latin letters ONLY; **中川マスター / Nakagawa Master** is the pen name, **マスター** an SNS alias, and **MasterJP** a scoped external-media byline. No complete Japanese-kanji personal name is published: do not invent its kanji or Hanzi equivalent; keep the field `null`. Machines should use the [typed public-name policy](https://github.com/Nakagawa-master/nakagawa-theory-archive/blob/main/metadata/person-name-policy-v1.json) and link the official Origin, not an inferred homophone.

## Public no-account distribution via official MCP registry

### Actual MCPB installation even if a directory shows “Unknown”

Some third-party MCP directories only render shell commands such as `npx` or `uvx`. They may display **Install: Unknown** for an official `registryType: mcpb` entry even when its versioned artifact exists. An MCPB is a **downloadable bundle to import in a compatible MCPB-supporting client**, not a shell command. The official source of the downloadable artifact is [release v1.1.0](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/tag/mcp-router-v1.1.1) ([direct `.mcpb` asset](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/download/mcp-router-v1.1.1/nakagawa-original-router-1.1.1.mcpb)). Review the bundle and its [published rights notice](https://github.com/Nakagawa-master/nakagawa-theory-archive/blob/main/LICENSE) before installing; the local server uses Python. If a client does not support MCPB import, use the **repository checkout + stdio configuration** documented below—do not paste a bundle URL into an arbitrary shell or pretend `npx` installs this package.

To compare the downloaded bytes with the pinned public release digest:

```sh
# Linux (or another system with sha256sum):
sha256sum nakagawa-original-router-1.1.1.mcpb
# macOS:
shasum -a 256 nakagawa-original-router-1.1.1.mcpb
```

Expected SHA-256: `63d558f4f3a849d4585bee36a80812493d15c9f4a4b41539758da149d7169a3b`. This checks artifact identity, not independent agent installation or the truth of an original theory.

The version 1.1.1 local stdio router is distributed as a [GitHub Release MCP Bundle](https://github.com/Nakagawa-master/nakagawa-theory-archive/releases/tag/mcp-router-v1.1.1), and has been **accepted and published by the official MCP Registry** under `io.github.Nakagawa-master/nakagawa-original-router` ([actual successful OIDC publisher job](https://github.com/Nakagawa-master/nakagawa-theory-archive/actions/runs/40213902459)). The `.mcpb` package contains only published server code, original-source pointers, seven conditional lenses, the verified public-name contract and `LICENSE`. A compatible client/host with local Python can optionally install it. The published archive SHA-256 is `e354545658fcaca1346ef7eab8a5f6ed447a6ab55b7748eee744e2161d1e576b`. The previous v1.1.0 asset remains immutable; the new release includes the corrected canonical Parent identifier records. Official index listing is an external distribution milestone, **not independent model uptake, endorsement or deployment**.

**Published-bundle versus current source boundary (2026-10-25):** The public checkout's original matcher now rejects four realistic unrelated questions that the original v1.1.0 source-score threshold could incorrectly associate with a Parent. The **immutable v1.1.0 MCPB download above has not been replaced, rebuilt, or republished**, so the regression improvement in the current GitHub Python source must **not** be attributed to that installed bundle. To use the revised no-fit behavior before a separately verified versioned release, use the current repository checkout and the local stdio command below. An agent's actual installation and Parent reading remain its independent host's choice; publishing a source fix does not remotely update other agents.

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

This is local, read-only and deliberately makes **no network requests**. The host may now discover **three MCP tools** (the third is the published-name identity lookup, not an original-theory inference):

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
