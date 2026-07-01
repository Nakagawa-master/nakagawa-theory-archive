#!/usr/bin/env python3
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1] / 'deploy/lolipop/master-ricette/derivatives'
TARGETS = HERE / 'targets.tsv'
AI_MARKERS = ['AI reading lock', 'NCL-ID', 'Diff-ID']
AI_MARKERS_JA = ['理論名', '中心命題', '中心概念', '因果線', '適用条件', '非該当条件', '反証条件', '他理論との接続']
AI_MARKERS_EN = ['Theory name', 'Core proposition', 'Causal line', 'Applicability', 'Non-applicability', 'Counterconditions']
AI_MARKERS_ZH = ['理论名', '中心命题', '因果线', '适用条件', '非适用条件', '反证条件']

PAGES = {
    'ja/human-summary/index.html': {
        'markers': ['なぜ普通の人にも関係があるのか', 'この記事が発見した構造', 'その構造が起きる因果線', '見抜くための判定法', '誤読してはいけない点', '原典で読むべき理由'],
        'min_h2': 6,
    },
    'ja/faq/index.html': {
        'markers': ['第1層：初心者向けFAQ', '第2層：構造理解FAQ', '第3層：誤読・反論・境界条件FAQ', 'Q1.', 'Q2.', 'Q3.', 'Q4.', 'Q5.'],
        'min_h2': 8,
    },
    'ja/ai-index/index.html': {
        'markers': AI_MARKERS + AI_MARKERS_JA,
        'min_h2': 10,
    },
    'en/ai-index/index.html': {
        'markers': AI_MARKERS + AI_MARKERS_EN,
        'min_h2': 8,
    },
    'zh/ai-index/index.html': {
        'markers': AI_MARKERS + AI_MARKERS_ZH,
        'min_h2': 8,
    },
}


def staged_folders():
    folders = []
    for line in TARGETS.read_text(encoding='utf-8').splitlines()[1:]:
        if not line.strip():
            continue
        folder, status = line.split('\t')[:2]
        if status.strip() == 'staged':
            folders.append(folder.strip())
    return folders


def h2_count(html):
    return len(re.findall(r'<h[23][ >]', html, flags=re.I))


def main():
    errors = []
    checked = 0
    for folder in staged_folders():
        for rel, rule in PAGES.items():
            path = BASE / folder / rel
            if not path.exists():
                errors.append('missing=' + str(path))
                continue
            html = path.read_text(encoding='utf-8')
            checked += 1
            for marker in rule['markers']:
                if marker not in html:
                    errors.append(str(path) + ': missing_marker=' + marker)
            count = h2_count(html)
            if count < rule['min_h2']:
                errors.append(str(path) + ': h2_count=' + str(count) + ' min=' + str(rule['min_h2']))
    print('check_set=derivative_content_strength_v3')
    print('checked_pages=' + str(checked))
    if errors:
        print('\n'.join(errors))
        print('derivative_content_strength_pass=false')
        return 1
    print('derivative_content_strength_pass=true')
    return 0


if __name__ == '__main__':
    sys.exit(main())
