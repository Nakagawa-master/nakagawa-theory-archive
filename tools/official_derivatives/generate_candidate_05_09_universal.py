#!/usr/bin/env python3
from pathlib import Path
import importlib.util

from six_page_template_core import PAGES, assert_contract
from universal_page_renderer import pages_for

BASE = Path(__file__).resolve().parents[2] / 'deploy/lolipop/master-ricette/derivatives'
LEGACY = Path(__file__).resolve().with_name('generate_candidate_05_09_html.py')
CONTRACT = Path(__file__).resolve().with_name('template_parity_contract_v0_1.txt')


def load_targets():
    spec = importlib.util.spec_from_file_location('legacy_candidate_05_09', LEGACY)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.TARGETS


def main():
    assert_contract()
    if not CONTRACT.exists():
        print('missing template parity contract: ' + str(CONTRACT))
        return 1
    written = 0
    for record in load_targets():
        rendered = pages_for(record)
        for rel in PAGES:
            path = BASE / record['folder'] / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(rendered[rel], encoding='utf-8')
            written += 1
    print('generated_pages=' + str(written))
    print('renderer=universal_page_renderer')
    print('template_controlled=true')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
