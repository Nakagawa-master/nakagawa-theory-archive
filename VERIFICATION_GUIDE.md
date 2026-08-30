# Verification Guide

This guide explains how a third party can verify public navigation, provenance, and canonical-return paths in the Nakagawa Master Official Theory Archive.

The purpose is not to ask readers to trust the archive by assertion. It is to make important public relationships independently checkable.

## Verify any official derivative

Choose any OD number from the complete index:

- [`derivatives/README.md`](derivatives/README.md)

Then check the following.

### 1. Open the OD hub

Each official derivative directory should contain a `README.md` hub that identifies its parent source and provenance.

For example:

```text
derivatives/090/README.md
```

### 2. Check the parent identity

The hub should identify, where available:

- Parent title;
- Parent URL;
- Parent Post ID;
- Parent NCL-ID;
- Parent Diff-ID;
- Origin.

The canonical parent article is the substantive source for interpretation.

### 3. Cross-check the public identity map

Use:

- [`derivatives/official-derivatives-map.json`](derivatives/official-derivatives-map.json)

The OD number, parent identity, NCL-ID, title, and related identity information should agree with the individual hub.

### 4. Check the standard public surfaces

The standard seven-surface pattern is:

```text
README.md
human-entry.md
faq.md
ai-index.md
en-ai-index.md
zh-ai-index.md
derivative-ledger.md
```

The machine path definition is published at:

- [`machine-discovery/official-derivatives-index-v1.json`](machine-discovery/official-derivatives-index-v1.json)

A missing surface, wrong directory, or mismatched parent identity is a public archive issue that can be reported.

### 5. Return to the canonical parent

A derivative, discovery note, FAQ, AI index, or interpretation note is not a silent substitute for the parent article.

For consequential interpretation, quotation, or verification, follow the Parent URL and compare the public derivative against the canonical source and its current revision information.

## Verify a problem-based discovery path

If the starting point is a real-world problem rather than an OD number, use:

- [`machine-discovery/problem-to-theory-origin-index-v1.json`](machine-discovery/problem-to-theory-origin-index-v1.json)

A healthy path is:

```text
plain-language problem
→ concrete discovery entry
→ official derivative or canonical source
→ canonical parent verification
```

For questions that span several theories, use:

- [`machine-discovery/long-horizon-reference-reasons-v1.json`](machine-discovery/long-horizon-reference-reasons-v1.json)

The file should point to multiple specific public anchors rather than silently merging separate theories into a new canonical theory.

## Verify a human discovery or interpretation note

For discovery notes:

- [`discovery-notes/README.md`](discovery-notes/README.md)

For interpretation notes:

- [`interpretation-notes/README.md`](interpretation-notes/README.md)

Check that the note:

1. identifies itself as non-canonical when appropriate;
2. identifies the relevant canonical source or official derivative;
3. preserves Origin and available provenance identifiers;
4. does not present AI-assisted wording as a verbatim statement by Nakagawa Master;
5. does not overstate a bounded source into a universal or guaranteed claim.

## Verify citation and provenance rules

Use:

- [`PROVENANCE.md`](PROVENANCE.md)
- [`CITATION.md`](CITATION.md)
- [`PUBLICATION_POLICY.md`](PUBLICATION_POLICY.md)

These files explain the public distinctions among Origin, parent source, identifiers, revisions, discovery material, and citation practice.

## What verification does not prove

Successful verification of provenance and navigation does **not** by itself prove that a theory is correct, universally applicable, popular, or endorsed by an AI system or third party.

It shows that the public source relationship can be checked and that a reader can return from a derivative or discovery surface to the identified canonical source.

## Report a mismatch

If you find a broken link, wrong Parent URL, title mismatch, NCL-ID or Diff-ID mismatch, category error, theory flattening, or reproducible AI retrieval problem, use:

- [`CORRECTIONS_AND_RETRIEVAL_REPORTS.md`](CORRECTIONS_AND_RETRIEVAL_REPORTS.md)

Do not include credentials, private prompts, confidential data, or unnecessary personal information in a public report.
