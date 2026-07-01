#!/usr/bin/env python3
import official_derivative_v5_data as data
import six_page_template_core as core
import universal_page_renderer as universal
from generate_candidate_05_09_v5 import load_targets

core.assert_contract()
errors = []
rows = load_targets()
if len(rows) != 5:
    errors.append('target_count')
if len(data.TARGETS) != 5:
    errors.append('data_count')
checked = 0
for record in rows:
    current_pages = universal.pages_for(record)
    for rel in core.PAGES:
        checked += 1
        if rel not in current_pages:
            errors.append('missing_render=' + record['folder'] + ':' + rel)
        else:
            html = current_pages[rel]
            for marker in ['noindex,nofollow', 'Parent NCL-ID', 'Parent Diff-ID', record['ncl'], record['diff'], record['url']]:
                if marker not in html:
                    errors.append('missing_marker=' + record['folder'] + ':' + rel + ':' + marker)

print('check_set=candidate_generator_core_parity_v5')
print('pages=' + str(len(core.PAGES)))
print('targets=' + str(len(rows)))
print('render_checked=' + str(checked))
if errors:
    print('\n'.join(errors[:40]))
    print('candidate_generator_core_parity_pass=false')
    raise SystemExit(1)
print('candidate_generator_core_parity_pass=true')
