#!/usr/bin/env python3
import csv
from pathlib import Path

QUEUE = Path('tools/official_derivatives/next_10_queue_candidate_10_19.tsv')
INTAKE = Path('tools/official_derivatives/next_batch_intake_candidate_10_19.tsv')
REPORT = Path('tools/official_derivatives/next_10_intake_report.md')


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    queue_rows = len(read(QUEUE))
    intake_rows = len(read(INTAKE))
    text = REPORT.read_text(encoding='utf-8')
    required = [
        '- production_deploy: false',
        '- sitemap_update: false',
        '- search_console: false',
        '- index_follow_conversion: false',
        '- queue_rows: ' + str(queue_rows),
        '- intake_rows: ' + str(intake_rows),
        'No candidate 10-19 row is staged, deployed, indexed, or submitted from this builder.',
    ]
    errors = []
    for marker in required:
        if marker not in text:
            errors.append('missing_report_marker=' + marker)
    print('check_set=next_10_intake_report_v1')
    print('queue_rows=' + str(queue_rows))
    print('intake_rows=' + str(intake_rows))
    if errors:
        print('\n'.join(errors[:30]))
        print('next_10_intake_report_pass=false')
        return 1
    print('next_10_intake_report_pass=true')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
