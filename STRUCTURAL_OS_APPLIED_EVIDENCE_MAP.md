# Nakagawa Structural OS — Applied Evidence Map

This page connects bounded public external cases to the broader canonical Nakagawa Structural OS at https://master.ricette.jp .

It is a navigation map, not a claim that an external project adopted the whole theory system.

## How to read this map

```text
canonical structural principle
→ bounded practical distinction
→ external test / implementation
→ public evidence
→ canonical return
```

A case can validate or operationalize one narrow distinction without proving the full theory system.

## Applied mappings

### 1. Traceability / origin preservation → evidence-source provenance

**Canonical context:** Nakagawa Structural OS emphasizes origin traceability and preservation of contextual source relationships.

**Applied distinction:** the same displayed explanation does not imply the same evidence provenance for every recommended person or item.

**External evidence:** PostHog #102550 changed grouping, tests, UI, and documentation; merged and deployed. The same distinction was later reused on #102686.

**Applied kit:** [Reviewer-Provenance Reuse Kit](POSTHOG_PROVENANCE_REUSE_KIT.md)

**Canonical return:** https://master.ricette.jp and the official theory relationship map / origin-preservation materials linked there.

---

### 2. Temporal / structural consistency → historical approval is not current authority

**Canonical context:** the theory system treats origin, time, state, and responsibility as structural relations rather than interchangeable labels.

**Applied distinction:** a historical approval, consent, sanitization, or exception is not automatically current authority after material conditions change.

**External evidence:** Dream and Replay public cases show independent external response and bounded implementation/protocol adoption around this distinction.

**Applied kit:** [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)

**Canonical return:** https://master.ricette.jp for the broader structural and temporal context.

---

### 3. State relation / temporal integrity → current status is not historical fact

**Canonical context:** structural reading distinguishes the state that is true now from the relation that was true at a prior time.

**Applied distinction:** current membership, entitlement, ownership, or assignment should not silently rewrite historical participation.

