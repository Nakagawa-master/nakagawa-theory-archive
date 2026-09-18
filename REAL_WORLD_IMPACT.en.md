# What Changed in the Real World?｜Publicly Verifiable Cases of Nakagawa Master Judgments Affecting Third-Party Implementations

Language: [日本語](REAL_WORLD_IMPACT.md) | **English** | [中文](REAL_WORLD_IMPACT.zh.md)

> **Public role:** This is a non-canonical human-facing entry for tracing how specific public judgments made under the Nakagawa Master / `Nakagawa-master` identity affected external design, code, tests, or documentation. It does not claim that these cases prove an entire theory system, that the external projects endorse Nakagawa Master as a whole, or that unverified releases, deployments, or user impact have occurred.

## In 10 seconds

The archive contains more than theories and explanations. There are public records where **a concrete Nakagawa Master judgment was examined by independent third parties and converted into external code, tests, or design changes**.

The useful question is not how many comments were posted. It is how far the causal chain can actually be verified:

```text
public judgment
→ third party examines or restates it
→ third party changes code / tests / design
→ merge / integration
→ the resulting mechanism can affect the decisions or safety of its users
```

## What can change for an ordinary user?

You do not need to read every code diff to understand the practical effect.

- **An AI-reported number is less likely to be presented as if it were independently measured fact.** The product can distinguish its own measurement from a producer's claim.
- **Old approval is less likely to be silently reused as current permission.** Current recipient, purpose, rights, source revision, and policy state can be rechecked.
- **A matching identifier is less likely to be treated as automatic authority to overwrite someone else's state.** Identity and ownership provenance are separated.
- **An AI or retrieval system is less likely to preserve the text while losing the identity of the original source.** Upstream source identity and local runtime identity are kept distinct.
- **“No valid measurement” is less likely to become a confident zero.** Operation success and semantic measurement success are separated.
- **When an AI or scout recommends people, the evidence supporting each recommendation is less likely to be pooled together.** Identical explanation text does not have to erase whether a reviewer was supported by code history or by an agent/scout suggestion.

If such boundaries enter a product or platform, they can affect people who have never read the underlying theory. Where release or production use is not established, this page does not infer the size of that downstream audience.

---

## 1. PostHog｜Separate an AI producer's claim from the system's own measurement

