#!/usr/bin/env python3
import csv
from pathlib import Path

QUEUE = Path('tools/official_derivatives/next_10_queue_candidate_10_19.tsv')
BUNDLE = Path('tools/official_derivatives/next_10_page_input_bundle_candidate_10_19.tsv')
VR = Path('tools/official_derivatives/next_10_vr_min_20260630.tsv')
ROLES = 'hub|human_summary|faq|ja_ai_index|en_ai_index|zh_ai_index'


def rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def active(row):
    return (row.get('selection_status') == 'candidate' and row.get('handoff_status') == 'intake_blocked') or (row.get('selection_status') == 'selected' and row.get('handoff_status') == 'intake_ready')


def main():
    q = rows(QUEUE)
    b = rows(BUNDLE)
    v = rows(VR)
    slots = {r.get('slot_id',''): r.get('folder_id','') for r in q if active(r)}
    errors = []
    seen = set()
    for r in b:
        slot = r.get('slot_id','')
        seen.add(slot)
        if slot not in slots:
            errors.append('slot_not_active=' + slot)
        elif r.get('folder_id','') != slots[slot]:
            errors.append('folder_mismatch=' + slot)
        if r.get('page_roles','') != ROLES:
            errors.append('roles_mismatch=' + slot)
        if r.get('input_state','') != 'pending':
            errors.append('state_not_pending=' + slot)
        if r.get('content_values_ready','') != 'true':
            errors.append('content_values_not_ready=' + slot)
        for key in ['public_export','page_generation']:
            if r.get(key,'') != 'false':
                errors.append(key + '_not_false=' + slot)
    if seen != set(slots):
        errors.append('slot_set_mismatch')
    v_seen = set()
    for r in v:
        slot = r.get('slot_id','')
        v_seen.add(slot)
        if slot not in slots:
            errors.append('vr_slot_not_active=' + slot)
        elif r.get('folder_id','') != slots[slot]:
            errors.append('vr_folder_mismatch=' + slot)
        if r.get('state','') != 'ok':
            errors.append('vr_state_not_ok=' + slot)
    if v_seen != set(slots):
        errors.append('vr_slot_set_mismatch')
    print('check_set=next_10_page_bundle_v4')
    print('active_slots=' + str(len(slots)))
    print('bundle_rows=' + str(len(b)))
    print('vr_rows=' + str(len(v)))
    print('content_values_ready=true')
    print('public_export=false')
    print('page_generation=false')
    if errors:
        print('\n'.join(errors[:50]))
        print('next_10_page_bundle_pass=false')
        return 1
    print('next_10_page_bundle_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
