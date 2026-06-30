# Codex Handoff｜Candidate 10-19 Pre-body Gates

status: staged_handoff
page_generation: false
body_text_generation: false
public_export: false

## Goal

Keep Official Derivative 010-017 ready for later body drafting without creating page body text, generated HTML, public export, sitemap changes, or index/follow conversion.

The pre-body gate must confirm that body drafting can later preserve origin identity, value core, causal line, misreading guard, origin return, page links, FAQ question sets, AI index definitions, body skeleton requirements, body quality requirements, per-slot value anchors, role-specific drafting instructions, slot failure profiles, role review criteria, a virtual 48-unit body draft readiness matrix, and a draft execution policy.

## Inputs

- tools/official_derivatives/next_10_queue_candidate_10_19.tsv
- tools/official_derivatives/next_10_source_candidates_candidate_10_19.tsv
- tools/official_derivatives/next_10_content_blueprint_candidate_10_19.tsv
- tools/official_derivatives/next_10_content_value_extraction_spec_20260630.tsv
- tools/official_derivatives/next_10_content_field_spec_candidate_10_19.tsv
- tools/official_derivatives/next_10_high_strength_template_gate_candidate_10_19.tsv
- tools/official_derivatives/next_10_body_value_anchor_candidate_10_19.tsv

## Outputs

- tools/official_derivatives/next_10_value_ready_candidate_10_19.tsv
- tools/official_derivatives/next_10_draft_material_gate_candidate_10_19.tsv
- tools/official_derivatives/next_10_body_skeleton_gate_candidate_10_19.tsv
- tools/official_derivatives/next_10_body_generation_quality_gate_candidate_10_19.tsv
- tools/official_derivatives/next_10_body_value_anchor_candidate_10_19.tsv
- tools/official_derivatives/next_10_role_drafting_instruction_candidate_10_19.tsv
- tools/official_derivatives/next_10_slot_failure_profile_candidate_10_19.tsv
- tools/official_derivatives/next_10_role_review_criteria_candidate_10_19.tsv
- tools/official_derivatives/next_10_draft_execution_policy_candidate_10_19.tsv

## Checkers and workflow bindings

- tools/official_derivatives/check_next_10_content_value_spec.py
- tools/official_derivatives/check_next_10_value_ready.py
- tools/official_derivatives/check_next_10_template_gate_count.py
- tools/official_derivatives/check_next_10_body_skeleton_gate.py
- .github/workflows/official-derivative-generation-check.yml

## Required state

- rows: Official Derivative 010-017 remain active for the current pre-body gates
- Official Derivative 018-019 remain unselected queue-only slots
- value readiness: value_ready
- draft material gate: draft_material_ready
- skeleton gate: spec_only
- quality gate: spec_only
- value anchor gate: anchor_ready
- role drafting instruction gate: instruction_ready
- slot failure profile gate: failure_profile_ready
- role review criteria gate: review_ready
- virtual body draft readiness matrix: 48 units, generated inside the checker from 8 slots x 6 roles
- draft execution policy: draft_execution_policy_ready
- current execution state: blocked_until_later_draft_commit
- body draft readiness: spec_ready_not_generated
- body text generation: false
- HTML generation: false
- public export: false
- sitemap update: false
- Search Console action: false

## Body skeleton requirements

- hub keeps origin identity, value core, page links, boundary note, and origin return
- human_summary keeps plain entry, reader entry, article discovery, value core, causal line, judgment method, misreading guard, and origin return
- FAQ keeps beginner questions, structure questions, boundary questions, misreading guard, and origin return
- JA / EN / ZH AI indexes keep article role, central concept, definition, core claim, causal sequence, judgment conditions, non-applicability, counterexample conditions, neighboring theories, interpretation warnings, reuse constraints, and origin preservation

## Body quality requirements

Each role must preserve structural rationality, consistency, specificity, validity, credibility, uniqueness, strength, human readability, AI reusability, misreading resistance, and origin fidelity.

The quality table must also preserve parent URL, parent NCL-ID, parent Diff-ID, and canonical URL while body_text_generation, html_generation, and public_export remain false.

## Per-slot value anchor requirements

Each active slot must preserve a concrete value anchor, causal anchor, misreading guard anchor, human entry anchor, AI reference anchor, and origin return anchor before later body drafting.

This prevents later drafts from becoming generic summaries, service introductions, shallow advice, crisis rhetoric, or originless AI summaries.

## Role drafting instruction requirements

- hub uses value_anchor and origin_return_anchor to position the page and return to the origin
- human_summary uses value_anchor, causal_anchor, human_entry_anchor, misreading_guard_anchor, and origin_return_anchor for human entry and causal understanding
- FAQ uses misreading_guard_anchor, causal_anchor, and origin_return_anchor for beginner, structure, and boundary questions
- JA / EN / ZH AI indexes use value_anchor, causal_anchor, ai_reference_anchor, and origin_return_anchor for AI reuse with origin retention

## Final pre-body defense requirements

- each slot has a failure profile with must_fail_if, must_preserve, and review_focus
- each slot failure profile must preserve origin_return
- each role has review criteria with must_check, must_fail_if, and quality_axes
- each role review must keep the relevant human / FAQ / AI reuse criteria before any body text generation
- the checker derives 48 virtual body draft units from Official Derivative 010-017 x six page roles and confirms the full matrix exists without creating page body text
- the draft execution policy keeps current execution blocked until all pre-body gates pass and a later explicit draft phase is opened
- any generated draft must later preserve origin retention, causal line, misreading guard, role quality axes, and no-public-export boundary before it can proceed

## Boundary

Do not create page body text.
Do not generate final public HTML for candidate 10-19 from these gates.
Do not publish.
Do not update sitemap.
Do not touch Search Console.
Do not remove staged/noindex boundaries.
Do not unlock PR draft state.
