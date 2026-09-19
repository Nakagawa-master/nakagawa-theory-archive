# Publicly Verifiable External Implementation Cases | Changes Recorded After Nakagawa Master Comments

Language: [日本語](REAL_WORLD_IMPACT.md) | **English** | [中文](REAL_WORLD_IMPACT.zh.md)

**Last checked: 2026-09-19**

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
**Current state:** open / draft / unmerged

A `Nakagawa-master` review identified that producer-authored evidence should not be presented as if it had been independently measured by the system.

- [Nakagawa-master review](https://github.com/PostHog/posthog/pull/92252#pullrequestreview-5233849200)

The PR author later added server-side measurement, regression coverage, and UI distinctions such as `Measured by PostHog` versus `Unverified`.

**Publicly verifiable here:** review followed by third-party code / test / UI changes.  
**Not established here:** merge, release, production deployment, or user scale.

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
**Current state:** both open / unmerged

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
**Not established here:** merge or release of either PR.

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

PR #1324 implements a per-session operator capability, connection-bound proofs, a common pre-dispatch guard, and explicit negative, positive, and tightening controls. It has also gone through multiple independent review, QA, design, and UX remediation rounds. On current head `fe2dc9b6`, Nakagawa-master re-checked the five acceptance conditions from the origin issue and recorded origin-side closure of the original #1310 boundary. That review is not a merge recommendation; the PR remains open for the operator/product decision documented by the repository.

- [origin-side closure review](https://github.com/damianvtran/local-operator/pull/1324#pullrequestreview-5257968951)

**Publicly verifiable in this follow-up:** origin issue → independent third-party reproduction → correction of the origin diagnosis → independent discovery of a stronger sibling bypass → third-party implementation → multiple independent remediation rounds → origin-side closure.  
**Not established yet:** merge/release of #1324, a guarantee on host configurations where the OS itself cannot isolate same-uid memory, completion of device-bound phone authority, or independent reuse of this boundary in another project.


## 12. MemberJunction | Row contents protected, then the remaining row-identity boundary carried into a second work item

**Surface:** [MemberJunction/MJ#4595](https://github.com/MemberJunction/MJ/pull/4595) → [issue #4610](https://github.com/MemberJunction/MJ/issues/4610)  
**Current state:** PR #4595 open / unmerged; issue #4610 open

PR #4595 stopped full row contents from riding an unfiltered cache-invalidation broadcast by default. A later `Nakagawa-master` review separated that fix from a remaining metadata boundary: even without `recordData`, a session could still learn another row's stable primary key and mutation timing.

- [Nakagawa-master row-identity review](https://github.com/MemberJunction/MJ/pull/4595#issuecomment-5253531713)
- [Nakagawa-master two-layer follow-up](https://github.com/MemberJunction/MJ/pull/4595#issuecomment-5737565146)
- [third-party implementation / carry response](https://github.com/MemberJunction/MJ/pull/4595#issuecomment-5737603820)
- [follow-up issue #4610](https://github.com/MemberJunction/MJ/issues/4610)

The PR author explicitly adopted the two-layer split: an entity-level permission filter was implemented in commit `293b9b40`, and the stronger row-level disclosure question was opened separately as #4610 instead of weakening the regression until it passed. The issue body says its framing is largely from `@Nakagawa-master`'s review and preserves the two-disjoint-row-visibility acceptance test.

A later public contribution on #4610 mapped the follow-up onto MemberJunction's existing ClassFactory extension pattern, keeping the per-subscriber path synchronous and no-I/O rather than routing it through the async permission engine.

- [implementation-shape contribution on #4610](https://github.com/MemberJunction/MJ/issues/4610#issuecomment-5739586260)

**Publicly verifiable here:** review → third-party code/test change → third-party explicit source attribution → second work item carrying the stronger boundary and regression.  
**Not established here:** row-level policy implementation, merge of #4595, merge/closure of #4610, release, deployment, or user-scale impact.

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
