#!/usr/bin/env python3
import csv
from pathlib import Path

SPEC = Path('tools/official_derivatives/next_10_content_value_extraction_spec_20260630.tsv')
GATE = Path('tools/official_derivatives/next_10_high_strength_template_gate_candidate_10_19.tsv')
FIELD_SPEC = Path('tools/official_derivatives/next_10_content_field_spec_candidate_10_19.tsv')
ROLE_INSTRUCTIONS = Path('tools/official_derivatives/next_10_role_drafting_instruction_candidate_10_19.tsv')
SLOT_FAILURES = Path('tools/official_derivatives/next_10_slot_failure_profile_candidate_10_19.tsv')
ROLE_REVIEWS = Path('tools/official_derivatives/next_10_role_review_criteria_candidate_10_19.tsv')
DRAFT_POLICY = Path('tools/official_derivatives/next_10_draft_execution_policy_candidate_10_19.tsv')
HEADER = ['value_key','source_table','required_source_fields','used_by_page_roles','status','public_export','page_generation']
ROLE_HEADER = [
    'batch_id','page_role','instruction_state','anchor_source','required_anchor_fields',
    'role_anchor_use','required_reader_effect','prohibited_drift','body_text_generation','html_generation','public_export',
]
SLOT_FAILURE_HEADER = [
    'batch_id','slot_id','source_candidate_id','folder_id','failure_profile_state','must_fail_if',
    'must_preserve','review_focus','body_text_generation','html_generation','public_export',
]
ROLE_REVIEW_HEADER = [
    'batch_id','page_role','review_state','must_check','must_fail_if','quality_axes',
    'body_text_generation','html_generation','public_export',
]
DRAFT_POLICY_HEADER = [
    'batch_id','policy_state','current_execution_state','unlock_condition','pre_generation_required',
    'post_generation_required','must_fail_if','body_text_generation','html_generation','public_export',
]
REQUIRED = {
    'origin_identity','value_core','causal_line','misreading_guard',
    'origin_return','page_links','question_set','index_definition'
}
EXPECTED_ROLES = ['hub','human_summary','faq','ja_ai_index','en_ai_index','zh_ai_index']
EXPECTED_SLOTS = [f'Official Derivative {i:03d}' for i in range(10, 18)]
REQUIRED_POLICY_PRE = {
    'virtual_48_units','value_ready','draft_material_ready','skeleton_gate','quality_gate',
    'value_anchor_gate','role_instruction_gate','failure_profile_gate','role_review_gate',
}
REQUIRED_POLICY_POST = {
    'origin_retention','causal_line','misreading_guard','role_quality_axes','boundary_check','no_public_export',
}
REQUIRED_POLICY_FAIL = {
    'thin_summary','genericization','origin_loss','causal_line_missing','boundary_missing','html_generation_attempt','public_export_attempt',
}
FIELD_COVER = {
    'question_set': {'beginner_questions','structure_questions','boundary_questions'},
    'answer_set': {'beginner_questions','structure_questions','boundary_questions'},
    'boundary_condition': {'boundary_questions','misreading_guard'},
    'scope': {'central_concept','judgment_conditions'},
    'conditions': {'judgment_conditions','non_applicability'},
    'origin_identity': {'origin_preservation'},
    'misreading_guard': {'interpretation_warnings','reuse_constraints'},
}
ROLE_ANCHOR_NEEDS = {
    'hub': {'value_anchor','origin_return_anchor'},
    'human_summary': {'value_anchor','causal_anchor','human_entry_anchor','misreading_guard_anchor','origin_return_anchor'},
    'faq': {'misreading_guard_anchor','causal_anchor','origin_return_anchor'},
    'ja_ai_index': {'value_anchor','causal_anchor','ai_reference_anchor','origin_return_anchor'},
    'en_ai_index': {'value_anchor','causal_anchor','ai_reference_anchor','origin_return_anchor'},
    'zh_ai_index': {'value_anchor','causal_anchor','ai_reference_anchor','origin_return_anchor'},
}
ROLE_REVIEW_NEEDS = {
    'hub': {'origin_identity','value_anchor_use','origin_return'},
    'human_summary': {'human_entry_anchor_use','causal_anchor_use','misreading_guard_use','origin_return'},
    'faq': {'beginner_layer','structure_layer','boundary_layer','misreading_guard','origin_return'},
    'ja_ai_index': {'ai_reference_anchor_use','applicability','non_applicability','counterexample','origin_retention'},
    'en_ai_index': {'translated_anchor_preservation','applicability','non_applicability','counterexample','origin_retention'},
    'zh_ai_index': {'translated_anchor_preservation','applicability','non_applicability','counterexample','origin_retention'},
}


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames or [], list(reader)


