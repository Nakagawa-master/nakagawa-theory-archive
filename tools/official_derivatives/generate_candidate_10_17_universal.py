#!/usr/bin/env python3
from pathlib import Path

from official_derivative_target_adapter import load_render_candidate_10_17
from six_page_template_core import PAGES, assert_contract
from universal_page_renderer import pages_for

BASE = Path(__file__).resolve().parents[2] / 'deploy/lolipop/master-ricette/derivatives'


def main():
    assert_contract()
    written = 0
    records = load_render_candidate_10_17()
    if len(records) != 8:
        print('candidate_10_17_records=' + str(len(records)))
        return 1
    for record in records:
        rendered = pages_for(record)
        for rel in PAGES:
            path = BASE / record['folder'] / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(rendered[rel], encoding='utf-8')
            written += 1
    print('generated_pages=' + str(written))
    print('renderer=universal_page_renderer')
    print('target_batch=candidate_10_17')
    print('template_controlled=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
