#!/usr/bin/env python3
import csv
from pathlib import Path

QUEUE = Path('tools/official_derivatives/next_10_queue_candidate_10_19.tsv')
INTAKE = Path('tools/official_derivatives/next_batch_intake_candidate_10_19.tsv')
PRE_GATE = Path('tools/official_derivatives/next_10_pre_intake_gate_20260630.tsv')
BLUEPRINT = Path('tools/official_derivatives/next_10_content_blueprint_candidate_10_19.tsv')
FIELD_SPEC = Path('tools/official_derivatives/next_10_content_field_spec_candidate_10_19.tsv')
FIELDS = ['batch_id','slot_id','source_status','parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url','hub_title','human_summary_ready','faq_ready','ja_ai_index_ready','en_ai_index_ready','zh_ai_index_ready','quality_gate_status','export_status','notes']
READY = ['parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url']
ROLES = {'hub':'index.html','human_summary':'ja/human-summary/index.html','faq':'ja/faq/index.html','ja_ai_index':'ja/ai-index/index.html','en_ai_index':'en/ai-index/index.html','zh_ai_index':'zh/ai-index/index.html'}
MIN_FIELDS = {
    'hub': {'origin_identity','value_core','page_links','boundary_note','origin_return'},
    'human_summary': {'value_core','causal_line','reader_entry','misreading_guard','origin_return'},
    'faq': {'question_set','answer_set','boundary_condition','misreading_guard','origin_return'},
    'ja_ai_index': {'definition','scope','conditions','misreading_guard','origin_identity'},
    'en_ai_index': {'definition','scope','conditions','misreading_guard','origin_identity'},
    'zh_ai_index': {'definition','scope','conditions','misreading_guard','origin_identity'},
}
QUALITY_MARKER = 'intake_quality_passed'
GATE_PASS = {'gate_state':'passed','identity_ok':'true','score_ok':'true','plan_ok':'true','origin_ok':'true','allow_intake':'true'}


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def is_ready(row):
    return row.get('selection_status') == 'selected' and row.get('handoff_status') == 'intake_ready' and all(row.get(k,'').strip() for k in READY)


def gate_passed(row):
    return all(row.get(k,'') == v for k, v in GATE_PASS.items())


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


def blueprint_index(rows):
    result = {}
    for row in rows:
        slot = row.get('slot_id','')
        result.setdefault(slot, []).append(row)
    return result


def field_spec_ok(rows, errors):
    spec = {row.get('page_role',''): row for row in rows}
    if sorted(spec) != sorted(ROLES):
        errors.append('content_field_spec_roles_mismatch')
        return spec
    for role, needed in MIN_FIELDS.items():
        row = spec.get(role)
        fields = set(filter(None, row.get('required_fields','').split('|'))) if row else set()
        if not needed.issubset(fields):
            errors.append('content_field_spec_missing=' + role)
        if row and row.get('field_status') != 'spec_only':
            errors.append('content_field_status_not_spec_only=' + role)
        if row and row.get('public_export') != 'false':
            errors.append('content_field_public_export_not_false=' + role)
        if row and row.get('page_generation') != 'false':
            errors.append('content_field_page_generation_not_false=' + role)
    return spec


def blueprint_complete(slot, folder, rows, spec, errors):
    roles = sorted(row.get('page_role','') for row in rows)
    if roles != sorted(ROLES):
        errors.append('blueprint_roles_not_complete=' + slot)
        return False
    for row in rows:
        role = row.get('page_role','')
        if row.get('folder_id') != folder:
            errors.append('blueprint_folder_mismatch=' + slot)
        if role in ROLES and row.get('page_path') != ROLES[role]:
            errors.append('blueprint_path_mismatch=' + slot + ':' + role)
        if role not in spec:
            errors.append('blueprint_role_without_field_spec=' + slot + ':' + role)
        if row.get('blueprint_status') != 'planned':
            errors.append('blueprint_not_planned=' + slot + ':' + role)
        if row.get('origin_trace_status') != 'linked':
            errors.append('blueprint_origin_not_linked=' + slot + ':' + role)
        if row.get('page_generation') != 'false':
            errors.append('blueprint_page_generation_not_false=' + slot + ':' + role)
    return True


def main():
    queue = read(QUEUE)
    intake = read(INTAKE)
    gates = {row.get('slot_id',''): row for row in read(PRE_GATE)}
    blueprints = blueprint_index(read(BLUEPRINT))
    errors = []
    spec = field_spec_ok(read(FIELD_SPEC), errors)
    ready_queue = [row for row in queue if is_ready(row)]
    blocked_candidates = [row for row in queue if row.get('selection_status') == 'candidate' and row.get('handoff_status') == 'intake_blocked']
    expected = [expected_row(r) for r in ready_queue]
    if norm(intake) != expected:
        errors.append('intake_exactness_mismatch')
    for row in ready_queue:
        slot = row.get('slot_id','unknown')
        gate = gates.get(slot)
        blueprint_complete(slot, row.get('folder_id',''), blueprints.get(slot, []), spec, errors)
        if not gate:
            errors.append('missing_pre_intake_gate=' + slot)
        elif not gate_passed(gate):
            errors.append('pre_intake_gate_not_passed=' + slot)
        if QUALITY_MARKER not in row.get('notes',''):
            errors.append('missing_intake_quality_marker=' + slot)
    for row in blocked_candidates:
        slot = row.get('slot_id','unknown')
        gate = gates.get(slot)
        blueprint_complete(slot, row.get('folder_id',''), blueprints.get(slot, []), spec, errors)
        if not gate:
            errors.append('missing_blocked_pre_intake_gate=' + slot)
        else:
            if gate.get('plan_ok') != 'true':
                errors.append('blocked_plan_not_ready=' + slot)
            if gate.get('allow_intake') != 'false':
                errors.append('blocked_row_allows_intake=' + slot)
        if QUALITY_MARKER in row.get('notes',''):
            errors.append('blocked_row_has_quality_marker=' + slot)
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
    print('check_set=next_10_intake_v6')
    print('pre_intake_gate_rows=' + str(len(gates)))
    print('content_blueprint_slots=' + str(len(blueprints)))
    print('content_blueprint_rows=' + str(sum(len(v) for v in blueprints.values())))
    print('content_field_spec_roles=' + str(len(spec)))
    print('blocked_candidate_rows=' + str(len(blocked_candidates)))
    print('ready_queue_rows=' + str(len(ready_queue)))
    print('expected_intake_rows=' + str(len(expected)))
    print('actual_intake_rows=' + str(len(intake)))
    if errors:
        print('\n'.join(errors[:70]))
        print('next_10_intake_pass=false')
        return 1
    print('next_10_intake_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())