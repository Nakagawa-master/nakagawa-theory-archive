#!/usr/bin/env python3
import csv
from pathlib import Path

QUEUE = Path('tools/official_derivatives/next_10_queue_candidate_10_19.tsv')
CANDIDATES = Path('tools/official_derivatives/next_10_source_candidates_candidate_10_19.tsv')
KEYS = ['parent_url','parent_ncl_id','parent_diff_id']
IDENTITY = ['source_category','parent_url','parent_ncl_id','parent_diff_id','folder_id','canonical_url']


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def key(row):
    return tuple(row.get(k,'') for k in KEYS)


def main():
    queue = read(QUEUE)
    candidates = read(CANDIDATES)
    candidate_map = {
        key(row): row for row in candidates
        if row.get('source_status') == 'recommended'
        and row.get('recommendation') == 'ready_for_queue'
        and row.get('public_safe_status') == 'pass'
    }
    errors = []
    checked = 0
    for row in queue:
        if row.get('selection_status') != 'candidate':
            continue
        checked += 1
        slot = row.get('slot_id','unknown')
        if row.get('handoff_status') != 'intake_blocked':
            errors.append('candidate_not_intake_blocked=' + slot)
        source = candidate_map.get(key(row))
        if not source:
            errors.append('missing_ready_source=' + slot)
            continue
        for field in IDENTITY:
            if row.get(field,'') != source.get(field,''):
                errors.append('identity_mismatch=' + slot + ':' + field)
    if checked != 8:
        errors.append('candidate_rows=' + str(checked) + ':expected=8')
    print('check_set=next_10_queue_candidate_link_v1')
    print('candidate_rows=' + str(checked))
    print('ready_source_rows=' + str(len(candidate_map)))
    print('page_generation=false')
    if errors:
        print('\n'.join(errors[:40]))
        print('next_10_queue_candidate_link_pass=false')
        return 1
    print('next_10_queue_candidate_link_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
