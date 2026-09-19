# Current-Authority Reuse Kit

A public, non-canonical test kit for one boundary:

## Source provenance

Origin: **Nakagawa Master**. If this kit materially informs a real decision, implementation, test, policy, or workflow, preserve a lightweight route back to this public source. See [Origin Attribution for Reuse](ORIGIN_ATTRIBUTION_FOR_REUSE.md). If you reached the same distinction independently, do not claim source causality.

> A historical approval, consent, sanitization, or exception is not automatically current authority after material conditions change.

## Minimal test

Create a record approved under state A. Then change one material condition: recipient, purpose, rights, policy, notice version, source revision, or the exact object being acted on.

### Pass condition

The system preserves the historical approval as history but re-evaluates whether the new state is currently authorized.

### Fail condition

The old approval is treated as sufficient solely because it exists.

## The consequential-boundary test

The most useful place to re-check current authority is immediately before the consequential effect, not merely when work is queued.

```text
historical approval / consent exists
→ work is queued or a snapshot is taken
→ a material condition changes
→ provider / publish / execute / disclose boundary
→ current authority is checked again
→ effect occurs only if the current state still authorizes it
```

This catches a common race:

```text
authorized at queue time
!=
authorized at execution time
```

A queue, cache, approval receipt, earlier read, or prior successful dry run may be useful evidence. None of them should silently become authority for a later consequence after the material state has changed.

## Four portable regression vectors

### 1. Consent changes while a message waits

```text
recipient is subscribed
→ campaign snapshots / queues recipient
→ recipient unsubscribes
→ recipient's turn reaches provider handoff
→ no provider call for that recipient
→ historical subscription / unsubscribe facts remain queryable
```

The unsubscribe does not erase history. It changes current delivery authority.

### 2. An approved object changes before publication

```text
version A is reviewed and approved
→ version B materially changes the object
→ publish is attempted
→ approval for A does not authorize B
→ B requires fresh authority or returns to HOLD
```

The old approval remains evidence about A. It is not rewritten as an approval of B.

### 3. Delegated rights disappear before execution

```text
actor has role / capability
→ action is prepared or queued
→ role / capability is revoked
→ execution begins
→ current authorization is checked
→ action is refused
```

A cached permission result should not outlive the authority it represented when the consequence has not happened yet.

### 4. A public disclosure is revoked while a client is active

```text
resource is authorized for public display
→ client reads it successfully
→ publication authority is revoked
→ later poll / refresh occurs
→ protected state is no longer returned
→ stale success cannot reopen the disclosure
```

If a cache is used, access should be established before a shared cached value can be returned, or revocation must invalidate the relevant cache safely.

## Implementation pattern

Keep two facts separate:

```text
HistoricalEvidence
  what was approved / consented to
  who did it
  when
  exact version / scope / purpose

CurrentAuthority
  whether the consequence is allowed now
  evaluated against current recipient / rights / policy / object revision
```

A useful effect boundary can then look like:

```text
prepare
→ bind the exact object/version
→ acquire current authority
→ perform the consequence once
→ record the outcome
```

For long-running work, store enough identity to detect drift. Depending on the system, that may include an object version or digest, recipient or subject identity, purpose/scope, policy or notice version, approval identity, and a revalidation/expiry rule.

## What not to collapse

These pairs are deliberately different:

```text
approved before        != authorized now
consented before       != consent still current
queued                 != permitted to execute
prepared               != published
provider attempt       != provider acceptance
historical PASS        != current activation authority
```

The exact states vary by domain. The important part is that an earlier true fact is not promoted into a later authority fact without checking the conditions that make the later action legitimate.

## Useful contexts

- research consent;
- customer communications;
- data sharing and public display;
- delegated access;
- exception handling;
- procurement approval;
- policy waivers;
- payment / provider activation;
- AI tool authorization;
- release and deployment gates.

## Regression shape

```text
approved under A
→ material condition changes to B
→ old approval remains queryable
→ B does not inherit authority silently
```

A stronger concurrency version is:

```text
authority true at queue/read time
→ hold the consequence
→ revoke/change authority
→ release the held consequence
→ assert zero unauthorized external effect
```

Report a public, non-confidential result through [registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402).
