#!/usr/bin/env python3
from pathlib import Path

from six_page_template_core import PAGES, TEMPLATE_VERSION, assert_contract
import official_derivative_v5_data as data

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'deploy/lolipop/master-ricette/derivatives'

assert_contract()
records = data.TARGETS
errors = []

if not records:
    errors.append('no_records')

for record in records:
    folder = record['folder']
    for rel in PAGES:
        path = BASE / folder / rel
        if not path.exists():
            errors.append('missing_page:' + folder + ':' + rel)
            continue
        html = path.read_text(encoding='utf-8')
        required = [
            TEMPLATE_VERSION,
            'noindex,nofollow',
            'official_derivative_staged_nonindexable',
            'Parent NCL-ID',
            'Parent Diff-ID',
            record['ncl'],
            record['diff'],
            record['url'],
            '/derivatives/' + folder + '/',
            'background:#eef8f1',
            'border-left:6px solid #2f855a',
        ]
        for marker in required:
            if marker not in html:
                errors.append('missing_marker:' + folder + ':' + rel + ':' + marker)
        for marker in ['6ページ構成', 'border-left:6px solid #1d4ed8']:
            if marker in html:
                errors.append('forbidden_marker:' + folder + ':' + rel + ':' + marker)
        if '<strong>直接リンク:</strong>' in html:
            direct = html.split('<strong>直接リンク:</strong>', 1)[1].split('</nav>', 1)[0]
            if '原典' in direct:
                errors.append('origin_in_direct_links:' + folder + ':' + rel)

expected_pages = len(records) * len(PAGES)
print('check_set=official_derivative_v5_global_contract')
print('template_version=' + TEMPLATE_VERSION)
print('target_count=' + str(len(records)))
print('expected_pages=' + str(expected_pages))
if errors:
    print('\n'.join(errors[:120]))
    print('official_derivative_v5_global_contract_pass=false')
    raise SystemExit(1)
print('official_derivative_v5_global_contract_pass=true')
