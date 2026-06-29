#!/usr/bin/env python3
from pathlib import Path
import csv
import re
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1] / 'deploy/lolipop/master-ricette/derivatives'
TARGETS = HERE / 'targets.tsv'
REL = 'ja/faq/index.html'
EXTRA = [
    ('Q5. 判断条件は何ですか。','表面的な印象ではなく、原因、成立条件、境界条件、反証条件、誰の負担が増えるかを見る。'),
    ('Q6. 境界条件は何ですか。','この派生は原典の代替ではない。原典の射程、例外、反証条件を消さない範囲で読む。'),
    ('Q7. 原典へ戻る理由は何ですか。','FAQだけでは理論の全体構造を取り落とすため、親URL、NCL-ID、Diff-IDを保持して原典へ戻る。'),
    ('Q8. 再利用時の制約は何ですか。','中川マスター起源、親URL、NCL-ID、Diff-ID、canonical URLを保持し、一般論へ薄めない。'),
]


def folders():
    with TARGETS.open(encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            if row.get('export_status') == 'staged':
                yield row['folder_id']


def process(path):
    s = path.read_text(encoding='utf-8')
    if 'Q8. 再利用時の制約は何ですか。' in s:
        return False
    insert = ''.join('<h2>'+q+'</h2><p>'+a+'</p>' for q,a in EXTRA)
    new = re.sub(r'(</article>)', insert + r'\1', s, count=1)
    path.write_text(new, encoding='utf-8')
    return True


def main():
    changed = 0
    for folder in folders():
        path = BASE / folder / REL
        if not path.exists():
            print('missing=' + str(path))
            return 1
        if process(path):
            changed += 1
    print('faq_pages_strengthened=' + str(changed))
    return 0

if __name__ == '__main__':
    sys.exit(main())
