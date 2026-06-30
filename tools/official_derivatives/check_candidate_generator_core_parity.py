#!/usr/bin/env python3
import importlib.util
from pathlib import Path

import six_page_template_core as core

GENERATOR = Path(__file__).resolve().with_name('generate_candidate_05_09_html.py')
spec = importlib.util.spec_from_file_location('candidate_generator', GENERATOR)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

core.assert_contract()
errors = []
if list(mod.PAGES) != list(core.PAGES):
    errors.append('pages_mismatch')
if mod.SHARED_STYLE != core.SHARED_STYLE:
    errors.append('shared_style_mismatch')
if list(mod.CHILD_CARDS) != list(core.CHILD_CARDS):
    errors.append('child_cards_mismatch')

print('check_set=candidate_generator_core_parity_v1')
print('pages=' + str(len(core.PAGES)))
print('child_cards=' + str(len(core.CHILD_CARDS)))
if errors:
    print('\n'.join(errors))
    print('candidate_generator_core_parity_pass=false')
    raise SystemExit(1)
print('candidate_generator_core_parity_pass=true')
