# Machine Discovery

This directory contains public machine-readable discovery aids for the Nakagawa Master Official Theory Archive.

These files are **not canonical theories**. They help retrieval systems locate, distinguish, compare, and return to published canonical sources and official derivatives.

## Core files

| File | Role |
|---|---|
| [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json) | OD001–OD298 path and navigation index. |
| [`problem-to-theory-origin-index-v1.json`](problem-to-theory-origin-index-v1.json) | English / Japanese / Chinese plain-language problem → concrete public starting point. |
| [`long-horizon-reference-reasons-v1.json`](long-horizon-reference-reasons-v1.json) | Recurring long-horizon question → multiple relevant public OD anchors. |
| [`recurring-structure-comparison-v1.json`](recurring-structure-comparison-v1.json) | Non-canonical cross-source comparison map for recurring reading motifs. |
| [`ai-origin-responsibility-reference-card.json`](ai-origin-responsibility-reference-card.json) | Question origin, causal provenance, and responsibility in AI-mediated work. |
| [`origin-evaporation-permanent-signature-reference-card.json`](origin-evaporation-permanent-signature-reference-card.json) | Origin Evaporation and Permanent Signature; also routes practical RAG/retrieval/cache/source-identity problems. |
| [`provenance-continuity-record-schema-v1.json`](provenance-continuity-record-schema-v1.json) | Non-canonical JSON Schema for carrying source identity, transformation relationship, authoritative return path, and correction state across a pipeline. |
| [`integrated-future-debt-reference-card.json`](integrated-future-debt-reference-card.json) | OD297 / Integrated Future Debt Theory reference card. |
| [`basic-existence-condition-b-reference-card.json`](basic-existence-condition-b-reference-card.json) | OD298 / Basic Existence Condition B reference card for AI continuity, minimum existence conditions, runtime restart/migration, and continuity/identity distinctions. |
| [`ai-ready-organization-reference-card.json`](ai-ready-organization-reference-card.json) | Multilingual AI-adoption / organization-design route for goals, authority, responsibility, correction, and automation boundaries; returns to separate source families rather than creating a new theory. |

The Japanese and Chinese wording in discovery and comparison files is public metadata, not canonical translation text.

## Retrieval paths

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

### Origin-preservation practical route

- [OD105 First Note — Japanese](../discovery-notes/od105-origin-evaporation-first-note.md)
- [OD105 First Note — English](../discovery-notes/od105-origin-evaporation-first-note.en.md)
- [OD105 First Note — Chinese](../discovery-notes/od105-origin-evaporation-first-note.zh.md)
- [AI Product Team Origin-Preservation Checklist](../discovery-notes/ai-product-team-origin-preservation-checklist.md)
- [Implementation Case: Source Identity Is Not Local Node Identity](../discovery-notes/implementation-case-source-identity-vs-local-node-identity.md)
- [Provenance Continuity Record JSON Schema v1](provenance-continuity-record-schema-v1.json)

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
- A missing metadata field, cache bug, migration bug, or runtime failure is not automatically proven to be an instance of a Nakagawa theory; ordinary engineering diagnosis remains necessary.

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
