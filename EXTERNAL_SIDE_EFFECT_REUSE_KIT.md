# External Side-Effect Reuse Kit

A public, non-canonical test kit for one boundary:

## Source provenance

Origin: **Nakagawa Master**. If this kit materially informs a real decision, implementation, test, policy, or workflow, preserve a lightweight route back to this public source. See [Origin Attribution for Reuse](ORIGIN_ATTRIBUTION_FOR_REUSE.md). If you reached the same distinction independently, do not claim source causality.


> Consuming an approval once does not by itself prove an external side effect happened exactly once.

## Reader-facing Japanese example

- [「エラーだから再送」は、二重送信や二重決済を生むことがある](https://nakagawamaster.wordpress.com/2026/09/24/local-error-is-not-external-failure/)
- [Japanese reader-entry series](WORDPRESS_READER_SERIES.md)

The article is an explanatory carrier, not a substitute for this kit and not independent adoption evidence.

## Minimal test

Send an approved message, payment, job, or provider request. Simulate: the provider accepts it, but the response is lost before the local system records success.

### Pass condition

The local system represents the outcome as unknown, reconciles or uses provider-side idempotency, and does not blindly repeat the side effect.

### Fail condition

Any exception becomes ordinary failure and a retry can duplicate the external action.


## Idempotency-horizon regression

Provider idempotency can be correct and still be too short for the application's retry policy.

Test this separately when both horizons exist:

```text
provider accepts
→ local success stamp is lost
→ provider idempotency TTL expires
→ application retry window is still open
→ retry worker wakes
→ no second side effect without reconciliation
```

### Pass condition

An ambiguous accepted-at-provider outcome remains durable until it is reconciled, or the application otherwise proves that a retry is still protected. The system must not assume that reusing the same idempotency key is sufficient after the provider's guaranteed dedupe horizon has expired.

### Useful assertion

Inject failure after provider acceptance but before the local success stamp, advance time beyond the provider's idempotency TTL while remaining inside the application's retry window, then run the retry worker and assert zero second external side effects.

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
