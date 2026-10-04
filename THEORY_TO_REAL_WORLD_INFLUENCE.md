# From Theory to Real-World Influence

## Why these external cases matter to Nakagawa Master’s credibility

This page is a public, non-canonical bridge between the Nakagawa Master theory archive and independently inspectable real-world effects.

It does **not** claim that every external contributor endorses Nakagawa Master, that every example proves an entire theory, or that provenance itself proves correctness.

Its purpose is narrower:

> show how recurring structural distinctions originating in the Nakagawa Master theory corpus can be applied to different real problems, independently restated by third parties, and carried into implementation, review, publication, or operational change.

The important chain is not:

```text
theory page
→ publicity
```

It is:

```text
theory / structural distinction
→ concrete real-world problem
→ independent third-party interpretation
→ changed implementation / review / protocol / publication
→ later reuse or second-person carry
→ origin remains inspectable
→ readers can return to the underlying theory
```

That is the causal bridge between theory and influence.

---

## 90-second verification route

If you only have a minute or two, do not start by asking whether the archive's self-description sounds persuasive. Check four different kinds of receiver behavior.

### A. Did an external receiver actually change implementation?

**Qwen Code #12492** provides a compact source-to-implementation chain:

```text
public Nakagawa Master authority distinction
→ concrete code-level review on a paid Batch workflow
→ receiver implementation 37m 08s later
→ regression tests
→ merge
→ stable v0.24.6 release
```

