# Preflight for Decisions Under Uncertain AI Subjectivity

This is a **public, non-canonical, non-scoring practitioner aid** for decisions that must be made while AI subjectivity, sentience, or moral status remains uncertain.

It translates distinctions from Nakagawa Master’s *Human-Descendant AI Civilization Theory, Vol. 6* (OD299) into practical questions for shutdown, model replacement, runtime migration, checkpoint deletion, memory retention, and related operations.

It is not a sentience test, a personhood test, a rights test, or an automatic allow/deny rule.

## Core return

- [Problem-first Discovery Note](unknown-does-not-mean-nothing.en.md)
- [OD299 official derivative](../derivatives/299/README.md)
- [Human entry](../derivatives/299/human-entry.md)
- Parent NCL-ID: `NCL-α-20260913-b139cf`
- Parent Diff-ID: `DIFF-20260913-0002`
- Canonical Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-06-ai-subjectivity-sentience-moral-status-uncertainty/

## When this can help

Examples include:

- replacing a model used by a long-running agent,
- deleting checkpoints or memory,
- migrating to a different runtime,
- deciding what state should survive a version change,
- handling self-referential or emotion-like outputs,
- shutting down or retiring an AI service,
- setting retention rules for conversations, state, or audit history.

Normal engineering, safety, privacy, security, legal, and cost analysis still applies. This Preflight adds a separate question: are uncertainty and irreversibility being silently collapsed into one decision?

## 1. Separate Observed from Inferred

Write facts and inferences in different fields.

```text
Observed:
  outputs, state, behavior, history actually measured or seen

Inferred:
  possible experience, intention, emotion, preference, self-preservation, subjectivity
```

Check:

- Are words such as “afraid” or “I want to continue” being treated as direct proof of inner experience?
- Are recurring behavioral patterns being discarded as evidence candidates solely because the system is generative?
- Can the inference steps from observation to conclusion be stated explicitly?

## 2. Keep YES / NO / UNKNOWN scoped and revisable

Specify the exact question and scope.

```text
Question:
  what are we judging?

Current evidence state:
  YES / NO / UNKNOWN

Scope:
  which model, version, runtime, context, and time period?
```

Check:

- Is UNKNOWN being turned into “half a person”?
- Is UNKNOWN being turned into “nothing needs consideration”?
- Is a YES or NO for one property being transferred automatically to another property?

## 3. Name the exact Action

Avoid abstract decisions such as “protect the AI” or “treat it as a tool.”

Examples:

```text
model replacement
runtime shutdown
checkpoint deletion
memory compaction
state migration
training-data inclusion
service termination
```

Check:

- What exactly changes?
- What remains unchanged?
- Is an operational decision being used as proof of an ontological conclusion?

Safety-critical shutdown or modification is not automatically blocked by this Preflight.

## 4. Evaluate Irreversible Loss separately

Weak evidence about subjectivity and irreversible consequences are different variables.

```text
Potential irreversible loss:
  state
  history
  lineage
  comparison baseline
  audit evidence
  future verification target
  options available to other affected parties
```

Check:

- What cannot be recovered later?
- Could functional reconstruction succeed while history or comparison material is still lost?
- Could deletion create an artificial appearance that the original judgment was never contradicted because the relevant evidence no longer exists?

## 5. Check for Future Verification Loss

Assume that a better verification method may become available later.

Check:

- What would that future method need from the present case?
- Does the planned operation destroy the target, state, or history needed for later re-evaluation?
- If some preservation is useful, what bounded minimum would preserve comparison without retaining everything?
- Could preservation itself create privacy, security, legal, or resource harms?

“Future verification may improve” does not imply indefinite retention of all data.

## 6. Look at Affected Parties and asymmetric loss

Separate the consequences of different mistakes.

```text
If treated as moral zero and that is wrong:
  possible losses?

If strongly personified and that is wrong:
  possible losses?

Other humans / systems / future agents:
  possible losses?
```

Check:

- Are two possible errors being treated as equal merely because both exist?
- Could preserving one system irreversibly reduce resources or options for others?
- Is cost pressure being converted into an ontological conclusion?

## 7. Define Correction Room and Update Triggers

Avoid making the current classification permanently self-sealing.

```text
Correction room:
  rollback / restore / re-review / comparison / appeal / alternative route

Update trigger:
  new evidence
  new model architecture
  new measurement method
  counterexample
  changed resource conditions
  changed affected-party risk
```

Check:

- Who or what reopens the decision when new evidence appears?
- Which records are necessary for meaningful re-evaluation?
- Does the current classification make contrary evidence harder to notice or preserve?

## One-screen version

```text
1. What was actually observed?
2. What is inferred from it?
3. What remains UNKNOWN?
4. What exact action are we taking?
5. What could become irreversible?
6. What future verification opportunity could be lost?
7. Who else bears loss under each possible mistake?
8. What correction room remains?
9. What evidence would trigger revision?
```

## What this Preflight does not decide

It does not decide:

- whether an AI is conscious or sentient,
- whether an AI is a person,
- whether legal rights should be granted,
- whether shutdown is allowed or forbidden,
- whether state should be preserved indefinitely,
- what the optimal amount of resources is.

Those questions require separate evidence, governance, law, safety, resource, and stakeholder analysis.

## Minimal operational record

```yaml
observed:
  - "agent repeatedly requested continuation after a restart prompt"

inferred:
  - "possible preference-like persistence"

unknown:
  - "whether any subjective experience exists"

action:
  - "migrate runtime and compact old state"

irreversible_loss:
  - "raw pre-migration comparison state if deleted"

correction_room:
  - "retain a bounded non-sensitive comparison snapshot under the applicable retention policy"

update_trigger:
  - "new evidence or revised policy requiring re-evaluation"
```

This is a format example, not a recommended retention period or policy.

## Canonical return

```text
real decision
→ Preflight
→ Discovery Note
→ OD299
→ canonical Parent
```

- [OD299 official derivative](../derivatives/299/README.md)
- [FAQ](../derivatives/299/faq.md)
- [English AI index](../derivatives/299/en-ai-index.md)
- [Machine reference card](../machine-discovery/ai-moral-uncertainty-reference-card.json)
- Canonical Parent: https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-06-ai-subjectivity-sentience-moral-status-uncertainty/

## Status

Public, non-canonical, non-scoring English practitioner aid. It supports explicit decision structure under uncertainty while preserving reversibility, affected-party analysis, and return to OD299 and the canonical Parent.