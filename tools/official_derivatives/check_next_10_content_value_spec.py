#!/usr/bin/env python3
import csv
from pathlib import Path

SPEC = Path('tools/official_derivatives/next_10_content_value_extraction_spec_20260630.tsv')
GATE = Path('tools/official_derivatives/next_10_high_strength_template_gate_candidate_10_19.tsv')
FIELD_SPEC = Path('tools/official_derivatives/next_10_content_field_spec_candidate_10_19.tsv')
HEADER = ['value_key','source_table','required_source_fields','used_by_page_roles','status','public_export','page_generation']
REQUIRED = {
    'origin_identity','value_core','causal_line','misreading_guard',
    'origin_return','page_links','question_set','index_definition'
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


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames or [], list(reader)


def covered(field, sections):
    if field in sections:
        return True
    required = FIELD_COVER.get(field)
    if not required:
        return False
    return required.issubset(sections)


def main():
    header, rows = read(SPEC)
    _, gate_rows = read(GATE)
    _, field_rows = read(FIELD_SPEC)
    errors = []
    keys = {r.get('value_key','') for r in rows}
    gate_by_role = {r.get('page_role',''): set(filter(None, r.get('required_sections','').split('|'))) for r in gate_rows}
    if header != HEADER:
        errors.append('bad_content_value_spec_header')
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
    print('check_set=next_10_content_value_spec_v2')
    print('content_value_spec_rows=' + str(len(rows)))
    print('field_rows=' + str(len(field_rows)))
    print('public_export=false')
    print('page_generation=false')
    if errors:
        print('\n'.join(errors[:60]))
        print('next_10_content_value_spec_pass=false')
        return 1
    print('next_10_content_value_spec_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
