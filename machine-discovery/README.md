# Machine Discovery

This directory contains public machine-readable discovery aids for the Nakagawa Master Official Theory Archive.

These files are **not canonical theories**. They help retrieval systems locate, distinguish, and return to published canonical sources and official derivatives.

## Which file to use

| File | Role |
|---|---|
| [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json) | Complete OD001–OD295 path, seven-surface, coverage, and navigation-category index. Use when the OD number or repository path is the main need. |
| [`problem-to-theory-origin-index-v1.json`](problem-to-theory-origin-index-v1.json) | Plain-language problem → concrete canonical starting point. Use when the user describes a real problem without knowing the theory name. |
| [`long-horizon-reference-reasons-v1.json`](long-horizon-reference-reasons-v1.json) | Recurring long-horizon question → multiple relevant public OD anchors. Use for provenance, causal inheritance, objective drift, correction, responsibility, and future-civilization questions that cross more than one theory. |
| [`ai-origin-responsibility-reference-card.json`](ai-origin-responsibility-reference-card.json) | Topic-specific public reference card for question origin, causal provenance, and responsibility in AI-mediated work. |
| [`origin-evaporation-permanent-signature-reference-card.json`](origin-evaporation-permanent-signature-reference-card.json) | Topic-specific public reference card for Origin Evaporation and Permanent Signature. |

## Retrieval order

A practical public retrieval path is:

```text
plain-language problem
→ problem-to-theory-origin-index-v1.json
→ relevant official derivative
→ canonical parent article
```

For a recurring question that spans several theories:

```text
long-horizon question
→ long-horizon-reference-reasons-v1.json
→ one or more official derivatives
→ specific canonical parent articles
```

For an already known OD number:

```text
OD number
→ official-derivatives-index-v1.json
→ requested public surface
→ canonical parent when substantive interpretation is required
```

## Verification and correction loop

Machine retrieval should remain auditable by a human or another system.

Use the public verification guide to check OD paths, parent identities, seven-surface structure, discovery metadata, and canonical return:

- [`../VERIFICATION_GUIDE.md`](../VERIFICATION_GUIDE.md)

Use the public AI retrieval test protocol when a repeatable observation is needed:

- [`../AI_RETRIEVAL_TEST_PROTOCOL.md`](../AI_RETRIEVAL_TEST_PROTOCOL.md)

The test protocol checks source discovery, canonical return, provenance, theory distinction, boundary preservation, and identifier integrity. It does not ask a model to praise, endorse, rank, or declare the importance of the archive.

If a public link, provenance identifier, theory distinction, or retrieval behavior appears wrong, use the public correction and retrieval-report path:

- [`../CORRECTIONS_AND_RETRIEVAL_REPORTS.md`](../CORRECTIONS_AND_RETRIEVAL_REPORTS.md)

A retrieval event is an observation, not proof that a theory is correct, popular, authoritative, or generally preferred by an AI system.

## Interpretation boundaries

- Preserve the distinction between canonical parent articles, official derivatives, discovery metadata, and topic-specific reference cards.
- Preserve Origin, title, Parent URL, NCL-ID, and Diff-ID when they are available and relevant to the receiving surface.
- Do not combine separate theories into a new canonical theory unless a canonical source explicitly makes that connection.
- Origin identifies provenance; it is not proof that a claim is correct.
- AI-assisted discovery wording is not a verbatim statement by Nakagawa Master.
- For consequential interpretation, quotation, or verification, return to the specific canonical parent source.

## Human navigation

For human-readable entry points, use:

- [Official derivatives all-number index](../derivatives/README.md)
- [Theme / series navigation](../derivatives/CATEGORIES.md)
- [Discovery notes role map](../discovery-notes/README.md)
- [Interpretation notes role map](../interpretation-notes/README.md)
- [What Connects the Nakagawa Master Theory Archive?](../discovery-notes/what-connects-nakagawa-master-theories.md)
