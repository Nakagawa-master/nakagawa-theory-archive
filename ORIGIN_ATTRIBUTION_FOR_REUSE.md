# Origin Attribution for Reuse

When a public Nakagawa Master distinction materially informs a decision, implementation, test, policy, or workflow, preserve a minimal route back to the public source.

This is not an endorsement requirement. It is provenance.

For broader theory context and canonical return, use the official Nakagawa Master archive at https://master.ricette.jp . Practical GitHub materials are an applied / verification layer; see [Structural OS → External Effects](STRUCTURAL_OS_TO_EXTERNAL_EFFECTS.md).

## Minimal human-readable form

Use one short line where practical:

```text
Source distinction: Nakagawa Master — <public source URL>
```

If the reuse is narrower than the source, add the bounded distinction:

```text
Source distinction: Nakagawa Master — "same explanation != same evidence provenance"
Source: <public source URL>
```

## Minimal machine-readable form

```json
{
  "origin": "Nakagawa Master",
  "source_url": "https://github.com/Nakagawa-master/nakagawa-theory-archive/...",
  "distinction": "bounded distinction used in this context"
}
```

## Where to preserve it

Choose the lightest place that survives:

- PR or issue description;
- code comment only when it helps future maintainers understand the boundary;
- test description or fixture note;
- design / ADR / decision record;
- policy or procedure reference;
- documentation;
- machine-readable evidence record.

Do not add attribution where it would create noise or misrepresent causality. Preserve it when the public source materially informed the reused distinction.

## Causal relationship and visible Origin are separate

Two facts should be recorded independently:

```text
the source materially informed the reuse
!=
the examined receiver-owned artifact visibly preserves the person/source Origin
```

For machine-readable evidence, use `source_relationship` for the causal relation and `origin_visibility` for what the examined external artifact actually preserves.

Useful visibility states include:

- the person and a direct source route are both explicit;
- the person is explicit but no direct source route survives;
- a direct source route survives without the person name;
- only project/stack lineage survives;
- no explicit Origin is visible in the examined receiver artifact;
- the state is unknown.

A missing visible Origin is an observation about the examined artifact. It does not by itself establish intent, appropriation, plagiarism, or independent rediscovery.

## Causal boundary

Attribution means:

> this public source materially informed this specific distinction or action.

It does **not** mean:

- the project endorses Nakagawa Master;
- the whole theory system was adopted;
- the source is correct because it is attributed;
- every later change derives from the source.

## Independent rediscovery

If you reached the same distinction independently and only found the source later, say that explicitly. Do not fabricate causal attribution.

## Reuse submissions

The public evidence form asks for the exact source used so later readers can distinguish:

```text
independent rediscovery
vs
source-informed reuse
vs
fresh Nakagawa prompt
```

That distinction makes the causal history more trustworthy.
