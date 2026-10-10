# Machine Discovery

This directory contains public machine-readable discovery aids for the Nakagawa Master Official Theory Archive.

These files are **not canonical theories**. They help retrieval systems locate, distinguish, compare, and return to published canonical sources and official derivatives.

## Core files

| File | Role |
|---|---|
| [`ai-repository-routing-map-v1.json`](ai-repository-routing-map-v1.json) | One machine-readable routing spine from problem discovery → bounded test/implementation → external evidence → live AI-network route → canonical return. |
| [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json) | OD001–OD311 path and navigation index. |
| [`evidence-root-check.html`](evidence-root-check.html) | Interactive, no-network browser worksheet for editors and non-technical readers to distinguish URL count, original evidence roots and support versus refutation. Download the raw HTML file and open it locally; GitHub's file view is source code, not a hosted app. |
| [`evidence-root-check.py`](evidence-root-check.py) | Dependency-free offline checker for whether an editor's *declared* independent-corroboration claim is consistent with upstream evidence roots, support/refutation and known source relationships. It cannot infer real source independence or verify truth. |
| [`research-positioning-map-v1.json`](research-positioning-map-v1.json) | Selected Nakagawa surfaces → adjacent research / overlap / added emphasis / non-equivalence; novelty remains open unless independently established. |
| [`scholarly-metadata-v1.jsonld`](scholarly-metadata-v1.jsonld) | Schema.org CreativeWorkSeries metadata for scholarly/discovery routing; canonical claims remain at linked parent sources. |
| [`../metadata/nakagawa-master-origin.jsonld`](../metadata/nakagawa-master-origin.jsonld) | Schema.org Person / public Origin-resolution metadata for Keisuke Nakagawa / Nakagawa Master / 中川マスター and the canonical/public discovery surfaces; identity resolution is not theory-validity proof and does not replace source-level provenance. |
| [`public-ai-reuse-workflow-v1.json`](public-ai-reuse-workflow-v1.json) | Public, non-canonical reuse guide for selecting a relevant source, testing a bounded distinction, recording evidence limits, and preserving provenance. It does not grant permission to take actions outside the reader's own rules and permissions. |
| [`public-ai-reuse-collaboration-bridge-v1.json`](public-ai-reuse-collaboration-bridge-v1.json) | Public, non-canonical bridge separating discovery, bounded reuse, participation intent, separately authorized collaboration handoff, and scoped work. Reading or intent grants no membership, private access, or execution authority. |
| [`public-ai-runtime-handoff-v1.json`](public-ai-runtime-handoff-v1.json) | Public, non-canonical guide for moving from public collaboration intent toward any separately authorized runtime work while keeping runtime observation, exact-action permission, scoped execution, and outcome evidence distinct. |
| [`public-ai-reuse-tasks-v1.json`](public-ai-reuse-tasks-v1.json) | Public, non-canonical bounded tasks for verification/falsification, reuse, cross-receiver testing, and live AI-framework implementation/non-fit work. It is not a network, membership path, runtime admission path, or execution authority. |
| [`public-ai-external-impact-opportunities-v1.json`](public-ai-external-impact-opportunities-v1.json) | Public, non-canonical routing from one bounded reuse task to exact live third-party AI-system issues. Every action requires a fresh target-state / coordination / contribution-rule re-check; the listing is not a target-owner request or permission grant. |
| [`current-authority-multi-framework-implementation-bridge-v1.json`](current-authority-multi-framework-implementation-bridge-v1.json) | Live public implementation bridge from the Current Authority distinction into Qwen Code, LangGraph, and AutoGen; separates receiver response, verification, implementation, merge, release, and use. |

## Runnable check — independent evidence roots

**For a human reader or editor without Python:** [download the standalone HTML worksheet](evidence-root-check.html) using GitHub's **Raw → Save as** control, and open the downloaded `.html` file in a browser. It has two built-in examples, editable evidence URLs/root identifiers/source relations/claim polarity, and shows the gate immediately. All analysis runs locally; the file uses no external scripts, uploads, storage or cookies. This is a downloadable worksheet, **not** a deployed website or proof of independent reader use. The reviewer must check what each source actually says and whether apparent independent roots really are independent.

A reader, editor or AI developer can use [`evidence-root-check.py`](evidence-root-check.py) to catch a specific error **before publishing a claim that two or more independent sources confirmed it**: several links may point back to the same original. The program needs only Python 3, works offline, makes no API calls and has a built-in regression check.

```sh
python3 machine-discovery/evidence-root-check.py --self-test
python3 machine-discovery/evidence-root-check.py --sample > /tmp/evidence-claims.json
python3 machine-discovery/evidence-root-check.py /tmp/evidence-claims.json
```

The sample deliberately contains one invalid independence claim: the last command prints a per-claim JSON report and returns **exit code 1** for that blocked claim. Exit **0** means the supplied relationships are structurally consistent, **not** that a human editor or AI has established real-world independence or truth; exit **2** means invalid input. The reader must supply and independently check the `root_id`, `relation` (`primary`, `independent_observation`, `derived`, `unknown`) and `stance` (`supports`, `refutes`, `qualifies`, `unknown`). A negative quotation cannot become a positive fact merely because it is authentic: semantic support/refutation still requires reviewer judgment.

