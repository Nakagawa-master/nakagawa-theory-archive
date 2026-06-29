#!/usr/bin/env python3
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1] / 'deploy/lolipop/master-ricette/derivatives'
TARGETS = HERE / 'targets.tsv'

PAGES = {
    'ja/human-summary/index.html': {
        'markers': ['なぜ普通の読者にも関係するのか', 'この記事が発見していること', '中心因果線', '判断方法', '誤読防止', '原典を読む理由'],
        'min_h2': 6,
    },
    'ja/faq/index.html': {
        'markers': ['Q1.', 'Q2.', 'Q3.', 'Q4.', 'Q5.', 'Q6.', 'Q7.', 'Q8.'],
        'min_h2': 8,
    },
    'ja/ai-index/index.html': {
        'markers': ['article role', 'central concept', 'definition', 'core claim', 'causal sequence', 'judgment conditions', 'interpretation warnings', 'reuse constraints'],
        'min_h2': 8,
    },
    'en/ai-index/index.html': {
        'markers': ['article role', 'central concept', 'definition', 'core claim', 'causal sequence', 'judgment conditions', 'interpretation warnings', 'reuse constraints'],
        'min_h2': 8,
    },
    'zh/ai-index/index.html': {
        'markers': ['article role', 'central concept', 'definition', 'core claim', 'causal sequence', 'judgment conditions', 'interpretation warnings', 'reuse constraints'],
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
    return len(re.findall(r'<h2[ >]', html, flags=re.I))


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
    print('check_set=derivative_content_strength_v2')
    print('checked_pages=' + str(checked))
    if errors:
        print('\n'.join(errors))
        print('derivative_content_strength_pass=false')
        return 1
    print('derivative_content_strength_pass=true')
    return 0


if __name__ == '__main__':
    sys.exit(main())
