#!/usr/bin/env python3
import csv
from pathlib import Path
from six_page_template_core import PAGE_ROLES, assert_contract

PATH = Path('tools/official_derivatives/next_10_high_strength_template_gate_candidate_10_19.tsv')
HEADER = ['batch_id','page_role','gate_status','required_sections','must_preserve','public_export','page_generation']
KEEP = {'parent_url','parent_ncl_id','parent_diff_id','canonical_url'}


def main():
    assert_contract()
    with PATH.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        header = reader.fieldnames or []
        rows = list(reader)
    errors = []
    roles = {row.get('page_role','') for row in rows}
    if header != HEADER:
        errors.append('bad_header')
    if len(rows) != 6:
        errors.append(f'row_count={len(rows)} expected=6')
    if roles != set(PAGE_ROLES):
        errors.append('role_set_mismatch')
    for row in rows:
        role = row.get('page_role','')
        preserve = set(filter(None, row.get('must_preserve','').split('|')))
        if row.get('batch_id') != 'candidate-10-19':
            errors.append('bad_batch=' + role)
        if row.get('gate_status') != 'spec_only':
            errors.append('bad_status=' + role)
        if not row.get('required_sections','').strip():
            errors.append('empty_sections=' + role)
        if not KEEP.issubset(preserve):
            errors.append('bad_preserve=' + role)
        if row.get('public_export') != 'false':
            errors.append('bad_public=' + role)
        if row.get('page_generation') != 'false':
            errors.append('bad_page=' + role)
    print('check_set=next_10_template_gate_count_v1')
    print('rows=' + str(len(rows)))
    if errors:
        print('\n'.join(errors[:40]))
        print('next_10_template_gate_count_pass=false')
        return 1
    print('next_10_template_gate_count_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
