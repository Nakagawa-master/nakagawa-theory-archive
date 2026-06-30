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
EXPECTED_SLOTS = [f'Official Derivative {i:03d}' for i in range(10, 18)]


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames or [], list(reader)


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
        if row.get('batch_id') != 'candidate-10-19':
            errors.append('bad_batch=' + slot)
        if slot not in ready_queue:
            errors.append('slot_not_intake_ready=' + slot)
        if candidate_id not in ready_candidates:
            errors.append('candidate_not_ready=' + candidate_id)
        if slot in ready_queue and row.get('folder_id') != ready_queue[slot].get('folder_id'):
            errors.append('folder_mismatch=' + slot)
        for field in VALUE_FIELDS:
            if row.get(field) != 'derived':
                errors.append('field_not_derived=' + slot + ':' + field)
        for field in ['body_generation','public_export','page_generation']:
            if row.get(field) != 'false':
                errors.append('boundary_not_false=' + slot + ':' + field)
        if row.get('readiness_state') != 'value_ready':
            errors.append('bad_readiness_state=' + slot)
    print('check_set=next_10_value_ready_v1')
    print('value_ready_rows=' + str(len(rows)))
    if errors:
        print('\n'.join(errors[:60]))
        print('next_10_value_ready_pass=false')
        return 1
    print('next_10_value_ready_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
