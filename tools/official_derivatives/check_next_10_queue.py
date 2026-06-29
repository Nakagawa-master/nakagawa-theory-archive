#!/usr/bin/env python3
import csv
from pathlib import Path

SCHEMA = Path('tools/official_derivatives/next_10_queue_schema.tsv')
QUEUE = Path('tools/official_derivatives/next_10_queue_candidate_10_19.tsv')
CANDIDATES = Path('tools/official_derivatives/next_10_source_candidates_candidate_10_19.tsv')
NEEDED = ['batch_id','slot_id','selection_status','source_category','reason_for_inclusion','risk_note','handoff_status']
SOURCE_FIELDS = ['parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url']
LINK_FIELDS = ['source_category','parent_url','parent_ncl_id','parent_diff_id','folder_id','canonical_url']
VALID_STATUS = {'unselected','candidate','selected','rejected'}
VALID_HANDOFF = {'queue_only','intake_ready','intake_blocked'}


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def has_source(row):
    return all(row.get(k,'').strip() for k in SOURCE_FIELDS)


def any_source(row):
    return any(row.get(k,'').strip() for k in SOURCE_FIELDS)


def link_key(row):
    return (row.get('parent_url',''), row.get('parent_ncl_id',''), row.get('parent_diff_id',''))


def ready_sources():
    rows = read(CANDIDATES)
    return {
        link_key(row): row for row in rows
        if row.get('source_status') == 'recommended'
        and row.get('recommendation') == 'ready_for_queue'
        and row.get('public_safe_status') == 'pass'
    }


def main():
    schema_fields = [r.get('field','') for r in read(SCHEMA)]
    rows = read(QUEUE)
    ready = ready_sources()
    errors = []
    queued_candidate_rows = 0
    for key in NEEDED + SOURCE_FIELDS:
        if key not in schema_fields:
            errors.append('schema_missing=' + key)
    if len(rows) != 10:
        errors.append('queue_rows_expected=10')
    for idx, row in enumerate(rows, start=10):
        expected = 'Official Derivative ' + str(idx).zfill(3)
        status = row.get('selection_status')
        handoff = row.get('handoff_status')
        if row.get('batch_id') != 'candidate-10-19':
            errors.append('batch_mismatch=' + str(idx))
        if row.get('slot_id') != expected:
            errors.append('slot_mismatch=' + str(idx))
        if status not in VALID_STATUS:
            errors.append('bad_selection_status=' + str(idx))
        if handoff not in VALID_HANDOFF:
            errors.append('bad_handoff_status=' + str(idx))
        if status == 'unselected' and handoff != 'queue_only':
            errors.append('unselected_not_queue_only=' + str(idx))
        if handoff == 'queue_only' and any_source(row):
            errors.append('queue_only_has_source_fields=' + str(idx))
        if status == 'selected' and handoff == 'intake_ready' and not has_source(row):
            errors.append('intake_ready_missing_source_fields=' + str(idx))
        if status == 'selected' and handoff == 'queue_only':
            errors.append('selected_still_queue_only=' + str(idx))
        if handoff == 'intake_ready' and not row.get('canonical_url','').startswith('https://master.ricette.jp/derivatives/'):
            errors.append('bad_intake_canonical=' + str(idx))
        if status == 'candidate':
            queued_candidate_rows += 1
            if handoff != 'intake_blocked':
                errors.append('candidate_not_intake_blocked=' + str(idx))
            source = ready.get(link_key(row))
            if not source:
                errors.append('candidate_without_ready_source=' + str(idx))
            else:
                for field in LINK_FIELDS:
                    if row.get(field,'') != source.get(field,''):
                        errors.append('candidate_source_mismatch=' + str(idx) + ':' + field)
    if queued_candidate_rows not in {0,8}:
        errors.append('unexpected_candidate_rows=' + str(queued_candidate_rows))
    print('check_set=next_10_queue_v3')
    print('queue_rows=' + str(len(rows)))
    print('candidate_rows=' + str(queued_candidate_rows))
    if errors:
        print('\n'.join(errors[:40]))
        print('next_10_queue_pass=false')
        return 1
    print('next_10_queue_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())