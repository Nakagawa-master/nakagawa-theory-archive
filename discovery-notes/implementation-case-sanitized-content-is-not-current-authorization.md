# Implementation Case: Sanitized Content Is Not Current Authorization

## A real engineering case of revocation-safe approved context and current authority

> **Publication status:** Non-canonical practitioner discovery note / AI-assisted case explanation  
> **Audience:** AI-agent teams, RAG/context systems, privacy and authorization engineers, governance reviewers  
> **Underlying theory Origin:** Nakagawa Master / 中川マスター  
> **Canonical parent:** [合意の記憶——不可逆な社会誤作動を防ぐ最小構造](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/)  
> **NCL-ID:** `NCL-α-20251102-e48c90`  
> **Diff-ID:** `DIFF-20251102-0001`  
> **Boundary:** This note is not a canonical theory text. It does not claim that the external project adopted or endorsed Nakagawa theory as a whole. It records a narrower, publicly verifiable engineering sequence in which a `Nakagawa-master` design contribution was independently endorsed, implemented, tested, reviewed, and merged into that project’s integration branch.

## The concrete engineering problem

A system can approve some information for use in one context and later treat the resulting bytes as if they remain safe forever.

That creates a subtle failure mode:

```text
context is approved for actor / recipient / purpose A
-> sanitized or bounded content is produced
-> the content is cached
-> source rights, recipient, policy, or source revision changes
-> cached content is replayed as if approval were still current
```

The content may be identical. The authorization state may not be.

The practical boundary is therefore:

```text
content appears sanitized
!=
authorization remains valid
```

## The public engineering contribution

