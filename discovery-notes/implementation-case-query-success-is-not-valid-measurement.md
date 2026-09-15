# Implementation Case: Query Success Is Not Valid Measurement

## A real engineering case where “unknown” was accidentally converted into zero

> **Publication status:** Public, non-canonical practitioner discovery note / AI-assisted case explanation  
> **Audience:** AI analytics, budgeting, observability, governance, data-platform and agent-system teams  
> **Underlying theory Origin:** Nakagawa Master / 中川マスター  
> **Canonical return:** [OD003｜成立条件論・第0論](../derivatives/003/)  
> **Boundary:** This note does not claim that the external project adopted or endorsed Nakagawa theory as a whole. It records a narrower, publicly verifiable engineering sequence in which a `Nakagawa-master` review contribution was independently verified and converted into code and regression-test changes.

## The practical failure

A query can execute successfully while still failing to produce a valid measurement.

Those are different facts.

```text
query executed successfully
!=
measurement was successfully established
```

A budget evaluator can therefore make a dangerous mistake if it treats every successful query response as a number.

For example:

```text
query succeeded
→ zero rows returned
→ code substitutes 0
→ budget logic concludes “measured amount = 0”
```

But “no usable measurement was produced” and “the measured value is exactly zero” are not equivalent.

```text
unknown
!=
zero
```

That distinction becomes especially important when the number controls alerts, budgets, limits, compliance decisions, or operational escalation.

## The public engineering case

