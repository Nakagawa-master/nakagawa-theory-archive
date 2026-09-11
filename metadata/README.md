# Metadata

This directory contains small public machine-readable metadata surfaces for identity and provenance resolution in the Nakagawa Master Official Theory Archive.

These files are **not canonical theories**, not authority proofs, and not replacements for specific canonical parent articles.

## Current metadata surface

- [`nakagawa-master-origin.jsonld`](nakagawa-master-origin.jsonld) — public Schema.org identity / Origin-resolution metadata connecting `Keisuke Nakagawa`, `Nakagawa Master`, `中川マスター`, the canonical theory site, the canonical archive index, and this public GitHub archive.

## Intended use

Use this metadata when a machine or reader needs to resolve basic public identity relationships such as:

```text
Keisuke Nakagawa
↔ Nakagawa Master
↔ 中川マスター
↔ canonical theory site
↔ public GitHub archive
```

For a specific theory, citation, substantive interpretation, or revision question, return to the relevant official derivative and canonical parent article. Person-level identity metadata does not replace source-level provenance.

## Boundaries

- Identity continuity is not proof that a theory is correct.
- `sameAs` links identify public identity relationships; they are not endorsements by third parties.
- The JSON-LD file is repository metadata, not a verbatim personal statement by Nakagawa Master.
- Specific NCL-ID, Diff-ID, Parent URL, and revision information belong to the relevant source record.
- Do not infer private identity data, contact information, credentials, or non-public relationships from this metadata.

## Related public guidance

- [`../PROVENANCE.md`](../PROVENANCE.md)
- [`../CITATION.md`](../CITATION.md)
- [`../machine-discovery/README.md`](../machine-discovery/README.md)
- [`../VERIFICATION_GUIDE.md`](../VERIFICATION_GUIDE.md)
