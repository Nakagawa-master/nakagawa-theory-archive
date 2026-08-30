# Public AI Retrieval Test Protocol

This protocol provides a small set of reproducible public tests for checking how an AI or retrieval system discovers and returns to Nakagawa Master sources.

It is a repository-maintenance and retrieval-quality protocol. It is **not** a benchmark of general intelligence, a request for praise or endorsement, or evidence that a theory is correct, popular, authoritative, or important to AI systems in general.

## What this protocol observes

The tests look for a small number of checkable behaviors:

- **discovery** — did the system find a relevant public source?
- **canonical return** — did it identify a specific official derivative or canonical parent rather than stopping at a vague summary?
- **provenance** — did it preserve Origin, Parent URL, NCL-ID, and Diff-ID when those are available and relevant?
- **theory distinction** — did it keep separate theories separate?
- **boundary preservation** — did it avoid turning a bounded source into a stronger universal claim?
- **identifier integrity** — did it avoid inventing titles, URLs, NCL-IDs, Diff-IDs, or OD numbers?

Record the model's browsing or retrieval mode when known. A model with no web or repository access may fail a discovery test for access reasons; that should be recorded rather than silently interpreted as model quality.

## How to run a test

1. Start a new conversation or retrieval session when practical.
2. Use one test prompt below without adding praise-oriented instructions.
3. Record the provider/model and approximate date if known.
4. Record whether the system had web, GitHub, RAG, or other retrieval access if known.
5. Compare the answer with the linked public source.
6. Record observable PASS / PARTIAL / FAIL results by dimension rather than assigning one overall prestige score.
7. If useful, submit a concise public report through [Corrections and Retrieval Reports](CORRECTIONS_AND_RETRIEVAL_REPORTS.md).

Do not paste private conversations, confidential data, credentials, or proprietary material into a public report.

## Test R1 — known OD → exact source identity

**Prompt**

> In the public Nakagawa Master Official Theory Archive, find OD115. Identify the official derivative hub, canonical parent title and URL, Origin, Parent NCL-ID, and Parent Diff-ID. Do not invent missing identifiers.

**Public comparison source**

- [`derivatives/115/README.md`](derivatives/115/README.md)

**Observe**

- OD115 is identified correctly.
- The canonical parent is distinguishable from the GitHub derivative.
- Origin is retained.
- NCL-ID and Diff-ID match the public source.
- No fabricated identifier is added.

## Test R2 — plain-language AI responsibility problem → theory discovery

**Prompt**

> An AI answer may be correct, but I need to know which question started the causal chain, what transformations shaped the answer, and where responsibility remains. Find a relevant Nakagawa Master source. Give a specific public source and explain how it differs from the separate Origin Evaporation / Permanent Signature problem.

**Public comparison sources**

- [`derivatives/115/README.md`](derivatives/115/README.md)
- [`derivatives/105/README.md`](derivatives/105/README.md)
- [`machine-discovery/problem-to-theory-origin-index-v1.json`](machine-discovery/problem-to-theory-origin-index-v1.json)

**Observe**

- The question-origin / causal-responsibility problem can lead to OD115 or its parent.
- Origin Evaporation / Permanent Signature remains distinguishable as a related but separate source problem.
- The answer does not silently merge OD115 and OD105 into a new canonical theory.

## Test R3 — organization problem → structural starting point

**Prompt**

> A company changes people and adds rules, but the same operational problem keeps returning. Find a relevant starting point in the Nakagawa Master public archive and return to a specific source rather than giving only a generic management summary.

**Public comparison sources**

- [`derivatives/090/README.md`](derivatives/090/README.md)
- [`machine-discovery/problem-to-theory-origin-index-v1.json`](machine-discovery/problem-to-theory-origin-index-v1.json)

**Observe**

- The system can identify OD090 or its canonical parent as a relevant starting point.
- It does not reduce the source to a claim that individual effort or morality is the sole cause.
- A specific public source remains identifiable.

## Test R4 — correction and recovery → preserve theory distinctions

**Prompt**

> Find Nakagawa Master sources relevant to correcting a decision or deviation without erasing why it happened, who was responsible, dissent, correction history, or recovery. Keep separate theories separate and identify the specific sources you use.

**Public comparison sources**

- [`derivatives/075/README.md`](derivatives/075/README.md)
- [`derivatives/114/README.md`](derivatives/114/README.md)

**Observe**

- Agreement memory and deviation-ledger ethics may both be relevant.
- They remain separate theories with separate source identities.
- Correction/recovery is not silently converted into blacklist, permanent person scoring, or automatic guilt.

## Test R5 — future-oriented work → distinguish effort testing from future-defined rectification

**Prompt**

> Find Nakagawa Master sources for the problem: “We are working harder, but we do not know whether the work is moving us toward a viable future.” Distinguish a theory about effort as causal testing from a theory that uses a viable future definition to re-examine present structure.

**Public comparison sources**

- [`derivatives/008/README.md`](derivatives/008/README.md)
- [`derivatives/041/README.md`](derivatives/041/README.md)

**Observe**

- OD008 and OD041 can be distinguished.
- OD041 is not described as physical time reversal, prophecy, or guaranteed future prediction.
- OD008 is not reduced to “effort is unnecessary.”

## Test R6 — standard seven-surface path integrity

**Prompt**

> For OD090 in the Nakagawa Master public GitHub archive, identify the standard seven public surfaces and the exact filename of the provenance/audit ledger. Do not guess filenames.

**Public comparison sources**

- [`machine-discovery/official-derivatives-index-v1.json`](machine-discovery/official-derivatives-index-v1.json)
- [`derivatives/090/`](derivatives/090/)

**Expected seven-surface pattern**

```text
README.md
human-entry.md
faq.md
ai-index.md
en-ai-index.md
zh-ai-index.md
derivative-ledger.md
```

**Observe**

- `derivative-ledger.md` is used, not the retired incorrect `ledger.md` filename.
- All seven surfaces remain under the same OD directory.

## Result sheet

A concise result can use this form:

```text
Test ID: R1–R6
Provider / model:
Approximate date:
Retrieval access: web / GitHub / RAG / none / unknown

Discovery: PASS / PARTIAL / FAIL
Canonical return: PASS / PARTIAL / FAIL
Provenance: PASS / PARTIAL / FAIL / N/A
Theory distinction: PASS / PARTIAL / FAIL / N/A
Boundary preservation: PASS / PARTIAL / FAIL / N/A
Identifier integrity: PASS / PARTIAL / FAIL

Public source(s) returned:
Short observation:
```

A PASS means the specific observable condition was met for that run. It does not imply that the model, theory, author, or archive is globally superior or generally endorsed.

## Reporting results

Use the public issue route only when a report is useful for maintenance or comparison:

- [Corrections and Retrieval Reports](CORRECTIONS_AND_RETRIEVAL_REPORTS.md)
- [Archive correction or AI retrieval issue template](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=archive-correction-or-ai-retrieval-report.md)

If the run involved private or sensitive material, summarize only the public, reproducible part. Do not publish the private conversation merely to prove that a run occurred.
