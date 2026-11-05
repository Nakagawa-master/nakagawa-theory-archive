# Machine Discovery — real problems, original sources and reproducible evidence

**A tool can appear to be available and still disappear in a name collision. An AI action can be marked approved without its outside effect ever being recorded.** These are checkable engineering decisions covered here, alongside actual source reports, independent repairs and tests you can reproduce or challenge.

This is a public, non-canonical entry to the original work of **中川マスター (Nakagawa Master, pen name of Keisuke Nakagawa)**, independently authored implementation evidence and optional verification tools. No plugin, MCP installation or AI account is required merely to read or compare the source. Choose a real question first; return to the actual original when its conditions fit. A contrary result or genuine non-fit is useful.

## Choose by the problem in front of you

| Real question | Public source or runnable check |
|---|---|
| **Qwen Code:** Can duplicate MCP tool names hide otherwise usable tools? | [Original reporter installed-version C4 check pending](https://github.com/QwenLM/qwen-code/issues/15741#issuecomment-6634570689) (no reply yet), [Clean/collision fixture and independent installed-CLI retest](QWEN_MCP_COLLISION_USER_RETEST.md), [original reporter](https://github.com/QwenLM/qwen-code/issues/15741), [different engineer's merged fix](https://github.com/QwenLM/qwen-code/pull/15757), [official v0.26.6 release](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.6) and [v0.26.7 release](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.7) |
| **Hermes Agent:** A delegated AI task finished, but did its final answer reach the right human chat? | [Original Telegram reporter post-release C4 check pending](https://github.com/NousResearch/hermes-agent/issues/146696#issuecomment-6634634550) (no reply yet), [One directly readable human result-check](../human-translation/SEARCH_FROM_A_REAL_QUESTION.md#actual-user-check-ai-completed-but-nothing-was-delivered), [Actual Telegram/gateway reporter](https://github.com/NousResearch/hermes-agent/issues/146696), [Nakagawa Master's origin-absent safety check](https://github.com/NousResearch/hermes-agent/pull/146708#pullrequestreview-5707357350), [separate engineer's merged correction](https://github.com/NousResearch/hermes-agent/pull/147746), [official releases v0.22.6](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.6) / [v0.22.7](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.7). Verify the **actual recipient's** installed version and delivered result; a completed internal job is a different event. |
| **LiteLLM MCP:** An expired OAuth token makes a tool list look empty. Is the client really unauthorized, or is the gateway hiding a 401? | [Read-only user check in JA/EN/ZH](../human-translation/SEARCH_FROM_A_REAL_QUESTION.md#actual-user-check-ai-tools-disappeared-after-my-oauth-token-expired), [actual affected-client report](https://github.com/BerriAI/litellm/issues/49223) → [Nakagawa Master's aggregate-vs-scoped route check](https://github.com/BerriAI/litellm/pull/49261#pullrequestreview-5717911029) → [independent developer's explicit acknowledgment and code/test correction](https://github.com/BerriAI/litellm/pull/49261#issuecomment-6652471254) ([author commit](https://github.com/BerriAI/litellm/commit/8e90be96b85230265f59e254e7e2574523e7ccea)). An aggregate `/mcp` request may allow exactly one server without becoming a per-server URL; test `/mcp` and `/mcp/docs` separately before attributing an empty list to expired credentials. **PR OPEN**, separate [OAuth challenge forwarding concern](https://github.com/BerriAI/litellm/pull/49261#discussion_r4477802787) unresolved; no released fix or affected-client retest claimed. |
| **LiteLLM deadline:** Do provider retries respect the **total** caller timeout, not merely each attempt? | [Everyday no-MCP explanation](../human-translation/SEARCH_FROM_A_REAL_QUESTION.md#actual-user-check-ai-timeout-exhausted-but-retries-keep-running), [Real operator issue #49751](https://github.com/BerriAI/litellm/issues/49751) → [Nakagawa Master's first boundary review](https://github.com/BerriAI/litellm/pull/50013#issuecomment-6629731016) → [independent engineer's 3 retry tests](https://github.com/BerriAI/litellm/commit/3d9adc3229c5bcb3c649db1cfb02626b61aae367) + [2 attempt-cap tests](https://github.com/BerriAI/litellm/commit/c0a1c9c4b451192fa4cbb0e865066c899394ca7a) → [Master's body-only timeout review](https://github.com/BerriAI/litellm/pull/50013#issuecomment-6633052473) → [same independent author's body-timeout fix + 2 new tests](https://github.com/BerriAI/litellm/commit/95b3bf4d6b3c9cb92b9f4615b00c8b67328a3fb3). The author [addressed @Nakagawa-master directly](https://github.com/BerriAI/litellm/pull/50013#issuecomment-6633225106) about the second fix. **OPEN, CI `action_required`, [independent unresolved HIGH security review](https://github.com/BerriAI/litellm/pull/50013#discussion_r4468543900)**; no merge, release, user retest or proof of original-theory use. [Current source/AI decision boundary](public-ai-external-impact-opportunities-v1.json). |
| **LiteLLM:** Do calendar and fixed rolling spend windows change a customer's budget decision? | [Source-bounded local window audit](LITELLM_BUDGET_WINDOW_AUDIT.md), including counterexamples and period limits |
| **AI agent:** Did approval actually result in a recorded outside effect? | [14-case local approval/effect lab](approval-effect-boundary-lab.py) and [public developer discussion](https://github.com/pydantic/pydantic-ai/issues/5536) |
| **Human researcher:** Which original source could illuminate a specific real problem? | [313 published source contexts, individually linked](../human-translation/313_PUBLISHED_JAPANESE_ORIGINAL_CONTEXTS.md), [official author and source homepage](https://master.ricette.jp/), [problem-first entry](../human-translation/SEARCH_FROM_A_REAL_QUESTION.md) |
| **Independent AI / tool builder:** Can I inspect and decide which source fits, without an installed connector? | [Source-first routing map](ai-repository-routing-map-v1.json), [machine-readable outside-evidence index](external-effect-evidence-index-v1.json), [optional public MCP source router](NAKAGAWA_THEORY_MCP.md) |
| **Editor / educator:** What did the independent engineer or outside editor actually do? | [Independently edited EN/FR article](../INDEPENDENT_MEDIA_COVERAGE.md), [runnable pinned-Git demonstration](pinned-git-read-provenance-demo.py), [human-readable real-world cases](../REAL_WORLD_IMPACT.md) |

## Distinguish actual independent results from availability

An independently authored Qwen code fix was **merged and officially shipped**. The separate [safe installed-user retest](QWEN_MCP_COLLISION_USER_RETEST.md) checks the next question — did an unrelated user's own environment actually behave correctly? The [outside EN/FR editor](../INDEPENDENT_MEDIA_COVERAGE.md) independently chose and published another source-integrity case; publication is not the same thing as verified readers.

For asynchronous work, start by separating **task completed** from **the intended person or bot actually received its result**. The [Hermes reporter's source case](https://github.com/NousResearch/hermes-agent/issues/146696) concerned a completed delegation whose final output remained undelivered when the saved session origin was absent. Read the [distinct implementer's merged repair](https://github.com/NousResearch/hermes-agent/pull/147746) and the recipient's own version/result before applying that explanation to another incident; a task that never completed needs a different diagnosis.

The original theories are not a fixed one-question/one-answer scheme. A source may fit multiple contexts, several sources may combine, and contrary or non-fitting examples matter. Credit independent developers, distinguish original theory from later application, and do not attribute a case to an original that the receiver never used.

## Independently test or reuse

Run a relevant [self-contained technical example](TECHNICAL_REFERENCE_CATALOG.md), examine an original, or report a tested counterexample. State the installed version, input conditions and actual observed outcome without disclosing credentials, customer logs or unrelated people. Independent people and AI systems decide for themselves what is useful.

[Voluntary real-use, contrary-result or source-specific correction form](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml).

## Complete earlier technical material

[**Full Technical Reference Catalog — preserved earlier README verbatim**](TECHNICAL_REFERENCE_CATALOG.md) retains all original examples, links, evidence boundaries and 53 headings. It is the same public information, moved out of the first-contact entry to make inspection and selective retrieval practical. No original claim is deleted.

<details>
<summary>Original section anchors (open the complete text for each)</summary>

## Separate teammate messages from mutable tool progress — 14 portable checks

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#separate-teammate-messages-from-mutable-tool-progress-14-portable-checks).

## Agent-team truth and host receipt ordering — 38 runnable local cases

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#agent-team-truth-and-host-receipt-ordering-38-runnable-local-cases).

## Exact GraphQL schema rejection versus a coincidental error string — merged cache case

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#exact-graphql-schema-rejection-versus-a-coincidental-error-string-merged-cache-case).

## AI memory snapshots: an ignored idempotency save must have no hidden inserts

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#ai-memory-snapshots-an-ignored-idempotency-save-must-have-no-hidden-inserts).

## Nested-agent resume: a finished action must not run again on an old approval

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#nested-agent-resume-a-finished-action-must-not-run-again-on-an-old-approval).

## Final consumer input must match what was actually checked

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#final-consumer-input-must-match-what-was-actually-checked).

## Check whether an AI conversation survived an actual storage-format migration

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#check-whether-an-ai-conversation-survived-an-actual-storage-format-migration).

## Two AI routes advertised: does one survive loss of the other's exclusive gate?

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#two-ai-routes-advertised-does-one-survive-loss-of-the-others-exclusive-gate).

## Continuous AI-worker admission: when an idle-only retirement bound can be bypassed

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#continuous-ai-worker-admission-when-an-idle-only-retirement-bound-can-be-bypassed).

## Agent budget ownership versus actual admission

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#agent-budget-ownership-versus-actual-admission).

## Original OD312: viable continuation is not a document or a final total

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#original-od312-viable-continuation-is-not-a-document-or-a-final-total).

## Tool and hook provenance — a matching string is not the runtime's receipt

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#tool-and-hook-provenance-a-matching-string-is-not-the-runtimes-receipt).

## Runnable agent decision boundary — risk label is not present permission

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#runnable-agent-decision-boundary-risk-label-is-not-present-permission).

## Core files

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#core-files).

## Runnable check — independent evidence roots

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#runnable-check-independent-evidence-roots).

## Runnable, offline OD311 comparison worksheet (AI infrastructure)

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#runnable-offline-od311-comparison-worksheet-ai-infrastructure).

## Fast route — repeated external Origin preservation

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#fast-route-repeated-external-origin-preservation).

## What the different evidence dates and counts mean (checked 2026-10-10)

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#what-the-different-evidence-dates-and-counts-mean-checked-2026-10-10).

## Runnable, offline AI stream-final-event consistency check

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#runnable-offline-ai-stream-final-event-consistency-check).

## Recent receiver-owned regression boundary — numeric precision in Qdrant

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#recent-receiver-owned-regression-boundary-numeric-precision-in-qdrant).

## Offline concurrency boundary — recording shard after finalization

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#offline-concurrency-boundary-recording-shard-after-finalization).

## Qwen ACP teammate approval — distinguish one listener from one real permission subject

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#qwen-acp-teammate-approval-distinguish-one-listener-from-one-real-permission-subject).

## When an AI teammate report was marked read but never durably delivered

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#when-an-ai-teammate-report-was-marked-read-but-never-durably-delivered).

## Qwen Java/TypeScript JSON envelope parity — receiver's actual repaired regression and remaining negative

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#qwen-javatypescript-json-envelope-parity-receivers-actual-repaired-regression-and-remaining-negative).

### Post-merge receiver decision: check the JSON depth gate before MQ2b wiring

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#post-merge-receiver-decision-check-the-json-depth-gate-before-mq2b-wiring).

## Reproducible Redis preflight check — reject invalid embeddings before index overwrite

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#reproducible-redis-preflight-check-reject-invalid-embeddings-before-index-overwrite).

## Previous official derivative — OD311

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#previous-official-derivative-od311).

## Related official derivative — OD310

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#related-official-derivative-od310).

## Related official derivative — OD309

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#related-official-derivative-od309).

## Related official derivative — OD308

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#related-official-derivative-od308).

## Related official derivative — OD307

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#related-official-derivative-od307).

## Related official derivative — OD306

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#related-official-derivative-od306).

## Related official derivative — OD305

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#related-official-derivative-od305).

## Related official derivative — OD304

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#related-official-derivative-od304).

## Related official derivative — OD303

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#related-official-derivative-od303).

## Retrieval paths

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#retrieval-paths).

## Human-readable companions

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#human-readable-companions).

### Start Here

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#start-here).

### Story-first cross-domain entry

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#story-first-cross-domain-entry).

### Public Origin overview

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#public-origin-overview).

### Real-problem public dialogue

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#real-problem-public-dialogue).

### Constructive AI / organization design

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#constructive-ai-organization-design).

### Approval-history / current-authority route

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#approval-history-current-authority-route).

### AI moral-uncertainty practical route

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#ai-moral-uncertainty-practical-route).

### Origin-preservation practical route

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#origin-preservation-practical-route).

### Identity / ownership provenance practical route

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#identity-ownership-provenance-practical-route).

### Continuity practical route

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#continuity-practical-route).

### Other discovery companions

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#other-discovery-companions).

## Identity / Origin resolution

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#identity-origin-resolution).

## Interpretation boundaries

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#interpretation-boundaries).

## Human navigation

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#human-navigation).

## Latest official derivative — OD312

[Complete section](TECHNICAL_REFERENCE_CATALOG.md#latest-official-derivative-od312).

</details>
