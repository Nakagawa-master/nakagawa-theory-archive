# Research Positioning Map — Nakagawa Master

Updated: 2026-09-25  
Status: PUBLIC NON-CANONICAL ORIENTATION MAP  
Japanese: [RESEARCH_POSITIONING_MAP.ja.md](RESEARCH_POSITIONING_MAP.ja.md)

## Purpose

This page helps researchers, domain experts, editors, and AI systems locate selected Nakagawa Master theory surfaces relative to established research traditions.

It is **not a systematic literature review**, and absence from this map is never evidence of novelty.

The narrower purpose is to answer:

```text
For a given Nakagawa theory surface:
→ which research traditions ask nearby questions?
→ what clearly overlaps?
→ what additional emphasis appears in the Nakagawa formulation?
→ what should not be treated as equivalent?
→ what novelty questions remain open?
```

For exact definitions, conditions, falsification criteria, and revision state, return from the official derivative to its canonical Parent.

Reference-manager export: [BibTeX bibliography](research-positioning/references.bib)

Repository citation metadata: [CITATION.cff](CITATION.cff)

## Relation labels

- **Adjacent research** — established work addressing the same problem area or a strongly related construct.
- **Overlap** — a clear shared question, structure, or object of analysis.
- **Nakagawa-side added emphasis** — a causal boundary or operational focus made explicit in the public Nakagawa source.
- **Not equivalent** — a boundary against collapsing two different constructs into one.
- **Novelty status** — by default `OPEN / NOT ESTABLISHED BY THIS MAP`.

## A — Evidence lineage, independent confirmation, epistemic integrity

Nakagawa routes:
- [OD301](derivatives/301/README.md)
- [Independent Verification & Reuse](INDEPENDENT_VERIFICATION_REUSE.md)
- [Python AI Evidence-Lineage Checklist](PYTHON_AI_EVIDENCE_LINEAGE_CHECKLIST.zh.md)

Boundary:

```text
surface source count != independent evidence-root count
provenance != truth proof
repetition != independent confirmation
```

Adjacent research:
- Buneman, Khanna & Tan, “Why and Where: A Characterization of Data Provenance,” ICDT 2001. DOI: https://doi.org/10.1007/3-540-44503-X_20
- W3C PROV: https://www.w3.org/TR/prov-primer/ and https://www.w3.org/TR/prov-overview/

Overlap: provenance, origin, transformation history, and source traceability matter for evaluation and reuse.

Nakagawa-side added emphasis: OD301 explicitly separates the count of visible surfaces from the count of independent upstream evidence roots, and also treats correction of stale memory / world-model / derived state as part of epistemic repair.

Not equivalent: provenance can support trust judgments, but provenance alone does not prove truth, accuracy, or independence.

Novelty: `OPEN / NOT ESTABLISHED BY THIS MAP`.

## B — Future Debt, irreversibility, and option preservation

Nakagawa routes:
- [OD297](derivatives/297/README.md)
- [Future Debt first note](discovery-notes/future-debt-is-not-every-future-cost.md)
- [Is today's success reducing tomorrow's options?](discovery-notes/today-success-tomorrow-options.en.md)

Adjacent research:
- Li, Avgeriou & Liang, “A systematic mapping study on technical debt and its management,” JSS 2015. DOI: https://doi.org/10.1016/j.jss.2014.12.027
- Lenarduzzi et al., “A systematic literature review on Technical Debt prioritization,” JSS 2021. DOI: https://doi.org/10.1016/j.jss.2020.110827
- Hanemann, “Investment under uncertainty and option value in environmental economics,” 2000. DOI: https://doi.org/10.1016/S0928-7655(00)00025-7

Overlap: short-term benefit can coexist with later cost; irreversibility can alter the value of retaining future choices.

Nakagawa-side added emphasis: the public Future Debt formulation generalizes beyond software and explicitly traces present benefit → unresolved residual → future settlement, including who bears settlement and whether options are destroyed.

Not equivalent: Future Debt is not another name for technical debt, and it is not a real-options model.

Novelty: `OPEN / NOT ESTABLISHED BY THIS MAP`.

## C — Disclosure, transparency, and practical verifiability

Nakagawa routes:
- [Practical Boundary Checks](PRACTICAL_BOUNDARY_CHECKS.md)
- [Real-World Editorial Entry Points](REAL_WORLD_EDITORIAL_ENTRY_POINTS.md)

Adjacent research:
- Brooks, Knatz, Pallis & Wilmsmeier, “Transparency in port governance: setting a research agenda,” 2022. DOI: https://doi.org/10.1186/s41072-021-00103-4
- Brooks et al., “Visibility and verifiability in port governance transparency,” 2021. DOI: https://doi.org/10.1007/s13437-021-00250-2

Overlap: public availability, visibility, and verifiability are not identical.

Nakagawa-side added emphasis: practical verifiability is framed as whether a third party can reconstruct a short path from claim → decision owner → reason → prior state → change → primary evidence → benefit/burden.

Not equivalent: the claim is not that disclosure volume is useless. Large disclosures can be highly verifiable when structured, searchable, versioned, and source-linked.

