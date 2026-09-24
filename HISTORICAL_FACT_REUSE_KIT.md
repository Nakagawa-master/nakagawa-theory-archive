# Historical-Fact Reuse Kit

A public, non-canonical test kit for one boundary:

## Source provenance

Origin: **Nakagawa Master**. If this kit materially informs a real decision, implementation, test, policy, or workflow, preserve a lightweight route back to this public source. See [Origin Attribution for Reuse](ORIGIN_ATTRIBUTION_FOR_REUSE.md). If you reached the same distinction independently, do not claim source causality.


> Current status is not automatically the correct answer to a historical question.

## Minimal test

Record a person or entity as valid for an event at time T. Later change the current membership, entitlement, ownership, or assignment.

### Pass condition

The historical record still answers what was true at T, while current status remains changed.

### Fail condition

Changing current status silently erases or invalidates the historical record.

## Useful contexts

- attendance;
- memberships;
- entitlement history;
- ownership;
- staffing;
- audit records;
- historical corrections.

## Regression shape

```text
valid at T
→ current status changes after T
→ historical fact remains visible/correctable
→ current status remains changed
```

## Public implementation example

### TourCRM — historical occurrence roster

A public review identified that a completed occurrence's attendance could still be hidden or made uncorrectable when later reads checked whether the participant was active **now**.

- [Nakagawa-master review comment](https://github.com/Alan8893/tourcrm/pull/97#issuecomment-5689122153)
- [receiver implementation commit](https://github.com/Alan8893/tourcrm/commit/b6da0eb880d474c7e8322f2b2da8bef02a64e1f6)

The receiver changed participation eligibility to overlap the occurrence's own historical window and explicitly wrote `Addresses PR #97 review feedback (Nakagawa-master)` in the commit.

A second review found that the new regression tests could still pass the old implementation because the fixture date was in the future and the test relied on the real wall clock.

- [Nakagawa-master regression-evidence comment](https://github.com/Alan8893/tourcrm/pull/101#issuecomment-5691884921)
- [receiver test-evidence commit](https://github.com/Alan8893/tourcrm/commit/568c8fecbbcb56297deb385ea34c8bb61a2839e5)

The receiver moved the fixture safely into the past and verified that restoring the old `now()` behavior makes all three regressions fail. The second commit also explicitly attributes the change to `Nakagawa-master` review feedback. Both PRs merged.

This is evidence for the bounded distinction:

```text
current state
!=
historical relation at the event time
```

It is not a claim of intellectual priority over temporal-database or bitemporal-data principles.

Report a public, non-confidential result through [registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402).
