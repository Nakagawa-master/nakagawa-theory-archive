#!/usr/bin/env python3
import csv
from pathlib import Path

QUEUE = Path('tools/official_derivatives/next_10_queue_candidate_10_19.tsv')
OUT = Path('tools/official_derivatives/next_batch_intake_candidate_10_19.tsv')
REPORT = Path('tools/official_derivatives/next_10_intake_report.md')
FIELDS = ['batch_id','slot_id','source_status','parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url','hub_title','human_summary_ready','faq_ready','ja_ai_index_ready','en_ai_index_ready','zh_ai_index_ready','quality_gate_status','export_status','notes']
SOURCE = ['parent_url','parent_title','parent_ncl_id','parent_diff_id','folder_id','canonical_url']


def read_queue():
    with QUEUE.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def ready(row):
    return row.get('selection_status') == 'selected' and row.get('handoff_status') == 'intake_ready' and all(row.get(k,'').strip() for k in SOURCE)


def hub_title(row):
    return row.get('slot_id','') + '｜' + row.get('parent_title','') + '｜公式派生物一覧'


def intake_row(row):
    return {
        'batch_id': row.get('batch_id',''),
        'slot_id': row.get('slot_id',''),
        'source_status': 'selected',
        'parent_url': row.get('parent_url',''),
        'parent_title': row.get('parent_title',''),
        'parent_ncl_id': row.get('parent_ncl_id',''),
        'parent_diff_id': row.get('parent_diff_id',''),
        'folder_id': row.get('folder_id',''),
        'canonical_url': row.get('canonical_url',''),
        'hub_title': hub_title(row),
        'human_summary_ready': 'false',
        'faq_ready': 'false',
        'ja_ai_index_ready': 'false',
        'en_ai_index_ready': 'false',
        'zh_ai_index_ready': 'false',
        'quality_gate_status': 'pending',
        'export_status': 'private',
        'notes': 'public-safe intake row generated from queue',
    }


def write_tsv(rows):
    with OUT.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


def write_report(queue_rows, intake_rows):
    lines = [
        '# Candidate 10-19 Intake Report',
        '',
        'This report is generated from the candidate 10-19 queue.',
        '',
        '## Status',
        '',
        '- production_deploy: false',
        '- sitemap_update: false',
        '- search_console: false',
        '- index_follow_conversion: false',
        '',
        '## Counts',
        '',
        '- queue_rows: ' + str(len(queue_rows)),
        '- intake_rows: ' + str(len(intake_rows)),
        '',
        '## Boundary',
        '',
        '- Only selected / intake_ready queue rows with complete origin metadata can enter intake.',
        '- Intake rows remain private and non-generated until quality gates pass.',
        '- No candidate 10-19 row is staged, deployed, indexed, or submitted from this builder.',
        '',
    ]
    REPORT.write_text('\n'.join(lines), encoding='utf-8')


def main():
    queue = read_queue()
    intake = [intake_row(r) for r in queue if ready(r)]
    write_tsv(intake)
    write_report(queue, intake)
    print('builder=next_10_intake_from_queue_v1')
    print('queue_rows=' + str(len(queue)))
    print('intake_rows=' + str(len(intake)))
    print('output=' + str(OUT))
    print('report=' + str(REPORT))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
