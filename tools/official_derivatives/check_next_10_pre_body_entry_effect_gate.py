#!/usr/bin/env python3
import csv
import runpy
from pathlib import Path

PATH = Path('tools/official_derivatives/next_10_pre_body_entry_effect_gate_candidate_10_19.tsv')
HEADER = [
    'batch_id','page_role','gate_state','required_human_entry_effect',
    'required_ai_reference_effect','required_origin_effect','must_block',
    'body_text_generation','html_generation','public_export',
]
ROLES = ['hub','human_summary','faq','ja_ai_index','en_ai_index','zh_ai_index']
ORIGIN = {'parent_url','parent_ncl_id','parent_diff_id','canonical_url'}
COMMON_BLOCKS = {'origin_blur'}
ROLE_EFFECTS = {
    'hub': {'role_clarity','origin_discovery','return_path'},
    'human_summary': {'plain_first_line','reader_problem_bridge','ordinary_not_signal','reason_to_read_original'},
    'faq': {'beginner_entry','structure_entry','boundary_entry','misread_prevention'},
    'ja_ai_index': {'role_signal','original_reading_return'},
    'en_ai_index': {'translated_role_signal','original_reading_return'},
    'zh_ai_index': {'translated_role_signal','original_reading_return'},
}
AI_EFFECTS = {
    'hub': {'role_map','source_identity','reuse_boundary'},
    'human_summary': {'causal_line','judgment_support','reuse_boundary'},
    'faq': {'question_map','boundary_conditions','reuse_boundary'},
    'ja_ai_index': {'definition','core_claim','applicability','non_applicability','counterexample','reuse_constraint'},
    'en_ai_index': {'definition','core_claim','applicability','non_applicability','counterexample','reuse_constraint'},
    'zh_ai_index': {'definition','core_claim','applicability','non_applicability','counterexample','reuse_constraint'},
}


def split(value: str) -> set[str]:
    return set(filter(None, value.split('|')))


def main() -> int:
    runpy.run_path('tools/official_derivatives/check_next_10_four_stage_gate.py', run_name='__main__')
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
        if row.get('batch_id') != 'candidate-10-19':
            errors.append('bad_batch=' + role)
        if row.get('gate_state') != 'spec_only':
            errors.append('bad_gate_state=' + role)
        if not ROLE_EFFECTS.get(role, set()).issubset(split(row.get('required_human_entry_effect',''))):
            errors.append('human_entry_effect_missing=' + role)
        if not AI_EFFECTS.get(role, set()).issubset(split(row.get('required_ai_reference_effect',''))):
            errors.append('ai_reference_effect_missing=' + role)
        if not ORIGIN.issubset(split(row.get('required_origin_effect',''))):
            errors.append('origin_effect_missing=' + role)
        if not COMMON_BLOCKS.issubset(split(row.get('must_block',''))):
            errors.append('must_block_missing=' + role)
        for field in ['body_text_generation','html_generation','public_export']:
            if row.get(field) != 'false':
                errors.append('boundary_not_false=' + role + ':' + field)
    print('check_set=next_10_pre_body_entry_effect_gate_v2')
    print('rows=' + str(len(rows)))
    print('public_export=false')
    print('body_text_generation=false')
    print('html_generation=false')
    if errors:
        print('\n'.join(errors[:80]))
        print('next_10_pre_body_entry_effect_gate_pass=false')
        return 1
    print('next_10_pre_body_entry_effect_gate_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
