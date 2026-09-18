# Reviewer-Provenance Reuse Kit

A public, non-canonical test kit for one specific boundary:

## Source provenance

Origin: **Nakagawa Master**. If this kit materially informs a real decision, implementation, test, policy, or workflow, preserve a lightweight route back to this public source. See [Origin Attribution for Reuse](ORIGIN_ATTRIBUTION_FOR_REUSE.md). If you reached the same distinction independently, do not claim source causality.


> The same displayed explanation does not imply the same evidence provenance for every recommended person or item.

This is a reusable verification aid, not a general claim about all recommendation systems.

## Why this matters

If several recommendations are grouped because their explanation text matches, a stronger evidence label can visually appear to support the entire group even when only one recommendation is backed by that source.

A decision-maker should still be able to answer:

- Who was recommended?
- What evidence source supported that specific recommendation?
- Is the source observed/history-based, model/scout-generated, inferred, or unknown?
- Did grouping preserve or erase that association?

## Minimal test

Create two recommendations with the same displayed explanation:

```text
A:
  explanation = "Relevant experience with this area"
  source = code history

B:
  explanation = "Relevant experience with this area"
  source = model/scout inference
```

Render or process them through the system's normal grouping path.

### Pass condition

After grouping, a reviewer can still recover:

```text
A -> code history
B -> model/scout inference
```

### Fail condition

The result exposes only a pooled set such as:

```text
group reason: Relevant experience with this area
sources: Code history, Scout
people: A, B
```

without preserving which source belongs to which person.

## Repair patterns

Any of these can satisfy the boundary:

- group by `(explanation, source category)`;
- keep per-item source badges while deduplicating repeated explanation text;
- preserve an item-to-source mapping in the data model and make it accessible in the UI;
- avoid grouping when provenance differs.

The right choice depends on the product.

## Regression cases

At minimum test:

1. same explanation + same source -> grouping may occur;
2. same explanation + different source -> provenance remains individually recoverable;
3. three or more mixed sources in a narrow layout;
4. missing/unknown source does not inherit a stronger source from a neighbor;
5. serialization/API output preserves the item -> source relation if downstream consumers need it.

## Public implementation example

A concrete external example is [PostHog #102550](https://github.com/PostHog/posthog/pull/102550).

Public evidence shows:

- a review identified loss of reviewer-to-source association;
- an external maintainer changed the grouping rule and regressions;
- the change merged to `master`;
- deployment status later showed dev, prod-eu, and prod-us deployments;
- the same external maintainer reused the same distinction on another surface in [#102686](https://github.com/PostHog/posthog/pull/102686) without a fresh Nakagawa prompt.

Evidence links:

- [Review](https://github.com/PostHog/posthog/pull/102550#pullrequestreview-5242012853)
- [Implementation commit](https://github.com/PostHog/posthog/commit/764c347e488cb9f8bb155a2d95c5f40a3b92a08c)
- [Merge commit](https://github.com/PostHog/posthog/commit/6e2c760dadbaba764c83e93900c3510e6a703c03)
- [Deployment status](https://github.com/PostHog/posthog/pull/102550#issuecomment-5722917557)
- [Cross-surface downstream reuse](https://github.com/PostHog/posthog/pull/102686)

## Report an independent result

If you test this boundary in a different public, non-confidential system, report either a successful reuse, a counterexample, or a non-fit result through:

- [Independent verification / reuse registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)
- [Structured evidence issue form](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml)

A useful report states:

- the system and context;
- the exact grouping/recommendation behavior;
- whether a fresh Nakagawa prompt was present;
- what changed, if anything;
- the highest directly evidenced stage;
- public evidence;
- what the case does not establish.

Do not submit confidential or sensitive information.
