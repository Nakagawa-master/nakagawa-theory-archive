#!/usr/bin/env python3
import csv
from pathlib import Path

QUEUE = Path('tools/official_derivatives/next_10_queue_candidate_10_19.tsv')
BLUEPRINT = Path('tools/official_derivatives/next_10_content_blueprint_candidate_10_19.tsv')
FIELD_SPEC = Path('tools/official_derivatives/next_10_content_field_spec_candidate_10_19.tsv')
ROLES = {
    'hub': 'index.html',
    'human_summary': 'ja/human-summary/index.html',
    'faq': 'ja/faq/index.html',
    'ja_ai_index': 'ja/ai-index/index.html',
    'en_ai_index': 'en/ai-index/index.html',
    'zh_ai_index': 'zh/ai-index/index.html',
}
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
    _, queue = read(QUEUE)
    header, rows = read(BLUEPRINT)
    spec_header, spec_rows = read(FIELD_SPEC)
    candidate_slots = {
        row.get('slot_id',''): row.get('folder_id','')
        for row in queue
        if row.get('selection_status') == 'candidate' and row.get('handoff_status') == 'intake_blocked'
    }
    errors = []
    spec = {row.get('page_role',''): row for row in spec_rows}
    if header != HEADER:
        errors.append('bad_content_blueprint_header')
    if spec_header != SPEC_HEADER:
        errors.append('bad_content_field_spec_header')
    if sorted(spec) != sorted(ROLES):
        errors.append('content_field_spec_roles_mismatch')
    for role, needed in MIN_FIELDS.items():
        row = spec.get(role)
        if not row:
            continue
        fields = set(filter(None, row.get('required_fields','').split('|')))
        if not needed.issubset(fields):
            errors.append('content_field_spec_missing=' + role)
        if row.get('field_status') != 'spec_only':
            errors.append('content_field_status_not_spec_only=' + role)
        if row.get('public_export') != 'false':
            errors.append('content_field_public_export_not_false=' + role)
        if row.get('page_generation') != 'false':
            errors.append('content_field_page_generation_not_false=' + role)
    by_slot = {slot: [] for slot in candidate_slots}
    for row in rows:
        slot = row.get('slot_id','')
        role = row.get('page_role','')
        if slot not in candidate_slots:
            errors.append('blueprint_slot_not_candidate=' + slot)
            continue
        by_slot[slot].append(row)
        if row.get('batch_id') != 'candidate-10-19':
            errors.append('bad_batch=' + slot)
        if row.get('folder_id') != candidate_slots[slot]:
            errors.append('folder_mismatch=' + slot)
        if role not in ROLES:
            errors.append('bad_page_role=' + slot + ':' + role)
        elif row.get('page_path') != ROLES[role]:
            errors.append('bad_page_path=' + slot + ':' + role)
        if role not in spec:
            errors.append('blueprint_role_without_field_spec=' + slot + ':' + role)
        if row.get('blueprint_status') != 'planned':
            errors.append('bad_blueprint_status=' + slot + ':' + role)
        if row.get('origin_trace_status') != 'linked':
            errors.append('bad_origin_trace_status=' + slot + ':' + role)
        if row.get('page_generation') != 'false':
            errors.append('page_generation_not_false=' + slot + ':' + role)
    for slot, slot_rows in by_slot.items():
        roles = sorted(row.get('page_role','') for row in slot_rows)
        if roles != sorted(ROLES):
            errors.append('missing_or_extra_roles=' + slot)
    if len(rows) != len(candidate_slots) * len(ROLES):
        errors.append('blueprint_rows=' + str(len(rows)) + ':expected=' + str(len(candidate_slots) * len(ROLES)))
    print('check_set=next_10_content_blueprint_v2')
    print('candidate_slots=' + str(len(candidate_slots)))
    print('content_blueprint_rows=' + str(len(rows)))
    print('content_field_spec_roles=' + str(len(spec_rows)))
    print('public_export=false')
    print('page_generation=false')
    if errors:
        print('\n'.join(errors[:60]))
        print('next_10_content_blueprint_pass=false')
        return 1
    print('next_10_content_blueprint_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())