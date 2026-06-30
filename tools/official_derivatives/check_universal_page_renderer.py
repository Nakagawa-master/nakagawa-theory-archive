#!/usr/bin/env python3
from universal_page_renderer import assert_renderer_contract, child_cards, hero, nav, shell

record = {
    'folder_id': 'ncl-alpha-test',
    'slot_id': 'Official Derivative TEST',
    'parent_url': 'https://master.ricette.jp/test/',
    'parent_title': 'Test Origin',
    'parent_ncl_id': 'NCL-TEST',
    'parent_diff_id': 'DIFF-TEST',
    'canonical_url': 'https://master.ricette.jp/derivatives/ncl-alpha-test/',
    'value_core': 'core',
    'causal_line': 'causal',
    'misreading_guard': 'guard',
    'origin_return': 'https://master.ricette.jp/test/',
    'public_export': 'false',
    'page_generation': 'false',
}

assert_renderer_contract(record)
text = shell(record, 'index.html', 'Test Title', '<article>' + child_cards(record) + '</article>')
checks = ['class="hero"', 'Parent NCL-ID', 'Parent Diff-ID', '/derivatives/ncl-alpha-test/', 'Test Origin']
missing = [item for item in checks if item not in text]
if missing:
    print('missing=' + ','.join(missing))
    print('universal_page_renderer_pass=false')
    raise SystemExit(1)
print('check_set=universal_page_renderer_v1')
print('universal_page_renderer_pass=true')
