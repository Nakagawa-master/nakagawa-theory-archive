# Practical Boundary Checks

A public, non-canonical checklist for testing several distinctions that have already produced independently inspectable third-party implementation or review evidence.

Use this as a **preflight** for a real, non-confidential workflow. It is not a substitute for domain-specific engineering, legal, security, safety, or professional review.

## Reader-facing Japanese entries

The short Japanese reader-entry series turns several boundaries below into concrete examples:

- [6つの短い実例 → source → 独立検証](WORDPRESS_READER_SERIES.md)
- Migration / overwrite example: [「同じIDだから上書きしてよい」とは限らない](https://nakagawamaster.wordpress.com/2026/09/24/same-id-does-not-mean-safe-overwrite/)

These WordPress entries are explanatory carriers, not evidence of independent adoption.

## 1. Approval / consent / exception

Before relying on a stored approval, ask:

- What exactly was approved?
- Which recipient, purpose, scope, policy, or notice version did it bind to?
- Has any material condition changed since approval?
- Can the system distinguish historical approval from current authorization?
- If current authorization no longer holds, is the old approval still preserved as history rather than overwritten?

Useful regression:

```text
approve under state/version A
→ material condition changes to B
→ old evidence remains queryable
→ B requires a new valid authorization
```

## 2. Migration / synchronization / overwrite

Before replacing existing state because identifiers match:

- Does matching identity prove common ownership or common provenance?
- Who is authoritative for the current destination state?
- Can both sides have changed independently?
- Is the operation overwrite, preserve, merge, reconcile, or refuse?
- Is that policy explicit and testable?

Useful regression:

```text
same ID
+ divergent local state
+ divergent incoming state
→ policy chooses intentionally
→ no silent overwrite merely because the ID matches
```

## 3. Measurement / reporting / AI evidence

Before treating a successful operation as a valid result:

- Did the query/tool/model call succeed?
- Was the required value actually observed or measured?
- Is the value grounded in the intended source?
- Is the measurement current enough for the decision?
- Can the UI/API distinguish missing, unknown, inferred, measured, and invalid?
- Could the provider, model, retrieval surface, geography, or session conditions have shifted between observation windows?
- Is there a stable control/reference panel that can distinguish subject-specific movement from environment-wide drift?
- Are the material observation conditions and raw-evidence identity preserved well enough to recheck the comparison?
- If the subject and controls move together, does the report label the result as environment/surface drift rather than silently crediting the subject?

Useful regressions:

```text
operation returns successfully
+ required measurement unavailable
→ output is not silently reported as a valid measured value
```

```text
same fixed observation panel
+ subject facts remain unchanged
+ provider/model behavior shifts
+ control cohort moves in the same direction
→ report environment / surface drift
→ do not credit subject-specific improvement
```

```text
control cohort remains broadly stable
+ subject-specific observation changes
→ subject-specific delta may be reported
→ causation still requires separate evidence
```

This matters for AI/search visibility, recommendation monitoring, model evaluations, and any longitudinal report where the measurement environment can change underneath a fixed query set. A stable prompt/query library is useful, but it does not by itself prove that an observed delta belongs to the subject rather than the measurement surface.

For a minimal independent test, use the [Measurement Attribution Reuse Kit](MEASUREMENT_ATTRIBUTION_REUSE_KIT.md).

## 4. Recommendation / ranking provenance

Before grouping recommendations that display the same explanation:

- Does every recommended person/item retain its own evidence source?
- Could one recommendation be based on code history while another is model/scout inference?
- Does grouping make the strongest source appear to support the whole group?
- Can a reviewer recover “who was recommended because of what?”

Useful regression:

```text
same displayed reason
+ different evidence source categories
→ grouped UI still preserves item → source association
```

## 5. External message / payment / provider side effect

Before retrying after an exception:

- Did the provider definitely reject the action?
- Or might the provider have accepted it before the response was lost?
- Is there an explicit `outcome_unknown` state?
- Is the retry protected by provider-side idempotency or reconciliation?
- Can an operator distinguish safe retry from uncertain duplicate risk?

Useful regression:

```text
provider accepts action
→ response is lost
→ local state becomes outcome_unknown
→ restart does not blindly resend
→ reconciliation or idempotency resolves the original attempt
```

## 6. Historical records

Before using current status to answer a historical question:

- Is the question “who is eligible now” or “who participated then”?
- Are current membership/entitlement dates being substituted for event-time state?
- Can a past record remain correct after a person later leaves, changes role, or loses access?
- Can historical corrections still be made without reactivating current membership?

Useful regression:

```text
person valid during past event
→ person later leaves
→ past participation remains visible/correctable
→ current membership remains inactive
```

## Public implementation example: reviewer recommendation provenance

For a minimal independent reproduction, use the [Reviewer-Provenance Reuse Kit](POSTHOG_PROVENANCE_REUSE_KIT.md).

A concrete external case now reaches beyond review and merge.

In [PostHog #102550](https://github.com/PostHog/posthog/pull/102550), a review identified that grouping reviewer suggestions by identical explanation text could pool different evidence-source labels and obscure which source justified each person. The external maintainer changed the grouping rule and regression coverage so identical reasons group only within the same source category.

Public evidence:

- [Nakagawa-master review](https://github.com/PostHog/posthog/pull/102550#pullrequestreview-5242012853)
- [Third-party implementation commit](https://github.com/PostHog/posthog/commit/764c347e488cb9f8bb155a2d95c5f40a3b92a08c)
- [Merge commit](https://github.com/PostHog/posthog/commit/6e2c760dadbaba764c83e93900c3510e6a703c03)
- [Deployment status](https://github.com/PostHog/posthog/pull/102550#issuecomment-5722917557), showing deployment to dev, prod-eu, and prod-us

The same external maintainer later reused the same distinction on [PostHog #102686](https://github.com/PostHog/posthog/pull/102686) without a fresh Nakagawa prompt. That downstream PR was merged on 2026-09-18 ([merge commit](https://github.com/PostHog/posthog/commit/0d533b34e67923055b6912aca93b6d60eb98bd09)) and its deploy-status record shows deployment to dev, prod-us, and prod-eu.

This case supports only the bounded statement that a specific provenance distinction changed third-party implementation, merged and deployed, and was then reused on another merged/deployed surface by the same external maintainer. It does not establish second-person Nakagawa attribution on #102686, user-scale outcome, or whole-system endorsement.

## What to do with a result

If this checklist changes a public, non-confidential decision, procedure, test, document, or implementation, you can report the bounded result through:

- [Independent verification / reuse registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)
- [Structured evidence issue form](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml)

Counterexamples and non-fit results are welcome.

## Evidence boundary

Do not infer:

- implementation from intent;
- merge from implementation;
- release or production use from merge;
- broad adoption from one bounded case;
- whole-theory endorsement from a specific fix;
- truth from provenance alone.

For independently inspectable external cases, see [Real-World Impact](REAL_WORLD_IMPACT.en.md).
