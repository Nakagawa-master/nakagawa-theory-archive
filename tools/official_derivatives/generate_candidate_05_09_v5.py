#!/usr/bin/env python3
from pathlib import Path
import importlib.util

from six_page_template_core import PAGES, assert_contract
from universal_page_renderer import pages_for

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'deploy/lolipop/master-ricette/derivatives'
DATA = Path(__file__).resolve().with_name('official_derivative_v5_data.py')


def load_targets():
    spec = importlib.util.spec_from_file_location('official_derivative_v5_data', DATA)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.TARGETS


def main():
    assert_contract()
    targets = load_targets()
    written = 0
    for record in targets:
        rendered = pages_for(record)
        for rel in PAGES:
            path = BASE / record['folder'] / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(rendered[rel], encoding='utf-8')
            written += 1
    print('target_count=' + str(len(targets)))
    print('generated_pages=' + str(written))
    print('renderer=universal_page_renderer_v5')
    print('template_controlled=true')
    print('candidate_05_09_v5_pass=' + str(len(targets) == 5 and written == 30).lower())
    if len(targets) != 5 or written != 30:
        raise SystemExit(1)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