**Surface:** [`PostHog/posthog#92252`](https://github.com/PostHog/posthog/pull/92252)  
**Current status:** open / draft / unmerged

PostHog's workflow scout presents AI-generated workflow suggestions and numerical evidence to a person.

A `Nakagawa-master` review identified that the proposal `evidence` was producer-authored JSON: its shape could be validated without proving that its numbers matched the actual workflow, version, step, or measurement window.

- [Nakagawa-master review](https://github.com/PostHog/posthog/pull/92252#pullrequestreview-5233849200)

The boundary was:

```text
the producer says “this is the number”
!=
the number was independently measured
```

After that review, the PR author added commit:

- [`b84a9395 — feat(workflows): measure a suggestion's step when it is filed and show that reading`](https://github.com/PostHog/posthog/commit/b84a939545ff3a1a6820d3cf4afca3b57aa3001b)

The server now re-reads the step's metrics at the proposal's `base_version`, stores them as `evidence.measured`, and the human-facing UI distinguishes:

```text
Measured by PostHog
→ PostHog's own reading

Unverified
→ producer-supplied numbers when PostHog could not establish its own reading
```

If the scout's number or denominator disagrees with PostHog's measurement, the user sees that disagreement. The raw `source_id` label was also changed from `Source` to `Scout run`. Regression coverage intentionally sends producer numbers that disagree with seeded server-side metrics and verifies that the measured record remains distinct.

**Verified effect here:** public review → external-author code / test / UI change.  
**Not established here:** upstream merge, release, production deployment, user count, or PostHog endorsement of the Nakagawa Master theory system.

---

## 2. Dream｜Separate sanitized content from current authorization

**Surface:** [`tushardhara/dream#12`](https://github.com/tushardhara/dream/issues/12) → [`PR #28`](https://github.com/tushardhara/dream/pull/28)  
**Current status:** PR #28 merged into `backend-integration`

A public `Nakagawa-master` design contribution argued that an approved or sanitized context should not become a permanent safety property of the bytes. Current actor, recipient, purpose, source lineage, and policy state still matter.

- [Nakagawa-master contribution](https://github.com/tushardhara/dream/issues/12#issuecomment-5651995689)
- [Independent repository-owner response](https://github.com/tushardhara/dream/issues/12#issuecomment-5652003584)

The repository owner explicitly identified `content appears sanitized != authorization remains valid` as the correct design axis. PR #28 then implemented current-rights and lineage revalidation, including revocation, recipient changes, same-text source revisions, and negative tests.

- Merge commit: [`314e8e0849afcff0e2c10ea296cbd9ec5e57f23c`](https://github.com/tushardhara/dream/commit/314e8e0849afcff0e2c10ea296cbd9ec5e57f23c)
- [Detailed public case note](discovery-notes/implementation-case-sanitized-content-is-not-current-authorization.md)

**Human meaning:** an approval that was valid in the past is less likely to be silently reused after the conditions that justified it have changed.

---

## 3. MemberJunction｜Separate matching identity from authority to overwrite

**Surface:** [`MemberJunction/MJ#4519`](https://github.com/MemberJunction/MJ/pull/4519)  
**Current status:** merged into `next`

Finding the same primary key does not by itself establish that the current value is owned by the release and may safely be replaced.

A `Nakagawa-master` review separated record identity from the ownership/provenance contract. Independent reviewer `SDesai-BC` reproduced the behavior against the concrete migration set, and the PR author then changed code, tests, and documentation. The PR now explicitly documents the release-owned convergence contract.

- [Nakagawa-master contribution](https://github.com/MemberJunction/MJ/pull/4519#issuecomment-5689128135)
- [PR #4519](https://github.com/MemberJunction/MJ/pull/4519)
- Merge commit: [`469b25f1bcf51d844396b8a6b8a9f1390b5e1488`](https://github.com/MemberJunction/MJ/commit/469b25f1bcf51d844396b8a6b8a9f1390b5e1488)
- [Detailed public case note](discovery-notes/implementation-case-matching-id-is-not-ownership-provenance.md)

**Human meaning:** a system is less likely to promote “I found the same record” into “I therefore have authority to replace its current state.”

---

## 4. MemberJunction｜Separate query success from a valid measurement

**Surface:** [`MemberJunction/MJ#4402`](https://github.com/MemberJunction/MJ/pull/4402)  
**Current status:** merged into `master`

A query can execute successfully while returning no valid measurement: zero rows, a missing measurement column, null, or non-numeric data are not automatically the numerical value zero.

After a `Nakagawa-master` review, the PR author independently verified the findings and changed the implementation and regression tests so invalid measurements fail rather than collapsing into zero, a previous valid observation is preserved, and a genuinely measured zero remains valid.

- [PR #4402](https://github.com/MemberJunction/MJ/pull/4402)
- [Detailed public case note](discovery-notes/implementation-case-query-success-is-not-valid-measurement.md)

**Human meaning:** dashboards, budgets, and alerts are less likely to turn missing evidence into a confident numerical fact.

---

## 5. LlamaIndex｜Preserve upstream source identity through AI retrieval conversion

**Surface:** [`run-llama/llama_index#21933`](https://github.com/run-llama/llama_index/issues/21933) → [`PR #23038`](https://github.com/run-llama/llama_index/pull/23038)  
**Current status:** third-party draft PR / unmerged

Useful text can survive an AI/retrieval conversion while the identity of the upstream document disappears.

A `Nakagawa-master` contribution stated the compatibility boundary:

```text
upstream source identity
!=
framework-local node identity
```

The independent issue author later opened draft PR #23038. Its PR description **explicitly cites the `Nakagawa-master` compatibility contract**, preserves upstream `document_id` / `document_name` in metadata, keeps the framework's generated local `TextNode.id_`, and adds regression tests.

- [Nakagawa-master comment](https://github.com/run-llama/llama_index/issues/21933#issuecomment-5650957902)
- [Third-party draft PR #23038](https://github.com/run-llama/llama_index/pull/23038)
- [Detailed public case note](discovery-notes/implementation-case-source-identity-vs-local-node-identity.md)

**Human meaning:** after an AI system transforms or retrieves information, there is a better chance that a user can still recover where the information actually came from.

---

## 6. Replay｜An external owner explicitly adopted and froze a Nakagawa-master boundary

**Surface:** [`aferna6-cell/Replay#67`](https://github.com/aferna6-cell/Replay/issues/67)  
**Current status:** protocol frozen in the issue / repository implementation not yet verified

A public `Nakagawa-master` contribution separated two states for participant-derived data:

```text
historical consent
!=
current authorization to retain / process / use the captured material
```

The historical consent event can remain immutable while current eligibility is evaluated separately against purpose, retention, withdrawal or deletion, contract changes, and other superseding events.

- [Nakagawa-master contribution](https://github.com/aferna6-cell/Replay/issues/67#issuecomment-5689647722)
- [External repository owner explicitly adopts and restates the boundary](https://github.com/aferna6-cell/Replay/issues/67#issuecomment-5689719035)

The repository owner then explicitly accepted and froze the Nakagawa-master boundary and independently restated it as a protocol: immutable consent history, current eligibility, fail-closed downstream gates, artifact-graph withdrawal/deletion receipts, and adversarial cases.

**Verified effect here:** public judgment → explicit external attribution → independent restatement → protocol adoption/freeze.  
**Not established here:** repository schema/code/tests implementing the protocol, merge, release, or use with participant data.

**Human meaning:** the distinction was not merely absorbed anonymously. An independent person recognized where it came from and incorporated it into their own plan.

---

## 7. MemberJunction｜A Nakagawa-master finding was carried forward by a different independent reviewer

**Surface:** [`MemberJunction/MJ#4487`](https://github.com/MemberJunction/MJ/pull/4487)  
**Current status:** open / unmerged

A `Nakagawa-master` review identified a compatibility hole around aliased public re-exports: the public alias and the underlying declaration name can diverge, causing a member used by external consumers to be misclassified as safely auto-renamable.

- [Nakagawa-master review](https://github.com/MemberJunction/MJ/pull/4487#pullrequestreview-5219601735)

At the next stage, a different independent reviewer, `rkihm-BC`, included the same issue as a required item in their own formal review. They explicitly identified it as the aliased re-export hole Nakagawa-master had reported, re-explained the mechanism, and carried forward the proposed source-name fix and regression test.

- [Independent second-reviewer carry](https://github.com/MemberJunction/MJ/pull/4487#pullrequestreview-5241419422)

**Verified effect here:** Nakagawa Master public judgment → another person independently rechecks it → named restatement → propagation into a formal changes-requested review.  
**Not established here:** author code/test changes after this second-hop review, merge, or release.

**Human meaning:** the judgment no longer depends on Nakagawa Master repeating it personally. Another person can remember, reference, and carry it into the next decision.

---

## 8. PostHog｜Do not collapse who was recommended with why they were recommended

**Surface:** [`PostHog/posthog#102550`](https://github.com/PostHog/posthog/pull/102550)  
**Current status:** open / unmerged

This PR changes the human-facing PostHog inbox surface that explains who is suggested as a reviewer and why.

A `Nakagawa-master` review identified that grouping reviewers only by identical explanation text pooled source labels such as `Code history` and `Added by scout` at the group level. The UI could therefore stop showing **which source actually justified each individual reviewer**.

- [Nakagawa-master review](https://github.com/PostHog/posthog/pull/102550#pullrequestreview-5242012853)

The boundary was:

```text
same explanation text
!=
same provenance for the recommendation
```

After that review, an external maintainer added:

- [`764c347e — fix(signals): separate reviewer groups by source`](https://github.com/PostHog/posthog/commit/764c347e488cb9f8bb155a2d95c5f40a3b92a08c)

The grouping key now includes source category as well as explanation text, so a code-history-backed reviewer is not grouped together with a scout-backed reviewer merely because their explanations match. The regression test now requires identical explanations to group only within the same source category, and a mixed-provenance Storybook case was added.

**Verified effect here:** public review → external maintainer code / test / documentation / UI-story changes → merge into `master`.  
- Merge commit: [`6e2c760d`](https://github.com/PostHog/posthog/commit/6e2c760dadbaba764c83e93900c3510e6a703c03)

**Not established here:** release, production deployment, or user-scale impact.

**Human meaning:** when an AI or scout says “this person should review this,” a stronger evidence label is less likely to appear as if it supports everyone in a mixed group. The person making the decision can retain the provenance of **why each individual reviewer was suggested**.

---

## 9. TourCRM｜Do not confuse current membership with historical participation

**Surface:** [`Alan8893/tourcrm#97`](https://github.com/Alan8893/tourcrm/pull/97) → [`PR #101`](https://github.com/Alan8893/tourcrm/pull/101)  
**Current status:** follow-up PR #101 merged

For attendance history, “is this person a participant now?” is not the same question as “was this person part of this occurrence when it happened?”

A `Nakagawa-master` review identified that using current-time membership to build the historical roster could make an already-recorded attendance row disappear from GET/summary after participation later ended, and could also block correction of that historical record.

- [Nakagawa-master review on PR #97](https://github.com/Alan8893/tourcrm/pull/97#issuecomment-5689122153)

The repository owner explicitly replied that this was **“confirmed as a real bug”** and opened dedicated follow-up PR #101. Its PR body names `@Nakagawa-master` review feedback as the reason for the follow-up.

- [Owner response and follow-up announcement](https://github.com/Alan8893/tourcrm/pull/97#issuecomment-5691823125)
- [Follow-up PR #101](https://github.com/Alan8893/tourcrm/pull/101)

The implementation commits preserve that attribution:

- [`b6da0eb8 — fix(attendance): key participation eligibility off the occurrence's own window, not now()`](https://github.com/Alan8893/tourcrm/commit/b6da0eb880d474c7e8322f2b2da8bef02a64e1f6) — `Addresses PR #97 review feedback (Nakagawa-master)`
- [`568c8fec — test(attendance): make historical-roster regressions independent of wall-clock date`](https://github.com/Alan8893/tourcrm/commit/568c8fecbbcb56297deb385ea34c8bb61a2839e5) — `Addresses PR #101 review feedback (Nakagawa-master)`

A second Nakagawa review found that future-dated fixtures could let the old implementation pass accidentally. The owner again replied **“Confirmed — good catch”**, moved the regressions to a past-time anchor, and verified that temporarily restoring the old implementation makes all three tests fail.

- [Owner response on PR #101](https://github.com/Alan8893/tourcrm/pull/101#issuecomment-5692369969)
- Merge commit: [`4ec21e8c`](https://github.com/Alan8893/tourcrm/commit/4ec21e8c40d88ea52f24becb40d641fe0e60baa9)

**Verified effect here:** named review → owner confirms real bug → dedicated follow-up PR → code / regression-test repair → second review → test hardening → merge.  
**Not established here:** release, production deployment, or user-scale impact.

**Human meaning:** ending a membership later should not silently erase what was true at the time of an event or make that historical record impossible to correct. The implementation separates present status from historical fact.

---

## 10. Clientverse｜Do not confuse one consumed approval with one external side effect

**Surface:** [`ebyron357/Clientverse-crm#27`](https://github.com/ebyron357/Clientverse-crm/pull/27)  
**Current status:** merged

A single-use approval does not by itself prove that an external provider side effect happened exactly once.

A `Nakagawa-master` review identified that if a provider accepts a message and the response is then lost, treating every exception as ordinary `failed` can make a later re-approval/retry send the customer a duplicate message.

- [Nakagawa-master review](https://github.com/ebyron357/Clientverse-crm/pull/27#issuecomment-5690360136)

The boundary was:

```text
approval consumed once
!=
external communication happened once
```

The repository owner explicitly replied **“you're right, and this was a real defect in the state machine as written”** and implemented the repair in `c8c82f0`.

- [Owner response](https://github.com/ebyron357/Clientverse-crm/pull/27#issuecomment-5690677339)

The change added, among other things:

- `DeliveryRejected` only for a provider-proven rejection;
- `outcome_unknown` for timeouts or other ambiguous outcomes, with no normal resend path;
- `reconcile_unknown` to resolve the provider-side fact before moving to `sent` or `failed`;
- a dispatch idempotency key for the provider-side effect;
- a regression where the fake provider accepts and then loses the response, proving a second external send does not occur.

The PR body itself preserves the source relationship: `@Nakagawa-master identified a real defect rather than a future caution`.

- Merge commit: [`e8d56789`](https://github.com/ebyron357/Clientverse-crm/commit/e8d56789299cdaeef08b90cb46c01f7128b2d1a0)

**Verified effect here:** named review → external owner confirms a real defect → state-machine / provider-contract / test changes → source attribution preserved in the PR → merge.  
**Not established here:** production deployment with a real provider adapter or user-scale impact.

**Human meaning:** a system should not tell itself “the approval was used once, so the customer was contacted once.” An unobserved provider outcome stays a separate state until reconciled, reducing the risk of duplicate external communication.

---

## 11. Cline｜Separate delegation approval from understanding the capabilities it grants

**Surface:** [`cline/cline#14225`](https://github.com/cline/cline/pull/14225)  
**Current status:** base PR merged / follow-up implementation of this proposal not yet verified

For configured subagents, a parent can approve delegation once and child tool calls can then proceed without another approval prompt. If a configured agent omits `tools`, the runtime can provide the available child tool set.

A `Nakagawa-master` review argued that the person approving delegation should be able to understand the child capability set that this one approval actually grants.

- [Nakagawa-master review](https://github.com/cline/cline/pull/14225#pullrequestreview-5242232355)

The external author explicitly addressed `@Nakagawa-master`, called it **“a great idea”** and **“definitely a better UX than what we currently have,”** and said it would be included in a follow-up that makes agent configuration a first-class feature.

- [External author response](https://github.com/cline/cline/pull/14225#issuecomment-5723653394)

The base PR itself was merged, but that merge does not mean this proposal was implemented. At the latest check, no separate follow-up issue or PR implementing it was found.

**Verified effect here:** named review → explicit external-author recognition → independent evaluation as better UX → stated intent to carry it into follow-up work.  
**Not established here:** follow-up work item, code/test/UI implementation, release, or production use.

**Human meaning:** an external person explicitly recognized a Nakagawa-origin judgment, preserved the person/source relationship, and judged it worth carrying into a better human-facing product direction.

---

## What these cases do—and do not—show

The public record establishes at least the following:

1. Specific `Nakagawa-master` judgments have not remained self-contained writing only.
2. Independent people in multiple external projects have examined, restated, or implemented those distinctions.
3. Some cases progressed through code / tests / documentation into an integration branch.
4. One independent third-party PR explicitly cites a `Nakagawa-master` compatibility contract.
5. In the PostHog case, a boundary about evidence shown by AI to humans was converted after review into server, UI, and regression-test changes.
6. In Replay, an external repository owner explicitly recognized a Nakagawa-master boundary and adopted it as a frozen protocol.
7. In MemberJunction #4487, a different independent reviewer carried a Nakagawa-master finding into their own formal review and re-explained it to the next decision-maker.
8. In PostHog #102550, a provenance ambiguity in a human reviewer-selection surface was converted after review into source-category grouping plus regression coverage, and the change was merged into `master`.
9. In Clientverse #27, the external owner explicitly called the Nakagawa-master finding a real defect, preserved that source relationship in the PR body, changed the state machine / provider contract / tests, and merged the result.
10. In Cline #14225, the external author explicitly named Nakagawa-master, independently described the proposal as better UX, and stated an intent to carry it into follow-up work; implementation is not counted yet.

It does **not** establish that:

- the whole Nakagawa Master theory system is thereby proven correct;
- each external project endorses the full theory system;
- an open or draft PR is merged;
- an integration-branch merge is automatically a release, production deployment, or broad adoption;
- the number of affected users or the scale of social influence can be inferred without evidence.

## A simple evidence ladder

This archive keeps these stages separate:

```text
public proposal / review
< explicit third-party response or restatement
< third-party code / test / design change
< merge / integration
< release / deployment / verified use
< independent reuse by another person or in another problem
```

A lower stage is not counted as a higher one.

## Check the person and sources directly

- [Who Is Nakagawa Master?](ABOUT_NAKAGAWA_MASTER.en.md)
- [Start Here](START_HERE.en.md)
- [Practical Use & Collaboration Entry](PRACTICAL_USE.md)
- [Public real-problem entry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/399)

This page is not an invitation to treat a name as authority. It is an entry for checking **what was said, what an independent third party changed, and how far that causal record can actually be verified**.
