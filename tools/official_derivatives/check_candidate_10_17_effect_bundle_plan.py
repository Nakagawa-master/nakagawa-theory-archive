#!/usr/bin/env python3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXPECTED = ROOT / 'effect_bundles' / 'candidate_10_17_effect_bundle_expected_counts.tsv'
TARGETS = ROOT / 'targets.tsv'
QUEUE = ROOT / 'next_10_queue_candidate_10_19.tsv'
SPEC = ROOT / 'effect_bundles' / 'candidate_10_17_unit_materialization_spec.md'


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    expected = read(EXPECTED)
    staged = {r['folder_id'] for r in read(TARGETS) if r.get('export_status') == 'staged'}
    selected = {r['folder_id'] for r in read(QUEUE) if r.get('selection_status') == 'selected' and r.get('handoff_status') == 'intake_ready'}
    errors = []
    total = 0
    folders = set()
    for row in expected:
        folder = row['folder_id']
        folders.add(folder)
        if folder not in staged:
            errors.append('not_staged=' + folder)
        if folder not in selected:
            errors.append('not_selected=' + folder)
        subtotal = int(row['quote_units']) + int(row['social_units']) + int(row['objection_or_clarification_units']) + int(row['notebooklm_units'])
        total += subtotal
        if subtotal != int(row['total_units']):
            errors.append('subtotal_mismatch=' + folder)
        if row.get('status_record_expected') != 'yes':
            errors.append('status_record_expected=' + folder)
        if row.get('public_activation') != 'false':
            errors.append('public_activation=' + folder)
        if row.get('production_deploy') != 'false':
            errors.append('production_deploy=' + folder)
    if len(expected) != 8:
        errors.append('row_count=' + str(len(expected)))
    if total != 264:
        errors.append('total_units=' + str(total))
    if not SPEC.exists():
        errors.append('missing_materialization_spec')
    print('check_set=candidate_10_17_effect_bundle_plan_v2')
    print('origin_count=' + str(len(folders)))
    print('expected_total_units=' + str(total))
    print('spec_exists=' + str(SPEC.exists()).lower())
    print('public_activation=false')
    print('production_deploy=false')
    if errors:
        print('\n'.join(errors[:30]))
        print('candidate_10_17_effect_bundle_plan_pass=false')
        return 1
    print('candidate_10_17_effect_bundle_plan_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
