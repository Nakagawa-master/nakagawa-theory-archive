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

all_html = '\n'.join(pages.values())
hub = pages['index.html']
checks = [
    'Parent NCL-ID',
    'Parent Diff-ID',
    '/derivatives/ncl-alpha-test/',
    'Test Origin',
    'noindex,nofollow',
    'official_derivative_staged_nonindexable',
    'AI reading lock',
    '第1層：初心者向けFAQ',
    'なぜ普通の人にも関係があるのか',
]
missing = [item for item in checks if item not in all_html]
forbidden = []
if '6ページ構成' in all_html:
    forbidden.append('six_page_label')
if 'border-left:6px solid #1d4ed8' in all_html:
    forbidden.append('blue_ai_border')
if '直接リンク:</strong>' in hub and '原典</a>' in hub.split('直接リンク:</strong>', 1)[1].split('</nav>', 1)[0]:
    forbidden.append('origin_in_quick_nav')
if missing or forbidden:
    if missing:
        print('missing=' + ','.join(missing))
    if forbidden:
        print('forbidden=' + ','.join(forbidden))
    print('universal_page_renderer_pass=false')
    raise SystemExit(1)

print('check_set=universal_page_renderer_v4')
print('page_count=' + str(len(pages)))
print('universal_page_renderer_pass=true')
