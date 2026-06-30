#!/usr/bin/env python3
import csv
from pathlib import Path

PATH = Path('tools/official_derivatives/next_10_four_stage_gate_candidate_10_19.tsv')
HEADER = [
    'batch_id','page_role','gate_state','stage_01','stage_02','stage_03','stage_04',
    'required_origin_fields','must_block','body_text_generation','html_generation','public_export',
]
ROLES = ['hub','human_summary','faq','ja_ai_index','en_ai_index','zh_ai_index']
ORIGIN = {'parent_url','parent_ncl_id','parent_diff_id','canonical_url'}
ROLE_REQUIREMENTS = {
    'hub': {
        'stage_01': {'first_signal'},
        'stage_02': {'role_explanation'},
        'stage_03': {'navigation_path'},
        'stage_04': {'origin_return'},
    },
    'human_summary': {
        'stage_01': {'plain_first_line'},
        'stage_02': {'discovery_and_value'},
        'stage_03': {'reader_bridge','judgment_support'},
        'stage_04': {'origin_return'},
    },
    'faq': {
        'stage_01': {'beginner_entry'},
        'stage_02': {'structure_path'},
        'stage_03': {'boundary_path','misread_prevention'},
        'stage_04': {'origin_return'},
    },
    'ja_ai_index': {
        'stage_01': {'role_signal'},
        'stage_02': {'definition','core_claim'},
        'stage_03': {'applicability','non_applicability','counterexample'},
        'stage_04': {'origin_preservation'},
    },
    'en_ai_index': {
        'stage_01': {'translated_role_signal'},
        'stage_02': {'definition','core_claim'},
        'stage_03': {'applicability','non_applicability','counterexample'},
        'stage_04': {'origin_preservation'},
    },
    'zh_ai_index': {
        'stage_01': {'translated_role_signal'},
        'stage_02': {'definition','core_claim'},
        'stage_03': {'applicability','non_applicability','counterexample'},
        'stage_04': {'origin_preservation'},
    },
}


def split(value: str) -> set[str]:
    return set(filter(None, value.split('|')))


def main() -> int:
    with PATH.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        header = reader.fieldnames or []
        rows = list(reader)
    errors = []
    if header != HEADER:
        errors.append('bad_header')
    if [row.get('page_role','') for row in rows] != ROLES:
        errors.append('role_sequence_mismatch')
    if len(rows) != 6:
        errors.append('row_count=' + str(len(rows)))
    for row in rows:
        role = row.get('page_role','')
        req = ROLE_REQUIREMENTS.get(role, {})
        if row.get('batch_id') != 'candidate-10-19':
            errors.append('bad_batch=' + role)
        if row.get('gate_state') != 'spec_only':
            errors.append('bad_gate_state=' + role)
        for stage in ['stage_01','stage_02','stage_03','stage_04']:
            if not req.get(stage, set()).issubset(split(row.get(stage,''))):
                errors.append(stage + '_missing=' + role)
        if not ORIGIN.issubset(split(row.get('required_origin_fields',''))):
            errors.append('origin_fields_missing=' + role)
        if 'origin_blur' not in split(row.get('must_block','')):
            errors.append('origin_block_missing=' + role)
        for field in ['body_text_generation','html_generation','public_export']:
            if row.get(field) != 'false':
                errors.append('boundary_not_false=' + role + ':' + field)
    print('check_set=next_10_four_stage_gate_v1')
    print('rows=' + str(len(rows)))
    print('public_export=false')
    print('body_text_generation=false')
    print('html_generation=false')
    if errors:
        print('\n'.join(errors[:80]))
        print('next_10_four_stage_gate_pass=false')
        return 1
    print('next_10_four_stage_gate_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
