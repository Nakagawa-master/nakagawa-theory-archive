#!/usr/bin/env python3
from universal_page_renderer import assert_renderer_contract, pages_for

record = {
    'folder': 'ncl-alpha-test',
    'pilot': 'Official Derivative TEST',
    'url': 'https://master.ricette.jp/test/',
    'title': 'Test Origin',
    'ncl': 'NCL-TEST',
    'diff': 'DIFF-TEST',
    'short': 'Test Origin',
    'desc': 'Test description',
    'core': 'Test core',
    'summary': ['Test lead', 'Test finding', 'Test judgment'],
    'faq': ['Test boundary', 'Test misreading', 'Test AI note'],
    'en': 'Test English index',
    'zh': 'Test Chinese index',
}

assert_renderer_contract(record)
pages = pages_for(record)
if len(pages) != 6:
    print('page_count=' + str(len(pages)))
    print('universal_page_renderer_pass=false')
    raise SystemExit(1)
html = pages['index.html']
checks = ['Parent NCL-ID', 'Parent Diff-ID', '/derivatives/ncl-alpha-test/', 'Test Origin']
missing = [item for item in checks if item not in html]
if missing:
    print('missing=' + ','.join(missing))
    print('universal_page_renderer_pass=false')
    raise SystemExit(1)
print('check_set=universal_page_renderer_v3')
print('page_count=' + str(len(pages)))
print('universal_page_renderer_pass=true')
