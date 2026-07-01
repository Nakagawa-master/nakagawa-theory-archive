#!/usr/bin/env python3
import importlib.util
from pathlib import Path

from six_page_template_core import PAGES

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'deploy/lolipop/master-ricette/derivatives'
DATA = Path(__file__).resolve().with_name('official_derivative_v5_data.py')

spec = importlib.util.spec_from_file_location('official_derivative_v5_data', DATA)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

targets = mod.TARGETS
errors = []
if len(targets) != 5:
    errors.append('target_count')

for record in targets:
    folder = record['folder']
    for rel in PAGES:
        path = BASE / folder / rel
        if not path.exists():
            errors.append('missing:' + folder + '/' + rel)
            continue
        html = path.read_text(encoding='utf-8')
        required = [
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
        for item in required:
            if item not in html:
                errors.append('missing:' + folder + '/' + rel + ':' + item)
        forbidden = ['6ページ構成', 'border-left:6px solid #1d4ed8']
        for item in forbidden:
            if item in html:
                errors.append('forbidden:' + folder + '/' + rel + ':' + item)
        if '<strong>直接リンク:</strong>' in html:
            block = html.split('<strong>直接リンク:</strong>', 1)[1].split('</nav>', 1)[0]
            if '原典' in block:
                errors.append('origin_in_direct_links:' + folder + '/' + rel)
        if rel == 'ja/human-summary/index.html':
            for item in ['なぜ普通の人にも関係があるのか', 'この記事が発見した構造', 'その構造が起きる因果線', '見抜くための判定法', '誤読してはいけない点', '原典で読むべき理由']:
                if item not in html:
                    errors.append('human_structure:' + folder + ':' + item)
        if rel == 'ja/faq/index.html':
            for item in ['第1層：初心者向けFAQ', '第2層：構造理解FAQ', '第3層：誤読・反論・境界条件FAQ']:
                if item not in html:
                    errors.append('faq_structure:' + folder + ':' + item)
        if 'ai-index' in rel:
            for item in ['AI reading lock', '適用', '反証']:
                if item not in html and rel.startswith('ja/'):
                    errors.append('ai_structure:' + folder + ':' + item)

print('check_set=candidate_05_09_v5')
print('target_count=' + str(len(targets)))
print('expected_pages=30')
if errors:
    print('\n'.join(errors[:80]))
    print('candidate_05_09_v5_pass=false')
    raise SystemExit(1)
print('candidate_05_09_v5_pass=true')
