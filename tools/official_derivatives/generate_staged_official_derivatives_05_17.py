#!/usr/bin/env python3
from pathlib import Path
import importlib.util

from six_page_template_core import PAGES, assert_contract
from high_strength_body_renderer import pages_for_high_strength
from official_derivative_v5_data_10_17 import TARGETS_10_17

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'deploy/lolipop/master-ricette/derivatives'
DATA_05_09 = Path(__file__).resolve().with_name('official_derivative_v5_data.py')


def load_05_09():
    spec = importlib.util.spec_from_file_location('official_derivative_v5_data', DATA_05_09)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return list(mod.TARGETS)


def main():
    assert_contract()
    targets = load_05_09() + list(TARGETS_10_17)
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
    print('renderer=high_strength_body_renderer_v5_05_17')
    print('staged_official_derivatives_05_17_pass=' + str(len(targets) == 13 and written == 78).lower())
    if len(targets) != 13 or written != 78:
        raise SystemExit(1)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
