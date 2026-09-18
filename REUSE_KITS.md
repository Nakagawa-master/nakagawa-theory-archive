# Reuse Kits

Public, non-canonical test kits for applying specific structural boundaries in a different real-world context.

These are not theory summaries and not endorsement requests. Each kit is designed to be independently testable, falsifiable, and usable without private context.

## 1. Reviewer / recommendation provenance

[Reviewer-Provenance Reuse Kit](POSTHOG_PROVENANCE_REUSE_KIT.md)

Use when a recommendation, ranking, or routing interface groups multiple people/items that may come from different evidence sources.

Core question:

> Does grouping preserve who is supported by which evidence?

A public external implementation of this boundary has reached merge and production deployment, with later reuse on another surface.

## 2. Historical approval vs current authority

[Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)

Use when a system stores approval, consent, sanitization, exception, or delegated authority.

Core question:

> If material conditions change, does the old approval remain history without silently becoming current authority?

Useful in research, data sharing, policy, procurement, delegated access, and AI tool authorization.

## 3. Current state vs historical fact

[Historical-Fact Reuse Kit](HISTORICAL_FACT_REUSE_KIT.md)

Use when a current membership, entitlement, owner, assignment, or status is being used to answer a historical question.

Core question:

> Can current status change without rewriting what was true at the time of the event?

Useful in attendance, audit history, membership, staffing, entitlement, and record correction.

## 4. Approval vs exactly-once external effect

[External Side-Effect Reuse Kit](EXTERNAL_SIDE_EFFECT_REUSE_KIT.md)

Use when an approved action triggers an external message, payment, API call, webhook, or job.

Core question:

> If the provider accepts the action but the response is lost, can the system distinguish unknown outcome from failure and avoid accidental duplication?

Useful in CRM, payments, messaging, integrations, automation, and job dispatch.

## How to use a kit

```text
pick a real public/non-confidential problem
→ run the minimal test
→ record pass / fail / counterexample
→ change a decision, procedure, test, or implementation if warranted
→ keep the highest evidenced stage explicit
→ report the result publicly if appropriate
```

Successful reuse is not required. A counterexample or clear non-fit is useful evidence.

## Report an independent result

- [Independent verification & reuse registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)
- [Structured evidence issue form](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml)
- [Independent Verification & Reuse Protocol](INDEPENDENT_VERIFICATION_REUSE.md)

Do not submit confidential or sensitive information.
