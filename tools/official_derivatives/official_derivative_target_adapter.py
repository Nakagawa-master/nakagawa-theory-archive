#!/usr/bin/env python3
from pathlib import Path
import csv
import importlib.util

from universal_renderer_contract import assert_input

HERE = Path(__file__).resolve().parent
LEGACY_05_09 = HERE / 'generate_candidate_05_09_html.py'
SOURCE_10_19 = HERE / 'next_10_source_candidates_candidate_10_19.tsv'


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def read_tsv(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def legacy_to_universal(record):
    mapped = {
        'folder_id': record['folder'],
        'slot_id': record['pilot'],
        'parent_url': record['url'],
        'parent_title': record['title'],
        'parent_ncl_id': record['ncl'],
        'parent_diff_id': record['diff'],
        'canonical_url': 'https://master.ricette.jp/derivatives/' + record['folder'] + '/',
        'value_core': record['core'],
        'causal_line': record['summary'][1],
        'misreading_guard': record['faq'][1],
        'origin_return': record['url'],
        'public_export': 'false',
        'page_generation': 'false',
    }
    assert_input(mapped)
    return mapped


def source_candidate_to_seed(row, slot_id):
    mapped = {
        'folder_id': row['folder_id'],
        'slot_id': slot_id,
        'parent_url': row['parent_url'],
        'parent_title': row['parent_title'],
        'parent_ncl_id': row['parent_ncl_id'],
        'parent_diff_id': row['parent_diff_id'],
        'canonical_url': row['canonical_url'],
        'value_core': row['reason_for_inclusion'],
        'causal_line': row['reason_for_inclusion'],
        'misreading_guard': row['risk_note'],
        'origin_return': row['parent_url'],
        'public_export': 'false',
        'page_generation': 'false',
    }
    assert_input(mapped)
    return mapped


def load_legacy_candidate_05_09():
    mod = load_module(LEGACY_05_09, 'legacy_candidate_05_09')
    return list(mod.TARGETS)


def load_universal_candidate_05_09():
    return [legacy_to_universal(record) for record in load_legacy_candidate_05_09()]


def load_universal_candidate_10_17_seed():
    rows = [r for r in read_tsv(SOURCE_10_19) if r.get('recommendation') == 'ready_for_queue']
    return [source_candidate_to_seed(row, 'Official Derivative ' + str(10 + i).zfill(3)) for i, row in enumerate(rows)]


def main():
    rows_05_09 = load_universal_candidate_05_09()
    rows_10_17 = load_universal_candidate_10_17_seed()
    print('adapter=official_derivative_target_adapter')
    print('candidate_05_09_universal_rows=' + str(len(rows_05_09)))
    print('candidate_10_17_seed_rows=' + str(len(rows_10_17)))
    print('adapter_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
