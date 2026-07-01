#!/usr/bin/env python3
from pathlib import Path
import sys
from six_page_template_core import CHILD_CARDS, PAGES, assert_contract
import official_derivative_v5_data as data

BASE = Path(__file__).resolve().parents[2] / 'deploy/lolipop/master-ricette/derivatives'
REQUIRED_META = ['description','canonical','derivative-type','derivative-scope','language','parent-url','parent-ncl-id','parent-diff-id','pilot-id','render-status','origin-author','source-archive','ai-purpose','ai-summary','ai-interpretation-warning','ai-reuse-constraint','ai-origin-policy','ai-citation-requirement','official-derivative-template-version','official-derivative-page-set']
REQUIRED_STRUCT = ['class="wrap"','class="hero"','Parent NCL-ID','Parent Diff-ID','/derivatives/','background:#eef8f1','border-left:6px solid #2f855a']
HUB_CARD_PATHS = [card[2] for card in CHILD_CARDS]
PRIVATE_MARKERS = ['private_only','qgate_pending','public_export_allowed: false']
FORBIDDEN = ['6ページ構成','border-left:6px solid #1d4ed8']


def has_field(s, name):
    if name == 'canonical':
        return 'rel="canonical"' in s or "rel='canonical'" in s
    return f'name="{name}"' in s or f"name='{name}'" in s


def check(path, rel, record):
    folder = record['folder']
    if not path.exists():
        return [f'missing {path}']
    s = path.read_text(encoding='utf-8')
    errors = []
    for name in REQUIRED_META:
        if not has_field(s, name):
            errors.append(f'{path}: missing field {name}')
    for marker in REQUIRED_STRUCT:
        if marker not in s:
            errors.append(f'{path}: missing structure {marker}')
    for marker in [record['url'], record['ncl'], record['diff'], record['pilot']]:
        if marker not in s:
            errors.append(f'{path}: missing identity {marker}')
    if rel == 'index.html':
        for child in HUB_CARD_PATHS:
            if child not in s:
                errors.append(f'{path}: missing hub child link {child}')
    else:
        if f'/derivatives/{folder}/' not in s:
            errors.append(f'{path}: missing hub backlink')
    if 'ai-index' in rel:
        for marker in ['AI reading lock', '適用', '反証']:
            if rel.startswith('ja/') and marker not in s:
                errors.append(f'{path}: missing ai marker {marker}')
    if rel == 'ja/human-summary/index.html':
        for marker in ['なぜ普通の人にも関係があるのか', 'この記事が発見した構造', 'その構造が起きる因果線', '見抜くための判定法', '誤読してはいけない点', '原典で読むべき理由']:
            if marker not in s:
                errors.append(f'{path}: missing human marker {marker}')
    if rel == 'ja/faq/index.html':
        for marker in ['第1層：初心者向けFAQ', '第2層：構造理解FAQ', '第3層：誤読・反論・境界条件FAQ']:
            if marker not in s:
                errors.append(f'{path}: missing faq marker {marker}')
    if '<strong>直接リンク:</strong>' in s:
        block = s.split('<strong>直接リンク:</strong>', 1)[1].split('</nav>', 1)[0]
        if '原典' in block:
            errors.append(f'{path}: origin in direct links')
    for marker in PRIVATE_MARKERS + FORBIDDEN:
        if marker in s:
            errors.append(f'{path}: forbidden marker {marker}')
    return errors


def main():
    assert_contract()
    selected = data.TARGETS
    errors = []
    checked = 0
    for record in selected:
        for rel in PAGES:
            path = BASE / record['folder'] / rel
            errors.extend(check(path, rel, record))
            if path.exists():
                checked += 1
    expected = len(selected) * len(PAGES)
    if checked != expected:
        errors.append(f'checked_pages={checked} expected_pages={expected}')
    if errors:
        print('\n'.join(errors[:120]))
        print('template_parity_pass=false')
        return 1
    print('checked_pages=' + str(checked))
    print('template_parity_pass=true')
    return 0


if __name__ == '__main__':
    sys.exit(main())
