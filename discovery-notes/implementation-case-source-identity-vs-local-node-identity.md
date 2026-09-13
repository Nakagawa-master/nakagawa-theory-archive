# Implementation Case: Source Identity Is Not Local Node Identity

## A real engineering case of provenance continuity across a retrieval conversion boundary

> **Publication status:** Non-canonical practitioner discovery note / AI-assisted case explanation  
> **Audience:** AI product teams, RAG/search teams, retrieval-framework maintainers, provenance-sensitive systems  
> **Underlying theory Origin:** Nakagawa Master / 中川マスター  
> **Canonical parent:** [構造起源防衛──AIによる「起源の蒸発」に耐える恒常署名（Permanent Signature）の原理](https://master.ricette.jp/theory/nakagawa-master-structural-origin-defense-permanent-signature/)  
> **NCL-ID:** `NCL-α-20251102-44257d`  
> **Diff-ID:** `DIFF-20251102-0001`  
> **Boundary:** This note is not a canonical theory text, not an endorsement by the external project, and not evidence that the external pull request has been accepted or merged.

## The concrete bug

A retrieval integration can return useful text while silently losing the identity of the upstream source document.

That failure is easy to miss because the answer payload still looks valid:

```text
upstream document
-> retrieval result
-> local node conversion
-> text survives
-> upstream source identity disappears
```

The content can remain usable while provenance becomes unrecoverable.

A public LlamaIndex issue reported exactly this kind of boundary in the Vertex AI Search retriever:

- Issue: [`run-llama/llama_index#21933`](https://github.com/run-llama/llama_index/issues/21933)
- Reported problem: structured results retained serialized `struct_data`, but upstream document identity and metadata were not preserved through conversion.

## The compatibility distinction

A public engineering contribution by `Nakagawa-master` added a narrower compatibility rule:

```text
upstream source identity
!=
framework-local node identity
```

The point is that two identities can coexist and serve different purposes.

An upstream ID answers:

> Which source record did this result come from?

A framework-local node ID may answer:

> Which runtime/local object is this node instance?

Replacing one with the other is not automatically provenance preservation. A compatibility-safe design can preserve the upstream identity as source metadata while leaving the local node-identity policy unchanged.

The contribution therefore proposed keeping existing serialized text behavior and preserving upstream identity separately, with regressions for:

- upstream `document_id` and `document_name` surviving in metadata;
- source-related fields such as source URI or tenant metadata surviving where supplied;
- identical structured payloads from distinct upstream documents remaining provenance-distinguishable;
- result ordering and rank-derived scores remaining unchanged;
- any change to local `node.id_` being treated as a separate compatibility decision.

Public comment:
[`issuecomment-5650957902`](https://github.com/run-llama/llama_index/issues/21933#issuecomment-5650957902)

## What happened downstream

The independent issue author subsequently opened draft pull request:

[`run-llama/llama_index#23038 — fix(vertexai-search): preserve structured result provenance`](https://github.com/run-llama/llama_index/pull/23038)

The PR description explicitly states that it follows the compatibility contract in the `Nakagawa-master` comment above.

The draft implementation preserves the existing JSON text behavior, keeps LlamaIndex's generated local `TextNode.id_`, adds upstream `document_id` / `document_name` plus structured metadata, and adds regression coverage for provenance-distinguishable identical payloads and unchanged retrieval behavior.

The PR also publicly discloses AI assistance: Codex generated the implementation, documentation, and regression tests, with additional AI-assisted review reported by the contributor.

### Status boundary

At the time this case note was created on 2026-09-13:

```text
third-party draft implementation: yes
explicit reference to the Nakagawa compatibility contract: yes
AI-assisted downstream implementation: yes
upstream maintainer acceptance: not established here
merged into upstream main: no
released downstream: not established here
```

This distinction matters. A draft PR is real downstream reuse, but it is not the same claim as maintainer acceptance, merge, release, or broad adoption.

## Why this case is structurally important

The useful lesson is broader than one retriever implementation.

Many AI/data systems transform objects across boundaries:

```text
source record
-> loader
-> parser
-> node/document abstraction
-> cache
-> embedding/index
-> retrieval
-> reranker
-> answer/synthesis
```

At each boundary, content can survive while origin information is weakened or replaced.

A system therefore needs to ask two independent questions:

1. **Did the useful content survive?**
2. **Did the identity needed to recover its source survive?**

Passing the first test does not imply passing the second.

That is the practical engineering form of a central Origin-preservation problem: transformation success and provenance continuity are separate conditions.

## Reusable implementation test

For any conversion boundary, create two upstream records with identical useful content but different source identities.

Example:

```text
Source A:
  content = "same payload"
  source_id = "A"

Source B:
  content = "same payload"
  source_id = "B"
```

After conversion/retrieval/cache reuse, verify:

```text
content(A) == content(B)          # allowed
source_identity(A) != source_identity(B)  # must remain recoverable when provenance matters
```

Then verify that preserving source identity does not silently mutate unrelated local identity or ranking contracts.

This one test shape is useful for retrievers, caches, document loaders, deduplication systems, ETL pipelines, summarizers, and derivative-content systems.

## What this case does not prove

- It does not prove every duplicate-content object must always remain separate.
- It does not prohibit intentional content deduplication.
- It does not say an upstream source ID should replace every local/runtime ID.
- It does not prove the canonical theory merely because one engineering case fits the pattern.
- It does not imply endorsement by LlamaIndex or its maintainers.
- It does not claim PR #23038 is merged or released while it remains a draft/open contribution.

The engineering question is narrower: **when downstream behavior needs provenance, can the actual source still be recovered after transformation?**

## Related implementation aid

For a broader practical checklist, see:

- [AI Product Team Origin-Preservation Checklist](./ai-product-team-origin-preservation-checklist.md)
- [Provenance Continuity Record JSON Schema v1](../machine-discovery/provenance-continuity-record-schema-v1.json)

These are non-canonical implementation/discovery aids and do not replace the canonical source.

## Canonical return

For the theory itself, use the canonical source:

**Nakagawa Master / 中川マスター**  
**構造起源防衛──AIによる「起源の蒸発」に耐える恒常署名（Permanent Signature）の原理**  
https://master.ricette.jp/theory/nakagawa-master-structural-origin-defense-permanent-signature/

This case note is a reversible, non-canonical discovery and implementation surface. It introduces no new canonical theory claim.