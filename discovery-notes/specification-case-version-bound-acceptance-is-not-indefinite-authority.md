# Specification Case: Version-Bound Acceptance Is Not Indefinite Authority

## A public case where an external maintainer turned a review boundary into a new specification issue

> **Publication status:** Non-canonical practitioner discovery note / AI-assisted case explanation  
> **Audience:** AI platform teams, authorization and consent designers, product/specification reviewers, governance engineers  
> **Underlying theory Origin:** Nakagawa Master / 中川マスター  
> **Canonical return:** OD075 / 「合意の記憶——不可逆な社会誤作動を防ぐ最小構造」  
> **Boundary:** This note does not claim that the external project adopted or endorsed Nakagawa theory as a whole. It records a narrower, publicly verifiable sequence in which a `Nakagawa-master` review distinction was independently acknowledged, restated, and turned into a new specification issue by the project maintainer.

## The concrete problem

A system may record that someone accepted a notice, policy, model condition, or other terms.

That record can remain historically true even after the thing being accepted changes.

The failure begins when the system silently converts:

```text
an acceptance existed in the past
```

into:

```text
the current version is authorized now
```

without preserving what version or policy identity was actually accepted.

The practical distinction is:

```text
approver + timestamp
!=
what was accepted

historical acceptance exists
!=
current requirement is satisfied
```

## The public external sequence

The sequence occurred in the public `ncsa/lumen` repository.

### 1. The project design was discussing project-level model acceptance

Issue:

- `ncsa/lumen#64` — Project keys: creator attribution, project-level model acceptance, and per-user allowances
- https://github.com/ncsa/lumen/issues/64

The design intentionally kept model acceptance at project scope: one authorized manager could approve a model for the project rather than requiring each key creator to accept separately.

That reduced one kind of operational complexity, but it made the identity of the accepted notice more important: one historical project acceptance could otherwise be interpreted as authority for later notice text.

### 2. `Nakagawa-master` supplied a narrower review boundary

Public contribution:

- https://github.com/ncsa/lumen/issues/64#issuecomment-5682799671

The contribution argued that approver attribution and a timestamp still do not record **what** the project approved if the notice changes later.

It proposed binding acceptance to an immutable notice or policy identity, for example:

```text
project / scope
+ model / acceptance subject
+ notice version or digest
+ accepted by
+ accepted at
```

and making the runtime question:

```text
does this scope have an acceptance
for the currently required notice version?
```

rather than merely:

```text
does a consent row exist?
```

The review also proposed lifecycle distinctions:

- a material notice change requires a new acceptance;
- prior acceptance evidence remains historical rather than being overwritten;
- non-material wording changes need an explicit compatibility rule;
- independently evolving acknowledgements such as early-access conditions need independent version identity;
- legacy unversioned consent must be handled deliberately rather than silently described as acceptance of current text.

## Independent third-party response

The repository maintainer, `robkooper`, responded publicly:

- https://github.com/ncsa/lumen/issues/64#issuecomment-5683288690

The response did more than acknowledge the comment. It independently restated the problem: each acceptance, whether user- or project-level, should carry a marker identifying exactly what was accepted, and changed text should require a new approval.

The maintainer also stated that a new issue would be created for this case.

## Independent third-party specification action

The maintainer then created:

- `ncsa/lumen#65` — **Acceptance records must be version-bound, at every scope**
- https://github.com/ncsa/lumen/issues/65

The new issue carries the distinction into a project-owned specification object. It defines versioning as a property of acceptance itself across user, project, organization, and early-access scopes.

Its proposed shape includes:

```text
Acceptance
  subject
  scope + scope_id
  notice_version / notice_digest
  accepted_by_entity_id
  accepted_at
```

and explicitly separates:

- material-change re-acceptance;
- immutable historical evidence;
- non-material compatibility rules;
- independently versioned early-access acknowledgement;
- legacy-unversioned migration semantics.

This is important because the downstream action was not authored by `Nakagawa-master`: the maintainer created the new issue and expressed the boundary in the project’s own specification language.

## A follow-up implementation consequence

After the maintainer-created issue existed, `Nakagawa-master` added a narrower implementation observation:

- https://github.com/ncsa/lumen/issues/65#issuecomment-5683852642

