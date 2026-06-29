#!/usr/bin/env python3
from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[2]
TARGETS = Path(__file__).resolve().parent / 'targets.tsv'
CHECK_FILES = [
    ROOT / 'deploy/lolipop/master-ricette/sitemap.xml',
    ROOT / 'deploy/lolipop/master-ricette/sitemap_index.xml',
    ROOT / 'deploy/lolipop/master-ricette/derivatives/index.html',
]
PAGE_SUFFIXES = ['', 'ja/human-summary/', 'ja/faq/', 'ja/ai-index/', 'en/ai-index/', 'zh/ai-index/']


def rows():
    with TARGETS.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def staged_patterns(folder):
    out = []
    for suffix in PAGE_SUFFIXES:
        rel = '/derivatives/' + folder + '/' + suffix
        out.append(rel)
        out.append('https://master.ricette.jp' + rel)
    return out


def main():
    print('check_set=staged_listing_v3')
    staged = [r['folder_id'] for r in rows() if r.get('export_status') == 'staged']
    errors = []
    checked = 0
    for path in CHECK_FILES:
        if not path.exists():
            continue
        checked += 1
        text = path.read_text(encoding='utf-8', errors='ignore')
        for folder in staged:
            for pattern in staged_patterns(folder):
                if pattern in text:
                    errors.append(str(path) + ' contains staged pattern ' + folder)
                    break
    if errors:
        print('\n'.join(errors))
        print('staged_listing_pass=false')
        return 1
    print('staged_targets=' + str(len(staged)))
    print('checked_listing_files=' + str(checked))
    print('staged_listing_pass=true')
    return 0


if __name__ == '__main__':
    sys.exit(main())
