#!/usr/bin/env python3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXPECTED = ROOT / 'effect_bundles' / 'candidate_10_17_effect_bundle_expected_counts.tsv'
TARGETS = ROOT / 'targets.tsv'
QUEUE = ROOT / 'next_10_queue_candidate_10_19.tsv'
SPEC = ROOT / 'effect_bundles' / 'candidate_10_17_unit_materialization_spec.md'
SUMMARY = ROOT / 'effect_bundles' / 'staged_effect_expansion_summary.tsv'


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def first_summary(summary, scopes):
    for scope in scopes:
        if scope in summary:
            return summary[scope]
    return {}


def main():
    expected = read(EXPECTED)
    staged = {r['folder_id'] for r in read(TARGETS) if r.get('export_status') == 'staged'}
    selected = {r['folder_id'] for r in read(QUEUE) if r.get('selection_status') == 'selected' and r.get('handoff_status') == 'intake_ready'}
    summary = {r['scope']: r for r in read(SUMMARY)} if SUMMARY.exists() else {}
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

    summary_10_17 = first_summary(summary, ['candidate_10_17_materialized', 'candidate_10_17_planned'])
    summary_total = first_summary(summary, ['staged_total_materialized', 'staged_total'])
    if summary_10_17.get('total_units') != '264':
        errors.append('summary_10_17_total')
    if summary_total.get('total_units') != '429':
        errors.append('summary_staged_total')
    if summary_10_17 and summary_10_17.get('public_activation') != 'false':
        errors.append('summary_10_17_public_activation')
    if summary_10_17 and summary_10_17.get('production_deploy') != 'false':
        errors.append('summary_10_17_production_deploy')
    if summary_total and summary_total.get('public_activation') != 'false':
        errors.append('summary_total_public_activation')
    if summary_total and summary_total.get('production_deploy') != 'false':
        errors.append('summary_total_production_deploy')

    print('check_set=candidate_10_17_effect_bundle_plan_v4')
    print('origin_count=' + str(len(folders)))
    print('expected_total_units=' + str(total))
    print('spec_exists=' + str(SPEC.exists()).lower())
    print('summary_exists=' + str(SUMMARY.exists()).lower())
    print('summary_10_17_scope=' + summary_10_17.get('scope', 'missing'))
    print('summary_total_scope=' + summary_total.get('scope', 'missing'))
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
