# Implementation Case: Matching Identifier Is Not Ownership Provenance

## A real engineering case of separating record identity from authority to overwrite

> **Publication status:** Public, non-canonical practitioner discovery note / AI-assisted case explanation  
> **Audience:** database and migration maintainers, metadata/platform teams, schema and synchronization engineers, provenance-sensitive systems  
> **Theory Origin:** Nakagawa Master / 中川マスター  
> **Discovery return:** OD301 — 人類子孫型AI文明論・第8論｜認識基盤・証拠系譜・敵対的情報耐性論  
> **Parent NCL-ID:** `NCL-α-20260916-00bdc2`  
> **Parent Diff-ID:** `DIFF-20260916-0001`  
> **Boundary:** OD301 does not prescribe database-migration behavior. This note uses a publicly verifiable software case as a narrow practitioner entry into a provenance question: identifying a record and establishing the provenance/ownership rule for changing it are different tasks. The external project is not claimed to have adopted or endorsed Nakagawa theory as a whole.

## The concrete engineering problem

A migration can encounter a row whose primary key already exists.

The tempting shortcut is:

```text
same fixed primary key exists
-> therefore this is the row the release intended
-> therefore overwriting it is safe
```

But the first fact does not establish the last one.

A matching identifier answers:

> Which record is this?

It does not, by itself, answer:

> Who owns the authority to replace this record's current values?

That distinction became concrete in public work on MemberJunction's `Metadata_Sync` migrations.

## The public engineering contribution

