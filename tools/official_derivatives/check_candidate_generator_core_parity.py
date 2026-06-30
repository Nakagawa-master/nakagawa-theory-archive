#!/usr/bin/env python3
import importlib.util
from pathlib import Path

import six_page_template_core as core
import universal_page_renderer as universal
from official_derivative_target_adapter import load_universal_candidate_05_09

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
adapter_rows = load_universal_candidate_05_09()
if len(adapter_rows) != len(mod.TARGETS):
    errors.append('adapter_count_mismatch')
checked = 0
for record in mod.TARGETS:
    current_pages = mod.pages_for(record)
    universal_pages = universal.pages_for(record)
    for rel in core.PAGES:
        checked += 1
        if current_pages.get(rel) != universal_pages.get(rel):
            errors.append('render_mismatch=' + record['folder'] + ':' + rel)

print('check_set=candidate_generator_core_parity_v3')
print('pages=' + str(len(core.PAGES)))
print('child_cards=' + str(len(core.CHILD_CARDS)))
print('adapter_rows=' + str(len(adapter_rows)))
print('render_checked=' + str(checked))
if errors:
    print('\n'.join(errors[:40]))
    print('candidate_generator_core_parity_pass=false')
    raise SystemExit(1)
print('candidate_generator_core_parity_pass=true')
