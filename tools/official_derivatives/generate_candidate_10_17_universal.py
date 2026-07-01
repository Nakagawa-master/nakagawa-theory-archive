#!/usr/bin/env python3
from pathlib import Path
import importlib.util

from six_page_template_core import PAGES, assert_contract
from high_strength_body_renderer import pages_for_high_strength

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'deploy/lolipop/master-ricette/derivatives'
DATA = Path(__file__).resolve().with_name('official_derivative_v5_data_10_17.py')


def load_targets():
    spec = importlib.util.spec_from_file_location('official_derivative_v5_data_10_17', DATA)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.TARGETS_10_17


def main():
    assert_contract()
    targets = load_targets()
    written = 0
    for record in targets:
        rendered = pages_for_high_strength(record)
        for rel in PAGES:
            path = BASE / record['folder'] / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(rendered[rel], encoding='utf-8')
            written += 1
    print('target_count=' + str(len(targets)))
    print('generated_pages=' + str(written))
    print('renderer=high_strength_body_renderer_v5')
    print('template_controlled=true')
    print('candidate_10_17_universal_pass=' + str(len(targets) == 8 and written == 48).lower())
    if len(targets) != 8 or written != 48:
        raise SystemExit(1)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
