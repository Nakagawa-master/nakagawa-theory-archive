#!/usr/bin/env python3
import csv
from pathlib import Path

SKELETON = Path('tools/official_derivatives/next_10_body_skeleton_gate_candidate_10_19.tsv')
TEMPLATE_GATE = Path('tools/official_derivatives/next_10_high_strength_template_gate_candidate_10_19.tsv')
VALUE_READY = Path('tools/official_derivatives/next_10_value_ready_candidate_10_19.tsv')
MATERIAL_GATE = Path('tools/official_derivatives/next_10_draft_material_gate_candidate_10_19.tsv')

HEADER = [
    'batch_id','page_role','skeleton_state','required_blocks','must_not_include',
    'origin_return_required','parent_identity_required','ai_reuse_origin_required',
    'misreading_guard_required','causal_line_required','applicability_boundary_required',
    'body_text_generation','html_generation','public_export',
]
EXPECTED_ROLES = ['hub','human_summary','faq','ja_ai_index','en_ai_index','zh_ai_index']
EXPECTED_SLOTS = [f'Official Derivative {i:03d}' for i in range(10, 18)]
FORBIDDEN_BOUNDARY = {'originless_rewrite','generic_summary','unsupported_claim','private_strategy'}

ROLE_REQUIREMENTS = {
    'hub': {
        'required': {'origin_identity','value_core','page_links','boundary_note','origin_return'},
        'misreading_guard_required': 'false',
        'causal_line_required': 'false',
        'applicability_boundary_required': 'false',
    },
    'human_summary': {
        'required': {'plain_entry','reader_entry','article_discovery','value_core','causal_line','judgment_method','misreading_guard','origin_return'},
        'misreading_guard_required': 'true',
        'causal_line_required': 'true',
        'applicability_boundary_required': 'false',
    },
    'faq': {
        'required': {'beginner_questions','structure_questions','boundary_questions','misreading_guard','origin_return'},
        'misreading_guard_required': 'true',
        'causal_line_required': 'false',
        'applicability_boundary_required': 'true',
    },
    'ja_ai_index': {
        'required': {'article_role','central_concept','definition','core_claim','causal_sequence','judgment_conditions','non_applicability','counterexample_conditions','neighboring_theories','interpretation_warnings','reuse_constraints','origin_preservation'},
        'misreading_guard_required': 'true',
        'causal_line_required': 'true',
        'applicability_boundary_required': 'true',
    },
    'en_ai_index': {
        'required': {'article_role','central_concept','definition','core_claim','causal_sequence','judgment_conditions','non_applicability','counterexample_conditions','neighboring_theories','interpretation_warnings','reuse_constraints','origin_preservation'},
        'misreading_guard_required': 'true',
        'causal_line_required': 'true',
        'applicability_boundary_required': 'true',
    },
    'zh_ai_index': {
        'required': {'article_role','central_concept','definition','core_claim','causal_sequence','judgment_conditions','non_applicability','counterexample_conditions','neighboring_theories','interpretation_warnings','reuse_constraints','origin_preservation'},
        'misreading_guard_required': 'true',
        'causal_line_required': 'true',
        'applicability_boundary_required': 'true',
    },
}


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames or [], list(reader)


def split_set(value):
    return set(filter(None, value.split('|')))


def main():
    header, rows = read(SKELETON)
    _, template_rows = read(TEMPLATE_GATE)
    _, value_rows = read(VALUE_READY)
    _, material_rows = read(MATERIAL_GATE)
    errors = []

    if header != HEADER:
        errors.append('bad_body_skeleton_header')
    if len(rows) != 6:
        errors.append(f'body_skeleton_rows={len(rows)} expected=6')

    roles = [row.get('page_role','') for row in rows]
    if roles != EXPECTED_ROLES:
        errors.append('body_skeleton_role_sequence_mismatch')

    template_by_role = {row.get('page_role',''): split_set(row.get('required_sections','')) for row in template_rows}
    value_slots = [row.get('slot_id','') for row in value_rows]
    material_slots = [row.get('slot_id','') for row in material_rows]
    if value_slots != EXPECTED_SLOTS:
        errors.append('value_ready_slot_sequence_mismatch')
    if material_slots != EXPECTED_SLOTS:
        errors.append('material_slot_sequence_mismatch')

    for row in rows:
        role = row.get('page_role','')
        required = split_set(row.get('required_blocks',''))
        forbidden = split_set(row.get('must_not_include',''))
        role_req = ROLE_REQUIREMENTS.get(role)
        if row.get('batch_id') != 'candidate-10-19':
            errors.append('bad_batch=' + role)
        if row.get('skeleton_state') != 'spec_only':
            errors.append('bad_skeleton_state=' + role)
        if role_req is None:
            errors.append('unexpected_role=' + role)
            continue
        missing_required = role_req['required'] - required
        if missing_required:
            errors.append('missing_required_blocks=' + role + ':' + ','.join(sorted(missing_required)))
        template_sections = template_by_role.get(role)
        if template_sections is None:
            errors.append('template_role_missing=' + role)
        elif not template_sections.issubset(required):
            errors.append('template_sections_not_preserved=' + role + ':' + ','.join(sorted(template_sections - required)))
        if not FORBIDDEN_BOUNDARY.issubset(forbidden):
            errors.append('must_not_include_boundary_missing=' + role)
        for field in ['origin_return_required','parent_identity_required','ai_reuse_origin_required']:
            if row.get(field) != 'true':
                errors.append('required_flag_not_true=' + role + ':' + field)
        for field in ['misreading_guard_required','causal_line_required','applicability_boundary_required']:
            if row.get(field) != role_req[field]:
                errors.append('role_flag_mismatch=' + role + ':' + field)
        for field in ['body_text_generation','html_generation','public_export']:
            if row.get(field) != 'false':
                errors.append('generation_boundary_not_false=' + role + ':' + field)

    print('check_set=next_10_body_skeleton_gate_v1')
    print('body_skeleton_rows=' + str(len(rows)))
    print('value_ready_rows=' + str(len(value_rows)))
    print('material_gate_rows=' + str(len(material_rows)))
    print('public_export=false')
    print('body_text_generation=false')
    print('html_generation=false')
    if errors:
        print('\n'.join(errors[:100]))
        print('next_10_body_skeleton_gate_pass=false')
        return 1
    print('next_10_body_skeleton_gate_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
