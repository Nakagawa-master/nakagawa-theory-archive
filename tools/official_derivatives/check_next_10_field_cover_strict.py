#!/usr/bin/env python3
import csv
from pathlib import Path

GATE = Path('tools/official_derivatives/next_10_high_strength_template_gate_candidate_10_19.tsv')
SPEC = Path('tools/official_derivatives/next_10_content_field_spec_candidate_10_19.tsv')
MAP = {
    'question_set': {'beginner_questions','structure_questions','boundary_questions'},
    'answer_set': {'beginner_questions','structure_questions','boundary_questions'},
    'boundary_condition': {'boundary_questions','misreading_guard'},
    'scope': {'central_concept','judgment_conditions'},
    'conditions': {'judgment_conditions','non_applicability'},
    'origin_identity': {'origin_preservation'},
    'misreading_guard': {'interpretation_warnings','reuse_constraints'},
}


def rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    gate_rows = rows(GATE)
    spec_rows = rows(SPEC)
    by_role = {row['page_role']: set(row['required_sections'].split('|')) for row in gate_rows}
    errors = []
    if len(gate_rows) != 6:
        errors.append(f'gate_rows={len(gate_rows)} expected=6')
    if len(spec_rows) != 6:
        errors.append(f'spec_rows={len(spec_rows)} expected=6')
    for row in spec_rows:
        role = row['page_role']
        sections = by_role.get(role)
        if sections is None:
            errors.append('missing_role=' + role)
            continue
        for field in filter(None, row['required_fields'].split('|')):
            if field in sections:
                continue
            required = MAP.get(field)
            if not required or not required.issubset(sections):
                errors.append('field_not_strictly_covered=' + role + ':' + field)
        if row['field_status'] != 'spec_only':
            errors.append('bad_status=' + role)
        if row['public_export'] != 'false':
            errors.append('bad_public=' + role)
        if row['page_generation'] != 'false':
            errors.append('bad_page=' + role)
    print('check_set=next_10_field_cover_strict_v1')
    print('gate_rows=' + str(len(gate_rows)))
    print('spec_rows=' + str(len(spec_rows)))
    if errors:
        print('\n'.join(errors[:40]))
        print('next_10_field_cover_strict_pass=false')
        return 1
    print('next_10_field_cover_strict_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
