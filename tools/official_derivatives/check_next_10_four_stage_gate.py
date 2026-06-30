#!/usr/bin/env python3
import csv
from pathlib import Path

PATH = Path('tools/official_derivatives/next_10_four_stage_gate_candidate_10_19.tsv')
ROLES = ['hub','human_summary','faq','ja_ai_index','en_ai_index','zh_ai_index']
REQ_COLS = ['stage_01','stage_02','stage_03','stage_04','layer_coverage','required_origin_fields','body_text_generation','html_generation','public_export']
ORIGIN = {'parent_url','parent_ncl_id','parent_diff_id','canonical_url'}


def split(v):
    return set(filter(None, v.split('|')))


def main():
    with PATH.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        header = reader.fieldnames or []
        rows = list(reader)
    errors = []
    for col in REQ_COLS:
        if col not in header:
            errors.append('missing_col=' + col)
    if [row.get('page_role','') for row in rows] != ROLES:
        errors.append('role_sequence_mismatch')
    if len(rows) != 6:
        errors.append('row_count=' + str(len(rows)))
    for row in rows:
        role = row.get('page_role','')
        for col in ['stage_01','stage_02','stage_03','stage_04']:
            if not row.get(col,'').strip():
                errors.append('empty_' + col + '=' + role)
        if not row.get('layer_coverage','').strip():
            errors.append('empty_layer_coverage=' + role)
        if not ORIGIN.issubset(split(row.get('required_origin_fields',''))):
            errors.append('origin_fields_missing=' + role)
        for col in ['body_text_generation','html_generation','public_export']:
            if row.get(col) != 'false':
                errors.append('boundary_not_false=' + role + ':' + col)
    print('check_set=next_10_four_stage_gate_v3')
    print('rows=' + str(len(rows)))
    if errors:
        print('\n'.join(errors[:80]))
        print('next_10_four_stage_gate_pass=false')
        return 1
    print('next_10_four_stage_gate_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
