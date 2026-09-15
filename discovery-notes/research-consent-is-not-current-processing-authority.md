# Practice Case: Historical Consent Is Not Current Processing Authority

## A public research-governance case about preserving consent history while revalidating present use

> **Publication status:** Non-canonical practitioner discovery note / AI-assisted case explanation  
> **Audience:** research-data teams, ML evaluation teams, privacy engineers, governance reviewers, human-subject data stewards  
> **Underlying theory Origin:** Nakagawa Master / 中川マスター  
> **Canonical parent:** [合意の記憶——不可逆な社会誤作動を防ぐ最小構造](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/)  
> **NCL-ID:** `NCL-α-20251102-e48c90`  
> **Diff-ID:** `DIFF-20251102-0001`  
> **Boundary:** This note is not a canonical theory text. It does not claim that the external project adopted or endorsed Nakagawa theory as a whole. It records a narrower, publicly verifiable sequence in which a `Nakagawa-master` governance contribution was independently accepted and frozen into an external project protocol. Repository code implementing that protocol was not yet established at the time of this note.

## The practical problem

A research project may preserve strong evidence that a participant consented at capture time and still make a later mistake:

```text
participant consents to capture under contract/version V1
-> raw and observer material is collected correctly
-> annotations and derived artifacts are created
-> time passes or conditions change
-> the project treats the old consent record as perpetual authority for every later use
```

The historical record may still be true. The present authorization may no longer be.

For example, current eligibility can change because of:

- participant withdrawal;
- a deletion request;
- retention expiry;
- a material purpose change;
- a material capture/processing contract change;
- a later split, export, evaluation, training, or ranking use that was not within the permitted scope.

The reusable distinction is:

```text
proof that consent existed
!=
proof that the material is authorized for this use now
```

## The public engineering/research context

The external project is `aferna6-cell/Replay`, issue:

