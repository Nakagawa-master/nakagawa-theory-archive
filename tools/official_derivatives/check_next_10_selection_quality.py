#!/usr/bin/env python3
import csv
from pathlib import Path

QUEUE = Path('tools/official_derivatives/next_10_queue_candidate_10_19.tsv')
VALID_CATEGORIES = {'theory','society','future','structural-reading','other'}
SOURCE_FIELDS = ['parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url']


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def filled(row, key):
    return bool(row.get(key,'').strip())


def main():
    rows = read(QUEUE)
    errors = []
    checked = 0
    for idx, row in enumerate(rows, start=10):
        status = row.get('selection_status','')
        handoff = row.get('handoff_status','')
        if status in {'candidate','selected'} or handoff in {'intake_ready','intake_blocked'}:
            checked += 1
            if row.get('source_category') not in VALID_CATEGORIES:
                errors.append('bad_source_category=' + str(idx))
            if row.get('reason_for_inclusion','').strip() in {'','pending source selection','none'}:
                errors.append('weak_reason=' + str(idx))
            if row.get('risk_note','').strip() == '':
                errors.append('missing_risk_note=' + str(idx))
        if handoff == 'intake_ready':
            for key in SOURCE_FIELDS:
                if not filled(row, key):
                    errors.append('intake_ready_missing_' + key + '=' + str(idx))
            if not row.get('parent_url','').startswith('https://master.ricette.jp/'):
                errors.append('bad_parent_url=' + str(idx))
            if not row.get('parent_ncl_id','').startswith('NCL-'):
                errors.append('bad_ncl_id=' + str(idx))
            if not row.get('parent_diff_id','').startswith('DIFF-'):
                errors.append('bad_diff_id=' + str(idx))
            if not row.get('canonical_url','').startswith('https://master.ricette.jp/derivatives/'):
                errors.append('bad_canonical_url=' + str(idx))
    print('check_set=next_10_selection_quality_v1')
    print('checked_rows=' + str(checked))
    if errors:
        print('\n'.join(errors[:30]))
        print('next_10_selection_quality_pass=false')
        return 1
    print('next_10_selection_quality_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
