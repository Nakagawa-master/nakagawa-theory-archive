#!/usr/bin/env python3
import csv
from pathlib import Path

SPEC = Path('tools/official_derivatives/next_10_content_value_extraction_spec_20260630.tsv')
HEADER = ['value_key','source_table','required_source_fields','used_by_page_roles','status','public_export','page_generation']
REQUIRED = {
    'origin_identity','value_core','causal_line','misreading_guard',
    'origin_return','page_links','question_set','index_definition'
}


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames or [], list(reader)


def main():
    header, rows = read(SPEC)
    errors = []
    keys = {r.get('value_key','') for r in rows}
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
    print('check_set=next_10_content_value_spec_v1')
    print('content_value_spec_rows=' + str(len(rows)))
    print('public_export=false')
    print('page_generation=false')
    if errors:
        print('\n'.join(errors[:40]))
        print('next_10_content_value_spec_pass=false')
        return 1
    print('next_10_content_value_spec_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
