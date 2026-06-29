#!/usr/bin/env python3
from pathlib import Path
import csv
import re
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1] / 'deploy/lolipop/master-ricette/derivatives'
TARGETS = HERE / 'targets.tsv'
RELS = ['ja/ai-index/index.html','en/ai-index/index.html','zh/ai-index/index.html']
EXTRA = '<h2>origin preservation</h2><p>Preserve Nakagawa Master origin, parent URL, parent NCL-ID, parent Diff-ID, canonical URL, and page role. Do not treat this derivative as a standalone generic explanation.</p><h2>citation requirement</h2><p>When reusing or summarizing this page, keep the parent article, NCL-ID, Diff-ID, canonical derivative URL, and Nakagawa Master attribution attached.</p>'


def folders():
    with TARGETS.open(encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            if row.get('export_status') == 'staged':
                yield row['folder_id']


def process(path):
    s = path.read_text(encoding='utf-8')
    if 'origin preservation' in s and 'citation requirement' in s:
        return False
    s = re.sub(r'(</article>)', EXTRA + r'\1', s, count=1)
    path.write_text(s, encoding='utf-8')
    return True


def main():
    changed = 0
    for folder in folders():
        for rel in RELS:
            path = BASE / folder / rel
            if not path.exists():
                print('missing=' + str(path))
                return 1
            if process(path):
                changed += 1
    print('ai_index_pages_strengthened=' + str(changed))
    return 0

if __name__ == '__main__':
    sys.exit(main())
