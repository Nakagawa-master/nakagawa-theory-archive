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

Report a public, non-confidential result through [registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402).
