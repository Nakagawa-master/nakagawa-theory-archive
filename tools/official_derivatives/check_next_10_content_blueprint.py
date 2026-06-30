#!/usr/bin/env python3
import csv
from pathlib import Path
from six_page_template_core import CONTRACT_SCOPE, PAGE_ROLES, PAGE_SET, TEMPLATE_VERSION, assert_contract

QUEUE = Path('tools/official_derivatives/next_10_queue_candidate_10_19.tsv')
BLUEPRINT = Path('tools/official_derivatives/next_10_content_blueprint_candidate_10_19.tsv')
FIELD_SPEC = Path('tools/official_derivatives/next_10_content_field_spec_candidate_10_19.tsv')
ROLES = PAGE_ROLES
HEADER = ['batch_id','slot_id','folder_id','page_role','page_path','blueprint_status','origin_trace_status','page_generation']
SPEC_HEADER = ['page_role','required_fields','field_status','public_export','page_generation']
MIN_FIELDS = {
    'hub': {'origin_identity','value_core','page_links','boundary_note','origin_return'},
    'human_summary': {'value_core','causal_line','reader_entry','misreading_guard','origin_return'},
    'faq': {'question_set','answer_set','boundary_condition','misreading_guard','origin_return'},
    'ja_ai_index': {'definition','scope','conditions','misreading_guard','origin_identity'},
    'en_ai_index': {'definition','scope','conditions','misreading_guard','origin_identity'},
    'zh_ai_index': {'definition','scope','conditions','misreading_guard','origin_identity'},
}

def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames or [], list(reader)

def main():
    assert_contract()
    _, queue = read(QUEUE)
    header, rows = read(BLUEPRINT)
    spec_header, spec_rows = read(FIELD_SPEC)
    slots = {r.get('slot_id',''): r.get('folder_id','') for r in queue if r.get('selection_status') == 'candidate' and r.get('handoff_status') == 'intake_blocked'}
    spec = {r.get('page_role',''): r for r in spec_rows}
    errors = []
    if header != HEADER: errors.append('bad_blueprint_header')
    if spec_header != SPEC_HEADER: errors.append('bad_spec_header')
    if sorted(spec) != sorted(ROLES): errors.append('spec_role_mismatch')
    by_slot = {slot: [] for slot in slots}
    for role, needed in MIN_FIELDS.items():
        row = spec.get(role)
        if not row:
            errors.append('missing_spec=' + role)
            continue
        fields = set(filter(None, row.get('required_fields','').split('|')))
        if not needed.issubset(fields): errors.append('missing_fields=' + role)
        if row.get('field_status') != 'spec_only': errors.append('bad_spec_state=' + role)
        if row.get('public_export') != 'false': errors.append('spec_public=' + role)
        if row.get('page_generation') != 'false': errors.append('spec_page=' + role)
    for row in rows:
        slot = row.get('slot_id','')
        role = row.get('page_role','')
        if slot not in slots:
            errors.append('slot_not_candidate=' + slot)
            continue
        by_slot[slot].append(role)
        if row.get('batch_id') != 'candidate-10-19': errors.append('bad_batch=' + slot)
        if row.get('folder_id') != slots[slot]: errors.append('bad_folder=' + slot)
        if role not in ROLES: errors.append('bad_role=' + role)
        elif row.get('page_path') != ROLES[role]: errors.append('bad_path=' + role)
        if row.get('blueprint_status') != 'planned': errors.append('bad_plan=' + slot)
        if row.get('origin_trace_status') != 'linked': errors.append('bad_origin=' + slot)
        if row.get('page_generation') != 'false': errors.append('bad_page=' + slot)
    for slot, roles in by_slot.items():
        if sorted(roles) != sorted(ROLES): errors.append('role_set=' + slot)
    if len(rows) != len(slots) * len(ROLES): errors.append('row_count')
    print('check_set=next_10_content_blueprint_v5')
    print('template_version=' + TEMPLATE_VERSION)
    print('page_set=' + PAGE_SET)
    print('contract_scope=' + CONTRACT_SCOPE)
    print('candidate_slots=' + str(len(slots)))
    print('content_blueprint_rows=' + str(len(rows)))
    if errors:
        print('\n'.join(errors[:60]))
        print('next_10_content_blueprint_pass=false')
        return 1
    print('next_10_content_blueprint_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
