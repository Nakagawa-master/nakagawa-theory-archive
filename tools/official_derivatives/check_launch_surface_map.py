#!/usr/bin/env python3
import csv
from pathlib import Path
rows = list(csv.DictReader(Path('tools/official_derivatives/launch_surface_map.tsv').open(encoding='utf-8'), delimiter='\t'))
required = {'official_pages','human_summary','faq','ja_ai_index','en_ai_index','zh_ai_index','quote_propositions','sns_short_text','video_script','notebooklm_prompt','business_use','fatigue_society_use','religious_reading','spiritual_reading','rebuttal_pack','deviation_ledger','third_party_derivative_log'}
surfaces = {r.get('surface','') for r in rows}
print('check_set=launch_surface_map_v1')
if not required.issubset(surfaces):
    print('launch_surface_map_pass=false')
    raise SystemExit(1)
for row in rows:
    if row.get('origin_return') != 'yes' or row.get('abuse_guard') != 'yes':
        print('launch_surface_map_pass=false')
        raise SystemExit(1)
print('launch_surface_map_pass=true')
