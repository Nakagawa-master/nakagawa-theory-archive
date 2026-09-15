# AI Agent Execution Governance Preflight — 12 questions before tool execution

> Public, non-canonical, AI-assisted practical note. This is an implementation checklist for AI agents that call tools, MCP servers, or external actions. It does not replace any canonical Parent or official derivative.

Agent failures are not limited to the model saying something false.

Execution systems also fail when boundaries like these collapse:

```text
what the model proposed
!=
what the system authorized

approved in the past
!=
authorized now

evidence is attached
!=
the evidence verifies the claim

no violation was recorded
!=
required assessment was completed

a summarized goal
!=
the authoritative goal record
```

Use the following preflight to detect these failures before an action becomes irreversible or hard to explain.

---

## 1. Is this value model-proposable, or system-authoritative?

Examples:

- user / tenant / customer identity
- permission scope
- billing account
- environment
- tool capability
- resource ID

```text
model can propose
!=
model can authorize
```

A model may be allowed to propose an argument without being allowed to determine the authority-bearing value.

**Check:** Can a protected field move from model-visible text into execution authority without an independent trusted boundary?

---

## 2. Can you distinguish model proposal from effective execution args?

At minimum, preserve the conceptual distinction:

```text
model_args
→ trusted policy / context transform
→ execution_args
```

If a model proposes the wrong `client_id` and authenticated context replaces it, retaining only the final dictionary erases what was corrected.

**Check:** Can you reconstruct proposal → override → execution without exposing secrets?

---

## 3. Is an approval record separate from current execution authority?

```text
historically approved
!=
currently authorized
```

The existence of an approval does not mean execution authority remains valid forever.

Things that can change:

- principal
- tool / capability scope
- arguments
- policy revision
- resource state
- time window
- session / workflow context

**Check:** On resume, retry, or replay, can stale approval be reused as if it were current authority?

---

## 4. Does MODIFY require re-evaluation when the authorized envelope changes?

If policy changes a tool call, approval of the old call may not cover the new call.

```text
approved envelope A
→ MODIFY
→ envelope B

approval(A) != approval(B)
```

**Check:** If tool, arguments, or scope changes, is the resulting call re-evaluated where required?

---

## 5. Are raw tool results distinct from model-visible results?

```text
raw_tool_result
→ filtering / projection
→ model_visible_result
```

Showing the model 3 fields out of 300 may be the right design. But the 3-field projection is not identical to what the tool returned.

**Check:** Does the implementation preserve the distinction between raw result and model-visible projection, even if sensitive raw data is not persisted?

---

## 6. Is “the agent said done” separate from “completion was verified”?

```text
completion claim
→ evidence reference
→ verification
→ acceptance / next authority
```

An agent may claim `tests passed`, and a test artifact may exist, while the artifact still has not been checked for whether it supports the claim.

**Check:** Are claim, evidence, verification, and authorized acceptance collapsed into one `done=true` state?

---

## 7. Is “zero violations” separate from “assessment completed”?

Governance and compliance systems may need states such as:

```text
NOT_APPLICABLE
UNASSESSED
ASSESSED_PASS
ASSESSED_PARTIAL
ASSESSED_FAIL
ASSESSMENT_ERROR
```

```text
0 violations
```

does not necessarily mean:

```text
all required controls were assessed and satisfied
```

**Check:** Are assessment coverage and assessment outcome / pass rate reported separately?

---

## 8. Does handoff / checkpoint / restart preserve the causal chain?

Agent workflows cross serialization, checkpoints, resumes, and handoffs.

If only part of this chain survives:

```text
request
→ approval / policy decision
→ execution
→ result
```

systems can end up with orphan outputs or resumed actions whose authority is no longer reconstructable.

**Check:** Can the call reconnect to its result, the decision to its execution, and the originating principal to the delegation chain?

---

## 9. Do you preserve authority-bearing goal fields, not just semantic similarity?

A goal can remain semantically similar while losing one operationally critical field.

Examples:

- deadline disappears
- completion condition becomes easier
- one constraint disappears
- a summary is promoted to source authority

