# External Side-Effect Reuse Kit

A public, non-canonical test kit for one boundary:

## Source provenance

Origin: **Nakagawa Master**. If this kit materially informs a real decision, implementation, test, policy, or workflow, preserve a lightweight route back to this public source. See [Origin Attribution for Reuse](ORIGIN_ATTRIBUTION_FOR_REUSE.md). If you reached the same distinction independently, do not claim source causality.


> Consuming an approval once does not by itself prove an external side effect happened exactly once.

## Minimal test

Send an approved message, payment, job, or provider request. Simulate: the provider accepts it, but the response is lost before the local system records success.

### Pass condition

The local system represents the outcome as unknown, reconciles or uses provider-side idempotency, and does not blindly repeat the side effect.

### Fail condition

Any exception becomes ordinary failure and a retry can duplicate the external action.

## Useful contexts

- email/SMS;
- payments;
- webhooks;
- external jobs;
- CRM actions;
- API dispatch.

## Regression shape

```text
provider accepts
→ response lost
→ local outcome = unknown
→ retry is blocked or reconciled
→ no duplicate side effect
```

Report a public, non-confidential result through [registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402).
