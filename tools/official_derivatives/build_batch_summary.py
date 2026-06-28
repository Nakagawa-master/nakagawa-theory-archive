#!/usr/bin/env python3
from pathlib import Path
import csv
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1] / 'deploy/lolipop/master-ricette/derivatives'
TARGETS = HERE / 'targets.tsv'
MANIFEST = HERE / 'origin_manifest.tsv'
PAGES = ['index.html','ja/human-summary/index.html','ja/faq/index.html','ja/ai-index/index.html','en/ai-index/index.html','zh/ai-index/index.html']


def read_tsv(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    targets = read_tsv(TARGETS)
    manifest = read_tsv(MANIFEST)
    counts = {}
    missing = []
    checked = 0
    for row in targets:
        status = row.get('export_status','')
        folder = row.get('folder_id','')
        counts[status] = counts.get(status, 0) + 1
        for rel in PAGES:
            path = BASE / folder / rel
            if path.exists():
                checked += 1
            else:
                missing.append(str(path))
    expected = len(targets) * len(PAGES)
    print('summary_set=official_derivative_batch_v1')
    print('target_count=' + str(len(targets)))
    print('active_targets=' + str(counts.get('active', 0)))
    print('staged_targets=' + str(counts.get('staged', 0)))
    print('pages_per_target=' + str(len(PAGES)))
    print('expected_pages=' + str(expected))
    print('checked_pages=' + str(checked))
    print('manifest_rows=' + str(len(manifest)))
    if missing:
        print('batch_summary_pass=false')
        for item in missing:
            print('missing=' + item)
        return 1
    if len(manifest) != len(targets):
        print('batch_summary_pass=false')
        print('manifest_target_count_mismatch=true')
        return 1
    print('batch_summary_pass=true')
    return 0


if __name__ == '__main__':
    sys.exit(main())
