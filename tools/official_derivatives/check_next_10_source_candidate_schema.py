#!/usr/bin/env python3
import csv
from pathlib import Path

SCHEMA = Path('tools/official_derivatives/next_10_source_candidate_schema.tsv')
CANDIDATES = Path('tools/official_derivatives/next_10_source_candidates_candidate_10_19.tsv')

SCHEMA_FIELDS = ['field_name','required','allowed_values','description','public_safe_note']
CANDIDATE_FIELDS = [
    'batch_id','source_candidate_id','source_status','source_category','parent_url','parent_title',
    'parent_ncl_id','parent_diff_id','folder_id','canonical_url','structural_rationality_score',
    'origin_integrity_score','ai_index_fit_score','human_entry_fit_score','effect_expansion_score',
    'quality_risk_control_score','total_score','public_safe_status','recommendation',
    'reason_for_inclusion','risk_note','review_notes'
]
STATUS = {'unscored','scored','recommended','blocked','rejected'}
CATEGORIES = {'theory','society','future','structural-reading','other'}
PUBLIC_SAFE = {'pending','pass','block'}
RECOMMENDATIONS = {'defer','ready_for_queue','reject','blocked'}
PRIVATE_MARKERS = {'private_only','internal_only','qgate_pending','secret','token','credential'}
SCORE_FIELDS = [
    'structural_rationality_score','origin_integrity_score','ai_index_fit_score',
    'human_entry_fit_score','effect_expansion_score','quality_risk_control_score'
]


def read_rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames or [], list(reader)


def nonempty(row, key):
    return bool(row.get(key, '').strip())


def as_score(value):
    if value == '':
        return None
    try:
        score = int(value)
    except ValueError:
        return None
    if score < 0 or score > 5:
        return None
    return score


def has_private_marker(row):
    haystack = '\t'.join(str(v).lower() for v in row.values())
    return any(marker in haystack for marker in PRIVATE_MARKERS)


def main():
    errors = []
    schema_fields, schema_rows = read_rows(SCHEMA)
    candidate_fields, candidate_rows = read_rows(CANDIDATES)

    if schema_fields != SCHEMA_FIELDS:
        errors.append('schema_header_mismatch')
    schema_field_names = [row.get('field_name','') for row in schema_rows]
    missing_schema = [field for field in CANDIDATE_FIELDS if field not in schema_field_names]
    if missing_schema:
        errors.append('schema_missing_fields=' + ','.join(missing_schema))

    if candidate_fields != CANDIDATE_FIELDS:
        errors.append('candidate_header_mismatch')

    for line_no, row in enumerate(candidate_rows, start=2):
        label = str(line_no)
        if row.get('batch_id') != 'candidate-10-19':
            errors.append('bad_batch_id=' + label)
        if not row.get('source_candidate_id','').startswith('SC-'):
            errors.append('bad_source_candidate_id=' + label)
        if row.get('source_status') not in STATUS:
            errors.append('bad_source_status=' + label)
        if row.get('source_category') not in CATEGORIES:
            errors.append('bad_source_category=' + label)
        if row.get('public_safe_status') not in PUBLIC_SAFE:
            errors.append('bad_public_safe_status=' + label)
        if row.get('recommendation') not in RECOMMENDATIONS:
            errors.append('bad_recommendation=' + label)
        if has_private_marker(row):
            errors.append('private_marker_present=' + label)

        active = row.get('source_status') in {'scored','recommended'} or row.get('recommendation') == 'ready_for_queue'
        if active:
            for key in ['parent_url','parent_title','parent_ncl_id','parent_diff_id','reason_for_inclusion','risk_note']:
                if not nonempty(row, key):
                    errors.append('active_missing_' + key + '=' + label)
            if not row.get('parent_url','').startswith('https://master.ricette.jp/'):
                errors.append('bad_parent_url=' + label)
            if not row.get('parent_ncl_id','').startswith('NCL-'):
                errors.append('bad_parent_ncl_id=' + label)
            if not row.get('parent_diff_id','').startswith('DIFF-'):
                errors.append('bad_parent_diff_id=' + label)
            scores = [as_score(row.get(key,'')) for key in SCORE_FIELDS]
            if any(score is None for score in scores):
                errors.append('active_bad_score=' + label)
            else:
                total = str(sum(scores))
                if row.get('total_score') != total:
                    errors.append('bad_total_score=' + label)

        ready = row.get('recommendation') == 'ready_for_queue'
        if ready:
            for key in ['folder_id','canonical_url']:
                if not nonempty(row, key):
                    errors.append('ready_missing_' + key + '=' + label)
            if not row.get('canonical_url','').startswith('https://master.ricette.jp/derivatives/'):
                errors.append('bad_canonical_url=' + label)
            if row.get('public_safe_status') != 'pass':
                errors.append('ready_without_public_safe_pass=' + label)

    print('check_set=next_10_source_candidate_schema_v1')
    print('schema_fields=' + str(len(schema_rows)))
    print('candidate_rows=' + str(len(candidate_rows)))
    if errors:
        print('\n'.join(errors[:50]))
        print('next_10_source_candidate_schema_pass=false')
        return 1
    print('next_10_source_candidate_schema_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
