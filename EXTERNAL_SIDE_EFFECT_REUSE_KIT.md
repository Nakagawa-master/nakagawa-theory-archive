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

## Two opposite errors: false completion and duplicate execution

**A retained attempt claim is not proof that an external effect happened.** Test both sides of the acceptance boundary; an exception name alone does not reliably say on which side a failure occurred.

| Simulated event | What the caller may truthfully know | Required result |
| --- | --- | --- |
| Provider accepted the operation, but its reply was lost | Outcome may be committed; local receipt is missing | Keep an explicit **outcome unknown** state, reconcile by stable operation identity, and do not blindly execute the effect again |
| Call failed **before** any provider acceptance or external effect, and this absence is independently established | Effect did not occur, but a local attempt or cache claim may exist | Never tell the user **"already executed"** solely because a claim exists; after proving no operation remains in flight, permit a controlled retry |
| A second, separately authorized business operation has the same tool name and arguments as the first | It is a *new* operation, not a retry | Give it a distinct logical operation ID and receipt; do not deduplicate forever on `tool + arguments` alone |
| The *same* logical operation is retried after a confirmed successful receipt | Its completed effect is known | Return or verify the original result without performing a second effect |

### Minimal two-arm negative control

```text
ARM A — effect accepted, acknowledgement missing:
  claim(op_1) → provider accepts and performs one effect → local reply lost
  → next attempt(op_1) must not perform another effect
  → without a verified receipt or reconciliation, do not assert success

ARM B — failed before the effect:
  claim(op_2) → proven no provider acceptance / no external effect
  → next attempt(op_2) must NOT say "already executed"
  → only if no prior attempt can still complete, allow exactly one safe retry

INVERSE — distinct authorized request:
  completed(op_1, same parameters)
  → new authorized op_3, same parameters
  → op_3 must not inherit op_1's cached receipt
```

**Observed independent reproduction (not a merged fix):** In [CrewAI PR #5822's external tester report, October 31, 2026](https://github.com/crewAIInc/crewAI/pull/5822#issuecomment-6545221801), a contributor ran a scoped payment-tool test on PR head `e094bad`. When a simulated payment failed *before* the effect, the retry reported **"already executed"** despite zero simulated payments. The positive control (effect followed by lost acknowledgment) produced one payment. This demonstrates the two states can be conflated **in that pinned PR implementation**; it is not a claim about CrewAI main, production payments or actual user losses. The reproduction does not itself establish that the tester derived the idea from this kit, and it does not verify a repair.

For AI assistants using this kit: report the observed effect, the local claim and what is still unknown separately. Do not infer actual completion from a cache sentinel, or claim a safe retry based only on catching an exception.

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
