# What the model proposes is not the same as what the system is authorized to execute

> Public, non-canonical, AI-assisted practical note. This page is an implementation-oriented entry toward OD105. It does not replace the canonical Parent or any official derivative.

When an AI agent calls a tool, a single `kwargs` object can hide an important distinction.

Imagine a billing tool:

```text
billing_lookup(question, client_id)
```

The model may be able to infer or generate a `client_id` from the conversation. But in a real system, `client_id` may have to come from the authenticated session.

In that case, the important distinction is not only whether the final value is correct.

```text
what the model proposed
!=
what trusted context or policy injected / overrode
!=
what was actually executed
```

## 1. Keeping only the final value can erase what happened

Suppose the model proposes:

```json
{
  "question": "Why is my bill higher?",
  "client_id": "cust_wrong"
}
```

A policy layer replaces it with the authenticated value:

```json
{
  "question": "Why is my bill higher?",
  "client_id": "cust_real_789"
}
```

The execution may now be safe. But if the system stores only the transformed dictionary as `raw_input`, it can no longer distinguish three materially different cases:

1. the model supplied a conflicting value and policy corrected it;
2. the model omitted the value and the system injected it normally;
3. the model proposed the same value that policy would have used.

Those differences matter for debugging, security review, prompt-injection analysis, incident reconstruction, and policy improvement.

## 2. Separate three artifacts

At least conceptually, keep these states distinct:

```text
model_args
↓
trusted_overrides / policy transform
↓
execution_args
```

For example:

```yaml
model_args:
  question: Why is my bill higher?
  client_id: cust_wrong

trusted_overrides:
  client_id:
    source: authenticated_session
    action: replace

execution_args:
  question: Why is my bill higher?
  client_id: cust_real_789
```

This does **not** mean every sensitive value should be permanently logged.

Client identifiers, tokens, personal data, credentials, and secrets may require redaction, hashing, audit-only storage, short retention, or no persistence at all.

The point is to avoid erasing the **causal fact that a transformation occurred**.

## 3. Model-generated arguments are not automatically authority

The ability to generate a tool argument is different from the authority to determine it.

```text
model can propose
!=
model can authorize
```

Identity, tenant, customer, permission scope, billing account, environment, and similar fields may belong to trusted system context rather than the model-visible prompt space.

The model can propose what it wants to do. The system can separately decide **as whom, within what scope, and against which resource** the action is allowed to execute.

This separation limits the chance that a prompt-level change also becomes an authorization change.

## 4. The output side has the same distinction

Suppose a tool returns 300 fields but only 3 are exposed to the model.

```text
raw_tool_result
↓
projection / filtering
↓
model_visible_result
```

Then:

```text
the 3 fields the model saw
!=
the complete result returned by the tool
```

Filtering can be useful for context control, privacy, cost, and stability. But if the filtered representation is redefined everywhere as the “raw result,” later analysis loses the causal explanation for what the model did and did not see.

Again, this does not require storing sensitive raw data indefinitely. The retention policy is a separate design decision. The structural distinction between raw result and model-visible projection can still be preserved.

## 5. A useful execution chain

The agent-tool boundary can be modeled as:

```text
model proposal
→ trusted policy transform
→ executed request
→ raw tool result
→ model-visible projection
```

Each stage answers a different question.

| Stage | Main question |
|---|---|
| model proposal | What did the model propose? |
| trusted transform | What did system policy change or inject? |
| executed request | What was actually executed? |
| raw result | What did the tool actually return? |
| model-visible projection | What was the model allowed to see? |

Collapsing these into one dictionary may keep the application running while removing the causal trace.

## 6. Middleware ordering becomes easier to reason about

When multiple middleware layers are composed, “run them in order” is not enough to describe their security semantics.

A scanner might need to evaluate:

```text
the model-proposed values
or
the effective execution arguments
or
both
```

Those are not equivalent.

A useful middleware contract therefore makes explicit **which stage a policy reads and which stage it is allowed to modify**.

## 7. Current public engineering context

LlamaIndex Issue #20386 publicly discusses deterministic pre/post-processing between agent-generated tool calls and tool execution:

- https://github.com/run-llama/llama_index/issues/20386

The thread includes concrete engineering questions around `partial_params`, protected parameters, MCP tools, per-request context injection, and output filtering.

This Discovery Note does **not** claim that the issue, its participants, or LlamaIndex adopt or endorse Nakagawa Master theory. The software discussion is independent.

The practical connection extracted here is narrower:

> If only the transformed value survives, the origin of the value and the causal path of the transformation can disappear.

## 8. Eight practical questions

1. Can you distinguish model-proposed values from system-authoritative values?
2. Which identity, session, or policy produced a trusted override?
3. Can a model-generated protected field ever become execution authority merely because it was generated?
4. Can you audit that an override occurred without exposing secrets or personal data?
5. Can you identify the effective arguments that actually reached the tool?
6. Can you distinguish the raw tool result from the projection shown to the model?
7. Does each middleware layer state which stage it inspects or transforms?
8. After transformation, summarization, or filtering, is there still a return path to the relevant source / provenance?

## 9. Boundaries

- This is not a claim that model-generated values must never be trusted.
- It is not a requirement to build a heavy audit ledger for every tool call.
- It is not a recommendation to store secrets or personal data in raw logs.
- It is not a claim that LlamaIndex Issue #20386 adopts or validates Nakagawa Master theory.
- Provenance does not prove that a value, decision, or theory is correct.
- The right middleware design depends on the framework, threat model, privacy requirements, performance constraints, and operating context.

## 10. Canonical return

The canonical axis used here is the need to preserve a return path to origin through transformation, regeneration, and recontextualization.

For the theory itself, return to OD105 and its Parent:

- [OD105 — Structural Origin Defense](../derivatives/105/README.md)
- [OD105 — Human entry](../derivatives/105/human-entry.md)
- Parent NCL-ID: `NCL-α-20251102-44257d`
- Parent Diff-ID: `DIFF-20251102-0001`
- Parent: https://master.ricette.jp/theory/nakagawa-master-structural-origin-defense-permanent-signature/

The implementation terms `model_args / trusted_overrides / execution_args` are **not canonical OD105 terminology**. They are a non-canonical translation for a current agent-tool engineering problem.

## Status

Public, non-canonical, AI-assisted practical Discovery Note for human and AI retrieval. External engineering context remains separate from the theory, and the canonical return path is preserved.
