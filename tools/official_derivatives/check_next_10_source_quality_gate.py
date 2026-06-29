#!/usr/bin/env python3
import csv
from pathlib import Path

CANDIDATES = Path('tools/official_derivatives/next_10_source_candidates_candidate_10_19.tsv')
QUEUE = Path('tools/official_derivatives/next_10_queue_candidate_10_19.tsv')
SCORE_FIELDS = [
    'structural_rationality_score','origin_integrity_score','ai_index_fit_score',
    'human_entry_fit_score','effect_expansion_score','quality_risk_control_score'
]


def rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def score(row, key):
    try:
        return int(row.get(key, ''))
    except ValueError:
        return None


def candidate_key(row):
    return (row.get('parent_url','').strip(), row.get('parent_ncl_id','').strip(), row.get('parent_diff_id','').strip())


def ready_candidate(row):
    scores = [score(row, key) for key in SCORE_FIELDS]
    if any(value is None for value in scores):
        return False
    if row.get('recommendation') != 'ready_for_queue':
        return False
    if row.get('source_status') != 'recommended':
        return False
    if row.get('public_safe_status') != 'pass':
        return False
    if scores[1] != 5:
        return False
    if any(value < 4 for value in scores):
        return False
    if sum(scores) < 27:
        return False
    if row.get('total_score') != str(sum(scores)):
        return False
    if row.get('reason_for_inclusion','').strip() in {'','none','pending source selection'}:
        return False
    if row.get('risk_note','').strip() in {'','none'}:
        return False
    if not row.get('parent_url','').startswith('https://master.ricette.jp/'):
        return False
    if not row.get('parent_ncl_id','').startswith('NCL-'):
        return False
    if not row.get('parent_diff_id','').startswith('DIFF-'):
        return False
    if not row.get('canonical_url','').startswith('https://master.ricette.jp/derivatives/'):
        return False
    return True


def main():
    candidate_rows = rows(CANDIDATES)
    queue_rows = rows(QUEUE)
    errors = []

    ready = {candidate_key(row): row for row in candidate_rows if ready_candidate(row)}
    malformed_ready = [row.get('source_candidate_id','') for row in candidate_rows if row.get('recommendation') == 'ready_for_queue' and not ready_candidate(row)]
    if malformed_ready:
        errors.append('malformed_ready_candidates=' + ','.join(malformed_ready))

    queue_active = 0
    for idx, row in enumerate(queue_rows, start=10):
        status = row.get('selection_status','')
        handoff = row.get('handoff_status','')
        active = status in {'candidate','selected'} or handoff in {'intake_ready','intake_blocked'}
        if not active:
            continue
        queue_active += 1
        key = candidate_key(row)
        if key not in ready:
            errors.append('queue_active_without_ready_source_candidate=' + str(idx))

    print('check_set=next_10_source_quality_gate_v1')
    print('source_candidate_rows=' + str(len(candidate_rows)))
    print('ready_for_queue_candidates=' + str(len(ready)))
    print('active_queue_rows=' + str(queue_active))
    if errors:
        print('\n'.join(errors[:50]))
        print('next_10_source_quality_gate_pass=false')
        return 1
    print('next_10_source_quality_gate_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