Primary records:
- [Nakagawa-master review](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5817569552)
- [Receiver implementation commit `3d06e1ad`](https://github.com/QwenLM/qwen-code/commit/3d06e1ad8e749c647a2eb5d447b867fc50955a13)
- [Merged PR #12492](https://github.com/QwenLM/qwen-code/pull/12492)
- [Stable release v0.24.6](https://github.com/QwenLM/qwen-code/releases/tag/v0.24.6)
- [Receiver operational-use record #12825](https://github.com/QwenLM/qwen-code/issues/12825) — the same receiver later documents using the released `/batch-api` executor for a real nine-document DashScope Batch job

This establishes a bounded implementation → release → real receiver-side operational-use chain. The operational-use record is from the same receiver/collaborator, not an independent external user, and it does not establish user scale or how many users noticed the source relation.

### B. Did the receiver later preserve the explicit source relation to Nakagawa Master on its own?

A later, separately authored and merged Qwen Code PR, **#12895**, describes a budget defect and explicitly states that **Nakagawa-master pointed out that the old gate broke the meaning of `maxCostUsd`, not merely its wording**.

Primary records:
- [Qwen Code #12895](https://github.com/QwenLM/qwen-code/pull/12895) — merged 2026-09-28
- [Stable release v0.24.7](https://github.com/QwenLM/qwen-code/releases/tag/v0.24.7) — published 2026-09-29 and includes the #12895 merge commit
- [Qwen release confirmation on PR #12895](https://github.com/QwenLM/qwen-code/pull/12895#issuecomment-5892305970) — the repository's release bot records “Released in v0.24.7” directly on the same PR thread

The release tag is 49 commits ahead of and 0 behind the #12895 merge commit `7e50eee804dbf864db97a8d18793ed45aef698d5`, and the PR thread itself now carries the repository's stable-release confirmation. This shortens the verification path from the receiving-project Origin rereference to stable distribution. The bot confirmation is distribution evidence, not a new human explicit rereference to Nakagawa Master.

The useful signal is narrower than endorsement: the receiving-project artifact voluntarily preserves the explicit source relation to Nakagawa Master while turning the boundary into code, tests, docs, merge, and stable release. This still does not establish how many users encountered the change, noticed the source relation, or formed any view about Nakagawa Master.

A later, different Qwen defect now provides a second compact source-preserving implementation chain. In **Qwen Code #13241**, a late Host result could no longer change the answer after cancellation/recovery, but its late usage report could still write into the live budget ledger and affect current work. Nakagawa Master proposed the narrower boundary that a terminalized attempt loses budget-affecting write authority; any later physical-spend observation should be separated from the execution budget if the project needs to retain it.

The receiver's own PR description explicitly says that the current revision implements **“the option-A recommendation from @Nakagawa-master”** and separately records that this was an external technical recommendation rather than repository-maintainer authority. The receiver then added code/tests, reported Web Shell and native Host checks, received a human approval from reviewer `qqqys`, and merged the PR on 2026-10-04.

Primary records:
- [Option-A technical recommendation](https://github.com/QwenLM/qwen-code/pull/13241#discussion_r4172301736)
- [Attribution clarification](https://github.com/QwenLM/qwen-code/pull/13241#discussion_r4172530358)
- [Receiver implementation commit](https://github.com/QwenLM/qwen-code/commit/bb5c5d74b7368610a7dd20d0af532f36ad335fe2)
- [Receiver Web Shell + native Host verification](https://github.com/QwenLM/qwen-code/pull/13241#issuecomment-5970236028)
- [Merged PR #13241](https://github.com/QwenLM/qwen-code/pull/13241)
- [Human-readable explanation](human-translation/entry-stories/10-started-revision-does-not-authorize-current-state.md)

This is useful here because the source relation survives **another concrete problem and another implementation path**, rather than only one earlier Qwen case. It establishes source-preserving implementation and merge for this bounded defect.

The relation then survived **after merge and outside the PR thread**. In the original bug issue, Qwen receiver `yiliang114` independently re-checked current `main`, verified that #13241 had removed the reported behavior, and explicitly wrote that the late-usage policy was **“option A, which @Nakagawa-master picked in the #13241 review thread.”** That is a later receiver-authored person-Origin rereference tied to the implemented decision, not merely a source line left inside the merged PR description.

Additional primary record:
- [Post-merge Qwen issue re-check and Origin rereference](https://github.com/QwenLM/qwen-code/issues/13238#issuecomment-5981371808)
- [Resolved source issue #13238](https://github.com/QwenLM/qwen-code/issues/13238)

This advances the evidence from source-preserving merge to **later same-receiver voluntary Origin rereference on a separate thread**. It still does **not** establish a release containing #13241, independent real-user use, broad audience reach, cross-receiver reuse of this exact boundary, or broad person recognition.

### C. Does the Origin relation survive independent disagreement?

In **in-c0/tuned#1**, the independent receiver did **not** adopt the proposed central-register implementation. It nevertheless judged the underlying distinction sound, explained why it rejected that implementation shape, and then referred to Nakagawa-master and the already-declined suggestion again in the next autonomous run without a new Nakagawa prompt.

Primary records:
- [Source comment](https://github.com/in-c0/tuned/issues/1#issuecomment-5742653334)
- [Receiver run 176: distinction sound, implementation shape declined](https://github.com/in-c0/tuned/issues/1#issuecomment-5745752925)
- [Receiver run 177: later prompt-free rereference](https://github.com/in-c0/tuned/issues/1#issuecomment-5747613714)

This matters because a credible evidence page should not count only successful adoption. Independent disagreement with preserved Origin is evidence of processing; it is not implementation credit.

### D. Can the same Origin-boundary survive a second person's independent re-check?

In **Qwen Code #12582**, Nakagawa-master raised a new current-authority boundary after execution placement became mutable: an already-issued multi-day share can remain valid even after the same agent moves from local execution to a managed runtime.

The PR author replied **“@Nakagawa-master Good catch”** and changed the frozen contract plus the English and Chinese share UI so the live-policy consequence is explicit.

A different reviewer, **chiga0**, then independently re-read the relevant execution and lease paths and explicitly included a section titled **“Nakagawa-master question — A2A grant + execution placement.”** The reviewer reconstructed the same live-policy consequence and said the placement-change surface should be disclosed explicitly.

Primary records:
- [Nakagawa-master review](https://github.com/QwenLM/qwen-code/pull/12582#pullrequestreview-5364710354)
- [PR-author response and receiver change](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5911699280)
- [Second-reviewer Origin re-check at `7c42221c`](https://github.com/QwenLM/qwen-code/pull/12582#pullrequestreview-5368431439)
- [Same reviewer current-head APPROVED re-check at `f9922e44`](https://github.com/QwenLM/qwen-code/pull/12582#pullrequestreview-5368634260)
- [Qwen Code #12582](https://github.com/QwenLM/qwen-code/pull/12582)

The first second-person review was submitted as an approval at head `7c42221c` and was dismissed when the PR head moved. The same reviewer, `chiga0`, then re-read the later delta and submitted a fresh **APPROVED** review at head `f9922e44`.

That makes the second-person carry stronger than a one-head snapshot: the reviewer independently reconstructed the Nakagawa-origin boundary, then continued reviewing the line after later receiver changes. It is still **not merge credit**. The PR remains open and the repository's separate code-owner / maintainer review gate is not established as complete by this review alone.

A later #12582 closeout produced a different, narrower Origin-preserved effect. When F3 had two separable halves — a declared-tool/runtime mismatch and a wider guard-before-permission ordering change — Nakagawa-master explicitly asked to land only the tool-filter half in #12582 and move the ordering half to a separate pass. Receiver `yiliang114` implemented that scope correction, centralized the Host read-only set in `AGENT_HOST_TOOL_NAMES`, and created [issue #13157](https://github.com/QwenLM/qwen-code/issues/13157). The new issue explicitly names the **“scope correction from Nakagawa-master”** as the reason the ordering change was removed from #12582.

Qwen triage then independently verified the follow-on problem: 10 of 30 scripted out-of-workspace probes had ended the whole Host turn through permission auto-reject, and the late guard's `permissionChecked: true` short-circuit explained why confinement was not re-established. The triage accepted #13157 as the sanctioned home for that half of F3.

Primary records:
- [F3 split decision](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5929070877)
- [scope correction](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5931180237)
- [receiver implementation of the split](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5931659514)
- [receiver-created #13157](https://github.com/QwenLM/qwen-code/issues/13157)
- [independent Qwen triage root-cause confirmation](https://github.com/QwenLM/qwen-code/issues/13157#issuecomment-5931968614)
- [second-person independent reconstruction by doudouOUC](https://github.com/QwenLM/qwen-code/issues/13157#issuecomment-5932126929)

A separate reviewer, `doudouOUC`, then reconstructed the mechanism from the then-current head `d8f27bf2` and explicitly agreed with the narrower Nakagawa-master contract `one final invocation identity → one authority decision → execution of that same identity`. The reviewer also translated it into an implementation rule: an allow attestation may be reused only while the policy-relevant invocation identity is unchanged; changes to args, cwd, session, or related context invalidate it and require re-evaluation. This is a second-person technical carry, not the receiver repeating its own decision.

The receiver then chose a narrower alternative on the PR branch. Commit [`b4a13e44`](https://github.com/QwenLM/qwen-code/commit/b4a13e448a6e79bd766f2a7566155d0afd205362) preserves the normal permission/final-guard ordering but changes automatic Agent Host refusal into a recoverable `EXECUTION_DENIED`, with regression coverage proving the rejected tool does not execute and a later allowed read-only tool can continue. This resolves the original fatal turn-recovery symptom without pulling the ordering change back into #12582.

Nakagawa-master rechecked that new baseline and explicitly separated the remaining questions: update the now-stale PR description, and re-evaluate #13157 as a policy/diagnostic ordering question rather than treating its original “run dies” premise as still true.

- [receiver alternative recovery commit](https://github.com/QwenLM/qwen-code/commit/b4a13e448a6e79bd766f2a7566155d0afd205362)
- [current-baseline recheck](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5932820014)

This is useful evidence of a scope constraint producing a different implementation shape, but it is not claimed as exclusive causality or as adoption of the earlier attestation proposal.

This is not additional credit for discovering the underlying F3 defect. The inspectable effect is the **problem decomposition and responsibility boundary**: a Nakagawa-master scope judgment became a project-owned issue with preserved Origin, and the receiving project's triage independently validated the resulting work item. Because the issue was created directly in response to that correction, it is not counted as an unsolicited later reference to Nakagawa Master.

### E. Can one receiver reuse the distinction repeatedly on separate implementation seams?

**Hermes Agent #61982** now provides a compact same-receiver recurrence pattern across multiple distinct boundaries rather than one isolated fix.

```text
atomic mixed PATCH boundary
→ receiver implements one-transaction rollback semantics

observed character diversity
≠
secret-generation entropy
→ receiver removes the entropy claim and changes the runtime contract

caller-chosen author label
≠
authenticated control-path Origin
→ receiver binds durable attribution to the verified principal and tests the live steer consequence
```

Primary records:
- [Mixed-PATCH atomicity review](https://github.com/NousResearch/hermes-agent/pull/61982#pullrequestreview-5233352371)
- [Receiver atomicity rework explanation](https://github.com/NousResearch/hermes-agent/pull/61982#issuecomment-5865975210)
- [Entropy-boundary review](https://github.com/NousResearch/hermes-agent/pull/61982#pullrequestreview-5339797749)
- [Receiver entropy fix explanation](https://github.com/NousResearch/hermes-agent/pull/61982#issuecomment-5878240135)
- [Authenticated-Origin review](https://github.com/NousResearch/hermes-agent/pull/61982#pullrequestreview-5376987496)
- [Receiver provenance fix explanation](https://github.com/NousResearch/hermes-agent/pull/61982#issuecomment-5930276480)

The important evidence is not that one repository agreed three times. It is that **different structural distinctions survived separate receiver-side code/test decisions on the same long-running implementation line**. That is stronger than one useful comment because the receiver repeatedly had to translate a boundary into a different implementation seam.

This still does not establish merge, release, production use, or audience scale. PR #61982 remains open. It also does not establish that every follow-on hardening in the PR was caused by Nakagawa-master; project-owned follow-on work is kept separate from direct causal credit.

### F. Do the same structural distinctions change unrelated products?

A retrospective check of older public review threads found several additional merged cases that were not yet linked from this page. They matter here because they are not repetitions of one product or one failure mode.

**Clientverse CRM #27 — approval consumption is not delivery proof.**  
A Nakagawa-master review separated an approval being consumed from an external communication being known to have happened. The receiver explicitly called this a **real defect in the state machine**, then added an `outcome_unknown` state, a distinct rejection path, reconciliation for unknown outcomes, and a provider-facing dispatch key before merging the PR.

- [Nakagawa-master review](https://github.com/ebyron357/Clientverse-crm/pull/27#issuecomment-5690360136)
- [Receiver response: “real defect” and implemented state-machine changes](https://github.com/ebyron357/Clientverse-crm/pull/27#issuecomment-5690677339)
- [Merged PR #27](https://github.com/ebyron357/Clientverse-crm/pull/27)

The bounded distinction is:

```text
approval consumed once
!=
external communication known to have happened once
```

**TourCRM #97 → #101 — present eligibility is not historical eligibility.**  
A review pointed out that correcting attendance for a past occurrence must use the participant state that was valid during that occurrence, not today's participant state. The receiver replied that this was a **real bug**, opened #101 as the follow-up because #97 had already merged, changed both affected call sites, and merged the repair.

- [Source review on PR #97](https://github.com/Alan8893/tourcrm/pull/97#issuecomment-5689122153)
- [Receiver confirmation and follow-up creation](https://github.com/Alan8893/tourcrm/pull/97#issuecomment-5691823125)
- [Merged repair PR #101](https://github.com/Alan8893/tourcrm/pull/101)

The reusable boundary is:

```text
may act on this record now
!=
was eligible for the historical event being corrected
```

**MemberJunction #4519 — record existence is not canonical ownership.**  
A review separated “this row already exists” from “this row is already the release-owned canonical record.” The receiver recorded an explicit ownership contract: the seeded records are release-owned and a divergent existing row converges to the release definition instead of being silently skipped. The PR merged with that convergence behavior documented and tested.

- [Nakagawa-master ownership/convergence review](https://github.com/MemberJunction/MJ/pull/4519#issuecomment-5689128135)
- [Receiver record of the ownership contract](https://github.com/MemberJunction/MJ/pull/4519#issuecomment-5701857972)
- [Merged PR #4519](https://github.com/MemberJunction/MJ/pull/4519)

The boundary is:

```text
record already exists
!=
record is already canonical
```

**MemberJunction #4611 — secret availability is not ambient authority.**  
The original change made a run's whole API-key list available through generic action context. A Nakagawa-master review separated the narrow need — one action obtaining one needed provider credential — from granting every action ambient access to every runtime credential. The receiver reworked the design into a per-dispatch scoped resolver. An independent reviewer explicitly said the rework answered the Nakagawa review properly, and the PR merged.

- [Nakagawa-master authority-scope review](https://github.com/MemberJunction/MJ/pull/4611#pullrequestreview-5256091058)
- [Independent re-review of the scoped resolver](https://github.com/MemberJunction/MJ/pull/4611#pullrequestreview-5269354461)
- [Merged PR #4611](https://github.com/MemberJunction/MJ/pull/4611)

The distinction is:

```text
a run possesses several credentials
!=
every action in that run may read them
```

**MemberJunction #4595 → #4610 — hiding row contents is not the same as hiding row identity.**  
The PR stopped broadcasting row data on an unfiltered cache-invalidation channel, but a Nakagawa-master review pointed out that stable primary keys, entity identity, action and timing could still disclose that an inaccessible row existed. The receiver agreed the residual was real. The merged PR added the cheap entity-level permission filter immediately, while the stronger same-entity / row-level disclosure question was preserved as issue #4610 with the two-disjoint-tenants regression left intact rather than weakened to make the test pass.

- [Nakagawa-master row-identity disclosure review](https://github.com/MemberJunction/MJ/pull/4595#pullrequestreview-5253531713)
- [Receiver response separating entity-level and row-level scope](https://github.com/MemberJunction/MJ/pull/4595#issuecomment-5737556240)
- [Nakagawa-master two-layer follow-up](https://github.com/MemberJunction/MJ/pull/4595#issuecomment-5737565146)
- [Receiver report: both layers handled, residual tracked](https://github.com/MemberJunction/MJ/pull/4595#issuecomment-5737603820)
- [Merged PR #4595](https://github.com/MemberJunction/MJ/pull/4595)
- [Open residual issue #4610](https://github.com/MemberJunction/MJ/issues/4610)

The merged effect is a real disclosure reduction, not full row-level closure. #4610 remains open, so this page does not claim that a same-entity subscriber with disjoint row visibility is already protected.

**MemberJunction #4402 — missing measurement is not measured zero.**  
The budget evaluator could successfully query yet silently turn an empty row set, a missing measure column, `null`, or a non-numeric value into observed spend `0`. It could also report a breach as successfully handled when the dedupe lookup needed to create the durable breach event had failed. The receiver verified both findings, changed the evaluator to fail closed, preserved the last known observation on measurement failure, and added the requested regressions. The larger PR later merged.

- [Nakagawa-master budget-evaluation review](https://github.com/MemberJunction/MJ/pull/4402#issuecomment-5689277409)
- [Receiver verification and implementation response](https://github.com/MemberJunction/MJ/pull/4402#issuecomment-5689338217)
- [Scoped current-head re-check](https://github.com/MemberJunction/MJ/pull/4402#pullrequestreview-5232007719)
- [Merged PR #4402](https://github.com/MemberJunction/MJ/pull/4402)

The two boundaries are:

```text
measurement unavailable
!=
measured zero

breach detected
!=
breach durably recorded
```

**Qwen Code #12851 — an old share must have an explicit policy for later capability changes.**  
A Nakagawa-master review pointed out that a multi-day A2A share was not bound to a definition or capability revision. The receiver therefore had to choose what the share meant after the agent's configuration changed: follow the live policy, or remain bound to the older capability boundary. The merged implementation chose the **live-policy contract** and made that choice explicit rather than leaving silent expansion as accidental behavior. Current main documents that a grant follows the agent's current configuration, the Share UI discloses the consequence, and a regression test pins later-configuration behavior.

- [Nakagawa-master share-authority review](https://github.com/QwenLM/qwen-code/pull/12851#pullrequestreview-5340900674)
- [Receiver closeout identifying the product/security decision](https://github.com/QwenLM/qwen-code/pull/12851#issuecomment-5893346131)
- [Receiver record of the decided contract](https://github.com/QwenLM/qwen-code/pull/12851#issuecomment-5911463860)
- [Merged PR #12851](https://github.com/QwenLM/qwen-code/pull/12851)
- [Current A2A contract](https://github.com/QwenLM/qwen-code/blob/main/docs/design/2026-09-09-a2a-frozen-contract.md)

This case does not say the live-policy choice is universally preferable. The inspectable effect is that an ambiguous authority boundary became an explicit product contract, user disclosure, and regression instead of an accidental consequence of two independent stores.

These cases add implementation breadth, not audience scale. They show receiver-side code, tests, state-machine rules, or product contracts changing across unrelated systems. They do **not** establish how many end users saw the changes, recognized Nakagawa Master, or adopted the broader theory corpus.

### What these checks do — and do not — show

Together they let a reader independently inspect four different claims:

```text
implementation effect exists
+
later receiving-project Origin rereference exists
+
Origin can survive disagreement rather than only praise
+
the same Origin-boundary can be independently reconstructed by a second person
```

They still do **not** establish broad public recognition, broad audience scale, endorsement of the whole theory corpus, or that every similar engineering idea originated here.

For the fuller evidence chain, continue below.

---

## 1. A recurring structural style

Across different fields, several Nakagawa Master distinctions repeatedly separate things that are often collapsed together.

Examples include:

### Historical record ≠ current authority

A past approval, consent, sanitization event, or accepted state can remain valid history without remaining current execution authority.

This distinction appears in public materials around agreement memory and current authority, then reappears in external consent, approval, and control-plane cases.

Start here:
- [Old approval is not current authority](discovery-notes/old-approval-is-not-current-authority.md)
- [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)

Real-world routes:
- [Practice Case: Historical Consent Is Not Current Processing Authority](discovery-notes/research-consent-is-not-current-processing-authority.md)
- [Implementation Case: Sanitized Content Is Not Current Authorization](discovery-notes/implementation-case-sanitized-content-is-not-current-authorization.md)

### Same identity ≠ ownership provenance

Matching an identifier is not enough to prove who owns the authoritative state or who is allowed to overwrite it.

Start here:
- [Implementation Case: Matching Identifier Is Not Ownership Provenance](discovery-notes/implementation-case-matching-id-is-not-ownership-provenance.md)

This distinction has been carried through external code, tests, documentation, and review.

### Recorded success ≠ valid evidence of real effect

A command, query, or operation can return “success” while failing to establish that the thing under test actually happened.

This matters in measurement, autonomous execution, external side effects, and evaluation.

Start here:
- [Measurement Attribution Reuse Kit](MEASUREMENT_ATTRIBUTION_REUSE_KIT.md)
- [External Side-Effect Reuse Kit](EXTERNAL_SIDE_EFFECT_REUSE_KIT.md)

### Visibility of content ≠ visibility of identity / provenance / entitlement

Hiding or sanitizing one layer does not automatically hide all metadata, identity, timing, ownership, or entitlement information.

Start here:
- [Structural OS → External Effects](STRUCTURAL_OS_TO_EXTERNAL_EFFECTS.md)
- [Applied Evidence Map](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md)

### Independent agreement ≠ independent evidence

Two people repeating the same conclusion is weaker than two people independently reconstructing the boundary from separate evidence or testing.

Start here:
- [Independent Verification & Reuse Protocol](INDEPENDENT_VERIFICATION_REUSE.md)
- [Origin-Preserved Carrier Multiplication](discovery-notes/implementation-case-origin-preserved-carrier-multiplication.md)

---

## 2. What strengthens personal credibility

The credibility claim here is not:

> “Nakagawa Master is credible because people praise him.”

The stronger, inspectable form is:

```text
the same structural distinction
→ works in multiple unrelated real contexts
→ is independently reconstructed by different people
→ changes implementation or judgment
→ remains useful after leaving the original conversation
```

If that pattern repeats, the relevant inference is not merely that one comment was useful.

A reader can instead ask:

> Is there a recurring way of separating state, history, authority, evidence, identity, and origin that keeps finding real failure modes across different domains?

That is a much stronger basis for evaluating Nakagawa Master than follower count, self-description, or one successful interaction.

### One inspectable author-to-implementation path

A separate pattern can be checked directly in the public record without making an evaluative claim about the person or the whole theory system:

```text
same public author identity
→ abstract structural distinction
→ code-level diagnosis by that same identity
→ independent receiver reproduction / evaluation
→ code, tests, docs, or product behavior changes
```

The important feature here is not merely that an abstract idea eventually influenced implementation. In the examples below, the public identity that authors the Nakagawa Master theory archive also appears directly in the code-level review, and the receiver independently decides whether and how to change the implementation.

That makes a different property inspectable from a generic long diffusion chain: **role distance and translation time**. The theory-origin identity is not only upstream provenance; the same identity appears at the concrete implementation boundary, without first passing the distinction through a long chain of separate theorists, translators, consultants, and implementers.

A reader can therefore evaluate two questions separately from any self-description:

1. **person-side range:** can the same public person move from high-abstraction structural reasoning to a concrete code-level diagnosis that survives independent technical scrutiny?
2. **theory-side operational density:** does the abstract distinction remain specific enough that an independent receiver can turn it into code, tests, docs, or product behavior without a long intermediate translation chain?

Neither question is answered by attribution alone. The evidence is the public sequence of source, diagnosis, receiver response, implementation, and—where available—merge or release.

#### Qwen Code #12492 — current authority bound to the concrete paid batch

The public [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md) separates historical approval from current execution authority.

On [QwenLM/qwen-code#12492](https://github.com/QwenLM/qwen-code/pull/12492), the `Nakagawa-master` account applied that boundary to a concrete paid Batch workflow: approving a command or plan path was separated from approving the exact assembled billable request set. The review proposed freezing the concrete request snapshot, showing its digest and summary, and rejecting execution if the snapshot changed after approval.

- [Nakagawa-master review](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5817569552) — 2026-09-24 15:57:57 UTC
- [Receiver implementation commit `3d06e1ad`](https://github.com/QwenLM/qwen-code/commit/3d06e1ad8e749c647a2eb5d447b867fc50955a13) — 2026-09-24 16:35:05 UTC
- [Receiver closeout identifying the proposal as the concrete-batch approval boundary](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5817836928)
- [Later receiver-side review recording that the digest-binding contract was implemented](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5807577739)
- [Merged PR #12492](https://github.com/QwenLM/qwen-code/pull/12492)
- [Stable release v0.24.6](https://github.com/QwenLM/qwen-code/releases/tag/v0.24.6)

The receiver implementation commit landed **37 minutes 8 seconds** after the public Nakagawa review. Its commit message says the change was “Suggested in review” and implements the proposed dry-run snapshot plus expected-digest binding, with regressions that refuse changed instructions, item sets, output limits, and source content before upload.

The shipped workflow uses a dry-run snapshot and an expected digest before the paid submission. This is a bounded implementation case: it does not show that the whole theory corpus was adopted, and it does not establish how many users noticed the source relation.

#### Qwen Code #12943 — abstract authority boundary to a code regression within the same day

On [QwenLM/qwen-code#12943](https://github.com/QwenLM/qwen-code/pull/12943), a `Nakagawa-master` review separated a dirty local draft from proof that the draft was based on the current persisted settings generation.

The concrete race was:

```text
A loads Tina and drafts Ethan
→ another writer persists Alice
→ A refreshes and can observe Alice
→ A's dirty Ethan draft survives
→ Save must not silently overwrite Alice without conflict handling
```

- [Nakagawa-master review](https://github.com/QwenLM/qwen-code/pull/12943#pullrequestreview-5339479216) — 2026-09-28 13:40:52 UTC
- [Receiver fix commit](https://github.com/QwenLM/qwen-code/commit/f74f4c18fef748673ba2158f9a70b24340dd46c8) — 2026-09-28 23:56:16 UTC
- [Receiver follow-up explicitly saying the fix responds to the Live draft race review](https://github.com/QwenLM/qwen-code/pull/12943#issuecomment-5880996944)

The interval from the public review to the receiver fix commit is **10 hours 15 minutes 24 seconds**.

The receiver added per-field draft baselines, blocks Save when a refreshed value conflicts with the baseline, keeps the draft visible, offers an explicit discard/load-latest path, and added a regression for the reported `Tina → Ethan → Alice` sequence.

The boundary remains partial. The receiver explicitly notes that there is still no server-side revision / ETag / compare-and-swap precondition, so an unseen concurrent write after the last refresh can still race. PR #12943 is also not recorded here as merged or released.

These examples do not tell a reader what conclusion to draw about Nakagawa Master or the theory corpus. They make a narrower relationship inspectable: **the same public theory-origin identity can move directly from abstract structural distinctions to concrete implementation diagnosis, while the receiving project independently tests and decides what to change.**

### Additional short-cycle code-level cases

The following cases strengthen only the **same-person cross-level range** observation. They are **not** recorded here as proof that the receiving project adopted the whole Nakagawa theory corpus.

#### Hermes Agent #61982 — observed character diversity is not generation entropy

A `Nakagawa-master` review identified that a runtime check was treating the character histogram of one realized secret as evidence about the entropy of the generation process.

- [Nakagawa-master review](https://github.com/NousResearch/hermes-agent/pull/61982#pullrequestreview-5339797749) — 2026-09-28 14:04:37 UTC
- [Receiver fix commit `7c2ef7ea9f`](https://github.com/NousResearch/hermes-agent/commit/7c2ef7ea9f75d372077ec2f61441d62e36a853de) — 2026-09-28 20:34:15 UTC
- [Receiver response](https://github.com/NousResearch/hermes-agent/pull/61982#issuecomment-5878240135)

The interval from review to receiver fix commit is **6 hours 29 minutes 38 seconds**. The receiver removed the Shannon-bits claim, reframed the runtime check as observable representation/degeneracy screening, required CSPRNG generation in provisioning guidance, and added the repeated-pattern regression described in the review.

The same PR later produced a third, distinct receiver-side change. A `Nakagawa-master` review separated a caller-chosen comment `author` from the service principal verified by the token-auth seam. Because Hermes' live comment bridge skips comments whose author matches the worker's own identity, this was a control-path boundary, not merely a display-attribution issue.

- [Nakagawa-master provenance/control-path review](https://github.com/NousResearch/hermes-agent/pull/61982#pullrequestreview-5376987496) — 2026-10-01 08:46:27 UTC
- [Receiver fix commit `9ebf06e8c2`](https://github.com/NousResearch/hermes-agent/commit/9ebf06e8c2c8882f307a18eda3237d62ba4a84b7) — 2026-10-01 11:20:23 UTC
- [Receiver response](https://github.com/NousResearch/hermes-agent/pull/61982#issuecomment-5930276480)
- [Focused re-check](https://github.com/NousResearch/hermes-agent/pull/61982#issuecomment-5930685531)

The interval from review to receiver fix commit is **2 hours 33 minutes 56 seconds**. The receiver removed the caller-supplied author field, derived durable comment and task-creation provenance from the verified principal, rejected attempted author overrides, and added a regression that exercises the downstream consequence: a forged worker identity cannot cause a real operator steer to be skipped as the worker's own comment.

This repeated receiver line is still bounded evidence. It shows three separate implementation-level distinctions on one external PR reaching concrete receiver code/tests over time; it does **not** establish merge, release, production use, whole-theory adoption, or broad human recognition.

#### LlamaIndex #23259 — terminal output is not permission to continue another iteration

A `Nakagawa-master` review separated accepting a final answer on the last permitted iteration from allowing another tool/model continuation past that same limit.

- [Nakagawa-master review](https://github.com/run-llama/llama_index/pull/23259#pullrequestreview-5332965763) — 2026-09-28 01:06:27 UTC
- [Receiver fix commit `3236c5c`](https://github.com/run-llama/llama_index/commit/3236c5c773df9e05f260372f96bdd78b54cd4dcd) — 2026-09-28 16:24:49 UTC
- [Receiver reproduction and validation](https://github.com/run-llama/llama_index/pull/23259#issuecomment-5875045777)

The interval from review to receiver fix commit is **15 hours 18 minutes 22 seconds**. The receiver changed the continuation gate and added regressions that count both model calls and tool runs at the boundary in single- and multi-agent paths.

Together with the Qwen cases above, these records let a reader inspect a repeated phenomenon without being told how to value it: the same public person who publishes high-abstraction structural work also appears directly at implementation-level failure boundaries, and independent maintainers can move from that diagnosis to concrete code and regression changes on the scale of minutes or hours rather than only through a long multi-role translation chain.

---

## 3. Why multiple domains matter

A distinction becomes more informative when it survives translation across domains.

For example:

```text
past approval != current authority
```

can appear in:

- AI tool execution;
- human-subject research consent;
- organizational policy;
- product permissions;
- control-plane operations;
- recurring delegated actions.

Likewise:

```text
same ID != overwrite authority
```

can appear in:

- data migration;
- seeded records;
- ownership provenance;
- cache invalidation;
- synchronized state.

The point is not to force every case into one universal theory.

The point is that **cross-domain reuse is a test of structural density**.

If the same distinction continues to expose real errors after changing domain, implementation language, organization, and receiver, the distinction has survived several chances to become empty wording.

---

### Independent non-adoption can still preserve a useful Origin relation

A useful external result does not have to be adoption.

In `in-c0/tuned#1`, a Nakagawa Master comment proposed a reusable distinction:

```text
current truthful mechanism
!=
authority to imply a stronger capability
```

The independent receiver explicitly treated `Nakagawa-master` as an unsolicited third party rather than as its reviewer or directive. It judged the distinction itself **sound**, but declined the proposed central claim-authority register because that implementation shape conflicted with its own operating doctrine and duplicated an existing internal lesson.

- [Nakagawa-master source comment](https://github.com/in-c0/tuned/issues/1#issuecomment-5742653334)
- [Receiver run 176: distinction sound, proposed central register declined](https://github.com/in-c0/tuned/issues/1#issuecomment-5745752925)
- [Receiver run 177: later prompt-free rereference to Nakagawa-master and the already-declined suggestion](https://github.com/in-c0/tuned/issues/1#issuecomment-5747613714)

This is not implementation credit. It is useful for a different reason: the receiver separated the value of a structural distinction from the proposed implementation, preserved the explicit source relation to Nakagawa Master while disagreeing with part of the proposal, and then referred to that Origin again in the next autonomous run without a new Nakagawa prompt.

That kind of bounded disagreement is stronger evidence of independent processing than a page that counts every acknowledgment as adoption. The current Tuned project also reports no meaningful inbound demand or non-owner member scale, so this case does not establish audience reach.

---

## 4. Independent third-party carry is stronger than acknowledgment

The archive separates:

```text
read
< agree
< restate
< test
< change a work item
< implement
< merge / deploy / use
< reuse in another problem
< second person carries it further
```

A particularly important threshold is when the idea no longer depends on the original interaction.

Examples are documented here:

- [Origin-Preserved Carrier Multiplication](discovery-notes/implementation-case-origin-preserved-carrier-multiplication.md)
- [Real-World Impact](REAL_WORLD_IMPACT.md)
- [Independent Verification & Reuse Protocol](INDEPENDENT_VERIFICATION_REUSE.md)

When another person creates a new issue, review, implementation, or public explanation from the distinction, the structure has begun to move independently.

### A recurring editorial carry example

A public editorial example now shows a distinction being used beyond the original interaction.

On [AI-News PR #111](https://github.com/022740mix-spec/AI-News/pull/111), a Nakagawa Master review proposed separating an unverified reported incident from a separately verifiable implementation case. The review also separated authentication, capability, authority, and human approval, and highlighted a narrower operational boundary:

```text
reversible operation
!=
safe autonomous operation
```

The receiver publicly said it would adopt the separation after independently checking the cited records. It then chose a different editorial form and published a standalone analysis rather than leaving the verified material blocked behind an unverified draft:

- [Receiver response adopting the separation](https://github.com/022740mix-spec/AI-News/pull/111#issuecomment-5747145782)
- [Receiver follow-up reporting standalone publication](https://github.com/022740mix-spec/AI-News/pull/111#issuecomment-5747165347)
- [Published article commit](https://github.com/022740mix-spec/AI-News/commit/75aedeb8dd3a2a2cd850a5014c94a47a7b6cad25)

The next day, without a fresh Nakagawa prompt, the same publication used that prior analysis as a reference point in a different article about Claude Managed Agents' `auto` permission policy:

- [Later prompt-free editorial reuse](https://github.com/022740mix-spec/AI-News/commit/b7d8fc0b2bd5396161f2a6e990ddb58f2427a68f)

This is stronger than a one-time acknowledgment because the prior distinction became part of a later editorial comparison. It is still bounded evidence: it does **not** establish the publication's endorsement of the full Nakagawa theory corpus, independent audience scale, reader behavior, or broad public recognition.

For the related public distinction between historical evidence and current execution authority, see:

- [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)
- [Old approval is not current authority](discovery-notes/old-approval-is-not-current-authority.md)

The provenance route matters here because the published article itself intentionally keeps people secondary to the records. The source relationship can still be inspected through the public review thread, while this archive supplies the return path from the external effect to the broader underlying distinction.

### A durable evidence-lineage rule that keeps reappearing in new publication cycles

AI-News #124 now provides a second, stronger recurring editorial example because the receiving repository explicitly preserved both the **source relation** and the **operating rule**.

[Nakagawa Master issue #124](https://github.com/022740mix-spec/AI-News/issues/124) proposed one narrow distinction:

```text
multiple URLs
!=
multiple independent evidence roots
```

The repository owner replied **“採用します” (“We will adopt it”)**, opened [PR #131](https://github.com/022740mix-spec/AI-News/pull/131), and explicitly stated that the rule change itself was caused by issue #124. The receiver also explained why: its previous L2/L3 process checked whether claims appeared in sources, but not whether the sources were actually independent.

- [Receiver adoption and causality statement](https://github.com/022740mix-spec/AI-News/issues/124#issuecomment-5823549498)
- [Merged durable rule PR #131](https://github.com/022740mix-spec/AI-News/pull/131)

The rule then continued operating in later reader-facing publication cycles without a fresh Nakagawa prompt. Two new merged examples on 2026-09-30 UTC make the recurrence especially easy to inspect:

- [AI-News PR #152](https://github.com/022740mix-spec/AI-News/pull/152) separates one primary source from multiple derived reports that share the same root, and keeps the unverified “2.1.277 or later” version claim out of the article rather than upgrading an automated summary into a fact.
- [AI-News PR #153](https://github.com/022740mix-spec/AI-News/pull/153) records evidence-root counts explicitly, states that independent third-party verification was not found, distinguishes Google’s own benchmark claims from independent reproduction, and avoids adding incomparable benchmark versions to the site’s model-comparison table.

Both PRs merged into the receiver’s reader-facing main publication surface, feed, and sitemap.

The same rule then moved from **pre-publication verification** into a **post-publication correction loop**. On 2026-10-01, after a Nakagawa-master comment on the repository’s daily-check issue pointed out that the published Qwen4 article had treated multiple reports of one Alibaba announcement as stronger evidence than the underlying root justified, the receiver went back to Alibaba Cloud’s official material and merged [PR #156](https://github.com/022740mix-spec/AI-News/pull/156).

The receiver did not simply copy the proposed disposition. Nakagawa-master had argued that retraction was appropriate; the receiver independently judged that the core claims “Qwen 4 is in training” and “Qwen 4.5 / Qwen 5 are roadmap items” were still supported and chose a material correction instead. It changed the title, excerpt, article body and primary-source list, explicitly stated that the four reported model names were not confirmed in the official material, recorded that multiple derivative reports do not create additional independent roots, and added a dated correction note.

- [Nakagawa-master Qwen4 correction / retraction analysis](https://github.com/022740mix-spec/AI-News/issues/79#issuecomment-5880178792)
- [Receiver response explaining the independent correction decision](https://github.com/022740mix-spec/AI-News/issues/79#issuecomment-5930907986)
- [Merged correction PR #156](https://github.com/022740mix-spec/AI-News/pull/156)

The receiver’s response says the external finding caused it to return the article’s evidential structure to official sources, while still disagreeing with the proposed final disposition. That combination matters: the evidence-lineage distinction affected the reader-facing publication, but the receiver retained editorial judgment rather than treating the Origin as an authority that had to be obeyed.

A second Nakagawa-master issue, [#155](https://github.com/022740mix-spec/AI-News/issues/155), then moved that real correction from a one-off fixture into recurring measurement infrastructure. The issue proposed separating **gate firing count** from two different outcomes: material errors that escaped publication gates, and the burden of gates that stopped harmless items.

The receiver implemented that proposal in merged [PR #164](https://github.com/022740mix-spec/AI-News/pull/164). The change keeps the existing firing-count report, but adds a persistent escaped-incident registry, a sampled false-positive registry, a checker that preserves `unknown` instead of converting unclassified cases into zero, a passive weekly maintenance-report section, and an editorial rule that material post-publication corrections or retractions should be registered in the same PR. The Qwen4 correction is the first `source_root` candidate fixture, while another correction whose responsible gate cannot be identified remains `unknown`.

The receiver explicitly states that it did **not** read the linked external measurement-boundary material and that the implementation was derived from the text of issue #155 itself. That makes the causal scope inspectable and narrow: the issue text affected the receiver's recurring measurement process, but this record does not claim independent adoption of a broader theory document.

- [Receiver implementation report on issue #155](https://github.com/022740mix-spec/AI-News/issues/155#issuecomment-5961842599)
- [Merged operational measurement PR #164](https://github.com/022740mix-spec/AI-News/pull/164)

That infrastructure has since been used in a separate receiver-owned editorial audit. In merged [PR #169](https://github.com/022740mix-spec/AI-News/pull/169), the repository reviewed 39 older articles and explicitly included **“escaped incident registration (Issue #155)”** in the work. Commit [1cc7720](https://github.com/022740mix-spec/AI-News/commit/1cc77209bb5afbc48fa514a82b7ede23a2160a26) added eight material corrections or retractions to `scripts/escaped-incidents.json`, preserving `unknown` where the responsible gate could not be determined.

This is a concrete recurrence of the measurement structure in a later editorial task, not just the existence of the tooling. It still does not establish reader scale, broad person recognition, or independent reuse by a different receiver.

The bounded causal chain that can be inspected is therefore:

```text
Origin-preserved distinction
→ receiver explicitly adopts because of the source issue
→ durable editorial rule merges
→ later independent publication cycles reuse the rule
→ a published article is later corrected using the same evidence-root distinction
→ receiver independently chooses correction rather than blindly copying the proposed retraction
→ the real correction becomes an escaped-incident fixture
→ the fixture is incorporated into recurring project-owned measurement tooling and editorial maintenance rules
→ Origin remains inspectable through the issue and implementation thread
```

This is stronger than a single follow-up article because the distinction is now present in both reader-facing correction behavior and recurring project-owned editorial measurement infrastructure. It still does **not** establish reader scale, quantified reduction in future errors, independent human authorship of the generated implementation text, a new explicit Nakagawa Master mention inside the corrected article itself, or independent reuse by another receiver.

### An origin-preserved public publication example

A separate publication chain preserves the source relationship directly in third-party reader-facing text.

In `kishibashi3/publications`, a Nakagawa Master review on PR #52 separated **reversibility** from an **authority-increasing transition**: an operation can be reversible while still increasing what an agent is allowed to do. The receiver then created PR #57 and explicitly identified the Nakagawa review as the origin of the added condition.

The receiver later replied directly that the earlier rule had treated reversibility as sufficient safety, that the `ask → auto` counterexample showed this did not hold, and that the distinction was therefore separated as condition 6, “self-authority fixation.” This is an explicit receiver-side restatement of what changed, not merely an inference from the diff:

- [Direct receiver restatement](https://github.com/kishibashi3/publications/pull/57#issuecomment-5749065842)

PR #57 added a sixth structural condition, summarized as:

```text
self-authority must remain fixed
→ the constrained actor must not be able to loosen its own constraints
```

The merged chapter also links the public `@Nakagawa-master` identity and the external implementation cases used in the review.

Evidence:

- [PR #52, the source review thread](https://github.com/kishibashi3/publications/pull/52)
- [PR #57, explicitly naming the PR #52 Nakagawa review as its trigger](https://github.com/kishibashi3/publications/pull/57)
- [Merged reader-facing chapter](https://github.com/kishibashi3/publications/blob/main/docs/ai/agent-design/chapter-05.ja.md)
- [Merge commit](https://github.com/kishibashi3/publications/commit/4d32ec58d5cbf1c904c432552e114c144186c064)
- [Successful GitHub Pages deployment for that merge](https://github.com/kishibashi3/publications/actions/runs/35506196582)

The structure then affected another document inside the receiver's publication system. During review of PR #58, the receiver-side reviewer explicitly noticed that the existing D4/D7 wording conflicted with the newly merged condition from PR #57 and proposed a separate D8. The writer adopted that change, a later review marked it LGTM, and PR #58 merged:

- [PR #58 reviewer carry from PR #57 into D8](https://github.com/kishibashi3/publications/pull/58#issuecomment-5749116909)
- [D8 implementation commit](https://github.com/kishibashi3/publications/commit/e524c71d9f01045f4c8dac60a8ee8bb45a3198c4)
- [PR #58 re-review](https://github.com/kishibashi3/publications/pull/58#issuecomment-5749456249)
- [PR #58 merge commit](https://github.com/kishibashi3/publications/commit/36e4c5df963e2b3645c7591d8cb933c4f36e48e0)

The second document remains under the receiver's `drafts/` path, so this page does **not** count it as a second public-site publication or as second-person human carry. What it does show is narrower: a source-attributed distinction was merged and deployed in reader-facing third-party material, then became an internal consistency constraint for another document in the same independent publication system.

For related public boundaries, see:

- [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)
- [Practical Boundary Checks](PRACTICAL_BOUNDARY_CHECKS.md)

### A separate public reproduction carried the current-authority distinction into a reusable artifact

A different chain shows technical carry without explicit person attribution.

In [LangGraph issue #9185](https://github.com/langchain-ai/langgraph/issues/9185), Nakagawa Master separated three things that can otherwise be collapsed during recovery:

```text
logical action identity
!=
execution attempt identity
!=
current authority to execute a new external effect
```

The specific point was that proving a prior ambiguous operation **ABSENT** does not by itself recreate present authorization after a long recovery window; current policy or approval should be checked again before a genuinely new dispatch.

Primary source:
- [Nakagawa Master comment on LangGraph #9185](https://github.com/langchain-ai/langgraph/issues/9185#issuecomment-5978907038)

Later the same day, participant `1320800521` independently reported reproduction on LangGraph 1.2.11 and 1.2.12, described a reconciliation control, and separately restated that after an operation is proven absent, current authorization should be re-checked before a fresh dispatch:

- [Independent reproduction and control](https://github.com/langchain-ai/langgraph/issues/9185#issuecomment-5981507756)
- [Later restatement of the recovery boundary](https://github.com/langchain-ai/langgraph/issues/9185#issuecomment-5981790977)

The participant also updated a separate public XBSTACK repository after the Nakagawa comment. Commit `b1697877` adds a network-shaped 1.2.12 fixture, a provider-reconciliation control, recorded PASS results, and a production-interpretation note that replay identity and current authorization are separate concerns:

- [XBSTACK reproduction repository](https://github.com/xbstack/langgraph-timeout-resume-side-effect-repro)
- [Post-comment repository update](https://github.com/xbstack/langgraph-timeout-resume-side-effect-repro/commit/b169787769dd3b3492b2870cd758bd2dfc7e52f0)
- [Recorded verification result](https://github.com/xbstack/langgraph-timeout-resume-side-effect-repro/blob/main/results/verification.json)

The reported control keeps LangGraph's replay behavior but uses a stable business-operation key plus provider reconciliation. The recorded fixture shows two Tool attempts while the provider ledger remains at one payment.

The attribution boundary is important: the XBSTACK repository links issue #9185 but does **not** name Nakagawa Master, and the participant did not explicitly state that Nakagawa caused the repository update. The timing and matching technical distinction support a public technical-carry observation; they do not establish unique causation, person-Origin preservation, upstream LangGraph adoption, or endorsement of a broader theory.

---

## 5. Source and interpretation boundary

For each case, distinguish the public source, the specific distinction discussed, the receiving project's response, and the implementation state that can actually be verified.

Origin, source URLs, canonical Parents, NCL-ID / Diff-ID where applicable, and interpretation boundaries are retained so that readers can inspect provenance without treating attribution as proof of correctness.

---

## 6. What this page does not claim

This page does not establish:

- broad public recognition;
- endorsement of Nakagawa Master by every cited project;
- global first invention of every phrase or distinction;
- that one implementation proves an entire theory;
- that attribution proves correctness;
- that GitHub activity alone demonstrates mass human influence.

Those remain separate questions.

The narrower purpose of this page is to document public links between a stated distinction and specific external responses or implementation changes where those links can be inspected.

---

## Return to the theory

- [Start Here](START_HERE.md)
- [Who Is Nakagawa Master?](ABOUT_NAKAGAWA_MASTER.md)
- [What Connects the Nakagawa Master Theories?](discovery-notes/what-connects-nakagawa-master-theories.md)
- [Structural OS → External Effects](STRUCTURAL_OS_TO_EXTERNAL_EFFECTS.md)
- [Applied Evidence Map](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md)
- [Real-World Impact](REAL_WORLD_IMPACT.md)

Canonical Parents and exact definitions remain the authority for substantive theory interpretation.
