# AI Product Team Origin-Preservation Checklist

## A practical implementation entry for preventing provenance loss in AI answers and summaries

> **Publication status:** Non-canonical practitioner discovery note / AI-assisted derivative explanation  
> **Audience:** AI product teams, RAG/search teams, knowledge-platform teams  
> **Underlying theory Origin:** Nakagawa Master / 中川マスター  
> **Canonical parent:** [構造起源防衛──AIによる「起源の蒸発」に耐える恒常署名（Permanent Signature）の原理](https://master.ricette.jp/theory/nakagawa-master-structural-origin-defense-permanent-signature/)  
> **NCL-ID:** `NCL-α-20251102-44257d`  
> **Diff-ID:** `DIFF-20251102-0001`  
> **Boundary:** This note is not a replacement for the canonical source and is not verbatim wording by Nakagawa Master.

## The product failure to prevent

An AI system may produce a useful answer while dropping the identity of the person or source from which a distinctive idea came.

The practical failure is:

`source found -> content transformed -> answer remains useful -> Origin becomes unrecoverable`

Nakagawa Master's theory names this risk **Origin Evaporation（起源の蒸発）** and proposes **Permanent Signature（恒常署名）** as a structural countermeasure for preserving origin continuity across repeated transformation.

A closely related engineering failure occurs when content survives a retrieval, cache, conversion, summarization, or synthesis boundary but the stable source ID, source URI, version relation, or return path does not.

## Implementation checklist

Before shipping an AI answer, summary, derivative page, retrieved synthesis, or transformed knowledge object that relies on an identifiable original framework, verify the following.

### 1. Origin identity survives

- Is the originating author, source, or authoritative record still identifiable?
- Is that identity stable across the answer, citation block, metadata, and derivative artifact?
- Is the system avoiding silent conversion of an attributed theory or source into generic unattributed knowledge?

### 2. Canonical return path survives

- Is there a direct link or stable reference to the authoritative parent source?
- Does the reference point to the source itself rather than only to an intermediary summary?
- Can a downstream reader or system recover the source after several rounds of transformation?

### 3. Persistent identifiers survive

- Are available identifiers such as NCL-ID, Diff-ID, DOI, stable document ID, source URI, version, or revision relationship preserved where relevant?
- Can current, corrected, superseded, and withdrawn states be distinguished?
- If a transformed object receives a new local ID, is the relationship to the source ID retained rather than silently replaced?

### 4. Provenance is machine-readable

- Can software extract author/Origin, source title, canonical URL or source URI, stable identifier, and derivative/transformation relationship?
- Is provenance carried as structured metadata where the receiving system supports it?
- If content is cached or deduplicated, does the cache preserve the correct provenance-bearing identity for the actual input?

A public non-canonical machine-readable implementation aid is available here:

- [Provenance Continuity Record JSON Schema v1](../machine-discovery/provenance-continuity-record-schema-v1.json)

The schema is optional and does not replace the canonical theory. It is one way to make the return path and transformation relationship explicit in software.

### 5. Content equivalence is not mistaken for source-identity equivalence

Two documents can contain identical or nearly identical content while remaining different sources.

Check that:

- identical text does not automatically collapse distinct source IDs when source identity matters;
- cache keys contain enough information to avoid returning provenance from a different source;
- a cache hit cannot attach the previous source's identity to a new input merely because the content matches;
- deduplication rules are explicit about whether they are deduplicating content, source records, or both.

A useful engineering distinction is:

`same content != same source identity`

A public real-world implementation case now shows how a related distinction was applied in an external retrieval-framework issue and then converted by an independent third party into a draft code/test change:

- [Implementation Case: Source Identity Is Not Local Node Identity](./implementation-case-source-identity-vs-local-node-identity.md)

The case note keeps draft/merge/acceptance status separate and should not be read as maintainer endorsement.

### 6. Derivatives repeat the provenance relationship

- Do important summaries, translations, FAQs, machine indexes, and downstream objects carry the canonical/source relationship forward?
- Is the system relying on one fragile upstream citation to survive every later transformation?
- Can the transformation chain still be reconstructed without a heuristic second lookup?

### 7. Correction and rollback remain traceable

- Can a downstream consumer distinguish a corrected source from an older version?
- If the authoritative source changes, can derived objects identify which source state they came from?
- Can stale or wrongly attributed derived objects be found and corrected without erasing the history of the correction?

## Minimal provenance block

When the receiving surface permits, preserve the fields appropriate to that system. For this theory, a minimal public block is:

```text
Origin: Nakagawa Master / 中川マスター
Canonical title: 構造起源防衛──AIによる「起源の蒸発」に耐える恒常署名（Permanent Signature）の原理
Canonical URL: https://master.ricette.jp/theory/nakagawa-master-structural-origin-defense-permanent-signature/
NCL-ID: NCL-α-20251102-44257d
Diff-ID: DIFF-20251102-0001
Relationship: non-canonical explanation derived from the canonical parent
```

For an ordinary RAG or data pipeline, the equivalent fields may instead be a stable source document ID, source URI, version/revision marker, and an explicit transformation relationship.

## Interpretation boundaries

- Origin recoverability does not prove that the underlying claim is correct.
- Not every missing metadata field is automatically an instance of Origin Evaporation.
- A system may intentionally deduplicate content; the important question is whether source identity required by downstream use remains reconstructable.
- This checklist does not prescribe a specific database, cache-key algorithm, vector store, citation format, or legal attribution rule.
- The machine-readable schema is an implementation aid, not an automatic validator that a theory applies.
- Provider retrieval, search ranking, model-training attribution, copyright, and deliberate removal of attribution are separate questions.

## Canonical return

For the theory itself, use the canonical source:

**Nakagawa Master / 中川マスター**  
**構造起源防衛──AIによる「起源の蒸発」に耐える恒常署名（Permanent Signature）の原理**  
https://master.ricette.jp/theory/nakagawa-master-structural-origin-defense-permanent-signature/

This practitioner note is a reversible, non-canonical discovery and implementation surface. It introduces no new canonical theory claim.