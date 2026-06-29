#!/usr/bin/env python3
import csv
from pathlib import Path

QUEUE = Path('tools/official_derivatives/next_10_queue_candidate_10_19.tsv')
INTAKE = Path('tools/official_derivatives/next_batch_intake_candidate_10_19.tsv')
REQUIRED = ['batch_id','slot_id','source_status','parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url','hub_title','quality_gate_status','export_status']
READY = ['parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url']


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    queue = read(QUEUE)
    intake = read(INTAKE)
    ready_slots = {r.get('slot_id') for r in queue if r.get('selection_status') == 'selected' and r.get('handoff_status') == 'intake_ready'}
    intake_slots = {r.get('slot_id') for r in intake}
    errors = []
    if intake_slots != ready_slots:
        errors.append('intake_slot_set_mismatch')
    for row in intake:
        for key in REQUIRED:
            if not row.get(key,'').strip():
                errors.append('missing_' + key + '=' + row.get('slot_id','unknown'))
        for key in READY:
            if not row.get(key,'').strip():
                errors.append('missing_ready_field_' + key + '=' + row.get('slot_id','unknown'))
        if row.get('export_status') != 'private':
            errors.append('bad_export_status=' + row.get('slot_id','unknown'))
        if row.get('quality_gate_status') != 'pending':
            errors.append('bad_quality_gate_status=' + row.get('slot_id','unknown'))
        if not row.get('canonical_url','').startswith('https://master.ricette.jp/derivatives/'):
            errors.append('bad_canonical=' + row.get('slot_id','unknown'))
    print('check_set=next_10_intake_v1')
    print('queue_ready_slots=' + str(len(ready_slots)))
    print('intake_rows=' + str(len(intake)))
    if errors:
        print('\n'.join(errors[:30]))
        print('next_10_intake_pass=false')
        return 1
    print('next_10_intake_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