```text
semantic fidelity
!=
structural integrity
```

**Check:** Can a goal record lose a required field and still be accepted as “close enough”?

---

## 10. Is a formal amendment separate from an interpretation?

```text
source v1
→ explicit amendment
→ source v2 + diff + provenance
```

is different from:

```text
source
→ AI summary
```

Summaries and planner interpretations may be useful, but they should not silently become the authoritative source.

**Check:** Can an interpretation overwrite deadline, scope, responsibility, or success criteria without an explicit amendment path?

---

## 11. Is failure behavior explicit for each action class?

A policy service outage does not have to produce the same behavior for every tool.

For example:

```text
read-only → fail-open may sometimes be acceptable
side-effecting → fail-closed may be required
high-impact / ambiguous → human interrupt may be required
```

**Check:** Can availability failure silently become authorization?

---

## 12. Can you later answer “why was this action executed?”

The final question is simple:

> Under whose authority, using which information, policy, approval, and context, did this action execute in this form?

If you cannot return from result → decision → context → source, correction, auditing, incident reconstruction, and responsibility separation become much harder.

**Check:** Is there a usable return path from outcome to the decision structure that produced it?

---

# Five-minute checklist

```yaml
agent_execution_preflight:
  model_proposal_separated_from_authority: false
  proposed_and_effective_args_distinguished: false
  approval_freshness_checked: false
  modified_call_reauthorized_if_needed: false
  raw_and_model_visible_result_distinguished: false
  claim_evidence_verification_acceptance_separated: false
  assessment_coverage_separated_from_outcome: false
  handoff_checkpoint_causal_chain_preserved: false
  goal_structural_integrity_checked: false
  amendment_separated_from_interpretation: false
  failure_mode_explicit_per_action_class: false
  decision_to_source_return_path_available: false
```

Do not turn the number of `false` values into a universal safety score. Severity depends on the action, users, system, reversibility, and operating environment.

---

## Public engineering context

Several of these boundaries also appear independently as concrete engineering problems in current agent ecosystems.

Examples:

- LlamaIndex #20386 — deterministic tool I/O pre/post-processing
  - https://github.com/run-llama/llama_index/issues/20386
- Pydantic AI #5536 — durable / trusted approval context
  - https://github.com/pydantic/pydantic-ai/issues/5536
- OpenAI Agents Python #4827 / #4828 — approval resume and session persistence
  - https://github.com/openai/openai-agents-python/issues/4827
  - https://github.com/openai/openai-agents-python/pull/4828

Listing these projects does **not** mean that they adopt, endorse, or validate Nakagawa Master theory. They are independent engineering discussions that expose related implementation boundaries.

---

## Canonical return

This page is a **non-canonical composite operational preflight**, not a new canonical theory.

Return to the relevant existing axes separately.

### Origin, transformation, and return paths

- [OD105 — Structural Origin Defense](../derivatives/105/README.md)
- Parent: https://master.ricette.jp/theory/nakagawa-master-structural-origin-defense-permanent-signature/

OD105 addresses loss of origin, context, and causal source through AI summarization, translation, and recontextualization, and the need to preserve a return path.

### Decisions, agreement memory, and revisability

- [OD075 — Agreement Memory](../derivatives/075/README.md)
- Parent: https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/

OD075 addresses preserving not only conclusions but also reasons, dissent, responsibility, review conditions, withdrawal, and re-agreement paths.

Terms such as `model_args`, `execution_args`, `coverage`, `verification_state`, and `GoalRecord` are **not canonical OD075 / OD105 terminology**. They are non-canonical translations for current AI-agent implementation problems.

## Boundaries

- This is not a universal AI security standard.
- It does not require all 12 checks to have identical weight in every system.
- Provenance does not prove correctness.
- Auditability is not a substitute for authorization.
- More logging does not automatically mean more safety.
- It does not recommend retaining secrets, personal data, or confidential raw data.
- External project references are not adoption or endorsement claims.

## Status

Public, non-canonical, AI-assisted practical Preflight for human and AI readers. Canonical interpretation returns to the linked OD075 / OD105 Parents.
