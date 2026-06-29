#!/usr/bin/env python3
import csv
from pathlib import Path

ORIGIN = Path('tools/official_derivatives/origin_manifest.tsv')
CATALOG = Path('tools/official_derivatives/next_10_origin_catalog_candidate_10_19.tsv')
EXPECTED_HEADER = [
    'batch_id','origin_catalog_id','catalog_status','source_category','parent_url','parent_title',
    'parent_ncl_id','parent_diff_id','folder_id','canonical_url','already_in_origin_manifest',
    'public_safe_status','exclusion_status','exclusion_reason','structural_rationality_score',
    'origin_integrity_score','ai_index_fit_score','human_entry_fit_score','effect_expansion_score',
    'quality_risk_control_score','total_score','reason_for_inclusion','risk_note','review_notes'
]
CATEGORIES = {'theory','society','future','structural-reading','other'}
STATUSES = {'unreviewed','reviewed','blocked','ready_for_candidate'}
PUBLIC_SAFE = {'pending','pass','block'}
EXCLUSION = {'available','excluded','review_required'}
PRIVATE_MARKERS = {'private_only','internal_only','secret','token','credential','password'}


def read_rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames, list(reader)


def concrete(value):
    return value.strip() not in {'', 'none', 'pending', 'pending source selection'}


def score(row, key, errors, rid):
    value = row.get(key, '')
    try:
        number = int(value)
    except ValueError:
        errors.append('bad_score=' + rid + ':' + key)
        return None
    if number < 0 or number > 5:
        errors.append('bad_score_range=' + rid + ':' + key)
    return number


def main():
    origin_header, origin_rows = read_rows(ORIGIN)
    header, rows = read_rows(CATALOG)
    origin_urls = {row.get('parent_url', '') for row in origin_rows}
    errors = []
    if header != EXPECTED_HEADER:
        errors.append('bad_origin_catalog_header')
    seen = set()
    ready_count = 0
    for row in rows:
        rid = row.get('origin_catalog_id','')
        if rid in seen:
            errors.append('duplicate_origin_catalog_id=' + rid)
        seen.add(rid)
        if row.get('batch_id') != 'candidate-10-19':
            errors.append('bad_batch_id=' + rid)
        if not rid.startswith('OC-'):
            errors.append('bad_origin_catalog_id=' + rid)
        if row.get('catalog_status') not in STATUSES:
            errors.append('bad_catalog_status=' + rid)
        if row.get('source_category') not in CATEGORIES:
            errors.append('bad_source_category=' + rid)
        if row.get('public_safe_status') not in PUBLIC_SAFE:
            errors.append('bad_public_safe_status=' + rid)
        if row.get('exclusion_status') not in EXCLUSION:
            errors.append('bad_exclusion_status=' + rid)
        joined = '\n'.join(row.values()).lower()
        for marker in PRIVATE_MARKERS:
            if marker in joined:
                errors.append('private_marker=' + rid + ':' + marker)
        in_manifest = row.get('parent_url','') in origin_urls
        if row.get('already_in_origin_manifest') not in {'true','false'}:
            errors.append('bad_already_in_origin_manifest=' + rid)
        elif (row.get('already_in_origin_manifest') == 'true') != in_manifest:
            errors.append('origin_manifest_presence_mismatch=' + rid)
        if in_manifest and row.get('exclusion_status') != 'excluded':
            errors.append('manifest_origin_must_be_excluded=' + rid)
        scores = [score(row, key, errors, rid) for key in [
            'structural_rationality_score','origin_integrity_score','ai_index_fit_score',
            'human_entry_fit_score','effect_expansion_score','quality_risk_control_score'
        ]]
        if all(value is not None for value in scores):
            total = sum(scores)
            if row.get('total_score') != str(total):
                errors.append('score_total_mismatch=' + rid)
        if row.get('catalog_status') == 'ready_for_candidate':
            ready_count += 1
            for key in ['parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url','reason_for_inclusion','risk_note','exclusion_reason']:
                if not concrete(row.get(key,'')):
                    errors.append('missing_ready_field=' + rid + ':' + key)
            if not row.get('parent_url','').startswith('https://master.ricette.jp/'):
                errors.append('bad_parent_url=' + rid)
            if not row.get('parent_ncl_id','').startswith('NCL-'):
                errors.append('bad_parent_ncl_id=' + rid)
            if not row.get('parent_diff_id','').startswith('DIFF-'):
                errors.append('bad_parent_diff_id=' + rid)
            if not row.get('folder_id','').startswith('ncl-'):
                errors.append('bad_folder_id=' + rid)
            if not row.get('canonical_url','').startswith('https://master.ricette.jp/derivatives/'):
                errors.append('bad_canonical_url=' + rid)
            if row.get('already_in_origin_manifest') != 'false':
                errors.append('ready_origin_already_used=' + rid)
            if row.get('public_safe_status') != 'pass':
                errors.append('ready_public_safe_not_pass=' + rid)
            if row.get('exclusion_status') != 'available':
                errors.append('ready_not_available=' + rid)
            if all(value is not None for value in scores):
                if scores[1] != 5 or any(value < 4 for value in scores) or sum(scores) < 27:
                    errors.append('ready_score_below_gate=' + rid)
    print('check_set=next_10_origin_catalog_v1')
    print('origin_catalog_rows=' + str(len(rows)))
    print('ready_for_candidate_rows=' + str(ready_count))
    if errors:
        print('\n'.join(errors[:50]))
        print('next_10_origin_catalog_pass=false')
        return 1
    print('next_10_origin_catalog_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
