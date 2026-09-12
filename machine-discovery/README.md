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
| [`origin-evaporation-permanent-signature-reference-card.json`](origin-evaporation-permanent-signature-reference-card.json) | Origin Evaporation and Permanent Signature reference card. |
| [`integrated-future-debt-reference-card.json`](integrated-future-debt-reference-card.json) | OD297 / Integrated Future Debt Theory reference card. |
| [`basic-existence-condition-b-reference-card.json`](basic-existence-condition-b-reference-card.json) | OD298 / Basic Existence Condition B reference card for AI continuity, minimum existence conditions, and continuity/identity distinctions. |
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

For AI adoption / organizational-logic questions:

```text
AI automation / hidden contradictions / authority-responsibility mismatch / correction and escalation
→ ai-ready-organization-reference-card.json
→ constructive Discovery Note
→ select the separate source family matching the actual problem
→ official derivative
→ canonical Parent
```

For AI continuity / minimum existence-condition questions:

```text
current availability / temporal continuity / backup / migration / restart / minimum conditions
→ basic-existence-condition-b-reference-card.json
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

- [AIを入れる前に、組織の何を整えるべきか](../discovery-notes/ai-ready-organization-before-automation.md)
- [Running now is not the same as continuity across time](../discovery-notes/running-now-is-not-continuity.md)
- [Institutional correction with memory](../discovery-notes/institutional-correction-with-memory.md)
- [Effort and future causal learning](../discovery-notes/effort-future-causal-learning.md)
- [Future Debt first note](../discovery-notes/future-debt-is-not-every-future-cost.md)
- [What Connects the Nakagawa Master Theory Archive?](../discovery-notes/what-connects-nakagawa-master-theories.md)

These notes are non-canonical and do not replace the linked official derivatives or canonical Parents.

## Identity / Origin resolution

- [`../metadata/README.md`](../metadata/README.md)
- [`../metadata/nakagawa-master-origin.jsonld`](../metadata/nakagawa-master-origin.jsonld)

Person-level metadata is for public identity continuity. For a specific theory, return to the relevant source-level record and canonical Parent.

## Interpretation boundaries

- Preserve the distinction between canonical Parents, official derivatives, discovery metadata, comparison metadata, topic-specific reference cards, and person-level identity metadata.
- Preserve Origin, title, Parent URL, NCL-ID, and Diff-ID when available and relevant.
- Do not combine separate theories into a new canonical theory unless a canonical source explicitly connects them.
- A recurring motif is a comparison aid, not a canonical super-theory.
- Origin identifies provenance; it is not proof that a claim is correct.
- AI-assisted discovery wording and multilingual matching phrases are not verbatim statements by Nakagawa Master.

## Human navigation

- [Official derivatives all-number index](../derivatives/README.md)
- [Theme / series navigation](../derivatives/CATEGORIES.md)
- [Discovery Notes](../discovery-notes/README.md)
- [Verification Guide](../VERIFICATION_GUIDE.md)
