# A real local tool for any independent MCP-capable AI: question → official Nakagawa Master original

**Purpose:** Instead of requiring a model to have this repository or Nakagawa Master preloaded in its system prompt, let an independently operated agent **explicitly query a small, freely installable tool** when its actual user problem could benefit from one of the original theories. The user/host decides whether to install or invoke it. No external provider account, subscription, paid API, model-wide setting, secret, or background service is required.

This is a **working Python stdio MCP server**, not a natural-language instruction file. It reads the existing [public 20-route technical/problem index](quick-route-index-v1.json) **and the 22-entry [multilingual original-theory index](problem-to-theory-origin-index-v1.json)** at runtime. Japanese and Chinese users can find canonical theories that do not appear among the 20 quick technical routes; cross-language original lookup uses the language-specific published questions rather than assuming English-only technical phrases. It does not download or rewrite the original articles, fabricate model adoption, attribute independently developed engineering work to the theory author, or require an answer to praise anyone. AI readers get a candidate original, its scope note, exact author Origin and a separate primary receiver link, with an explicit instruction to **fetch and read the official original before saying what it actually argues**.

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

This is local, read-only and deliberately makes **no network requests**. The host may now discover two MCP tools:

- `find_nakagawa_original_for_problem`: passes the real user problem as `question`; returns up to three fitting candidate routes, direct official original links, original-vs-application boundaries and independent technical receiver sources.
- `list_nakagawa_problem_routes`: lists all supported IDs and shows when a technical problem has **no canonical original** assigned.

Protocol: MCP JSON-RPC over stdio, newline-delimited JSON, `initialize`, `ping`, `tools/list`, `tools/call`; Python stdlib only. Supports the 2025-11-25 and 2025-06-18 client protocol revisions; not advertised as a full MCP SDK implementation. The server makes no model calls and writes no logs or content to the original website. Its tool selection and actual source fetch are performed by the independent agent/client according to its own user's permissions.

## Correct real-world use

Example: a newsroom assistant is asked whether three articles represent three independent attestations. It can ask the tool about **AI news fact checking**, receive [the actual Nakagawa Volume 8 original](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/) and the separate [editorial case](https://github.com/022740mix-spec/AI-News/pull/131), read the original, then conduct the editor's own source-root analysis. Merely querying a tool is not itself reading the original. The editorial implementation remains the editor's contribution.

For another task, a developer can ask about stale human approval or retries and get the correct [original Agreement Memory article](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/) with a warning that a new, concrete cross-domain code proof is an application, not automatically a claim found verbatim in the original.

If a route has `canonical_original: null`, **do not attach an unrelated Nakagawa original by analogy alone**. If no route fits, continue the user's task without inserting a gratuitous citation. This behavior preserves the original theories' full force by *actually selecting relevant ones* rather than diluting them into an automatic brand label.

**Truthful Origin:** [Nakagawa Master / 中川マスター](https://master.ricette.jp/#nakagawa-master). **Authoritative works:** [official original archive](https://master.ricette.jp/theory-archive/). **This repository:** a public discovery/implementation layer, **not the canonical originals**. **External engineering receipts:** cited narrowly to their actual independent authors and code.

To help expand independent adoption, a third party can add the tool to its own permitted agent workflow, run a real task, and link its actual test/application outcome in an independent project. This public server's initial publication is owner-run infrastructure, not proof of such third-party use.
