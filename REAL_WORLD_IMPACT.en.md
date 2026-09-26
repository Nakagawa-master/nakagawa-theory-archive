# Publicly Verifiable External Implementation Cases | Changes Recorded After Nakagawa Master Comments

Language: [日本語](REAL_WORLD_IMPACT.md) | **English** | [中文](REAL_WORLD_IMPACT.zh.md)

**Last checked: 2026-09-25**

Nakagawa Master is the pen name of Keisuke Nakagawa. On social media, the name “マスター” (“Master”) is also used; some external posts use “MasterJP.”

This page is a **public verification guide**. It links public GitHub comments or reviews made under the `Nakagawa-master` account to later changes that can be checked in third-party repositories.

It is not an impact score, an authority claim, or a claim that an entire project or theory system was adopted. Each case is separated into:

1. the original public contribution;
2. the third party's response or change;
3. the current repository state;
4. what remains unverified.

A comment is not the same as an implementation. An implementation is not the same as a merge. A merge is not the same as a release, deployment, or verified use.

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

---

## 1. PostHog | Separate producer-supplied evidence from PostHog's own measurement

**Surface:** [PostHog/posthog#92252](https://github.com/PostHog/posthog/pull/92252)  
**Current state:** open / unmerged

A `Nakagawa-master` review identified that producer-authored evidence should not be presented as if it had been independently measured by the system.

- [Nakagawa-master evidence review](https://github.com/PostHog/posthog/pull/92252#pullrequestreview-5233849200)
- [Nakagawa-master capability-boundary review](https://github.com/PostHog/posthog/pull/92252#pullrequestreview-5245587245)

The PR author later added server-side measurement, regression coverage, and UI distinctions such as `Measured by PostHog` versus `Unverified`.

A second review separated a narrow capability from a user-grantable capability. The current PR also makes `hog_flow_proposal` programmatic/internal, removes it from ordinary personal-key/OAuth/session grant surfaces, and treats it as a server-minted scout scope.

- [server-side measurement commit `721311a9`](https://github.com/PostHog/posthog/commit/721311a97488781dd590708abe697480c5c0e9e8)
- [programmatic-only scope commit `3ecb122d`](https://github.com/PostHog/posthog/commit/3ecb122dd7062d864c135213282613bfc80a2ebf)
- [server-minted scope commit `d962e51c`](https://github.com/PostHog/posthog/commit/d962e51c22e34f526f94ce6d581aa429ed7d87a3)

Those commit messages do not identify the `Nakagawa-master` reviews as the sole cause. This page therefore records that matching third-party implementation changes occurred after the reviews, without claiming exclusive causality.

**Publicly verifiable here:** review followed by third-party code / test / UI / scope-boundary changes.  
**Not established here:** merge, release, production deployment, user scale, or exclusive causality.

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
**Not established here:** user scale or broad adoption outside this project.

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
**Not established here:** fleet-wide results or market-wide adoption.

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
**Not established here:** merge, release, or deployment.

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
**Not established here:** release/downstream use of #4487, merge of #4524 (closed unmerged), or intellectual priority for the general API-compatibility principle.

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
**Not established here:** user-scale outcomes or further reuse by a different person/context.

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
**Not established here:** release, production deployment, or user scale.

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
**Not established here:** production deployment against a real provider or user scale.

---

## 9. Replay | Separate historical consent records from current eligibility

**Surface:** [aferna6-cell/Replay#67](https://github.com/aferna6-cell/Replay/issues/67)  
**Current state:** design direction accepted in the issue; repository code implementation not verified

The public contribution proposed keeping the historical consent event while separately evaluating whether the material is currently eligible for retention, processing, or use.

- [Nakagawa-master contribution](https://github.com/aferna6-cell/Replay/issues/67#issuecomment-5689647722)
- [repository-owner response](https://github.com/aferna6-cell/Replay/issues/67#issuecomment-5689719035)

The repository owner explicitly identified the source and restated the distinction as part of the project's protocol design.

**Publicly verifiable here:** comment → owner acknowledgment and protocol-level adoption.  
**Not established here:** schema/code/tests, merge, release, or real-data operation.

---

## 10. Cline | Make delegated child capabilities visible at approval time

**Surface:** [cline/cline#14225](https://github.com/cline/cline/pull/14225)  
**Current state:** base PR merged; follow-up implementation of this proposal not verified

A `Nakagawa-master` review proposed that a person approving delegation should be able to see the effective capability set that will be available to the child agent.

- [Nakagawa-master review](https://github.com/cline/cline/pull/14225#pullrequestreview-5242232355)
- [external-author response](https://github.com/cline/cline/pull/14225#issuecomment-5723653394)

The external author named `@Nakagawa-master`, described the proposal as better UX than the current behavior, and stated an intention to include it in future agent-config work.

The base PR itself is merged, but that merge does not mean this proposal was implemented.

**Publicly verifiable here:** named review plus explicit author acknowledgment and follow-up intent.  
**Not established here:** a follow-up issue/PR, code/tests/UI implementation, or release.

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
**Not established here:** effect at broader user scale, user counts, or independent downstream reuse beyond this release.

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


## 12. MemberJunction | Row contents protected, then the remaining row-identity boundary carried into a second work item

**Surface:** [MemberJunction/MJ#4595](https://github.com/MemberJunction/MJ/pull/4595) → [issue #4610](https://github.com/MemberJunction/MJ/issues/4610)  
**Current state:** PR #4595 merged on 2026-09-23; issue #4610 open

PR #4595 stopped full row contents from riding an unfiltered cache-invalidation broadcast by default. A later `Nakagawa-master` review separated that fix from a remaining metadata boundary: even without `recordData`, a session could still learn another row's stable primary key and mutation timing.

- [Nakagawa-master row-identity review](https://github.com/MemberJunction/MJ/pull/4595#issuecomment-5253531713)
- [Nakagawa-master two-layer follow-up](https://github.com/MemberJunction/MJ/pull/4595#issuecomment-5737565146)
- [third-party implementation / carry response](https://github.com/MemberJunction/MJ/pull/4595#issuecomment-5737603820)
- [follow-up issue #4610](https://github.com/MemberJunction/MJ/issues/4610)

The PR author explicitly adopted the two-layer split: an entity-level permission filter was implemented in commit `293b9b40`, and the stronger row-level disclosure question was opened separately as #4610 instead of weakening the regression until it passed. The issue body says its framing is largely from `@Nakagawa-master`'s review and preserves the two-disjoint-row-visibility acceptance test.

A later public contribution on #4610 mapped the follow-up onto MemberJunction's existing ClassFactory extension pattern, keeping the per-subscriber path synchronous and no-I/O rather than routing it through the async permission engine.

- [implementation-shape contribution on #4610](https://github.com/MemberJunction/MJ/issues/4610#issuecomment-5739586260)

**Publicly verifiable here:** review → third-party code/test change → third-party explicit source attribution → #4595 merge → second work item carrying the stronger boundary and regression.  
**Not established here:** row-level policy implementation, merge/closure of #4610, release, deployment, or user-scale impact.

---

## 13. Waves Customer Portal | Preserve payment proof while removing a newly unsafe estimate CTA

**Surface:** [wavespestcontrolfl/waves-customer-portal#4608](https://github.com/wavespestcontrolfl/waves-customer-portal/pull/4608)  
**Current state:** merged on 2026-09-19

The PR introduced a delivery-time guard for estimate links and a special rewrite policy for payment receipts: if an estimate CTA is no longer safe to expose, the receipt should still be sent with that CTA removed rather than suppressing proof of payment.

A `Nakagawa-master` review found a vocabulary mismatch in that rewrite path. The refusal guard recognized a short code minted for another entity when its `target_url` resolved to an estimate link, but `rewriteWithheldEstimateLinks()` rewrote only short codes directly typed as `entity_type='estimates'`. The same link form could therefore be classified as unsafe but not transformed, causing the receipt to be refused.

- [Nakagawa-master review](https://github.com/wavespestcontrolfl/waves-customer-portal/pull/4608#pullrequestreview-5254456120)

After that review, commit `029ae44d53` explicitly added the missing `target_url` short-link rewrite path. The current merged implementation resolves both direct estimate short codes and other short codes whose target URL embeds an estimate link, strips the unsafe literal link, preserves the receipt, and records the rewritten estimate id. The PR later merged as `5cecd7627b70d739d7feaf6f45fd784b5741efc3`.

**Publicly verifiable here:** review → matching code/test change for the reported short-link mismatch → merge.  
**Not established here:** production deployment, user-scale outcomes, or whole-project endorsement of any broader theory.

---

## 14. UpGrade | A UI-only delete rule became a backend-authority work item

**Surface:** [CarnegieLearningWeb/UpGrade#3323](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323) → [issue #3326](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326)  
**Current state:** #3323 open; #3326 open / implementation pending

A `Nakagawa-master` review found that the product's frontend delete-permission matrix was not enforced by the backend. In the reviewed branch, an authenticated Reader could directly call destructive single/batch APIs even though the UI hid Delete.

- [Nakagawa-master review](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323#pullrequestreview-5249193998)
- [third-party author response](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323#issuecomment-5732584639)
- [follow-up issue #3326](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326)
- [implementation-shape contribution on #3326](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326#issuecomment-5740003355)

The PR author explicitly named `@Nakagawa-master`, confirmed that the routes had historically lacked role enforcement, and opened #3326 to enforce the role matrix and state rules across both single and batch deletion rather than keeping two inconsistent behaviors.

The later #3326 contribution mapped that work onto the current branch: one shared backend deletion policy, evaluated against current locked target state before mutation, with policy refusals separated from operational deletion failures.

**Publicly verifiable here:** review → author acknowledgment/restatement → dedicated child work item preserving the boundary → source-level implementation guidance.  
**Not established here:** code/test implementation of #3326, merge, release, deployment, or user-scale effect.

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
**Not established here:** sole causation, production launch, customer-scale effect, independent reuse by a different person, industry-wide reuse, or endorsement of the broader theory corpus.

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
**Not established here:** the #23083 contract decision, follow-up code/tests, merge, release, deployment, or user-scale effect.

---

## 17. Publications | Separate reversibility from authority increase, then reuse the boundary in another document

**Surface:** [kishibashi3/publications#52](https://github.com/kishibashi3/publications/pull/52) → [PR #57](https://github.com/kishibashi3/publications/pull/57) → [PR #58](https://github.com/kishibashi3/publications/pull/58)  
**Current state:** #57 merged / GitHub Pages deployment verified; #58 merged / reused inside the same receiver's separate document

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

**Publicly verifiable here:** origin-preserved review → third-party restatement → dedicated reader-facing implementation → merge / Pages deployment → reuse as a consistency rule in another document inside the same receiver → merge.  
**Not established here:** that #58 is a second independent public-site publication, carry by a different receiver, broad reader response, mass human recognition, or endorsement of the full theory corpus.

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
**Not established here:** merge, release, production deployment, user scale, or exclusive causality.

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

This case is stronger than a mere temporal sequence: the receiver's own commit explicitly attributes the two concrete hardenings to the `@Nakagawa-master` review. That is evidence about this specific artifact change, not a claim of intellectual priority over the general security principle or adoption of the broader theory system.

**Publicly verifiable here:** review → explicit third-party agreement/restatement → implementation commit explicitly naming the review as the source of the two hardenings → concrete reader-facing teaching change.  
**Not established here:** merge, release/deployment, reader scale, intellectual priority over the general principle, or endorsement of the full theory corpus.

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
**Not established here:** production deployment, user-scale effect, intellectual priority over the general temporal-data principle, or endorsement of the full theory corpus.

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
**Not established here:** downstream adoption or user scale of this particular fix, a release of the fix into other repositories using `@memberjunction/standards`, intellectual priority over the general API-compatibility principle, or endorsement of the full theory corpus.

---

## What this page supports — and what it does not

### Supported by the linked public record

Across multiple independent GitHub repositories, public records show one or more of the following after specific `Nakagawa-master` comments or reviews:

- explicit third-party acknowledgment or restatement;
- code, test, documentation, or UI changes;
- source attribution in a PR or commit;
- merge, backport, release, or deployment in specific cases;
- independent verification by another reviewer;
- reuse of the same distinction on another PR.

Each section states exactly which of those are verified for that case.

### Not established by this page alone

This page does not establish:

- that the entire Nakagawa Master theory corpus is correct;
- that any third-party project endorses the theory corpus as a whole;
- industry-wide adoption;
- user counts, revenue, or societal impact without direct evidence;
- future merge of open/draft PRs;
- production effect where release/deployment/use has not been separately verified.

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

- [Who Is Nakagawa Master?](ABOUT_NAKAGAWA_MASTER.en.md)
- [Start Here](START_HERE.md)
- [Practical Use & Collaboration Entry](PRACTICAL_USE.md)
- [Nakagawa Structural OS — Applied Evidence Map](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md)
- [Independent Verification & Reuse Protocol](INDEPENDENT_VERIFICATION_REUSE.md)
- [Public registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)
- [Public dialogue entry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/399)

This page is not asking readers to trust a name or a count. It is an index for checking the original public contribution, the third party's response, the actual change, and the repository state for themselves.

---

## 22. Qwen Code | Approval boundary for paid Batch API actions

**Target:** [QwenLM/qwen-code#12492](https://github.com/QwenLM/qwen-code/pull/12492)  
**Current state:** merged and released in Qwen Code v0.24.6 (2026-09-26 JST) / merge commit `c3a4058a0c72`

[Nakagawa-master's public comment](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5817569552) separated approval of `qwen batch run` from approval of the concrete billed batch snapshot. The proposed contract binds the exact item set, frozen settings and cost estimate to a canonical digest, and treats later drift as stale approval.

Third-party developer `yiliang114` attributed and adopted the proposal, implementing a preview, snapshot digest, pre-submit revalidation and regression tests in `3d06e1ad8e`. The author described this as a lighter form of the full proposed flow.

- [third-party response](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5817836928)
- [adoption response](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5818159716)
- [implementation commit `3d06e1ad8e`](https://github.com/QwenLM/qwen-code/commit/3d06e1ad8e749c647a2eb5d447b867fc50955a13)
- [maintainer verification at head `206a444b`](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5836312195)
- [merge commit](https://github.com/QwenLM/qwen-code/commit/c3a4058a0c7207de7b421e9da0622a9ec890dbad)
- [Qwen Code v0.24.6 release](https://github.com/QwenLM/qwen-code/releases/tag/v0.24.6)

The author fixed the three maintainer-requested pre-merge findings in `56f06075b3` and two additional suggestions in `206a444b30`. Qwen Code CI (run 43130) and TUI parity (run 3993) passed on the current head. The maintainer judged head `206a444b` mergeable; the PR merged on 2026-09-26 JST and shipped in v0.24.6 that day. Non-blocking follow-ups remain in [#12707](https://github.com/QwenLM/qwen-code/issues/12707).

**Confirmed by the public record:** source-attributed third-party adoption, implementation of the proposed approval boundary, PR merge and release. A real paid use at an earlier PR head is also documented.  
**Not yet confirmed:** independent production use of v0.24.6, broad reader propagation, or endorsement of the wider theory system. The entire PR, later fixes and release are not attributed to Nakagawa-master alone.


---


## 23. AI-News | Separate URL count from independent evidence-root count in recurring editorial verification

**Target:** [022740mix-spec/AI-News#124](https://github.com/022740mix-spec/AI-News/issues/124) → [PR #131](https://github.com/022740mix-spec/AI-News/pull/131)  
**Current state:** explicitly adopted by the receiver / implementation draft in CLAUDE.md / open and unmerged

In issue #124, `Nakagawa-master` proposed separating the number of URLs from the number of independent evidence roots in AI-news verification. The proposal distinguishes primary sources, independent observations, derived/syndicated material and unknown lineage, rather than treating `url_count` as `evidence_root_count`.

- [origin issue #124](https://github.com/022740mix-spec/AI-News/issues/124)

The repository owner later explicitly said the proposal was adopted and distinguished this rule change from an earlier unrelated article update. The response explains that the existing L2/L3 checks verified whether information appeared in a source but did not test whether sources were independent; an audit also found ten articles that had relied on agreement across multiple media outlets as evidence.

- [receiver adoption / rationale](https://github.com/022740mix-spec/AI-News/issues/124#issuecomment-5823549498)

Draft PR #131 implements the distinction in the repository's recurring `CLAUDE.md` editorial-verification rules. It aligns terminology with W3C PROV-O where possible, adds operational cases such as wire-service republication and regulatory filings, and requires draft PRs to record the root breakdown for material claims.

- [implementation draft PR #131](https://github.com/022740mix-spec/AI-News/pull/131)

**Publicly verifiable here:** origin-preserved proposal → explicit receiver adoption and rationale → concrete implementation in a recurring editorial rule draft.  
**Not established yet:** merge of PR #131, repeated use after merge, effect on error rate, reader scale, independent reuse by another receiver, or endorsement of the wider theory corpus.


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
