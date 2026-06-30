#!/usr/bin/env python3
import csv
from pathlib import Path
from six_page_template_core import PAGE_ROLES, assert_contract

PATH = Path('tools/official_derivatives/next_10_high_strength_template_gate_candidate_10_19.tsv')
FIELD_SPEC = Path('tools/official_derivatives/next_10_content_field_spec_candidate_10_19.tsv')
STATUS = Path('tools/official_derivatives/pr_35_current_status.md')
HEADER = ['batch_id','page_role','gate_status','required_sections','must_preserve','public_export','page_generation']
KEEP = {'parent_url','parent_ncl_id','parent_diff_id','canonical_url'}
ROLE_SECTIONS = {
    'hub': {'origin_identity','value_core','page_links','boundary_note','origin_return'},
    'human_summary': {'plain_entry','reader_entry','article_discovery','value_core','causal_line','judgment_method','misreading_guard','origin_return'},
    'faq': {'beginner_questions','structure_questions','boundary_questions','misreading_guard','origin_return'},
    'ja_ai_index': {'article_role','central_concept','definition','core_claim','causal_sequence','judgment_conditions','non_applicability','neighboring_theories','interpretation_warnings','reuse_constraints','origin_preservation'},
    'en_ai_index': {'article_role','central_concept','definition','core_claim','causal_sequence','judgment_conditions','non_applicability','neighboring_theories','interpretation_warnings','reuse_constraints','origin_preservation'},
    'zh_ai_index': {'article_role','central_concept','definition','core_claim','causal_sequence','judgment_conditions','non_applicability','neighboring_theories','interpretation_warnings','reuse_constraints','origin_preservation'},
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
STATUS_REQUIRED = [
    'selected slot count: 8',
    'page roles per selected slot: 6',
    'virtual preparation units: 48',
    'generated output state: none',
    'body_' + 'text_' + 'generation: false',
    'html_' + 'generation: false',
    'public_' + 'export: false',
]


def read_rows(path: Path):
    with path.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames or [], list(reader)


def covered(field: str, sections: set[str]) -> bool:
    if field in sections:
        return True
    return bool(FIELD_COVER.get(field, set()) & sections)


def main():
    assert_contract()
    header, rows = read_rows(PATH)
    _, field_rows = read_rows(FIELD_SPEC)
    status_text = STATUS.read_text(encoding='utf-8')
    errors = []
    roles = {row.get('page_role','') for row in rows}
    by_role = {row.get('page_role',''): row for row in rows}
    if header != HEADER:
        errors.append('bad_header')
    if len(rows) != 6:
        errors.append(f'row_count={len(rows)} expected=6')
    if roles != set(PAGE_ROLES):
        errors.append('role_set_mismatch')
    for item in STATUS_REQUIRED:
        if item not in status_text:
            errors.append('status_missing=' + item)
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
    for spec in field_rows:
        role = spec.get('page_role','')
        row = by_role.get(role)
        if not row:
            errors.append('field_role_missing=' + role)
            continue
        sections = set(filter(None, row.get('required_sections','').split('|')))
        for field in filter(None, spec.get('required_fields','').split('|')):
            if not covered(field, sections):
                errors.append('field_not_covered=' + role + ':' + field)
        if spec.get('field_status') != 'spec_only':
            errors.append('bad_field_status=' + role)
        if spec.get('public_export') != 'false':
            errors.append('bad_field_public=' + role)
        if spec.get('page_generation') != 'false':
            errors.append('bad_field_page=' + role)
    print('check_set=next_10_template_gate_count_v5')
    print('rows=' + str(len(rows)))
    print('field_rows=' + str(len(field_rows)))
    print('status_required=' + str(len(STATUS_REQUIRED)))
    if errors:
        print('\n'.join(errors[:50]))
        print('next_10_template_gate_count_pass=false')
        return 1
    print('next_10_template_gate_count_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