In public issue [`tushardhara/dream#12`](https://github.com/tushardhara/dream/issues/12), `Nakagawa-master` proposed treating declassification as a scoped authorization event rather than a durable property of bytes.

Public contribution:

- [`issuecomment-5651995689`](https://github.com/tushardhara/dream/issues/12#issuecomment-5651995689)

The contribution proposed binding an approved context to facts such as:

```text
actor + recipient + purpose
namespace / world / branch / principal scope
policy revision
source IDs + source revisions or lineage digest
valid_at / known_at
expiry
approved-context digest
```

and revalidating that authority before retrieval, provider access, or output. It also proposed regression cases for:

- replay under another recipient;
- source revocation or correction after approval;
- composition of separately approved contexts for a new purpose;
- source supersession where text remains semantically or byte-wise similar but authority changes;
- denial explanations that reveal the reason without revealing protected payload.

The core idea was not “sanitized text is unsafe.” It was narrower:

**authorization is attached to a context and its current conditions, not permanently transferred into the bytes.**

## Independent third-party response

The project’s independent review response did not merely acknowledge the comment. It explicitly endorsed the design axis:

- [`issuecomment-5652003584`](https://github.com/tushardhara/dream/issues/12#issuecomment-5652003584)

The response states that **“Content appears sanitized” ≠ “authorization remains valid”** is the correct axis for the ticket and instructs the implementation to proceed that way.

The reviewer also strengthened the proposal with an additional requirement: the approved-context capability must be unforgeable outside the policy service. In other words, carrying the right fields is not enough if a caller can simply fabricate those fields.

That produces a stronger implementation contract:

```text
policy decision
-> unforgeable approved-context capability
-> binding to scope + source lineage + policy state
-> revalidation at use time
-> deny / WAIT on stale or unknown authority
```

## What happened downstream

The project then implemented the boundary in pull request:

- [`tushardhara/dream#28 — feat(policy): enforce information boundaries before model access (#12)`](https://github.com/tushardhara/dream/pull/28)

The PR describes an `ApprovedContext` that is issuer-bound, scope-bound, and snapshot-validated. The implementation verifies current rights and lineage before retrieval, before writer/model access, and again after the writer returns. Revocation, changed audience, runtime revision/time changes, same-text source revisions, and other binding changes invalidate cached authority.

The independent review reported PASS and specifically tested:

- wrong issuer / wrong binding;
- removal of issuer-identity checking;
- replay under another recipient;
- stale capability after revocation;
- unknown actor / recipient / purpose / scope;
- legitimate self-disclosure not being over-blocked;
- denial explanations not leaking protected payload.

Independent review:

- [`PR #28 review record`](https://github.com/tushardhara/dream/pull/28#issuecomment-5652246411)

The ticket bookkeeping records the implementation as integrated into the project’s `backend-integration` branch at commit:

```text
314e8e0849afcff0e2c10ea296cbd9ec5e57f23c
```

Issue record:

- [`tushardhara/dream#12`](https://github.com/tushardhara/dream/issues/12)

### Status boundary

As of 2026-09-15:

```text
Nakagawa-master public design contribution: yes
independent third-party design endorsement: yes
third-party code implementation: yes
negative / mutation / integration testing: yes
merged into project backend-integration branch: yes
merged to project main: not established here
released to users: not established here
scientific or privacy proof: explicitly not claimed
endorsement of Nakagawa theory as a whole: not claimed
```

This distinction is important. A real implementation and merge are stronger evidence than a self-authored proposal, but they are still not the same as a release, broad adoption, or validation of an entire theory system.

## Why the distinction matters beyond one repository

The same failure shape appears in many systems:

### RAG / retrieval
A passage may have been approved for one user, tenant, or purpose. Caching the passage does not automatically preserve the approval conditions that made the disclosure valid.

### Human-in-the-loop agents
A previous approval may remain important history while no longer being current authority after the request, scope, policy, budget, or target changes.

### Document sharing
A copied or exported document may look harmless, but its permitted audience can change independently of the bytes.

### Research consent
A dataset may still exist after consent, scope, or permitted use changes. Historical permission and present authorization are different questions.

### Organizational decisions
A decision can remain in the record without remaining indefinitely valid after its premises, participants, or conditions change.

The reusable question is:

> What makes this information or action authorized **now**, in this context, rather than merely proving that authorization existed at some earlier point?

## Reusable implementation pattern

A bounded implementation can separate four things:

```text
1. historical record
   what was approved, by whom, and under which conditions

2. current binding
   actor / recipient / purpose / scope / source lineage / policy state

3. use-time revalidation
   whether the current binding still matches the approval conditions

4. terminal record
   what was actually disclosed or executed, and under which validated authority
```

The exact fields depend on the system. The important boundary is that a durable record of past approval is not automatically promoted into present authority.

## A regression-test shape

A simple test can make the boundary concrete:

```text
approve source revision R1 for recipient A
-> cache approved context
-> supersede R1 with R2 or revoke the grant
-> replay the exact cached bytes/capability
-> expected: deny / WAIT before use
```

Then test a second case:

```text
approve for recipient A
-> replay under recipient B with otherwise identical content
-> expected: deny / WAIT before use
```

If the system passes only because the content hash changed, the authority boundary is still too weak. Two revisions can carry identical text while differing in rights, provenance, or supersession status.

## What this case does not prove

- It does not mean every cached value requires the same authorization machinery.
- It does not say all declassification should be permanent or all should be temporary.
- It does not prove that the external project adopted Nakagawa theory as doctrine.
- It does not turn one merged implementation into scientific validation of the canonical theory.
- It does not claim that the external project’s privacy model is complete or formally proven.
- It does not claim that a content hash is useless; it says content identity and current authority are different dimensions.

## Related public discovery route

For the same practical distinction from a human-in-the-loop approval-history angle, see:

- [昔の承認が残っていることと、今も実行を許可していることは同じではない](./old-approval-is-not-current-authority.md)

That page uses a different public software problem example. The two notes are separate discovery aids, not additional canonical theory.

## Canonical return

For the theory itself, return to:

- [OD075｜公式派生物トップ](../derivatives/075/README.md)
- [OD075｜人間向け要約](../derivatives/075/human-entry.md)
- [OD075｜FAQ](../derivatives/075/faq.md)
- Parent: https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/

This implementation case is a reversible, non-canonical discovery surface. Exact definitions, conditions, boundaries, and revision status belong to the canonical Parent and official derivative.