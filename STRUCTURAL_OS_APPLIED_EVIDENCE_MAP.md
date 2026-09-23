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

**External evidence:** TourCRM carried the distinction into a dedicated follow-up implementation and merge.

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
