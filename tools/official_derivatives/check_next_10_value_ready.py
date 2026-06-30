#!/usr/bin/env python3
import csv
from pathlib import Path

LEDGER = Path('tools/official_derivatives/next_10_value_ready_candidate_10_19.tsv')
QUEUE = Path('tools/official_derivatives/next_10_queue_candidate_10_19.tsv')
CANDIDATES = Path('tools/official_derivatives/next_10_source_candidates_candidate_10_19.tsv')
HEADER = [
    'batch_id','slot_id','source_candidate_id','folder_id',
    'origin_identity','value_core','causal_line','misreading_guard',
    'origin_return','page_links','question_set','index_definition',
    'body_generation','public_export','page_generation','readiness_state',
]
VALUE_FIELDS = [
    'origin_identity','value_core','causal_line','misreading_guard',
    'origin_return','page_links','question_set','index_definition',
]
QUEUE_MATERIAL_FIELDS = [
    'reason_for_inclusion','risk_note','parent_url','parent_title',
    'parent_ncl_id','parent_diff_id','canonical_url',
]
CANDIDATE_MATERIAL_FIELDS = [
    'parent_title','reason_for_inclusion','risk_note','total_score',
]
EXPECTED_SLOTS = [f'Official Derivative {i:03d}' for i in range(10, 18)]


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames or [], list(reader)


def present(row, fields):
    return all(row.get(field, '').strip() for field in fields)


def main():
    header, rows = read(LEDGER)
    _, queue_rows = read(QUEUE)
    _, candidate_rows = read(CANDIDATES)
    errors = []
    ready_queue = {row['slot_id']: row for row in queue_rows if row.get('handoff_status') == 'intake_ready'}
    ready_candidates = {row['source_candidate_id']: row for row in candidate_rows if row.get('recommendation') == 'ready_for_queue'}
    if header != HEADER:
        errors.append('bad_value_ready_header')
    if len(rows) != 8:
        errors.append(f'value_ready_rows={len(rows)} expected=8')
    slots = [row.get('slot_id','') for row in rows]
    if slots != EXPECTED_SLOTS:
        errors.append('slot_sequence_mismatch')
    for row in rows:
        slot = row.get('slot_id','')
        candidate_id = row.get('source_candidate_id','')
        queue_row = ready_queue.get(slot)
        candidate_row = ready_candidates.get(candidate_id)
        if row.get('batch_id') != 'candidate-10-19':
            errors.append('bad_batch=' + slot)
        if queue_row is None:
            errors.append('slot_not_intake_ready=' + slot)
        if candidate_row is None:
            errors.append('candidate_not_ready=' + candidate_id)
        if queue_row and row.get('folder_id') != queue_row.get('folder_id'):
            errors.append('folder_mismatch=' + slot)
        if queue_row and not present(queue_row, QUEUE_MATERIAL_FIELDS):
            errors.append('queue_material_missing=' + slot)
        if candidate_row and not present(candidate_row, CANDIDATE_MATERIAL_FIELDS):
            errors.append('candidate_material_missing=' + candidate_id)
        if queue_row and candidate_row:
            for field in ['parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url']:
                if queue_row.get(field) != candidate_row.get(field):
                    errors.append('source_queue_mismatch=' + slot + ':' + field)
        for field in VALUE_FIELDS:
            if row.get(field) != 'derived':
                errors.append('field_not_derived=' + slot + ':' + field)
        for field in ['body_generation','public_export','page_generation']:
            if row.get(field) != 'false':
                errors.append('boundary_not_false=' + slot + ':' + field)
        if row.get('readiness_state') != 'value_ready':
            errors.append('bad_readiness_state=' + slot)
    print('check_set=next_10_value_ready_v2')
    print('value_ready_rows=' + str(len(rows)))
    if errors:
        print('\n'.join(errors[:80]))
        print('next_10_value_ready_pass=false')
        return 1
    print('next_10_value_ready_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