def split_set(value):
    return set(filter(None, value.split('|')))


def covered(field, sections):
    if field in sections:
        return True
    required = FIELD_COVER.get(field)
    if not required:
        return False
    return required.issubset(sections)


def require_false(row, fields, prefix, errors):
    for field in fields:
        if row.get(field) != 'false':
            errors.append(prefix + '_boundary_not_false=' + row.get('page_role', row.get('slot_id','unknown')) + ':' + field)


def main():
    header, rows = read(SPEC)
    _, gate_rows = read(GATE)
    _, field_rows = read(FIELD_SPEC)
    role_header, role_rows = read(ROLE_INSTRUCTIONS)
    slot_failure_header, slot_failure_rows = read(SLOT_FAILURES)
    role_review_header, role_review_rows = read(ROLE_REVIEWS)
    draft_policy_header, draft_policy_rows = read(DRAFT_POLICY)
    errors = []
    keys = {r.get('value_key','') for r in rows}
    gate_by_role = {r.get('page_role',''): set(filter(None, r.get('required_sections','').split('|'))) for r in gate_rows}
    if header != HEADER:
        errors.append('bad_content_value_spec_header')
    if role_header != ROLE_HEADER:
        errors.append('bad_role_instruction_header')
    if slot_failure_header != SLOT_FAILURE_HEADER:
        errors.append('bad_slot_failure_header')
    if role_review_header != ROLE_REVIEW_HEADER:
        errors.append('bad_role_review_header')
    if draft_policy_header != DRAFT_POLICY_HEADER:
        errors.append('bad_draft_policy_header')
    if keys != REQUIRED:
        errors.append('content_value_spec_keys_mismatch')
    for r in rows:
        key = r.get('value_key','')
        for field in ['source_table','required_source_fields','used_by_page_roles']:
            if not r.get(field,'').strip():
                errors.append('missing_' + field + '=' + key)
        if r.get('status') != 'spec_only':
            errors.append('status_not_spec_only=' + key)
        if r.get('public_export') != 'false':
            errors.append('public_export_not_false=' + key)
        if r.get('page_generation') != 'false':
            errors.append('page_generation_not_false=' + key)
    if len(gate_rows) != 6:
        errors.append(f'gate_rows={len(gate_rows)} expected=6')
    if len(field_rows) != 6:
        errors.append(f'field_rows={len(field_rows)} expected=6')
    if len(role_rows) != 6:
        errors.append(f'role_instruction_rows={len(role_rows)} expected=6')
    if len(slot_failure_rows) != 8:
        errors.append(f'slot_failure_rows={len(slot_failure_rows)} expected=8')
    if len(role_review_rows) != 6:
        errors.append(f'role_review_rows={len(role_review_rows)} expected=6')
    if len(draft_policy_rows) != 1:
        errors.append(f'draft_policy_rows={len(draft_policy_rows)} expected=1')
    if [r.get('page_role','') for r in role_rows] != EXPECTED_ROLES:
        errors.append('role_instruction_sequence_mismatch')
    if [r.get('slot_id','') for r in slot_failure_rows] != EXPECTED_SLOTS:
        errors.append('slot_failure_sequence_mismatch')
    if [r.get('page_role','') for r in role_review_rows] != EXPECTED_ROLES:
        errors.append('role_review_sequence_mismatch')
    for spec_row in field_rows:
        role = spec_row.get('page_role','')
        sections = gate_by_role.get(role)
        if sections is None:
            errors.append('field_role_missing=' + role)
            continue
        for field in filter(None, spec_row.get('required_fields','').split('|')):
            if not covered(field, sections):
                errors.append('field_not_strictly_covered=' + role + ':' + field)
        if spec_row.get('field_status') != 'spec_only':
            errors.append('field_status_not_spec_only=' + role)
        if spec_row.get('public_export') != 'false':
            errors.append('field_public_export_not_false=' + role)
        if spec_row.get('page_generation') != 'false':
            errors.append('field_page_generation_not_false=' + role)
    for r in role_rows:
        role = r.get('page_role','')
        if r.get('batch_id') != 'candidate-10-19':
            errors.append('bad_role_instruction_batch=' + role)
        if r.get('instruction_state') != 'instruction_ready':
            errors.append('bad_role_instruction_state=' + role)
        if r.get('anchor_source') != 'next_10_body_value_anchor_candidate_10_19.tsv':
            errors.append('bad_role_anchor_source=' + role)
        if not ROLE_ANCHOR_NEEDS.get(role, set()).issubset(split_set(r.get('required_anchor_fields',''))):
            errors.append('role_anchor_fields_missing=' + role)
        for field in ['role_anchor_use','required_reader_effect','prohibited_drift']:
            if not r.get(field,'').strip():
                errors.append('role_instruction_field_missing=' + role + ':' + field)
        require_false(r, ['body_text_generation','html_generation','public_export'], 'role_instruction', errors)
    for r in slot_failure_rows:
        slot = r.get('slot_id','')
        if r.get('batch_id') != 'candidate-10-19':
            errors.append('bad_slot_failure_batch=' + slot)
        if r.get('failure_profile_state') != 'failure_profile_ready':
            errors.append('bad_slot_failure_state=' + slot)
        if 'origin_return' not in split_set(r.get('must_preserve','')):
            errors.append('slot_failure_origin_return_missing=' + slot)
        for field in ['source_candidate_id','folder_id','must_fail_if','must_preserve','review_focus']:
            if not r.get(field,'').strip():
                errors.append('slot_failure_field_missing=' + slot + ':' + field)
        require_false(r, ['body_text_generation','html_generation','public_export'], 'slot_failure', errors)
    for r in role_review_rows:
        role = r.get('page_role','')
        if r.get('batch_id') != 'candidate-10-19':
            errors.append('bad_role_review_batch=' + role)
        if r.get('review_state') != 'review_ready':
            errors.append('bad_role_review_state=' + role)
        if not ROLE_REVIEW_NEEDS.get(role, set()).issubset(split_set(r.get('must_check',''))):
            errors.append('role_review_must_check_missing=' + role)
        for field in ['must_fail_if','quality_axes']:
            if not r.get(field,'').strip():
                errors.append('role_review_field_missing=' + role + ':' + field)
        require_false(r, ['body_text_generation','html_generation','public_export'], 'role_review', errors)
    for r in draft_policy_rows:
        if r.get('batch_id') != 'candidate-10-19':
            errors.append('bad_draft_policy_batch')
        if r.get('policy_state') != 'draft_execution_policy_ready':
            errors.append('bad_draft_policy_state')
        if r.get('current_execution_state') != 'blocked_until_later_draft_commit':
            errors.append('bad_draft_current_execution_state')
        if r.get('unlock_condition') != 'all_pre_body_gates_pass_and_explicit_draft_phase':
            errors.append('bad_draft_unlock_condition')
        if not REQUIRED_POLICY_PRE.issubset(split_set(r.get('pre_generation_required',''))):
            errors.append('draft_policy_pre_generation_missing')
        if not REQUIRED_POLICY_POST.issubset(split_set(r.get('post_generation_required',''))):
            errors.append('draft_policy_post_generation_missing')
        if not REQUIRED_POLICY_FAIL.issubset(split_set(r.get('must_fail_if',''))):
            errors.append('draft_policy_must_fail_missing')
        require_false(r, ['body_text_generation','html_generation','public_export'], 'draft_policy', errors)
    virtual_body_draft_units = [(slot, role) for slot in EXPECTED_SLOTS for role in EXPECTED_ROLES]
    if len(virtual_body_draft_units) != 48:
        errors.append('virtual_body_draft_unit_count_mismatch')
    if len(set(virtual_body_draft_units)) != 48:
        errors.append('virtual_body_draft_unit_duplicate')
    print('check_set=next_10_content_value_spec_v6')
    print('content_value_spec_rows=' + str(len(rows)))
    print('field_rows=' + str(len(field_rows)))
    print('role_instruction_rows=' + str(len(role_rows)))
    print('slot_failure_rows=' + str(len(slot_failure_rows)))
    print('role_review_rows=' + str(len(role_review_rows)))
    print('draft_policy_rows=' + str(len(draft_policy_rows)))
    print('virtual_body_draft_units=' + str(len(virtual_body_draft_units)))
    print('draft_execution_policy=ready_blocked')
    print('body_draft_readiness=spec_ready_not_generated')
    print('public_export=false')
    print('page_generation=false')
    if errors:
        print('\n'.join(errors[:140]))
        print('next_10_content_value_spec_pass=false')
        return 1
    print('next_10_content_value_spec_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
