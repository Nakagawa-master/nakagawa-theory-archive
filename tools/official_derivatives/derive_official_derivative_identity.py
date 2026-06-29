#!/usr/bin/env python3
import re

GREEK = {
    'α': 'alpha',
    'β': 'beta',
    'γ': 'gamma',
    'δ': 'delta',
}
CANONICAL_BASE = 'https://master.ricette.jp/derivatives/'
ORIGIN_BASE = 'https://master.ricette.jp/'


def folder_id_from_ncl(parent_ncl_id):
    value = parent_ncl_id.strip()
    for src, dst in GREEK.items():
        value = value.replace(src, dst)
    value = value.lower()
    value = re.sub(r'[^a-z0-9-]+', '-', value)
    value = re.sub(r'-+', '-', value).strip('-')
    return value


def canonical_url_from_folder(folder_id):
    folder = folder_id.strip().strip('/')
    return CANONICAL_BASE + folder + '/'


def expected_identity(parent_ncl_id):
    folder = folder_id_from_ncl(parent_ncl_id)
    return folder, canonical_url_from_folder(folder)


def row_has_origin_identity(row):
    return bool(row.get('parent_url','').strip() and row.get('parent_ncl_id','').strip() and row.get('parent_diff_id','').strip())


def row_identity_errors(row, label):
    errors = []
    parent_url = row.get('parent_url','').strip()
    parent_ncl_id = row.get('parent_ncl_id','').strip()
    parent_diff_id = row.get('parent_diff_id','').strip()
    folder_id = row.get('folder_id','').strip()
    canonical_url = row.get('canonical_url','').strip()
    if not row_has_origin_identity(row):
        return errors
    if not parent_url.startswith(ORIGIN_BASE):
        errors.append(label + ': bad_parent_url')
    if not parent_ncl_id.startswith('NCL-'):
        errors.append(label + ': bad_parent_ncl_id')
    if not parent_diff_id.startswith('DIFF-'):
        errors.append(label + ': bad_parent_diff_id')
    expected_folder, expected_canonical = expected_identity(parent_ncl_id)
    if folder_id and folder_id != expected_folder:
        errors.append(label + ': folder_id_mismatch expected=' + expected_folder + ' actual=' + folder_id)
    if canonical_url and canonical_url != expected_canonical:
        errors.append(label + ': canonical_url_mismatch expected=' + expected_canonical + ' actual=' + canonical_url)
    return errors
