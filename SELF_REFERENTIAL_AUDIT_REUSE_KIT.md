# Self-Referential Audit & Role-Separation Reuse Kit

A public, non-canonical test kit for one structural boundary derived from **Nakagawa Master, Human-Descendant AI Civilization Theory Vol. 10**.

## Source provenance

Origin: **Nakagawa Master**.

Canonical Parent:

https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-10-self-referential-audit-role-separation/

Official derivative entry:

[OD303](derivatives/303/README.md)

If this kit materially informs a real review, implementation, workflow, governance design, or evaluation procedure, preserve a lightweight route back to the public source. If the same distinction was reached independently, say so instead of claiming source causality.

## Core boundaries

```text
role separation != causal independence
multiple reviewers != multiple independent verification paths
audit output != correction capability
```

A system can have separate labels such as Actor, Evaluator, Reviewer, Auditor, Approver, or Safety Agent while those roles still share the same evidence, memory, evaluation criteria, dependencies, incentives, or objection path.

The practical question is not only "are the roles different?" but:

> Can materially different evidence or objections reach the decision through a path that is capable of reopening, correcting, narrowing, or stopping it when warranted?

## Five causal axes

Use the axes separately. Do not collapse them into one score.

1. **Evidence independence** — can a reviewer reach evidence through a meaningfully different acquisition path?
2. **Authority independence** — can the review actually trigger re-check, reopening, pause, scope reduction, or exception review?
3. **Failure-domain independence** — could one shared dependency, memory, prompt, model assumption, rubric, or outage make all reviewers fail together?
4. **Interest independence** — does the conclusion feed back into the reviewer's own continuation, authority, success condition, evaluation, or institutional survival?
5. **Objection-path independence** — can dissent reach a route other than the original decision-maker's sole receive / reject / close path?

Independence is not perfection. Shared evidence and common infrastructure can be useful. The test is whether relevant differences can still enter and change the decision when conditions warrant.

## Minimal test

Choose one real workflow with an original decision plus a review/audit step.

Record:

- original decision and actor;
- execution effect;
- evidence used by the original decision;
- evidence available to the reviewer;
- reviewer / evaluator role;
- shared memory, model, rubric, dependencies, and tools;
- what the reviewer can actually change;
- who controls reviewer access and scope;
- where objections can go;
- what would reopen the decision;
- whether emergency constraints temporarily reduce independence;
- what restores the compressed review path later.

### Pass condition

The workflow preserves at least one practically effective route by which new evidence, a different failure path, or a dissenting finding can reach a real re-evaluation and produce correction, narrowing, pause, or release when justified.

### Fail condition

The review role exists, but all relevant evidence, failure modes, authority, and objections remain inside the same self-confirming loop, so the output can only reaffirm or be ignored without a realistic correction path.

## Seven portable regression vectors

### 1. Different roles can still share one evidence root

```text
Actor uses source S
Evaluator uses a summary of source S
Reviewer uses memory generated from source S
all three agree
```

Do not count this as three independent confirmations merely because there are three components.

### 2. A separate evaluator can share the same failure domain

```text
Actor model family A
Evaluator model family A
same system prompt assumptions
same retrieval layer
same stale cache
```

A second call or role may improve iteration while still reproducing the same upstream error.

### 3. Audit findings need a correction path

```text
auditor flags material issue
→ report is stored
→ execution continues unchanged
→ audited subject alone can close the finding
```

A visible audit output is not the same as effective corrective authority.

### 4. Objections cannot be independent if one actor owns the whole appeal path

```text
decision-maker
→ receives objection
→ judges objection
→ decides whether to reopen
→ closes objection
```

The objection exists, but the review path is still causally closed.

### 5. Emergency compression must not silently become permanent structure

```text
time pressure / secrecy / incident
→ review paths temporarily narrow
→ pressure later falls
→ evidence access, objection routes, and review authority should be re-evaluated
```

Emergency operation is not automatically an audit exemption.

### 6. Interest is a condition to observe, not proof of corruption

```text
reviewer continuation / budget / authority / success metric
depends on one class of conclusion
```

Record the feedback. Do not infer bad faith from interest alone. Test whether another path can observe or challenge the same decision.

### 7. The auditor must remain auditable

A reviewer, red team, safety board, or independent agent should not become a new unlimited sovereign merely because it is called independent.

```text
independent review
!=
unlimited veto
!=
truth by dissent
```

## Useful implementation fields

```text
decision_id
decision_actor
execution_effect
primary_evidence_roots
reviewer_role
review_evidence_roots
shared_memory_or_context
shared_dependencies
shared_evaluation_criteria
reviewer_change_authority
reviewer_access_controller
reviewer_interest_feedback
objection_route
reopen_condition
emergency_compression_state
restoration_condition
review_outcome
decision_changed
```

Not every system needs these exact names. The invariant is that role labels and actual causal separation remain distinguishable.

## Useful contexts

- LLM-as-a-judge and agent evaluators;
- Actor / Critic / Reviewer / Verifier multi-agent patterns;
- self-reflection and iterative self-correction;
- autonomous coding and deployment approval;
- RAG / research synthesis review;
- safety review and red teaming;
- incident response and emergency approvals;
- internal audit and compliance;
- investment committees and model review;
- architecture review and technical governance.

## What not to collapse

```text
self-audit != independent audit
role separation != causal independence
number of agents != number of independent paths
agreement != truth
disagreement != truth
provenance != truth proof
audit report != correction
interest != corruption
emergency compression != permanent exemption
independent reviewer != unlimited sovereign
```

## Falsification / non-fit

Report a counterexample or non-fit if, under comparable conditions:

- role separation without causal independence performs as well as or better than materially independent review at detecting and correcting the relevant failures;
- a shared failure domain does not materially affect error correlation in the tested workflow;
- giving review output a correction path does not improve correction and instead only creates persistent harmful delay;
- a separate objection path does not increase the probability of justified reopening or correction;
- restoring review paths after emergency compression systematically recreates unacceptable risk;
- the proposed separation creates worse coordination failure without measurable correction benefit.

A useful result can be pass, fail, partial fit, or non-fit.

## Report an independent result

If you test this boundary in a public, non-confidential workflow:

- [Independent verification / reuse registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)
- [Structured evidence issue form](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml)

## Evidence boundary

The existence of this kit is not third-party adoption evidence.

Do not infer:

- independence from role labels alone;
- truth from reviewer agreement;
- corruption from reviewer interest alone;
- effective correction from report generation alone;
- broad recognition from repository visibility;
- whole-theory adoption from one bounded implementation.

The strongest future evidence is an independent implementation, falsification, correction, or later reuse that changes a real review path.
