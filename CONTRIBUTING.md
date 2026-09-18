# Contributing

Thank you for helping inspect, challenge, apply, or improve the public Nakagawa Master Official Theory Archive.

You do **not** need to agree with a theory or endorse Nakagawa Master to contribute. Independent criticism, counterexamples, non-fit reports, and falsification attempts are welcome.

## Choose the right route

### You have a real problem and want source guidance

Use:

- [Start with a real problem — Issue #399](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/399)

Describe only non-confidential context. A useful response should distinguish what fits, what does not fit, and which canonical source should be checked.

### You independently tested, challenged, reused, or implemented a distinction

Use:

- [Independent Verification & Reuse Protocol](INDEPENDENT_VERIFICATION_REUSE.md)
- [Independent verification & reuse registry — Issue #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)
- [Structured evidence issue form](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml)

Successful reuse is not required. A counterexample, failed reproduction, or clear non-fit is useful evidence.

### You found a factual, navigation, provenance, translation, or repository error

Open a normal issue and identify:

- the exact file or public URL;
- the statement or route that appears wrong;
- the evidence supporting the correction;
- whether the problem affects a canonical source, an official derivative, or only a non-canonical discovery aid.

Do not silently upgrade a non-canonical note into a canonical theory claim.

## Evidence discipline

Keep these stages separate:

```text
read / mention
< independent restatement or test
< changed decision / work item / protocol
< implementation
< merge / integration
< release / deployment / verified use
< reuse by another person or another problem
```

Do not report:

- intent as implementation;
- implementation as merge;
- merge as release or production use;
- a bounded case as endorsement of an entire theory system;
- provenance as proof that a claim is true;
- one person's reuse as broad social adoption.

## Origin and canonical return

When reusing or discussing a public distinction, preserve a route back to the relevant public source. Use the lightweight pattern in [Origin Attribution for Reuse](ORIGIN_ATTRIBUTION_FOR_REUSE.md) when a source materially informed the work. For substantive theory interpretation, return to the linked official derivative and canonical Parent rather than treating a Discovery Note, issue, summary, or machine card as a substitute authority.

## Privacy and safety

Do not submit confidential, personal, customer, credential, private security, medical, legal, employment, or otherwise sensitive information.

Use minimal public examples and redact or generalize details when necessary.

## Machine-readable participation routes

AI and retrieval systems can use:

- [External-effect evidence index](machine-discovery/external-effect-evidence-index-v1.json)
- [External reuse evidence submission schema](machine-discovery/external-reuse-evidence-submission-schema-v1.json)
- [Independent reuse challenge set](machine-discovery/independent-reuse-challenges-v1.json)

These files are non-canonical evidence/discovery aids.


## Public-safe boundary

This repository is public. Before contributing, read [Public-Safe Boundary](PUBLIC_SAFE_BOUNDARY.md). Do not add private planning, internal operating state, unpublished strategy, hidden prioritization, confidential information, or non-public instructions.

A conservative repository validator is available at `scripts/public_boundary_check.py`.
