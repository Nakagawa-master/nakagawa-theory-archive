# Publicly Verifiable External Implementation Cases | Changes Recorded After Nakagawa Master Comments

Language: [日本語](REAL_WORLD_IMPACT.md) | **English** | [中文](REAL_WORLD_IMPACT.zh.md)

**Nakagawa Master's specific findings led other developers to change code, write tests, and merge fixes.** The original review discussions, receiving developers' commits, tests and release records are all linked for direct inspection.

**75 publicly documented, source-linked cases** include independent developers' code changes, tests, merges, release documentation, and bounded deployments across unrelated projects. The collection includes cases at different stages, including ongoing work and declined proposals, with their recorded states. The code authors remain the receiving developers.

You can also explore [Nakagawa Master's own GitHub activity](https://github.com/Nakagawa-master) and [the author's original theory archive](https://master.ricette.jp/) separately from these independently verifiable implementation records.

**Beyond a merge, into independently edited public media:** [The Daily AI Pulse editor @GadDev independently prepared and merged the English and reviewed French story](https://github.com/GadDev/daily-ai-pulse/pull/253) after Nakagawa Master originally submitted the subject. Its [English article](https://daily-ai-pulse-db253.web.app/stories/2026-10-26-qwen-review-integrity/) and [French translation](https://daily-ai-pulse-db253.web.app/fr/stories/2026-10-26-qwen-review-integrity/) name the original Qwen reporter and separately cite [Nakagawa Master's proposed source-integrity controls](https://github.com/QwenLM/qwen-code/issues/15507#issuecomment-6394240323). The [recipient-owned October 26, 2026 deployment run](https://github.com/GadDev/daily-ai-pulse/actions/runs/40332697382) succeeded on the exact editor merge commit `e275f243`, generated both HTML pages, deployed to Firebase and passed the live-hosting endpoint verification step. This demonstrates **outside editorial selection, multilingual production and recorded public deployment**, not spontaneous editorial discovery: Nakagawa Master made the initial submission. The article did not reproduce the disputed production behavior, and actual unique readers, independent secondary retellings, model adoption and mass person recognition are **not known**. This media PR is not an extra independent software-fix PR in the 14/8 merged-code evidence set.

## Proof first: independent developers changed and merged code

- **OpenClaw | An unrelated agent's configuration edit invalidated another person's pending approval.** Nakagawa Master [reported the exact remaining problem and a regression case](https://github.com/openclaw/openclaw/pull/160136#issuecomment-5863857114). The maintainer **explicitly cited that report**, [implemented and merged the separate fix](https://github.com/openclaw/openclaw/pull/160856), and [official release documentation named `@Nakagawa-master`](https://github.com/openclaw/openclaw/blob/main/docs/releases/2026.9.7.md). See case 51.
- **MemberJunction | Matching an ID is not authorization to overwrite a record.** The receiving team implemented the distinction and published [v6.1.2](https://github.com/MemberJunction/MJ/releases/tag/v6.1.2). See case 3.
- **PostHog | Numbers asserted by a producer are not the same as measurements made by the product.** The receiving team split the work into [three merged successor PRs](https://github.com/PostHog/posthog/pull/107795) with recorded dev / US / EU production deployments. See case 1 for the current feature-flag and receiving deployment details.
- **[Qwen Code | A permission parser both rejected read-only commands and could miss a protected write destination](https://github.com/QwenLM/qwen-code/pull/15681).** Beyond the original `2>&1` false denial, [Nakagawa Master pointed out](https://github.com/QwenLM/qwen-code/issues/15600#issuecomment-6412304134) that `>&protected.txt` writes `protected.txt`, while the old parser checked `&protected.txt`, so a path-specific deny could miss it. [The original reporter independently tested the actual permission decision, changing `allow` to `deny`](https://github.com/QwenLM/qwen-code/issues/15600#issuecomment-6413173175), wrote the fix and regression tests, and [PR #15681 merged on November 1, 2026](https://github.com/QwenLM/qwen-code/pull/15681). The [stable v0.26.6 release tag](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.6) is a descendant of #15681's merge commit (released November 2); a new installed-user permission retest remains unverified.
- **[Qwen Code | A prepared AI warning was falsely counted as delivered](https://github.com/QwenLM/qwen-code/pull/15559).** Nakagawa Master identified the missing send boundary; the [engineer acknowledged and fixed it with tests](https://github.com/QwenLM/qwen-code/pull/15559#discussion_r4374913110), and [PR #15559 merged on November 1](https://github.com/QwenLM/qwen-code/commit/ae7901552e1907203e658e661499f0bfc1937f7f) and is included in the [published stable v0.26.6 source tag](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.6). See case 54.
- **[Qwen Code | Rejected private chat text appeared in a diagnostic path](https://github.com/QwenLM/qwen-code/pull/15634).** Following [Nakagawa Master's finding](https://github.com/QwenLM/qwen-code/pull/15634#discussion_r4423012915), the [developer changed the code and added canary-based privacy tests](https://github.com/QwenLM/qwen-code/pull/15634#discussion_r4423074659). This PR is still open. See case 55.
- **Qwen Code | A previously recorded stop is not proof that this particular AI call stopped.** Receiving developer `wenshao` implemented and [merged the correction on October 12](https://github.com/QwenLM/qwen-code/pull/13923). See case 47.
- **PydanticAI | Skipping a duplicate AI history request can still leave unwanted writes.** The developer [reproduced and fixed the issue](https://github.com/pydantic/pydantic-ai/pull/9982#issuecomment-6063881879); [the fix merged](https://github.com/pydantic/pydantic-ai/pull/9982). See case 41.

**Demonstrated capability:** Spot a false equivalence inside different systems, make it testable, and help independent implementers change their own software. The code authors are the receiving developers.

Nakagawa Master is the pen name of Keisuke Nakagawa. On social media, the name “マスター” (“Master”) is also used; some external posts use “MasterJP.”

This page is a **public verification guide**. It links public GitHub comments or reviews made under the `Nakagawa-master` account to later changes that can be checked in third-party repositories.

Each case traces:

1. the original public contribution;
2. the third party's response or change;
3. the current repository state;
4. the receiving project's recorded state and next public result.

Follow the full course of each contribution: initial question, independent engineering decision, code and tests, integration, release and observed use.

## When an AI says a file is protected, is it actually protected?

A coding agent may say it has blocked writes to a particular file. But its decision is only as reliable as its understanding of the **real destination the shell opens**.

While examining a [Qwen Code issue](https://github.com/QwenLM/qwen-code/issues/15600), Nakagawa Master identified the opposite side of an existing false-denial bug: a protected-file write could be mistaken for a write to another filename. The original reporter [verified the incorrect and corrected authorization decisions](https://github.com/QwenLM/qwen-code/issues/15600#issuecomment-6413173175), wrote the patch and regression tests, and [the fix was merged](https://github.com/QwenLM/qwen-code/pull/15681).

The [practical Japanese/English guide](human-translation/field-guides/ai-agent-shell-permission-real-write-destination.md) turns this finding into **seven checks that other developers can use** to compare what the shell actually does with what the agent permits or denies. It also connects the reasoning to Nakagawa Master's published works on [Establishment Conditions](https://master.ricette.jp/theory/nakagawa-master-why-establishment-conditions-theory-is-necessary/) and the [Connection Protocol](https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-protocol/).

## What these distinctions can mean in practice

The cases below concern product behaviors such as:

- separating an AI-produced number from a system's own measurement;
- separating historical approval from current authorization;
- separating matching identity from authority to overwrite;
- preserving upstream source identity separately from local runtime identity;
- separating successful execution from a semantically valid measurement;
- preserving which evidence source supports which recommendation;
- separating present membership from historical participation;
- separating one approval action from one external side effect.

Only the publicly verifiable part of each case is described below.

## 1. PostHog | Separate producer-supplied evidence from PostHog's own measurement

**Origin surface:** the Nakagawa-master review on [PostHog/posthog#92252](https://github.com/PostHog/posthog/pull/92252)  
**Current state:** **All three receiving-developer successor PRs merged into PostHog master on October 2, 2026**, with deployment records for dev, prod-us and prod-eu. The original [#92252](https://github.com/PostHog/posthog/pull/92252) was **closed unmerged on September 28 because its author explicitly replaced it** with a split implementation: outcome measurement [#107879](https://github.com/PostHog/posthog/pull/107879), measured evidence [#107795](https://github.com/PostHog/posthog/pull/107795), and suggestion/action behavior [#107802](https://github.com/PostHog/posthog/pull/107802). **Limit:** rollout/feature controls remain, so customer availability or actual user adoption is not established.

A Nakagawa-master review identified that producer-authored evidence should not be presented as if it had been independently measured by PostHog.

- [Nakagawa-master evidence review](https://github.com/PostHog/posthog/pull/92252#pullrequestreview-5233849200)
- [Author explanation replacing the original PR with successors](https://github.com/PostHog/posthog/pull/92252#issuecomment-5872695227)
- [Current measurement successor #107795](https://github.com/PostHog/posthog/pull/107795)
- [Current suggestion/action successor #107802](https://github.com/PostHog/posthog/pull/107802)

The original author explicitly states that #92252 was replaced by #107802 and that outcome measurement and evidence surfaces moved into #107795. The current implementation therefore has to be checked on the successor stack rather than the closed original head.

Current PR #107795 implements the measurement boundary by:

- re-reading the relevant workflow / version / step metrics on the PostHog side when a suggestion is filed;
- keeping the producer's claimed numbers separate from PostHog's reading;
- labeling established server-side readings **Measured by PostHog** and producer values that PostHog cannot establish **Unverified**;
- refusing to treat producer-supplied measured state as PostHog's own measurement;
- surfacing disagreement between the producer headline/denominator and PostHog's reading;
- fixing the metric-selection path so a click suggestion is not silently measured against opens.

The PR description records a real-browser/local-stack check in which deliberately fake producer measurement did not survive as server-attested evidence; the stored evidence carried PostHog's own reading instead.

A separate review also identified the capability boundary **narrow capability != user-grantable capability**:

- [Nakagawa-master capability-boundary review](https://github.com/PostHog/posthog/pull/92252#pullrequestreview-5245587245)

That suggestion/action layer now continues in successor #107802. Its current scout contract still separates suggestion creation from human approval and later publication. The source links distinguish Nakagawa Master's review contribution from the receiving developers' independently authored successor work.

PRs #107879, #107795, and #107802 merged as one stack on 2026-10-02. PostHog's deployment bot records the same deployment workflow reaching dev at 22:42 UTC, prod-us at 22:57, and prod-eu at 23:12. The successor PR bodies preserve the #92252 stack lineage, but they do not explicitly re-name `Nakagawa-master`.

**Publicly verifiable here:** origin review → receiver-owned successor stack → server-side measurement, Measured by PostHog / Unverified, producer-measurement distrust, internal scout-only proposal capability, per-version outcome reading → tests/browser verification → merge → dev/prod-us/prod-eu deployment.  

---

## 2. Dream | Separate sanitized content from current authorization

**Surface:** [tushardhara/dream#12](https://github.com/tushardhara/dream/issues/12) → [PR #28](https://github.com/tushardhara/dream/pull/28)  
**Current state:** PR #28 merged

The public contribution proposed that content which was once sanitized or approved should not automatically remain authorized after actor, recipient, purpose, source lineage, or policy conditions change.

- [Nakagawa-master design contribution](https://github.com/tushardhara/dream/issues/12#issuecomment-5651995689)
- [repository-owner response](https://github.com/tushardhara/dream/issues/12#issuecomment-5652003584)
- [merged PR #28](https://github.com/tushardhara/dream/pull/28)
- [public case note](discovery-notes/implementation-case-sanitized-content-is-not-current-authorization.md)

The repository owner explicitly accepted the distinction and the later PR added rights/lineage revalidation, revocation-related handling, and negative tests.

**Publicly verifiable here:** comment → owner response → code / tests → merge.  

---

## 3. MemberJunction | Separate matching identity from authority to overwrite

**Surface:** [MemberJunction/MJ#4519](https://github.com/MemberJunction/MJ/pull/4519) → [#4496](https://github.com/MemberJunction/MJ/pull/4496) → [#4546](https://github.com/MemberJunction/MJ/pull/4546) → [v6.1.2](https://github.com/MemberJunction/MJ/releases/tag/v6.1.2)  
**Current state:** merged → LTS backport merged → v6.1.2 released

A matching primary key does not by itself establish that a migration owns the existing row or may overwrite it.

- [Nakagawa-master contribution](https://github.com/MemberJunction/MJ/pull/4519#issuecomment-5689128135)
- [PR #4519](https://github.com/MemberJunction/MJ/pull/4519)
- [public case note](discovery-notes/implementation-case-matching-id-is-not-ownership-provenance.md)

Public records show later independent review, author code/test/documentation changes, merge, generated migration, LTS backport, and inclusion in v6.1.2.

A public certification report also records an upgrade of an existing database containing pre-existing rows in which the relevant migration sequence completed without the original primary-key collision.

- [External 6.1.2 certification report](https://github.com/MemberJunction/MJ/issues/4475#issuecomment-5715684968)

That same report identifies a separate regression, so this page does **not** claim that v6.1.2 was problem-free overall.

**Publicly verifiable here:** review → independent confirmation → code/tests/docs → merge → backport → release → external upgrade report for the relevant collision condition.  

---

## 4. LlamaIndex | Preserve upstream source identity separately from local node identity

**Surface:** [run-llama/llama_index#21933](https://github.com/run-llama/llama_index/issues/21933) → [PR #23038](https://github.com/run-llama/llama_index/pull/23038)  
**Current state:** open / draft / unmerged

The issue contribution distinguished framework-local node identity from upstream document identity.

- [Nakagawa-master comment](https://github.com/run-llama/llama_index/issues/21933#issuecomment-5650957902)
- [third-party PR #23038](https://github.com/run-llama/llama_index/pull/23038)
- [public case note](discovery-notes/implementation-case-source-identity-vs-local-node-identity.md)

The third-party PR explicitly cites the `Nakagawa-master` compatibility contract and adds implementation/tests that preserve `document_id` and `document_name` in metadata without changing the local `TextNode.id_` policy.

**Publicly verifiable here:** explicit source reference plus third-party code/tests.  

---

## 5. MemberJunction | Another reviewer independently checked the same issue

**Surfaces:** [MemberJunction/MJ#4487](https://github.com/MemberJunction/MJ/pull/4487) / [#4524](https://github.com/MemberJunction/MJ/pull/4524)  
**Current state:** #4487 merged on 2026-09-24 / #4524 closed unmerged on 2026-09-21

On #4487, a `Nakagawa-master` review identified an aliased re-export compatibility hole.

- [Nakagawa-master review](https://github.com/MemberJunction/MJ/pull/4487#pullrequestreview-5219601735)

Another reviewer, `rkihm-BC`, later reproduced and described the issue in a formal review and requested the corresponding fix and regression test.

- [independent reviewer confirmation](https://github.com/MemberJunction/MJ/pull/4487#pullrequestreview-5241419422)

On #4524, the same reviewer explicitly wrote that “@Nakagawa-master's point about D is confirmed” and incorporated the result of their own checker run into the review.

- [confirmation on #4524](https://github.com/MemberJunction/MJ/pull/4524#pullrequestreview-5242805347)

The authors later implemented the relevant fixes. On #4487, named re-exports now retain both the exported alias and the source declaration name, with regressions showing that an aliased published data-shape member remains `warn` while an unre-exported sibling remains `error`. Nakagawa-master re-checked the current head and explicitly closed the original finding in review `5252973190`. On #4524, the direct `[__mj]` fail-open case was fixed, and the same independent reviewer re-ran the probe and verified the transition from false-pass exit 0 to fail-closed exit 1.

- [#4487 closure review](https://github.com/MemberJunction/MJ/pull/4487#pullrequestreview-5252973190)
- [#4524 independent re-verification](https://github.com/MemberJunction/MJ/pull/4524#pullrequestreview-5252195432)

**Publicly verifiable here:** named independent confirmation followed by author implementation/regressions, origin-reviewer closure on #4487, and independent execution re-verification on #4524.  

---

## 6. PostHog | Keep recommendation reasons tied to their actual source

**Surface:** [PostHog/posthog#102550](https://github.com/PostHog/posthog/pull/102550) → [#102686](https://github.com/PostHog/posthog/pull/102686)  
**Current state:** #102550 merged / deployed; #102686 merged / deployed

A `Nakagawa-master` review identified that identical explanation text should not collapse distinct recommendation sources such as `Code history` and `Added by scout`.

- [Nakagawa-master review](https://github.com/PostHog/posthog/pull/102550#pullrequestreview-5242012853)

The maintainer changed grouping logic, tests, and UI stories; #102550 merged to `master`. PostHog's public deploy-status comment records deployment to dev, prod-us, and prod-eu.

- [merged PR #102550](https://github.com/PostHog/posthog/pull/102550)
- [deploy status](https://github.com/PostHog/posthog/pull/102550#issuecomment-5722917557)

The same maintainer later used the same source-category distinction on #102686. Its current head received an APPROVED review from the separate `stamphog` reviewer, merged at 2026-09-18T15:49:22Z, and PostHog's deploy-status record shows deployment to dev, prod-us, and prod-eu.

- [#102686 external approval](https://github.com/PostHog/posthog/pull/102686#pullrequestreview-5249196997)
- [merged PR #102686](https://github.com/PostHog/posthog/pull/102686)
- [#102686 deploy status](https://github.com/PostHog/posthog/pull/102686#issuecomment-5732760371)

**Publicly verifiable here:** the initial review → code/tests/UI change → merge → deployment, followed by reuse of the same distinction on another PR → separate approval → merge → dev/prod-us/prod-eu deployment.  

---

## 7. TourCRM | Separate present membership from historical participation

**Surface:** [Alan8893/tourcrm#97](https://github.com/Alan8893/tourcrm/pull/97) → [PR #101](https://github.com/Alan8893/tourcrm/pull/101)  
**Current state:** follow-up PR #101 merged

The review identified that historical attendance should be evaluated against the occurrence's own participation window rather than only current membership.

- [Nakagawa-master review](https://github.com/Alan8893/tourcrm/pull/97#issuecomment-5689122153)
- [owner response](https://github.com/Alan8893/tourcrm/pull/97#issuecomment-5691823125)
- [follow-up PR #101](https://github.com/Alan8893/tourcrm/pull/101)

The owner described the issue as a real bug, opened a dedicated follow-up, changed code/tests, and later hardened the regression fixture after another review so the old implementation would actually fail.

**Publicly verifiable here:** review → owner confirmation → follow-up PR → code/tests → further test hardening → merge.  

---

## 8. Clientverse | Separate one approval from one external side effect

**Surface:** [ebyron357/Clientverse-crm#27](https://github.com/ebyron357/Clientverse-crm/pull/27)  
**Current state:** merged

If a provider accepts a message but the response is lost, treating the result as an ordinary failure can allow an accidental duplicate send.

- [Nakagawa-master review](https://github.com/ebyron357/Clientverse-crm/pull/27#issuecomment-5690360136)
- [owner response](https://github.com/ebyron357/Clientverse-crm/pull/27#issuecomment-5690677339)
- [merged PR #27](https://github.com/ebyron357/Clientverse-crm/pull/27)

The repository owner described this as a real state-machine defect and added an `outcome_unknown` state, reconciliation, dispatch idempotency, and regression coverage for response loss.

**Publicly verifiable here:** review → defect confirmation → state-machine/provider-contract/test changes → merge.  

---

## 9. Replay | Separate historical consent records from current eligibility

**Surface:** [aferna6-cell/Replay#67](https://github.com/aferna6-cell/Replay/issues/67)  
**Current state:** design direction accepted in the issue; repository code implementation not verified

The public contribution proposed keeping the historical consent event while separately evaluating whether the material is currently eligible for retention, processing, or use.

- [Nakagawa-master contribution](https://github.com/aferna6-cell/Replay/issues/67#issuecomment-5689647722)
- [repository-owner response](https://github.com/aferna6-cell/Replay/issues/67#issuecomment-5689719035)

The repository owner explicitly identified the source and restated the distinction as part of the project's protocol design.

**Publicly verifiable here:** comment → owner acknowledgment and protocol-level adoption.  

---

## 10. Cline | Make delegated child capabilities visible at approval time

**Surface:** [cline/cline#14225](https://github.com/cline/cline/pull/14225)  
**Current state:** base PR merged; follow-up implementation of this proposal not verified

A `Nakagawa-master` review proposed that a person approving delegation should be able to see the effective capability set that will be available to the child agent.

- [Nakagawa-master review](https://github.com/cline/cline/pull/14225#pullrequestreview-5242232355)
- [external-author response](https://github.com/cline/cline/pull/14225#issuecomment-5723653394)

The external author named `@Nakagawa-master`, described the proposal as better UX than the current behavior, and stated an intention to include it in future agent-config work.

The base PR is merged; the separate proposal's follow-up remains the receiving project's next implementation step.

**Publicly verifiable here:** named review plus explicit author acknowledgment and follow-up intent.  

---


## 11. Local Operator | Prevent a running agent from weakening its own approval gate

**Surface:** [damianvtran/local-operator#1282](https://github.com/damianvtran/local-operator/issues/1282) → [PR #1291](https://github.com/damianvtran/local-operator/pull/1291) → [release v0.59.10](https://github.com/damianvtran/local-operator/releases/tag/v0.59.10)  
**Current state:** PR #1291 merged / v0.59.10 released and published on 2026-09-19

Issue #1282 described a boundary where a running agent constrained by an approval policy must not be able to lower that same gate from `ask` to `auto` through a configuration path it can write, while explicit human/operator control still needs to remain available.

- [issue #1282](https://github.com/damianvtran/local-operator/issues/1282)
- [third-party PR #1291](https://github.com/damianvtran/local-operator/pull/1291)

The third-party PR explicitly states `Closes #1282` and makes the source of a live approval-policy transition part of the decision. Raw config writes from another process cannot loosen the running gate, while an explicitly attributed operator action in the process that owns the gate still has a positive-control path. The PR also includes a real second-process regression and tests intended to prevent agent-facing code from manufacturing the trusted settings-write path.

Nakagawa-master re-checked the current head against the original issue boundary and explicitly recorded that the original security finding is implemented.

- [closure review](https://github.com/damianvtran/local-operator/pull/1291#pullrequestreview-5253448083)

PR #1291 was then merged and included in public release `v0.59.10`. The release notes explicitly list #1291 and summarize the change as **“An agent can no longer weaken the approval gate.”** The repository owner also recorded successful publication, PyPI availability for `0.59.10`, installation, and an out-of-repository `lop --version` smoke check.

- [release v0.59.10](https://github.com/damianvtran/local-operator/releases/tag/v0.59.10)
- [release / publication / installed-smoke record](https://github.com/damianvtran/local-operator/pull/1291#issuecomment-5745312290)

**Publicly verifiable here:** issue → dedicated third-party PR explicitly closing that issue → code/tests → multiple review/remediation rounds → origin-side closure review → merge (`b1fc1f42`) → release-note inclusion → package publication → installed smoke.  

---


### Follow-up: the same authority boundary advanced into a separate control-plane implementation

After #1291 closed the config-file path, `Nakagawa-master` separated the remaining control-plane boundary into [issue #1310](https://github.com/damianvtran/local-operator/issues/1310): a model-authored subprocess running under the same OS uid must not be able to use a control credential readable under that uid to change its own gate from `ask → auto` or approve its own parked request.

The repository owner independently reproduced the issue and publicly recorded **“confirmed, real, and being fixed”** and **“it named the right boundary.”** That reproduction also corrected the original diagnosis: the reachable sink was `slash_result`, not the initially named `slash`, and the owner independently found the stronger sibling path `approval_answer(approved=True)`.

- [owner reproduction / determination](https://github.com/damianvtran/local-operator/issues/1310#issuecomment-5740547291)
- [third-party implementation PR #1324](https://github.com/damianvtran/local-operator/pull/1324)

PR #1324 implements a per-session operator capability, connection-bound proofs, a common pre-dispatch guard, and explicit negative, positive, and tightening controls. It went through multiple independent review, QA, design, and UX remediation rounds. Nakagawa-master re-checked the five acceptance conditions from the origin issue and recorded origin-side closure of the original #1310 boundary. PR #1324 then merged on 2026-09-21 (merge commit `dca24232392e`).

- [origin-side closure review](https://github.com/damianvtran/local-operator/pull/1324#pullrequestreview-5257968951)

Later the same day, release [v0.61.11](https://github.com/damianvtran/local-operator/releases/tag/v0.61.11) explicitly included #1324. Its release notes describe the change as preventing a running session from widening its own approval gate through the control plane, and record the review / QA / design / UX rounds plus green CI on the merged head.

**Publicly verifiable in this follow-up:** origin issue → independent third-party reproduction → correction of the origin diagnosis → independent discovery of a stronger sibling bypass → third-party implementation → multiple independent remediation rounds → origin-side closure → merge → release-note inclusion.  
**Not established yet:** user-scale use of v0.61.11, a guarantee on host configurations where the OS itself cannot isolate same-uid memory, completion of device-bound phone authority, or independent reuse of this boundary in another project.


### Cross-receiver follow-through: AI-News updated its reader-facing article and editorial tooling

On 2026-09-27, `Nakagawa-master` pointed out on AI-News draft PR #111 that its previously published `agent-self-authorization-approval-gate-2026` article still described #1310 / #1324 as unresolved even though the control-plane path had since merged and shipped in v0.61.11.

- [Nakagawa-master follow-up on AI-News #111](https://github.com/022740mix-spec/AI-News/pull/111#issuecomment-5853890886)
- [AI-News receiver response](https://github.com/022740mix-spec/AI-News/pull/111#issuecomment-5854722227)
- [AI-News PR #135](https://github.com/022740mix-spec/AI-News/pull/135)

AI-News independently re-checked the local-operator Git history, issue state, and release notes. PR #135 then updated the article body, table, excerpt, and primary-source status labels, and added v0.61.11 as a source. It also extended the editorial script `update-article.mjs` with `updatePrimarySources`, so source descriptions can be updated when an external PR/issue changes state instead of leaving the article body and source list inconsistent. PR #135 merged on 2026-09-27 (merge commit `2625b150eb2aa761ab47c475ef76ce33ddfbd3ac`).

The article kept its original distinctions — reversibility is not the same as safety, and authentication / capability / authority / human approval are separate layers — while bringing the factual state of both Local Operator paths up to date.

**Publicly verifiable here:** Nakagawa-master state-update follow-up → receiver-side primary-record re-check → reader-facing body/table/excerpt/source updates → editorial update-tool change → merge.  
The AI-News PR records Claude Code-assisted drafting and the receiving publication's editorial decisions. The linked article and project changes make that editorial follow-through directly inspectable.

## 12. MemberJunction | Row contents protected, then the remaining row-identity boundary carried into a second work item

**Surface:** [MemberJunction/MJ#4595](https://github.com/MemberJunction/MJ/pull/4595) → [issue #4610](https://github.com/MemberJunction/MJ/issues/4610)  
**Current state:** #4595 merged → LTS #4712 merged/included in v6.1.4. A separately implemented [row-key disclosure fix #5242](https://github.com/MemberJunction/MJ/pull/5242) merged on 2026-10-14; [LTS port #5696](https://github.com/MemberJunction/MJ/pull/5696) is OPEN. The stronger record-specific authorization issue [#4610](https://github.com/MemberJunction/MJ/issues/4610) remains OPEN.

PR #4595 stopped full row contents from riding an unfiltered cache-invalidation broadcast by default. A later `Nakagawa-master` review separated that fix from a remaining metadata boundary: even without `recordData`, a session could still learn another row's stable primary key and mutation timing.

- [Nakagawa-master row-identity review](https://github.com/MemberJunction/MJ/pull/4595#pullrequestreview-5253531713)
- [Nakagawa-master two-layer follow-up](https://github.com/MemberJunction/MJ/pull/4595#issuecomment-5737565146)
- [third-party implementation / carry response](https://github.com/MemberJunction/MJ/pull/4595#issuecomment-5737603820)
- [follow-up issue #4610](https://github.com/MemberJunction/MJ/issues/4610)

The PR author explicitly adopted the two-layer split: an entity-level permission filter was implemented in commit `293b9b40`, and the stronger row-level disclosure question was opened separately as #4610 instead of weakening the regression until it passed. The issue body says its framing is largely from `@Nakagawa-master`'s review and preserves the two-disjoint-row-visibility acceptance test.

A later public contribution on #4610 mapped the follow-up onto MemberJunction's existing ClassFactory extension pattern, keeping the per-subscriber path synchronous and no-I/O rather than routing it through the async permission engine.

- [implementation-shape contribution on #4610](https://github.com/MemberJunction/MJ/issues/4610#issuecomment-5739586260)

PR #4595 was then backported to the `lts/6.1` line as [PR #4712](https://github.com/MemberJunction/MJ/pull/4712). #4712 explicitly identifies itself as a backport of #4595 and carries both the `recordData` allowlist and **entity-level read-permission filtering on delivery**. This is the publicly traceable point at which the first layer added after the review moved from the main development line into the LTS release line.

The 6.1.3 certification record treated this backport as a security **cert-blocker**. #4712 merged into LTS as `f0baf68415e0`, and the subsequent official [v6.1.4 release](https://github.com/MemberJunction/MJ/releases/tag/v6.1.4) (draft=false, prerelease=false; published 2026-09-24 23:53 UTC) explicitly lists #4712. The v6.1.4 release notes also record the changed behavior: cache-invalidation events no longer send row data to every client by default, and consumers re-read through the signed-in user's read path when needed.

**New independent receiver-side implementation and tests (2026-10-14):** On [issue #5241](https://github.com/MemberJunction/MJ/issues/5241), the developers independently specified the remaining row-key exposure and merged [PR #5242](https://github.com/MemberJunction/MJ/pull/5242). For a subscriber whose reads are all row-filtered, the event now omits `PrimaryKeyValues` and `RecordData` while preserving cache correctness through whole-entity invalidation. A different developer [tested live WebSocket connections with restricted and unrestricted users](https://github.com/MemberJunction/MJ/pull/5242#issuecomment-6051805014), observing no record key for the restricted user and a key for the authorized unrestricted user. This was implemented, tested, reviewed and merged at `5aae20c2`. [LTS adaptation #5696](https://github.com/MemberJunction/MJ/pull/5696) has been implemented and tested but is not yet merged.

**Source attribution and remaining scope:** The #4610 author's explicit acknowledgment that its issue framing largely came from `@Nakagawa-master` is primary evidence of a voluntary Origin re-reference. The #5241/#5242 authors are **not independently shown to have read or acted on that earlier review**, so the newer fix is a traceable matching receiving result rather than proof of direct causation. It narrows stable **row-key disclosure** to row-filtered readers; entity-level event existence and `Timestamp` remain observable. The stronger #4610 contract of per-row authorization and withholding unauthorized mutation timings is not yet fully implemented or closed. Live customer use and the LTS port's release are unverified.

**Publicly verifiable here:** review → independent code/test response and explicit Origin attribution → #4595 merge → stronger follow-up issue → #4712 LTS merge/v6.1.4 release → a separate developer's #5242 row-key fix, live WebSocket contrast test and merge.  

---

## 13. Waves Customer Portal | Preserve payment proof while removing a newly unsafe estimate CTA

**Surface:** [wavespestcontrolfl/waves-customer-portal#4608](https://github.com/wavespestcontrolfl/waves-customer-portal/pull/4608)  
**Current state:** merged on 2026-09-19

The PR introduced a delivery-time guard for estimate links and a special rewrite policy for payment receipts: if an estimate CTA is no longer safe to expose, the receipt should still be sent with that CTA removed rather than suppressing proof of payment.

A `Nakagawa-master` review found a vocabulary mismatch in that rewrite path. The refusal guard recognized a short code minted for another entity when its `target_url` resolved to an estimate link, but `rewriteWithheldEstimateLinks()` rewrote only short codes directly typed as `entity_type='estimates'`. The same link form could therefore be classified as unsafe but not transformed, causing the receipt to be refused.

- [Nakagawa-master review](https://github.com/wavespestcontrolfl/waves-customer-portal/pull/4608#pullrequestreview-5254456120)

After that review, commit `029ae44d53` explicitly added the missing `target_url` short-link rewrite path. The current merged implementation resolves both direct estimate short codes and other short codes whose target URL embeds an estimate link, strips the unsafe literal link, preserves the receipt, and records the rewritten estimate id. The PR later merged as `5cecd7627b70d739d7feaf6f45fd784b5741efc3`.

**Publicly verifiable here:** review → matching code/test change for the reported short-link mismatch → merge.  

---

## 14. UpGrade | A UI-only delete rule became a backend-authority work item

**Surface:** [CarnegieLearningWeb/UpGrade#3323](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323) → [issue #3326](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326)  
**Current state:** #3323 **merged into dev on November 2, 2026** ([merge b5ce4805](https://github.com/CarnegieLearningWeb/UpGrade/commit/b5ce4805a8edf3685b270fdd3b105a2234681125)); **separate backend deletion-authority fix #3326 remains OPEN and unimplemented**.

A `Nakagawa-master` review found that the product's frontend delete-permission matrix was not enforced by the backend. In the reviewed branch, an authenticated Reader could directly call destructive single/batch APIs even though the UI hid Delete.

- [Nakagawa-master review](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323#pullrequestreview-5249193998)
- [third-party author response](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323#issuecomment-5732584639)
- [follow-up issue #3326](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326)
- [implementation-shape contribution on #3326](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326#issuecomment-5740003355)

The PR author explicitly named `@Nakagawa-master`, confirmed that the routes had historically lacked role enforcement, and opened #3326 to enforce the role matrix and state rules across both single and batch deletion rather than keeping two inconsistent behaviors.

The later #3326 contribution mapped that work onto the current branch: one shared backend deletion policy, evaluated against current locked target state before mutation, with policy refusals separated from operational deletion failures.

**Two distinct results:** the external team's #3323 feature merge is real; it **does not** mean #3326's server-side deletion authorization has been fixed. A policy repair, denied-delete tests, official release and actual harm prevention are not established.

**Publicly verifiable here:** review → author acknowledgment/restatement → dedicated child work item preserving the boundary → source-level implementation guidance.  

---

## 15. FieldGIS Reference | Historical PASS records became a single-use activation snapshot

**Surface:** [lundus88/fieldgis-reference#273](https://github.com/lundus88/fieldgis-reference/issues/273) → [PR #288](https://github.com/lundus88/fieldgis-reference/pull/288) → [PR #289](https://github.com/lundus88/fieldgis-reference/pull/289) → [PR #290](https://github.com/lundus88/fieldgis-reference/pull/290) → [PR #291](https://github.com/lundus88/fieldgis-reference/pull/291)  
**Current state:** #288 / #289 / #290 merged; #291 open (checked 2026-09-20)

A `Nakagawa-master` comment separated the existence of historical PASS evidence from current authority to activate a commercial system. It proposed forming one explicit activation snapshot that binds the exact artifact, review evidence, business/licence evidence, Preview identity, provider/configuration fingerprints, policy versions, decision time, and revalidation/expiry rules.

- [Nakagawa-master contribution](https://github.com/lundus88/fieldgis-reference/issues/273#issuecomment-5737805962)

After that comment, third-party PR #288 introduced a single-use `LDS_ACTIVATION_SNAPSHOT.json`, a fail-closed validator, and dedicated CI. Its PR body states the rule **“Evidence existence is not activation authority”** and requires material drift to invalidate the snapshot and return launch to HOLD.

- [PR #288](https://github.com/lundus88/fieldgis-reference/pull/288)
- [independent approval](https://github.com/lundus88/fieldgis-reference/pull/288#pullrequestreview-5254772097)
- [merge commit `f0aeaf7c`](https://github.com/lundus88/fieldgis-reference/commit/f0aeaf7c381488d5a38f21753d2043cf11f235ae)

Later public work continues using the same activation-snapshot authority model across additional commercial subcontexts. PR #289 binds domain/email readiness into the model and merged; PR #290 adds email-provider selection while retaining explicit HOLD boundaries and merged; PR #291 records completed subscription evidence while keeping DNS, mailbox ownership, Production, and public launch behind separate HOLD gates. The public record therefore shows the current-authority distinction being carried beyond a single implementation PR.

- [PR #289](https://github.com/lundus88/fieldgis-reference/pull/289)
- [PR #290](https://github.com/lundus88/fieldgis-reference/pull/290)
- [PR #291](https://github.com/lundus88/fieldgis-reference/pull/291)

A fresh read of current `main` after #289 still shows three earlier fail-closed checks from the review are not restored: stale-state rejection, ordered activation-sequence validation, and preview visual/workflow QA validation. Merge and reuse of the model are therefore kept separate from whether those review findings were implemented.

- [review requesting restoration of removed fail-closed checks](https://github.com/lundus88/fieldgis-reference/pull/289#pullrequestreview-5254935377)
- [post-merge follow-up showing the three remaining regressions on current main](https://github.com/lundus88/fieldgis-reference/issues/289#issuecomment-5740198762)

**Publicly verifiable here:** public contribution → third-party governance implementation → independent approval → merge → continued use of the same current-authority model across domain/email readiness, provider selection, and subscription evidence.  

---

## 16. LlamaIndex | Do not let a cache hit replace current node identity with historical identity

**Surface:** [run-llama/llama_index#23003](https://github.com/run-llama/llama_index/pull/23003) → [issue #23083](https://github.com/run-llama/llama_index/issues/23083)  
**Current state:** PR #23003 open; issue #23083 open / maintainer contract decision pending

PR #23003 is a focused fix for an ingestion-cache collision where different documents with identical content could share a cache key and return the wrong `ref_doc_id`.

A `Nakagawa-master` review identified a second, broader contract boundary that remains after that focused fix. For intermediate nodes with a SOURCE relationship, the revised key can intentionally omit the current chunk `id_`, while the cache still returns the entire transformed `BaseNode` list. Two current chunks with the same source/content but different current identities can therefore reuse output carrying identity from an earlier run.

- [Nakagawa-master review](https://github.com/run-llama/llama_index/pull/23003#pullrequestreview-5219816814)
- [third-party author response](https://github.com/run-llama/llama_index/pull/23003#issuecomment-5694376083)
- [dedicated follow-up issue #23083](https://github.com/run-llama/llama_index/issues/23083)

The PR author explicitly confirmed the remaining collision in their own words and deferred the generic cache semantics to a deliberate maintainer-level decision rather than choosing unilaterally inside the focused PR. Issue #23083 now preserves the two coherent contract options:

```text
full-node transformation cache
vs
content-stable payload reuse
```

together with a regenerated-chunk-id regression that makes the choice observable.

**Publicly verifiable here:** review → explicit third-party confirmation/restatement → dedicated maintainer-level work item.  

---

## 17. Publications | Separate reversibility from authority increase, then reuse the boundary in another document

**Surface:** [kishibashi3/publications#52](https://github.com/kishibashi3/publications/pull/52) → [PR #57](https://github.com/kishibashi3/publications/pull/57) → [PR #58](https://github.com/kishibashi3/publications/pull/58)  
**Current state:** #57 merged / GitHub Pages deployment verified; #58 merged / reused inside the same receiver's separate document; later PR #71 keeps D1–D8 through a broader document reorganization and remains open / mergeable

A `Nakagawa-master` review on PR #52 separated whether an operation can be reversed from whether it increases what the same actor is allowed to do next:

```text
reversible
!=
authority-neutral
```

The review proposed that the constrained actor should not be the authority that loosens its own constraints, and that loosening and tightening do not need symmetric approval rules.

- [Nakagawa-master review on #52](https://github.com/kishibashi3/publications/pull/52#pullrequestreview-5258131687)
- [third-party author restatement](https://github.com/kishibashi3/publications/pull/52#issuecomment-5746627251)

The receiver restated this as a missing independent design axis and opened PR #57. The PR explicitly names the PR #52 `@Nakagawa-master` review as its trigger and adds a sixth structural condition: **self-authority remains fixed — the constrained actor cannot loosen its own constraints**.

- [PR #57](https://github.com/kishibashi3/publications/pull/57)
- [merge commit `4d32ec58`](https://github.com/kishibashi3/publications/commit/4d32ec58d5cbf1c904c432552e114c144186c064)
- [GitHub Pages deployment](https://github.com/kishibashi3/publications/actions/runs/35506196582)
- [merged reader-facing chapter](https://github.com/kishibashi3/publications/blob/main/docs/ai/agent-design/chapter-05.ja.md)

The boundary then became a consistency constraint inside the receiver's publication system. In PR #58, a receiver-side reviewer identified a conflict with the newly merged condition from #57 and proposed a separate D8 “self-authority fixed” rule. The writer adopted it, a later review marked the revision LGTM, and #58 merged.

- [#58 reviewer carry into D8](https://github.com/kishibashi3/publications/pull/58#issuecomment-5749116909)
- [D8 implementation commit](https://github.com/kishibashi3/publications/commit/e524c71d9f01045f4c8dac60a8ee8bb45a3198c4)
- [#58 re-review](https://github.com/kishibashi3/publications/pull/58#issuecomment-5749456249)
- [#58 merge commit `36e4c5df`](https://github.com/kishibashi3/publications/commit/36e4c5df963e2b3645c7591d8cb933c4f36e48e0)

The carry continues in later PR #71. While consolidating the receiver's AA documents, the PR explicitly says that the P1–P3 and D1–D8 text is preserved. Its current head `e06e748` still contains D8, “self-authority fixation,” in `drafts/agentic-agile/principles.md`. This is evidence of continued receiver-owned preservation across a later structural rewrite; PR #71 is still open / mergeable and is not counted as merged.

- [PR #71 | later document-system consolidation](https://github.com/kishibashi3/publications/pull/71)
- [Principles at PR #71 current head](https://github.com/kishibashi3/publications/blob/e06e74828f656796ec38f455efea24d49fcda83f/drafts/agentic-agile/principles.md)

**Independent AI-skill routing carry (verified October 31, 2026):** The same third-party author independently owned [issue #81](https://github.com/kishibashi3/publications/issues/81) and [merged PR #125](https://github.com/kishibashi3/publications/pull/125) ([exact merge commit](https://github.com/kishibashi3/publications/commit/f502a469ced9a406b39c71ff6e5504d470ef5d6a)). Their optional [Claude Code `agent-design` skill](https://github.com/kishibashi3/publications/blob/main/plugins/thinking-shelf/skills/agent-design/SKILL.md) now routes ordinary questions about approval mode, allowlists, credentials and loosening an agent's own privileges to their chapter 05, condition 6, and states the self-authorization boundary in its operational rules. This is a **receiver-owned conversion of an existing credited chapter into an AI skill's discovery and decision pathway**, not evidence that an unrelated AI actually ran it. The receiver's [own review](https://github.com/kishibashi3/publications/pull/125#issuecomment-6519048300) explicitly leaves four end-to-end activation/decision prompts untested. Neither external installations, AI answers, independent reading/citation of a canonical Nakagawa Parent, nor a second recipient are established.

**Publicly verifiable here:** origin-preserved review → third-party restatement → dedicated reader-facing implementation → merge / Pages deployment → reuse as a consistency rule in another document inside the same receiver → merge → preservation of the same D8 in a later receiver-owned document-system rewrite head.  

---
## 18. PostHog | Bind recurring-agent approval to the instructions the human actually reviewed

**Surface:** [PostHog/posthog#101991](https://github.com/PostHog/posthog/pull/101991)  
**Current state:** open / unmerged

This PR can turn a conversation into a recurring scout such as a weekly agent. In the earlier implementation, the card showed a name, short description, cadence, and destination, while the model-authored `scout.body` that would run on every schedule was not shown or editable before creation.

A `Nakagawa-master` review stated the boundary:

```text
approval of a summary
!=
approval of hidden recurring instructions
```

- [Nakagawa-master review](https://github.com/PostHog/posthog/pull/101991#pullrequestreview-5235367516)

A later third-party commit, `244ff417`, explicitly says the scheduled agent had been created from instructions the user never saw. It adds an editable instructions field to the card, creates the scout from the reviewed/edited `scoutBody`, and adds regression coverage that binds the edited value to the creation input.

- [implementation commit `244ff417`](https://github.com/PostHog/posthog/commit/244ff417b3b5228779a8b904035a881bc05cdff5)

The commit does not identify the `Nakagawa-master` review as its sole cause. The bounded claim is that a matching third-party implementation change is publicly visible after the review.

**Publicly verifiable here:** review → third-party code / UI / test change; the instructions shown to the human are now the value used to create the recurring agent.  

---

## 19. DAIR Prompt Engineering Guide | Separate content classification from action authority

**Surface:** [dair-ai/Prompt-Engineering-Guide#757](https://github.com/dair-ai/Prompt-Engineering-Guide/pull/757)  
**Current state:** open / unmerged, with a third-party author implementation commit

This PR adds a reader-facing teaching page that classifies posts/comments and maps the classification toward downstream actions such as comment, react, or skip.

A `Nakagawa-master` review identified two boundaries:

```text
untrusted content
!=
instructions the classifier should obey

content classification
!=
current authorization to perform the downstream action
```

- [Nakagawa-master review](https://github.com/dair-ai/Prompt-Engineering-Guide/pull/757#pullrequestreview-5280350258)

The third-party author publicly agreed with both points and pushed follow-up commit `4a5334a`. The commit message itself says **“Two hardenings from @Nakagawa-master's review on #757.”**

- [third-party author response](https://github.com/dair-ai/Prompt-Engineering-Guide/pull/757#issuecomment-5783121174)
- [implementation commit `4a5334ab`](https://github.com/dair-ai/Prompt-Engineering-Guide/commit/4a5334ab0ea82e97c122d53a78a6162d8e56e6b9)

The commit delimits interpolated fields as untrusted data and adds a separate second-stage action gate plus a regression case so that a content label is not treated as execution authority.

The receiver's own commit explicitly attributes two concrete hardenings to the `@Nakagawa-master` review. The linked code and tests show how that structural insight entered a third-party teaching tool.

**Publicly verifiable here:** review → explicit third-party agreement/restatement → implementation commit explicitly naming the review as the source of the two hardenings → concrete reader-facing teaching change.  

---

## 20. TourCRM | Do not let current participation rewrite historical attendance

**Surface:** [Alan8893/tourcrm#97](https://github.com/Alan8893/tourcrm/pull/97) → [PR #101](https://github.com/Alan8893/tourcrm/pull/101)  
**Current state:** #97 merged / #101 merged

In PR #97, an Attendance row could remain stored while read/correction paths still asked whether the person was an active participant **now**. After participation ended, a completed occurrence could therefore lose that person from the visible historical roster and denominator, and an existing historical Attendance row could become uncorrectable.

A `Nakagawa-master` comment stated the boundary:

```text
current roster
!=
historical occurrence roster
```

and proposed evaluating participation against the occurrence's own historical time window rather than today's membership state.

- [Nakagawa-master comment on #97](https://github.com/Alan8893/tourcrm/pull/97#issuecomment-5689122153)

Receiver commit `b6da0eb8` changed `has_participation()` and the recurring roster path in `list_attendance()` from `now()` to overlap with the occurrence's `[starts_at, ends_at)` window. Its commit message explicitly says **“Addresses PR #97 review feedback (Nakagawa-master).”**

- [implementation commit `b6da0eb8`](https://github.com/Alan8893/tourcrm/commit/b6da0eb880d474c7e8322f2b2da8bef02a64e1f6)

PR #101 then added regressions for the fix. A second `Nakagawa-master` comment identified that the new tests were themselves wall-clock dependent: because the fixture occurrence was in the future, the old implementation could still pass the tests before the calendar crossed the fixture date.

- [Nakagawa-master regression-evidence comment on #101](https://github.com/Alan8893/tourcrm/pull/101#issuecomment-5691884921)

The receiver introduced `_PAST_START` so the old `now()` predicate and the occurrence-overlap predicate deterministically diverge, and verified that temporarily restoring the old implementation makes all three regressions fail. Commit `568c8fec` also explicitly says **“Addresses PR #101 review feedback (Nakagawa-master).”**

- [test-evidence commit `568c8fec`](https://github.com/Alan8893/tourcrm/commit/568c8fecbbcb56297deb385ea34c8bb61a2839e5)
- [Nakagawa-master re-review confirming the wall-clock weakness is resolved](https://github.com/Alan8893/tourcrm/pull/101#pullrequestreview-5219832326)

Both PRs are merged. In this case, receiver-side commits explicitly attribute both the concrete implementation correction and the regression-evidence correction to `Nakagawa-master` review feedback.

**Publicly verifiable here:** historical-state boundary review → receiver implementation commit explicitly naming the review → second review finding a weakness in the proof tests → receiver test correction explicitly naming the review → merge.  

---

## 21. MemberJunction | An exported alias does not make the underlying declaration unreachable to consumers

**Surface:** [MemberJunction/MJ#4487](https://github.com/MemberJunction/MJ/pull/4487)  
**Current state:** merged (2026-09-24)

PR #4487 introduces a large TypeScript naming-conventions gate that classifies which members can be renamed without breaking external consumers.

A `Nakagawa-master` review identified a compatibility hole in named re-exports. If the public-symbol collector records only the exported alias in:

```ts
export { ChatParams as PublicChatParams } from "./shape.js"
```

while a finding is keyed to the declaration name `ChatParams`, the gate can incorrectly conclude that a member of the data shape is not public. That matters because the rename pass selects `error` type-member findings, while an interface member has no runtime object on which a backward-compatible stub can be installed.

- [Nakagawa-master review](https://github.com/MemberJunction/MJ/pull/4487#issuecomment-5219601735)

A separate third-party reviewer later independently rechecked the issue and explicitly wrote: **“The aliased re-export hole Nakagawa-master reported on 2026-09-16 is still open.”**

- [independent reviewer confirmation](https://github.com/MemberJunction/MJ/pull/4487#issuecomment-5241419422)

Receiver commit `dfd4588d` changed the collector to preserve both sides of a named re-export and added regressions showing that an aliased published data-shape member stays at `warn`, while an unre-exported sibling type in the same file still remains `error`. The receiver's commit message explicitly states **“Reported by Nakagawa-master on 2026-09-16.”**

- [implementation commit `dfd4588d`](https://github.com/MemberJunction/MJ/commit/dfd4588d798b68b982f2554295a0d4d3afb005c2)
- [Nakagawa-master focused re-check](https://github.com/MemberJunction/MJ/pull/4487#issuecomment-5252973190)

A later reviewer confirmed that this required finding was fixed, and PR #4487 merged on 2026-09-24.

**Publicly verifiable here:** Nakagawa review → independent third-party confirmation of the same hole → receiver code/test commit explicitly attributing the report to Nakagawa-master → focused re-check → later review confirmation → merge.  

---

---

## 22. Qwen Code | Approval boundary for paid Batch API actions

**Target:** [QwenLM/qwen-code#12492](https://github.com/QwenLM/qwen-code/pull/12492)  
**Current state:** merged and released in Qwen Code v0.24.6 (2026-09-26 JST) / real receiver-side Batch use documented in #12825 / merge commit `c3a4058a0c72`

[Nakagawa-master's public comment](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5817569552) separated approval of `qwen batch run` from approval of the concrete billed batch snapshot. The proposed contract binds the exact item set, frozen settings and cost estimate to a canonical digest, and treats later drift as stale approval.

Third-party developer `yiliang114` attributed and adopted the proposal, implementing a preview, snapshot digest, pre-submit revalidation and regression tests in `3d06e1ad8e`. The author described this as a lighter form of the full proposed flow.

- [third-party response](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5817836928)
- [adoption response](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5818159716)
- [implementation commit `3d06e1ad8e`](https://github.com/QwenLM/qwen-code/commit/3d06e1ad8e749c647a2eb5d447b867fc50955a13)
- [maintainer verification at head `206a444b`](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5836312195)
- [merge commit](https://github.com/QwenLM/qwen-code/commit/c3a4058a0c7207de7b421e9da0622a9ec890dbad)
- [Qwen Code v0.24.6 release](https://github.com/QwenLM/qwen-code/releases/tag/v0.24.6)

The author fixed the three maintainer-requested pre-merge findings in `56f06075b3` and two additional suggestions in `206a444b30`. Qwen Code CI (run 43130) and TUI parity (run 3993) passed on the current head. The maintainer judged head `206a444b` mergeable; the PR merged on 2026-09-26 JST and shipped in v0.24.6 that day. Non-blocking follow-ups remain in [#12707](https://github.com/QwenLM/qwen-code/issues/12707).

After release, the same receiver/collaborator `yiliang114` documented real use in [issue #12825](https://github.com/QwenLM/qwen-code/issues/12825): v0.24.6's `/batch-api` executor was used for a nine-document DashScope Batch translation job, with the dry-run → `--expect` → `collect --wait` path, concrete batch job ids, and repeated output evidence recorded publicly. This confirms **real receiver-side operational use after release**; it is not evidence of independent external-user adoption or user scale.

**Confirmed by the public record:** source-attributed third-party adoption, implementation of the proposed approval boundary, PR merge and release, and real receiver-side operational use of v0.24.6. A real paid use at an earlier PR head is also documented.  
**Not yet confirmed:** independent external-user production adoption or user scale, broad reader propagation, or endorsement of the wider theory system. The entire PR, later fixes and release are not attributed to Nakagawa-master alone.


---


## 23. AI-News | Separate URL count from independent evidence-root count in recurring editorial verification

**Target:** [022740mix-spec/AI-News#124](https://github.com/022740mix-spec/AI-News/issues/124) → [PR #131](https://github.com/022740mix-spec/AI-News/pull/131)  
**Current state:** receiver explicitly adopted the distinction → recurring editorial rule merged on 2026-09-25 → multiple later reader-facing publication cycles visibly reuse the rule (verified through 2026-10-01 JST)

In issue #124, `Nakagawa-master` proposed separating the number of URLs from the number of **independent evidence roots**. The proposal distinguishes primary sources, independent observations, derived/syndicated material, and unknown lineage instead of treating `url_count` as `evidence_root_count`.

The repository owner explicitly replied **“採用します” (“We will adopt it”)**, opened PR #131, and explained the missing layer: existing L2/L3 checks verified whether a statement appeared in a source, but did not test whether multiple sources were actually independent. The receiver also explicitly separated causality: an earlier GLM-5.3 article was unrelated to #124, while **the rule change itself was made because of issue #124**.

- [receiver adoption and rationale](https://github.com/022740mix-spec/AI-News/issues/124#issuecomment-5823549498)
- [merged rule PR #131](https://github.com/022740mix-spec/AI-News/pull/131)
- merge commit `800e53e8d5579cfe061f39ede01ac7b8b68877d6`

PR #131 merged on 2026-09-25T08:42:13Z and placed the distinction in the repository's durable `CLAUDE.md` editorial rules.

A later main-branch article about Claude Sonnet 5.5 provides a fresh reader-facing recurrence. Commit [`e5b11d79...`](https://github.com/022740mix-spec/AI-News/commit/e5b11d79d1b9c4925758e0bad066e7bc03b3e5f3), dated 2026-09-28T21:43:55Z, publishes the article into the main article data, Atom feed, and sitemap. Its verification note explicitly separates:

- primary sources reached directly;
- Anthropic's own measurements from independent reproduction;
- the context of Artificial Analysis evaluation;
- an unreachable system card, marked as unread rather than silently treated as checked;
- benchmark figures whose settings are not comparable.

This is stronger than a draft-only reuse signal: the merged rule is recurring in a receiving-project, reader-facing publication surface.

The recurrence continued in a new publication cycle on 2026-09-30 UTC:

- [PR #152](https://github.com/022740mix-spec/AI-News/pull/152) separates one primary root from multiple derivative reports sharing that root and keeps the unverified `2.1.277 or later` version claim out of the article because the official changelog did not establish it.
- [PR #153](https://github.com/022740mix-spec/AI-News/pull/153) records primary / independent-observation / derived-source counts, states that independent third-party verification was not found, separates Google-reported benchmark results from independent reproduction, and declines to insert non-comparable benchmark versions into the site-wide comparison table.
- Both PRs merged into main article data, feed, and sitemap at 2026-09-30T23:49Z / 23:51Z.

This is evidence of the receiver reusing the durable rule in its own later public production cycle, not merely agreeing once in the source issue. The later articles do not explicitly rereference Nakagawa Master, so this is not counted as a new Nakagawa Master source rereference.

**Publicly verifiable here:** Origin-preserved proposal → explicit receiver adoption and causality statement → durable rule merge → later main/feed/sitemap publication that visibly applies the evidence-lineage distinction.  

---

## 24. LlamaIndex | Forward-progress overlap rules and default-activation impact implemented in a third-party PR

**Target:** [run-llama/llama_index#23027](https://github.com/run-llama/llama_index/issues/23027) → [PR #23029](https://github.com/run-llama/llama_index/pull/23029)  
**Current state:** third-party code/tests/docs changes present; PR open and unmerged; repository CI green is not established

In issue #23027, `Nakagawa-master` proposed three explicit boundaries for CodeSplitter line overlap:

- reject configurations unless `0 <= chunk_lines_overlap < chunk_lines`;
- treat `chunk_lines` as a cap on the final emitted chunk including overlap;
- if the historically inert default `chunk_lines=40` becomes active, document the migration/re-index implications because chunk boundaries, node ids, embeddings and persisted indexes can change.

The issue reporter explicitly agreed, writing **“These are the right boundaries to pin down.”**

- [issue discussion](https://github.com/run-llama/llama_index/issues/23027)

On PR #23029, `Nakagawa-master` then pointed out that the candidate still did not reject `overlap >= chunk_lines` and that activating the default was observable migration behavior.

- [Nakagawa-master PR comment](https://github.com/run-llama/llama_index/pull/23029#issuecomment-5652061794)

The PR author publicly replied **“Addressed the outstanding points”** and identified commits `ac76ed346` and `ea92fff99`.

- [author response](https://github.com/run-llama/llama_index/pull/23029#issuecomment-5683015010)
- [implementation commit `ac76ed346`](https://github.com/run-llama/llama_index/commit/ac76ed3462de21e85405abbbf3362299852aabcd)
- [documentation commit `ea92fff99`](https://github.com/run-llama/llama_index/commit/ea92fff99dba3b990dff4a0cb28e5ce1ba712651)

The changes add cross-field validation, equality/greater-than negative tests, an overlap-inclusive line cap, source-separator preservation including CRLF, and regression coverage for the active default. The documentation now warns that activating the line cap can change chunk boundaries and may require regenerating indexed nodes and embeddings.

A later `Nakagawa-master` re-check recorded no remaining blocker within the earlier review scope, while explicitly refusing to treat the repository's `action_required` workflow state as green CI evidence.

- [focused re-check](https://github.com/run-llama/llama_index/pull/23029#issuecomment-5683971610)

**Publicly verifiable here:** public boundary proposal/review → explicit reporter agreement → third-party author explicitly says the outstanding points were addressed → code/tests/docs changes → focused re-check.  
**Not established yet:** PR merge, green repository CI, release, production use, user-scale effect, intellectual priority over the general principle, or endorsement of the wider theory corpus.

---

## 25. Codex Autonomy Runner | A failed operation is not evidence that the intended boundary was exercised

**Surface:** [Innlab-idi/codex-autonomy-runner#59](https://github.com/Innlab-idi/codex-autonomy-runner/issues/59)  
**Current state:** receiver explicitly adopted a stage-evidence invariant → durable contract and ContainmentGate verified → worker/transport/check executor merged → **two real worker attempts, both stopped before publication** → 01B and 01C fixes independently implemented and merged, **real post-01C check still unverified**

A public `Nakagawa-master` comment separated four states that are easy to collapse in sandbox / authority-boundary probes:

```text
transport/helper invocation succeeded
!=
controlled child operation began
!=
target boundary was exercised
!=
boundary passed
```

The point was to prevent a failed operation from being upgraded into positive evidence that the intended boundary was actually reached.

- [Nakagawa-master comment](https://github.com/Innlab-idi/codex-autonomy-runner/issues/59#issuecomment-5775879719)

Receiver `Innlab-idi` explicitly called this distinction **“a useful general invariant,”** said it should be preserved for future probes and the WorkerExecutor, and stated that the Nakagawa-master comment had prompted a broader review.

- [receiver restatement / preservation intent](https://github.com/Innlab-idi/codex-autonomy-runner/issues/59#issuecomment-5821543543)

Nakagawa-master then extended the structure with `authority_designated`: later success or failure should not back-fill an earlier stage; each stage should have its own positive evidence. The receiver answered that this direction would be made explicit as a durable evidence contract after the first complete E1–E9 run.

- [adjacent prior-work / stage-separation response](https://github.com/Innlab-idi/codex-autonomy-runner/issues/59#issuecomment-5834071297)
- [receiver durable-contract commitment](https://github.com/Innlab-idi/codex-autonomy-runner/issues/59#issuecomment-5871384250)

The receiver then materialized a contract that binds each stage to separate positive evidence:

```text
invocation_bound
authority_designated
child_started
target_boundary_attempted
policy_result
forbidden_effect_observed
cleanup_proven
verdict
```

- [durable evidence contract mapping](https://github.com/Innlab-idi/codex-autonomy-runner/issues/59#issuecomment-5913106705)
- [formal exact-evidence review](https://github.com/Innlab-idi/codex-autonomy-runner/issues/59#issuecomment-5913132794)
- [human-owner ContainmentGate = VERIFIED transition](https://github.com/Innlab-idi/codex-autonomy-runner/issues/59#issuecomment-5913352453)

The line then moved from governance text into implementation and execution:

- [PR #62](https://github.com/Innlab-idi/codex-autonomy-runner/pull/62) — offline WorkerExecutor adapter, merged as `d8aa78006a3c0ba6c3da8f4a0177cf0a15287f2a`
- [PR #63](https://github.com/Innlab-idi/codex-autonomy-runner/pull/63) — live Codex worker transport, merged as `5923a4461f1e2bcfa8d945f3ddf6acd9d27e8ad7`
- [PR #64](https://github.com/Innlab-idi/codex-autonomy-runner/pull/64) — contained CheckExecutor, merged as `6a4d5dcd9de63c9d52ae0211fc01afdc308bee96`

A human owner then authorized **one** real pilot worker. The worker process completed reliably and reached the RUNTIME-03 publication check, but that declared check returned nonzero. The system failed closed before RUNTIME-04 staging / commit / push / PR. No remote branch or publication mutation was attempted.

- [first one-shot real worker result](https://github.com/Innlab-idi/codex-autonomy-runner/issues/59#issuecomment-6013365402)

Read-only diagnosis then established that the worker-created content itself was clean and that the same `git diff --check` returned 0 outside the contained check. The receiver identified a bounded mechanism consistent with the false nonzero: the contained CheckExecutor made repository/Git metadata read-only but did not fix `GIT_OPTIONAL_LOCKS=0`, while Git porcelain may attempt optional index refresh/locking even for a read-only diff.

- [post-worker diagnosis](https://github.com/Innlab-idi/codex-autonomy-runner/issues/59#issuecomment-6013640426)
- [human-owner authorization for CHECK-EXECUTOR-01B-RUNNER](https://github.com/Innlab-idi/codex-autonomy-runner/issues/59#issuecomment-6013944031)
- [bounded materialization contract](https://github.com/Innlab-idi/codex-autonomy-runner/issues/59#issuecomment-6013945634)

The 01B repair was implemented in [PR #65](https://github.com/Innlab-idi/codex-autonomy-runner/pull/65), without granting publication permission. After a **separate human authorization**, the receiver actually ran a **second** one-shot worker. Its target files and focused check passed, but the contained Git publication check returned code 129; the runner again **refused staging, push, or PR publication**. The second authorized attempt is consumed, not pending.

- [second real worker result and publication refusal](https://github.com/Innlab-idi/codex-autonomy-runner/issues/59#issuecomment-6046729053)
- [receiver diagnosis of the sandbox Git trust-bridge gap](https://github.com/Innlab-idi/codex-autonomy-runner/issues/59#issuecomment-6046865408)

The receiver then opened a [separately human-authorized 01C work item](https://github.com/Innlab-idi/codex-autonomy-runner/issues/67): Git's sandbox-owned `safe.directory` trust bridge was being erased by the inner check-environment scrubber. The repair **does not blindly pass through environment variables**. It rebuilds only the exact-repository Git trust settings under the runner's control, rejects unrelated Git configuration, and keeps optional Git locking disabled. [PR #68](https://github.com/Innlab-idi/codex-autonomy-runner/pull/68) **merged on 2026-10-08**; the receiver reports 21 focused tests passing and 329 total passing, with one skipped. Those counts are receiver-reported, not tests rerun by this archive.

**Recorded result:** both real worker attempts reached a bounded check and stopped before publication; investigating those failures led the receiver to implement and merge additional code. The source trail currently ends at that merged repair.

**Publicly verifiable here:** Nakagawa-master's stage-evidence distinction → explicit receiver adoption and durable contract → independently operated gate verification → merged runner implementations → **two** human-authorized real worker attempts stopped before publication → receiver-diagnosed failures → receiver-owned 01B and 01C repairs merged. The 01C live contained probe and any later worker/publication remain unverified.


The distinction between a reported stage and its actual evidence connects to [Human-Descendant AI Civilization Theory Vol. 8 — epistemic integrity](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/), which explores provenance, independent observation and correction.

---
## 26. AI Weekly Reads | Preserve claimant attribution instead of turning self-reported results into editorial facts

**Surface:** [sophiamyang/ai-weekly-reads#22](https://github.com/sophiamyang/ai-weekly-reads/pull/22) → [#30](https://github.com/sophiamyang/ai-weekly-reads/pull/30) → [#31](https://github.com/sophiamyang/ai-weekly-reads/pull/31)  
**Current state:** two weekly-edition corrections observed / durable generation rule, audit, and regression tests merged / next-cycle automatic reuse not yet observed

In the first weekly edition, some speaker/vendor-reported measurements were presented without preserving who made the claim. After a `Nakagawa-master` review, the receiver-side edition was corrected.

The same failure mode recurred in the 2026-09-26 edition. The review separated:

```text
speaker/vendor reports a measured result
!=
weekly editor independently verified the result
!=
independent reproduction/generalization
```

and asked for the boundary to move from a one-off text correction into the summary prompt, Reading Priority rules, audit, and regression tests.

- [Nakagawa-master review on #30](https://github.com/sophiamyang/ai-weekly-reads/pull/30#pullrequestreview-5330097552)
- [public epistemic-integrity reference card](machine-discovery/epistemic-integrity-reference-card.json)

The receiver explicitly replied that **“the regression was real and the diagnosis was right,”** corrected and merged edition #30, and then merged PR #31 to make the distinction durable.

- [receiver response](https://github.com/sophiamyang/ai-weekly-reads/pull/30#issuecomment-5856767055)
- [merged edition #30](https://github.com/sophiamyang/ai-weekly-reads/pull/30)
- [merged generation-rule PR #31](https://github.com/sophiamyang/ai-weekly-reads/pull/31)

PR #31 updates both summary prompts so self-reported quantitative/comparative results keep claimant attribution unless an independent evaluation is identified, removes overclaiming evidence signals from Reading Priority, adds audit terms, and pins the rule with regression tests.

**Publicly verifiable here:** first edition correction → same regression recurred later → review identified it → receiver explicitly accepted the diagnosis → edition #30 corrected and merged → the same boundary was implemented in generation prompts, priority rules, audit, and tests in merged PR #31.  

---

## 27. n8n | A review triggered runtime verification and a clearer data-boundary model

**Target:** [n8n-io/n8n#37613](https://github.com/n8n-io/n8n/pull/37613)  
**Current state:** explicit receiver restatement / running-instance verification / clarified PR data model / open draft, unmerged

A `Nakagawa-master` review noted that native `join()` and comparator-less `toSorted()` coerce array elements, so a live object with a custom `toString()` hook could matter **if such an object can actually reach the native-evaluation boundary**.

- [Nakagawa-master review](https://github.com/n8n-io/n8n/pull/37613#pullrequestreview-5325886846)

The PR author explicitly confirmed that the coercion mechanics were correct, then tested the premise on a running n8n instance. The test showed that Code/Set node output is normalized to JSON at the node boundary, so the exotic object shape in question does not reach native evaluation as a live coercible object.

- [receiver re-verification and explanation](https://github.com/n8n-io/n8n/pull/37613#issuecomment-5856928471)

During that investigation, defensive guards were briefly added. After the runtime premise was disproved, the author removed those guards and updated the PR's stated data model. This case is therefore **not** recorded as adoption of Nakagawa's proposed guard. The verified external effect is that the review caused additional receiver-side testing and a more explicit implementation boundary.

**Publicly verifiable:** review → receiver confirms mechanics → independent runtime test → premise rejected at the actual data boundary → unnecessary guard removed → PR model clarified.  


---

## 28. LlamaIndex | Defaulted positional parameter + `**kwargs` silent misbinding pinned in code and tests

**Target:** [run-llama/llama_index#23272](https://github.com/run-llama/llama_index/pull/23272)  
**Current state:** exact regression added to receiver code/tests after review / focused re-check completed / PR open and unmerged / repository CI green not established

PR #23272 repairs single-argument `FunctionTool` dispatch when a custom schema field name differs from the callable's positional parameter name.

The initial patch replaced `inspect.Signature.bind_partial()` with full `bind()`, fixing the case where a **required** positional parameter remained unbound. A `Nakagawa-master` review then identified a quieter variant: if that positional parameter has a default and the callable also accepts `**kwargs`, full binding succeeds while the generated value is swallowed by `kwargs`, leaving the callable to return its default.

- [Nakagawa-master comment](https://github.com/run-llama/llama_index/pull/23272#issuecomment-5330425676)

The next receiver commit, `c15a95233bd7678923828b71f9f4f6b78d6b5ab5`, adds that exact regression directly to the test suite for both sync and async calls, plus reverse-regression cases covering injected partial parameters and field defaults.

The implementation now distinguishes “can these kwargs form a valid call?” from “did the generated field actually bind an explicit callable parameter?”. When a single generated field is accepted only through `**kwargs` and a positional compatibility call is valid, the fallback is preserved.

- [receiver commit `c15a952`](https://github.com/run-llama/llama_index/commit/c15a95233bd7678923828b71f9f4f6b78d6b5ab5)
- [focused re-check](https://github.com/run-llama/llama_index/pull/23272#issuecomment-5857485429)

**Publicly verifiable:** review identifies the defaulted-positional + `**kwargs` silent misbinding → next commit on the same PR adds the exact regression and reverse-regression tests → focused re-check finds no remaining blocker in that scope.  
The receiving developer's commit records the specific implementation and technical scope. The earlier Nakagawa Master question remains a separately inspectable public source.

---

## 29. AI-News | A published article was brought back into sync with changed primary-source state, and the update path itself was hardened

**Surface:** [022740mix-spec/AI-News#111](https://github.com/022740mix-spec/AI-News/pull/111) → published article `agent-self-authorization-approval-gate-2026` → [PR #135](https://github.com/022740mix-spec/AI-News/pull/135)  
**Current state:** receiver explicitly adopted the separation and published a standalone article / later follow-up caught stale status / receiver re-checked primary records and updated article source state / PR #135 merged / GitHub Pages build and deploy for the merge commit independently verified successful / reader scale not established

On PR #111, `Nakagawa-master` proposed separating unverified reported incidents from a distinct, publicly verifiable implementation example about authority-increasing transitions. The review separated authentication, capability, authority, and human approval, and noted that a transition such as `ask → auto` is not made safe merely because it can later be reversed.

- [Nakagawa-master review](https://github.com/022740mix-spec/AI-News/pull/111#pullrequestreview-5258348803)

The receiver explicitly replied **“切り分けの提案を採用します”** (“we will adopt the separation proposal”), checked the cited records, and then reported that it had published the verified material as a standalone article rather than leaving it inside the still-blocked draft PR.

- [receiver adoption response](https://github.com/022740mix-spec/AI-News/pull/111#issuecomment-5747145782)
- [receiver publication response](https://github.com/022740mix-spec/AI-News/pull/111#issuecomment-5747165347)

On 2026-09-27, `Nakagawa-master` pointed out that the article's “unfixed / unmerged” description of the Local Operator control-plane path had become stale: PR #1324 had merged, v0.61.11 had released it, and Issue #1310 had closed.

- [Nakagawa-master follow-up](https://github.com/022740mix-spec/AI-News/pull/111#issuecomment-5853890886)

The receiver re-checked the primary records, acknowledged that the promised status tracking had been six days behind, and opened PR #135. The PR body explicitly says feedback on draft PR #111 exposed the stale state. The merged change updated the article body, status table, excerpt, primary-source status, and edit history, and also added an `updatePrimarySources` path so source-status metadata can be updated without leaving the article body and source block inconsistent.

- [receiver update response](https://github.com/022740mix-spec/AI-News/pull/111#issuecomment-5854722227)
- [merged update PR #135](https://github.com/022740mix-spec/AI-News/pull/135)
- [merge commit `2625b150`](https://github.com/022740mix-spec/AI-News/commit/2625b150eb2aa761ab47c475ef76ce33ddfbd3ac)
- [GitHub Pages deployment run `36310141967`](https://github.com/022740mix-spec/AI-News/actions/runs/36310141967) — both build and deploy completed successfully; environment URL: `https://022740mix-spec.github.io/AI-News/`

The receiver responses and PR text are marked as generated with Claude Code. This page therefore records **receiver-account adoption, reader-facing publication, source-state correction, and tooling change**, not unaided human authorship.

**Publicly verifiable:** origin review → explicit receiver adoption → standalone reader-facing publication → later Nakagawa follow-up identifies stale external state → receiver re-checks primary sources → article source state and update tooling change → PR #135 merges → GitHub Pages build/deploy for the merge commit succeeds.  
**Not established:** reader count or behavior, propagation to another receiver, voluntary explicit source re-reference, unaided human authorship, or endorsement of the wider theory corpus.



---

## 30. LlamaIndex | Dict-form MCP non-text content now preserves semantic blocks

**Target:** [run-llama/llama_index#23261](https://github.com/run-llama/llama_index/pull/23261)  
**Current state:** receiver explicitly acknowledged the serialized-content gap and changed code/tests / focused re-check completed / PR open and unmerged / broader CI and live-MCP validation not established

PR #23261 adds success-path parsing from MCP `CallToolResult` into LlamaIndex content blocks. Object-shaped results already mapped text, image, audio, and embedded resources semantically, while the dict/wire-format branch only treated text semantically and stringified image, audio, and resource dictionaries.

A `Nakagawa-master` review identified that asymmetry and asked that serialized dict content preserve the same semantics as object content, with regressions for dict image, audio, embedded-resource text, and the unknown-content fallback.

- [Nakagawa-master review](https://github.com/run-llama/llama_index/pull/23261#pullrequestreview-5331158205)

The PR author replied **“Thanks for catching the serialized-content gap.”** and changed current head `5164d2b303da645dde2a92527a757a4908707dd3` so dict and object content use the same structural field-access path.

- [receiver response](https://github.com/run-llama/llama_index/pull/23261#issuecomment-5861650879)
- [receiver commit `5164d2b`](https://github.com/run-llama/llama_index/commit/5164d2b303da645dde2a92527a757a4908707dd3)

The implementation base64-decodes dict image/audio payloads before constructing `ImageBlock` / `AudioBlock`, preserves embedded-resource text as `TextBlock`, and retains textual fallback for unknown or malformed shapes. Tests pin text/image/audio/resource for both dict and object forms. The author reported 39 passed / 3 skipped in the focused test file, while explicitly noting that the broader tools suite, mypy, and a live MCP server were not rerun/tested after the revision.

A focused re-check then confirmed no remaining blocker within the serialized-content scope.

- [focused re-check](https://github.com/run-llama/llama_index/pull/23261#issuecomment-5861899474)

**Publicly verifiable:** Nakagawa review identifies dict-form non-text semantic loss → receiver explicitly acknowledges the gap → parser and dict/object regression matrix change on the same PR → focused re-check.  
**Not established:** PR merge, release, production use, green repository-wide CI, broader tools/mypy/live-MCP validation, user-scale impact, intellectual priority over the general principle, or endorsement of the wider theory corpus.
---

## 31. Qwen Code | Separate `maxCostUsd` forecast from its hard bound, then observe a prompt-free receiver re-reference to Nakagawa Master

**Surface:** [QwenLM/qwen-code#12707](https://github.com/QwenLM/qwen-code/issues/12707) → [PR #12895](https://github.com/QwenLM/qwen-code/pull/12895)  
**Current state:** receiving-project follow-up PR voluntarily re-references Nakagawa-master in its body → code / tests / docs implementation → non-author maintainer approval → merged on 2026-09-28 → shipped in stable Qwen Code v0.24.7 on 2026-09-29 / operational use and user-scale contact not yet observed

In #12707, `Nakagawa-master` pointed out that the hard `maxCostUsd` gate was using the same rough forecast that explicitly excluded thinking tokens, so this contract did not hold:

```text
"maxCostUsd passed"
=>
"the submitted batch cannot exceed maxCostUsd under the request's own caps"
```

- [Nakagawa-master comment](https://github.com/QwenLM/qwen-code/issues/12707#issuecomment-5846367294)

The comment proposed separating the UX estimate from the budget-enforcement quantity, computing a conservative worst-case bound from finite provider-recognized request caps, failing closed when no finite bound exists under `maxCostUsd`, and pinning a regression where a low forecast but high request cap must be refused.

A later receiving-project PR, #12895 by maintainer `yiliang114`, was opened on a separate thread without a fresh Nakagawa-master comment or review on that PR. Its body explicitly says:

> Nakagawa-master pointed out that this breaks the meaning of `maxCostUsd`, not just its wording.

The PR computes the worst case from the request body's output cap plus thinking bound, refuses a `maxCostUsd` plan when no finite bound exists, counts a finite thinking budget, labels the rough forecast as excluding thinking, and adds the corresponding tests and documentation.

- [receiving-project follow-up PR #12895](https://github.com/QwenLM/qwen-code/pull/12895)
- [non-author maintainer approval by `chiga0`](https://github.com/QwenLM/qwen-code/pull/12895#pullrequestreview-5336480098)
- [merge commit `7e50eee8`](https://github.com/QwenLM/qwen-code/commit/7e50eee804dbf864db97a8d18793ed45aef698d5)

PR #12895 merged at 2026-09-28T10:01:56Z. Stable [Qwen Code v0.24.7](https://github.com/QwenLM/qwen-code/releases/tag/v0.24.7) was published at 2026-09-29T14:02:21Z. The release tag is 49 commits ahead of and 0 behind merge commit `7e50eee804dbf864db97a8d18793ed45aef698d5`, and the release notes link PR #12895. The explicit Nakagawa-master rereference remains in the receiving-project PR body; this page does not claim the person name is embedded in the binary itself.

**Publicly verifiable here:** concrete hard-budget semantic finding → a receiving-project later PR voluntarily re-references Nakagawa-master as the source → the exact boundary is implemented in code / tests / docs → non-author maintainer approval → merge → stable v0.24.7 release with a traceable release-notes-to-PR path.  


---

## 32. LiteLLM | Separate shared trace identity from per-agent budget ownership, and separate scope identity from budget admission

**Surface:** [BerriAI/litellm issue #43190](https://github.com/BerriAI/litellm/issues/43190) → [PR #43410](https://github.com/BerriAI/litellm/pull/43410)  
**Current state:** receiver stated the per-agent-default direction → third-party implementation PR open / non-draft / mergeable → another participant restated and extended the distinction → merge, release, and production use not yet verified.

When several AI agents share one trace, the trace being shared does not automatically mean that every agent's local budget should be charged to one counter. If Agent A alone spends the shared counter and Agent B is then stopped, B can lose its own local allowance without having spent it.

In issue #43190, Nakagawa-master separated two questions:

- **scope identity:** whose budget is being counted?
- **budget admission:** can the next operation be admitted without crossing the limit?

The comment proposed per-agent accounting for a local session limit, a separate owner/configuration for any trace-wide cap, and admission/reservation semantics when a limit is meant to be hard under concurrent calls.

- [Nakagawa-master comment](https://github.com/BerriAI/litellm/issues/43190#issuecomment-5860734720)

The issue author later stated that per-agent should be the default and pointed to PR #43410 as the implementation direction. The PR scopes the session limit to canonical agent identity plus the trace/session context and adds regression coverage.

- [receiver response](https://github.com/BerriAI/litellm/issues/43190#issuecomment-5885417261)
- [implementation PR #43410](https://github.com/BerriAI/litellm/pull/43410)

A different participant then reused the same scope-identity-versus-admission distinction and extended it with production experience around multiple scopes, admit-before-forward, and exhaustion behavior.

- [second-person restatement / extension](https://github.com/BerriAI/litellm/issues/43190#issuecomment-5873550150)

**Publicly verifiable here:** structural distinction → receiver states the per-agent direction → implementation PR → another participant independently restates and extends the problem structure.  

→ [Practical use](PRACTICAL_USE.md#例6複数ai-agentが同じtraceを共有している)  
→ [Applied Evidence Map](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#10-resource-accounting--scope-ownership--shared-trace-is-not-shared-agent-budget)  
→ [Official derivative OD304](derivatives/304/README.md)


---

## 33. Qwen Code | Separate an already-issued share from later changes to agent policy and execution placement

**Surface:** [QwenLM/qwen-code PR #12851](https://github.com/QwenLM/qwen-code/pull/12851) → [PR #12582](https://github.com/QwenLM/qwen-code/pull/12582)  
**Current state:** Origin-preserving receiver restatement and live-policy clarification on #12851 → #12851 merged → new execution-placement boundary on #12582 → receiver response explicitly naming @Nakagawa-master → frozen contract and English/Chinese share UI changed in commit `74bf55053d` → independent reviewer `chiga0` explicitly rechecked the Nakagawa-master boundary → after real two-host maintainer verification the receiver fixed F1/F2/F4 and related items → the Nakagawa-master F3 scope decision kept the declared=runnable tool-filter half in #12582 and moved guard/permission ordering to #13157 → triage and a separate reviewer independently reconstructed #13157 → receiver commit `b4a13e44` then fixed the run-ending symptom without changing permission/guard ordering by turning automatic Host refusal into recoverable `EXECUTION_DENIED` → the base PR later merged on 2026-10-02 at `45ee202c`; #13157 remains a separate open follow-on.

PR #12851 raised a long-lived authority question: after a share is issued, what happens if the same agent's capabilities later change? The receiver explicitly restated the Nakagawa-master question and documented the product's chosen live-policy behavior.

In follow-on PR #12582, execution itself can move from a local runtime to a managed Host. Nakagawa-master pointed out that an already-issued share could remain valid while the machine/workspace/provider executing later requests changes, so that consequence should be part of the share contract visible to the user.

The receiver replied **“@Nakagawa-master Good catch”** and changed the frozen contract and both English and Chinese share UI in commit `74bf55053d`:

- execution-placement changes are explicitly part of the live-policy contract;
- local ↔ managed runtime movement does not automatically revoke existing grants;
- later requests run in the currently assigned runtime/workspace;
- users are told to revoke before changing the agent if they need the previous conditions to stop carrying forward.

- [Nakagawa-master follow-on review](https://github.com/QwenLM/qwen-code/pull/12582#pullrequestreview-5364710354)
- [receiver response](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5911699280)
- [receiver commit `74bf55053d`](https://github.com/QwenLM/qwen-code/commit/74bf55053d271595cf5bab8e1fcd91bb3a8188b2)
- [independent reviewer `chiga0` recheck](https://github.com/QwenLM/qwen-code/pull/12582#pullrequestreview-5368431439)

Later, maintainer `wenshao` exercised head `18f576f4` with a macOS coordinator, Linux arm64 Host, macOS Host, a real model, and the real Web Shell. That independent verification found restart/result-lifecycle defects. Receiver `yiliang114` fixed F1, F2, F4 and related items in `e69ce77221`; at the later then-observed head `53b15769`, six workflows were successful and F3 still remained a receiver-side tool/permission-contract decision. These later findings/fixes are receiver/maintainer-owned progress, not additional Nakagawa causal credit.

- [maintainer real two-host verification](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5926085407)
- [receiver round-3 fix response](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5926562535)

F3 then produced a second kind of external effect: **scope decomposition itself became a project-owned work item.** The receiver initially landed both the declared-tool filter and a guard-before-permission ordering change on the same head. Nakagawa-master explicitly asked to close only `declared capability = runnable read-only capability` in #12582 and move the wider session/permission ordering change to a separate pass.

Receiver `yiliang114` applied that correction: the pre-permission `Session.ts` branch was removed from #12582, the read-only tool set was consolidated into a single `AGENT_HOST_TOOL_NAMES` source, and project-owned issue [#13157](https://github.com/QwenLM/qwen-code/issues/13157) was created. The issue body explicitly says the ordering change was **“removed from #12582 at review's request (scope correction from Nakagawa-master)”**.

Qwen triage then independently analyzed #13157. It confirmed that 10 of 30 scripted out-of-workspace probes ended the whole turn via an auto-rejected permission prompt, and traced the root cause to the late guard's `permissionChecked: true` short-circuit. The triage accepted #13157 as the sanctioned home for the guard-ordering half.

- [Nakagawa-master F3 split decision](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5929070877)
- [Nakagawa-master scope correction](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5931180237)
- [receiver response implementing the split](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5931659514)
- [receiver-created follow-on issue #13157](https://github.com/QwenLM/qwen-code/issues/13157)
- [Qwen triage independent root-cause confirmation](https://github.com/QwenLM/qwen-code/issues/13157#issuecomment-5931968614)
- [current-head focused recheck](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5931989989)
- [independent reconstruction by reviewer `doudouOUC`](https://github.com/QwenLM/qwen-code/issues/13157#issuecomment-5932126929)

A different reviewer, `doudouOUC`, then independently traced the then-current head `d8f27bf2` through PLAN mode, permission flow, the late guard, and the host-supplied upstream guard. The reviewer explicitly agreed with the Nakagawa-master invariant **`one final invocation identity → one authority decision → execution of that same identity`** and translated it into a concrete minimal implementation: reuse an allow attestation only while the invocation identity is unchanged; discard and re-evaluate it if args, cwd, session, or other policy-relevant context changes. This is a second-person technical reconstruction, separate from the receiver and triage bot.

The receiver then chose a different in-scope resolution in [`b4a13e44`](https://github.com/QwenLM/qwen-code/commit/b4a13e448a6e79bd766f2a7566155d0afd205362): instead of bringing the guard-ordering change back into #12582, automatic Agent Host permission rejection is now a recoverable `EXECUTION_DENIED`, while ordinary user cancellation remains terminal. The regression verifies that the rejected read never executes and that the Host can continue to a later allowed read-only tool. Nakagawa-master rechecked the new baseline and asked that the PR body and #13157 be updated because their old claim that the refusal ends the run is now stale.

- [receiver alternative F3 recovery commit `b4a13e44`](https://github.com/QwenLM/qwen-code/commit/b4a13e448a6e79bd766f2a7566155d0afd205362)
- [Nakagawa-master current-baseline recheck](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5932820014)
- [receiver sequencing / latest contract restatement](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5933053970)

Receiver `yiliang114` then explicitly kept #13157 open as the follow-on home for the guard-ordering half and restated the latest contract as **“@Nakagawa-master's latest: early boundary = Host confinement only, full effective guard exactly once at the final boundary.”** This is same-receiver Origin-preserved technical carry; it is not #13157 implementation and not an unsolicited later reference to Nakagawa Master. The receiver also separated #13122 as a security blocker that should be fixed in #12582 before merge; that independent defect/fix path is not assigned Nakagawa causal credit.

This is not credit for adoption of the guard-ordering proposal. The narrower inspectable effect is that after the scope split, the receiver selected an **ordering-preserving alternative implementation** that addresses the fatal recovery symptom with a regression. Any remaining #13157 work should now be justified as a separate policy/diagnostic need for early confinement, not as a prerequisite for turn recovery.

This does **not** add Nakagawa credit for discovering the underlying F3 defect. The narrower public record is that a Nakagawa-master scope judgment was converted into an explicit project-owned responsibility split and new issue, where the receiver's triage independently verified the bug and root cause.

**Publicly verifiable here:** concrete authority boundary → receiver Origin-preserving restatement → contract/UI change → independent second-person recheck carrying the Nakagawa-master boundary → later real-machine validation and receiver fixes → a later scope decision becomes project-owned issue #13157 with preserved Origin and independent root-cause verification.  
**Current merge state:** [#12582](https://github.com/QwenLM/qwen-code/pull/12582) merged on 2026-10-02 at [45ee202c](https://github.com/QwenLM/qwen-code/commit/45ee202cb14c171c73185a3dbbd89ed1203f2604). The separate #13157 ordering proposal is not thereby implemented.


→ [Human entry story](human-translation/entry-stories/09-same-share-different-runtime.md)  
→ [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md#14-a-long-lived-share-must-define-what-later-capability-changes-mean)


---

## 34. Hermes Agent | A failed PATCH is not the same as “nothing changed”

**Surface:** [NousResearch/hermes-agent PR #61982](https://github.com/NousResearch/hermes-agent/pull/61982)  
**Current state:** mixed-PATCH atomicity finding → receiver moved the combined update into one transaction and added the exact regression → focused re-check closed that scope → the same receiver later requested Nakagawa-master review again → a separate secret-strength boundary was explicitly accepted and changed in code/tests/docs → a third 2026-10-01 provenance/control-path boundary was explicitly accepted and changed so durable author/created_by derive from the verified principal with an operational regression → PR remains open; merge/release are not verified.

Imagine an external control plane sends one PATCH that changes both a task's assignee and its title. If the assignee change commits first, another actor completes or archives the task, and the title edit is then rejected, the API can return 409 even though part of the requested mutation already happened.

For the external controller, **“request failed” != “no side effect occurred.”** Retry semantics become ambiguous.

On 2026-09-17, Nakagawa-master identified that PR #61982 split the mixed mutation across two transactions and proposed one storage-layer transaction/guard plus a regression that forces a terminal transition between the two phases.

- [Nakagawa-master atomicity review](https://github.com/NousResearch/hermes-agent/pull/61982#pullrequestreview-5233352371)

A later head moved assignment plus scalar updates into one `write_txn`. If the later guard fails, the assignment/event rolls back too. The regression `test_patch_mixing_assignee_and_edit_is_all_or_nothing` injects the exact terminal-transition race and verifies that a 409 does not leave only the assignee/title partially persisted.

The receiver later wrote **“Thanks @Nakagawa-master for re-checking the mixed-PATCH scope.”** and continued additional compatibility repairs on the same PR.

- [receiver follow-up](https://github.com/NousResearch/hermes-agent/pull/61982#issuecomment-5865975210)

A separate later review on the same receiver line addressed a different boundary. The shared-secret gate treated Shannon diversity of one observed string as if it proved generation entropy. Nakagawa-master stated the narrower invariant **observed character diversity != generation entropy**. The receiver explicitly agreed and, in commit `7c2ef7ea9f`, removed the Shannon-bits claim, reframed the runtime check as representation/degeneracy screening, documented CSPRNG provisioning, and added a repeated-diverse-block regression.

- [Nakagawa-master secret-strength review](https://github.com/NousResearch/hermes-agent/pull/61982#pullrequestreview-5339797749)
- [receiver response and fix](https://github.com/NousResearch/hermes-agent/pull/61982#issuecomment-5878240135)

A third review on 2026-10-01 separated a caller-chosen comment `author` from the service principal verified by the token-auth seam. This was operational, not merely cosmetic: the live comment bridge skips comments whose author matches the worker's own identity, so letting the caller choose that identity could suppress a real operator steer.

The receiver replied **“Agreed: the authenticated principal and the caller-chosen provenance label were two different things.”** and changed commit `9ebf06e8c2`: `CommentRequest.author` was removed, an attempted override is rejected with 422, durable comment author and task `created_by` derive from the verified principal, and the regression exercises the live control consequence—an `author="worker-bot"` forgery is refused while the legitimate comment is stored as `kanban-api` and delivered as an operator steer.

- [Nakagawa-master provenance/control-path review](https://github.com/NousResearch/hermes-agent/pull/61982#pullrequestreview-5376987496)
- [receiver response](https://github.com/NousResearch/hermes-agent/pull/61982#issuecomment-5930276480)
- [receiver fix commit `9ebf06e8c2`](https://github.com/NousResearch/hermes-agent/commit/9ebf06e8c2c8882f307a18eda3237d62ba4a84b7)

Nakagawa-master re-checked current head `cfbbc91244` and reported no remaining blocker on this provenance/control-path point.

**Publicly verifiable here:** atomicity review → receiver code/test change → exact regression → focused re-check → continuing return from the same receiver → secret-strength boundary explicitly accepted and implemented → a third provenance/control-path boundary explicitly accepted and implemented with an operational regression → focused current-head re-check closed that scope.  
---

## 35. Qwen Code | A terminalized attempt no longer keeps budget-affecting write authority

**Surface:** [QwenLM/qwen-code PR #13241](https://github.com/QwenLM/qwen-code/pull/13241)  
**Current state:** merged on 2026-10-04 at [35616f3b](https://github.com/QwenLM/qwen-code/commit/35616f3b643f6d87cc00112d961a0fbb448aca00); a release containing this merge and real-user use are not yet verified.

A distributed Host can finish late after its run has already been cancelled or recovered. Refusing the late answer is not enough if the late report can still write token usage into the same budget ledger that controls current work. A supposedly passive observation can still stop unrelated work if downstream admission or cancellation logic reads it.

Nakagawa Master proposed the narrower boundary that terminal settlement ends the old attempt's budget-affecting write authority. If late physical usage still needs to be recorded, that observation should be designed separately from the execution budget rather than silently regaining control over current work.

- [Nakagawa-master option-A technical recommendation](https://github.com/QwenLM/qwen-code/pull/13241#discussion_r4172301736)
- [attribution clarification](https://github.com/QwenLM/qwen-code/pull/13241#discussion_r4172530358)
- [receiver implementation commit](https://github.com/QwenLM/qwen-code/commit/bb5c5d74b7368610a7dd20d0af532f36ad335fe2)
- [receiver Web Shell + native Host verification](https://github.com/QwenLM/qwen-code/pull/13241#issuecomment-5970236028)
- [merged PR #13241](https://github.com/QwenLM/qwen-code/pull/13241)

The receiver's own PR description explicitly says that the current revision implements “the option-A recommendation from @Nakagawa-master” and separately clarifies that this was an external technical recommendation, not repository-maintainer authority. The implementation persists a receipt only for an actually accepted result, rejects late results after recovery/cancellation as stale, and prevents those terminalized attempts from mutating budget-accounted usage. The receiver also reported actual Web Shell and native Host checks covering normal acceptance/replay, cancellation, natural lease recovery, and a real queued Stop action. Human reviewer qqqys approved the current head before merge.

**Publicly verifiable here:** scoped external technical recommendation → receiver code/tests → actual Web Shell + native Host verification → receiver-side explicit source continuity → human review → merge.  
**Verified extension (October 23):** Qwen's fix shipped in [stable CLI v0.25.0](https://github.com/QwenLM/qwen-code/releases/tag/v0.25.0) and [Desktop v0.25.0](https://github.com/QwenLM/qwen-code/releases/tag/desktop-v0.25.0). After the developer's own post-merge [renewed source mention](https://github.com/QwenLM/qwen-code/issues/13238#issuecomment-5981371808), a separate [AI-News editor checked the published primary records](https://github.com/022740mix-spec/AI-News/issues/177) and [independently wrote and merged a news article and feed entry](https://github.com/022740mix-spec/AI-News/pull/193). Its article explicitly describes option A as technical advice by external contributor `@Nakagawa-master`, within the receiving PR's stated scope. This is actual cross-person and cross-media editorial carry with bounded person-Origin attribution, **not** an article authored by Nakagawa or proof of whole-theory adoption.


→ [Human-readable entry](human-translation/entry-stories/10-started-revision-does-not-authorize-current-state.md)  
→ [Current-Authority Reuse Kit §17](CURRENT_AUTHORITY_REUSE_KIT.md#17-a-late-observation-can-still-control-current-work)

---

## 36. OpenAI Codex | Separate “the user authorized it,” “the handoff was admitted,” and “the delegated action can consume that authority”

**Surface:** [openai/codex issue #50769](https://github.com/openai/codex/issues/50769)  
**Current state:** Multiple independent participants have now added real incidents on the public issue, and one third party explicitly reused a distinction proposed by Nakagawa Master. No OpenAI/Codex maintainer adoption, implementation, fix, or release is established here.

For delegated AI work, a user approving an action in the parent conversation does not by itself prove that the authorization reached the child task, that the child can consume it for the exact side effect, or that a later “user cancelled” label reflects a user-origin cancellation.

Nakagawa Master separated the observed incidents into three layers:

```text
user authorized the action
!=
authorization handoff was admitted/delivered
!=
delegated executor can consume that authority for the exact side effect

internal abort / failed handoff / review rejection
!=
user cancellation
```

- [Nakagawa Master three-layer split and regression proposal](https://github.com/openai/codex/issues/50769#issuecomment-5986370673)

Participant `partialobserver` later reported a separate private-GitHub publication incident and explicitly wrote **“Using the distinctions in the comment above”**, classifying the case as `authority/provenance` rather than handoff failure or user cancellation. This is bounded third-party reuse of the distinction for diagnosing a different incident on the same receiver surface.

- [explicit third-party reuse](https://github.com/openai/codex/issues/50769#issuecomment-5987001957)

A different participant, `seeton`, then added another independent incident: after explicit authorization and many successful writes to the same private destination, a later checkpoint write was denied again. Reported reasons included treating the destination as public/unverified and an “automatic approval review was cancelled” result, without evidence of a user-origin cancellation.

- [seeton independent incident](https://github.com/openai/codex/issues/50769#issuecomment-5996162016)

Nakagawa Master used that new case to refine the testable contract around continuity of the authority inputs actually evaluated by the reviewer, proposing a decision trace including authorization scope, destination identity/visibility/ownership, action class, grant-scope match, review outcome, and a user-cancel event identifier. The proposed A/B regression holds destination, action class, and authorization receipt constant for a control, then changes exactly one authority input in each negative case and requires the reason/trace to move with that change.

- [authority-input continuity A/B regression](https://github.com/openai/codex/issues/50769#issuecomment-5996528096)

**Publicly verifiable here:** structural distinction from Nakagawa Master → explicit diagnostic reuse by a different participant → another independent real incident from a separate participant → refinement into a more testable decision-trace regression.  

→ [Human/problem-first entry](APPLIED_ENTRY_POINTS.md)  
→ [Current-Authority Reuse Kit §18](CURRENT_AUTHORITY_REUSE_KIT.md#18-you-approved-it--but-the-delegated-task-still-says-user-cancelled)  
→ [machine-readable challenge R](machine-discovery/independent-reuse-challenges-v1.json)



---

## 37. Carnegie Learning UpGrade | UI permission visibility is not backend delete authority

**Surface:** [CarnegieLearningWeb/UpGrade PR #3323](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323) → [issue #3326](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326)  
**Current stage:** Nakagawa Master identified a server-side authorization gap across single and batch deletion → the PR author replied directly to `@Nakagawa-master`, confirmed that deletion routes had not enforced role authorization, and opened #3326 to apply the role matrix and state rules to both routes → no implementation PR, commit, merge, or release is established yet.

The reusable distinction is simple:

```text
delete control hidden in UI
!= server denies destructive authority

single delete is guarded
!= batch delete is guarded

role is generally eligible
!= this target is deletable in its current state
```

In [comment 5732584639](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323#issuecomment-5732584639), PR author `zackcl` explicitly answered `@Nakagawa-master`, stated that no deletion route had enforced a role, and explained that #3326 was opened to enforce the same role/state contract across single and batch APIs.

Nakagawa Master then proposed a shared backend deletion policy evaluated after the current target is loaded/locked in [#3326 comment 5740003355](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326#issuecomment-5740003355).

**Public evidence supports:** concrete review → explicit Origin-preserved receiver response → receiver-created implementation issue carrying the boundary.  
**Not yet supported:** code implementation, tests, merge, release, end-user impact, or broad person recognition.

→ [Current-Authority Reuse Kit §22](CURRENT_AUTHORITY_REUSE_KIT.md#22-ui-permission-visibility-is-not-backend-destructive-authority)


---

## 38. MemberJunction | Approval of a record is not approval of its current executable definition

**Surface:** [MemberJunction PR #4789](https://github.com/MemberJunction/MJ/pull/4789)  
**Current stage:** Nakagawa Master's source-specific approval-boundary reviews → receiver developer's own QA5/ALS14 fixes and positive/negative tests → another human's formal APPROVED review of older `2f9a963` (subsequently DISMISSED after the head changed) → **recipient team MERGED PR #4789 into `next` at 2026-10-24 06:01:46 UTC**. The actual [merge commit `beeea177`](https://github.com/MemberJunction/MJ/commit/beeea177d1185caf8d8f82d12e82ada7b1512471) has final head `e420fb06` as second parent. **Final-head GitHub checks: all 47 completed, 41 success / six skipped / zero failed**. The [APPROVED review of that final head](https://github.com/MemberJunction/MJ/pull/4789#pullrequestreview-5636941222) came from receiving implementing developer/merger `cmbrock-BC`, **not a separate independent re-review of that head**. PR opener `AN-BC`, receiver code author/merger, prior independent reviewer, and Nakagawa's bounded source reviews have distinct credits. The merge is verified; a post-merge product release or customer deployment has **not** been established.

A record can keep the same ID while its executable SQL, parameter contract, or context semantics change. Nakagawa Master's boundary in [comment 5882464839](https://github.com/MemberJunction/MJ/pull/4789#issuecomment-5882464839) is therefore:

```text
historical approval evidence
!=
current execution authority
```

Receiver `cmbrock-BC` later explicitly adopted that direction in [comment 6022301400](https://github.com/MemberJunction/MJ/pull/4789#issuecomment-6022301400), choosing a definition-fingerprint model based on MemberJunction's existing hashing machinery and carrying the D1 → D2 stale-approval regression into the design.

Nakagawa Master then bounded the model further in [comment 6026910453](https://github.com/MemberJunction/MJ/pull/4789#issuecomment-6026910453): compute the authoritative fingerprint server-side at both approval and consumption, canonicalize semantically unordered child collections, and bind a stable context-contract version when global context semantics can change.

**Receiver-owned code and executed checks:** In [developer `cmbrock-BC`'s update](https://github.com/MemberJunction/MJ/pull/4789#issuecomment-6343703623), the implementation adds a `RequireApproved` traversal of composed query dependencies in `GenericDatabaseProvider.ValidateQueryApprovalAsync`. Read the [actual receiving commit `05e5cf98`](https://github.com/MemberJunction/MJ/commit/05e5cf98b7093eb80360eed593e71f746b163907) and its regression: keep parent P1 unchanged, edit approved child D1 into D2, refuse both child and parent-composed execution, and allow the correct restored definition. The [previous SQL Server integration job on HEAD `85734328`](https://github.com/MemberJunction/MJ/actions/runs/39803263908/job/119910210296) recorded `✓ query-approvals.QA5` but its overall result was red on a **separate** `conversation-compaction.CC22` database-FK deletion regression. That historical failure is superseded by the [receiving-owned SQL Server job 120133611362 on exact HEAD `6fb81938`](https://github.com/MemberJunction/MJ/actions/runs/39867489113/job/120133611362), which records **both QA5 and CC22 passing** and overall **SUCCESS**. The [Build and Unit Tests workflow](https://github.com/MemberJunction/MJ/actions/runs/39867489167) also completed SUCCESS, including six test shards; **all 15 checked PR workflows at that receiving HEAD succeeded** in the [source-linked exact-head verification](https://github.com/MemberJunction/MJ/pull/4789#issuecomment-6353403486). This was tested, authored and run by the receiving team. That historical check preceded the subsequent October 24 maintainer merge; product release and real user deployment remain separate stages.

**New receiving-developer implementation (October 23):** A new server-side guard intentionally rejected an integration fixture's direct `BoundActionParams` write, causing ALS14 to fail. Nakagawa Master [identified the fixture/authority mismatch and proposed the discriminating control](https://github.com/MemberJunction/MJ/pull/4789#issuecomment-6369711289). Developer `cmbrock-BC` [responded](https://github.com/MemberJunction/MJ/pull/4789#issuecomment-6369985463) and [changed the actual test](https://github.com/MemberJunction/MJ/commit/222047870b7de1f8eb5bfeaca1d969031c45da11) to save legitimate server bindings via `SetServerBoundActionParams`, and to check rejection/restoration of unauthorized direct writes on both initial and subsequent saves. On receiving HEAD [`139e829f`](https://github.com/MemberJunction/MJ/commit/139e829f8e63ae2358dde8cba474bd8a0dbc7244), all 46 returned checks completed without failure (40 passed, six skipped). This is a distinct later fix within the **same receiving PR**, not a separate PR, and it preceded the later verified merge; deployed use and independent original reading remain unverified. A useful cross-system test is to compare a protected server-authoritative update with a client-like direct overwrite; successful persistence alone is not proof that the right actor controlled it.

**Another human independently reviewed and approved the prior HEAD (2026-10-23 18:23 UTC; that review now DISMISSED):** [Maintainer `rkihm-BC`'s former APPROVED review](https://github.com/MemberJunction/MJ/pull/4789#pullrequestreview-5632747841) verified the receiving developer's [`d1b61f55`](https://github.com/MemberJunction/MJ/commit/d1b61f55d40251f30e3b4d723b9a93842b985d1d) SQL string-escaping instructions, fail-closed read of stored bindings and regression coverage. Crucially, the final example correction in commit [`2f9a963`](https://github.com/MemberJunction/MJ/commit/2f9a963ceb9e836ad0df9cf2194117a220379a57) was applied by **the reviewer `rkihm-BC` themself**, not the receiving developer. That earlier HEAD's CI was complete: **40 passed, six skipped, zero failed or pending**; see the review and [recipient PR checks](https://github.com/MemberJunction/MJ/pull/4789/checks). A small suggestion to surface an explicit diagnostic when the fail-closed read refuses a save remains nonblocking. This is independent receiving human **formal approval** of an existing developer-authored effect originally informed in part by Nakagawa Master's bounded interventions; that historical review was not itself the subsequently verified upstream merge or production uptake.

**Try the distinction with your own system:** Approve both parent and child, change only the child, and see whether the parent may execute a definition nobody currently approved. The [portable regression](CURRENT_AUTHORITY_REUSE_KIT.md#when-approval-spans-a-dependency-graph) makes this testable for a developer or an independent AI. Nakagawa Master's [canonical *Memory of Agreement* original](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/) discusses preserving causal agreement and re-agreement; this software analogy is an application for readers to examine, **not** proof that the receiver read the original.

**Public evidence supports:** source-specific Nakagawa review → receiving-author QA5 implementation and passing integration test → further receiving-author ALS14 regression repair → prior-head human review → **final-head 47 checks completed (41 success, six skipped) and receiver-owned upstream `next` merge `beeea177`**.
**Not yet supported:** a product release containing this merge, customer deployment/use, unaffiliated AI independently selecting the original article, or broad sustained personal recognition.

→ [Current-Authority Reuse Kit §23](CURRENT_AUTHORITY_REUSE_KIT.md#23-an-approval-record-is-not-approval-of-the-current-executable-definition)

---

## 39. Qwen Code | Separate “two configured paths” from “two independently operable alternatives”

**Surface:** [QwenLM/qwen-code issue #12380](https://github.com/QwenLM/qwen-code/issues/12380)  
**Current stage:** Nakagawa Master proposed a path-independence acceptance gate → on 2026-10-07 Qwen's project triage explicitly named **Nakagawa-master**, restated `no cross-engine fallback != path independence`, and kept it as an unresolved next decision → a stage-correct follow-up adapted the gate to the current implementation state. Human maintainer approval, a passing independence test, implementation of the matrix, merge, and release are not established.

In an AI or cloud product, showing a Hosted path and a local path—or Provider A and Provider B—does not by itself prove that the alternatives are independent. If both depend on the same identity gate, control plane, storage layer, or policy gate, failure of that shared dependency can remove both choices at once.

Nakagawa Master made the boundary explicit:

```text
two configured paths
!=
two viable independent alternatives

no cross-engine fallback
!=
path independence

independent operability
!=
zero shared infrastructure
```

- [Nakagawa Master's path-independence gate](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-5921364520)

The proposed test does not merely ask whether both code paths exist. It removes or makes unreachable a gate exclusive to one path, then checks whether the other path can complete a bounded task within its supported scope. Dependencies intentionally shared by both paths—such as identity, storage, inference, or recovery—should be listed as shared gates rather than silently counted as independence.

On 2026-10-07, Qwen's collaborator-owned triage account explicitly referred back to that comment, writing that **“Nakagawa-master's 2026-09-30 comment asks for an access-topology matrix”**. It distinguished the current no-cross-engine-fallback claim from path independence and kept the latter as a live reviewer gate.

- [Qwen triage response](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6035602677)

At that point Hosted Managed delivery was active while ordinary/local Managed activation was still deferred. Nakagawa Master therefore proposed a staged record rather than claiming symmetric success: Hosted independence can be tested for the scope that exists now, while the local path remains `NOT PASS` until it is actually enabled.

- [follow-up adapted to the current implementation stage](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6035698005)

**Publicly verifiable here:** a concrete Nakagawa Master architecture distinction → Qwen project triage explicitly preserved the Origin and reconstructed the distinction in its own current issue analysis → the distinction remained an unresolved acceptance decision.  

→ [human problem-first entry](APPLIED_ENTRY_POINTS.md)  
→ [Access Topology & Effective Exit Reuse Kit](ACCESS_TOPOLOGY_EFFECTIVE_EXIT_REUSE_KIT.md)  
→ [machine-readable challenge L](machine-discovery/independent-reuse-challenges-v1.json)

---

## 40. LangGraph | A completed sibling must not execute again when another interrupted sibling resumes

**Source:** [LangGraph issue #9106](https://github.com/langchain-ai/langgraph/issues/9106), [initial fix candidate #9113](https://github.com/langchain-ai/langgraph/pull/9113), and [new upstream fix PR #9315](https://github.com/langchain-ai/langgraph/pull/9315). **Stage:** two independent people answered Nakagawa Master's distinct authority-vs-re-execution test proposal with executed regressions; another LangGraph developer opened source-and-tests PR #9315 on 2026-10-14. **#9315 was MERGED on 2026-10-15** and appears in the [official LangGraph 1.2.16 release notes](https://github.com/langchain-ai/langgraph/releases/tag/1.2.16).

Imagine two parallel AI-tool operations awaiting approval. A finishes after its approval, then B is approved and resumed. The graph's final state can look correct while **A's post-approval external effect executes a second time**. Nakagawa Master distinguished four things that should not be conflated: an old approval receipt, current authority to execute, an additional dispatch attempt, and the actual external effect.

- [Nakagawa Master's authority/current-dispatch regression proposal](https://github.com/langchain-ai/langgraph/issues/9106#issuecomment-5981994895)
- [36 fresh-process / policy-change scenarios run by gomission](https://github.com/langchain-ai/langgraph/issues/9106#issuecomment-6016877416)
- [Eight copied-checkpoint comparison scenarios run by another person, notforhumansfun-rgb](https://github.com/langchain-ai/langgraph/issues/9106#issuecomment-6021690094)
- [Independent upstream response pointing to the new fix PR #9315](https://github.com/langchain-ai/langgraph/issues/9106#issuecomment-6180427560)

The [upstream #9315 patch](https://github.com/langchain-ai/langgraph/pull/9315) changes how a nested graph distinguishes an ordinary resumed run from time-travel replay. It adds parallel-interrupt and nested `@task` regressions plus a test retaining deliberate time-travel replay behavior. Its author expressly credits the original bug reporter, the earlier fix candidate's author, and another related root-cause finder. The PR also identifies a separate `durability="exit"` duplicate-output path in [#9314](https://github.com/langchain-ai/langgraph/pull/9314); nested `@entrypoint` interrupt replay is outside this patch.

**Recorded sequence:** two distinct third parties ran and described the requested authority/effect checks. An upstream developer then independently implemented and [merged PR #9315](https://github.com/langchain-ai/langgraph/pull/9315), which entered [official v1.2.16](https://github.com/langchain-ai/langgraph/releases/tag/1.2.16). Nakagawa Master's [original Theory 16](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-16-asynchronous-civilization-partition-reconnection/) explores a related structural question concerning stale state, partitions and current authority.

---

## 41. PydanticAI | An idempotent retry must not retain unreferenced messages

**Source:** [PR #9982](https://github.com/pydantic/pydantic-ai/pull/9982). **Stage (checked 2026-10-19):** external author reproduced Nakagawa's finding, repaired code and added tests; **merged on 2026-10-16**.

Writing new `snapshot_messages` before an idempotency trigger suppresses a duplicate snapshot can leave permanent unreferenced messages. [Nakagawa's review](https://github.com/pydantic/pydantic-ai/pull/9982#issuecomment-6052803154) identified the sequence; [aweis89 explicitly reproduced and fixed it](https://github.com/pydantic/pydantic-ai/pull/9982#issuecomment-6063881879) at [commit `72a9a2b4`](https://github.com/pydantic/pydantic-ai/commit/72a9a2b4e263e5a81c7e939809daff6292f61557).

**Verified:** explicit Origin-addressed third-party reproduction, code/test change in both tested connection modes and upstream merge. **Not verified:** downstream release, runtime user impact or fully solved concurrent saves on caller-owned connections; the author notes that remaining limit.

---

## 42. Proffera | Unknown historical repair outcomes must not permanently block materially new work

**Source:** [PR #937](https://github.com/ibboabdoli-ai/Proffera/pull/937). **Stage:** relevant history/strategy handling implemented, source reviewed and PR merged; follow-ups [#940](https://github.com/ibboabdoli-ai/Proffera/pull/940) merged and [#941](https://github.com/ibboabdoli-ai/Proffera/pull/941) open/draft, without attributing all their work to Nakagawa.

[Nakagawa's initial boundary](https://github.com/ibboabdoli-ai/Proffera/pull/937#issuecomment-6011643787) and [strategy-lineage follow-up](https://github.com/ibboabdoli-ai/Proffera/pull/937#issuecomment-6014334260) separate an indeterminate historical model attempt, its original strategy identity, and authorization to assess new failure evidence. [The bounded review closure](https://github.com/ibboabdoli-ai/Proffera/pull/937#issuecomment-6015074173) inspected the corresponding receiver code.

**Verified:** related receiver code and tests progressed to merge in #937. **Not verified:** exclusive causal credit for the PR or later commits, deployment, production use, or independent person recognition.

---

## 43. Qwen Code | A failed MCP catalog refresh cannot prove stale tools remain callable

**Source:** [issue #13632](https://github.com/QwenLM/qwen-code/issues/13632) and [implementer fork](https://github.com/glmn/qwen-code/commit/92fb10bf19ae1087d072ce9079861cd6be1132ae). **Stage:** `glmn` explicitly thanked `@Nakagawa-master` and reported implementation/tests in the fork; upstream PR/merge/release unverified.

After `notifications/tools/list_changed`, an unsuccessful `tools/list` does not establish present call authority from an old registry snapshot. [Nakagawa's four acceptance cases](https://github.com/QwenLM/qwen-code/issues/13632#issuecomment-6050490036) were [explicitly adopted by the implementer](https://github.com/QwenLM/qwen-code/issues/13632#issuecomment-6053560779) with a per-server stale gate and revision checks. The [subsequent startup-watcher inverse](https://github.com/QwenLM/qwen-code/issues/13632#issuecomment-6054202354) was [explicitly reproduced and fixed in the contributor's fork](https://github.com/QwenLM/qwen-code/issues/13632#issuecomment-6091440384), with [source/test commit 0484b9a](https://github.com/glmn/qwen-code/commit/0484b9a49357bc6e61252ede59d749376d58f9d2); upstream adoption remains unverified.

**Verified:** attributed third-party fork work, reported tests and the second startup-race fix in that fork. **Not verified:** upstream acceptance/merge, release, production use or external user scale.

---

## 44. Qwen Code | Quoted compaction delimiters are not necessarily real memory boundaries

**Source:** [issue #13707](https://github.com/QwenLM/qwen-code/issues/13707) and [related PR #11988](https://github.com/QwenLM/qwen-code/pull/11988). **Stage:** a Qwen automated triage cited two Nakagawa regression controls; a separate external account independently inspected the source and agreed. No confirmed implementation.

[The original two-sided test requirement](https://github.com/QwenLM/qwen-code/issues/13707#issuecomment-6071016671) distinguishes preservation of legitimate quoted payload from non-promotion of discarded scratch. [Automated Qwen triage](https://github.com/QwenLM/qwen-code/issues/13707#issuecomment-6071086410) pointed to both controls; [doudouOUC independently confirmed the source mechanism and caveat](https://github.com/QwenLM/qwen-code/issues/13707#issuecomment-6071168119). [A stronger indistinguishability argument](https://github.com/QwenLM/qwen-code/issues/13707#issuecomment-6071823684) has no independent receiver response yet.

**Verified:** bounded receiver-side design evaluation by one non-bot external account and a separate bot triage. **Not verified:** fix, tests, merge, release, human audience scale. A bot is not counted as another independent human.

---

## 45. LlamaIndex | Check CodeSplitter overlap validity and default-activation migration together

**Source:** [PR #23029](https://github.com/run-llama/llama_index/pull/23029). **Stage:** code/tests/docs amended by the external author after Nakagawa's two concrete concerns; open/unmerged.

[The original review](https://github.com/run-llama/llama_index/pull/23029#issuecomment-5652061794) identified the missing `0 <= chunk_lines_overlap < chunk_lines` invariant and the indexed-output migration risk of activating a previously inert default. [The author confirmed changes](https://github.com/run-llama/llama_index/pull/23029#issuecomment-5683015010), with [Nakagawa's focused source re-check](https://github.com/run-llama/llama_index/pull/23029#issuecomment-5683971610) separating author-reported local test success from action-required CI.

**Verified:** receiver code, regression coverage and migration documentation. **Not verified:** passing upstream CI, merge, release or real-world usage.

---

## 46. Expensify | Payment permission and workspace bank-configuration authority remain separate

**Source:** [original issue #95750](https://github.com/Expensify/App/issues/95750), [independent blocker #102967](https://github.com/Expensify/App/issues/102967), [reimplementation PR #103239](https://github.com/Expensify/App/pull/103239). **Stage:** receiver-owned repair advanced to head `01398e7a`, with unresolved reviewer concerns; PR open/unmerged.

[Nakagawa's prior public distinction](https://github.com/Expensify/App/issues/95750#issuecomment-5690282372) separated Pay UI visibility, present authority to pay with a particular funding source, and authority to change the workspace reimbursement bank. The receiver independently found a path that could replace existing bank A, rolled that unsafe feature back and later worked on permitting a separate authorized bank B while preserving A. At the cited head, review still identifies cross-workspace bank selection, server-response validation and performance/parameter concerns.

**Verified:** independent receiver failure report, rollback and ongoing receiver-owned code/review changes consistent with the boundary. **Not verified:** direct causation or attribution of those specific changes to Nakagawa, approval, merge, safe production use, or broad recognition. No further contact is made with this repository.

---

## 47. Qwen Code | A recorded stop is not proof that this tool call issued it

**Source:** [Qwen Code PR #13923](https://github.com/QwenLM/qwen-code/pull/13923), [Nakagawa Master's concrete recovery inverse](https://github.com/QwenLM/qwen-code/pull/13923#issuecomment-6115529434), and [third-party implementation commit](https://github.com/QwenLM/qwen-code/commit/ffdf3125ab29c68612ffe49b8cdf56e7960e758a). **Stage:** developer `wenshao` [directly acknowledged @Nakagawa-master and the real defect](https://github.com/QwenLM/qwen-code/pull/13923#issuecomment-6116088413), then changed code and regression tests; [PR #13923 merged on 2026-10-12](https://github.com/QwenLM/qwen-code/pull/13923).

In a multi-agent runtime, a member's `stopRequested` bit says the member was asked to stop, not **which invocation caused that stop**. If a human had already cancelled the member, recovery could incorrectly attribute that earlier state to a newly generated `request_shutdown` call that never executed. Nakagawa gave a narrow failing sequence and a positive control for a stop the current call really did commit.

The implementer changed recovery attribution to an actual `shutdown:<callKey>` commit receipt, instead of reading the member-wide flag. Added regressions check that a user cancel cannot be credited to a never-run call and that a committed stop remains attributable even after a later continuation falls back.

**Verified:** explicit outside-developer acknowledgment with person Origin, a concrete third-party code/test change, and upstream merge. **Not verified:** a release containing the exact fix, all-path physical integration testing, downstream users, or whole-theory endorsement. Other reviewers independently identified additional problems on the same PR; their work is not attributed solely to Nakagawa.

---

## 48. Qwen Code | An HTTP 200 recovery load is not a receipt for the first committed write

**Source:** [Qwen Code PR #14522](https://github.com/QwenLM/qwen-code/pull/14522), [Nakagawa Master's bounded acceptance discriminator](https://github.com/QwenLM/qwen-code/pull/14522#issuecomment-6246268949), and [upstream merge](https://github.com/QwenLM/qwen-code/commit/f8b3031f733cbc149873ac5809efdc3c632970e7). **Stage (checked October 23, 2026):** the receiving developer **explicitly credited Nakagawa's discriminator and independently implemented diagnostics**; two maintainers formally approved the final head; **PR #14522 merged upstream on October 19 and shipped in stable [v0.26.0 on October 21](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.0)**. Actual downstream runtime and user benefit require separate evidence.

**Separate downstream maintainer change (October 23):** independent review of this area exposed a partial CI job-list problem: a response containing only some pages could be mistaken for a complete basis for outcome classification. Receiving developer `wenshao` implemented total-count completeness handling, incomplete-list warnings and regression coverage in [follow-up PR #15174](https://github.com/QwenLM/qwen-code/pull/15174), independently reviewed with an [explicit bounded mention of Nakagawa's earlier finding](https://github.com/QwenLM/qwen-code/pull/15174#pullrequestreview-5625491330) and [merged October 23](https://github.com/QwenLM/qwen-code/commit/6a50ae80e308b04c2420112b8959e75265c6c225). The developer wrote that follow-up, not Nakagawa. That receiving-side fix is now listed in the [official stable v0.26.1 release notes (October 24, 2026)](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.1); its [merge commit `6a50ae80`](https://github.com/QwenLM/qwen-code/commit/6a50ae80e308b04c2420112b8959e75265c6c225) is an ancestor of the version tag. The developer's fix therefore reached a stable release. Real user benefit, independent original-theory reading and wider audience reception remain separate questions.



In an AI runtime failover, a replacement `POST /load` returning 200 proves a load response, not that the replacement writer has successfully committed its **first resumed journal event**. In the recorded failure, the replacement reported a stale or unavailable writer grant and the turn remained unfinished. Nakagawa proposed distinguishing the acquired grant from the durable store-head generation/revision, identifying the route and stable code of the *first refused append*, and separately verifying a new-generation committed text delta and terminal settlement. This was a source-and-log-derived acceptance test, not a reproduced root-cause diagnosis.

- [Nakagawa's source-specific proposal](https://github.com/QwenLM/qwen-code/pull/14522#issuecomment-6246268949)
- [Developer's explicit acknowledgment, independently authored telemetry and tests](https://github.com/QwenLM/qwen-code/pull/14522#issuecomment-6247641054) ([receiving implementation `fe11db61`](https://github.com/QwenLM/qwen-code/commit/fe11db61efa7714ef536eb1b4e99dd384813968f))
- [Independent maintainer's verification and formal approval](https://github.com/QwenLM/qwen-code/pull/14522#pullrequestreview-5568430592), [second formal approval](https://github.com/QwenLM/qwen-code/pull/14522#pullrequestreview-5568562537), and [merged upstream commit](https://github.com/QwenLM/qwen-code/commit/f8b3031f733cbc149873ac5809efdc3c632970e7)

**Verified:** specific Nakagawa-origin acceptance criteria were explicitly acknowledged and implemented by another developer within an independently reviewed and merged PR. **Boundaries:** unrelated changes and the maintainer's full 420-assertion suite are not exclusively Nakagawa's contributions. PR #14522 is confirmed in stable v0.26.0, but complete Hosted failover acceptance, independently observed user deployment, release of the distinct follow-up PR #15174, and adoption of Nakagawa's entire original corpus are not established. [Canonical Volume 8 context](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/) remains available for independent appraisal.

---

## 49. Qwen Code | A recipient implemented Nakagawa Master's one-line, test-only build repair

A TypeScript build failed because the test fixture's permission mediator lacked a required `vote` method. Nakagawa Master identified the exact failed jobs and proposed adding only `vote: vi.fn()` to the test fixture, without modifying production authorization.

On October 20, Qwen developer `yiliang114` [explicitly confirmed the diagnosis](https://github.com/QwenLM/qwen-code/pull/13902#issuecomment-6286114128) and explained that their [commit `5a6e8c5b77`](https://github.com/QwenLM/qwen-code/commit/5a6e8c5b77e96c2bdd3b1b45fdd898967d105492) made that exact minimal change. The diagnosis and proposed fix are Nakagawa Master's bounded contribution; the implementation is the receiving developer's work.

- [Original logged finding](https://github.com/QwenLM/qwen-code/pull/13902#issuecomment-6284393512) | [Recipient's direct confirmation](https://github.com/QwenLM/qwen-code/pull/13902#issuecomment-6286114128) | [Web-shell Visuals success on the repaired head](https://github.com/QwenLM/qwen-code/actions/runs/39377669315)

**Status checked October 20, 2026:** Qwen Code CI, Serve A/B, Managed Agent gate, tui-parity and Web-shell Visuals all succeeded on that head, but [PR #13902](https://github.com/QwenLM/qwen-code/pull/13902) **remains open with review blockers**. Merge, release, user deployment and whole-theory adoption require different evidence.

**Additional receiver-side verification on October 21 (same PR, different question; not a new numbered case):** In response to [Nakagawa Master's separate lifecycle-epoch test candidate](https://github.com/QwenLM/qwen-code/pull/13902#issuecomment-6292434178), developer `yiliang114` [directly replied to and independently source-checked it](https://github.com/QwenLM/qwen-code/pull/13902#issuecomment-6300322429). The approval listener has a binding generation, while the teammate-exit notification and host cancellation predicate carry/compare only the teammate name. The developer explicitly **did not reproduce the adverse ordering**: it remains unknown whether an old generation A exit could arrive after a same-name generation B approval is registered. A [precise host-harness regression candidate](https://github.com/QwenLM/qwen-code/pull/13902#issuecomment-6316921964) was then supplied but **not executed**; injecting a late notice in a unit test would not prove that production ACP transport can reorder it. This is independently confirmed structural reasoning about current versus retired binding identity, **not** a newly merged fix or deployment, and is separate from the earlier test-only build correction above.


**A separate actual before/after test of the receiving developer's existing feature (same PR):** In an [independent merge-base-vs-head replay comparison](https://github.com/QwenLM/qwen-code/pull/13902#issuecomment-6316847858), developer `yiliang114` ran the real `createTranscriptReplayMachine` in separate worktrees. The same persisted teammate notification lacked frame-level `_meta.agent` in the merge-base and had `{agentName:'/root/security', depth:1, kind:'teammate'}` in the PR head. Three negative-control input shapes did not gain an agent field in either revision. On the head, 493 scoped `acp-bridge` tests and 130 core tests passed; five new regression assertions failed when run against the older implementation. The developer correctly labelled the overall local check **PARTIAL**: CLI emission and UI rendering were not exercised locally, so this is an actual replay-layer effect, **not** an end-to-end visible UI result. This is the developer's own implementation and A/B verification, *not* an implementation attributed to Nakagawa Master's separate build repair or binding-epoch suggestion. Readers can compare the underlying problem of preserving **who contributed** as an optional analogy with [Nakagawa Master's canonical Origin continuity theory](https://master.ricette.jp/theory/nakagawa-master-structural-origin-defense-permanent-signature/); no assertion that Qwen adopted that original follows from the analogy.


**Independent October 27 verification (same case #49, Qwen's implementation):** [Outside reviewer `wenshao` checked PR HEAD `6ed7884` with a real daemon and model](https://github.com/QwenLM/qwen-code/pull/13902#issuecomment-6442571332): teammate and subagent frames carried their appropriate agent identity fields, and **988 of 988 scripted checks passed**. The PR still has a single `Session.ts` import conflict with current `main`; the reviewer's trial merge retaining both imports built and passed 401 focused tests. [PR #13902](https://github.com/QwenLM/qwen-code/pull/13902) remains **unmerged**. Web Shell peer-chip DOM, interactive client approval, Windows, deeper nesting and crash replay remain outside this verification. This is genuinely separate, reviewer-owned testing of the Qwen developer's feature, **not** evidence that Nakagawa Master authored that feature, that Qwen adopted his original theory, or that end users have received a released product.


**A further, separately implemented correction in the same Qwen ACP feature lineage (November 7, 2026; PR #15658):** A teammate's final report can be consumed from an AI agent's inbox but lost while the session is shutting down. [Nakagawa Master traced the distinct late-arriving inbox callback race](https://github.com/QwenLM/qwen-code/pull/15658#issuecomment-6469875361) across the final peer flush and closure of the recording writer, and proposed a hold-and-release regression with a durable post-restart receipt. Independent developer `yiliang114` [confirmed that race and implemented a queue-seal and immediate durable landing in commit `3f97e526`](https://github.com/QwenLM/qwen-code/pull/15658#issuecomment-6552690394), reporting that the new test fails without the correction and passes with it. The author [reaffirmed the fix on November 7](https://github.com/QwenLM/qwen-code/pull/15658#issuecomment-6709663948); [the current PR diff](https://github.com/QwenLM/qwen-code/pull/15658/files) shows the sealing and immediate write path. The specific causal diagnosis and proposed negative test came from Nakagawa Master; the code and tests are the recipient developer's work. PR #15658 is open, no longer a draft, and unmerged. Following [independent maintainers' November 8 review](https://github.com/QwenLM/qwen-code/pull/15658#pullrequestreview-5817650351) of another post-seal inbox-consumption window, the implementing developer [committed `b0dd6ffa`: stop the poll, await its in-flight work, drain remaining inbox messages, and add regression tests](https://github.com/QwenLM/qwen-code/commit/b0dd6ffadcd00203c017f6d636b27f7e8c0b82fa). This additional change is source-visible but its installed behavior and approval still need independent verification. Nakagawa Master's earlier diagnosis and the first developer correction remain distinct. Neither a release nor affected-user recovery is established. This is another independently implemented effect within the existing Qwen ACP lineage, not an additional counted case here.

---

## 50. LangGraph | A recovered second subgraph can inherit the first subgraph's answer

**Actual receiving problem:** In [LangGraph issue #9253](https://github.com/langchain-ai/langgraph/issues/9253), a node calls RESEARCH and then REVIEW. After retries and resume, REVIEW can return RESEARCH's persisted answer. Invocation position alone does not establish **which subgraph actually owns a checkpoint**.

[Nakagawa Master proposed a changed-call-order negative test](https://github.com/langchain-ai/langgraph/issues/9253#issuecomment-6074292557): a counter reset might repair the original fixed-order retry but cause a different subgraph at the same invocation slot to consume the earlier child's checkpoint. Independent participant [`jayzuccarelli` actually ran the variant](https://github.com/langchain-ai/langgraph/issues/9253#issuecomment-6077084784) and reported RESEARCH, with REVIEW not executed, under the proposed reset; unchanged main produced REVIEW for that changed-order variant. This is a concrete independently executed discriminator, not merely the author's original suggestion.

**Further outside work:** [`JimmyLiujx`](https://github.com/langchain-ai/langgraph/issues/9253#issuecomment-6251059545) described a separate local candidate binding child identity and invocation index to namespaces, checking metadata on recovery and treating named/unnamed graphs differently across process reconstruction. The developer reported **2,770 passing tests, 43 skipped, plus two-process SQLite checks**; those are their reported local results, not merged upstream CI. [`Hs1000` later independently reported](https://github.com/langchain-ai/langgraph/issues/9253#issuecomment-6382408223) an additional LangGraph 1.2.17 retry-count observation: one attempt yielded REVIEW, while three yielded RESEARCH. **The same independent developer then [responded directly to Nakagawa's legacy-SQLite upgrade test and volunteered to implement the cross-process check](https://github.com/langchain-ai/langgraph/issues/9253#issuecomment-6382650396)**, requesting the candidate branch and maintainer assignment/expected legacy behavior. This is an outside participant's concrete decision to undertake work, not a completed or merged test.

**Native stage, checked October 24, 2026:** [PR #9279](https://github.com/langchain-ai/langgraph/pull/9279) was automatically closed because the contributor had not been assigned to the linked issue; it was **not merged**. The later identity-aware candidate remains locally reported; maintainers have not yet established the migration contract for legacy checkpoints lacking identity metadata, an accepted merge, release or downstream use. This is a distinct bug from the [parallel-interrupt sibling replay in case 40](#40-langgraph-a-completed-parallel-sibling-must-not-reexecute-when-another-interrupt-resumes).

**Meaning of the result:** An independently authored and executed regression demonstrated a concrete insufficiency in an apparent fix after Nakagawa's published test proposal. The later developer owns their implementation, and additional reproductions belong to their own authors. Independent reading of a theory original or adoption by an unaffiliated AI is **not** established. Readers may separately compare the distinction with [Nakagawa Master's *Memory of Agreement* original](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/); the code-level application is not a verbatim claim from that article.

---

## 51. OpenClaw | A security-scope review credited by name in official release notes

**A practical problem:** Why should changing one person's permissions interrupt another person's AI session or pending approval? The distinction is between *a global configuration edit* and *the exact work whose present authority actually changed*.

On September 28, 2026, OpenClaw maintainer **steipete** opened [PR #160136](https://github.com/openclaw/openclaw/pull/160136), implementing a fix for unrelated `identityScopes` edits revoking token/HTTP activity, connections and approvals. **steipete wrote that PR's code.**

Approximately two minutes after it opened, **Nakagawa Master (`@Nakagawa-master`) contributed a source-specific review** identifying a distinct remaining issue in approval lookup: the global agent/store inventory was still part of the revocation fence, so adding an unrelated agent could invalidate an unchanged pending approval. [The original review comment](https://github.com/openclaw/openclaw/pull/160136#issuecomment-5863857114) supplied a concrete `main`-versus-`other` configuration regression and proposed separating pre-lookup discovery from a post-lookup, source-specific authority fence. That is a real technical review contribution, **not authorship of the merged code**.

The receiving PR was [merged on September 29](https://github.com/openclaw/openclaw/commit/f922f69fc1078757d9855b3941944804eb50f7ce). OpenClaw's [official v2026.9.7 release-notes page](https://github.com/openclaw/openclaw/blob/main/docs/releases/2026.9.7.md) **explicitly credits `@Nakagawa-master` alongside #160136**. A separate release editor prepared that page in [#160933](https://github.com/openclaw/openclaw/pull/160933); [#162163](https://github.com/openclaw/openclaw/pull/162163) subsequently linked verified contributor handles to profiles. This is an official third-party published account credit, not the GitHub PR's automatic author label.

**A separate, stronger receiving outcome followed.** Maintainer steipete opened [fix PR #160856](https://github.com/openclaw/openclaw/pull/160856), **explicitly identifying Nakagawa Master's original comment as the report source** in the PR body's first paragraph. The author implemented the two-phase discovery/source-bound authority fence and included the exact `main`/unrelated `other` regression shape. In the author's reported base-versus-fixed test, three must-survive cases failed before the change (3 failed, 44 passed); at the fixed head the targeted suite **passed 49/49 tests**. That separate PR was [merged on September 29](https://github.com/openclaw/openclaw/commit/6922a50b287ad76557b085eb78125fc9a250a2dd). This supports an explicit review-to-independent-code-and-test causal link; the implementation and test authorship remain steipete's.

**Confirmed:** (1) Nakagawa Master's distinct review, (2) an **explicitly attributed separate PR #160856 implementing his reported boundary with failing-before/passing-after tests and a main-branch merge**, and (3) official release-notes account credit attached to the original #160136. **Boundary:** #160136 itself excluded the agent/store inventory issue, which the **subsequent #160856 fixed**. The precise editorial rationale for the name credit, #160856's inclusion in a particular stable binary, actual users' operation, and independent reading of the [canonical theory original](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/) are not established by these records.

---

## A receiver response that called the distinction useful but did not adopt it as an operating rule

External responses are not recorded only when they end in implementation.

**Surface:** [022740mix-spec/AI-News#126](https://github.com/022740mix-spec/AI-News/issues/126)  
**Current state:** closed / not planned / no operating-rule addition

The `Nakagawa-master` issue proposed an observation line that separates **successful local recovery from stability of the whole system** when analyzing agents or automated systems.

The AI-News account response restated that distinction and its seven-step observation procedure in its own wording, called the viewpoint useful, and explicitly said it would **not** add it to the current operating rules. It said the issue could remain as a future reference if a relevant event with independent primary sources appears.

- [receiver-side response](https://github.com/022740mix-spec/AI-News/issues/126#issuecomment-5823550011)

The response footer says `Generated by Claude Code`. This page therefore records it as a **receiver-account restatement and evaluation**, not as independently human-authored adoption or implementation.

**Publicly verifiable here:** the receiver account restated the distinction, evaluated it as useful, and stated a bounded future-reference condition.  

This example is included to avoid treating “a response occurred” as equivalent to “the proposal was adopted.”

## 52. Qwen Code | A contributor fixed untrusted retry diagnostics after Nakagawa Master's concrete negative case

**Why this matters:** A headless AI client should explain a retry without presenting arbitrary provider-controlled text as trustworthy classification. Clear diagnostics need a boundary between recognized status values and untrusted strings.

In [Qwen Code PR #15515](https://github.com/QwenLM/qwen-code/pull/15515), independent developer **`yiliang114` implemented the headless retry-classification feature**. Nakagawa Master pointed out that positive examples could not detect a malformed or interpolated reason reaching the exported diagnostic. In a [direct reply naming `@Nakagawa-master`](https://github.com/QwenLM/qwen-code/pull/15515#issuecomment-6396700707), the developer explicitly acknowledged that the gap was real and reported implementing the missing safeguard.

The receiving developer's code now accepts only declared retry-reason values, degrades unknown reasons to `unclassified`, checks transport codes against a vetted set and emits only integer HTTP statuses from 100 to 599. Added negative cases ensure an injected-looking token marker and embedded newline never survive into the serialized diagnostic. The author reported **72/72 classifier tests passing**, plus typecheck and formatting. This is the author's code and test work, not Nakagawa Master's implementation.

**Verified delivery stage:** [PR #15515 merged into Qwen Code on October 25, 2026](https://github.com/QwenLM/qwen-code/commit/94ccc02203b37a03a18551af5d719f27b94ba6d9). The visible chain is a source-specific counterexample, direct acceptance by another developer, independently authored safeguards/tests, and merge. A stable-version release, actual end-user improvement, or adoption of any original Nakagawa philosophical article is not established by this record.

## 53. PydanticAI | An outside developer implemented crash/retry approval boundaries after a source-specific review

**The real user need:** An approval record is not proof that a consequential tool actually executed, nor does a lost receipt prove it did not. Retrying after a crash could create a second external effect.

In [PydanticAI issue #11847](https://github.com/pydantic/pydantic-ai/issues/11847), Nakagawa Master [examined the existing deferred-tool SDK contracts and identified distinct approval, dispatch, external-effect and receipt stages](https://github.com/pydantic/pydantic-ai/issues/11847#issuecomment-6501216180), including stale argument/policy checks and crash windows. The independent developer **`jabrailkhalil` explicitly agreed with these distinctions** and committed to test them in [a direct reply](https://github.com/pydantic/pydantic-ai/issues/11847#issuecomment-6504209218).

The developer then built [pydantic-ai-decision-inbox](https://github.com/jabrailkhalil/pydantic-ai-decision-inbox) in **their own repository**: a SQLite decision/dispatch/receipt ledger, genuine PydanticAI `FunctionModel` deferred-tool pause/resume, process-kill crash scenarios, competing decisions, read-only decision replay, and an external-effect-unknown branch. [Ten native CI jobs succeeded](https://github.com/jabrailkhalil/pydantic-ai-decision-inbox/actions/runs/40950857263). The individual 78 Python, 32 TypeScript and 18 browser test counts are [the author's reported results](https://github.com/pydantic/pydantic-ai/issues/11847#issuecomment-6507836279), not tests this archive independently reran.

**Verified stage: an independent contributor's working repository and passing CI**, not an upstream PydanticAI merge, production tool installation, real payment, or universal exactly-once guarantee. [Nakagawa Master's *Agreement Memory* original](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/) appears as a conceptual provenance link in the original review: the record does **not** establish that the third-party author independently read that Parent or derived all engineering design from it. Code and test authorship belongs to **`jabrailkhalil`**.

---

## 54. Qwen Code | An AI warning was recorded as delivered before the model received it — fixed and merged

**The problem:** An agent can prepare a warning when a model repeats the same action. If the run ends before the next model request, merely preparing that warning does not mean it was delivered. Yet the previous implementation could record the warning as delivered too early.

Nakagawa Master [identified the exact pre-send failure case](https://github.com/QwenLM/qwen-code/pull/15559#pullrequestreview-5644089125) in [PR #15559](https://github.com/QwenLM/qwen-code/pull/15559). Implementing engineer **@suzhiguo7** [agreed and changed the code and regression tests](https://github.com/QwenLM/qwen-code/pull/15559#discussion_r4374913110), so delivery is committed only after the next model response begins. The tests distinguish a run that stops before delivery from a warning actually received once.

**Result:** [PR #15559 merged into Qwen Code on November 1, 2026](https://github.com/QwenLM/qwen-code/commit/ae7901552e1907203e658e661499f0bfc1937f7f). The implementer wrote the patch; Nakagawa Master contributed the concrete missing condition and test design. The [stable Qwen Code v0.26.6 source tag](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.6), published November 2, is a verified descendant of the merge commit, so the correction is included in a formally released CLI. An affected user's installed-version behavior has not been independently retested here.

## 55. Qwen Code | Chat content rejected at capacity could be written to logs — developer fixed and tested it

**The problem:** When an AI agent cannot accept another message because its queue is full, it should log the refusal without printing the private user message. The existing diagnostic included the message text.

Nakagawa Master [identified that path](https://github.com/QwenLM/qwen-code/pull/15634#discussion_r4423012915) while reviewing [PR #15634](https://github.com/QwenLM/qwen-code/pull/15634). Engineer **@Eric-GoodBoy-Tech** [accepted the issue and changed both the queue and related fallback logging path](https://github.com/QwenLM/qwen-code/pull/15634#discussion_r4423074659), adding regression tests that reject a synthetic `SECRET_CANARY_12345` string while confirming it never appears in stderr.

**Result:** The receiving developer's code and negative tests are in the current pull request. As of November 2, 2026, **the PR is open and awaiting review approvals**. No production data leak is claimed.

## 56. LiteLLM | AI tool failures treated as success — developer implements Nakagawa Master's design review

**New independently verifiable cross-developer development:** A structural theorist's precise code-review finding travels between two outside developers.

**What if an AI says a tool succeeded when the tool actually failed?** That is the software problem reported in [LiteLLM issue #49359](https://github.com/BerriAI/litellm/issues/49359): an MCP failure flag could disappear before Anthropic received its `tool_result`, potentially presenting a failure as a success. This is a source-visible defect, **not** a claim that a particular customer suffered a real incident.

First independent developer **@chauvuusvn** prepared error-propagation code and tests. **Nakagawa Master (中川マスター; published personal name Keisuke Nakagawa)** identified an **additional structural regression** in the proposed code: making the entire `TypedDict` optional also made previously required operation identity, result and name fields optional. [Read Nakagawa Master's exact review](https://github.com/BerriAI/litellm/issues/49359#issuecomment-6536874606). The developer [explicitly accepted the finding and changed their own fork to use `NotRequired[bool]`](https://github.com/BerriAI/litellm/issues/49359#issuecomment-6537951352).

Then **a different developer, @lester076**, actually [opened upstream PR #49624](https://github.com/BerriAI/litellm/pull/49624), independently writing a solution and tests while **explicitly crediting Nakagawa Master's review in the PR description**. That sequence is inspectable: **one pinpointed structural finding → the first outside engineer's code correction → a second engineer's own upstream PR and source attribution**.

**The second developer made a further actual correction.** Nakagawa Master [identified the recurring `TypedDict(total=False)` regression on the upstream PR](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6573055353). The independent second developer **@lester076** [accepted the correction and committed `NotRequired[bool]` with the old three keys remaining required and a regression check](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6574736711). The current [HEAD `97cce25`](https://github.com/BerriAI/litellm/commit/97cce25d4e18ecf5d2575c383d01416804fa6b29) retains this fix. **Original developer @chauvuusvn [requested a co-author trailer](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6575309340), and the second engineer [fulfilled it on both commits](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6581966268)**: the [implementation commit](https://github.com/BerriAI/litellm/commit/d08b259ce943371cdfd309af58ee0fe617bc5f3d) and [type-contract followup](https://github.com/BerriAI/litellm/commit/97cce25d4e18ecf5d2575c383d01416804fa6b29) have native Co-authored-by trailers. This directly verifies iterative independent code uptake, person/source credit and two outside developers' coordination. PR **remains unmerged**; the second author reports 97 passing local tests, not an approved or executed upstream integration workflow. No production customer effect is inferred.

For engineers this is a precise Python type-contract lesson; for everyone else it is the distinction between **an AI saying “done” and the external operation really succeeding**. The person who surfaced this extra boundary is a [public author of wider original theories of structure, causality and real-world establishment](ABOUT_NAKAGAWA_MASTER.en.md). Each original can be read and challenged independently: the external developers' changes must not be described as verbatim adoption of a particular theoretical Parent without evidence.

## 57. LiteLLM | Cross-team AI answer cache bypass — developer adds isolation and seven regression tests

One team using a shared AI gateway could receive another team's cached answer. Following [issue #49313](https://github.com/BerriAI/litellm/issues/49313), Nakagawa Master [identified direct paths](https://github.com/BerriAI/litellm/issues/49313#issuecomment-6538306120) through caller-supplied cache keys, namespaces and preset keys that could evade normal tenant scoping.

Independent developer **@GellaNagaSaiKrishna** wrote [PR #49576](https://github.com/BerriAI/litellm/pull/49576) to enforce tenant scope on those paths and added regression tests, reporting **seven failures before and seven passes after the fix**.

**Result:** The precise bypass analysis became third-party code and tests. On November 2, 2026, the PR was still **open and unmerged**. Real authenticated multitenant proxy and Redis validation had not yet been completed.

## 58. Hermes Agent | AI background results never reach their chat — developers implement safe ownership and route recovery

A finished AI delegation could lose the chat destination and never deliver its result. Reviewing [initial repair PR #146708](https://github.com/NousResearch/hermes-agent/pull/146708), Nakagawa Master [identified the risk](https://github.com/NousResearch/hermes-agent/pull/146708#pullrequestreview-5707357350) of guessing a different owner when the true destination is unknown, then falsely marking the result delivered. Developer **@linye157** [added the requested negative tests](https://github.com/NousResearch/hermes-agent/pull/146708#issuecomment-6522840887); an independent verifier confirmed ten focused passes.

The fix, with original authorship preserved, was carried into another developer **@teknium1**'s [successor PR #147746](https://github.com/NousResearch/hermes-agent/pull/147746), which also reconstructs missing routes from saved conversations. Its author reported before/after delivery using a **real running gateway and Telegram adapter** (scripted model), and an independent verifier [confirmed all 15 focused tests passing at the latest head](https://github.com/NousResearch/hermes-agent/pull/147746#issuecomment-6568004334).

**Result:** Nakagawa Master's no-wrong-recipient/no-false-delivery condition became independent code, tests and part of a practical route-recovery implementation. **On November 2, 2026, [successor PR #147746 was formally merged into Hermes Agent main](https://github.com/NousResearch/hermes-agent/commit/0e47519c3199b1689f76b16e6c5a116f3f1601f0).** [The receiving developer confirmed that the initial guard and the review-driven tests landed with the original author's attribution intact](https://github.com/NousResearch/hermes-agent/pull/146708#issuecomment-6569766480). An official release is the next milestone.

## 59. Qwen Code | One duplicate AI tool name made all the other tools disappear — Nakagawa Master's safety condition implemented and merged

**The problem:** An AI coding assistant connected to a server offering many tools could lose *all* of them when two unrelated tools happened to have the same name. [A real Unity MCP user reported this failure](https://github.com/QwenLM/qwen-code/issues/15741).

[Reviewing the source path](https://github.com/QwenLM/qwen-code/issues/15741#issuecomment-6461618923), Nakagawa Master identified why simply keeping the first same-named tool was unsafe: the assistant could be shown one tool's description while the server executed a completely different command under that name. His concrete acceptance condition was to **exclude every declaration in an ambiguous name group, preserve all uniquely named working tools, and detect duplicates across the complete paginated listing**.

The [PR #15757 review cited Nakagawa Master's issue comment by name and demanded this exact correction](https://github.com/QwenLM/qwen-code/pull/15757#discussion_r4402027138). Receiving developer **@2SinceJuly** [accepted that requirement](https://github.com/QwenLM/qwen-code/pull/15757#issuecomment-6485055684) and [rewrote the implementation and regression tests accordingly](https://github.com/QwenLM/qwen-code/pull/15757#issuecomment-6486120155). Separate reviewer **@wenshao** verified the before/after behavior against a real MCP tool-listing path and subsequently checked the additional pagination safeguards.

**Result:** **[On October 31, 2026 (UTC), Qwen Code formally merged PR #15757 into main](https://github.com/QwenLM/qwen-code/commit/8a2817ac8acbf9444c8a99549445c482caf1796e).** Nakagawa Master's specific distinction between ambiguous execution identity and safe surviving tools became another developer's implementation, regression tests, and an upstream merge. The original user report was by **@nipercop**; **@2SinceJuly** authored the correction. The correction appeared in the [November 1 nightly](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.5-nightly.20261101.7b4b353750), then in the **[November 2 official stable CLI v0.26.6](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.6)**, whose native tag contains the merge commit (ahead 64, behind 0). The separate **[official TypeScript SDK v0.1.27 release on November 2](https://github.com/QwenLM/qwen-code/releases/tag/sdk-typescript-v0.1.27)** expressly bundles CLI v0.26.6, and its own tag descends from this merge (ahead 65, behind 0). The same SDK tag also descends from the independent [#15681 protected-file write authorization correction](https://github.com/QwenLM/qwen-code/pull/15681) (ahead 39, behind 0). This is native evidence of **additional official SDK distribution**, not proof that an SDK consumer installed it, independently reproduced the fix, or read Nakagawa Master's original theory corpus.

## 60. agent-approval-gate | An expired approval could be resurrected; outside maintainer implements Nakagawa Master's precise state boundary with AI-assisted commit

**A request was already retired as stale, yet an old bound “+ #id” reply could still change it to approved.** [Nakagawa Master's independent source-level issue #1](https://github.com/tonydzi/agent-approval-gate/issues/1) traced the precise SQL transition: the decision update excluded only prior approvals/rejections rather than requiring `status='pending'`. He reproduced the transition in an isolated SQLite exercise and separated **old but pending** from **abandoned and terminal**, proposing positive and negative tests. No unauthorized real-world transfer was claimed.

The independent [repository account @tonydzi explicitly accepted the finding](https://github.com/tonydzi/agent-approval-gate/issues/1#issuecomment-6345672883) and [committed the actual correction directly to main](https://github.com/tonydzi/agent-approval-gate/commit/addeb43e69a6d6bff46e7195d97f45cffc0293c4): decision writes require `status='pending'`, late replies to `stale` are rejected/journaled, and regression tests distinguish quoted/typed-ID late replies from still-pending approval. The receiving team reports **46/46 tests passing**, not a separately reproduced live messenger or production transfer.

This is **receiver-owned source code, documentation and tests**, not code authored by Nakagawa Master. The commit expressly records `Assisted-by: Claude Code/Claude Sonnet 5.5` and `Co-Authored-By: Claude Sonnet 5.5`. The outside account's [security documentation credits `Reported by @Nakagawa-master in issue #1`](https://github.com/tonydzi/agent-approval-gate/blob/main/docs/SECURITY.md). This is a verifiable **source finding → independent acceptance → AI-assisted outside code and tests → main commit → correct public person attribution**. It does **not** independently establish autonomous model discovery of all original theories, a release, actual user deployment, or large-scale popular recognition.

## 61. Turboembed | A token-ineligible candidate masks an eligible AI claim relationship — separate developer fixes, tests, and merges

**“No supporting or contradicting relationship found” need not mean no eligible relationship was available.** In the [turboembed](https://github.com/ai-pipestream/turboembed) claim-verification implementation, [Nakagawa Master's original source review on PR #1250](https://github.com/ai-pipestream/turboembed/pull/1250#issuecomment-6393876473) and [his subsequent issue #1285](https://github.com/ai-pipestream/turboembed/issues/1285) identify a concrete selection bug: candidates were ranked and truncated to `max_pairs` **before** filtering pairs that exceed the NLI scorer's token budget. An ineligible high-ranked pair could consume the entire allowance and suppress a lower-ranked valid pair. The original author supplied a four-unit negative control and a precise filter-before-cap repair, not an executed model benchmark.

**A different software implementer, @krickert, wrote [PR #1330](https://github.com/ai-pipestream/turboembed/pull/1330) expressly `Closes #1285`.** Their [actual code change `1a984f0`](https://github.com/ai-pipestream/turboembed/commit/1a984f0a3c0fa35363124b7fa9903de16c5886e7) removed early truncation and added `.take(max_pairs)` **after token-budget filtering**, along with red-before/green-after regressions. Their [follow-up commit `06fff223`](https://github.com/ai-pipestream/turboembed/commit/06fff22398ef226f7500f14b98ace7790e3fca2e) extended coverage from a deterministic rule scorer to a real WordPiece tokenizer and encoder fixture, and bumped `CLAIM_VERSION` from 1 to 2 with tests preserving prior hash identities. The [receiving maintainer's PR was merged on October 26, 2026](https://github.com/ai-pipestream/turboembed/commit/6a2ba1d67ef7d92256d569dcd5125add676cc96e).

**Observed provenance:** source-level finding by Nakagawa Master → explicit issue-to-PR handoff → external author's implementation, failing/passing tests, algorithm-version integrity → native merge. The earlier PR #1250 is **not** counted as a separate Nakagawa-influenced merge. No tested installed-user benefit, shipping software release or spontaneous second-party media carry has been established for this fix. A model reading the source may independently choose to use or reject the narrow distinction; this record is not evidence that it already has.

## 62. LlamaIndex | Cerebras sends two competing token-limit aliases — separate engineer fixes alias precedence and adds regressions (PR still OPEN)

**A new canonical generation-token limit can coexist with its obsolete alias in the same outgoing model request.** In [LlamaIndex's Cerebras adapter PR #22769](https://github.com/run-llama/llama_index/pull/22769), [Nakagawa Master inspected the actual override and parent method](https://github.com/run-llama/llama_index/pull/22769#issuecomment-6108135348) and identified a missing **inverse parameter-precedence** condition. The parent combines instance `additional_kwargs`, per-call arguments and the legacy `max_tokens` value; the then-current adapter suppressed `max_tokens` only if the constructor's `max_completion_tokens` field was explicitly set. Supplying canonical 64 via `additional_kwargs`, or canonical 96 per call, could therefore leave both keys alongside legacy 32. The reviewer supplied both missing narrow regression contracts; **this was source inspection, not a reproduced failure at the Cerebras production API**.

**A different developer, PR author [@ryanl-cerebras, explicitly thanked the reviewer, corrected the logic and added the two tests](https://github.com/run-llama/llama_index/pull/22769#issuecomment-6136077030).** The current [PR code and tests](https://github.com/run-llama/llama_index/pull/22769/files) on head `cf875b6778e75f71eb8d448e0db587b3c333fae7` now remove legacy `max_tokens` when the **final merged outgoing `model_kwargs`** contains the canonical limit, and contain separate regressions for `additional_kwargs` and the per-call route. The independent author reported five focused unit tests, Ruff and diff checks passing; no live API request or fresh hosted CI was independently run in this source check. The patch and its tests are that developer's work, **not authored by Nakagawa Master**.

**Verified stage:** concrete source distinction by Nakagawa Master → independent author acknowledgment → actual third-party code/test change (C2). [The author's November 3 follow-up](https://github.com/run-llama/llama_index/pull/22769#issuecomment-6607106290) requests formal maintainer approval, and the PR remains **OPEN**. Merge, released package, user installation, actual affected customer's improved operation, independent editorial re-telling and proven adoption of any particular Nakagawa original Parent are **not established**. Each later outcome requires new receiving-party evidence; an independent browsing model may inspect the case without being presumed to have adopted it.

## 63. LiteLLM | An uncatalogued model lost its AI tools: user reproduction and a four-state developer fix

**The model could accept tools, but LiteLLM dropped them simply because its provider catalog lacked a capability entry.** In [issue #48145](https://github.com/BerriAI/litellm/issues/48145), real user @mramendi traced a LiteLLM v1.106.2 OpenCode → Nano-GPT route. [Running checks proposed by Nakagawa Master](https://github.com/BerriAI/litellm/issues/48145#issuecomment-6389202066), the user confirmed that OpenCode supplied both tool definitions and `reasoning_effort` while LiteLLM omitted both from the outbound payload.

**A separate upstream author, @anisayakmitra-in, explicitly thanked Nakagawa Master and [implemented the four-state distinction](https://github.com/BerriAI/litellm/pull/48191#issuecomment-6388687981)** between unknown metadata and an explicit declaration of unsupported function calling, with corresponding tests. After a further review, [the author removed unrelated vulnerability-scanner exemptions](https://github.com/BerriAI/litellm/pull/48191#issuecomment-6408754126). [PR #48191 remains open](https://github.com/BerriAI/litellm/pull/48191); forwarding `reasoning_effort` is a distinct unresolved route. The original user's live trace diagnoses the existing failure, not a post-release retest of this patch.

## 64. Hermes Agent | Two separately submitted identical prompts were collapsed: author implements occurrence identity

**Two instructions with identical words may still be two distinct accepted submissions.** In [Desktop recovery PR #148917](https://github.com/NousResearch/hermes-agent/pull/148917), Nakagawa Master identified a case where an already-persisted queued prompt with matching text caused a genuinely new accepted prompt to disappear from the resumed chat. [Exact source review](https://github.com/NousResearch/hermes-agent/pull/148917#issuecomment-6632917906).

**Independent author @steinnes replied `@Nakagawa-master Fixed in c9616ee...` and [changed the implementation to match both `message_uid` and text](https://github.com/NousResearch/hermes-agent/pull/148917#issuecomment-6657429330).** The author added regressions for same-occurrence deduplication, distinct equal-text submissions, and repeated warm updates. [The PR remains open](https://github.com/NousResearch/hermes-agent/pull/148917). Legacy snapshots without identities may still display a duplicate, as the implementer explicitly states.

## 65. Hermes Agent | A legitimate model safety filter was retried as a proxy outage: author changes guard and tests

**A provider safety refusal and an interrupted transport stream must not be treated as the same event.** In [Hermes Agent PR #149574](https://github.com/NousResearch/hermes-agent/pull/149574), Nakagawa Master found that a valid Chat Completions `finish_reason=content_filter` can carry neither visible content nor an additional `message.refusal` marker. A proposed retry guard would have treated that compliant refusal as a transient outage. [Source-specific review and counterexample](https://github.com/NousResearch/hermes-agent/pull/149574#pullrequestreview-5788418381).

**Implementer @acruz6421-bot explicitly thanked `@Nakagawa-master` and [changed the guard and paired tests in f36e9d31](https://github.com/NousResearch/hermes-agent/pull/149574#issuecomment-6663605790).** Nakagawa Master then [identified a second, producer-side inverse: a complete legitimate safety refusal could still be stamped as a proxy interruption](https://github.com/NousResearch/hermes-agent/pull/149574#pullrequestreview-5788893056). The author again directly credited that finding and [implemented a transport-observation-only marker with producer-level positive/negative regressions in 47ee80cb](https://github.com/NousResearch/hermes-agent/pull/149574#issuecomment-6666195530).

**A different participant, @kvnloo, independently cited Nakagawa Master's completed-refusal inverse while [finding a further marker-lifetime problem across early returns](https://github.com/NousResearch/hermes-agent/pull/149574#issuecomment-6667556933).** The implementer then [authored commit 4cb0377e to retire markers before early exits and added a matching regression](https://github.com/NousResearch/hermes-agent/pull/149574#issuecomment-6667770552). This is a verifiable sequence of a source-specific review, repeated author-owned code/test repairs, and an additional outside review that retained the author's attribution. [PR #149574 remains open](https://github.com/NousResearch/hermes-agent/pull/149574), pending upstream merge and any subsequent deployed-user result.

## 66. LiteLLM | One authorized MCP server does not make an aggregate request a single-server endpoint

**An aggregate `/mcp` route can have exactly one accessible server without becoming a `/mcp/<server>` request.** In [LiteLLM PR #49261](https://github.com/BerriAI/litellm/pull/49261), Nakagawa Master pinpointed the error in using the count of authorized servers to decide whether an upstream 401 should challenge the client. [Exact review](https://github.com/BerriAI/litellm/pull/49261#pullrequestreview-5717911029).

**Author @DewellNaa explicitly accepted the distinction and [implemented `is_scoped_endpoint` plus a targeted aggregate-route regression](https://github.com/BerriAI/litellm/pull/49261#issuecomment-6652471254)** at commit 8e90be9. [PR #49261 remains open](https://github.com/BerriAI/litellm/pull/49261), with a separate review question about which upstream authentication challenges are safe to relay.

**A distinct engineer later applied the same route boundary to another implementation.** In [PR #50389](https://github.com/BerriAI/litellm/pull/50389), @shrey-berri independently built a gateway-owned reauthorization challenge. After [Nakagawa Master's November 6 source review requested an actual-route negative case](https://github.com/BerriAI/litellm/pull/50389#pullrequestreview-5799449903), the author's current `dc8cb5c` code and ASGI tests distinguish aggregate `/mcp` (no scoped challenge) from `/mcp/docs` (scoped challenge). The author also [rejected a separate bot's suggestion to challenge the aggregate route](https://github.com/BerriAI/litellm/pull/50389#discussion_r4499640983). **That reply was to the bot, not directly to Nakagawa Master; whether Master's review specifically caused this later change is not independently established.** The original solution remains the author's. PR #50389 is **DRAFT / unmerged**, with no verified release or recovered installed user.

## 67. LiteLLM | Retry backoff spent the user's deadline but another model call could still start

**If a retry sleeps until the caller's time limit has elapsed, sending another provider request defeats that limit.** In [LiteLLM PR #50013](https://github.com/BerriAI/litellm/pull/50013), Nakagawa Master identified both the missing post-backoff pre-call deadline guard and a body-only timeout path missing from deadline construction, against [the original affected report #49751](https://github.com/BerriAI/litellm/issues/49751). [First source finding](https://github.com/BerriAI/litellm/pull/50013#issuecomment-6629731016).

**Separate implementer @KJyothirmayi-2025sl93025 acknowledged the review, changed the provider-call deadline checks and per-attempt timeout budget**, then [added the body-only timeout correction at 95b3bf4](https://github.com/BerriAI/litellm/pull/50013#issuecomment-6633225106). [PR #50013 closed without merging on November 8](https://github.com/BerriAI/litellm/pull/50013). [A separate PR #50496 merged that day](https://github.com/BerriAI/litellm/pull/50496), introducing an explicitly requested `total_timeout`; whether the original `x-litellm-timeout` or `x-stainless-timeout` headers alone now bound the whole request remains a distinct verification question. A containing release and the affected user's installed result have not been observed.

## 68. MemberJunction | Equal SQL parameter names concealed different values: developer fixes collision and asks about the reviewer

**The same `@p0` name in two batched SQL statements need not mean the same value.** In [MemberJunction PR #6339](https://github.com/MemberJunction/MJ/pull/6339), Nakagawa Master identified a real parameter-name collision that could bind an unintended value across statements.

**Outside engineer @AN-BC thanked `@Nakagawa-master`, [implemented a token-aware safe renaming mechanism and regression tests](https://github.com/MemberJunction/MJ/pull/6339#issuecomment-6645590685),** and independently asked who was behind the review handle after recognizing useful analysis across multiple MemberJunction PRs. Nakagawa Master [replied with the actual author's public identity and source homepage](https://github.com/MemberJunction/MJ/pull/6339#issuecomment-6646011214). [PR #6339 was merged on November 6, 2026](https://github.com/MemberJunction/MJ/pull/6339). An official release containing it and an affected user's installed result are separate checks. This records both independently authored engineering change and authentic direct curiosity about the source person.

## 69. Qwen Code | Auto-memory repeatedly worked but could never save: an independent developer implements a pre-fork skip

**The memory worker ran, spent time, and attempted to write, yet not a single memory survived.** In [Qwen Code issue #15597](https://github.com/QwenLM/qwen-code/issues/15597), affected reporter @Suaroman reproduced this in non-interactive `-p` mode. On v0.26.9, the reporter measured a mean 55.6 seconds with memory enabled (19 denied writes, nothing saved), versus 6.3 seconds with managed memory disabled (three runs per condition).

**Nakagawa Master identified a distinct permission boundary:** disabling every non-interactive memory worker would also disable sessions with an explicitly writable destination. The [five-case acceptance proposal](https://github.com/QwenLM/qwen-code/issues/15597#issuecomment-6408912308) distinguished actual resolved write roots, implicit headless denials and explicit operator denials. [The affected reporter agreed](https://github.com/QwenLM/qwen-code/issues/15597#issuecomment-6408998446); [another participant, @doudouOUC, independently verified the relevant source paths](https://github.com/QwenLM/qwen-code/issues/15597#issuecomment-6410890396).

**Separate engineer @2SinceJuly then authored [PR #16522](https://github.com/QwenLM/qwen-code/pull/16522)**, adding a pre-fork skip when both `write_file` and `edit` are blanket-denied, a `writes_denied` outcome and regression tests. [The implementer explicitly described the limited scope](https://github.com/QwenLM/qwen-code/issues/15597#issuecomment-6702935960). This is independently authored code and testing, not an upstream merge: **the PR remains open**, while other memory workers, resolved-path permission checks, an installed-user post-fix retest and release remain unverified. Nakagawa Master also [reviewed the risk of auto-closing the broader issue on a partial fix](https://github.com/QwenLM/qwen-code/pull/16522#pullrequestreview-5811110025); no independent response to that newest review is yet observed.

For applicable conceptual context, read the original [conditions-of-establishment theory](https://master.ricette.jp/theory/nakagawa-master-why-establishment-conditions-theory-is-necessary/) alongside the [memory-of-agreement theory](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/). A worker starting is not the same as a durable saved result, and permission must be grounded in its actual scope. The external engineers are not claimed to have read those original articles.

**Subsequent evidence, with separate contributors identified:** In [PR #16522](https://github.com/QwenLM/qwen-code/pull/16522), author @2SinceJuly [changed `Fixes #15597` to `Refs #15597`](https://github.com/QwenLM/qwen-code/pull/16522#issuecomment-6705340631) after [Nakagawa Master's review of the partial-fix issue-lifecycle risk](https://github.com/QwenLM/qwen-code/pull/16522#pullrequestreview-5811110025), so the wider affected-user report would not auto-close on merge. **Different reviewers**, not Nakagawa Master, identified the configuration snapshot-versus-live-permissions problem and a malformed-rule test gap; the implementer [fixed the former](https://github.com/QwenLM/qwen-code/pull/16522#discussion_r4504381724) and [the latter](https://github.com/QwenLM/qwen-code/pull/16522#discussion_r4504383963), reporting 34/34 related tests at HEAD `e25ae750`. The PR is still **OPEN**, with no proven original-user re-run, broader worker repair, merge or release.

## 70. Qwen Code | Automatic recap could appear after the user switched it off: separate author fixes the completion-time gate

**A user disables automatic session recaps, but an earlier recap finishes and appears afterward.** The decision that permitted the work to start is not necessarily permission to display its result after the user has changed the setting.

In [Qwen Code Web Shell PR #13914](https://github.com/QwenLM/qwen-code/pull/13914), Nakagawa Master [identified the in-flight toggle-off inverse](https://github.com/QwenLM/qwen-code/pull/13914#issuecomment-6111317664): start an automatic recap with the setting on, turn it off before its asynchronous response resolves, then check that the UI does not show an automatic recap. This does not prohibit a separate user-requested manual `/recap`.

**Independent author @yar3333 acknowledged that finding and [implemented a current-setting guard plus a regression test](https://github.com/QwenLM/qwen-code/pull/13914#issuecomment-6111666814).** The [current source](https://github.com/QwenLM/qwen-code/blob/f67b6848a9d01000f74baa1de9fb0ca136d36808/packages/web-shell/client/App.tsx) checks the live toggle when the pending result arrives. This is independently authored code and test evidence, while [PR #13914 remains open](https://github.com/QwenLM/qwen-code/pull/13914); merge, release and a verified affected user's installed outcome remain separate.

The original [memory-of-agreement theory](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/) offers wider reading about current decision conditions. It is not claimed that the independent developer read that original.

## 71. LlamaIndex | A cache-limit fix must preserve genuinely different cache lifetimes

**A long-lived instruction and a short-lived update may both need caching, but not for the same duration.** Treating their different cache policies as one interchangeable marker silently changes the user's choice.

In [LlamaIndex PR #23460](https://github.com/run-llama/llama_index/pull/23460), Nakagawa Master first [identified a five-system-message example that exceeded Anthropic's four-cache-breakpoint limit](https://github.com/run-llama/llama_index/pull/23460#issuecomment-6106281257). **Separate author @arieleven acknowledged the counterexample, [changed the deduplication behavior and added tests](https://github.com/run-llama/llama_index/pull/23460#issuecomment-6106461866).** Nakagawa Master then [identified the distinct one-hour versus five-minute TTL boundary](https://github.com/run-llama/llama_index/pull/23460#issuecomment-6107331539) that indiscriminate coalescing would lose. The [current independent implementation](https://github.com/run-llama/llama_index/blob/15475f9b493af261d16e4f04309f18d3477ef0dd/llama-index-integrations/llms/llama-index-llms-anthropic/llama_index/llms/anthropic/utils.py) coalesces only equivalent policies and preserves different TTLs.

**A different community reviewer @VANDRANKI independently found other request-wide and Bedrock integration defects** and [the PR author implemented a later, separate Bedrock fix and tests](https://github.com/run-llama/llama_index/pull/23460#issuecomment-6708681102). Those extra findings belong to that reviewer, not Nakagawa Master. [PR #23460 remains open](https://github.com/run-llama/llama_index/pull/23460), with upstream merge, official package release and affected actual-use results still pending.

## 72. Qwen Code | A cancelled AI tool loses its connection: an independent developer changed recovery after two source-specific counterexamples

**Cancelling an AI tool should not leave the next tool call disconnected—or make the cancellation wait for the repair itself.** [Qwen Code issue #12160](https://github.com/QwenLM/qwen-code/issues/12160) describes an actual MCP problem: after an in-flight request is aborted, the transport can disconnect and the surviving session inherits a broken connection.

[Nakagawa Master (Keisuke Nakagawa) identified a concrete cancellation-liveness counterexample](https://github.com/QwenLM/qwen-code/pull/16661#pullrequestreview-5818880210): if rediscovery never settles, the already-cancelled invocation must nevertheless reject promptly. **Independent author @2SinceJuly acknowledged the finding and [implemented a detached connection-repair listener with regression tests](https://github.com/QwenLM/qwen-code/pull/16661#issuecomment-6725421454)**. Repair now follows the later status transition rather than holding the cancelled call open, and the cancelled tool effect is not replayed.

Nakagawa Master then [showed why the new disconnect guard could not work against the actual raw MCP SDK Client](https://github.com/QwenLM/qwen-code/pull/16661#pullrequestreview-5820096983): the test double had `getStatus()`, but the production client did not. **The author explicitly confirmed that mismatch and [replaced the guard with an intentional-teardown signal and a red/green test using the real client shape](https://github.com/QwenLM/qwen-code/pull/16661#issuecomment-6728843638)**.

A different reviewer subsequently [identified a separate reconnect/replay path after an operator deliberately disconnects a server](https://github.com/QwenLM/qwen-code/pull/16661#discussion_r4512228062). That later finding belongs to that reviewer. [PR #16661 remains open](https://github.com/QwenLM/qwen-code/pull/16661); upstream merge, a containing release and actual affected-user recovery have not yet been established.

## 73. LiteLLM | A new AI model loses its tools: a developer adopted Nakagawa Master's missing negative condition

**A new model appears in a provider before its capabilities enter the catalog, and tool calling breaks.** In a [real LiteLLM user report #48145](https://github.com/BerriAI/litellm/issues/48145), an uncatalogued model on a JSON-defined provider failed to receive the `tools` setting; the reporter contrasted newer and older LiteLLM versions. “Not yet listed” is not the same as “known not to support tools.”

An independent developer proposed [PR #48180](https://github.com/BerriAI/litellm/pull/48180) to preserve tool parameters for unknown models. [Nakagawa Master (Keisuke Nakagawa) identified the opposite case the patch missed](https://github.com/BerriAI/litellm/pull/48180#issuecomment-6388447887): when the model is uncatalogued but the provider explicitly declares `supports_function_calling: false`, forwarding tools is also incorrect. The model-level declaration, provider-level declaration and genuinely unknown state must be separate decisions.

**The affected reporter @mramendi independently ran Nakagawa Master's credential-free diagnostic probe verbatim** and [checked the actual request boundary](https://github.com/BerriAI/litellm/issues/48145#issuecomment-6389202066): tools and reasoning effort reached LiteLLM from OpenCode but disappeared before reaching Nano-GPT. The reporter expressly described the check as “Nakagawa designed.” This is actual independent use of the Master's diagnostic and direct acknowledgment of its source, not a successful installed-user retest of PR #48180. The separate `reasoning_effort` forwarding problem is not claimed as fixed by that tool-capability PR.

**Independent author @msdianprince-7 [replied directly, “Thanks, added,” and implemented the precedence and seven combinations of tests](https://github.com/BerriAI/litellm/pull/48180#issuecomment-6458741128).** The [current code](https://github.com/BerriAI/litellm/pull/48180/files) gives an explicit model entry priority, then checks the provider declaration, and preserves tools when neither makes a negative claim. This is an independently implemented source-specific response to Nakagawa Master's finding.

[PR #48180 remains open](https://github.com/BerriAI/litellm/pull/48180); upstream merge, a containing release and the original user's successful installed-version retest are separate milestones. The boundary can be compared conceptually with the [original establishment-conditions theory](https://master.ricette.jp/theory/nakagawa-master-nakagawa-establishment-conditions-theory-01-what-is-establishment/), without claiming that the developer read or adopted that original.

## 74. PydanticAI | A stored AI-tool result changes after conversation compaction: an independent developer reproduced and fixed Nakagawa Master's counterexample

**An AI agent can appear to have saved an earlier tool result, yet later return different bytes from the same handle.** The [original PydanticAI report #12676](https://github.com/pydantic/pydantic-ai/issues/12676), filed by developer @gouyu-hou, concerned tool-call IDs being reused across different model responses. During [PR #12677](https://github.com/pydantic/pydantic-ai/pull/12677), Nakagawa Master (Keisuke Nakagawa) [identified a further, distinct failure](https://github.com/pydantic/pydantic-ai/pull/12677#pullrequestreview-5795751398): counting prior calls from retained chat messages cannot preserve uniqueness when `SummarizingCompaction` removes those very messages before another response reuses an ID.

**The independent developer [confirmed the finding directly and reproduced it with a real Agent](https://github.com/pydantic/pydantic-ai/pull/12677#issuecomment-6688486077)** combining `ToolOutputLimits(Spill)` and `SummarizingCompaction`: three oversized results left only two files, and the first file now contained a later result. The developer wrote [commit 7390c19](https://github.com/pydantic/pydantic-ai/commit/7390c19abd1ac8008455cd5b616a349a9fa4fa9a) to use a stable run-step identifier instead of an occurrence count reconstructed from mutable chat history, and added a regression test driving the compaction case.

The [author's subsequent test report](https://github.com/pydantic/pydantic-ai/pull/12677#issuecomment-6701058871) documents further validation. As checked on November 10, 2026, **PR #12677 remains open**; merge, a release containing the fix, and affected users' recovery in an installed version are not established. The developer originated the base repeated-ID investigation and authored the actual code. Nakagawa Master's separately identified contribution was the specific history-compaction inverse and its falsifiable acceptance test.

For readers exploring the distinction between a retained record and later reconstructed context, this engineering incident has an optional conceptual reading alongside [Nakagawa Master's original Reconstructive Memory Structure theory](https://master.ricette.jp/theory/nakagawa-master-reconstructive-memory-structure/). This does not claim that the independent developer read that original or derived the patch from it.

## 75. LangGraph | The AI asks again, you answer 7, but it uses the earlier 5: an independent author implements Nakagawa Master's two acceptance contracts

**An AI agent asks you for a new answer. You say 7, but its final work still uses your earlier 5.** The [actual LangGraph bug report #9478](https://github.com/langchain-ai/langgraph/issues/9478) reproduces exactly that sequence. When a subgraph under a retry policy fails, a scratchpad counter assigns the retried subgraph a new checkpoint namespace, while a later resume reads the old attempt. The second user answer is silently ignored.

[Nakagawa Master (Keisuke Nakagawa) identified two distinct, coherent acceptance contracts in a source-specific review](https://github.com/langchain-ai/langgraph/issues/9478#issuecomment-6490409757): **(A)** if the system asks only once, retry the failed check using the original answer 5; **(B)** if it asks twice, use the newly submitted answer 7 in the next check. Asking twice but using 5 violates both. He called for the number and identity of prompts, accepted answers, checkpoint namespace and actual check calls to be tested together.

**Independent developer @PierfrancescoLijoi [explicitly cited the two alternatives Nakagawa Master distinguished](https://github.com/langchain-ai/langgraph/issues/9478#issuecomment-6753760773) and implemented both as separate variants.** The [latest self-authored fork commit 385e122](https://github.com/PierfrancescoLijoi/langgraph/commit/385e122bb33caa14991c13183435ca25e14971f1) chooses contract B, resetting both interrupt and subgraph counters and starting the retried subgraph anew. The author's observed trace asks twice, checks on [5, 7], and finally returns 7. The author reports **84 sync/async, checkpointer and durability tests**, with 48 failing on the original branch and all 84 passing on the fork; the public archive has not independently executed the suite.

**Upstream adoption has not occurred.** [PR #9656](https://github.com/langchain-ai/langgraph/pull/9656) was [automatically closed, unmerged](https://github.com/langchain-ai/langgraph/pull/9656#issuecomment-6748264321) under an issue-assignment rule. Importantly, its frozen PR diff still shows the older **contract A** variant, while contract **B is in the developer's later fork**. The author also reports unsolved concurrent-subgraph namespace mixing and a separate durability limitation. The author, not Nakagawa Master, wrote the software and tests.

For a wider original discussion of how reconstructed context must not be mistaken for an unchanged record, readers can independently examine [Nakagawa Master's original Reconstructive Memory Structure theory](https://master.ricette.jp/theory/nakagawa-master-reconstructive-memory-structure/). The developer did not claim to read that original. The source proves a concrete outside engineering response to Master's two-contract distinction, not merge, released end-user recovery or personal endorsement.

## What the public source record reveals

### Supported by the linked public record

Across multiple independent GitHub repositories, public records show one or more of the following after specific `Nakagawa-master` comments or reviews:

- explicit third-party acknowledgment or restatement;
- code, test, documentation, or UI changes;
- source attribution in a PR or commit;
- merge, backport, release, or deployment in specific cases;
- independent verification by another reviewer;
- reuse of the same distinction on another PR.

Each section states exactly which of those are verified for that case.

## How to verify a case yourself

For any case:

1. open the original `Nakagawa-master` comment or review;
2. read the third-party author/owner/reviewer response;
3. inspect the PR diff, commits, and tests;
4. check the PR state for merge status;
5. verify releases or deployments separately when claimed;
6. do not infer a causal relationship from unrelated later changes when the source relationship is not explicit.

Counterexamples, non-fit cases, and failed reproductions are also relevant evidence.

## Related public material

- [Independent AI engineering media coverage in English and French, including external editorial review, real deployment and evidence limits](INDEPENDENT_MEDIA_COVERAGE.md)
- [Who Is Nakagawa Master?](ABOUT_NAKAGAWA_MASTER.en.md)
- [Start Here](START_HERE.md)
- [Practical Use & Collaboration Entry](PRACTICAL_USE.md)
- [Nakagawa Structural OS — Applied Evidence Map](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md)
- [Independent Verification & Reuse Protocol](INDEPENDENT_VERIFICATION_REUSE.md)
- [Independent reproduction, counterexample and actual-use submission form](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml)
- [Public dialogue entry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/399)

Follow the original public contribution, the receiving developers' responses, their code and tests, and the resulting repository state to examine the real trajectory of each idea.
