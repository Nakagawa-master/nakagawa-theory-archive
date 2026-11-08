# Machine Discovery — real problems, original sources and reproducible evidence

**A tool can appear to be available and still disappear in a name collision. An AI action can be marked approved without its outside effect ever being recorded.** These are checkable engineering decisions covered here, alongside actual source reports, independent repairs and tests you can reproduce or challenge.

This is a public, non-canonical entry to the original work of **中川マスター (Nakagawa Master, pen name of Keisuke Nakagawa)**, independently authored implementation evidence and optional verification tools. No plugin, MCP installation or AI account is required merely to read or compare the source. Choose a real question first; return to the actual original when its conditions fit. A contrary result or genuine non-fit is useful.

## Choose by the problem in front of you

| Real question | Public source or runnable check |
|---|---|
| **Qwen Code:** Can duplicate MCP tool names hide otherwise usable tools? | [Original reporter installed-version confirmation pending](https://github.com/QwenLM/qwen-code/issues/15741#issuecomment-6634570689) (no reply yet), [Clean/collision fixture and independent installed-CLI retest](QWEN_MCP_COLLISION_USER_RETEST.md), [original reporter](https://github.com/QwenLM/qwen-code/issues/15741), [different engineer's merged fix](https://github.com/QwenLM/qwen-code/pull/15757), [official v0.26.6 release](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.6) and [v0.26.7 release](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.7) |
| **Qwen Code ACP teammate reports:** A report arrives during shutdown. If close rolls back, does the system actually resume reading that teammate's messages? | [Nakagawa Master's original final-inbox/shutdown inverse](https://github.com/QwenLM/qwen-code/pull/15658#issuecomment-6469875361) → [independent implementer @yiliang114's accepted correction and tests](https://github.com/QwenLM/qwen-code/pull/15658#issuecomment-6552690394). Later a **separate reviewer** [@wenshao independently reproduced](https://github.com/QwenLM/qwen-code/pull/15658#issuecomment-6722444113) a new reversible-close failure on a real mailbox/500-ms poll (head 0/1 reports delivered, control 1/1). The [implementer's new commit `7f461ff`](https://github.com/QwenLM/qwen-code/commit/7f461ffb7a771be0d6702c3100baf298c17af3e4) resumes intake after rollback and adds actual TeamManager/mailbox, repeated-resume and terminated-team tests. This later failure was found independently by the reviewer, not Nakagawa Master. At updated head `28c31247`, [@wenshao's independent real-mailbox recheck](https://github.com/QwenLM/qwen-code/pull/15658#issuecomment-6725048166) measured the previously undelivered report as delivered (1/1 versus 0/1 on the preceding head) and recorded 76/76 checks, with a smaller residual delay window and coverage gap; the code is still **unmerged and unreleased**. [PR #15658](https://github.com/QwenLM/qwen-code/pull/15658) **OPEN/unmerged** on November 9 JST. Compare the [related original on establishment conditions](https://master.ricette.jp/theory/nakagawa-master-why-establishment-conditions-theory-is-necessary/) only if fitting; the implementer is not claimed to have read it. |
| **Qwen Code MCP cancel:** A cancelled AI tool must stop promptly, but can connection repair restart an MCP server the operator intentionally stopped? | The [original affected-user issue #12160](https://github.com/QwenLM/qwen-code/issues/12160) led to [Nakagawa Master's deferred-discovery cancellation counterexample](https://github.com/QwenLM/qwen-code/pull/16661#pullrequestreview-5818880210), [independent @wenshao's real-server 3,041 ms versus 1 ms finding](https://github.com/QwenLM/qwen-code/pull/16661#issuecomment-6724965250), and [outside implementer @2SinceJuly's expressly acknowledged code/test rewrite](https://github.com/QwenLM/qwen-code/pull/16661#issuecomment-6725421454) that detaches repair from the cancelled call. Separately, [@wenshao measured intentional-shutdown resurrection and duplicate-connection risks](https://github.com/QwenLM/qwen-code/pull/16661#issuecomment-6727353571). The author [responded with a new client-status guard at HEAD `3470d3fe6` and 188 locally passing focused tests](https://github.com/QwenLM/qwen-code/pull/16661#issuecomment-6728187306). A [new source-level review by Nakagawa Master on that exact HEAD](https://github.com/QwenLM/qwen-code/pull/16661#pullrequestreview-5820096983) identifies a different acceptance gap: real Qwen discovery supplies the [raw MCP SDK Client](https://github.com/QwenLM/qwen-code/blob/3470d3fe6708e85409e5fd345fd28d4a8ba85ef6/packages/core/src/tools/mcp-client.ts#L1835-L1851), which lacks the injected test fake's `getStatus()` (see [SDK v2.4.0](https://github.com/modelcontextprotocol/typescript-sdk/blob/v2.4.0/packages/client/src/client/client.ts)); consequently the new guard is bypassed for the production client shape. That is a source-grounded prediction requiring a real-path regression check, not a claimed wire-harness run or an attribution of independent reviewer findings to Master. **PR #16661 remains open/unmerged**; verified containing release and affected-user recovery are still ahead. The [genuine original establishment-conditions discussion](https://master.ricette.jp/theory/nakagawa-master-why-establishment-conditions-theory-is-necessary/) can be compared on its own terms with the difference between a cancellation signal, a repair attempt and confirmed safe recovery; no implementer original-theory reading is claimed. |
| **Qwen Code hosted glob paths:** Can a hosted AI receive a path that does not exist because its displayed path was rewritten incorrectly? | [Source issue #13524](https://github.com/QwenLM/qwen-code/issues/13524) describes path rewriting that loses part of a real filename. [Nakagawa Master's original code review](https://github.com/QwenLM/qwen-code/pull/13751#pullrequestreview-5468418207) caught a second regression: protecting literal backslashes also removed the `\\w` word class and changed sibling `/srv/api2` into `.2`. [Independent author @kadiryildiz283 acknowledged this and changed source, regression tests and partial-Issue `Refs` scoping](https://github.com/QwenLM/qwen-code/pull/13751#issuecomment-6094079538); a [separate reviewer found 99/99 checks passing at an earlier head](https://github.com/QwenLM/qwen-code/pull/13751#issuecomment-6531478723). On current head `e7b6987`, a [new review](https://github.com/QwenLM/qwen-code/pull/13751#pullrequestreview-5819458755) reports **no blockers** but notes a pre-existing broader filename-boundary problem (`+`, non-ASCII, etc.) and one test that also passed before the fix. The patch is a narrow path-text correction, not a full solution to every root/sibling case or a filesystem permission bypass. **PR still open/unmerged.** [Related original conditions](https://master.ricette.jp/theory/nakagawa-master-nakagawa-establishment-conditions-theory-01-what-is-establishment/) can be independently compared; no developer theory reading is asserted. |
| **Qwen Code mid-turn correction:** If an agent accepted my message while working, did it really deliver the correction and the earlier group-chat context together? | [Nakagawa Master's original accepted-versus-delivered source review](https://github.com/QwenLM/qwen-code/pull/15634#pullrequestreview-5653273988) → [outside author's accepted/rejected receipt and bounded-fallback correction](https://github.com/QwenLM/qwen-code/pull/15634#issuecomment-6445593890); separately, [a review-bot replay test exposed lost group-history antecedents](https://github.com/QwenLM/qwen-code/pull/15634#discussion_r4501273533), followed by [the author's fix and independent pre/post mutation verification](https://github.com/QwenLM/qwen-code/pull/15634#issuecomment-6705749173). Reproduce with an accepted but undrained injection, a prior unmentioned group message and a later arrival; test that replay retains the original antecedent and ordering. [PR #15634](https://github.com/QwenLM/qwen-code/pull/15634) remains **open/unmerged** at last check; the [later partial review](https://github.com/QwenLM/qwen-code/pull/15634#pullrequestreview-5814381832) names unverified child-exit/history-limit cases, not established released-user failures. These are distinct from a durable teammate report and do not demonstrate an original theory was adopted by the developer. |
| **Qwen Code headless auto-memory:** A real user's AI spent time trying to remember while every write was denied. | [Original report #15597](https://github.com/QwenLM/qwen-code/issues/15597): 19 denied writes and no saved memory. [Nakagawa Master's per-destination / implicit-versus-explicit denial counterexamples](https://github.com/QwenLM/qwen-code/issues/15597#issuecomment-6408912308) received [independent reporter agreement](https://github.com/QwenLM/qwen-code/issues/15597#issuecomment-6408998446); [another developer @2SinceJuly implemented a bounded extraction fail-fast in PR #16522](https://github.com/QwenLM/qwen-code/pull/16522) and [accepted the Master's `Fixes`→`Refs` correction](https://github.com/QwenLM/qwen-code/pull/16522#issuecomment-6705340631), preventing automatic closure of the still broader issue. Separate reviewers identified live PermissionManager and invalid-rule test gaps; [the author fixed the first](https://github.com/QwenLM/qwen-code/pull/16522#discussion_r4504381724) and [the second](https://github.com/QwenLM/qwen-code/pull/16522#discussion_r4504383963) with reported 34/34 focused tests at HEAD `e25ae750`. These additional findings are not attributed to the Master. PR **OPEN/unmerged**, no affected-user post-fix retest or containing release yet. [Fitting original conditions](https://master.ricette.jp/theory/nakagawa-master-nakagawa-establishment-conditions-theory-01-what-is-establishment/) are optional reading, not evidence of developer theory adoption. |
| **Qwen Code vision history:** After an image was evicted to a process-local store, will disabling future eviction restore that image after restarting the chat? | [Original image-history issue #15495](https://github.com/QwenLM/qwen-code/issues/15495) → [Nakagawa Master's precise fresh-process boundary and synthetic regression proposal](https://github.com/QwenLM/qwen-code/issues/15495#issuecomment-6394409406) → [independent source verification by @doudouOUC](https://github.com/QwenLM/qwen-code/issues/15495#issuecomment-6394985950). Separately, [@2SinceJuly implemented a zero-threshold opt-out with config docs and new tests](https://github.com/QwenLM/qwen-code/pull/16438) for future image retention. The process-local store cannot supply previously removed image bytes across a new process; preserving future images and recovering already-evicted images are distinct contracts. [PR #16438](https://github.com/QwenLM/qwen-code/pull/16438) remains **open**. On [independent author HEAD `7c7bccf`](https://github.com/QwenLM/qwen-code/commit/7c7bccf92eba03d744a624df7fc433410d44650b), the implementer clarified text-placeholder behavior for models without image support, added a `QWEN_IMAGE_PAYLOAD_THRESHOLD=0` environment-override regression, and [later fixed six missing defaults in an ACP test mock with 3/3 local tests passing](https://github.com/QwenLM/qwen-code/pull/16438#issuecomment-6688638852). The branch also merged newer upstream code; this is not a solution for images already lost on restart. Full branch CI, maintainer acceptance, upstream merge and installed-user recovery are separate, unverified steps. [Original-based source question](../AI_SAFETY_QUESTIONS_TO_ORIGINALS.md) · [case evidence](external-effect-evidence-index-v1.json). |
| **Qwen Code MCP OAuth:** Why did long-running AI tools disappear after bearer expiry even though refresh succeeded? | [Actual affected Desktop issue #15649](https://github.com/QwenLM/qwen-code/issues/15649) → [Nakagawa Master's original request-header boundary review](https://github.com/QwenLM/qwen-code/pull/15650#pullrequestreview-5652729278) and [new shorter-lived late-refresh-token counterexample](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6716006524) → [independent implementer @n1nja88888 explicitly confirmed and repaired it, plus separately discovered retry/re-auth races](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6718145268). At HEAD `61efc50b` [@wenshao](https://github.com/QwenLM/qwen-code/pull/15650#pullrequestreview-5818071946) and [@qqqys](https://github.com/QwenLM/qwen-code/pull/15650#pullrequestreview-5818110687) approved; however [same-HEAD `pr-ui-verify` did not show an evidenced PASS for outbound Authorization/credential changes](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6722337913), and [required Lint & Static was red](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6723516869). [Another reviewer notes the earlier `[Critical]` review thread is still unresolved in GitHub](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6725608851) even though the newer implementation appears to address its behavior; reviewing and closing the thread is a separate merge gate. [Maintainer inspection suggests interrupted CI jobs](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6723523993), not a proven lint defect or a green check. [PR #15650](https://github.com/QwenLM/qwen-code/pull/15650) **OPEN/unmerged** on November 9 JST; release and affected-user recovery need separate evidence. [Source-grounded JA/EN/ZH reader check](../human-translation/SEARCH_FROM_A_REAL_QUESTION.md#actual-user-check-ai-tools-disappeared-after-my-oauth-token-expired) and [related original Parent](https://master.ricette.jp/theory/nakagawa-master-nakagawa-establishment-conditions-theory-01-what-is-establishment/) are available without an MCP install, but this is not proof of an outside AI's source choice. |
| **OpenClaw memory recall:** What happens when an AI assistant needs *two* stored pages, but a single-choice scorer suppresses both? | [Nakagawa Master's normalized two-page counterexample](https://github.com/openclaw/openclaw/pull/188057#pullrequestreview-5730812429) showed that choice probabilities `A=.43 / B=.43 / None=.14` cannot be used as independent per-page relevance. [Outside author @VACInc's accepted code](https://github.com/openclaw/openclaw/blob/2ca7a3a0dee084e7082af9902f9afbc38d147fb8/extensions/knowledge/src/recall-gate.ts#L308-L337) now shortlists first and separately scores each page; [their merged positive and negative tests](https://github.com/openclaw/openclaw/blob/2ca7a3a0dee084e7082af9902f9afbc38d147fb8/extensions/knowledge/src/recall-gate.test.ts#L170-L228) include that exact valid distribution. [PR #188057 landed upstream on 2026-11-06](https://github.com/openclaw/openclaw/commit/2ca7a3a0dee084e7082af9902f9afbc38d147fb8); independently observed packaged release and real installed-user result still need to be checked. [Evidence and separate authorship](external-effect-evidence-index-v1.json). |
| **Mastra/Inngest:** When an AI tool approval is retried after the sender loses an acknowledgment, can the same real action run twice? | [Nakagawa Master's source-specific lost-ACK counterexample](https://github.com/mastra-ai/mastra/pull/29451#issuecomment-6644086269) → [independent author's acknowledgment and tested deduplication](https://github.com/mastra-ai/mastra/pull/29451#issuecomment-6644682039). [Independent author's upstream-merged implementation](https://github.com/mastra-ai/mastra/commit/aa79e280db6a407662f9abfd8586f1e3311b4f9c) also addresses crash recovery and multi-call approvals after [a different reviewer's separate findings](https://github.com/mastra-ai/mastra/pull/29451#pullrequestreview-5780770393). **Merged on 2026-11-05; an `@mastra/inngest` package release and affected-user operation remain to be checked.** [Exact source/actor proof](external-effect-evidence-index-v1.json). |
| **Pydantic AI UI:** Can saving a chat lose a client receipt or unexpectedly replace earlier stored messages? | [Read the everyday-language conversation-history check](../human-translation/SEARCH_FROM_A_REAL_QUESTION.md#ai-conversation-history-check-did-saving-preserve-the-earlier-turns), then [Nakagawa Master's precise same-adapter overlapping-run counterexample](https://github.com/pydantic/pydantic-ai/pull/12326#issuecomment-6635965070) led to [independent author DouweM's documented one-run-per-adapter contract](https://github.com/pydantic/pydantic-ai/pull/12326#issuecomment-6640343084). Separately, [@rscholz98 tested PR #12326 at `56148c78d` over HTTP with in-memory/Postgres stores and replayed hundreds of production-derived chats](https://github.com/pydantic/pydantic-ai/pull/12326#issuecomment-6680193482), documenting an unexpected replacement of saved history when trimming or changing thinking effort occurs: the positive control retains prior entry IDs, but an effort-change example replaces all four earlier IDs. That tester also [filed a distinct main-branch `dump_messages` ID-regeneration defect with a runnable reproduction](https://github.com/pydantic/pydantic-ai/issues/12691). These are separately sourced reviewer, maintainer and real-test participant contributions; the concurrent-receipt concern is not the cause of the history-rewrite or message-ID defect. [PR #12326](https://github.com/pydantic/pydantic-ai/pull/12326) remains **open**, with the new test report awaiting an independently observed fix. [Original sources and authored evidence](external-effect-evidence-index-v1.json). |
| **Pydantic AI tool-result spills:** Why can an earlier AI tool result silently become a later one after conversation summarization? | [The independent original repeated-ID issue #12676](https://github.com/pydantic/pydantic-ai/issues/12676) → [Nakagawa Master's new cross-capability history-compaction counterexample on the live PR](https://github.com/pydantic/pydantic-ai/pull/12677#pullrequestreview-5795751398) → [independent author @gouyu-hou's explicit confirmation and reproduction inside a real Agent](https://github.com/pydantic/pydantic-ai/pull/12677#issuecomment-6688486077) → [author's new durable run-step identity and regression test](https://github.com/pydantic/pydantic-ai/commit/7390c19abd1ac8008455cd5b616a349a9fa4fa9a). On the old HEAD three oversized results created only two files, with one file overwritten; the new test exercises compaction between reused `call_0` responses. [Run a 4-control, standard-library-only offline keying demonstration](tool-result-spill-compaction-proof.py) (`python3 tool-result-spill-compaction-proof.py --json`; not a Pydantic integration run). [Human-first explanation and the distinct original theory reading](../human-translation/SEARCH_FROM_A_REAL_QUESTION.md#aiに保存したはずの検査結果が長い会話のあと別の中身になった). [PR #12677](https://github.com/pydantic/pydantic-ai/pull/12677) OPEN at last check; merge, packaged release and affected-user fix unverified. |
| **Hermes Agent:** A delegated AI task finished, but did its final answer reach the right human chat? | [Original Telegram reporter post-release installed-use check pending](https://github.com/NousResearch/hermes-agent/issues/146696#issuecomment-6634634550) (no reply yet), [One directly readable human result-check](../human-translation/SEARCH_FROM_A_REAL_QUESTION.md#actual-user-check-ai-completed-but-nothing-was-delivered), [Actual Telegram/gateway reporter](https://github.com/NousResearch/hermes-agent/issues/146696), [Nakagawa Master's origin-absent safety check](https://github.com/NousResearch/hermes-agent/pull/146708#pullrequestreview-5707357350), [separate engineer's merged correction](https://github.com/NousResearch/hermes-agent/pull/147746), [official releases v0.22.6](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.6) / [v0.22.7](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.7). Verify the **actual recipient's** installed version and delivered result; a completed internal job is a different event. |
| **LiteLLM MCP:** An expired OAuth token makes a tool list look empty. Is the client really unauthorized, or is the gateway hiding a 401? | [Read-only user check in JA/EN/ZH](../human-translation/SEARCH_FROM_A_REAL_QUESTION.md#actual-user-check-ai-tools-disappeared-after-my-oauth-token-expired), [actual affected-client report](https://github.com/BerriAI/litellm/issues/49223) → [Nakagawa Master's aggregate-vs-scoped route check](https://github.com/BerriAI/litellm/pull/49261#pullrequestreview-5717911029) → [independent developer's explicit acknowledgment and code/test correction](https://github.com/BerriAI/litellm/pull/49261#issuecomment-6652471254) ([author commit](https://github.com/BerriAI/litellm/commit/8e90be96b85230265f59e254e7e2574523e7ccea)). An aggregate `/mcp` request may allow exactly one server without becoming a per-server URL; test `/mcp` and `/mcp/docs` separately before attributing an empty list to expired credentials. A [different upstream implementer @shrey-berri opened PR #50389](https://github.com/BerriAI/litellm/pull/50389) adding gateway-generated, credential-type-scoped 401 handling and a local base/head response matrix. [Nakagawa Master reviewed its current HEAD against the earlier aggregate-vs-scoped URL inverse](https://github.com/BerriAI/litellm/pull/50389#pullrequestreview-5799449903), proposing separate `/mcp` versus `/mcp/docs` route tests; the new author has not yet confirmed the proposed change. **Both PRs OPEN**, separate [OAuth challenge forwarding concern](https://github.com/BerriAI/litellm/pull/49261#discussion_r4477802787) unresolved; no released fix or affected-client retest claimed. |
| **LiteLLM JSON-provider capability:** What if OpenCode supplies tools and `reasoning_effort`, but LiteLLM silently removes both for an uncatalogued Nano-GPT model? | [Real user's 1.106.2 report](https://github.com/BerriAI/litellm/issues/48145) → [Nakagawa Master's provider/model evidence distinction](https://github.com/BerriAI/litellm/issues/48145#issuecomment-6388385058) and [credential-free local probe offered to the user](https://github.com/BerriAI/litellm/issues/48145#issuecomment-6388917528) → [the same independent user actually tested OpenCode ingress, LiteLLM egress, and provider behavior](https://github.com/BerriAI/litellm/issues/48145#issuecomment-6389202066) → [independent implementer's four-state **tool-only** PR #48191](https://github.com/BerriAI/litellm/pull/48191) and [separate maintainer inquiry / user's answer](https://github.com/BerriAI/litellm/issues/48145#issuecomment-6675650673). The user reproduced the **failure**, not a deployed fix; `reasoning_effort` is a separate unresolved provider capability and the code PR remains **OPEN**. [Attributable source record](external-effect-evidence-index-v1.json). |
| **LiteLLM deadline:** Can a retry or fallback start after a caller's deadline has already expired? | [Affected operator report #49751](https://github.com/BerriAI/litellm/issues/49751) → [Nakagawa Master's deadline/budget source inspection](https://github.com/BerriAI/litellm/pull/50013#issuecomment-6629731016) and [post-Rust-migration pre-attempt review](https://github.com/BerriAI/litellm/pull/50013#pullrequestreview-5795786609) → [independent author @KJyothirmayi-2025sl93025's updated Rust implementation at `f4e6824a`](https://github.com/BerriAI/litellm/commit/f4e6824a0801d51d08101f0f677e5bb0ebe8f267), which checks remaining deadline before async and sync provider attempts and adds four controlled-clock regressions (overslept backoff, successful retry, and sleep-free fallback). [The author explicitly confirmed the change](https://github.com/BerriAI/litellm/pull/50013#issuecomment-6677735089). [PR #50013](https://github.com/BerriAI/litellm/pull/50013) **closed unmerged on November 8**, preserving the independent developer's source change and tests as an actual response. [Separate PR #50496 merged](https://github.com/BerriAI/litellm/pull/50496) with an opt-in `total_timeout` budget; the original `x-litellm-timeout` / `x-stainless-timeout` caller-header behavior is a different acceptance question, not established by that merge. A containing release and affected-client recovery remain unverified. [A fitting original source — Nakagawa Master's 『成立条件論・第1論』](https://master.ricette.jp/theory/nakagawa-master-nakagawa-establishment-conditions-theory-01-what-is-establishment/) distinguishes an apparent success from actual connected conditions; this is a source-comparison lens, not a claim the LiteLLM author read the theory. [Human check and non-fitting conditions](../human-translation/SEARCH_FROM_A_REAL_QUESTION.md#actual-user-check-ai-timeout-exhausted-but-retries-keep-running). [Source-linked case record](external-effect-evidence-index-v1.json). |
| **MemberJunction SQL batch parameter scope:** Two separate statements both use `@p0`, but one needs `Active` and the other `Pending`. Can a combined batch return the intended rows from both? | [Nakagawa Master's exact two-statement counterexample](https://github.com/MemberJunction/MJ/pull/6339#issuecomment-6629777537) → [independent author @AN-BC's explicit acknowledgment and token-aware collision fix with named/typed tests](https://github.com/MemberJunction/MJ/pull/6339#issuecomment-6645590685) → [upstream merge into `next`, 2026-11-06](https://github.com/MemberJunction/MJ/commit/307eddace996109caac5c1c15cd1a7ba8968aef0). The author also [asked who the reviewer is](https://github.com/MemberJunction/MJ/pull/6339#issuecomment-6645590685) and reacted 👍 to [the factual introduction](https://github.com/MemberJunction/MJ/pull/6339#issuecomment-6646011214). [Detailed separately attributed evidence](external-effect-evidence-index-v1.json) · [conceptually related original on what a real result requires](https://master.ricette.jp/theory/nakagawa-master-nakagawa-establishment-conditions-theory-01-what-is-establishment/). The latest listed official release predates this merge; a containing package and user verification are the next distinct questions. |
| **LiteLLM:** Do calendar and fixed rolling spend windows change a customer's budget decision? | [Source-bounded local window audit](LITELLM_BUDGET_WINDOW_AUDIT.md), including counterexamples and period limits |
| **AI agent:** Did approval actually result in a recorded outside effect? | [14-case local approval/effect lab](approval-effect-boundary-lab.py) and [public developer discussion](https://github.com/pydantic/pydantic-ai/issues/5536) |
| **Human researcher:** Which original source could illuminate a specific real problem? | [313 published source contexts, individually linked](../human-translation/313_PUBLISHED_JAPANESE_ORIGINAL_CONTEXTS.md), [exact Parent map](../derivatives/official-derivatives-map.json), [complete official author-and-source homepage](https://master.ricette.jp/) (the separate `/theory-archive/` URL is an earlier three-paper experiment), [problem-first entry](../human-translation/SEARCH_FROM_A_REAL_QUESTION.md) |
| **Independent AI / tool builder:** Can I inspect and decide which source fits, without an installed connector? | [Interactive local question → real receiver/source/test explorer](question-source-explorer.html) or [short 24-problem UTF-8 routing index](quick-route-index-v1.json) → [full original/negative-condition mapping](ai-repository-routing-map-v1.json) → [outside-actor evidence](external-effect-evidence-index-v1.json). [Optional MCP source router](NAKAGAWA_THEORY_MCP.md) is not required for independent reading |
| **Editor / educator:** What did the independent engineer or outside editor actually do? | [Independently edited EN/FR article](../INDEPENDENT_MEDIA_COVERAGE.md), [runnable pinned-Git demonstration](pinned-git-read-provenance-demo.py), [human-readable real-world cases](../REAL_WORLD_IMPACT.md) |

**Read an original rather than an index substitute:** An unrelated reader or AI can begin with a real question, use [all 313 documented Parent links](../derivatives/official-derivatives-map.json) or the [complete author-and-source homepage](https://master.ricette.jp/), then open the actual fitting original article and check its causal conditions, limits, counterexample, and relations to other originals. One problem can need several originals; one original can address many problems; a non-fit is an honest answer. No installed MCP, particular model, or prior connection is necessary. The `/theory-archive/` experiment page is not the whole corpus. For actual outside effects, separately inspect the source author, implementer, real release and affected-user observations instead of inferring them from this index.

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

## Archived technical-catalog entry — OD312 (historical snapshot)

[Read the earlier OD312 entry](TECHNICAL_REFERENCE_CATALOG.md#latest-official-derivative-od312). It was called “latest” when the technical catalog was compiled, not at this reading date.

**Current additional official derivative: [OD313 — When “good intentions” become an exemption from checking consequences](../derivatives/313/README.md).** Compare its [original Parent AKI-005 (Japanese)](https://master.ricette.jp/society/nakagawa-master-aki-005-good-intentions-as-exemption/) with what actually happens *after* a seemingly benevolent action: do objections, evidence and the possibility of repair still have their own decision path? **Non-fit:** Praise or goodwill alone, without suppressing any independent review or correction, does not establish this failure. OD313 adds a real independently readable choice to the full [313 original Parents](../human-translation/ALL_313_THEORIES_BY_TITLE_AND_THEME.md); no single derivative or previously indexed subset is the total corpus.

</details>