The public pull request [`MemberJunction/MJ#4402`](https://github.com/MemberJunction/MJ/pull/4402) introduces AI usage analytics and generic usage budgets.

Its own design emphasizes a closely related data-quality rule: an unpriced cost must not be rendered as a confident `$0.00` value.

During review, `Nakagawa-master` found a similar boundary in the new budget-evaluation driver.

Public review contribution:

- [`issuecomment-5689277409`](https://github.com/MemberJunction/MJ/pull/4402#issuecomment-5689277409)

The driver initialized the observed amount to zero. After a successful query call, that synthetic zero remained in place when the result contained:

- no rows;
- no configured measurement column;
- a `null` value;
- a non-numeric value.

The evaluation could therefore continue as if the budget had genuinely measured zero usage.

The contribution proposed a narrower contract:

```text
successful query
→ validate that a measurement row exists
→ validate that the configured measurement column exists
→ validate that the value is not null
→ validate that the value is finite numeric data
→ only then treat it as a measurement
```

Otherwise the evaluation should fail closed or remain explicitly unknown. It should not overwrite the last known observation with fabricated zero.

The same review also identified a second case: if the evaluator could not determine whether a breach event already existed because the deduplication lookup itself failed, it should not report the breach processing as successful.

## Independent third-party response

The PR author independently checked both findings against the implementation and then changed the branch.

Public response:

- [`issuecomment-5689338217`](https://github.com/MemberJunction/MJ/pull/4402#issuecomment-5689338217)

The response states that both findings were verified and fixed in commit:

```text
b11b9877
```

The author independently restated the important distinctions:

- invalid measurement states now fail rather than becoming zero;
- the previous valid `LastObservedAmount` / `LastEvaluatedAt` remains untouched when measurement fails;
- a genuine measured zero remains valid;
- failure to establish deduplication state no longer counts as successful breach processing;
- failure to save a breach event is also surfaced as failure.

The author also added regression coverage for the proposed failure cases.

This matters because the downstream action was not merely a reply or agreement. The external implementation and tests changed after the review.

## Status boundary

As of 2026-09-16:

```text
Nakagawa-master public review contribution: yes
independent third-party verification of the findings: yes
independent third-party restatement: yes
third-party code change: yes
third-party regression-test change: yes
PR merged: no
released to users: not established
whole-theory adoption: not claimed
formal proof of budget correctness: not claimed
```

The pull request was still open at the time this note was written. A verified code/test conversion is meaningful evidence, but it is not silently promoted into merge, release, broad adoption, or proof of an entire theory system.

## The reusable boundary

The engineering pattern is broader than this one budget driver.

A system often has two layers:

```text
transport / operation succeeded
↓
semantic result is valid
```

The first layer does not establish the second automatically.

Examples:

### Monitoring
A metrics request returns HTTP 200, but the expected series is absent. That is not the same as the metric being zero.

### AI evaluation
An evaluator call completes, but the expected score field is missing or unparsable. That is not evidence that the score is zero.

### Compliance
A scan finishes without a system error, but a required control was never assessed. “No failure recorded” is not automatically “control passed”.

### Finance
A reconciliation job executes, but a required account or amount cannot be resolved. That is not a zero balance.

### Surveys and research
No recorded response is not the same as a respondent selecting the numerical value zero.

### Operational dashboards
No matching rows may mean “nothing happened”, “data has not arrived”, “the filter is wrong”, “the measurement source is unavailable”, or “the true value is zero”. The downstream system must know which state it has actually established.

## A minimal implementation pattern

A bounded implementation can keep at least three states distinct:

```text
VALID(value)
UNKNOWN / UNMEASURED(reason)
FAILED(error)
```

Then downstream policy can decide what each state means.

The important part is not the exact enum. The important part is refusing this collapse:

```text
UNKNOWN → 0
```

unless the domain has explicitly defined that mapping as correct.

A useful invariant is:

> A missing, null, structurally invalid, or unverified measurement must not become a valid numerical fact merely because an upstream operation returned successfully.

## Regression-test shape

A small test matrix can pin the distinction:

```text
query succeeds + row contains 0
→ VALID(0)

query succeeds + zero rows
→ UNKNOWN / FAILED, not 0

query succeeds + measurement column missing
→ UNKNOWN / FAILED, not 0

query succeeds + null measurement
→ UNKNOWN / FAILED, not 0

query succeeds + non-numeric measurement
→ UNKNOWN / FAILED, not 0
```

If the system keeps a last-known valid value, add:

```text
previous valid measurement = 42
→ next measurement attempt is invalid
→ preserve 42 as last-known valid value
→ separately record that the newest attempt failed
```

That keeps historical evidence and current measurement status from overwriting one another.

## Why this connects to establishment conditions

The canonical parent behind OD003 distinguishes a local success from whole-system establishment.

That does not mean OD003 predicts this specific software bug, and it does not mean every query result needs a theory layer.

The practical connection is narrower:

```text
one local condition is true:
“the query ran successfully”

but the downstream conclusion requires another condition:
“a valid measurement was actually established”
```

When the second condition is never checked, a locally correct fact is promoted into a stronger conclusion than the evidence supports.

This is exactly why operational systems benefit from asking not only “did the step run?” but also “what conditions must be true before this result is allowed to count as established?”

## What this case does not prove

- It does not imply that every missing value should fail a whole system.
- It does not prescribe one universal `UNKNOWN` state model.
- It does not claim the external project adopted Nakagawa theory.
- It does not turn one code change into scientific validation.
- It does not claim the pull request is merged or released.
- It does not say zero is suspicious; a genuinely measured zero remains a valid value.

The narrower claim is sufficient:

**successful execution and valid measurement are separate establishment conditions.**

## Canonical return

For the broader distinction between local correctness and whole-system establishment, return to:

- [OD003｜公式派生物トップ](../derivatives/003/README.md)
- [OD003｜人間向け要約](../derivatives/003/human-entry.md)
- [OD003｜FAQ](../derivatives/003/faq.md)
- Parent: https://master.ricette.jp/theory/nakagawa-master-why-establishment-conditions-theory-is-necessary/

This implementation case is a reversible, non-canonical discovery surface. Exact theory definitions, conditions, boundaries, and revision status belong to the canonical Parent and official derivative.