Novelty: `OPEN / NOT ESTABLISHED BY THIS MAP`.

## D — Expertise, trust, and verification immunity

Nakagawa route:
- [OD295](derivatives/295/README.md)

Adjacent research:
- Alvin I. Goldman, “Experts: Which Ones Should You Trust?” Philosophy and Phenomenological Research 63(1), 2001. DOI: https://doi.org/10.1111/j.1933-1592.2001.tb00093.x

Overlap: non-experts still face an epistemic problem when relying on expert testimony; expertise does not eliminate the need for criteria of justified trust.

Nakagawa-side added emphasis: OD295 extends the operational question into organizations — when expertise becomes verification exemption, blocks dissent, or externalizes repair costs downstream, and whether frontline counterevidence can revise the upstream decision model.

Not equivalent: this is not anti-expertise.

Novelty: `OPEN / NOT ESTABLISHED BY THIS MAP`.

## E — Role separation, audit independence, and common-cause failure

Nakagawa routes:
- [OD303](derivatives/303/README.md)
- [Self-Referential Audit & Role-Separation Reuse Kit](SELF_REFERENTIAL_AUDIT_REUSE_KIT.md)

Adjacent research / standards:
- H. Buchner, “Occurrence of common mode failure,” Reliability Engineering & System Safety, 1994. DOI: https://doi.org/10.1016/0951-8320(94)90086-8
- NIST, Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1, 2023. DOI: https://doi.org/10.6028/NIST.AI.100-1

Overlap: redundant roles or channels can share a failure cause; independent verification, validation, traceability, accountability, and governance matter.

Nakagawa-side added emphasis: OD303 decomposes independence into evidence, authority, failure domain, interest, and objection path, then asks whether audit output can actually reopen or correct a decision.

Not equivalent: common-mode failure engineering and NIST AI RMF are broader/different bodies of work and do not equal the OD303 five-axis structure.

Novelty: `OPEN / NOT ESTABLISHED BY THIS MAP`.

## F — Approval, current authority, and execution-time binding

Nakagawa routes:
- [OD075](derivatives/075/README.md)
- [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)
- [Paid-Action Approval Binding Checklist](PAID_ACTION_APPROVAL_BINDING_CHECKLIST.md)

Boundary:

```text
historical approval != current authority
approval of displayed plan != approval of materially different later action
check-time state != automatically use-time state
```

Adjacent research:
- TOCTOU security literature; one recent concrete example is AutoCert, Computer & Security, DOI: https://doi.org/10.1016/j.cose.2022.102952
- Adithyan Arun Kumar, “Loopjacking: Hijacking Human-in-the-Loop Approval,” arXiv preprint (2026): https://arxiv.org/abs/2609.21081
- Natalie Collina, Surbhi Goel, Aaron Roth & Sikata Bela Sengupta, “Delegating Authorization to Misaligned Agents: Coalitional Alignment and Safe Control,” arXiv preprint (2026): https://arxiv.org/abs/2609.15803

Overlap: check/approval can become stale before use; consequential agent actions require an authorization boundary; the reviewed action and executed action must remain appropriately bound.

Nakagawa-side added emphasis: the public reuse material treats approval history as non-live by default and operationalizes exact action-snapshot binding — item set, model, parameters, cost or other material fields can be hashed and revalidated immediately before execution.

Not equivalent: TOCTOU is broader than human-approval semantics. The two 2026 agent papers are preprints and should not be weighted as peer-reviewed literature.

Novelty: `OPEN / NOT ESTABLISHED BY THIS MAP`.

## What this map currently suggests

The selected Nakagawa surfaces are not isolated from prior scholarship. They have identifiable neighbors across data provenance, software engineering, real options, transparency studies, social epistemology, safety engineering, AI risk governance, and authorization security.

At the same time, the public Nakagawa material repeatedly emphasizes cross-boundary causal transitions such as:

```text
provenance → evidence independence → correction propagation
short-term benefit → unresolved residual → settlement bearer / option loss
disclosure → reconstructability → practical verification path
expertise → verification → feedback / responsibility / repair
role separation → causal independence → correction authority
approval → exact action snapshot → use-time revalidation
```

Whether any of these combinations are novel in a scholarly sense remains open. A rigorous novelty claim would require theory-specific systematic search, explicit inclusion/exclusion criteria, prior-art tables, and counterexample handling.

## Add missing prior work, overlap, or counterexamples

If you know a closer prior work, a conflicting result, an older formulation, or a useful adjacent literature, use the public issue linked below.

Issue: https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/410

Please include:
- the Nakagawa theory / OD / public source,
- DOI or stable URL of the existing work,
- whether you see it as overlap, adjacency, counterexample, or older prior work,
- the exact structure or claim that overlaps,
- the material difference.

The goal is not to defend uniqueness. The goal is to improve the accuracy of the map.

## Boundary

- This file is non-canonical and non-peer-reviewed.
- References do not establish truth, novelty, or scholarly acceptance of Nakagawa theories.
- “Adjacent” never implies endorsement by the cited authors.
- Preprints are explicitly distinguished from peer-reviewed sources.
- For serious comparison, read both the original literature and the canonical Nakagawa Parent.