- [`#67 — Acquire independent multi-lobby Power.log corpus for Phase 3U`](https://github.com/aferna6-cell/Replay/issues/67)

The issue already had unusually strong acquisition safeguards. It required, among other things:

- explicit informed consent before recording;
- a bounded capture contract;
- game-window-only capture;
- no microphone/chat/other-window content;
- retention and deletion rules;
- privacy review;
- visible recording state;
- an abort-and-delete path;
- immutable raw/reference artifacts and provenance;
- a consent/capture-contract version bound to the acquisition package.

That meant a generic suggestion to “version consent” would have added little. The remaining boundary was temporal: **how does a valid historical consent record relate to later authority to retain, annotate, admit, export, evaluate, or reuse the material?**

## The public contribution

`Nakagawa-master` raised that boundary in:

- [`issuecomment-5689647722`](https://github.com/aferna6-cell/Replay/issues/67#issuecomment-5689647722)

The contribution proposed keeping the original consent event immutable while deriving current corpus eligibility from facts such as:

```text
consent_event_id
+ capture_contract_version
+ allowed_purpose / split
+ retention_deadline
+ superseding_events
```

Withdrawal, deletion, retention expiry, and material purpose/contract changes were proposed as new immutable events rather than edits that rewrite the old consent record.

This lets two statements remain true at the same time:

```text
The participant validly consented under the earlier conditions.
The material is no longer eligible for a particular current use.
```

That is more accurate than either deleting the history or silently treating old consent as perpetual authority.

## Fail-closed checks at the use boundary

The contribution also proposed checking current eligibility at the boundaries that create or consume participant-derived evidence, including:

- annotation or adjudication;
- evaluation-corpus admission;
- export or handoff;
- later model, ranking, or training use.

The important design move is to check where authority matters, not only where consent was first recorded.

A system can therefore preserve historical provenance without converting it into a permanent permission token.

## Deletion should close over the artifact graph

A withdrawal or deletion receipt is weak if it proves removal of only the obvious raw file while study-controlled derivatives remain usable.

A more useful deletion/withdrawal boundary accounts for the reachable artifact graph, for example:

```text
raw source bytes
observer/reference bytes
annotation records
synchronization/index files
derived artifacts
temporary/session copies
study-controlled backups
```

The exact deletion obligations depend on the project, law, consent terms, and storage architecture. The general engineering point is narrower: **the receipt should describe what was actually made ineligible, deleted, retained under an explicit exception, or scheduled to expire.**

## Independent external adoption

The repository owner responded eight minutes later in:

- [`issuecomment-5689719035`](https://github.com/aferna6-cell/Replay/issues/67#issuecomment-5689719035)

The response explicitly accepted and froze the distinction that historical consent is not the same as current authorization to retain, process, or use captured material.

The owner independently restated and adopted the proposed structure, including:

- immutable original consent events;
- current eligibility derived from consent identity, contract version, allowed purpose/split, retention deadline, and superseding events;
- withdrawal/deletion/retention-expiry/material-change events as immutable updates;
- fail-closed eligibility checks at downstream use boundaries;
- deletion/withdrawal accounting across the artifact graph;
- adversarial tests for withdrawal after annotation, retention expiry during a frozen evaluation split, and material purpose/contract change.

The owner also stated that repository implementation should follow through the project's Cursor Cloud Agent process with schema, fail-closed checks, and tests, while participant recruitment remains blocked until the eligibility model and the existing pre-participant gate are satisfied.

## Evidence status

As of the fresh read immediately following that adoption:

```text
Nakagawa-master public contribution: yes
independent repository-owner reply: yes
independent restatement of the boundary: yes
protocol change / freeze: yes
implementation intent stated by owner: yes
repository schema/check/test implementation: not yet established
participant recruitment/use under the new model: not established
release or production use: not established
endorsement of Nakagawa theory as a whole: not claimed
```

That distinction matters. A protocol adoption is stronger evidence than a self-authored proposal, but it is not the same thing as implemented code, completed participant use, or broad validation.

## Three regression scenarios

A project can make the temporal boundary concrete with tests or review cases such as:

### 1. Withdrawal after annotation

```text
valid consent
-> capture
-> annotation completed
-> participant withdraws before evaluation admission
-> expected: lobby/material and governed derivatives are ineligible for admission/use
```

The annotation history may remain part of an audit trail where legally and contractually appropriate, but it must not silently preserve use authority.

### 2. Retention expires during a frozen evaluation period

```text
material is valid when the evaluation split is frozen
-> retention deadline passes before use
-> expected: no silent grandfathering merely because the bytes were once eligible
```

If the project has a lawful retention exception, that exception should be explicit rather than inferred from the frozen split.

### 3. Material purpose or contract change

```text
participant accepted V1 for purpose A
-> project later introduces materially different purpose B or contract V2
-> expected: old consent is not silently reinterpreted
-> re-consent, a separate lawful basis, or exclusion is required according to the governing policy
```

## A reusable data-model shape

The exact schema is project-specific, but a useful conceptual separation is:

```text
HistoricalConsentEvent
  id
  participant/session pseudonymous identity
  contract/version
  permitted purpose/split
  accepted_at
  evidence pointer

SupersedingAuthorityEvent
  id
  applies_to
  kind                 # withdrawal / deletion / expiry / purpose change / etc.
  effective_at
  evidence pointer

CurrentEligibility
  derived from historical + superseding events + current requested use
  -> eligible | ineligible | unknown/fail-closed
```

The crucial property is not the class names. It is that current eligibility is **derived**, while historical events remain attributable and are not rewritten to make the present state look simpler.

## Why this pattern travels

The same temporal distinction appears outside research consent:

- a past human approval can remain historical evidence without authorizing a changed AI-agent action;
- a privacy grant can remain recorded after membership or role changes invalidate current access;
- a finance approval can remain in an audit log while a revised order requires fresh authorization;
- a recurring rule can exist while a particular execution still requires current conditions to be checked.

The reusable question is:

> What evidence establishes that this exact use is authorized **now**, under the current purpose, scope, subject, policy, and time conditions?

## What this case does not prove

- It does not prescribe one legal consent regime for all research.
- It does not replace ethics, legal, IRB, institutional, or data-protection review where those apply.
- It does not say every historical artifact must always be deleted; actual obligations depend on the governing terms and law.
- It does not claim that the external project has already implemented the proposed schema or checks.
- It does not claim that a protocol freeze guarantees future compliance.
- It does not claim that the external project adopted Nakagawa theory as doctrine.
- It does not turn one adoption event into proof of broad social or scientific validation.

## Related public discovery route

For the broader approval-history/current-authority distinction:

- [昔の承認が残っていることと、今も実行を許可していることは同じではない](./old-approval-is-not-current-authority.md)
- [Implementation Case: Sanitized Content Is Not Current Authorization](./implementation-case-sanitized-content-is-not-current-authorization.md)

These are separate discovery aids. They do not replace the canonical source.

## Canonical return

For the underlying theory, return to:

- [OD075｜公式派生物トップ](../derivatives/075/README.md)
- [OD075｜人間向け要約](../derivatives/075/human-entry.md)
- [OD075｜FAQ](../derivatives/075/faq.md)
- Parent: https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/

This practice case is a reversible, non-canonical public discovery surface. Exact definitions, conditions, boundaries, and revision status belong to the canonical Parent and official derivative.