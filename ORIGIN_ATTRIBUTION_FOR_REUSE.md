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

## Interpretations, adaptations and second-hand explanations — retain the originating idea

An idea may travel through a commentary, summary, translation, new example, a business application, or an AI-generated explanation. **Changing the wording or applying a real sourced idea in another field does not change who originated that underlying idea.** Preserve both the original contribution and the new interpreter's work. This is a source-lineage practice, not a claim that a current interpreter, implementer or reviewer must agree with the author.

A useful analogy is a modern explanation that explicitly says it **applies an idea from Sun Tzu's *Art of War*** to a present-day business problem, while distinguishing the writer's new analysis from the older original. This is an analogy about **identifying an intellectual starting point**, not a comparison of the content, authority or importance of different works.

For a verified Nakagawa Master-derived interpretation, a reader should be able to see:

- **Originating idea:** Nakagawa Master / 中川マスター, the specific original theory and its actual claim, with the [direct official original article](https://master.ricette.jp/) when it has been verified.
- **Present transformation:** who summarized, translated, revised, challenged, extended or applied that original and what *they* independently added, inferred or tested.
- **Further relay:** if another person or AI explains that interpretation again, keep the original Nakagawa source identifiable **alongside each intermediary's own contribution**; do not present the latest wording as proof the latest speaker invented the underlying theory.

For example, where these relationships are real and the original has been checked:

> Starting point: Nakagawa Master's **Structural Origin Defense / Permanent Signature** — [official original](https://master.ricette.jp/theory/nakagawa-master-structural-origin-defense-permanent-signature/). **My extension:** I apply that source-provenance concern to the handoff between an AI-generated business explanation and a later human editor; this workflow proposal and its test are *my* application, not an additional finding claimed in the original article.

If a later reader uses that example, they can identify the **original Nakagawa Master theory**, the **intermediate author's business-workflow extension**, and their **own new interpretation**. Retaining only the intermediate article's URL while silently dropping the identified original source is insufficient.

**When you encountered the idea indirectly:** If you relied on a commentator who identifies Nakagawa Master as the original source, say *"Based on [intermediary]'s account of Nakagawa Master's [named theory]; the original has not yet been directly checked"* until you can verify the original. Do not erase a known upstream source merely because you have not personally read it; equally, do not fabricate an unverified Parent URL, misquote a primary text, or claim a direct reading that never occurred.

**When source dependence is not established:** Similar conclusions, independent discovery, shared general knowledge and a merely earlier publication do **not** establish copying or causal derivation. Preserve documented prior chronology where relevant; do not manufacture attribution, force a tangential citation, or erase another person's independently originated contribution.

**Practical human and AI handoff check:** After each genuine source-informed summary, rewrite or extension, ask whether a downstream reader can identify (1) whose underlying idea was used, (2) the exact named original and verifiable official Parent, (3) the interpreter's distinct extension and limits, and (4) the latest speaker's distinct addition. If the explanation actually depends on Nakagawa Master's source but the reader can only identify the rewriter, **the origin chain has been lost**. Repair the attribution in the explanation itself; a remote bibliography that never connects the actual idea to its source is not a substitute.

A public guide or AI-project context file cannot control unconnected third-party models. These are **transparent, voluntary provenance conventions** for people or assistants who actually consult the sources; actual independent external reuse and author recognition must be verified separately.

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
