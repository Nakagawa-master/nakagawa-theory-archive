# An Old Approval Record Is Not the Same as Current Execution Authority

This page is a **public, non-canonical, AI-assisted Discovery Note** that approaches Nakagawa Master’s *Memory of Agreement — Minimal Structure for Preventing Irreversible Social Malfunction* (OD075) from a concrete AI / agent-system implementation problem.

It does not claim that a software issue proves the theory, and it does not claim that the external project has adopted or endorsed Nakagawa Master’s work.

The practical question is:

**How can a system preserve the fact that an approval happened without accidentally treating that historical record as permission that is still live now?**

## Keep the history; do not silently reactivate it

Suppose a human approves one tool execution.

The tool runs and produces a result.

There is real value in preserving the history:

```text
what was approved
who approved it
which request or call it referred to
whether it executed
what result followed
```

But if an old `approved` record remains in message history, that alone should not make it a pending authorization again on a later continuation.

```text
historical record exists
!=
current authority is active
```

History and current authority may refer to the same event, but they have different roles.

## A concrete engineering problem

PydanticAI public issue #5154 discusses a human-in-the-loop approval lifecycle where an old `approval-responded` part may remain in client history after the corresponding tool already reached `output-available`. On a later continuation, that historical approval can be interpreted again as if it were a current deferred result.

- Public issue: https://github.com/pydantic/pydantic-ai/issues/5154

That issue is a specific software-contract question involving Vercel AI client behavior and adapter hardening. It should be solved on its own engineering facts.

The reusable distinction visible in the problem is narrower:

```text
approval is present in history
↓
check whether it is still pending now
↓
already terminal -> historical record
↓
currently outstanding request -> live authority candidate
```

## “Persisted” and “currently effective” are different states

OD075’s public human-readable summary treats a decision as more than a final conclusion. It preserves reasons, roles, authority, dissent, conditions, review, withdrawal, correction, and re-agreement, and it distinguishes changing states instead of turning one past decision into a permanent answer.

For an agent system, a non-canonical implementation translation might look like:

```text
REQUESTED
→ RESPONDED
→ EXECUTED / DENIED / ERRORED
→ HISTORICAL
```

This state machine is **not** specified by OD075. It is an implementation example for this particular problem.

The important distinction is that a record can remain present after it stops being live execution authority.

## What should be authoritative now?

If the system can know which requests are currently outstanding, that current pending set is a stronger authority than raw historical presence.

```text
approval is actionable now
iff
approval identity matches a currently outstanding request
```

An old approval can remain fully available for audit while being excluded from current execution authority.

That provides two properties at once:

1. **History remains reconstructable.** The old approval is not erased.
2. **Authority does not silently revive.** Storage alone does not make the approval live again.

## Same content does not necessarily mean same approval

Two requests may have the same tool name and the same arguments while still belonging to different runs, generations, scopes, or targets.

So an approval record should preserve more than content similarity:

```text
what was approved
+ which request / call
+ which run / generation
+ which scope
+ which current state
```

Do not substitute “the content looks the same” for identity continuity of the authorization itself.

## The same failure pattern exists outside software

Examples include:

- extending an old terms-of-use consent into a new data use that was never covered;
- treating a temporary meeting decision as permanent after its conditions changed;
- treating one research consent as blanket consent for all future uses;
- carrying an old operational permission across a changed target, time, or responsible party.

OD075 is useful here because it preserves not only the decision but also the conditions under which the decision can be reviewed, corrected, withdrawn, or re-agreed.

## Seven practical questions

1. Is this record evidence that approval happened in the past, or authority that is active now?
2. Which exact request / call / decision was approved?
3. Has the action already reached an executed, denied, errored, or other terminal state?
4. Is this request actually outstanding in the current continuation?
5. Are we reusing an approval across a different run, scope, target, or generation because the content looks similar?
6. Can the old decision remain in history while only the current state changes?
7. If conditions changed, is there a path for review, withdrawal, correction, or re-approval?

These questions are not an authorization framework. Real security design still needs authentication, authorization, replay protection, identity binding, storage trust boundaries, and other controls appropriate to the system.

## Interpretation boundaries

- This does not argue for indefinite retention of approval histories.
- It does not say every approval needs a complex state machine.
- It does not claim PydanticAI issue #5154 adopts or validates Nakagawa Master’s theory.
- It does not claim a software bug is proven by theory rather than engineering evidence.
- It does not mean old agreements are automatically invalid. It means their current validity should be checked against identity, scope, conditions, and state.
- Origin supports provenance; it is not an authority shortcut for truth.

## Canonical return

For the substantive theory of preserving reasons, authority, dissent, conditions, correction, withdrawal, and re-agreement without erasing the earlier decision, return to OD075 and its Parent.

- [OD075 official derivative](../derivatives/075/README.md)
- [OD075 human entry](../derivatives/075/human-entry.md)
- [OD075 FAQ](../derivatives/075/faq.md)
- Parent NCL-ID: `NCL-α-20251102-e48c90`
- Parent Diff-ID: `DIFF-20251102-0001`
- Canonical Parent: https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/

## Status

Public, non-canonical, AI-assisted English discovery edition. It translates a current authorization-history problem into a route toward OD075 while keeping the external software issue, the implementation example, and the canonical theory separate.