The observation notes that a single row unique on `(entity_id, model_config_id)` cannot both preserve immutable historical acceptance events and represent a moving current requirement if re-acceptance merely overwrites the row.

One conceptual separation is:

```text
AcceptanceEvent
  = immutable evidence of what was accepted

CurrentRequirement
  = the version / digest that must be satisfied now
```

Then authorization becomes a set-membership question:

```text
current authority exists
iff
an acceptance event matches the currently required identity
```

This follow-up is still a proposal. It is not evidence that the external project implemented that particular data model.

## Status boundary

As of 2026-09-16:

```text
Nakagawa-master review contribution: yes
independent maintainer acknowledgement: yes
independent maintainer restatement: yes
maintainer-created specification issue carrying the boundary: yes
third-party implementation of issue #65: not established here
merged code for issue #65: not established here
released behavior: not established here
endorsement of Nakagawa theory as a whole: not claimed
scientific or legal validation of the theory: not claimed
```

The distinction matters. A maintainer turning an external review boundary into a new project specification issue is stronger evidence than a self-authored proposal or a reaction count. It is still not the same as implementation, merge, release, broad adoption, or validation of an entire theory system.

## Why this pattern matters beyond one project

The same structural error appears in several domains.

### AI model notices and policy acknowledgements
A user or organization may have accepted version 1. Version 2 can remain unaccepted even when the old acceptance record is preserved perfectly.

### Human-in-the-loop agent approvals
An old approval can remain useful audit history without remaining executable authority after arguments, target, budget, scope, policy, or run identity changes.

### Terms and organizational policy
A historical sign-off can prove what was agreed at that time without granting indefinite consent to materially different future text.

### Data and research consent
A dataset may still exist after the permitted purpose, population, scope, or notice changes. Historical consent and current permitted use are different questions.

### Operational change approvals
A deployment or migration approved for one revision should not automatically authorize a later revision simply because the same approval row still exists.

## Reusable implementation pattern

A bounded design can separate four layers:

```text
1. requirement identity
   what exact notice / policy / action version currently requires acceptance

2. immutable acceptance event
   who accepted which identity, for which scope, and when

3. current authorization check
   whether current scope has evidence matching the current requirement

4. history and correction
   older acceptances remain attributable without being silently promoted to current authority
```

The exact database shape can vary. The reusable boundary is the separation between evidence of a past decision and authority under current conditions.

## Regression-test shape

A minimal lifecycle test is:

```text
required notice = v1
-> scope accepts v1
-> access works
-> required notice becomes material v2
-> v1 acceptance remains queryable
-> access requiring v2 does not treat v1 as sufficient
-> authorized actor accepts v2
-> access resumes
-> both acceptance events remain attributable
```

Then vary the source of the requirement:

```text
global default changes
vs
one model-specific override changes
vs
early-access notice changes independently
```

Only the acceptance identity whose effective requirement changed should be invalidated.

## What this case does not prove

- It does not imply that every wording edit must force re-acceptance.
- It does not prescribe one universal digest or schema design.
- It does not say historical acceptance is invalid or should be deleted.
- It does not establish that `ncsa/lumen` implemented issue #65.
- It does not claim that `ncsa/lumen` adopted Nakagawa theory as doctrine.
- It does not turn one specification conversion into proof of the full canonical theory.
- Origin and provenance show where a contribution came from; they do not make the contribution true by authority alone.

## Related public route

For the broader distinction between historical approval and current executable authority:

- [昔の承認が残っていることと、今も実行を許可していることは同じではない](old-approval-is-not-current-authority.md)

For a separate case that progressed through third-party implementation, testing, review, and integration:

- [Implementation Case: Sanitized Content Is Not Current Authorization](implementation-case-sanitized-content-is-not-current-authorization.md)

## Canonical return

For the theory itself, return to:

- [OD075｜公式派生物トップ](../derivatives/075/README.md)
- [OD075｜人間向け要約](../derivatives/075/human-entry.md)
- [OD075｜FAQ](../derivatives/075/faq.md)
- Parent NCL-ID: `NCL-α-20251102-e48c90`
- Parent Diff-ID: `DIFF-20251102-0001`
- Parent: https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/

This page is a public, non-canonical, AI-assisted case explanation. The external project’s issue and maintainer statements remain authoritative for what happened in that project; the canonical Parent remains authoritative for the theory itself.
