#!/usr/bin/env python3
from pathlib import Path
import csv
import re
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1] / 'deploy/lolipop/master-ricette/derivatives'
TARGETS = HERE / 'targets.tsv'
REL = 'ja/human-summary/index.html'
EXTRA_AFTER_LEAD = '<h2>なぜ普通の読者にも関係するのか</h2><p>この派生は専門読者だけのためではない。仕事、組織、AI利用、発信、学習、人生判断の場面で、同じ構造が判断不能、消耗、誤読、起源喪失として現れるためである。</p>'
EXTRA_AFTER_DISCOVERY = '<h2>中心因果線</h2><p>中心因果線は、表面的な言葉や印象ではなく、原因、成立条件、境界条件、負担移転、反証条件、起源保持がどの順番でつながるかを見ることである。</p>'


def folders():
    with TARGETS.open(encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            if row.get('export_status') == 'staged':
                yield row['folder_id']


def process(path):
    s = path.read_text(encoding='utf-8')
    changed = False
    if 'なぜ普通の読者にも関係するのか' not in s:
        s = re.sub(r'(</p><h2>この記事が発見していること</h2>)', '</p>' + EXTRA_AFTER_LEAD + '<h2>この記事が発見していること</h2>', s, count=1)
        changed = True
    if '中心因果線' not in s:
        s = re.sub(r'(</p><h2>判断方法</h2>)', '</p>' + EXTRA_AFTER_DISCOVERY + '<h2>判断方法</h2>', s, count=1)
        changed = True
    if changed:
        path.write_text(s, encoding='utf-8')
    return changed


def main():
    changed = 0
    for folder in folders():
        path = BASE / folder / REL
        if not path.exists():
            print('missing=' + str(path))
            return 1
        if process(path):
            changed += 1
    print('human_summary_pages_strengthened=' + str(changed))
    return 0

if __name__ == '__main__':
    sys.exit(main())