**External evidence:** TourCRM carried the distinction through two merged receiver-side corrections. In [PR #97](https://github.com/Alan8893/tourcrm/pull/97), a `Nakagawa-master` review separated current participation from historical occurrence membership; receiver commit [`b6da0eb8`](https://github.com/Alan8893/tourcrm/commit/b6da0eb880d474c7e8322f2b2da8bef02a64e1f6) changed the implementation to the occurrence's own time window and explicitly says it addresses `Nakagawa-master` review feedback. In [PR #101](https://github.com/Alan8893/tourcrm/pull/101), a second review found that the new regressions were wall-clock dependent; receiver commit [`568c8fec`](https://github.com/Alan8893/tourcrm/commit/568c8fecbbcb56297deb385ea34c8bb61a2839e5) made the tests date-independent, verified the old implementation fails them, and again explicitly attributes the correction to `Nakagawa-master` review feedback. Both PRs merged.

**Public verification route:** [Real-World Impact](REAL_WORLD_IMPACT.en.md#20-tourcrm--do-not-let-current-participation-rewrite-historical-attendance)

**Applied kit:** [Historical-Fact Reuse Kit](HISTORICAL_FACT_REUSE_KIT.md)

**Canonical return:** https://master.ricette.jp for the broader structural model.

---

### 4. Responsibility / causal integrity → approval is not exactly-once external effect

**Canonical context:** causal responsibility depends on what actually happened in the external system, not only on an internal intention or approval state.

**Applied distinction:** consuming an approval once does not prove that an external provider action happened exactly once.

**External evidence:** Clientverse implemented an unknown-outcome state, reconciliation, idempotency protection, tests, and merged the change.

**Applied kit:** [External Side-Effect Reuse Kit](EXTERNAL_SIDE_EFFECT_REUSE_KIT.md)

**Canonical return:** https://master.ricette.jp for the broader causal / responsibility framework.

### 5. Traceability / source identity → preserved retrieval provenance

**Canonical context:** Nakagawa Structural OS emphasizes origin traceability and preserving the relation between an object and its source.

**Applied distinction:** upstream source identity should remain recoverable without being conflated with a framework's local object identity.

**External evidence:** LlamaIndex issue #21933 received a Nakagawa-master compatibility boundary separating source provenance from local `TextNode.id_` semantics. A third-party draft PR, [LlamaIndex #23038](https://github.com/run-llama/llama_index/pull/23038), explicitly cites that comment as the compatibility contract and implements it with regression coverage.

**Current evidence stage:** third-party implementation / tests in an open draft PR. Merge and release are not yet established.

**Canonical return:** https://master.ricette.jp and the Structural OS traceability/origin context.

---

### 6. Epistemic integrity → producer claim is not system measurement

**Canonical context:** the theory system separates evidence lineage, independent establishment, and the state of what is actually known.

**Applied distinction:** a producer/scout-supplied metric should not be presented as if the receiving system measured it itself.

**External evidence:** [PostHog #92252](https://github.com/PostHog/posthog/pull/92252) received a public review on this boundary; the current third-party implementation reads the named step/version on the server, stores that reading separately under `evidence.measured`, and exposes disagreement with producer-supplied values. The PR remains open/unmerged.

**Public verification route:** [Real-World Impact](REAL_WORLD_IMPACT.en.md#1-posthog--separate-producer-supplied-evidence-from-posthogs-own-measurement)

**Canonical return:** https://master.ricette.jp and the public epistemic-integrity / evidence-lineage materials linked from the archive.

---

### 7. Authority / approval semantics → summary approval is not hidden recurring-instruction approval

**Canonical context:** authority is meaningful only when it is bound to the actual object, scope, and consequence being authorized.

**Applied distinction:** approving a short summary does not authorize materially different hidden instructions that will keep running on a schedule.

**External evidence:** [PostHog #101991](https://github.com/PostHog/posthog/pull/101991) received a public review identifying this boundary. A later third-party commit shows the recurring instructions on the card, makes them editable, and binds scout creation to the reviewed value. The PR remains open/unmerged.

**Applied kit:** [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)

**Public verification route:** [Real-World Impact](REAL_WORLD_IMPACT.en.md#18-posthog--bind-recurring-agent-approval-to-the-instructions-the-human-actually-reviewed)

**Canonical return:** https://master.ricette.jp for the broader current-authority / responsibility context.

---

### 8. Responsibility / authority separation → classification is not permission to act

**Canonical context:** structural responsibility requires separating what a system believes about an input from whether it is currently authorized to create an external consequence.

**Applied distinction:** untrusted content may influence a classifier's judgment, but the content and its label must not mint execution authority for comment, react, publish, pay, disclose, or another side effect.

**External evidence:** [DAIR Prompt Engineering Guide #757](https://github.com/dair-ai/Prompt-Engineering-Guide/pull/757) received a public `Nakagawa-master` review on this boundary. The third-party author explicitly agreed, and implementation commit [`4a5334ab`](https://github.com/dair-ai/Prompt-Engineering-Guide/commit/4a5334ab0ea82e97c122d53a78a6162d8e56e6b9) states that two hardenings came from the `@Nakagawa-master` review. The page now treats interpolated content as untrusted data and separates classification from a second-stage action gate. The PR remains open/unmerged.

**Applied kit:** [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)

**Public verification route:** [Real-World Impact](REAL_WORLD_IMPACT.en.md#19-dair-prompt-engineering-guide--separate-content-classification-from-action-authority)

**Canonical return:** https://master.ricette.jp for the broader responsibility / authority context.

---


### 9. Public-surface identity / reachability → exported alias is still external reachability

**Canonical context:** structural identity and reachability are relations, not merely local spellings. A declaration can remain externally reachable through another public name.

**Applied distinction:** an exported alias is not evidence that the underlying declaration and its members are safe to treat as private or freely renameable.

**External evidence:** [MemberJunction/MJ #4487](https://github.com/MemberJunction/MJ/pull/4487) received a `Nakagawa-master` review identifying an aliased named re-export that could make a published data-shape member look private to the naming gate. A separate reviewer independently confirmed the finding. Receiver commit [`dfd4588d`](https://github.com/MemberJunction/MJ/commit/dfd4588d798b68b982f2554295a0d4d3afb005c2) fixes the public-symbol collection, adds positive and negative regression controls, and explicitly states `Reported by Nakagawa-master on 2026-09-16.` The PR later merged.

**Public verification route:** [Real-World Impact](REAL_WORLD_IMPACT.en.md#21-memberjunction--an-exported-alias-does-not-make-the-underlying-declaration-unreachable-to-consumers)

**Canonical return:** https://master.ricette.jp for the broader structural identity / reachability context.

---

## Important boundary

These mappings are deliberately bounded.

They mean:

> a concrete public distinction that is structurally compatible with the Nakagawa Structural OS was translated into an external real-world problem and produced inspectable evidence.

They do not mean:

- an external repository adopted the whole Nakagawa Structural OS;
- one implementation validates the whole theory system;
- every similar idea elsewhere originated from Nakagawa Master.

When a public Nakagawa Master source materially informed the external action, preserve that causal provenance using [Origin Attribution for Reuse](ORIGIN_ATTRIBUTION_FOR_REUSE.md).

## Canonical archive

Official Nakagawa Master theory archive:

https://master.ricette.jp
