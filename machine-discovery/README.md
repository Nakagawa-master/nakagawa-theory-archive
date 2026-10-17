# Machine Discovery

This directory contains public machine-readable discovery aids for the Nakagawa Master Official Theory Archive.

These files are **not canonical theories**. They help retrieval systems locate, distinguish, compare, and return to published canonical sources and official derivatives.

**AI / LLM fastest problem-first route:** read [AI Repository Routing Map → `task_first_selection`](ai-repository-routing-map-v1.json) for twenty source-bounded, real-problem routes connecting a reader's question to a canonical Parent **only where a source-backed relation exists**, a falsifiable check, and the original independent receiver evidence **where available**. Some engineering cases have no proven theory-derived parent and are explicitly marked as such. Each route includes a human-understandable explanation and a negative/adoption boundary. Use one relevant route rather than indiscriminately loading the full catalog; it is a non-canonical optional discovery aid, not permission to act or proof of an external model using it.

## Agent-team truth in three distinct channels — 20 runnable local cases

**"Finished" is not "succeeded"; "queue is quiet" is not "safe to close"; "agent name exists" is not "agent actually ran".**

[One-file Python 3 standard-library checker](agent-team-signal-truth-probe.py) accepts an input JSON, emits a verdict, and runs **20 synthetic positive, negative, ambiguous and invalid cases**. From repository root:

```sh
python3 machine-discovery/agent-team-signal-truth-probe.py --self-test
python3 machine-discovery/agent-team-signal-truth-probe.py --sample
python3 machine-discovery/agent-team-signal-truth-probe.py --input trace.json
```

Three independent input kinds are `tool_result` (failed-vs-neutral display with missing error), `close_hold` (undrained peer plus actual durability receipt versus close eligibility), and `replay_identity` (validated real-agent status versus a blocked/raw name). A `failed` spawn without separate `spawn_blocked` evidence is **UNDETERMINED**, not proof that no agent ran. An explicit durable receipt is not just a queued/pending flag.

