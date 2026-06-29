#!/usr/bin/env python3
import csv
from pathlib import Path

QUEUE = Path('tools/official_derivatives/next_10_queue_candidate_10_19.tsv')
BUNDLE = Path('tools/official_derivatives/next_10_page_input_bundle_candidate_10_19.tsv')
ROLES = 'hub|human_summary|faq|ja_ai_index|en_ai_index|zh_ai_index'


def rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    q = rows(QUEUE)
    b = rows(BUNDLE)
    slots = {r.get('slot_id',''): r.get('folder_id','') for r in q if r.get('selection_status') == 'candidate'}
    errors = []
    seen = set()
    for r in b:
        slot = r.get('slot_id','')
        seen.add(slot)
        if slot not in slots:
            errors.append('slot_not_candidate=' + slot)
        elif r.get('folder_id','') != slots[slot]:
            errors.append('folder_mismatch=' + slot)
        if r.get('page_roles','') != ROLES:
            errors.append('roles_mismatch=' + slot)
        if r.get('input_state','') != 'pending':
            errors.append('state_not_pending=' + slot)
        for key in ['public_export','page_generation','content_values_ready']:
            if r.get(key,'') != 'false':
                errors.append(key + '_not_false=' + slot)
    if seen != set(slots):
        errors.append('slot_set_mismatch')
    print('check_set=next_10_page_bundle_v1')
    print('candidate_slots=' + str(len(slots)))
    print('bundle_rows=' + str(len(b)))
    if errors:
        print('\n'.join(errors[:40]))
        print('next_10_page_bundle_pass=false')
        return 1
    print('next_10_page_bundle_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
