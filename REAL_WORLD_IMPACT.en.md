# Publicly Verifiable External Implementation Cases | Changes Recorded After Nakagawa Master Comments

Language: [日本語](REAL_WORLD_IMPACT.md) | **English** | [中文](REAL_WORLD_IMPACT.zh.md)

**Last checked: 2026-09-18**

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

**Surface:** [damianvtran/local-operator#1282](https://github.com/damianvtran/local-operator/issues/1282) → [PR #1291](https://github.com/damianvtran/local-operator/pull/1291)  
**Current state:** PR #1291 open / unmerged

Issue #1282 described a boundary where a running agent constrained by an approval policy must not be able to lower that same gate from `ask` to `auto` through a configuration path it can write, while explicit human/operator control still needs to remain available.

- [issue #1282](https://github.com/damianvtran/local-operator/issues/1282)
- [third-party PR #1291](https://github.com/damianvtran/local-operator/pull/1291)

The third-party PR explicitly states `Closes #1282` and makes the source of a live approval-policy transition part of the decision. Raw config writes from another process cannot loosen the running gate, while an explicitly attributed operator action in the process that owns the gate still has a positive-control path. The PR also includes a real second-process regression and tests intended to prevent agent-facing code from manufacturing the trusted settings-write path.

Nakagawa-master re-checked the current head against the original issue boundary and explicitly recorded that the original security finding is implemented.

- [closure review](https://github.com/damianvtran/local-operator/pull/1291#pullrequestreview-5253448083)

**Publicly verifiable here:** issue → dedicated third-party PR explicitly closing that issue → code/tests → multiple review/remediation rounds → origin-side closure review.  
**Not established here:** merge, release, or user-scale outcomes.

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
