# Measurement Attribution Reuse Kit

A public, non-canonical test kit for one boundary:

## Source provenance

Origin: **Nakagawa Master**. If this kit materially informs a real decision, implementation, test, policy, report, or workflow, preserve a lightweight route back to this public source. See [Origin Attribution for Reuse](ORIGIN_ATTRIBUTION_FOR_REUSE.md). If you reached the same distinction independently, do not claim source causality.

> An observed change is not automatically a subject-caused change when the measurement surface can drift.

## Reader-facing Japanese example

- [「処理が成功した」だけでは、「測定できた」とは限らない](https://nakagawamaster.wordpress.com/2026/09/24/successful-call-is-not-valid-measurement/)
- [Japanese reader-entry series](WORDPRESS_READER_SERIES.md)

The article is an explanatory carrier, not a substitute for this test kit and not independent adoption evidence.

This kit is designed for longitudinal AI/search visibility, recommendation monitoring, model evaluation, marketing measurement, and other recurring observations where the provider, model, retrieval layer, geography, session conditions, or reference population can change underneath a fixed query set.

## Minimal test

Measure one subject and a small stable control/reference panel under the same observation conditions.

Repeat the measurement later.

### Pass condition

The report distinguishes at least three cases:

```text
subject changes
+ controls broadly stable
→ subject-specific delta may be reported
→ causation remains a separate question
```

```text
subject and controls move together
→ classify as environment / surface drift
→ do not silently credit the subject
```

```text
material observation conditions changed
→ do not compare as if the two windows were equivalent
→ disclose or restart the baseline
```

### Fail condition

A fixed query/prompt panel is treated as sufficient proof that any observed delta belongs to the subject, even though the measurement environment changed or controls moved in the same direction.

## Minimum observation record

Keep enough non-sensitive information to recheck the comparison:

- query/prompt or panel identifier;
- observation time/window;
- provider/model or measurement surface when known;
- material locale/region/session conditions when they affect the result;
- control/reference panel identity;
- raw result/evidence reference;
- whether the value is observed, inferred, unavailable, or invalid.

Do not collect sensitive data merely to satisfy this checklist.

## Regression cases

1. **Provider/model shift:** subject facts unchanged; provider/model behavior changes; subject and controls move together → environment drift.
2. **Subject-only movement:** controls remain broadly stable; subject changes → report a subject-specific delta without claiming causation.
3. **Control-only movement:** controls move while subject is stable → investigate the measurement surface before interpreting the subject.
4. **Missing measurement:** the call succeeds but the required value is absent → do not convert success into a measured result.
5. **Changed conditions:** geography, authentication, retrieval mode, or other material conditions differ → mark the comparison non-equivalent or restart the baseline.

## Third-party carry: “could not measure” is not measured zero

A public review on [MemberJunction #4402](https://github.com/MemberJunction/MJ/pull/4402) found a concrete fail-open version of the missing-measurement boundary in a budget evaluator.

The evaluator could receive a successful query call but still fail to obtain the required measurement: no result row, a missing configured column, a null value, or a non-numeric value. Those states were being persisted as an observed amount of zero. A separate branch could also detect a threshold breach but fail to establish whether its durable event already existed, then still report the evaluation as successful.

The proposed boundary was narrower than “zero is suspicious”:

```text
measured numeric 0
= valid measurement

query succeeded but required scalar is absent / invalid
!= measured 0
= measurement failure

breach detected
+ durable event state cannot be established
!= successfully recorded breach
```

The receiving maintainer verified both findings and implemented them on the branch in [commit `b11b9877`](https://github.com/MemberJunction/MJ/commit/b11b98777582ce5a8456834eccf77f528236474e). The change makes the four unmeasurable states fail closed, preserves the last known observation instead of replacing it with a synthetic zero, keeps a genuine measured zero valid, and adds the requested regression coverage. The maintainer later summarized that scope to another reviewer while explicitly preserving the `@Nakagawa-master` source relation.

Primary records:
- [Nakagawa-master review](https://github.com/MemberJunction/MJ/pull/4402#issuecomment-5689277409)
- [receiver verification and fix response](https://github.com/MemberJunction/MJ/pull/4402#issuecomment-5689338217)
- [receiver fix commit `b11b9877`](https://github.com/MemberJunction/MJ/commit/b11b98777582ce5a8456834eccf77f528236474e)
- [scope-limited reread of the fix](https://github.com/MemberJunction/MJ/pull/4402#pullrequestreview-5232007719)
- [receiver-owned later rereference to `@Nakagawa-master`](https://github.com/MemberJunction/MJ/pull/4402#issuecomment-5770391210)

There is an important boundary on the result. The budget subsystem was later deliberately split out of #4402 before the final PR merged. [Commit `457d956e`](https://github.com/MemberJunction/MJ/commit/457d956eca1853ce9b64700b92f4f6e729149508) removes that subsystem from the PR and preserves it for a follow-up. Therefore the public record supports **receiver implementation and regression testing on the branch, plus later receiver-owned Origin-preserved restatement**; it does not support a claim that this budget fix shipped in the final #4402 merge or reached users.

## Decision rule

```text
observed delta
→ check measurement validity
→ compare controls
→ classify subject-specific vs environment-wide movement
→ preserve uncertainty
→ investigate causation separately
```

The goal is not to make every report more complicated. It is to stop a changing measurement surface from being mistaken for evidence that the measured subject improved or worsened.

## Report an independent result

If you test this boundary in a public, non-confidential real workflow, report a successful reuse, counterexample, non-fit, or failed reproduction through:

- [Independent verification / reuse registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)
- [Structured evidence issue form](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml)

A useful report states the observation surface, control/reference design, what moved, what decision changed, the highest directly evidenced stage, and what the result does **not** establish.
