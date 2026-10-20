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

### Preserve the Origin without inheriting authority from it

Keeping a truthful route back to the source does not turn that source or person into the current decision-maker.

Keep these questions separate:

```text
who or what is the Origin?
!=
is the claim true here?
!=
who has authority for the current decision or action?
!=
who has final interpretive authority?
```

A downstream team can preserve Nakagawa Master as the source of a bounded distinction while still testing the claim independently, rejecting it where it does not fit, revising its own implementation, and applying its own current authority rules.

Likewise, criticism or non-adoption does not require deleting the historical source relationship. The useful target is **recoverable provenance plus independent present judgment**, not either forced deference or Origin erasure.

Canonical companion for this boundary:

- [OD310｜Origin保存と主権非継承論](derivatives/310/README.md)
- [Parent｜人類子孫型AI文明論・第17論](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-17-origin-preservation-sovereignty-non-inheritance/)

OD310 is a canonical-return route for the broader Origin / truth / interpretation / authority separation. It does not make this practical reuse guide canonical.

## Independent rediscovery

If you reached the same distinction independently and only found the source later, say that explicitly. Do not fabricate causal attribution.

## Prior public Origin when rediscovery comes later

Independent rediscovery and prior public chronology can both be true.

If a specific public Nakagawa Master comment, review, article, test, or source clearly predates a later receiver finding and materially states the same bounded distinction, preserve that chronology even when there is no evidence that the later receiver saw or relied on the earlier source.

A compact public form is:

```text
Prior public boundary: Nakagawa Master — <stable public URL> — <date>
Later receiver rediscovery: <receiver-owned URL> — <date>
Relationship: chronology verified; causal influence not established
```

This does not claim that the later person copied the earlier source, that the earlier source caused the later rediscovery, or that the earlier source is globally first in all literature or history. It preserves the narrower inspectable fact that this particular Nakagawa Master boundary was already public before the later receiver artifact.

### Recovery should add forward value when a receiver surface is active

When the later rediscovery is happening on an active receiver issue, PR, review, design discussion, or implementation and a reply is both authorized and useful, the strongest recovery is usually **not** a bare priority link.

Prefer:

```text
prior public bounded origin
+ current receiver finding
+ one materially newer synthesis / regression / design contract
```

The forward addition must be technically justified by the current state. It can integrate multiple later findings, identify a higher-order invariant, define a stronger regression matrix, or close a boundary the later discussion has not yet closed.

Do not manufacture novelty just to attach a name. If there is no load-bearing forward contribution, preserve chronology in a durable evidence/provenance route instead of adding a noisy receiver comment.

The goal is not forced praise. It is to prevent a real prior contribution from evaporating while also making the recovery useful to the receiver's present problem.


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