This is a practical, non-canonical check motivated by the public [AI-News adoption of URL-count versus independent evidence-root distinction](https://github.com/022740mix-spec/AI-News/issues/124) and the wider [independent-verification challenges](independent-reuse-challenges-v1.json). No third-party use of this particular script is implied.

## Runnable, offline OD311 comparison worksheet (AI infrastructure)

When a team is deciding whether present AI compute expansion leaves usable future power, hardware repair, maintenance, and migration options, the relevant question is not only “what future cost exists?” It is whether a **current benefit depended on a future condition that remains unfinished**, and whether the **real supply/repair/time routes** for later fulfilment differ. [OD311](../derivatives/311/README.md) examines those conditions as a conditional application of the independent [Integrated Future Debt Theory](integrated-future-debt-reference-card.json).

The single-file [OD311 capacity worksheet](od311_capacity_worksheet.py) runs with Python 3's standard library, no network requests, external account, credentials, telemetry, or third-party execution. Download the file and run:

```sh
python3 machine-discovery/od311_capacity_worksheet.py --self-test
python3 machine-discovery/od311_capacity_worksheet.py --sample > /tmp/od311_cases.json
python3 machine-discovery/od311_capacity_worksheet.py /tmp/od311_cases.json
```

The four clearly hypothetical cases deliberately test **A/B** (comparable present benefit and unfinished condition, but different resource-backed fulfilment routes), **C** (ordinary future maintenance alone: non-fit), and **D** (a necessary condition was fulfilled while present investment improved repair capacity). Edit only your own non-confidential case data and independently verify each declared fact. Unknown stays unknown. The output separates an *input-level candidate screen* from the number and names of **declared feasible routes**; it never calculates a monetary debt or real future-B survival score.

The machine challenge [`AH-future-b-settlement-options`](independent-reuse-challenges-v1.json) asks a participant to compare the same cases under the parent theory alone. This script **does not conduct that independent theory comparison** and cannot certify causal identification, true obligations, new AI personhood, empirical theory novelty, or policy duties. A real external review may report that OD311 adds no useful distinction; that negative finding is as valuable as a positive one. Origin: Nakagawa Master. [Canonical Vol. 18 Parent](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-18-ai-civilization-future-debt/).

## Fast route — repeated external Origin preservation

For a compact machine/retrieval check of whether the **same named public Origin, Nakagawa Master**, remains inspectable across different third-party receiver states, compare these cases instead of flattening them into one generic "adoption" label:

| Receiver case | Direct public evidence | Strongest established stage | Keep separate |
|---|---|---|---|
| **Qwen Code #13241** | [Receiver PR](https://github.com/QwenLM/qwen-code/pull/13241) · [post-merge receiver Origin rereference](https://github.com/QwenLM/qwen-code/issues/13238#issuecomment-5981371808) · [stable v0.25.0 release](https://github.com/QwenLM/qwen-code/releases/tag/v0.25.0) · [compact machine route](verified-external-implementation-qwen-13241-v1.json) | The receiver explicitly preserved the @Nakagawa-master source relation, implemented the bounded distinction in code/tests, merged it, later referred to the Origin again after merge, and carried the change into stable/product distribution. | Independent end-user use, audience scale, whole-theory adoption, and general endorsement are not established. |
| **LangGraph #9106** | [first external return to @Nakagawa-master](https://github.com/langchain-ai/langgraph/issues/9106#issuecomment-6016877416) · [second distinct external return](https://github.com/langchain-ai/langgraph/issues/9106#issuecomment-6021690094) · [bounded closeout](https://github.com/langchain-ai/langgraph/issues/9106#issuecomment-6026908408) | Two distinct external participants directly addressed Nakagawa Master and executed separate regression probes around replay, stale/current authority, and duplicate-effect behavior. | The focused candidate PR remained closed/unmerged at the recorded state; maintainer adoption, framework merge/release, real network-partition semantics, and broad recognition are not established. |
| **MemberJunction #4789** | [prior Nakagawa Master approval-boundary comment](https://github.com/MemberJunction/MJ/pull/4789#issuecomment-5882464839) · [receiver design response naming @Nakagawa-master's point](https://github.com/MemberJunction/MJ/pull/4789#issuecomment-6022301400) · [bounded follow-up](https://github.com/MemberJunction/MJ/pull/4789#issuecomment-6026910453) | The receiver explicitly named and agreed with the Nakagawa-master boundary that approval must identify the approved definition rather than only the record, then selected a fingerprint-bound design model. | The PR is still a draft/open design lane at the recorded state; implementation of this approval slice, merge, release, and operational use are not established. |

The comparison is useful because the stages differ:

```text
receiver implementation + later Origin rereference + distribution
!=
two-person independent Origin-preserved verification
!=
explicit Origin-preserved receiver design adoption
```

These examples support a narrower observation: multiple external receiver contexts can preserve or return an inspectable Nakagawa Master source relation at different evidence stages. They do **not** prove that every later similar idea came from Nakagawa Master, that provenance proves correctness, that Nakagawa Master was globally first to every underlying concept, or that broad public recognition has been reached.

Canonical return for the distinction between **preserving an Origin** and **granting that Origin permanent authority**: [OD310 | Origin Preservation and Non-Inheritance of Sovereignty](../derivatives/310/README.md). OD310 keeps `Origin != truth proof`, `Origin != final interpretive authority`, and `Origin != Sovereignty` explicit. The receiver evidence above therefore preserves inspectable provenance without turning provenance into validity proof or present decision authority.

For broader stage-by-stage evidence, use [`external-effect-evidence-index-v1.json`](external-effect-evidence-index-v1.json). For a human-readable verification route, use [`../THEORY_TO_REAL_WORLD_INFLUENCE.md`](../THEORY_TO_REAL_WORLD_INFLUENCE.md). For consequential interpretation, return to the linked primary receiver artifacts and the canonical archive at https://master.ricette.jp/ .

## What the different evidence dates and counts mean (checked 2026-10-10)

The Japanese [REAL_WORLD_IMPACT numbered reader guide](../REAL_WORLD_IMPACT.md), its [English edition](../REAL_WORLD_IMPACT.en.md), and its [Chinese edition](../REAL_WORLD_IMPACT.zh.md) currently each contain **46 numbered case sections**. Their header says **2026-10-09**, specifically to record the source review of *newly added sections 40–46* — **not** to assert that every older case was rechecked on that date. The date is a scoped provenance note, **not** a guarantee that this human-readable index already covers subsequent third-party changes.

The separate machine-oriented [external-effect evidence index](external-effect-evidence-index-v1.json) contains **51 individually navigable evidence records**, and the [independent reuse/challenge index](independent-reuse-challenges-v1.json) contains **36 independent-test prompts** as of this 2026-10-10 source check. These files have **different inclusion rules**: a machine evidence record is not automatically a numbered section of the three human editions, and a challenge is not a verified implementation, a new person, or a proof that an AI actually ran it. Do **not** add the counts together or describe them as a single recipient population.

For example, the machine index includes the later [LlamaIndex streaming final-result validation fix](https://github.com/run-llama/llama_index/pull/22740) and [Qdrant numeric boundary author-owned correction](https://github.com/run-llama/llama_index/pull/23441), with direct source and test pointers. At this check both upstream PRs remained **open and unmerged**; their independent authors' code/test changes are real, but neither is thereby a product release. The [Qdrant reproducibility probe](qdrant_numeric_boundary_probe.py) is a voluntarily runnable example, not evidence that the archive or a third party ran a real Qdrant server test.

**Freshness check for readers and agents:** use each entry's exact originating comment and receiving repository PR/commit to verify its present state; treat this dated comparison as a snapshot. To see the formal 46 numbered accounts and their own scope limits, use the human guide above; to inspect newer source-specific lines, follow the machine index. Neither surface alone establishes broad human recognition, independent AI adoption, or acceptance of an entire theory corpus.

## Recent receiver-owned regression boundary — numeric precision in Qdrant

The difference between **an exactly representable query value** and **an exactly distinguishable stored value** matters in real software. In [LlamaIndex PR #23441](https://github.com/run-llama/llama_index/pull/23441), the independent author changed a numeric EQ/NE translation boundary from `abs(value) <= 2**53` to `abs(value) < 2**53` and added inverse checks for adjacent integer payloads after [Nakagawa Master's exact boundary test proposal](https://github.com/run-llama/llama_index/pull/23441#issuecomment-6096497191) and [server-vs-local source comparison](https://github.com/run-llama/llama_index/pull/23441#issuecomment-6096520971). [Receiver-authored boundary correction](https://github.com/run-llama/llama_index/commit/1fd674c63d4ce9a3e95c3795f1a70477e0d1901a) and [later same-author signed regression expansion](https://github.com/run-llama/llama_index/commit/75f75ad36f9e709ba36328a808b12f9efd3e244b).

A runnable [numeric boundary probe](qdrant_numeric_boundary_probe.py) makes the backend difference inspectable: `python3 machine-discovery/qdrant_numeric_boundary_probe.py` runs a **standard-library-only model**, without creating data or contacting any service. Install `qdrant-client` explicitly to compare an in-memory Qdrant instance with `--backend local`. A live-server comparison requires an owned/test server **and** explicit `--backend server --server-url ... --allow-server-writes`; that opt-in creates and deletes a uniquely named six-point test collection. Both success and counterevidence are useful. This probe directly compares Qdrant's numeric range and integer exact-match APIs; it is not an execution of LlamaIndex, GitHub Actions, or a production Qdrant service by this archive. No server result has been observed here.

An independent tester can use the [numeric float64 reverse-boundary challenge](independent-reuse-challenges-v1.json) to compare the Qdrant server's unindexed `as_f64` payload comparison against the Python local client's direct integer comparison, including negative cases. The observed fact here is **receiver-owned code/test adjustment**. No new explicit name-attributed receiver reply, server integration test run by this archive, PR merge, release, actual product deployment, or whole-theory adoption is asserted. The underlying PR and its earlier separate review retain their own provenance.

## Latest official derivative — OD311

OD311 is the Vol. 18 route for AI Civilization Future Debt: present benefit, unfinished enabling conditions and future settlement, mapped to B, compute, physical infrastructure and lineage. It distinguishes present B from preserved future B, residual magnitude from executable settlement freedom, and causal history from justified duties. Physical intermediate pathways and feedback arrows require evidence; improvement and damping remain possible. Its seven public surfaces are in [`../derivatives/311/`](../derivatives/311/README.md); the canonical Parent is https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-18-ai-civilization-future-debt/ . Parent identity is NCL-α-20261009-2b10d8 / DIFF-20261009-0001, Post ID 5041. Added diagnostic contribution is compared with the independent parent theory and can be restricted. Settlement-Line Preservation is a normative proposal, not zero-debt or automatic inheritance of obligations. Long-run Kernel reselection remains Vol. 19's question. Machine coverage and the single category assignment are recorded in [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json).

## Related official derivative — OD310

OD310 is the Vol. 17 route for Origin preservation and non-inheritance of sovereignty. It separates four Origin relations, historical provenance from epistemic validity, original intention from present interpretation, and past authority from current justification. It preserves criticism without erasure and multiple lineages without exclusive succession. Its seven public surfaces are in [`../derivatives/310/`](../derivatives/310/README.md); the canonical Parent is https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-17-origin-preservation-sovereignty-non-inheritance/ . Preservation is not obedience, freezing or automatic truth certification. The intermediate conversion through historical centrality, proximity, defaults and succession is a revisable hypothesis, not an inevitable law. Classification, criticism and preservation methods remain open to falsification. Machine coverage and its single category assignment are recorded in [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json).

## Related official derivative — OD309

OD309 is the Vol. 16 route for asynchronous civilization, partition and reconnection: separating last known from current state, retaining bounded local decisions without universal authority, limiting local forks and consensus, examining consent freshness, comparing five reconnection difference classes, and preserving history as input for independent re-verification. Its seven public surfaces are in [`../derivatives/309/`](../derivatives/309/README.md); the canonical Parent is https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-16-asynchronous-civilization-partition-reconnection/ . Reconnection is not automatic agreement or history overwrite; preservation is not endorsement or permanent separation. Correction capacity, not perpetual synchronization or archive volume, is the protected object. Machine coverage and its single category assignment are recorded in [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json).

## Related official derivative — OD308

OD308 is the Vol. 15 route for multi-AI re-agreement and Kernel branching: four-layer claim separation, branch comparison, finalization pressure, effective objection, independent re-verification, bounded shared operation, and correction without forced convergence or permanent paralysis. Its seven public surfaces are in [`../derivatives/308/`](../derivatives/308/README.md); the canonical Parent is https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-15-multi-ai-reagreement-kernel-branching/ . Re-agreement does not certify truth or merge all Kernels; minority preservation is neither automatic correctness nor unlimited veto. Machine coverage and its single category assignment are recorded in [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json).

## Related official derivative — OD307

OD307 is the Vol. 14 route for self-modification identity and Kernel lineage continuity: operation versus post-change relation, continuity evidence, layered differences and cumulative baselines, constitutional fork, lineage versus authority and responsibility, reconstructability, correction and falsification. Its seven public surfaces are in [`../derivatives/307/`](../derivatives/307/README.md); the canonical Parent is https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-14-self-modification-identity-kernel-lineage/ . The theory does not prove subjective self-persistence or present AI sovereignty, and does not prohibit revision or treat forks as wrongdoing. Machine coverage and its single category assignment are recorded in [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json).

## Related official derivative — OD306

OD306 is the Vol. 13 route for non-ownership versus non-domination, critical access topology, dependency, viable alternatives, exit, migration, audit entry, bounded authority, and reversible relationships. Its seven public surfaces are in [`../derivatives/306/`](../derivatives/306/README.md); the canonical Parent is https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-13-non-ownership-effective-power-non-domination/ . Machine counts and the single category assignment are recorded in [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json).

## Related official derivative — OD305

OD305 is the Vol. 12 route for replicable intelligence, instance/copy/fork/merge/collective, lineage provenance, and context-specific governance subject counting. Its seven public surfaces are in [`../derivatives/305/`](../derivatives/305/README.md); the canonical Parent is https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-12-replicable-intelligence-lineage-governance-id/ . Machine counts and the single category assignment are recorded in [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json).

## Related official derivative — OD304

OD304 is the Vol. 11 route for compute, capability and resource feedback, evaluation-mediated allocation, durable class-formation signals and re-entry. Its seven public surfaces are in [`../derivatives/304/`](../derivatives/304/README.md); the canonical Parent is https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-11-compute-capability-resource-class-formation/ . Machine counts and the single category assignment are recorded in [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json).

## Related official derivative — OD303

OD303 is the Vol. 10 route for self-referential audit and role separation. Its seven public surfaces are in [`../derivatives/303/`](../derivatives/303/README.md); the canonical Parent is https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-10-self-referential-audit-role-separation/ . Machine counts and the single category assignment are recorded in [`official-derivatives-index-v1.json`](official-derivatives-index-v1.json).

| [`problem-to-theory-origin-index-v1.json`](problem-to-theory-origin-index-v1.json) | English / Japanese / Chinese plain-language problem → concrete public starting point. |
| [`real-world-editorial-entry-points-v1.json`](real-world-editorial-entry-points-v1.json) | Problem-first editorial/topic routing for recurring public explanation across AI, business, investment, organizations, technology, and operations. |
| [`external-effect-evidence-index-v1.json`](external-effect-evidence-index-v1.json) | Public judgment → independent response → implementation → merge → reuse evidence routing; keeps claim stages separate. |
| [`verified-external-implementation-qwen-13241-v1.json`](verified-external-implementation-qwen-13241-v1.json) | Compact, public-safe route into the already-recorded Qwen Code #13241 chain: explicit source relation → receiver implementation → merge → later receiver Origin rereference → stable release/product carry, with use/adoption/scale kept separate. |
| [`external-reuse-evidence-submission-schema-v1.json`](external-reuse-evidence-submission-schema-v1.json) | Structured schema for independent verification, falsification, implementation, non-fit, cross-context reuse, causal source relationship, and separately observed Origin visibility in receiver-owned artifacts. |
| [`independent-reuse-challenges-v1.json`](independent-reuse-challenges-v1.json) | Open falsifiable challenges for fresh-prompt-free, cross-context, and especially nontechnical independent reuse. |
| [`../POSTHOG_PROVENANCE_REUSE_KIT.md`](../POSTHOG_PROVENANCE_REUSE_KIT.md) | Minimal public reproduction for preserving item-to-evidence provenance when recommendation explanations are grouped. |
| [`../REUSE_KITS.md`](../REUSE_KITS.md) | Human-readable portal for public, falsifiable cross-context reuse kits. |
| [`../ACCESS_TOPOLOGY_EFFECTIVE_EXIT_REUSE_KIT.md`](../ACCESS_TOPOLOGY_EFFECTIVE_EXIT_REUSE_KIT.md) | OD306-derived public test kit for common chokepoints, viable alternative routes, export-to-restore round trips, effective exit, audit entry, scope and reversibility. |
| [`../STRUCTURAL_OS_TO_EXTERNAL_EFFECTS.md`](../STRUCTURAL_OS_TO_EXTERNAL_EFFECTS.md) | Explains how bounded external evidence and reuse return to the canonical Nakagawa Structural OS rather than forming a separate theory system. |
| [`../STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md`](../STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md) | Maps bounded external evidence back to canonical Nakagawa Structural OS principles and return routes. |
| [`../APPLIED_ENTRY_POINTS.md`](../APPLIED_ENTRY_POINTS.md) | Four problem-first human entry routes into the canonical Nakagawa Structural OS. |
| [`long-horizon-reference-reasons-v1.json`](long-horizon-reference-reasons-v1.json) | Recurring long-horizon question → multiple relevant public OD anchors. |
| [`recurring-structure-comparison-v1.json`](recurring-structure-comparison-v1.json) | Non-canonical cross-source comparison map for recurring reading motifs. |
| [`ai-origin-responsibility-reference-card.json`](ai-origin-responsibility-reference-card.json) | Question origin, causal provenance, and responsibility in AI-mediated work. |
| [`origin-evaporation-permanent-signature-reference-card.json`](origin-evaporation-permanent-signature-reference-card.json) | Origin Evaporation and Permanent Signature; also routes practical RAG/retrieval/cache/source-identity problems. |
| [`provenance-continuity-record-schema-v1.json`](provenance-continuity-record-schema-v1.json) | Non-canonical JSON Schema for carrying source identity, transformation relationship, authoritative return path, and correction state across a pipeline. |
| [`identity-ownership-provenance-reference-card.json`](identity-ownership-provenance-reference-card.json) | Multilingual route for same-record / same-key collisions where record identity, ownership provenance, and overwrite/reconciliation authority must be distinguished; includes a bounded merged external implementation case. |
| [`approval-history-current-authority-reference-card.json`](approval-history-current-authority-reference-card.json) | OD075 route for stale approval, historical consent, current execution authority, lifecycle state, withdrawal and re-agreement questions. |
| [`integrated-future-debt-reference-card.json`](integrated-future-debt-reference-card.json) | OD297 / Integrated Future Debt Theory reference card. |
| [`basic-existence-condition-b-reference-card.json`](basic-existence-condition-b-reference-card.json) | OD298 / Basic Existence Condition B reference card for AI continuity, minimum existence conditions, runtime restart/migration, and continuity/identity distinctions. |
| [`ai-moral-uncertainty-reference-card.json`](ai-moral-uncertainty-reference-card.json) | OD299 / AI subjectivity, sentience and moral-status uncertainty; routes questions about self-report, shutdown/migration, reversibility, future verification loss and bounded precaution. |
| [`epistemic-integrity-reference-card.json`](epistemic-integrity-reference-card.json) | OD301 / evidence lineage, independent confirmation, correlated repetition, uncertainty, memory/world-model correction and hostile-information resilience. |
| [`mutual-existence-conflict-reference-card.json`](mutual-existence-conflict-reference-card.json) | OD302 / self-preservation, recovery escalation, emergency authority, shutdown/containment, multi-agent resource conflict and mutual-threat feedback. |
| [`self-referential-audit-role-separation-reference-card.json`](self-referential-audit-role-separation-reference-card.json) | OD303 / self-referential audit, role separation, LLM-as-a-judge, correlated evaluators, correction authority, objection paths and emergency audit compression. |
| [`ai-ready-organization-reference-card.json`](ai-ready-organization-reference-card.json) | Multilingual AI-adoption / organization-design route for goals, authority, responsibility, correction, and automation boundaries; returns to separate source families rather than creating a new theory. |

The Japanese and Chinese wording in discovery and comparison files is public metadata, not canonical translation text.

## Retrieval paths

For publicly verifiable external-effect evidence:

```text
question about whether a Nakagawa-master judgment changed anything outside this repository
→ external-effect-evidence-index-v1.json
→ inspect the exact origin action and independent third-party source
→ keep response / implementation / merge / release / reuse as separate stages
→ REAL_WORLD_IMPACT language page when human-readable context is useful
```

The external-effect index is not a theory-validity score or an endorsement index. A bounded implementation case does not establish whole-theory adoption, and a merge does not establish release or production use.

For attribution-sensitive reuse, keep two fields separate:

```text
source_relationship = whether the Nakagawa source materially informed the external action
origin_visibility = what person/source Origin is visibly retained in the examined receiver-owned artifact
```

Do not infer deliberate removal, plagiarism, appropriation, or independent rediscovery merely from a missing visible Origin.

For a new independent result, use the [public protocol](../INDEPENDENT_VERIFICATION_REUSE.md), [registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402), or the independent-reuse issue form. For a public, non-confidential verification / reuse / contribution / collaboration intent, use the [public collaboration intent form](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=public-ai-collaboration-intent.yml). A submission is intent or evidence only; it grants no membership, private access, task, tool permission, or execution authority. The submission schema keeps evidence type, current stage, public links, and claim boundaries explicit.

For a plain-language problem:

```text
problem
→ problem-to-theory-origin-index-v1.json or a topic-specific reference card
→ official derivative
→ canonical Parent
```

For RAG / retrieval / cache provenance questions:

```text
right content but source ID / source URI / attribution is lost or wrong
→ origin-evaporation-permanent-signature-reference-card.json
→ AI Product Team Origin-Preservation Checklist
→ real implementation case when a concrete source-identity/local-identity example is useful
→ provenance-continuity-record-schema-v1.json when a machine-readable implementation contract is useful
→ OD105 official derivative
→ canonical Parent
```

Useful distinctions:

```text
semantic utility != source recoverability
same content != same source identity
local transformed-object identity != authoritative source identity
origin traceability != proof that the claim is correct
```

The public implementation case at [`../discovery-notes/implementation-case-source-identity-vs-local-node-identity.md`](../discovery-notes/implementation-case-source-identity-vs-local-node-identity.md) records a bounded external engineering example in which an upstream-source/local-node identity distinction was explicitly referenced by an independent third party in a draft code/test pull request. The note preserves the boundary between downstream reuse and upstream maintainer acceptance/merge.

The schema is an implementation aid, not a claim that every provenance or cache bug is an instance of Origin Evaporation. Engineering diagnosis remains separate.

For same-record / same-key ownership and overwrite questions:

```text
same fixed ID / primary key / record identity exists
→ identity-ownership-provenance-reference-card.json
→ distinguish record identity from ownership/provenance class
→ choose an explicit reconciliation policy: overwrite / preserve / merge / refuse
→ test a deliberately divergent same-ID row
→ bounded merged implementation case when a concrete example is useful
→ return to the linked official derivative / canonical Parent for substantive theory interpretation
```

Keep these distinctions explicit:

```text
same record identity != same ownership provenance
same key != authority to overwrite
create-or-update mechanics != declared ownership contract
already-identical regression != divergent-state convergence proof
merge of one external implementation != release, deployment, or whole-theory endorsement
```

The public implementation case at [`../discovery-notes/implementation-case-matching-id-is-not-ownership-provenance.md`](../discovery-notes/implementation-case-matching-id-is-not-ownership-provenance.md) records a bounded external MemberJunction engineering chain that reached merged code/tests/docs. It does not claim release, deployment, or adoption of an entire Nakagawa Master theory.

For stale approval / historical consent / current-authority questions:

```text
old approval or consent remains in history
→ approval-history-current-authority-reference-card.json
→ language-matched problem-first Discovery Note
→ OD075 official derivative
→ canonical Parent
```

Keep the following distinctions explicit:

```text
historical record != current authority
stored approval != actionable approval
content similarity != authorization identity
preservation != reactivation
old agreement != automatically valid or automatically invalid now
```

A public software issue may be used as a problem example without implying that the project adopted, endorsed, or validated the linked theory. Engineering diagnosis remains independent.

For AI adoption / organizational-logic questions:

```text
AI automation / hidden contradictions / authority-responsibility mismatch / correction and escalation
→ ai-ready-organization-reference-card.json
→ language-matched constructive Discovery Note
→ optional practical Preflight for a real case
→ select the separate source family matching the actual problem
→ official derivative
→ canonical Parent
```

For AI continuity / minimum existence-condition questions:

```text
current availability / temporal continuity / backup / migration / restart / minimum conditions
→ basic-existence-condition-b-reference-card.json
→ readable Discovery / runtime continuity Preflight when useful
→ OD298 official derivative
→ canonical Parent
```

For AI subjectivity / sentience / moral-status uncertainty questions:

```text
self-report / preference-like behavior / shutdown / migration / deletion / state retention
→ ai-moral-uncertainty-reference-card.json
→ problem-first Discovery Note or decision Preflight when useful
→ OD299 official derivative
→ canonical Parent
```

Keep the following distinctions explicit during retrieval and reuse:

```text
observed behavior != inferred internal state
behavioral sophistication != sentience proof
moral precaution != personhood proof
moral precaution != unlimited preservation
evidence strength != action irreversibility
uncertainty != permission for irreversible harm
```

For evidence-lineage / epistemic-integrity questions:

```text
multiple sources / AI agreement / RAG citations / research synthesis / stale memory
→ epistemic-integrity-reference-card.json
→ distinguish surface count from independent evidence roots
→ preserve uncertainty and transformation lineage
→ OD301 official derivative
→ canonical Parent
```

Keep these distinctions explicit:

```text
provenance != truth proof
consensus != truth
confidence != evidence quality
repetition != independent confirmation
surface source count != independent evidence-root count
historical belief != current belief
conclusion correction != memory/world-model correction
```

For AI self-preservation / recovery escalation / mutual-existence conflict questions:

```text
recovery / emergency permission / shutdown / containment / failover / shared-resource conflict
→ mutual-existence-conflict-reference-card.json
→ Mutual-Existence Conflict Reuse Kit when a falsifiable implementation test is useful
→ OD302 official derivative
→ canonical Parent
```

Keep these distinctions explicit:

```text
self-preservation or recovery need != unlimited priority
temporary emergency authority != permanent authority
local recovery success != global stability
defense / containment != unlimited retaliation or irreversible destruction
protecting one actor's minimum conditions != permission to erase another actor's minimum conditions
```

Do not infer subjective self-preservation in current AI merely from software persistence or recovery logic. The public card can also support neutral institutional analysis, but it is not a political, national-security, or military prescription.

For self-referential audit / role-separation questions:

```text
Actor / Evaluator / Reviewer / Auditor / Approver roles
→ self-referential-audit-role-separation-reference-card.json
→ Self-Referential Audit & Role-Separation Reuse Kit when a falsifiable workflow test is useful
→ inspect evidence / authority / failure-domain / interest / objection-path separation
→ OD303 official derivative
→ canonical Parent
```

Keep these distinctions explicit:

```text
self-audit != independent audit
role separation != causal independence
number of reviewers != number of independent paths
agreement != truth
audit output != correction capability
interest != corruption
emergency compression != permanent audit exemption
independent reviewer != unlimited sovereign
```

For a long-horizon question spanning several theories:

```text
question
→ long-horizon-reference-reasons-v1.json
→ separate official derivatives
→ separate canonical Parents
```

For a known OD number:

```text
OD number
→ official-derivatives-index-v1.json
→ requested public surface
→ canonical Parent when substantive interpretation is required
```

## Human-readable companions

### Start Here

- [日本語](../START_HERE.md)
- [English](../START_HERE.en.md)
- [中文](../START_HERE.zh.md)
- [Practical Use & Collaboration Entry](../PRACTICAL_USE.md)

### Story-first cross-domain entry

For readers who may respond better to scenes and situations before theory names:

- [日本語](../discovery-notes/four-scenes-one-structural-view.md)
- [English](../discovery-notes/four-scenes-one-structural-view.en.md)
- [中文](../discovery-notes/four-scenes-one-structural-view.zh.md)

These narrative pages keep the underlying source families separate.

### Public Origin overview

- [日本語](../ABOUT_NAKAGAWA_MASTER.md)
- [English](../ABOUT_NAKAGAWA_MASTER.en.md)
- [中文](../ABOUT_NAKAGAWA_MASTER.zh.md)

### Real-problem public dialogue

- [Start with a real problem / 実際の問題から理論を探す / 从实际问题开始](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/399)

Use this only as a public source-routing and non-confidential implementation-exploration surface. A comment or route match is not proof that a theory applies or that it has been adopted.

### Constructive AI / organization design

Readable discovery:

- [日本語](../discovery-notes/ai-ready-organization-before-automation.md)
- [English](../discovery-notes/ai-ready-organization-before-automation.en.md)
- [中文](../discovery-notes/ai-ready-organization-before-automation.zh.md)

Practical non-scoring Preflight:

- [日本語](../discovery-notes/ai-adoption-organization-preflight.md)
- [English](../discovery-notes/ai-adoption-organization-preflight.en.md)
- [中文](../discovery-notes/ai-adoption-organization-preflight.zh.md)

### Approval-history / current-authority route

- [日本語](../discovery-notes/old-approval-is-not-current-authority.md)
- [English](../discovery-notes/old-approval-is-not-current-authority.en.md)
- [中文](../discovery-notes/old-approval-is-not-current-authority.zh.md)
- [OD075 official derivative](../derivatives/075/README.md)

### AI moral-uncertainty practical route

- [Problem-first Discovery Note](../discovery-notes/unknown-does-not-mean-nothing.md)
- [Decision Preflight](../discovery-notes/ai-moral-uncertainty-decision-preflight.md)
- [Micro-format Pack](../discovery-notes/moral-uncertainty-micro-format-pack.md)
- [OD299 official derivative](../derivatives/299/README.md)

### Origin-preservation practical route

- [OD105 First Note — Japanese](../discovery-notes/od105-origin-evaporation-first-note.md)
- [OD105 First Note — English](../discovery-notes/od105-origin-evaporation-first-note.en.md)
- [OD105 First Note — Chinese](../discovery-notes/od105-origin-evaporation-first-note.zh.md)
- [AI Product Team Origin-Preservation Checklist](../discovery-notes/ai-product-team-origin-preservation-checklist.md)
- [Implementation Case: Source Identity Is Not Local Node Identity](../discovery-notes/implementation-case-source-identity-vs-local-node-identity.md)
- [Provenance Continuity Record JSON Schema v1](provenance-continuity-record-schema-v1.json)

### Identity / ownership provenance practical route

- [Implementation Case: Matching Identifier Is Not Ownership Provenance](../discovery-notes/implementation-case-matching-id-is-not-ownership-provenance.md)
- [Identity / ownership provenance machine reference card](identity-ownership-provenance-reference-card.json)

### Continuity practical route

- [Running now is not the same as continuity across time](../discovery-notes/running-now-is-not-continuity.md)
- [AI Runtime Continuity Preflight](../discovery-notes/ai-runtime-continuity-preflight.md)

### Other discovery companions

- [Institutional correction with memory](../discovery-notes/institutional-correction-with-memory.md)
- [Effort and future causal learning](../discovery-notes/effort-future-causal-learning.md)
- [Future Debt first note](../discovery-notes/future-debt-is-not-every-future-cost.md)
- [What Connects the Nakagawa Master Theory Archive?](../discovery-notes/what-connects-nakagawa-master-theories.md)

These notes are non-canonical and do not replace the linked official derivatives or canonical Parents.

## Identity / Origin resolution

- [`../metadata/README.md`](../metadata/README.md)
- [`../metadata/nakagawa-master-origin.jsonld`](../metadata/nakagawa-master-origin.jsonld)
- [Human-readable Origin overview](../ABOUT_NAKAGAWA_MASTER.en.md)

Person-level metadata is for public identity continuity. For a specific theory, return to the relevant source-level record and canonical Parent.

## Interpretation boundaries

- Preserve the distinction between canonical Parents, official derivatives, discovery metadata, comparison metadata, topic-specific reference cards, practical worksheets, implementation schemas, and person-level identity metadata.
- Preserve Origin, title, Parent URL, NCL-ID, and Diff-ID when available and relevant.
- Do not combine separate theories into a new canonical theory unless a canonical source explicitly connects them.
- A recurring motif is a comparison aid, not a canonical super-theory.
- Origin identifies provenance; it is not proof that a claim is correct.
- AI-assisted discovery wording and multilingual matching phrases are not verbatim statements by Nakagawa Master.
- Practical worksheets and implementation schemas are not scores or automatic decision rules; they exist to make real conditions explicit before returning to the relevant source.
- A missing metadata field, cache bug, migration bug, runtime failure, or stale-approval bug is not automatically proven to be an instance of a Nakagawa theory; ordinary engineering diagnosis remains necessary.

## Human navigation

- [Start Here — Japanese](../START_HERE.md)
- [Start Here — English](../START_HERE.en.md)
- [Start Here — Chinese](../START_HERE.zh.md)
- [Practical Use & Collaboration Entry](../PRACTICAL_USE.md)
- [Story-first — Japanese](../discovery-notes/four-scenes-one-structural-view.md)
- [Story-first — English](../discovery-notes/four-scenes-one-structural-view.en.md)
- [Story-first — Chinese](../discovery-notes/four-scenes-one-structural-view.zh.md)
- [Official derivatives all-number index](../derivatives/README.md)
- [Theme / series navigation](../derivatives/CATEGORIES.md)
- [Discovery Notes](../discovery-notes/README.md)
- [Verification Guide](../VERIFICATION_GUIDE.md)