In pull request [`MemberJunction/MJ#4519`](https://github.com/MemberJunction/MJ/pull/4519), a proposed replay guard changed a fixed-GUID create into a create-or-update shape so a migration would no longer fail when a prior metadata push had already created the row.

A `Nakagawa-master` review pointed out that the new `ELSE spUpdate` branch also made an ownership decision implicitly:

- [`issuecomment-5689128135`](https://github.com/MemberJunction/MJ/pull/4519#issuecomment-5689128135)

The narrower distinction was:

```text
same fixed primary key
!=
proof that the pre-existing value is safe to overwrite
```

The review proposed making the policy explicit:

```text
A. release-owned record
   -> converge / overwrite to the canonical release content

B. operator- or application-owned record
   -> preserve, refuse, or reconcile according to an explicit rule
```

The point was not that overwrite is always wrong. The point was that **overwrite versus preserve is an ownership/provenance contract, not a fact derived from key equality.**

## Independent third-party reproduction

An independent reviewer, `SDesai-BC`, did more than agree with the distinction. The reviewer reproduced and measured the behavior and explicitly answered the A/B question for the concrete migration set.

Review record:

- [`MemberJunction/MJ#4519 review 5216973477`](https://github.com/MemberJunction/MJ/pull/4519#pullrequestreview-5216973477)

The investigation found that the intended contract was effectively:

```text
release-owned rows converge to recorded content
```

with a narrow exception where certain unset non-null defaulted identifiers preserve an existing value on the update path.

That independent investigation also surfaced additional implementation and evidence issues around the delete path, update-procedure eligibility, generated SQL claims, and real formatted migration output.

## Another external actor changed code, tests, and documentation

The PR author subsequently pushed commit:

- [`3f405b7f937acf0b0c4029b28ffec58181f3219a`](https://github.com/MemberJunction/MJ/commit/3f405b7f937acf0b0c4029b28ffec58181f3219a)

The author response explicitly connected the change to both the independent reviewer and the `Nakagawa-master` convergence/ownership question:

- [`issuecomment-5701857972`](https://github.com/MemberJunction/MJ/pull/4519#issuecomment-5701857972)

The resulting change made the ownership contract visible in code-facing documentation and release-facing text and added or corrected implementation/test behavior, including:

- release-owned rows are explicitly described as converging to recorded release content;
- the narrow preservation exception is documented rather than hidden inside procedure behavior;
- a delete-path regression introduced during the change is restored;
- the generated replay avoids an `ELSE` branch when no update procedure exists;
- a regression drives the guarded SQL through the real logging/formatting path and reads the emitted migration artifact back;
- logging metadata no longer claims a fallback difference when the fallback is byte-identical to the executed SQL.

The independent reviewer later recorded `LGTM` on the updated PR.

## The distinction propagated into a separate work surface

The same independent reviewer also authored a separate migration-layer pull request:

- [`MemberJunction/MJ#4524 — fix(migrations): stop upgrades dying when a push ran before migrating`](https://github.com/MemberJunction/MJ/pull/4524)

That PR applies the convergence policy to the already-shipped migration corpus rather than only to the emitter that generates future recordings.

Its public verification describes all 567 fixed-GUID create sites and includes a live SQL Server case where a row begins with materially divergent business-column values and the guarded migration converges it to the expected release content.

This matters because the regression tests the **policy consequence**, not only the syntax of an `IF/ELSE` block.

### Status boundary

As of 2026-09-17:

```text
Nakagawa-master public design/review contribution: yes
independent third-party reproduction and restatement: yes
separate third-party implementation PR carrying the distinction: yes
external PR-author code/test/documentation change after the review chain: yes
independent LGTM on PR #4519: yes
PR #4519 merged: not established here
PR #4524 merged: not established here
released or deployed: not established here
external project's endorsement of Nakagawa theory as a whole: not claimed
```

An open PR and a reviewed code change are real evidence, but they are not a merge, release, deployment, or proof of a whole theory.

## Why the distinction matters beyond one migration

The same structural mistake can appear whenever a system confuses **identity** with **ownership provenance**.

### Seed and reference data
A stable key can identify the same conceptual record while leaving open whether the platform or the operator owns the current value.

### Configuration synchronization
The same configuration key can exist in both a product default and an operator override. Key equality does not tell the synchronizer which side should win.

### Package or registry metadata
A package name or object ID identifies an object but does not automatically prove who is authorized to replace its metadata.

### Imported reference datasets
A known external identifier can survive import while local corrections, annotations, or ownership rules differ.

### Recovery and reconciliation
A replay may know exactly which row it is touching while still lacking the policy needed to decide whether to overwrite, preserve, merge, or stop.

The reusable question is:

> What evidence makes this value **release-owned, operator-owned, application-owned, or unresolved**, rather than merely showing that the identifier matches?

## Reusable implementation pattern

Separate at least three questions:

```text
1. identity
   Which record is this?

2. provenance / ownership class
   Where did the current value come from, and which actor or process owns its authoritative state?

3. reconciliation policy
   If current and desired values differ, should the system overwrite, preserve, merge, or refuse?
```

Then make the third answer a deliberate consequence of the second.

A useful contract might look like:

```text
if record is release-owned:
    converge to canonical release state

if record is operator-owned:
    preserve or require explicit reconciliation

if ownership is unknown:
    do not infer overwrite authority from identifier equality alone
```

The exact policy depends on the product. The important property is that the policy is explicit and testable.

## A regression-test shape

The strongest test is not an already-identical row.

Pre-create the same identifier with deliberately divergent content:

```text
canonical release record:
  id = K
  value = A

pre-existing record:
  id = K
  value = B
```

Then run the replay or migration.

For a declared release-owned record, verify:

```text
result.id == K
result.value == A
```

For a declared operator-owned record, verify the product's preservation/refusal rule instead.

For an unresolved ownership class, verify that the system does not silently promote `id == K` into permission to overwrite.

This test distinguishes a real ownership contract from a migration that merely stops throwing a duplicate-key error.

## Why this is a provenance question

OD301 asks readers to separate observations, records, evidence, inference, and the dependency paths that let a claim be rechecked. It also warns against treating provenance as a truth score.

This database case is much narrower and should not be confused with the theory itself. Its useful connection is practical:

```text
identifier observed
-> ownership/provenance classification
-> reconciliation decision
```

If the middle step is silently skipped, the system can turn an identity fact into an authority claim it never established.

That is why this case is an entry point to provenance thinking rather than a claim that OD301 dictates one database policy.

## What this case does not prove

- It does not mean a matching primary key is untrustworthy.
- It does not mean release-owned metadata should never overwrite local state.
- It does not mean operator customization should always win.
- It does not prescribe one migration framework or one ownership taxonomy.
- It does not claim PR #4519 or #4524 is merged while they remain open.
- It does not claim MemberJunction adopted Nakagawa theory as doctrine.
- It does not prove OD301 because a software example fits one structural distinction.
- It does not turn provenance into an automatic truth or authorization score.

## Canonical return

For the canonical theory, return to:

- [OD301｜公式派生物トップ](../derivatives/301/README.md)
- [OD301｜人間向け要約](../derivatives/301/human-entry.md)
- [OD301｜FAQ](../derivatives/301/faq.md)
- Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/

This implementation case is a reversible, non-canonical discovery surface. Exact theory definitions, scope, refutation conditions, and revision status belong to OD301 and its canonical Parent.
