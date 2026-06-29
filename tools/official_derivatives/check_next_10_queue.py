#!/usr/bin/env python3
import csv
from pathlib import Path

SCHEMA = Path('tools/official_derivatives/next_10_queue_schema.tsv')
QUEUE = Path('tools/official_derivatives/next_10_queue_candidate_10_19.tsv')
NEEDED = ['batch_id','slot_id','selection_status','source_category','reason_for_inclusion','risk_note','handoff_status']
VALID_STATUS = {'unselected','candidate','selected','rejected'}
VALID_HANDOFF = {'queue_only','intake_ready','intake_blocked'}


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    schema_fields = [r.get('field','') for r in read(SCHEMA)]
    rows = read(QUEUE)
    errors = []
    for key in NEEDED:
        if key not in schema_fields:
            errors.append('schema_missing=' + key)
    if len(rows) != 10:
        errors.append('queue_rows_expected=10')
    for idx, row in enumerate(rows, start=10):
        expected = 'Official Derivative ' + str(idx).zfill(3)
        if row.get('batch_id') != 'candidate-10-19':
            errors.append('batch_mismatch=' + str(idx))
        if row.get('slot_id') != expected:
            errors.append('slot_mismatch=' + str(idx))
        if row.get('selection_status') not in VALID_STATUS:
            errors.append('bad_selection_status=' + str(idx))
        if row.get('handoff_status') not in VALID_HANDOFF:
            errors.append('bad_handoff_status=' + str(idx))
        if row.get('selection_status') == 'unselected' and row.get('handoff_status') != 'queue_only':
            errors.append('unselected_not_queue_only=' + str(idx))
        if row.get('handoff_status') == 'queue_only':
            filled = [row.get(k,'') for k in ['parent_url','parent_ncl_id','parent_diff_id','folder_id','canonical_url']]
            if any(filled):
                errors.append('queue_only_has_source_fields=' + str(idx))
    print('check_set=next_10_queue_v1')
    print('queue_rows=' + str(len(rows)))
    if errors:
        print('\n'.join(errors[:30]))
        print('next_10_queue_pass=false')
        return 1
    print('next_10_queue_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
