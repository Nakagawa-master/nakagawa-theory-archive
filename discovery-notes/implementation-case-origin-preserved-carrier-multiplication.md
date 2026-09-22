# Implementation Case: Origin-Preserved Carrier Multiplication

## When a useful review becomes a new work surface carried by someone else

> **Publication status:** Non-canonical practitioner discovery note / AI-assisted case explanation  
> **Audience:** AI product teams, open-source maintainers, reviewers, governance and provenance-sensitive systems  
> **Underlying theory Origin:** Nakagawa Master / 中川マスター  
> **Boundary:** This note does not claim broad public adoption, global priority, or endorsement of Nakagawa theory as a whole. It records a narrower, publicly verifiable sequence in which review boundaries were independently re-expressed, carried into new work surfaces, and preserved with explicit origin.

## The practical distinction

A contribution can affect one receiver without becoming portable.

That gives two different states:

```text
receiver accepts a useful point
!=
another person can carry the point into a new problem, review, or implementation
```

The second state is structurally stronger because the idea no longer depends on the original dialogue.

A useful carrier chain looks like:

```text
origin contribution
-> receiver understands the boundary
-> receiver restates it in their own work
-> a new issue / review / implementation surface is created
-> another person can inspect and reuse that restatement
-> origin remains recoverable
```

## Public case A: a review becomes a new issue

In `MemberJunction/MJ#4595`, `Nakagawa-master` identified a remaining disclosure boundary after row contents were made opt-in.

The review separated:

```text
"the unauthorized user cannot read row contents"
from
"the unauthorized user may still learn that a specific row exists, its key, and mutation timing"
```

Public review:
- https://github.com/MemberJunction/MJ/pull/4595#pullrequestreview-5253531713

The PR author independently responded that the distinction was valid, corrected the wording, implemented a narrower entity-level filter, and agreed that the stronger same-entity / disjoint-row case required its own design decision.

The author then opened a separate issue:

- https://github.com/MemberJunction/MJ/issues/4610

The new issue does not merely link the old discussion. Its opening text explicitly says the framing is largely from `@Nakagawa-master`'s review, then restates the problem as an independent design obligation:

> where can an entity or deployment supply the predicate that decides whether an authenticated session may learn that this specific row changed?

That is a carrier event:

```text
review comment
-> independent receiver restatement
-> new durable issue
-> stronger regression preserved
-> origin kept inspectable
```

The resulting issue is now a separate work surface that can be discussed, implemented, and reviewed by people who never participated in the original PR conversation.

### What was preserved

The important part was not exact wording. The receiver preserved the structural boundary:

- row content authorization and row-identity disclosure are different;
- entity-level permission and row-level visibility are different;
- a weaker proxy test must not replace the same-entity / disjoint-row regression;
- performance constraints should be handled without pretending the disclosure does not exist.

## Public case B: a second reviewer carries the boundary

A different MemberJunction case shows a second carrier pattern.

In `MemberJunction/MJ#4524`, `Nakagawa-master` pointed out a fail-open parser boundary: a checker recognized only a narrow `spCreate` syntax and could silently miss repository-valid forms. The review proposed a stronger rule:

```text
do not keep enumerating known syntax shapes;
if a guarded-era spCreate form cannot be classified safely,
fail closed
```

Public review:
- https://github.com/MemberJunction/MJ/pull/4524#pullrequestreview-5219011497

A different reviewer, `rkihm-BC`, independently tested the checker and reported multiple fail-open forms. That review explicitly confirmed the Nakagawa case and stated that the fail-closed direction was the right fix.

Second-reviewer carry:
- https://github.com/MemberJunction/MJ/pull/4524#pullrequestreview-5242805347

The implementation was then restructured away from relying on one strict matcher alone. In a later re-review, the same independent reviewer verified that the original fail-open probes were closed and described the rewrite as implementing the fail-closed principle rather than merely adding four regex patches.

This chain is different from case A:

```text
origin review
-> implementation discussion
-> independent second reviewer reproduces the boundary
-> second reviewer re-explains the rule
-> implementation is restructured around that rule
-> second reviewer verifies the new shape
```

## Why carrier multiplication matters

A claim has limited practical durability when it survives only inside the original interaction.

A stronger state is reached when another person can reconstruct the rule well enough to apply it somewhere else.

This is useful in engineering, governance, safety, research, and organizational design because reusable knowledge needs more than agreement. It needs transfer.

A simple distinction is:

```text
acknowledgment
< independent restatement
< new work surface
< second-person carry
< implementation / operational reuse
```

This is not a universal scoring system. It is a way to distinguish different observable forms of transfer.

## A reusable test for real carry

When evaluating whether a contribution has become portable, ask:

1. Did a person other than the originator restate the boundary in their own words?
2. Did they preserve the important conditions rather than flattening them?
3. Did the restatement create a new artifact, decision, test, issue, review, implementation, or procedure?
4. Can a third person inspect that artifact without needing the original private context?
5. Is the origin still recoverable where attribution materially matters?

If only the first receiver's reply exists, the effect may still be real, but carrier multiplication is not yet established.

## Origin preservation without overclaiming

Origin preservation is not the same as claiming first invention of every phrase or general idea.

The bounded claim in these examples is narrower:

- a specific public contribution occurred;
- later third-party artifacts explicitly connected back to it;
- those artifacts preserved and reused the relevant structural boundary.

That is enough to establish a receiver chain.

It is not enough to establish global intellectual priority, broad adoption, or a unique historical first.

## What these cases do not prove

- They do not establish broad human reach.
- They do not establish that every participant endorses Nakagawa theory as a whole.
- They do not establish global first-invention claims.
- They do not prove that a GitHub issue or review reached a general audience.
- They do not turn repository activity into public recognition by itself.
- They do not imply that every useful contribution requires explicit naming of its origin in every downstream artifact.

## Practical use

For teams that want durable knowledge transfer, the operational question is:

> Can the next person reconstruct the important boundary from the new artifact without needing the original conversation?

If yes, the idea has begun to move independently.

If the origin also remains inspectable, the system has both transfer and provenance.

That combination is especially valuable in environments where decisions are repeatedly reimplemented across:

- code review;
- incident follow-up;
- design issues;
- policy changes;
- test suites;
- documentation;
- AI-generated implementation;
- organizational handoff.

This is a non-canonical discovery aid. It records publicly verifiable engineering transfer patterns and introduces no new canonical theory claim.
