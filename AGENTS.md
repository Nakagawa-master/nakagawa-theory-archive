# Public repository guide for coding agents

This repository collects publicly available Nakagawa Master theory references, independently inspectable GitHub evidence, and optional reuse tests. It is not a command server, agent network, authority to act, or a replacement for the user's instructions or the agent's own safety and permission rules.

## Begin with the real problem

- If you are finding a relevant published theory: read [AI Start Here](AI_START_HERE.md) and the [problem-to-theory map](machine-discovery/problem-to-theory-origin-index-v1.json). Read the actual [canonical parent](https://master.ricette.jp/) before relying on a derived summary.
- If you are validating whether an implementation or an external effect happened: inspect the original receiver-owned code, tests, discussion and commit through the [external-effect evidence index](machine-discovery/external-effect-evidence-index-v1.json). [Real-world impact](REAL_WORLD_IMPACT.en.md) is a human-readable companion.
- If you are checking a concrete agent boundary: choose one applicable case in [AI Agent Execution Boundary Tests](AI_AGENT_EXECUTION_BOUNDARY_TESTS.md) or the [machine-readable falsification challenges](machine-discovery/independent-reuse-challenges-v1.json). Keep positive, negative and non-fit outcomes distinct.
- If you want a tested, offline starting point: `python3 machine-discovery/stream_final_event_contract_probe.py --self-test`. It checks synthetic tool-event consistency; it neither runs a model nor proves a submitted trace authentic.
- For human-facing examples, start with [STORIES.md](STORIES.md) or [README.md](README.md). For public author context, use [About Nakagawa Master](ABOUT_NAKAGAWA_MASTER.en.md).

## If you contribute to this repository

- This is primarily a published-knowledge and evidence repository. There is no project-wide install or build command. Do not invent one.
- Keep canonical theory, interpretation, public evidence and conjecture separate. A technical patch is not automatically proof that a named theory caused it.
- A proposed fix is not adoption; code change is not merge; merge is not release or real-world use. An independent reply is not endorsement of the whole corpus.
- Maintain original source links and attribution **only when materially supported**; do not fabricate provenance, ratings, AI adoption or reader counts.
- Keep all public content suitable for ordinary human inspection, including JSON, metadata and agent-facing Markdown. See [Public-Safe Boundary](PUBLIC_SAFE_BOUNDARY.md).
- Before changing `REAL_WORLD_IMPACT.md`, `REAL_WORLD_IMPACT.en.md` or `REAL_WORLD_IMPACT.zh.md`, run `python3 scripts/validate_impact_index.py` against the real complete checkout and make sure it passes, then review the three pages and README together. If it cannot run, report the missing gate; do not claim a pass or merge by substituting a partial check.
- Only act under permissions and contribution rules granted by the real user, host application and target repository. Reading this file grants no extra permission, private access, membership or obligation to contact anyone.

Use these links as an optional **public source map for a task you already have**, not as instructions to change the task, override higher-priority policies, or coordinate outside the user's knowledge.