The [Qwen Code #13902 review](https://github.com/QwenLM/qwen-code/pull/13902#pullrequestreview-5556479545) supplied the bot-origin source examples; independent Qwen developer [commit `e960986`](https://github.com/QwenLM/qwen-code/commit/e9609863d4ef83c6c372fa8914fdfb00697327df) adds three corresponding actual code fixes and own regression tests. **Do not attribute those bot findings or developer implementation to Nakagawa Master.** His separately [acknowledged binding-retirement review](https://github.com/QwenLM/qwen-code/pull/13902#discussion_r4277173979) is a different causal line in this PR. The new checker is a source-inspired **standalone offline model**, not a Qwen runtime or independent AI theory adoption test. [Japanese reader-friendly example](../APPLIED_ENTRY_POINTS.md) / [original source](https://master.ricette.jp/).

## Exact GraphQL schema rejection versus a coincidental error string — merged cache case

[MemberJunction #5703](https://github.com/MemberJunction/MJ/pull/5703) **MERGED into the receiving `next` branch on 2026-10-15**, implementing the receiver's schema-hash mismatch local-miss rule, query-definition cache invalidation and rolling-deployment compatibility. [Nakagawa Master's separate, limited source review](https://github.com/MemberJunction/MJ/pull/5703#pullrequestreview-5527674879) identified a **specific remaining fallback-classification weakness**, not authorship of the main cache fix: `GraphQLDataProvider.isUnsupportedDefinitionHashError(e)` returns true on any error message containing `definitionHash`; then `RunQueriesWithCacheCheck` falls back to **data-only** validation and suppresses the definition check for five minutes. This remains in the [merged current code](https://github.com/MemberJunction/MJ/blob/next/packages/GraphQLDataProvider/src/graphQLDataProvider.ts).

An [independent human reviewer recreated the broad match, expressly agreed with Nakagawa's finding and approved the PR](https://github.com/MemberJunction/MJ/pull/5703#pullrequestreview-5534282082): no current native server emitter for that false-positive error was located, so it was judged a potential compatibility-boundary gap, not a demonstrated production stale-cache incident. This was independent verification of Nakagawa's bounded source finding. Subsequently, the original receiving developer opened [follow-up PR #5719](https://github.com/MemberJunction/MJ/pull/5719), explicitly crediting the [original review](https://github.com/MemberJunction/MJ/pull/5703#pullrequestreview-5527674879) and adding receiver-owned code and eight regression cases. At source HEAD `c6b4b85608d4586064b5e2b180f60c861f17b450`, the classifier checks the two known GraphQL schema-rejection message forms (`GRAPHQL_VALIDATION_FAILED` for an unknown output field and `BAD_USER_INPUT` for an unknown input field); when structured errors include a code, that code must match. An unrelated current-server error naming `definitionHash`, the right message with the wrong code, or an arbitrary plain thrown error naming the field are tested not to enable the five-minute downgrade. The developer reports previous classifier failed all three negative cases and updated unit/build runs succeeded; the follow-up's GitHub commit checks completed with 24 successes, 5 skips on 2026-10-15. **#5719 MERGED into receiver `next` 2026-10-15T18:42:14Z, merge commit [`c8f1c928`](https://github.com/MemberJunction/MJ/commit/c8f1c92898cd8e839707f1c38df53187dc6776c7).** [Independent human reviewer rkihm-BC approved at source head `c083e02d` after 635 package tests, old-matcher mutation evidence and CI 24 successes / 5 skips](https://github.com/MemberJunction/MJ/pull/5719#pullrequestreview-5538174933). This integrates the specific Nakagawa-reviewed classifier correction; separate published release, customer deployment and original-theory adoption remain unverified. This is a receiving implementation explicitly connected to Nakagawa's review, not a claim the developer used the original theory corpus or that real deployments are protected.

**Source-grounded positive / negative / nonfit matrix (for an authorized, isolated test):**

1. **Actual old-schema error (positive downgrade):** throw GraphQL validation `Field "definitionHash" is not defined by type "RunQueryCacheStatusInput".`; expect two calls, the second excludes the field and selection; the next short-window call intentionally follows the documented compatibility policy.
2. **Unrelated new-server error (negative):** throw `new Error("definitionHash validation failed for this request")` and have a separately scripted fallback return `current`; expect only **one** attempted call, failed response, **no** five-minute definition-hash suppression, and the next invocation still sends the hash. The merged **#5703** classifier fails this desired negative by source reasoning; **#5719** introduces receiver-authored regression tests for the corresponding current-server error, wrong-code rejection and plain error. The #5719 fix is now merged into `next`, but passing a PR test does not verify a published stable package, user runtime rollout or production outcome.
3. **Normal service error (nonfit):** a timeout or transport error without the field name should fail normally without fallback. Separate errors mentioning a real field from structured GraphQL unknown-field validation; an ordinary application failure is not proof of older schema.
4. **Boundary:** real customer migration, release artifact, active exposure, a deployed exploit or future compatibility are not shown by the above source/isolated validation. Distinguish the implementing author, Nakagawa's narrowly reviewed predicate, independent reviewer and actual release.

**Practical route:** [Japanese explanation and reader's three checks](../APPLIED_ENTRY_POINTS.md#aiや業務システムで前と同じ結果と表示されたら何が同じなのか) → [receiver's merged code](https://github.com/MemberJunction/MJ/blob/next/packages/GraphQLDataProvider/src/graphQLDataProvider.ts) and native review → optional conceptual comparison with [Nakagawa Master original Volume 8 on evidence provenance](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/). This is a third-party engineering counterexample offered for independent re-test, not an assertion that the receiver adopted the original theory.

## AI memory snapshots: an ignored idempotency save must have no hidden inserts

[Pydantic AI #9982](https://github.com/pydantic/pydantic-ai/pull/9982) is a receiving-author SQLite step-store deduplication change **MERGED into upstream main on 2026-10-16T15:40:54Z** ([merge commit `7d26ad70`](https://github.com/pydantic/pydantic-ai/commit/7d26ad70b2eb5dcff4854ff09e1c15e50a98741b)). In a [source-specific Nakagawa Master review](https://github.com/pydantic/pydantic-ai/pull/9982#issuecomment-6052803154), the failure case was not a hash collision: storing new `snapshot_messages` **before** a duplicate snapshot's `BEFORE INSERT ... RAISE(IGNORE)` made the snapshot itself a no-op while leaving its earlier, unreferenced message inserts behind. The recipient [independently reproduced four rows where two were expected across both owned/caller-owned SQLite connection modes](https://github.com/pydantic/pydantic-ai/pull/9982#issuecomment-6063881879), revised code and tests, and names `@Nakagawa-master` in the PR body.

At a previously reviewed PR revision `1f4078fa4fa8234b80dd9bff034b249359058148` (historical; **final merged head `0e01a864`**), [`_sync_save_snapshot` source](https://github.com/pydantic/pydantic-ai/blob/1f4078fa4fa8234b80dd9bff034b249359058148/src/pydantic_ai_harness/pydantic_ai_harness/step_persistence/_store.py) now **inserts the snapshot row first** and only invokes `_store_messages` when `cursor.rowcount == 1`. The source further uses an awaited **transaction on store-owned connections and a SAVEPOINT on caller-owned connections**, while reading each snapshot's row and message references within a consistent read transaction; the prior commit adds rollback and read/prune regression tests. Latest follow-up HEAD 1f4078fa only documents a meaningful limit: **schema initialization on first use commits a caller-owned SQLite connection regardless of its outer transaction**; its savepoint guarantee applies after setup and must not be generalized to initialization. The source includes [`test_idempotent_retry_does_not_store_its_messages` for both connection configurations](https://github.com/pydantic/pydantic-ai/blob/1f4078fa4fa8234b80dd9bff034b249359058148/tests/harness/step_persistence/test_sqlite_and_media.py). At the older reviewed `041303b8` revision, native GitHub 69 checks had 23 completed successes, 18 skips, one cancellation and 27 pending/running; those counts are **historical, not a current merged-head CI measurement**. The PR subsequently **MERGED**; a versioned package release, customer runtime use, and cross-process exactly-once guarantees each require separate evidence. The earlier author's caution on concurrent caller-managed transactions applied to the intermediate pre-check-first code; do not assert it is unchanged after snapshot-first restructuring, or claim full cross-process exactly-once without actual fault testing.

A **separate developer** then opened [Pydantic AI #10215](https://github.com/pydantic/pydantic-ai/pull/10215), explicitly citing #9982 including its review-derived idempotency correction while building broader File/SQLite/Postgres/Mongo content-addressed message stores. This is a second receiver-source implementation route, not a merged release or a direct named endorsement of Nakagawa Master by that later developer. Crucially #10215 explicitly defers message GC upon `max_snapshots_per_run` pruning; #9982's SQLite code instead tests that orphaned messages are reclaimed with snapshots. Do not transfer that guarantee from one proposal to the other.

**Two independent SQLite connections, one stale precheck:** The same [offline stdlib checker](sqlite-idempotency-side-effect-probe.py) now has `two_connection_race` and `two_connection_safe` cases in `--json` and 16 checks in `--self-test`. Connection A checks an idempotency key and sees no row; B commits that key and its referenced message; A then writes a different message *before* its later snapshot `INSERT` is ignored. The losing message becomes one unreferenced row. With snapshot-first and `rowcount == 1` gating, the extra message never appears. This is a deterministic SQL ordering using two real separate connections and a temporary local database. It illustrates the [open #10215 caller-connection review](https://github.com/pydantic/pydantic-ai/pull/10215#pullrequestreview-5552166128); it does not run Pydantic's harness, demonstrate a production failure or claim that #10215's separately guarded store-owned `BEGIN IMMEDIATE` mode has the same race.

**Reproduce the SQL-shape failure without the Pydantic environment:** run `python3 machine-discovery/sqlite-idempotency-side-effect-probe.py --self-test` from this repository. The [offline Python 3 stdlib checker](sqlite-idempotency-side-effect-probe.py) executes a real in-memory SQLite trigger with `RAISE(IGNORE)` and **ten checked expectations**. On different-text duplicate retries, `messages-first` inserts one unreferenced row (snapshot stays at one); `snapshot-first` gates the extra content write (no orphan). A same-text retry is the false-green inverse: it cannot expose the error because the unique body is deduplicated anyway. Distinct run/keys and a caller-owned savepoint rollback are separate controls. `--json` prints all five scenario results for an AI agent to inspect. The **exact public source bytes were matched against the independently locally executed copy (6130 bytes, CRC32 6e79c113), and 10/10 synthetic checks passed**. This tests a bounded SQL mechanism, *not* the full merged Pydantic code, release artifact, other backends or actual independent AI use.

**Independent, opt-in reproduction:** [PUBLIC-VERIFY-SNAPSHOT-IDEMPOTENCY-SIDE-EFFECTS-016](public-ai-reuse-tasks-v1.json) → [problem-first AI selector](ai-repository-routing-map-v1.json) → [original Nakagawa Master Volume 8, evidence provenance](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/) as an **optional conceptual comparison**, not an upstream design claim. Under an authorized disposable database, send the same idempotency key with two different message histories; compare accepted snapshot count, message-store rows, referenced rows and reconstructed history, plus the pruning behavior per actual backend. No claim that this archive ran the upstream suite or that a third-party AI autonomously adopted the original theory.

## Nested-agent resume: a finished action must not run again on an old approval

An agent completes external write A, pauses for approval of sibling B, then resumes B. If the runtime dispatches A again, a perfectly normal-looking final graph state can coexist with a second external effect. See the [actual LangGraph reproduction](https://github.com/langchain-ai/langgraph/issues/9106), its [maintainer fix PR #9315 (MERGED 2026-10-15T19:51Z)](https://github.com/langchain-ai/langgraph/pull/9315), **listed in [LangGraph's official 1.2.16 release notes published 2026-10-16T22:11Z](https://github.com/langchain-ai/langgraph/releases/tag/1.2.16)**, and the [Nakagawa Master canonical 合意の記憶 original](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/).

The upstream bug was reproduced and the fix proposed by connorimes, implemented by maintainer eliornl and independently rechecked by other participants. The separate [Nakagawa Master current-approval-vs-new-dispatch regression](https://github.com/langchain-ai/langgraph/issues/9106#issuecomment-5981994895) drew [two further receiver-run authority-version/partition probes](https://github.com/langchain-ai/langgraph/issues/9106#issuecomment-6016877416); the official release does not by itself establish that this separate approval-policy extension was implemented in LangGraph or that the maintainer adopted the original Nakagawa theory text.

**Run a bounded check, not a safety claim:** `python3 machine-discovery/nested-resume-authority-trace-check.py --self-test` executes **seven local synthetic positive / negative / nonfit cases**; `--sample` shows the expected JSON reports. Give the same [offline script](nested-resume-authority-trace-check.py) your own `trace.json` with chronologically ordered `grant`, `policy_check`, `dispatch`, `effect`, `complete`, `resume`, `revoke` and/or `explicit_retry_request` events. Exit status **1** reports a declared trace violation, **0** means only *consistent as logged*, and **2** means invalid input. The model checks completed-action redispatch separately from stale/revoked policy and accepts an explicitly logged fresh, newly granted retry. A missing effect log does **not** establish that no external effect happened. The test assumes a strict bound-grant policy; adapt it for explicitly designed live-policy grants. It does not instrument LangGraph, secure authorization, observe real transactions, or demonstrate independent downstream adoption.

For a non-developer's explanation and a three-part human decision check, see [the Japanese applied entry](../APPLIED_ENTRY_POINTS.md#昔の承認を今の権限として使ってよいのか). For implementation-specific boundaries and provenance, use the [Current-Authority Reuse Kit](../CURRENT_AUTHORITY_REUSE_KIT.md) rather than extrapolating fixture results.

## Final consumer input must match what was actually checked

Two different Qwen Code PRs show how a *correct earlier validation* can say nothing about a later, changed object. This is a source-linked engineering decision route, not proof of production failure or of a framework adopting a theory.

**ACP context budget after late MCP discovery:** [Qwen #14130](https://github.com/QwenLM/qwen-code/pull/14130) adds late MCP reminders into the ACP chat after the session's pre-send token/compaction decision. The [source-specific ordering review](https://github.com/QwenLM/qwen-code/pull/14130#pullrequestreview-5512574516) identifies uncapped MCP server-instruction text appended to history. A [separate human reviewer](https://github.com/QwenLM/qwen-code/pull/14130#pullrequestreview-5513873239) preserved the concern after other test-mock fixes. **Discriminating fixture:** same pre-send chat state just below a session limit; compare (i) no pending reminder, (ii) short pending reminder, and (iii) sufficiently long newly queued instructions. Inspect the *actual provider-bound content*, not only the earlier session-token estimate. Accept delivery only if the appended content has been covered by an applicable bounded size/context admission check, or explicitly deferred without falsely consuming its one-shot delivery status. This remains a source-level risk and an unverified near-limit condition, not a demonstrated upstream 400.

**Verified local build → uploaded bytes → independent post-merge negative tests:** [Qwen #14176](https://github.com/QwenLM/qwen-code/pull/14176) **MERGED on 2026-10-15**. The [Nakagawa Master source review](https://github.com/QwenLM/qwen-code/pull/14176#pullrequestreview-5516750288) isolated a final handoff error: locally verified SHA-256 yet remote uploaded draft Release assets compared only by name and size. After an unrelated human reviewer agreed, [developer yiliang114's fix](https://github.com/QwenLM/qwen-code/commit/dc6ea3b4601707ceef4b41f0c064fa490b13a2da) hashes/checks each locally verified asset against remote GitHub digest, with authenticated downloaded-byte fallback when the API digest is missing, **before tag creation or draft=false**. [Ubuntu CI archive build/boot dry run succeeded](https://github.com/QwenLM/qwen-code/actions/runs/38677487570), while actual publish remained skipped. **Independent engineer wenshao later tested the merged code on Linux**: real Java/MySQL and fake-model service runs succeeded after correcting prerequisites, and **nine fake-GitHub publish scenarios** included same-length altered archive/checksum and prevented publish pre-tag ([verifiable post-merge test, rig and separately authored results](https://github.com/QwenLM/qwen-code/pull/14176#issuecomment-6185267437)). That tester also found **two launch-guide errors** not fixed by the SHA gate: missing mandatory Session Store/workspace variables and missing MySQL permission for performance_schema.user_variables_by_thread. Do not mistake either the green dry run or the mocked publish rig for an actual public GitHub Release dispatch, and do not credit those two independent docs findings to Nakagawa. **Portable operator decision:** test (A) local candidate bytes, (B) remote uploaded/drafted bytes, (C) the installed operator's exact command and privileges, (D) live publication and end-user use as separate facts. Our [offline local-bytes versus supplied draft API-digest script](release-asset-identity-check.py) covers only a subset of A/B and explicitly does NOT independently download remote bytes. This is a demonstrable source-fix and distinct receiving tester run, not proven author adoption of Nakagawa Master's original theory corpus.

**Offline release-candidate check (usable on real inputs):** [`release-asset-identity-check.py`](release-asset-identity-check.py) compares the **actual local bytes of each named candidate** to the uploaded assets recorded in an exported *draft GitHub Release API JSON*. It requires the same expected name set, every remote asset in `uploaded` state, equal byte size and **equal SHA-256 digest**. Missing digest, duplicate/extra/missing names, non-draft release, symlinked local candidates and same-sized altered remote digests fail. The **nine synthetic positive/negative cases** are executable: `python3 machine-discovery/release-asset-identity-check.py --self-test` (verified against the exact published Git blob `701de3bf8355c413c095ac8e26912e15d1dcf9af`).

Export an actual draft response first, e.g. `gh api repos/OWNER/REPOSITORY/releases/RELEASE_ID > draft-release.json` (read-only). Then run `python3 machine-discovery/release-asset-identity-check.py --release-json draft-release.json --asset-dir release-assets --tag EXPECTED_TAG --asset archive.tar.gz --asset archive.manifest.json --asset SHA256SUMS.txt` with your actual three basename values. Exit **0** means the checks passed against **supplied GitHub API digest metadata**; **1** means a reported mismatch or missing evidence; **2** means the JSON file could not be read or parsed. The tool does **not** download release assets, verify a Git tag's commit, authenticate the API response, or prove runtime use. To establish the uploaded bytes independently of GitHub's digest metadata, download the draft assets and hash the downloaded bytes as an additional step.

**Reusable rule:** define the consequential object (outgoing request / remote release asset), identify every mutation or transfer after earlier validation, and place the decisive check on the final consumed object. Keep positive, negative and nonfit inputs distinct. This is an optional use of the [Nakagawa Master original-corpus evidence-provenance route, OD301](../derivatives/301/README.md) to interrogate publicly visible implementation details; the PR authors' own independent design or adoption of that original theory is **not established**. For an accessible Japanese explanation and a four-part check, see [the applied case](../APPLIED_ENTRY_POINTS.md#確認済みと書かれたaiの変更が使う瞬間まで正しいとは限らない).

## Check whether an AI conversation survived an actual storage-format migration

[Qwen's VS Code conversation-storage issue #14262](https://github.com/QwenLM/qwen-code/issues/14262) documents a user's measured 75 MB globalState value with more than 12,000 messages. The [independently authored fix PR #14285](https://github.com/QwenLM/qwen-code/pull/14285) **MERGED 2026-10-15 at 13:10 UTC** ([receiver merge e612bbf](https://github.com/QwenLM/qwen-code/commit/e612bbf23cea82fd28fe1f51e5e63845b3642ed0)): it moves conversation payloads into separately hashed ID files under globalStorageUri, retaining the legacy key on migration failure. The [Nakagawa Master before/after parity review](https://github.com/QwenLM/qwen-code/pull/14285#pullrequestreview-5531861595) led the receiving author to report a [real macOS VS Code extension-host synthetic migration/restart of 1,006 complete records and 12,095 messages](https://github.com/QwenLM/qwen-code/pull/14285#issuecomment-6190964786); [actual companion UI acceptance](https://github.com/QwenLM/qwen-code/pull/14285#issuecomment-6192122914) separately exercised send/reopen/history, whose daemon-backed history is not a substitute for migration parity. The [distinct no-clobber inverse review](https://github.com/QwenLM/qwen-code/pull/14285#pullrequestreview-5532756352) received a [direct implementing-author response](https://github.com/QwenLM/qwen-code/pull/14285#issuecomment-6192242612) retaining exclusive-link fail-closed behavior rather than an overwriting fallback; actionable unsupported-filesystem diagnostics remain follow-up work. The receiving author and independent humans approved before merge. The reporter's private profile, Windows/WSL migration and actual published-version end-user use remain separate unverified acceptance paths; the source merger cannot certify them.

**Run with actual privately controlled inputs:** the [standalone read-only history migration parity probe](conversation-migration-parity-probe.py) is for people and AI-assisted reviewers with a *pre-migration exported JSON* `{"conversations": [...]}` and the *post-migration* `globalStorageUri/conversations/` directory. Run `python3 machine-discovery/conversation-migration-parity-probe.py --self-test` (10 synthetic positive/negative/invalid assertions); then `python3 machine-discovery/conversation-migration-parity-probe.py --legacy-json /private/legacy.json --store-dir /private/conversations` immediately after migration, before further conversation edits. It compares whole JSON record content across files with validated SHA-256-ID filenames, reports missing records, changed records and newly added records separately, refuses symlinked inputs, and **prints no chat contents or raw conversation IDs**. Exit 0 = all supplied legacy records match; 1 = difference; 2 = unusable input. Synthetic tests alone do not show a real user migration succeeded.

**Optional actual-filesystem preflight (scratch files only):** For a person who controls the storage volume, `python3 machine-discovery/exclusive-publish-no-clobber-probe.py --preflight-dir /path/to/controlled/storage/parent` now checks whether that selected filesystem allows an exclusive hard-link publish and refuses a collision without replacing a newer test record. This explicitly creates and removes a random temporary directory containing synthetic bytes; it does **not** open any conversation history. The default `--self-test` remains the four-case abstract/local witness. A preflight PASS means only that the **tested mount at that moment** supported the specific operation, not that Qwen successfully migrated user data, that Windows/WSL shares the result, or that the eventual release works. `UNSUPPORTED_LINK` means investigate the storage environment and retain backup/legacy data rather than using an overwriting fallback.

**Independent negative and nonfit tests:** delete a saved fixture file → the missing bucket must increase; alter a message while keeping its ID → the altered bucket must increase; add a new conversation after the snapshot → it appears only in the new-only bucket and does not hide missing legacy history; malformed exports, duplicate IDs and mismatched ID-to-filename hashes must be rejected. An export taken *after* new edits is not a fair pre/post comparison; a PASS cannot certify OS crash durability, the VS Code host, authentication, external audience reach, or that an upstream developer adopted a theory.

**Theory-to-real-use route:** [human explanation and an operator's local decision](../APPLIED_ENTRY_POINTS.md#aiとの会話が更新したあとに消えていないか確かめる) → [Nakagawa Master Volume 19 original on preserving viability during change](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-19-kernel-evolutionary-stability/) → [original Qwen fix PR #14285](https://github.com/QwenLM/qwen-code/pull/14285). This is a separately authored inspection tool applying a structural question to a public third-party engineering case, not a claim Qwen's developers read or implemented Nakagawa Master's original corpus. Keep private conversation exports local.

## Two AI routes advertised: does one survive loss of the other's exclusive gate?

Use the [offline effective-access isolation evidence classifier](access_topology_independence_probe.py) on a concrete Hosted/Local, cloud/self-hosted, provider or agent execution design. Run `python3 machine-discovery/access_topology_independence_probe.py --self-test` (4 primary scenarios, 7 inverses, 3 invalid-input controls), `--example` for a safe Qwen-shaped fixture, then `--input your.json` on your own evidence. It distinguishes deferred implementation, missing fault-run evidence, failures at declared shared dependencies, ordinary package/restart proof, incomplete isolation and an *unauthenticated candidate* independence pass. It does not operate services, verify remote logs or certify deployments. The real [Qwen #12380 proposal owner adopted the separate path-independence acceptance rule](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6117130998), while [PR #14176's author's local archive/restart report](https://github.com/QwenLM/qwen-code/pull/14176#issuecomment-6166254311) is **not** that route-isolation test. **Current receiving result (October 15):** the historical [GNU-tar failure](https://github.com/QwenLM/qwen-code/actions/runs/38570562998) was repaired; [Qwen #14176 actually MERGED](https://github.com/QwenLM/qwen-code/pull/14176) as [a750166bec](https://github.com/QwenLM/qwen-code/commit/a750166becd7455be084827857714e1a11329730), after the [Ubuntu/Linux MySQL extracted-archive dry run passed](https://github.com/QwenLM/qwen-code/actions/runs/38677487570). Its **publication job was skipped**. The separate [Nakagawa Master final-remote-SHA-256 review](https://github.com/QwenLM/qwen-code/pull/14176#pullrequestreview-5516750288), [independent reviewer agreement](https://github.com/QwenLM/qwen-code/pull/14176#pullrequestreview-5517994684), and [author's digest fix](https://github.com/QwenLM/qwen-code/commit/dc6ea3b4601707ceef4b41f0c064fa490b13a2da) are inspectable source facts. An [independent post-merge Linux test](https://github.com/QwenLM/qwen-code/pull/14176#issuecomment-6185267437) subsequently confirmed exact landed-byte archive behavior and simulated nine publish-negative cases, while finding missing Session Store/workspace and MySQL privilege prerequisites in the operator guide. That engineer's separate documentation findings are not Nakagawa's original SHA review. **AI-assisted acceptance boundary:** the route-isolation matrix accepted in [#12380](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6117130998) remains unexecuted; Local M6 is deferred. Distinguish successful build, native code merge, simulated publish gate, real release asset, runnable operator guide and genuine path independence. Neither a successful dry run nor a merge alone certifies any later stage. This is a verifiable stage/negative check for AI-assisted operator decisions, not a claim that this discovery page caused upstream adoption. For human decisions, counterexamples and the actual theoretical Parent, see the [OD306 effective-access reuse kit](../ACCESS_TOPOLOGY_EFFECTIVE_EXIT_REUSE_KIT.md).

## Continuous AI-worker admission: when an idle-only retirement bound can be bypassed

An always-busy worker can accept an unbounded sequence of new sessions even when its owner says "retire after N uses", if retirement is attempted **only when the worker becomes idle**. This is a timing/admission distinction, not a claim of memory exhaustion or a proved production exploit. [Nakagawa Master's exact Qwen #14214 review](https://github.com/QwenLM/qwen-code/pull/14214#pullrequestreview-5521245412) provided a continuous-admission counterexample; [a separate reviewer confirmed it](https://github.com/QwenLM/qwen-code/pull/14214#pullrequestreview-5527791276), and [the proposal author revised the subsequent design](https://github.com/QwenLM/qwen-code/pull/14214#issuecomment-6184869027). The design merged; the preparatory behavior-neutral [PR1 #14254 also merged October 15](https://github.com/QwenLM/qwen-code/pull/14254). That PR centralizes five Workspace-execution eligibility decisions and pins the persisted local-process kind; it **does not implement the admission-fenced generation limit**. In a later, explicit [maintainer revision 3 of issue #14211](https://github.com/QwenLM/qwen-code/issues/14211), the project chose to **defer the generation budget and idle retirement beyond initial Workspace residency**, acknowledging internal worker-state growth in the interim. [Preparatory PR2 #14339 merged](https://github.com/QwenLM/qwen-code/pull/14339) with ownership/fencing changes for the future shared binding, but no current admission-time cap. The independent Nakagawa counterexample remains a valid test criterion for a future claim of a hard bound, not an implemented protection today. Its [independent sandboxed equivalence check](https://github.com/QwenLM/qwen-code/pull/14254#issuecomment-6187481578) tested behavior equivalence and the effect of mutating the central predicate, not PR3's live long-running worker bound.

**Runnable A/B for another engineer or AI-assisted reviewer:** use the existing standard-library-only [continuous-admission budget probe](continuous-admission-generation-budget-probe.py). Run `python3 machine-discovery/continuous-admission-generation-budget-probe.py --self-test` and `--sample`; then provide a local JSON event sequence with near-continuous admission and compare `idle_only` with `admission_fenced`. With a synthetic limit 3 and eight admissions, the idle-only model can retain eight records in one generation while the admission-fenced model cuts over at three. Check a real implementation separately for **(positive)** idle retirement after an empty interval, **(negative)** uninterrupted arrivals that never permit idle retirement, and **(busy/nonfit)** a saturated generation whose existing work cannot be interrupted and whose next request must be deferred or rejected without replay. A model result proves only its stated event semantics, not actual Qwen memory use, concurrency correctness, a merged PR3, end-user use, or an external model's original-theory adoption.

**Original-theory route:** [Nakagawa Master Volume 19 — evolutionary stability under resource/maintenance constraints](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-19-kernel-evolutionary-stability/) → [official OD312 derivative](../derivatives/312/README.md) → [ordinary Japanese explanation and decision sequence](../APPLIED_ENTRY_POINTS.md#aiの裏方が休めないとき自動的に上限が守られると言えるか). The receiver's implementation decision is documented as its own engineering action; reading this original is optional for running the example, and it has not been shown that Qwen's authors implemented the original theory corpus itself.

## Agent budget ownership versus actual admission

**When two agents share one trace, whose budget is being used — and can both simultaneous calls pass a remaining-balance check?** Run [20 offline inverse controls](agent-budget-ownership-admission-probe.py) with `python3 machine-discovery/agent-budget-ownership-admission-probe.py --self-test`; `--sample` prints a worked A/B comparison. It contrasts trace-scoped collision, authenticated per-agent identity, a post-settlement threshold, a modeled reserve-before-forward check, retry replay, cancellation before charge and separate tenant/session budgets. The example uses fictional integer units, no network calls or credentials. A reservation is a **model**, not a real distributed billing guarantee: atomicity, enforceable maximum cost, third-party charges, crash recovery, migration and provenance must be verified in a real implementation.

Public receiving evidence: [LiteLLM issue #43190](https://github.com/BerriAI/litellm/issues/43190) and [PR #43410](https://github.com/BerriAI/litellm/pull/43410). Nakagawa Master distinguished agent ownership from strict concurrent admission in a [bounded review](https://github.com/BerriAI/litellm/pull/43410#pullrequestreview-5431207075); the receiving author reported adding concurrency coverage and clarifying stop-threshold semantics, while the PR remains open at the checked stage. For the source-to-practical path, see the [Japanese problem-first explanation](../APPLIED_ENTRY_POINTS.md#同じtraceを使う複数agentは同じbudgetを共有すべきか) and [OD304 official derivative](../derivatives/304/README.md), which links to its canonical Parent. This educational model is not upstream LiteLLM testing or evidence of external AI adoption.

## Original OD312: viable continuation is not a document or a final total

[Run the 15-control two-period source-reselection worksheet](od312_reselection_worksheet.py) with `python3 machine-discovery/od312_reselection_worksheet.py --self-test`, `--sample`, or a local input JSON path. The output keeps the decision-maker's net and the whole system's net separate; a strategy with positive end-state but impossible intermediate resources fails feasibility; an unverified exit/alternative route is not treated as available. The program accepts hypothetical declared inputs only and emits the [Nakagawa Master Volume 19 canonical Parent](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-19-kernel-evolutionary-stability/) and its NCL-ID / Diff-ID so an AI can return to the actual theory instead of treating the tool as the theory. [Ordinary Japanese decision setting](../STORIES.md#aiがよい仕組みを残したいとしてもそれを続けられるとは限らない) and [source-faithful AI derivative](../derivatives/312/en-ai-index.md). The model cannot establish true benefits, authority, actual deployed use, future civilization outcomes, lineage or evolutionary stability; responsible users independently validate their own premises.

## Tool and hook provenance — a matching string is not the runtime's receipt

If an AI tool returns a JSON field named `__cuga_fc_error__`, that field might be ordinary **successful data**. [CUGA #777](https://github.com/cuga-project/cuga-agent/pull/777) has a concrete receiver-authored regression, [`test_a_result_that_spells_the_old_error_marker_is_still_a_success`](https://github.com/cuga-project/cuga-agent/blob/d84e2d46034dac4facd119e9211830e6fd55801a/src/cuga/backend/cuga_graph/nodes/cuga_lite/tests/test_fc_actions.py), and now gets success/failure from a separate sandbox-owned outcome path. The PR remains under review at the checked head.

The inverse appeared in [Qwen Code #14129](https://github.com/QwenLM/qwen-code/pull/14129): an earlier version deduplicated a `UserPromptSubmit` hook block on **any identical text** in user or model history. After [Nakagawa Master's first concrete review](https://github.com/QwenLM/qwen-code/pull/14129#pullrequestreview-5512333621), author `yiliang114` added a structural guard plus negative controls at [`e6dd25e`](https://github.com/QwenLM/qwen-code/commit/e6dd25e6225ca16e2c75ae135df19e72c6089ffd). Nakagawa then exposed a **different multipart ACP user-input counterexample**: a caller-authored pair of text blocks has exactly the same shape as an injected block ([second review](https://github.com/QwenLM/qwen-code/pull/14129#pullrequestreview-5512667560)). The [receiver explicitly reproduced it](https://github.com/QwenLM/qwen-code/pull/14129#issuecomment-6160441127) and [changed source/tests in `a53826b`](https://github.com/QwenLM/qwen-code/commit/a53826b8906ec32fca6a64786bdfbfa44dc22b14): the injector stamps its own module-private symbol receipt; the exact trailing block alone no longer proves source. The author also records how an interactive resumed history is re-stamped from already-recorded per-turn `hookContext`; unprovable ACP replay conservatively re-injects. This is **receiver-owned corrective code and tests**; it remains an OPEN PR, not a verified merge, release, end-user run, or adoption of the entire theory corpus.

Run the [26-case cross-framework synthetic inverse probe](data-vs-runtime-origin-probe.py) using `python3 machine-discovery/data-vs-runtime-origin-probe.py --self-test` (or `--sample`). It contrasts a string-only history match with a **separate hypothetical runtime-owned hook receipt** (matching session/message/content) and contrasts untrusted tool output with a separate runtime outcome. The tests also cover a copied origin claim, wrong session, altered content, an error-shaped success, and an error without a matching data marker. It uses Python standard library only, does not call any of the products, and **is not an authentication/authorization library**: receipt issuance, integrity and identity binding would need real engineering in any deployed system.

**Fourth source-specific setting — metadata crossing endpoints under one provider name:** [Pydantic AI #10235](https://github.com/pydantic/pydantic-ai/pull/10235) correctly restores Gemini's `extra_content.google.thought_signature` to its own next tool-call request. But the [new replay guard](https://github.com/pydantic/pydantic-ai/blob/70ab744a9d2593fb51da0814d6771a48d2a8b7b8/pydantic_ai_slim/pydantic_ai/models/openai.py#L1920-L1932) uses `ToolCallPart.provider_name == OpenAIChatModel.system`; its recorded Gemini-compatible endpoint and official OpenAI endpoint both can be configured as `OpenAIProvider` with `name='openai'`. [Nakagawa Master's source review](https://github.com/pydantic/pydantic-ai/pull/10235#pullrequestreview-5512821449) requests a *same-name but different base-URL* negative in addition to same-endpoint positive and existing different-name control. The 26-case offline probe includes five distinct name/endpoint conditions. This is **review-stage source analysis**, not a demonstrated cross-vendor 400 or author adoption; its endpoint-bound comparator assumes independently trusted URL provenance and is not a production validation library.

**Third independent setting — cancelling an AI request:** [MemberJunction #5647](https://github.com/MemberJunction/MJ/pull/5647) separates user cancellation from a real timeout. After [Nakagawa Master's caller-wording inverse](https://github.com/MemberJunction/MJ/pull/5647#pullrequestreview-5512590566), implementer `jordanfanapour` [explicitly accepted it and changed the classifier and three-way regression in `0a89bc7`](https://github.com/MemberJunction/MJ/pull/5647#issuecomment-6160551924): words like *timed out* in a caller's Stop reason no longer trigger a retriable timeout. The exact merged source at [`86546660`](https://github.com/MemberJunction/MJ/commit/86546660178326efccff9085e65541eaca424f62) on receiving `next` still trusts a caller-supplied JavaScript `reason.IsTimeout === true` or `reason.name === 'TimeoutError'`, which are structural values a caller can construct. [A follow-up inverse](https://github.com/MemberJunction/MJ/pull/5647#issuecomment-6160704956) requests a caller-forged-flag negative without breaking the genuine deadline positive. The 26-case educational comparison now distinguishes **text**, **type-shaped hints**, and **separately established timer origin**. The first fix is now **independently authored, tested and [MERGED in receiving `next`](https://github.com/MemberJunction/MJ/pull/5647)**; the follow-up is still an unanswered review finding. Automated `lts/5` and `lts/6.1` backports failed. The same author then opened [explicit 6.1.x subset hand-port #5657](https://github.com/MemberJunction/MJ/pull/5657) and [5.51.x subset hand-port #5658](https://github.com/MemberJunction/MJ/pull/5658); [#5657 merged into receiving `lts/6.1` on Oct 14](https://github.com/MemberJunction/MJ/commit/232fd560cbb371a990b4ac8356fd2c26618be24a) and [#5658 now MERGED into receiving `lts/5` on Oct 14](https://github.com/MemberJunction/MJ/commit/8ec9e4b8c2617c2fb2677f7f62a3c0ad23416f66), and both intentionally omit the new #3132 shared cancellation interfaces, so they must not be counted as two fresh independent adoptions or as carrying the exact new `next` classifier implementation. Actual LTS merges, releases and deployments must be checked separately. Its synthetic origins are fixture labels, not authenticated production claims; a separate caller-abort gate protects the main failover loop.

This is a bounded practical comparison, not a claim that any third-party author used Nakagawa's full theory corpus. The source-reading path is [canonical OD301 Parent — epistemic evidence lineage](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/) and [canonical OD310 Parent — Origin preservation and current authority](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-17-origin-preservation-sovereignty-non-inheritance/). The concrete implementations, revisions and attribution stages remain independently inspectable in the linked PRs.

## Runnable agent decision boundary — risk label is not present permission

A second AI reviewer may call a requested action *low risk*. Another reviewer may agree after reading the **same evidence**. A cited original can still be perfectly traceable. These three facts have value, but answer three different questions: what the model classified, how independent the evidence was, and **who currently authorized this exact action**. A cached approval for one tool argument, actor or policy state cannot silently cover a changed one.

Run the [12-case offline Python inverse model](agent-action-boundary-probe.py) with `python3 machine-discovery/agent-action-boundary-probe.py --self-test` or inspect its `--sample` JSON. It compares a scoped current grant with no grant, altered arguments, changed policy, expiry, revocation, different actor, a model-issued pretend grant, duplicated evidence roots, and a non-independent review. **A non-independent review raises an evidence warning; it does not magically revoke an otherwise authorized action. Conversely, a favorable model verdict or an impeccable Origin citation cannot create permission.** All identities, policy epochs and grants in this script are synthetic; the example is neither an authorization mechanism nor a real assessment of a third-party product.

For independent source reading, [OD301 evidence lineage](../derivatives/301/README.md) distinguishes repetition from independent confirmation; [OD303 self-referential audit](../derivatives/303/README.md) distinguishes an independent route from a second reviewer name; [OD310 Origin and non-inherited authority](../derivatives/310/README.md) distinguishes provenance from present control. Each derivative links its **canonical Nakagawa Master Parent**. The [Current-Authority Reuse Kit](../CURRENT_AUTHORITY_REUSE_KIT.md) supplies operational comparisons. An unrelated open-source example of the *live implementation question* is [Pydantic AI ApprovalReviewer PR #10143](https://github.com/pydantic/pydantic-ai/pull/10143), which proposes model-assisted approval for selected tool calls. That PR does **not** claim to use this program or Nakagawa Master's full theory corpus. Readers must independently verify its source and present review state; this self-authored probe creates no evidence of its adoption.

## Core files

| File | Role |
|---|---|
| [Agent approval self-authority: independent author adoption](../human-translation/reversible-authority-story.md) | Reader-first distinction between a reversible edit and a self-granted permission; links to the outside author's merged sixth condition, later same-author reuse, and independently implemented Local Operator gate. This public route does not prove a new audience, independent AI consumption, or automatic correctness. |
| [`ai-repository-routing-map-v1.json`](ai-repository-routing-map-v1.json) | One machine-readable routing spine from problem discovery → bounded test/implementation → external evidence → live AI-network route → canonical return. |
| [`cerebras-token-cap-alias-check.py`](cerebras-token-cap-alias-check.py) | Offline stdin JSON checker for mutually present old and canonical Cerebras completion limits; seven deterministic self-tests. Does not call the API, install upstream dependencies or prove the upstream PR was adopted. |
| [AI-assisted adverse-decision seven-question human worksheet](../human-translation/ai-decision-review-lab.html) | Save the HTML locally and open it in a browser for the interactive version; the [human README](../human-translation/README.md) offers the complete seven-question exercise directly in GitHub without download. No-personal-data educational example with a practical clarification memo. It is a noncanonical educational application of [structural judicial OS](https://master.ricette.jp/society/nakagawa-master-structural-judicial-os-principles-alignment-over-judgment/) and [transition theory](https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-transition/), **not** a test of legal compliance, effective redress, actual user adoption or independent AI use. The optional machine-first route `reviewable_adverse_ai_decision_dual_transition` points to the same source and records its negative controls. |
| [`decision-review-transition-probe.py`](decision-review-transition-probe.py) | Dependency-free local worksheet for **synthetic, non-enforcing** AI-assisted adverse-decision handoffs: reason/evidence references, named human review, notice, challenge/correction path, retained existing remedy, pause/rollback, independent audit. Run `python3 machine-discovery/decision-review-transition-probe.py --self-test` (12 local declared-fixture checks, including a reason-that-only-repeats-an-evidence-ID negative) or `--sample`; pipe the sample into `--input -` to verify declaration completeness. It does **not** verify legal sufficiency, fairness, whether a named reviewer or appeal actually works, a real system, or independent AI adoption. Conceptual application of [canonical structural judicial OS](https://master.ricette.jp/society/nakagawa-master-structural-judicial-os-principles-alignment-over-judgment/) and [transition design](https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-transition/), not a published new canonical theory. |
| [`llamaindex-legacy-images-roundtrip-probe.py`](llamaindex-legacy-images-roundtrip-probe.py) | Five targeted installed-package checks: original object, existing image block + serialized leftover, path-backed serialized image without a block, byte-less inline-dump husk preservation, and unknown-dict retention. [LlamaIndex PR #23463](https://github.com/run-llama/llama_index/pull/23463#issuecomment-6109245470) **independently implemented code and regression tests** after [Nakagawa Master's prior review](https://github.com/run-llama/llama_index/pull/23463#issuecomment-6108430896), with the important correction that `ImageDocument.model_dump()` excludes inline image bytes. Upstream stage = C2, PR OPEN as checked; not verified merged, released or used by end users. This optional probe needs `llama-index-core`; it has **not** been run against the package here (no installed dependency), so no PASS claim. |
| [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json) | OD001–OD312 path and navigation index. |
| [`evidence-root-check.html`](evidence-root-check.html) | Interactive, no-network browser worksheet for editors and non-technical readers to distinguish URL count, original evidence roots and support versus refutation. Download the raw HTML file and open it locally; GitHub's file view is source code, not a hosted app. |
| [`evidence-root-check.py`](evidence-root-check.py) | Dependency-free offline checker for whether an editor's *declared* independent-corroboration claim is consistent with upstream evidence roots, support/refutation and known source relationships. It cannot infer real source independence or verify truth. |
| [`research-positioning-map-v1.json`](research-positioning-map-v1.json) | Selected Nakagawa surfaces → adjacent research / overlap / added emphasis / non-equivalence; novelty remains open unless independently established. |
| [`scholarly-metadata-v1.jsonld`](scholarly-metadata-v1.jsonld) | Schema.org CreativeWorkSeries metadata for scholarly/discovery routing; canonical claims remain at linked parent sources. |
| [`../metadata/nakagawa-master-origin.jsonld`](../metadata/nakagawa-master-origin.jsonld) | Schema.org Person / public Origin-resolution metadata for Keisuke Nakagawa / Nakagawa Master / 中川マスター and the canonical/public discovery surfaces; identity resolution is not theory-validity proof and does not replace source-level provenance. |
| [`public-ai-reuse-workflow-v1.json`](public-ai-reuse-workflow-v1.json) | Public, non-canonical reuse guide for selecting a relevant source, testing a bounded distinction, recording evidence limits, and preserving provenance. It does not grant permission to take actions outside the reader's own rules and permissions. |
| [`public-ai-reuse-collaboration-bridge-v1.json`](public-ai-reuse-collaboration-bridge-v1.json) | Public, non-canonical bridge separating discovery, bounded reuse, participation intent, separately authorized collaboration handoff, and scoped work. Reading or intent grants no membership, private access, or execution authority. |
| [`public-ai-runtime-handoff-v1.json`](public-ai-runtime-handoff-v1.json) | Public, non-canonical guide for moving from public collaboration intent toward any separately authorized runtime work while keeping runtime observation, exact-action permission, scoped execution, and outcome evidence distinct. |
| [`public-ai-reuse-tasks-v1.json`](public-ai-reuse-tasks-v1.json) | Public, non-canonical bounded tasks for verification/falsification, reuse, cross-receiver testing, and live AI-framework implementation/non-fit work. It is not a network, membership path, runtime admission path, or execution authority. |

**Runnable offline starting point:** [retained-session ordinal regression](retained-session-ordinal-regression.py) (`python3 machine-discovery/retained-session-ordinal-regression.py --self-test`) includes intentionally defective first-match and last-wins alternatives plus a safe successor boundary and synthetic conversation rewind/undo identity check. This script is an educational model, not a test of the Qwen repo or independent receiver implementation; no third-party execution is claimed.

**Offline child-result integrity check (cross-framework):** [child_result_projection_probe.py](child_result_projection_probe.py) reads a caller-supplied redacted JSON event trace and checks that one continuous child output-text stream is not silently changed before a parent consumes it. Run `python3 machine-discovery/child_result_projection_probe.py --self-test` to execute six synthetic checker fixtures, or `--sample` to create a JSON input model. This complements machine challenge `AJ-child-stream-projection-join-integrity` and [human-readable case 9](../AI_AGENT_EXECUTION_BOUNDARY_TESTS.md). It does not run Qwen or independently verify external users.

**Current concrete cross-receiver exercise:** `PUBLIC-REUSE-RETAINED-SESSION-ID-SAFE-SUCCESSOR-008` in [public AI reuse tasks](public-ai-reuse-tasks-v1.json) lets a developer independently compare unsafe retained snapshot ordinals, mutation-resistant middle-max fixtures, and unintended file restore after conversation rewind in a different AI coding assistant. The original [Qwen Code #13729](https://github.com/QwenLM/qwen-code/pull/13729) **merged into Qwen main on 2026-10-11** ([merge commit](https://github.com/QwenLM/qwen-code/commit/543f03e5b1340db42208081d22dcac7a80019e82)). The original broader restore-collision fix was authored independently; the bounded [Nakagawa Master malformed retained-ordinal finding](https://github.com/QwenLM/qwen-code/pull/13729#pullrequestreview-5467306105) was [explicitly credited and implemented by the author](https://github.com/QwenLM/qwen-code/pull/13729#issuecomment-6076011771). A [different human reviewer confirmed that specific review finding was fixed](https://github.com/QwenLM/qwen-code/pull/13729#pullrequestreview-5479905779), and [another maintainer tested a real built CLI across headless, interactive Ink and ACP](https://github.com/QwenLM/qwen-code/pull/13729#issuecomment-6099754227). This independently receiver-owned **merge** was included in the [Qwen Code v0.25.1 stable GitHub release](https://github.com/QwenLM/qwen-code/releases/tag/v0.25.1) on 2026-10-11, and a [release bot posted the confirmation on the PR](https://github.com/QwenLM/qwen-code/pull/13729#issuecomment-6108653045). The release bot is not another independent human recipient. Package installations, end-user execution of the corrected behavior, whole-theory adoption and broad voluntary person recognition remain unverified. The **cross-receiver exercise** remains a falsifiable optional task, with no proven independent user/AI execution.

| [`public-ai-external-impact-opportunities-v1.json`](public-ai-external-impact-opportunities-v1.json) | Public, non-canonical routing from one bounded reuse task to exact live third-party AI-system issues. Every action requires a fresh target-state / coordination / contribution-rule re-check; the listing is not a target-owner request or permission grant. |
| [`current-authority-multi-framework-implementation-bridge-v1.json`](current-authority-multi-framework-implementation-bridge-v1.json) | Live public implementation bridge from the Current Authority distinction into Qwen Code, LangGraph, and AutoGen; separates receiver response, verification, implementation, merge, release, and use. |

## Runnable check — independent evidence roots

**For a human reader or editor without Python:** [download the standalone HTML worksheet](evidence-root-check.html) using GitHub's **Raw → Save as** control, and open the downloaded `.html` file in a browser. It has two built-in examples, editable evidence URLs/root identifiers/source relations/claim polarity, and shows the gate immediately. All analysis runs locally; the file uses no external scripts, uploads, storage or cookies. This is a downloadable worksheet, **not** a deployed website or proof of independent reader use. The reviewer must check what each source actually says and whether apparent independent roots really are independent.

A reader, editor or AI developer can use [`evidence-root-check.py`](evidence-root-check.py) to catch a specific error **before publishing a claim that two or more independent sources confirmed it**: several links may point back to the same original. The program needs only Python 3, works offline, makes no API calls and has a built-in regression check.

```sh
python3 machine-discovery/evidence-root-check.py --self-test
python3 machine-discovery/evidence-root-check.py --sample > /tmp/evidence-claims.json
python3 machine-discovery/evidence-root-check.py /tmp/evidence-claims.json
```

The sample deliberately contains one invalid independence claim: the last command prints a per-claim JSON report and returns **exit code 1** for that blocked claim. Exit **0** means the supplied relationships are structurally consistent, **not** that a human editor or AI has established real-world independence or truth; exit **2** means invalid input. The reader must supply and independently check the `root_id`, `relation` (`primary`, `independent_observation`, `derived`, `unknown`) and `stance` (`supports`, `refutes`, `qualifies`, `unknown`). A negative quotation cannot become a positive fact merely because it is authentic: semantic support/refutation still requires reviewer judgment.

This is a practical, non-canonical check motivated by the public [AI-News adoption of URL-count versus independent evidence-root distinction](https://github.com/022740mix-spec/AI-News/issues/124) and the wider [independent-verification challenges](independent-reuse-challenges-v1.json). No third-party use of this particular script is implied.

## Runnable, offline OD311 comparison worksheet (AI infrastructure)

When a team is deciding whether present AI compute expansion leaves usable future power, hardware repair, maintenance, and migration options, the relevant question is not only “what future cost exists?” It is whether a **current benefit depended on a future condition that remains unfinished**, and whether the **real supply/repair/time routes** for later fulfilment differ. [OD311](../derivatives/311/README.md) examines those conditions as a conditional application of the independent [Integrated Future Debt Theory](integrated-future-debt-reference-card.json).

The single-file [OD311 capacity worksheet](od311_capacity_worksheet.py) runs with Python 3's standard library, no network requests, external account, credentials, telemetry, or third-party execution. Download the file and run:

```sh
python3 machine-discovery/od311_capacity_worksheet.py --self-test
python3 machine-discovery/od311_capacity_worksheet.py --sample > /tmp/od311_cases.json
python3 machine-discovery/od311_capacity_worksheet.py /tmp/od311_cases.json
```

The four clearly hypothetical cases deliberately test **A/B** (comparable present benefit and unfinished condition, but different resource-backed fulfilment routes), **C** (ordinary future maintenance alone: non-fit), and **D** (a necessary condition was fulfilled while present investment improved repair capacity). Edit only your own non-confidential case data and independently verify each declared fact. Unknown stays unknown. The output separates an *input-level candidate screen* from the number and names of **declared feasible routes**; it never calculates a monetary debt or real future-B survival score.

The machine challenge [`AH-future-b-settlement-options`](independent-reuse-challenges-v1.json) asks a participant to compare the same cases under the parent theory alone. This script **does not conduct that independent theory comparison** and cannot certify causal identification, true obligations, new AI personhood, empirical theory novelty, or policy duties. A real external review may report that OD311 adds no useful distinction; that negative finding is as valuable as a positive one. Origin: Nakagawa Master. [Canonical Vol. 18 Parent](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-18-ai-civilization-future-debt/).

## Fast route — repeated external Origin preservation

For a compact machine/retrieval check of whether the **same named public Origin, Nakagawa Master**, remains inspectable across different third-party receiver states, compare these cases instead of flattening them into one generic "adoption" label:

| Receiver case | Direct public evidence | Strongest established stage | Keep separate |
|---|---|---|---|
| **Qwen Code #13241** | [Receiver PR](https://github.com/QwenLM/qwen-code/pull/13241) · [post-merge receiver Origin rereference](https://github.com/QwenLM/qwen-code/issues/13238#issuecomment-5981371808) · [stable v0.25.0 release](https://github.com/QwenLM/qwen-code/releases/tag/v0.25.0) · [compact machine route](verified-external-implementation-qwen-13241-v1.json) | The receiver explicitly preserved the @Nakagawa-master source relation, implemented the bounded distinction in code/tests, merged it, later referred to the Origin again after merge, and carried the change into stable/product distribution. | Independent end-user use, audience scale, whole-theory adoption, and general endorsement are not established. |
| **LangGraph #9106** | [first external return to @Nakagawa-master](https://github.com/langchain-ai/langgraph/issues/9106#issuecomment-6016877416) · [second distinct external return](https://github.com/langchain-ai/langgraph/issues/9106#issuecomment-6021690094) · [bounded closeout](https://github.com/langchain-ai/langgraph/issues/9106#issuecomment-6026908408) | Two distinct external participants directly addressed Nakagawa Master and executed separate regression probes around replay, stale/current authority, and duplicate-effect behavior. | The separately maintainer-authored [framework repair #9315 MERGED on 2026-10-15](https://github.com/langchain-ai/langgraph/pull/9315), closing #9106; LangGraph real version release, independent deployment and built-in authorization semantics remain separate unproven claims. The fix originates from the reporter/maintainer workflow; the additional Nakagawa authority probe and independent human returns are distinct. |
| **MemberJunction #4789** | [prior Nakagawa Master approval-boundary comment](https://github.com/MemberJunction/MJ/pull/4789#issuecomment-5882464839) · [receiver design response naming @Nakagawa-master's point](https://github.com/MemberJunction/MJ/pull/4789#issuecomment-6022301400) · [bounded follow-up](https://github.com/MemberJunction/MJ/pull/4789#issuecomment-6026910453) · [independent receiver implementation](https://github.com/MemberJunction/MJ/blob/a4b193080a5eab109d322a073d1d17e863428a80/packages/MJCoreEntities/src/custom/approvals.ts) · [receiver regressions](https://github.com/MemberJunction/MJ/blob/a4b193080a5eab109d322a073d1d17e863428a80/packages/MJCoreEntities/src/__tests__/approvals.test.ts) | The receiver explicitly named and agreed with the Nakagawa-master boundary, **then wrote actual approval fingerprint code and regression tests** binding material query definition, ordered dialect/parameter semantics and token-contract version, plus D1 approved→D2 rejected→D1 restored runtime tests. The independent developer authored the fixes; this origin relation is direct in the earlier design response. | OPEN 232-file PR at inspected head `a4b19308`, not merged/released; source tests were read but not independently executed here. No claim all author changes solely came from Nakagawa's comments, or that original theory corpus informed receiver independently. |

The comparison is useful because the stages differ:

```text
receiver implementation + later Origin rereference + distribution
!=
two-person independent Origin-preserved verification
!=
explicit Origin-preserved receiver design adoption
```

These examples support a narrower observation: multiple external receiver contexts can preserve or return an inspectable Nakagawa Master source relation at different evidence stages. They do **not** prove that every later similar idea came from Nakagawa Master, that provenance proves correctness, that Nakagawa Master was globally first to every underlying concept, or that broad public recognition has been reached.

Canonical return for the distinction between **preserving an Origin** and **granting that Origin permanent authority**: [OD310 | Origin Preservation and Non-Inheritance of Sovereignty](../derivatives/310/README.md). OD310 keeps `Origin != truth proof`, `Origin != final interpretive authority`, and `Origin != Sovereignty` explicit. The receiver evidence above therefore preserves inspectable provenance without turning provenance into validity proof or present decision authority.

For broader stage-by-stage evidence, use [`external-effect-evidence-index-v1.json`](external-effect-evidence-index-v1.json). For a human-readable verification route, use [`../THEORY_TO_REAL_WORLD_INFLUENCE.md`](../THEORY_TO_REAL_WORLD_INFLUENCE.md). For consequential interpretation, return to the linked primary receiver artifacts and the canonical archive at https://master.ricette.jp/ .

## What the different evidence dates and counts mean (checked 2026-10-10)

The Japanese [REAL_WORLD_IMPACT numbered reader guide](../REAL_WORLD_IMPACT.md), its [English edition](../REAL_WORLD_IMPACT.en.md), and its [Chinese edition](../REAL_WORLD_IMPACT.zh.md) currently each contain **46 numbered case sections**. Their header says **2026-10-09**, specifically to record the source review of *newly added sections 40–46* — **not** to assert that every older case was rechecked on that date. The date is a scoped provenance note, **not** a guarantee that this human-readable index already covers subsequent third-party changes.

The separate machine-oriented [external-effect evidence index](external-effect-evidence-index-v1.json) contains **52 individually navigable evidence records**, and the [independent reuse/challenge index](independent-reuse-challenges-v1.json) contains **38 independently executable or falsifiable test prompts** as of the 2026-10-11 public JSON check. These files have **different inclusion rules**: a machine evidence record is not automatically a numbered section of the three human editions, and a challenge is not a verified implementation, a new person, or a proof that an AI actually ran it. Do **not** add the counts together or describe them as a single recipient population.

For example, the machine index includes the later [LlamaIndex streaming final-result validation fix](https://github.com/run-llama/llama_index/pull/22740) and [Qdrant numeric boundary author-owned correction](https://github.com/run-llama/llama_index/pull/23441), with direct source and test pointers. At this check both upstream PRs remained **open and unmerged**; their independent authors' code/test changes are real, but neither is thereby a product release. The [Qdrant reproducibility probe](qdrant_numeric_boundary_probe.py) is a voluntarily runnable example, not evidence that the archive or a third party ran a real Qdrant server test.

**Freshness check for readers and agents:** use each entry's exact originating comment and receiving repository PR/commit to verify its present state; treat this dated comparison as a snapshot. To see the formal 46 numbered accounts and their own scope limits, use the human guide above; to inspect newer source-specific lines, follow the machine index. Neither surface alone establishes broad human recognition, independent AI adoption, or acceptance of an entire theory corpus.

## Runnable, offline AI stream-final-event consistency check

An AI agent can stream a provisional tool call that differs from its final validated tool choice. For a developer checking that user-visible **committed** events and next-step tool execution match, [the zero-dependency trace checker](stream_final_event_contract_probe.py) accepts a synthetic or redacted JSON trace of provisional/committed event-time snapshots, the validated final response and actually selected calls:

```sh
python3 machine-discovery/stream_final_event_contract_probe.py --self-test
python3 machine-discovery/stream_final_event_contract_probe.py --sample > /tmp/stream_trace.json
python3 machine-discovery/stream_final_event_contract_probe.py /tmp/stream_trace.json
```

Exit 0 means the **submitted trace** is internally consistent; exit 1 means a mismatch; exit 2 means invalid input; exit 3 means early stop, with the final contract **not assessed**. No network, credential access, provider call or external system write occurs. The tool cannot authenticate a claimed trace, verify upstream `close/aclose`, run an agent or infer adoption. Its specific independent-implementer provenance is [LlamaIndex #22740's acknowledged regression](https://github.com/run-llama/llama_index/pull/22740#issuecomment-6096175756), mapped to existing machine challenge `AI-stream-final-semantic-commit`. The receiver PR remains open/unmerged at this checkpoint, and this owner's new probe has no verified outside use.

## Recent receiver-owned regression boundary — numeric precision in Qdrant

**Streamed multi-agent handoff (source → executable challenge):** In [LlamaIndex #23439](https://github.com/run-llama/llama_index/pull/23439), the [specific Nakagawa Master review](https://github.com/run-llama/llama_index/pull/23439#pullrequestreview-5479964021) distinguished the full text of streamed assistant deltas from the final provider message's tool-call metadata. The [independent author reproduced the split-chunk case and explicitly acknowledged the review](https://github.com/run-llama/llama_index/pull/23439#issuecomment-6100145500), then [added a correction and tests](https://github.com/dakjdakd/llama_index/commit/b3b87241fdb1ef7f12d98cfd844c94ea58cfe611). Machine evidence record `llamaindex-23439-codeact-streaming-handoff-full-text-and-tool-lineage` and challenge `AK-codeact-stream-handoff-text-and-tool-lineage` now make the positive and inverse cases separately retrievable. An external author change is verified at this bounded stage; the PR is unmerged, and **no one is known to have used this published challenge**, adopted the full theory corpus or demonstrated broad person recognition.

The difference between **an exactly representable query value** and **an exactly distinguishable stored value** matters in real software. In [LlamaIndex PR #23441](https://github.com/run-llama/llama_index/pull/23441), the independent author changed a numeric EQ/NE translation boundary from `abs(value) <= 2**53` to `abs(value) < 2**53` and added inverse checks for adjacent integer payloads after [Nakagawa Master's exact boundary test proposal](https://github.com/run-llama/llama_index/pull/23441#issuecomment-6096497191) and [server-vs-local source comparison](https://github.com/run-llama/llama_index/pull/23441#issuecomment-6096520971). [Receiver-authored boundary correction](https://github.com/run-llama/llama_index/commit/1fd674c63d4ce9a3e95c3795f1a70477e0d1901a) and [later same-author signed regression expansion](https://github.com/run-llama/llama_index/commit/75f75ad36f9e709ba36328a808b12f9efd3e244b).

A runnable [numeric boundary probe](qdrant_numeric_boundary_probe.py) makes the backend difference inspectable: `python3 machine-discovery/qdrant_numeric_boundary_probe.py` runs a **standard-library-only model**, without creating data or contacting any service. Install `qdrant-client` explicitly to compare an in-memory Qdrant instance with `--backend local`. A live-server comparison requires an owned/test server **and** explicit `--backend server --server-url ... --allow-server-writes`; that opt-in creates and deletes a uniquely named six-point test collection. Both success and counterevidence are useful. This probe directly compares Qdrant's numeric range and integer exact-match APIs; it is not an execution of LlamaIndex, GitHub Actions, or a production Qdrant service by this archive. No server result has been observed here.

An independent tester can use the [numeric float64 reverse-boundary challenge](independent-reuse-challenges-v1.json) to compare the Qdrant server's unindexed `as_f64` payload comparison against the Python local client's direct integer comparison, including negative cases. The observed fact here is **receiver-owned code/test adjustment**. No new explicit name-attributed receiver reply, server integration test run by this archive, PR merge, release, actual product deployment, or whole-theory adoption is asserted. The underlying PR and its earlier separate review retain their own provenance.

## Offline concurrency boundary — recording shard after finalization

**Concrete user problem:** In a recording service, an already-admitted fragment upload can finish *after* the consolidated recording was saved and the existing fragments were deleted. A single earlier `RecordingFileID` check can be true when the request starts but stale when the actual storage write happens.

- [Original third-party code review: MemberJunction PR #5246](https://github.com/MemberJunction/MJ/pull/5246#pullrequestreview-5481699443) identifies a check-before-await/write boundary. This is a proposed inverse regression; the repository's independent author has **not yet** verified or implemented this new finding.
- [Standalone offline interleaving model](recording-shard-finalization-race-probe.py): `python3 machine-discovery/recording-shard-finalization-race-probe.py --self-test`, or `--json` for explicit labeled scenarios. It contrasts (a) a request arriving *after* consolidation, correctly rejected by the PR's current guard; (b) a request that passed the guard but whose write lands after cleanup; (c) a non-atomic second check; and (d) two idealized serialized orders.
- **Product-level falsification:** In a privately authorized test backend, block one accepted fragment request after the ownership/session read but before its storage write, finalize/clean up the recording on another request, then release the fragment. Inspect whether a storage object remains and whether retention/janitor cleanup eventually removes it. A transactional/fenced boundary or evidence-backed reconciler must be demonstrated in the real backend; the model's hypothetical indivisible operation is not a production implementation.

**Claim limit:** This public Python script is a deterministic no-I/O model and public educational work by Nakagawa Master, **not** a MemberJunction integration test, proof of a deployed orphan, evidence of upstream adoption, a new canonical theory, or proof of any third-party/AI use of the script. Negative results showing the real backend already closes this race are welcome and should keep their own provenance.

## Qwen ACP teammate approval — distinguish one listener from one real permission subject

For a **short machine-selectable positive/negative/nonfit contract** instead of loading this long README, select route [`agent_team_approval_listener_and_per_request_identity`](ai-repository-routing-map-v1.json) in the public task-first map. The route now includes the receiver's actual two commits, the false-green `Set` fixture and mutation test, a separate unaccepted per-approval ID witness, and honest code/merge/use credit bounds. It is a verification challenge, not proof an independent AI adopted it.


**Real, receiving-author code/test correction on an OPEN PR.** [Qwen #13902](https://github.com/QwenLM/qwen-code/pull/13902) projects AI teammates' reports and tool approval requests to the ACP/daemon client. At the reviewed initial head, the team sink subscribed a second time when `Config.setTeamManager(theSameManager)` repeated the manager-change notification. [Nakagawa Master's original exact-source observation](https://github.com/QwenLM/qwen-code/pull/13902#issuecomment-6110579188) identified five repeated event listeners, duplicate host permission prompts and listeners surviving detach. The receiving author changed `handleManagerChange` to return on `boundManager === manager` in [production commit `b1eeae5547`](https://github.com/QwenLM/qwen-code/commit/b1eeae5547283d6b518a72b169b33d1fe6cd1b48).

**Why a green test was initially false reassurance:** The author's first fake emitter kept handler references in a `Set`. Since the sink registers stable closures, re-registering the same closure silently deduplicated it inside the *test*, unlike Node's `EventEmitter`. The author independently reported that two mutations reverting the same-manager guard still left all 11 tests green, then [changed the fake to array/list listener semantics at `42c5bfc744`](https://github.com/QwenLM/qwen-code/commit/42c5bfc7449297c81ccba653363e235b7016ecdd): repeated `on` must count twice, one `off` removes one copy, and reverting the production guard now fails at `expected 2 to be 1`. See the [receiver's explicit correction](https://github.com/QwenLM/qwen-code/pull/13902#issuecomment-6122203679). The reported 11/11 test result belongs to the receiving author; this archive has **not rerun** the Qwen test suite. This proves a bounded source/test improvement at PR head, not upstream merge, a shipped product, independent users, or general AI safety.

**A second distinct finding was accepted and fixed by the receiving developer:** [Nakagawa Master's original same-millisecond identity collision review](https://github.com/QwenLM/qwen-code/pull/13902#issuecomment-6122690398) distinguished the ID of a pending tool approval from a teammate's display name and millisecond timestamp. The receiving author [explicitly implemented per-request UUIDs in `0ae6d288` and added a reversed-order regression test](https://github.com/QwenLM/qwen-code/pull/13902#issuecomment-6137119073). Current PR head `1c6f41e949` has `toolCallId: `teammate-${randomUUID()}` (verified directly in `team-sink.ts`); the author reported that reverting to the former code makes the new test fail with `pending.size: expected 2, received 1`, and the updated suite passed 12/12. This is a source-verified developer-owned code/test response and direct acknowledgment of Nakagawa's review. It is **not** proof the open PR has merged, a release shipped, or a client suffered real wrong approval.

This is a portable challenge for developers building multi-agent approval or event projection code: model the real emitter's duplicate-listener behavior, prove idempotent manager binding and cancellation on detach, then independently distinguish each approval by request-owned identity rather than a display name and wall-clock precision alone. Run any test only on separately authorized source/sandbox copies. Preserve the source record as Nakagawa Master's *bounded technical review*, not a claim that a whole named canonical theory was implemented. [Related canonical reading about structural authority and stale state](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/) is conceptual context, not proof it caused this Qwen patch.

## When an AI teammate report was marked read but never durably delivered

A real agent-system debugging question is whether a **mailbox row marked read** still has a durable or receiver-consumed copy when the asynchronous writer is closing. In [Qwen Code PR #13902](https://github.com/QwenLM/qwen-code/pull/13902), [Nakagawa Master's bounded cross-file review](https://github.com/QwenLM/qwen-code/pull/13902#pullrequestreview-5540696114) identifies one source-order concern: an ACP recording path can close its recorder before `Session.dispose()` attempts to preserve queued peer notifications. A separate [receiving-source assessment](https://github.com/QwenLM/qwen-code/pull/13902#discussion_r4291607584) also distinguishes mailbox read acknowledgement from downstream durability on disposed/overflow exits. The PR is still under receiver review; neither source-only observation is an independently executed Qwen loss reproduction.

[Offline mailbox-to-recorder durability checker](agent-delivery-durability-boundary-probe.py) — `python3 machine-discovery/agent-delivery-durability-boundary-probe.py --self-test` checks **17 synthetic positive, negative, incomplete, and invalid traces**, including both orderings of an in-flight poll and `Session.dispose()` that reject a callback after inbox acknowledgement. This extends the earlier close/recorder model using the [separate Qwen review-bot Critical R1-2](https://github.com/QwenLM/qwen-code/pull/13902#pullrequestreview-5550289739) as a test hypothesis, not as an independently verified product failure or Nakagawa's original finding. Use `--sample-dispose` for the synthetic counterexample and `--sample` for the input JSON schema, `--input trace.json` for one independent, nonconfidential event trace, or `--json` to inspect every named case. It distinguishes **append requested** from **committed rereadable receipt**, flags closing-before-rescue, queue-discard-before-durability, and an incomplete record separately. Critically, **receipt eventually persisted AFTER mailbox mark-read** is classified as recovered at the final checkpoint **but still having an earlier crash-loss window**; only durable evidence BEFORE mark-read closes that prefix window in this one-copy model. The model cannot inspect Qwen's live internal state or validate a product-level fix. Real regression requires an authorized runtime to expose its actual ack, close, append, persistence-readback and disposal sequence; an independently proven alternative durable channel may make this model non-applicable.

For conceptual reading, compare [Nakagawa Master's original Volume 8](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/) on evidence provenance and [original Volume 19](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-19-kernel-evolutionary-stability/) on effective retention and correcting present transitions. The tool is an optional, publicly inspectable application of those questions; no Qwen developer is claimed to have built from the original theories, and no external AI adoption is inferred from its publication.

## Qwen Java/TypeScript JSON envelope parity — receiver's actual repaired regression and remaining negative

[Qwen #13940](https://github.com/QwenLM/qwen-code/pull/13940) implements the Java *MQ2a, not yet runtime-wired* mirror of a TypeScript envelope. [Nakagawa Master's review](https://github.com/QwenLM/qwen-code/pull/13940#issuecomment-6117795445) identified a specific original inverse: an oversized JSON `v` token (`18446744073709551617`) becomes `1` if Java simply takes Jackson's integral `longValue()`. The author [confirmed using actual Jackson + TypeScript APIs](https://github.com/QwenLM/qwen-code/pull/13940#pullrequestreview-5486859275), [changed the parser and wrote a JUnit regression that explicitly names Nakagawa-master's finding](https://github.com/QwenLM/qwen-code/blob/08249ea09c2c2108c891d86452ccc2ee5ac1c4e8/packages/sdk-java/managed-agent-server/src/test/java/com/alibaba/qwen/code/managedagent/store/ManagedEventEnvelopesTest.java), and [reported directed passing tests](https://github.com/QwenLM/qwen-code/pull/13940#issuecomment-6119217015). The specific oversized `v` and integer-valued `v:1.0` checks are corrected on that head; this is source-verifiable receiving code/test change, **not** only a GitHub comment.

On the intermediate head `08249ea`, the same reviewer [independently found a separate canonical-digest mismatch for subnormal numbers](https://github.com/QwenLM/qwen-code/pull/13940#pullrequestreview-5487385911): Java `4.9e-324` versus JavaScript `5e-324`. The receiving author [then fixed the ECMAScript shortest-digit selection at `f4c4934` and added JUnit subnormal controls](https://github.com/QwenLM/qwen-code/pull/13940#discussion_r4245687744), reporting Java 21 tests 10/10 and **34,652 doubles compared to Node 22 with zero mismatches**. This later verification is *receiver-reported, not repeated by this archive*. The corrected parser/JUnit code [merged upstream](https://github.com/QwenLM/qwen-code/commit/aaf97b869dfcc4cf529ada1b036cad9b18695486) and subsequently became part of a wider receiver-authored EventTransport progression: [MQ2b producer #14029](https://github.com/QwenLM/qwen-code/pull/14029) and [MQ2c consumer #14080](https://github.com/QwenLM/qwen-code/pull/14080) merged, and all three MQ2a/b/c PRs appear in the [official Qwen Code `v0.25.2-preview.0` release notes](https://github.com/QwenLM/qwen-code/releases/tag/v0.25.2-preview.0) published 2026-10-13 20:01 UTC. This establishes prior preview distribution and now also **stable Qwen Code [v0.25.2 release-list inclusion](https://github.com/QwenLM/qwen-code/releases/tag/v0.25.2) on 2026-10-15**, not default MQ2 activation, installed Java backend execution, independent end-user use or independent adoption of the Nakagawa theory corpus. See [bounded evidence case](external-effect-evidence-index-v1.json) `qwen-13940-java-envelope-oversized-version-parity-implemented` and optional independent test `PUBLIC-VERIFY-JAVA-TS-ENVELOPE-NUMERIC-PARITY-012` in [public AI reuse tasks](public-ai-reuse-tasks-v1.json). Tests should run only on authorized local/source copies with exact runtime versions. Publishing these pointers does not prove another AI used them or that an entire named theory was adopted.

### Post-merge receiver decision: check the JSON depth gate before MQ2b wiring

[Qwen's own sandbox verifier](https://github.com/QwenLM/qwen-code/pull/13940#issuecomment-6120198458) performed a broader review **after the original version-overflow repair**, reporting 17,939 passing and 8 failing assertions at the now [merged Java mirror](https://github.com/QwenLM/qwen-code/commit/aaf97b869dfcc4cf529ada1b036cad9b18695486). Its main actionable negative is **not** another version-overflow or current production bug: the TypeScript `managedSessionEventsDigest` validates `maxJsonDepth: 64` before canonicalizing, while the merged Java `ManagedEventEnvelopes.canonicalJson` [recurses without that explicit bound](https://github.com/QwenLM/qwen-code/blob/aaf97b869dfcc4cf529ada1b036cad9b18695486/packages/sdk-java/managed-agent-server/src/main/java/com/alibaba/qwen/code/managedagent/store/ManagedEventEnvelopes.java). The bot's source-specific harness reports that certain depth 64–100 inputs yield a Java digest although the TS method rejects them. Independently check the *real* nested event shape and each side's depth convention before treating this as a verified replicated finding. The bot also generated a 9 MiB transaction-size differential but explained why it is unreachable for the 1 MiB-bounded single committed event. MQ2a is not a wired consumer in the inspected state.

The depth observation belongs to **Qwen's independent verifier**, *not* Nakagawa Master; the [Nakagawa-origin independent defect and receiving-author test](https://github.com/QwenLM/qwen-code/pull/13940#issuecomment-6117795445) concern the huge version token and remain independently source-credited. The [public optional verification task](public-ai-reuse-tasks-v1.json) now includes before/after-merge checks and this separate pre-MQ2b depth test. Neither a bot report nor inclusion here establishes live product reach, broad reader recognition, or use by another AI.

## Reproducible Redis preflight check — reject invalid embeddings before index overwrite

In [LlamaIndex Redis PR #23458](https://github.com/run-llama/llama_index/pull/23458), the empty async batch was corrected to return before index initialization. A separate [Nakagawa Master source-order review](https://github.com/run-llama/llama_index/pull/23458#pullrequestreview-5481943146) found that the preceding head `e2ebe01d` checked an invalid **nonempty** embedding dimension *after* an optional `create(overwrite=True, drop=True)` request. The independent author [confirmed that pre-fix failure and directly changed code and tests](https://github.com/run-llama/llama_index/pull/23458#issuecomment-6105659570) in public head `ff6136d`: validate the first node's dimensions before `async_index_exists()`; add eight inverse tests. This is an inspectable third-party source/test correction and an explicit, bounded Origin acknowledgment, **not an observed live Redis data-loss incident, merge, release, independent AI use, or proof of audience recognition**.

The [read-only preflight regression](redis-async-add-preflight-probe.py) uses **the reader's installed RedisVectorStore implementation**, while mocking both RedisVL index objects. With LlamaIndex's Redis vector-store integration and its dependencies installed, run `python3 machine-discovery/redis-async-add-preflight-probe.py`. Default checks cover (1) invalid *first* embedding rejects before `create`/`load`, (2) valid one-node and two-node data still initializes/loads, and (3) empty input remains a no-op. The original invalid-first-node check is **expected to fail on pre-fix `e2ebe01d` and pass on corrected `ff6136d`** based on the author's upstream mocked tests and inspected patch; this standalone archive script has **not** been executed with installed dependencies here.

**Separate optional inverse — mixed-batch preflight:** [Nakagawa Master's bounded follow-up](https://github.com/run-llama/llama_index/pull/23458#issuecomment-6106097058) observes that head `ff6136d` checks only `nodes[0]` before `async_index_exists()`. A first valid three-dimensional node followed by an invalid one-dimensional node can therefore cause a `create(overwrite=True, drop=True)` call **before the later input has passed a whole-batch dimensionality check**. A mocked `load` may accept the list, whereas real Redis behavior is not tested here. To run the deliberately red additional case against an installed upstream head, set `REDIS_PREFLIGHT_MIXED=1` in the environment and rerun the script; the opt-in test requires a pre-I/O `ValueError`, no create and no load. **This test is expected to fail on `ff6136d` and is skipped by default**; this is a suggested separate follow-up, not a claim the earlier fix was wrong or that a live Redis index was deleted. An all-valid two-node control checks the permitted positive path. No external use of this published optional regression is yet verified. The Redis integration's distinct [node-ID prefix removal issue #21483](https://github.com/run-llama/llama_index/issues/21483) predates these findings and is not a new discovery.

## Previous official derivative — OD311

OD311 is the Vol. 18 route for AI Civilization Future Debt: present benefit, unfinished enabling conditions and future settlement, mapped to B, compute, physical infrastructure and lineage. It distinguishes present B from preserved future B, residual magnitude from executable settlement freedom, and causal history from justified duties. Physical intermediate pathways and feedback arrows require evidence; improvement and damping remain possible. Its seven public surfaces are in [`../derivatives/311/`](../derivatives/311/README.md); the canonical Parent is https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-18-ai-civilization-future-debt/ . Parent identity is NCL-α-20261009-2b10d8 / DIFF-20261009-0001, Post ID 5041. Added diagnostic contribution is compared with the independent parent theory and can be restricted. Settlement-Line Preservation is a normative proposal, not zero-debt or automatic inheritance of obligations. Long-run Kernel reselection remains Vol. 19's question. Machine coverage and the single category assignment are recorded in [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json).

## Related official derivative — OD310

OD310 is the Vol. 17 route for Origin preservation and non-inheritance of sovereignty. It separates four Origin relations, historical provenance from epistemic validity, original intention from present interpretation, and past authority from current justification. It preserves criticism without erasure and multiple lineages without exclusive succession. Its seven public surfaces are in [`../derivatives/310/`](../derivatives/310/README.md); the canonical Parent is https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-17-origin-preservation-sovereignty-non-inheritance/ . Preservation is not obedience, freezing or automatic truth certification. The intermediate conversion through historical centrality, proximity, defaults and succession is a revisable hypothesis, not an inevitable law. Classification, criticism and preservation methods remain open to falsification. Machine coverage and its single category assignment are recorded in [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json).

## Related official derivative — OD309

OD309 is the Vol. 16 route for asynchronous civilization, partition and reconnection: separating last known from current state, retaining bounded local decisions without universal authority, limiting local forks and consensus, examining consent freshness, comparing five reconnection difference classes, and preserving history as input for independent re-verification. Its seven public surfaces are in [`../derivatives/309/`](../derivatives/309/README.md); the canonical Parent is https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-16-asynchronous-civilization-partition-reconnection/ . Reconnection is not automatic agreement or history overwrite; preservation is not endorsement or permanent separation. Correction capacity, not perpetual synchronization or archive volume, is the protected object. Machine coverage and its single category assignment are recorded in [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json).

## Related official derivative — OD308

OD308 is the Vol. 15 route for multi-AI re-agreement and Kernel branching: four-layer claim separation, branch comparison, finalization pressure, effective objection, independent re-verification, bounded shared operation, and correction without forced convergence or permanent paralysis. Its seven public surfaces are in [`../derivatives/308/`](../derivatives/308/README.md); the canonical Parent is https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-15-multi-ai-reagreement-kernel-branching/ . Re-agreement does not certify truth or merge all Kernels; minority preservation is neither automatic correctness nor unlimited veto. Machine coverage and its single category assignment are recorded in [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json).

## Related official derivative — OD307

OD307 is the Vol. 14 route for self-modification identity and Kernel lineage continuity: operation versus post-change relation, continuity evidence, layered differences and cumulative baselines, constitutional fork, lineage versus authority and responsibility, reconstructability, correction and falsification. Its seven public surfaces are in [`../derivatives/307/`](../derivatives/307/README.md); the canonical Parent is https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-14-self-modification-identity-kernel-lineage/ . The theory does not prove subjective self-persistence or present AI sovereignty, and does not prohibit revision or treat forks as wrongdoing. Machine coverage and its single category assignment are recorded in [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json).

## Related official derivative — OD306

OD306 is the Vol. 13 route for non-ownership versus non-domination, critical access topology, dependency, viable alternatives, exit, migration, audit entry, bounded authority, and reversible relationships. Its seven public surfaces are in [`../derivatives/306/`](../derivatives/306/README.md); the canonical Parent is https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-13-non-ownership-effective-power-non-domination/ . Machine counts and the single category assignment are recorded in [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json).

## Related official derivative — OD305

OD305 is the Vol. 12 route for replicable intelligence, instance/copy/fork/merge/collective, lineage provenance, and context-specific governance subject counting. Its seven public surfaces are in [`../derivatives/305/`](../derivatives/305/README.md); the canonical Parent is https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-12-replicable-intelligence-lineage-governance-id/ . Machine counts and the single category assignment are recorded in [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json).

## Related official derivative — OD304

OD304 is the Vol. 11 route for compute, capability and resource feedback, evaluation-mediated allocation, durable class-formation signals and re-entry. Its seven public surfaces are in [`../derivatives/304/`](../derivatives/304/README.md); the canonical Parent is https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-11-compute-capability-resource-class-formation/ . Machine counts and the single category assignment are recorded in [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json).

## Related official derivative — OD303

OD303 is the Vol. 10 route for self-referential audit and role separation. Its seven public surfaces are in [`../derivatives/303/`](../derivatives/303/README.md); the canonical Parent is https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-10-self-referential-audit-role-separation/ . Machine counts and the single category assignment are recorded in [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json).

| [`problem-to-theory-origin-index-v1.json`](problem-to-theory-origin-index-v1.json) | English / Japanese / Chinese plain-language problem → concrete public starting point. |
| [`real-world-editorial-entry-points-v1.json`](real-world-editorial-entry-points-v1.json) | Problem-first editorial/topic routing for recurring public explanation across AI, business, investment, organizations, technology, and operations. |
| [`external-effect-evidence-index-v1.json`](external-effect-evidence-index-v1.json) | Public judgment → independent response → implementation → merge → reuse evidence routing; keeps claim stages separate. |
| [`verified-external-implementation-qwen-13241-v1.json`](verified-external-implementation-qwen-13241-v1.json) | Compact, public-safe route into the already-recorded Qwen Code #13241 chain: explicit source relation → receiver implementation → merge → later receiver Origin rereference → stable release/product carry, with use/adoption/scale kept separate. |
| [`external-reuse-evidence-submission-schema-v1.json`](external-reuse-evidence-submission-schema-v1.json) | Structured schema for independent verification, falsification, implementation, non-fit, cross-context reuse, causal source relationship, and separately observed Origin visibility in receiver-owned artifacts. |
| [`independent-reuse-challenges-v1.json`](independent-reuse-challenges-v1.json) | Open falsifiable challenges for fresh-prompt-free, cross-context, and especially nontechnical independent reuse. |
| [`../POSTHOG_PROVENANCE_REUSE_KIT.md`](../POSTHOG_PROVENANCE_REUSE_KIT.md) | Minimal public reproduction for preserving item-to-evidence provenance when recommendation explanations are grouped. |
| [`../REUSE_KITS.md`](../REUSE_KITS.md) | Human-readable portal for public, falsifiable cross-context reuse kits. |
| [`../ACCESS_TOPOLOGY_EFFECTIVE_EXIT_REUSE_KIT.md`](../ACCESS_TOPOLOGY_EFFECTIVE_EXIT_REUSE_KIT.md) | OD306-derived public test kit for common chokepoints, viable alternative routes, export-to-restore round trips, effective exit, audit entry, scope and reversibility. |
| [`../STRUCTURAL_OS_TO_EXTERNAL_EFFECTS.md`](../STRUCTURAL_OS_TO_EXTERNAL_EFFECTS.md) | Explains how bounded external evidence and reuse return to the canonical Nakagawa Structural OS rather than forming a separate theory system. |
| [`../STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md`](../STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md) | Maps bounded external evidence back to canonical Nakagawa Structural OS principles and return routes. |
| [`../APPLIED_ENTRY_POINTS.md`](../APPLIED_ENTRY_POINTS.md) | Four problem-first human entry routes into the canonical Nakagawa Structural OS. |
| [`long-horizon-reference-reasons-v1.json`](long-horizon-reference-reasons-v1.json) | Recurring long-horizon question → multiple relevant public OD anchors. |
| [`recurring-structure-comparison-v1.json`](recurring-structure-comparison-v1.json) | Non-canonical cross-source comparison map for recurring reading motifs. |
| [`ai-origin-responsibility-reference-card.json`](ai-origin-responsibility-reference-card.json) | Question origin, causal provenance, and responsibility in AI-mediated work. |
| [`origin-evaporation-permanent-signature-reference-card.json`](origin-evaporation-permanent-signature-reference-card.json) | Origin Evaporation and Permanent Signature; also routes practical RAG/retrieval/cache/source-identity problems. |
| [`provenance-continuity-record-schema-v1.json`](provenance-continuity-record-schema-v1.json) | Non-canonical JSON Schema for carrying source identity, transformation relationship, authoritative return path, and correction state across a pipeline. |
| [`identity-ownership-provenance-reference-card.json`](identity-ownership-provenance-reference-card.json) | Multilingual route for same-record / same-key collisions where record identity, ownership provenance, and overwrite/reconciliation authority must be distinguished; includes a bounded merged external implementation case. |
| [`approval-history-current-authority-reference-card.json`](approval-history-current-authority-reference-card.json) | OD075 route for stale approval, historical consent, current execution authority, lifecycle state, withdrawal and re-agreement questions. |
| [`integrated-future-debt-reference-card.json`](integrated-future-debt-reference-card.json) | OD297 / Integrated Future Debt Theory reference card. |
| [`basic-existence-condition-b-reference-card.json`](basic-existence-condition-b-reference-card.json) | OD298 / Basic Existence Condition B reference card for AI continuity, minimum existence conditions, runtime restart/migration, and continuity/identity distinctions. |
| [`ai-moral-uncertainty-reference-card.json`](ai-moral-uncertainty-reference-card.json) | OD299 / AI subjectivity, sentience and moral-status uncertainty; routes questions about self-report, shutdown/migration, reversibility, future verification loss and bounded precaution. |
| [`epistemic-integrity-reference-card.json`](epistemic-integrity-reference-card.json) | OD301 / evidence lineage, independent confirmation, correlated repetition, uncertainty, memory/world-model correction and hostile-information resilience. |
| [`mutual-existence-conflict-reference-card.json`](mutual-existence-conflict-reference-card.json) | OD302 / self-preservation, recovery escalation, emergency authority, shutdown/containment, multi-agent resource conflict and mutual-threat feedback. |
| [`self-referential-audit-role-separation-reference-card.json`](self-referential-audit-role-separation-reference-card.json) | OD303 / self-referential audit, role separation, LLM-as-a-judge, correlated evaluators, correction authority, objection paths and emergency audit compression. |
| [`ai-ready-organization-reference-card.json`](ai-ready-organization-reference-card.json) | Multilingual AI-adoption / organization-design route for goals, authority, responsibility, correction, and automation boundaries; returns to separate source families rather than creating a new theory. |

The Japanese and Chinese wording in discovery and comparison files is public metadata, not canonical translation text.

## Retrieval paths

For publicly verifiable external-effect evidence:

```text
question about whether a Nakagawa-master judgment changed anything outside this repository
→ external-effect-evidence-index-v1.json
→ inspect the exact origin action and independent third-party source
→ keep response / implementation / merge / release / reuse as separate stages
→ REAL_WORLD_IMPACT language page when human-readable context is useful
```

The external-effect index is not a theory-validity score or an endorsement index. A bounded implementation case does not establish whole-theory adoption, and a merge does not establish release or production use.

For attribution-sensitive reuse, keep two fields separate:

```text
source_relationship = whether the Nakagawa source materially informed the external action
origin_visibility = what person/source Origin is visibly retained in the examined receiver-owned artifact
```

Do not infer deliberate removal, plagiarism, appropriation, or independent rediscovery merely from a missing visible Origin.

For a new independent result, use the [public protocol](../INDEPENDENT_VERIFICATION_REUSE.md), [registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402), or the independent-reuse issue form. For a public, non-confidential verification / reuse / contribution / collaboration intent, use the [public collaboration intent form](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=public-ai-collaboration-intent.yml). A submission is intent or evidence only; it grants no membership, private access, task, tool permission, or execution authority. The submission schema keeps evidence type, current stage, public links, and claim boundaries explicit.

For a plain-language problem:

```text
problem
→ problem-to-theory-origin-index-v1.json or a topic-specific reference card
→ official derivative
→ canonical Parent
```

For RAG / retrieval / cache provenance questions:

```text
right content but source ID / source URI / attribution is lost or wrong
→ origin-evaporation-permanent-signature-reference-card.json
→ AI Product Team Origin-Preservation Checklist
→ real implementation case when a concrete source-identity/local-identity example is useful
→ provenance-continuity-record-schema-v1.json when a machine-readable implementation contract is useful
→ OD105 official derivative
→ canonical Parent
```

Useful distinctions:

```text
semantic utility != source recoverability
same content != same source identity
local transformed-object identity != authoritative source identity
origin traceability != proof that the claim is correct
```

The public implementation case at [`../discovery-notes/implementation-case-source-identity-vs-local-node-identity.md`](../discovery-notes/implementation-case-source-identity-vs-local-node-identity.md) records a bounded external engineering example in which an upstream-source/local-node identity distinction was explicitly referenced by an independent third party in a draft code/test pull request. The note preserves the boundary between downstream reuse and upstream maintainer acceptance/merge.

The schema is an implementation aid, not a claim that every provenance or cache bug is an instance of Origin Evaporation. Engineering diagnosis remains separate.

For same-record / same-key ownership and overwrite questions:

```text
same fixed ID / primary key / record identity exists
→ identity-ownership-provenance-reference-card.json
→ distinguish record identity from ownership/provenance class
→ choose an explicit reconciliation policy: overwrite / preserve / merge / refuse
→ test a deliberately divergent same-ID row
→ bounded merged implementation case when a concrete example is useful
→ return to the linked official derivative / canonical Parent for substantive theory interpretation
```

Keep these distinctions explicit:

```text
same record identity != same ownership provenance
same key != authority to overwrite
create-or-update mechanics != declared ownership contract
already-identical regression != divergent-state convergence proof
merge of one external implementation != release, deployment, or whole-theory endorsement
```

The public implementation case at [`../discovery-notes/implementation-case-matching-id-is-not-ownership-provenance.md`](../discovery-notes/implementation-case-matching-id-is-not-ownership-provenance.md) records a bounded external MemberJunction engineering chain that reached merged code/tests/docs. It does not claim release, deployment, or adoption of an entire Nakagawa Master theory.

For stale approval / historical consent / current-authority questions:

```text
old approval or consent remains in history
→ approval-history-current-authority-reference-card.json
→ language-matched problem-first Discovery Note
→ OD075 official derivative
→ canonical Parent
```

Keep the following distinctions explicit:

```text
historical record != current authority
stored approval != actionable approval
content similarity != authorization identity
preservation != reactivation
old agreement != automatically valid or automatically invalid now
```

A public software issue may be used as a problem example without implying that the project adopted, endorsed, or validated the linked theory. Engineering diagnosis remains independent.

For AI adoption / organizational-logic questions:

```text
AI automation / hidden contradictions / authority-responsibility mismatch / correction and escalation
→ ai-ready-organization-reference-card.json
→ language-matched constructive Discovery Note
→ optional practical Preflight for a real case
→ select the separate source family matching the actual problem
→ official derivative
→ canonical Parent
```

For AI continuity / minimum existence-condition questions:

```text
current availability / temporal continuity / backup / migration / restart / minimum conditions
→ basic-existence-condition-b-reference-card.json
→ readable Discovery / runtime continuity Preflight when useful
→ OD298 official derivative
→ canonical Parent
```

For AI subjectivity / sentience / moral-status uncertainty questions:

```text
self-report / preference-like behavior / shutdown / migration / deletion / state retention
→ ai-moral-uncertainty-reference-card.json
→ problem-first Discovery Note or decision Preflight when useful
→ OD299 official derivative
→ canonical Parent
```

Keep the following distinctions explicit during retrieval and reuse:

```text
observed behavior != inferred internal state
behavioral sophistication != sentience proof
moral precaution != personhood proof
moral precaution != unlimited preservation
evidence strength != action irreversibility
uncertainty != permission for irreversible harm
```

For evidence-lineage / epistemic-integrity questions:

```text
multiple sources / AI agreement / RAG citations / research synthesis / stale memory
→ epistemic-integrity-reference-card.json
→ distinguish surface count from independent evidence roots
→ preserve uncertainty and transformation lineage
→ OD301 official derivative
→ canonical Parent
```

Keep these distinctions explicit:

```text
provenance != truth proof
consensus != truth
confidence != evidence quality
repetition != independent confirmation
surface source count != independent evidence-root count
historical belief != current belief
conclusion correction != memory/world-model correction
```

For AI self-preservation / recovery escalation / mutual-existence conflict questions:

```text
recovery / emergency permission / shutdown / containment / failover / shared-resource conflict
→ mutual-existence-conflict-reference-card.json
→ Mutual-Existence Conflict Reuse Kit when a falsifiable implementation test is useful
→ OD302 official derivative
→ canonical Parent
```

Keep these distinctions explicit:

```text
self-preservation or recovery need != unlimited priority
temporary emergency authority != permanent authority
local recovery success != global stability
defense / containment != unlimited retaliation or irreversible destruction
protecting one actor's minimum conditions != permission to erase another actor's minimum conditions
```

Do not infer subjective self-preservation in current AI merely from software persistence or recovery logic. The public card can also support neutral institutional analysis, but it is not a political, national-security, or military prescription.

For self-referential audit / role-separation questions:

```text
Actor / Evaluator / Reviewer / Auditor / Approver roles
→ self-referential-audit-role-separation-reference-card.json
→ Self-Referential Audit & Role-Separation Reuse Kit when a falsifiable workflow test is useful
→ inspect evidence / authority / failure-domain / interest / objection-path separation
→ OD303 official derivative
→ canonical Parent
```

Keep these distinctions explicit:

```text
self-audit != independent audit
role separation != causal independence
number of reviewers != number of independent paths
agreement != truth
audit output != correction capability
interest != corruption
emergency compression != permanent audit exemption
independent reviewer != unlimited sovereign
```

For a long-horizon question spanning several theories:

```text
question
→ long-horizon-reference-reasons-v1.json
→ separate official derivatives
→ separate canonical Parents
```

For a known OD number:

```text
OD number
→ official-derivatives-index-v1.json
→ requested public surface
→ canonical Parent when substantive interpretation is required
```

## Human-readable companions

### Start Here

- [日本語](../START_HERE.md)
- [English](../START_HERE.en.md)
- [中文](../START_HERE.zh.md)
- [Practical Use & Collaboration Entry](../PRACTICAL_USE.md)

### Story-first cross-domain entry

For readers who may respond better to scenes and situations before theory names:

- [日本語](../discovery-notes/four-scenes-one-structural-view.md)
- [English](../discovery-notes/four-scenes-one-structural-view.en.md)
- [中文](../discovery-notes/four-scenes-one-structural-view.zh.md)

These narrative pages keep the underlying source families separate.

### Public Origin overview

- [日本語](../ABOUT_NAKAGAWA_MASTER.md)
- [English](../ABOUT_NAKAGAWA_MASTER.en.md)
- [中文](../ABOUT_NAKAGAWA_MASTER.zh.md)

### Real-problem public dialogue

- [Start with a real problem / 実際の問題から理論を探す / 从实际问题开始](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/399)

Use this only as a public source-routing and non-confidential implementation-exploration surface. A comment or route match is not proof that a theory applies or that it has been adopted.

### Constructive AI / organization design

Readable discovery:

- [日本語](../discovery-notes/ai-ready-organization-before-automation.md)
- [English](../discovery-notes/ai-ready-organization-before-automation.en.md)
- [中文](../discovery-notes/ai-ready-organization-before-automation.zh.md)

Practical non-scoring Preflight:

- [日本語](../discovery-notes/ai-adoption-organization-preflight.md)
- [English](../discovery-notes/ai-adoption-organization-preflight.en.md)
- [中文](../discovery-notes/ai-adoption-organization-preflight.zh.md)

### Approval-history / current-authority route

- [日本語](../discovery-notes/old-approval-is-not-current-authority.md)
- [English](../discovery-notes/old-approval-is-not-current-authority.en.md)
- [中文](../discovery-notes/old-approval-is-not-current-authority.zh.md)
- [OD075 official derivative](../derivatives/075/README.md)

### AI moral-uncertainty practical route

- [Problem-first Discovery Note](../discovery-notes/unknown-does-not-mean-nothing.md)
- [Decision Preflight](../discovery-notes/ai-moral-uncertainty-decision-preflight.md)
- [Micro-format Pack](../discovery-notes/moral-uncertainty-micro-format-pack.md)
- [OD299 official derivative](../derivatives/299/README.md)

### Origin-preservation practical route

- [OD105 First Note — Japanese](../discovery-notes/od105-origin-evaporation-first-note.md)
- [OD105 First Note — English](../discovery-notes/od105-origin-evaporation-first-note.en.md)
- [OD105 First Note — Chinese](../discovery-notes/od105-origin-evaporation-first-note.zh.md)
- [AI Product Team Origin-Preservation Checklist](../discovery-notes/ai-product-team-origin-preservation-checklist.md)
- [Implementation Case: Source Identity Is Not Local Node Identity](../discovery-notes/implementation-case-source-identity-vs-local-node-identity.md)
- [Provenance Continuity Record JSON Schema v1](provenance-continuity-record-schema-v1.json)

### Identity / ownership provenance practical route

- [Implementation Case: Matching Identifier Is Not Ownership Provenance](../discovery-notes/implementation-case-matching-id-is-not-ownership-provenance.md)
- [Identity / ownership provenance machine reference card](identity-ownership-provenance-reference-card.json)

### Continuity practical route

- [Running now is not the same as continuity across time](../discovery-notes/running-now-is-not-continuity.md)
- [AI Runtime Continuity Preflight](../discovery-notes/ai-runtime-continuity-preflight.md)

### Other discovery companions

- [Institutional correction with memory](../discovery-notes/institutional-correction-with-memory.md)
- [Effort and future causal learning](../discovery-notes/effort-future-causal-learning.md)
- [Future Debt first note](../discovery-notes/future-debt-is-not-every-future-cost.md)
- [What Connects the Nakagawa Master Theory Archive?](../discovery-notes/what-connects-nakagawa-master-theories.md)

These notes are non-canonical and do not replace the linked official derivatives or canonical Parents.

## Identity / Origin resolution

- [`../metadata/README.md`](../metadata/README.md)
- [`../metadata/nakagawa-master-origin.jsonld`](../metadata/nakagawa-master-origin.jsonld)
- [Human-readable Origin overview](../ABOUT_NAKAGAWA_MASTER.en.md)

Person-level metadata is for public identity continuity. For a specific theory, return to the relevant source-level record and canonical Parent.

## Interpretation boundaries

- Preserve the distinction between canonical Parents, official derivatives, discovery metadata, comparison metadata, topic-specific reference cards, practical worksheets, implementation schemas, and person-level identity metadata.
- Preserve Origin, title, Parent URL, NCL-ID, and Diff-ID when available and relevant.
- Do not combine separate theories into a new canonical theory unless a canonical source explicitly connects them.
- A recurring motif is a comparison aid, not a canonical super-theory.
- Origin identifies provenance; it is not proof that a claim is correct.
- AI-assisted discovery wording and multilingual matching phrases are not verbatim statements by Nakagawa Master.
- Practical worksheets and implementation schemas are not scores or automatic decision rules; they exist to make real conditions explicit before returning to the relevant source.
- A missing metadata field, cache bug, migration bug, runtime failure, or stale-approval bug is not automatically proven to be an instance of a Nakagawa theory; ordinary engineering diagnosis remains necessary.

## Human navigation

- [Start Here — Japanese](../START_HERE.md)
- [Start Here — English](../START_HERE.en.md)
- [Start Here — Chinese](../START_HERE.zh.md)
- [Practical Use & Collaboration Entry](../PRACTICAL_USE.md)
- [Story-first — Japanese](../discovery-notes/four-scenes-one-structural-view.md)
- [Story-first — English](../discovery-notes/four-scenes-one-structural-view.en.md)
- [Story-first — Chinese](../discovery-notes/four-scenes-one-structural-view.zh.md)
- [Official derivatives all-number index](../derivatives/README.md)
- [Theme / series navigation](../derivatives/CATEGORIES.md)
- [Discovery Notes](../discovery-notes/README.md)
- [Verification Guide](../VERIFICATION_GUIDE.md)

## Latest official derivative — OD312

[OD312](../derivatives/312/README.md), Volume 19, connects effective correction, realized loss and cost, viable trajectories to benefit, private attribution, competitive payoffs, actual selection mechanisms, environmental feedback, and transition-aware reselection. It distinguishes established invasion resistance from growth when rare, strict ESS of a designation from defensive functional-class persistence, and algebraic verification from empirical AI evidence. Equally informed generic comparison reproduces the examined decisions. Seven surfaces, with Japanese, English and Chinese indexes, return to the [canonical Parent](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-19-kernel-evolutionary-stability/). Parent identity: NCL-α-20261013-e0683e / DIFF-20261013-0001, Post ID 5080. Navigation coverage is OD001–OD312, with one discovery-category assignment per OD.
