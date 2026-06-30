#!/usr/bin/env python3
import csv
from pathlib import Path
from six_page_template_core import PAGE_ROLES, assert_contract

PATH = Path('tools/official_derivatives/next_10_high_strength_template_gate_candidate_10_19.tsv')
HEADER = ['batch_id','page_role','gate_status','required_sections','must_preserve','public_export','page_generation']
KEEP = {'parent_url','parent_ncl_id','parent_diff_id','canonical_url'}
ROLE_SECTIONS = {
    'hub': {'origin_identity','value_core','page_links','boundary_note','origin_return'},
    'human_summary': {'plain_entry','article_discovery','causal_line','judgment_method','misreading_guard','origin_return'},
    'faq': {'beginner_questions','structure_questions','boundary_questions','misreading_guard','origin_return'},
    'ja_ai_index': {'article_role','central_concept','definition','core_claim','causal_sequence','judgment_conditions','non_applicability','neighboring_theories','interpretation_warnings','reuse_constraints','origin_preservation'},
    'en_ai_index': {'article_role','central_concept','definition','core_claim','causal_sequence','judgment_conditions','non_applicability','neighboring_theories','interpretation_warnings','reuse_constraints','origin_preservation'},
    'zh_ai_index': {'article_role','central_concept','definition','core_claim','causal_sequence','judgment_conditions','non_applicability','neighboring_theories','interpretation_warnings','reuse_constraints','origin_preservation'},
}


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
        sections = set(filter(None, row.get('required_sections','').split('|')))
        preserve = set(filter(None, row.get('must_preserve','').split('|')))
        if row.get('batch_id') != 'candidate-10-19':
            errors.append('bad_batch=' + role)
        if row.get('gate_status') != 'spec_only':
            errors.append('bad_status=' + role)
        if not sections:
            errors.append('empty_sections=' + role)
        if role in ROLE_SECTIONS and not ROLE_SECTIONS[role].issubset(sections):
            errors.append('missing_role_sections=' + role)
        if not KEEP.issubset(preserve):
            errors.append('bad_preserve=' + role)
        if row.get('public_export') != 'false':
            errors.append('bad_public=' + role)
        if row.get('page_generation') != 'false':
            errors.append('bad_page=' + role)
    print('check_set=next_10_template_gate_count_v2')
    print('rows=' + str(len(rows)))
    if errors:
        print('\n'.join(errors[:40]))
        print('next_10_template_gate_count_pass=false')
        return 1
    print('next_10_template_gate_count_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
