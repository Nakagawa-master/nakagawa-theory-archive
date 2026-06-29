#!/usr/bin/env python3
import csv
from pathlib import Path

QUEUE = Path('tools/official_derivatives/next_10_queue_candidate_10_19.tsv')
INTAKE = Path('tools/official_derivatives/next_batch_intake_candidate_10_19.tsv')
FIELDS = ['batch_id','slot_id','source_status','parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url','hub_title','human_summary_ready','faq_ready','ja_ai_index_ready','en_ai_index_ready','zh_ai_index_ready','quality_gate_status','export_status','notes']
READY = ['parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url']
QUALITY_MARKER = 'intake_quality_passed'


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def is_ready(row):
    return row.get('selection_status') == 'selected' and row.get('handoff_status') == 'intake_ready' and all(row.get(k,'').strip() for k in READY)


def expected_row(row):
    title = row.get('slot_id','') + '｜' + row.get('parent_title','') + '｜公式派生物一覧'
    return {
        'batch_id': row.get('batch_id',''),
        'slot_id': row.get('slot_id',''),
        'source_status': 'selected',
        'parent_url': row.get('parent_url',''),
        'parent_title': row.get('parent_title',''),
        'parent_ncl_id': row.get('parent_ncl_id',''),
        'parent_diff_id': row.get('parent_diff_id',''),
        'folder_id': row.get('folder_id',''),
        'canonical_url': row.get('canonical_url',''),
        'hub_title': title,
        'human_summary_ready': 'false',
        'faq_ready': 'false',
        'ja_ai_index_ready': 'false',
        'en_ai_index_ready': 'false',
        'zh_ai_index_ready': 'false',
        'quality_gate_status': 'pending',
        'export_status': 'private',
        'notes': 'public-safe intake row generated from queue',
    }


def norm(rows):
    return [{k: r.get(k,'') for k in FIELDS} for r in rows]


def main():
    queue = read(QUEUE)
    intake = read(INTAKE)
    ready_queue = [row for row in queue if is_ready(row)]
    blocked_candidates = [row for row in queue if row.get('selection_status') == 'candidate' and row.get('handoff_status') == 'intake_blocked']
    expected = [expected_row(r) for r in ready_queue]
    errors = []
    if norm(intake) != expected:
        errors.append('intake_exactness_mismatch')
    for row in ready_queue:
        slot = row.get('slot_id','unknown')
        if QUALITY_MARKER not in row.get('notes',''):
            errors.append('missing_intake_quality_marker=' + slot)
    for row in intake:
        slot = row.get('slot_id','unknown')
        for key in FIELDS:
            if key not in row:
                errors.append('missing_column_' + key)
        for key in READY:
            if not row.get(key,'').strip():
                errors.append('missing_ready_field_' + key + '=' + slot)
        if row.get('export_status') != 'private':
            errors.append('bad_export_status=' + slot)
        if row.get('quality_gate_status') != 'pending':
            errors.append('bad_quality_gate_status=' + slot)
        if not row.get('canonical_url','').startswith('https://master.ricette.jp/derivatives/'):
            errors.append('bad_canonical=' + slot)
    print('check_set=next_10_intake_v3')
    print('blocked_candidate_rows=' + str(len(blocked_candidates)))
    print('ready_queue_rows=' + str(len(ready_queue)))
    print('expected_intake_rows=' + str(len(expected)))
    print('actual_intake_rows=' + str(len(intake)))
    if errors:
        print('\n'.join(errors[:30]))
        print('next_10_intake_pass=false')
        return 1
    print('next_10_intake_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())