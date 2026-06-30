#!/usr/bin/env python3
from pathlib import Path
import importlib.util

from universal_renderer_contract import assert_input

LEGACY_05_09 = Path(__file__).resolve().with_name('generate_candidate_05_09_html.py')


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


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


def load_legacy_candidate_05_09():
    mod = load_module(LEGACY_05_09, 'legacy_candidate_05_09')
    return list(mod.TARGETS)


def load_universal_candidate_05_09():
    return [legacy_to_universal(record) for record in load_legacy_candidate_05_09()]


def main():
    rows = load_universal_candidate_05_09()
    print('adapter=official_derivative_target_adapter')
    print('candidate_05_09_universal_rows=' + str(len(rows)))
    print('adapter_pass=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
