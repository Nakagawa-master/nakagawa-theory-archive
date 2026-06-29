#!/usr/bin/env python3
import csv
from collections import Counter
from pathlib import Path
root = Path('tools/official_derivatives')
units = list(csv.DictReader((root / 'priority_artifact_units_candidate_05_09.tsv').open(encoding='utf-8'), delimiter='\t'))
slots = list(csv.DictReader((root / 'priority_artifact_slots_candidate_05_09.tsv').open(encoding='utf-8'), delimiter='\t'))
print('check_set=priority_artifact_units_v1')
if len(units) != 10:
    print('priority_artifact_units_pass=false')
    raise SystemExit(1)
count_by_slot = Counter(u.get('slot_id') for u in units)
for slot in ['005','006','007','008','009']:
    if count_by_slot[slot] != 2:
        print('priority_artifact_units_pass=false')
        raise SystemExit(1)
slot_map = {s.get('slot_id'): s for s in slots}
for unit in units:
    slot = slot_map.get(unit.get('slot_id'))
    if not slot or unit.get('folder_id') != slot.get('folder_id'):
        print('priority_artifact_units_pass=false')
        raise SystemExit(1)
    if unit.get('target_layer') not in [slot.get('layer_a'), slot.get('layer_b')]:
        print('priority_artifact_units_pass=false')
        raise SystemExit(1)
    if unit.get('quality_floor') != 'ultra_high' or unit.get('origin_return') != 'yes' or unit.get('state') != 'pre_release':
        print('priority_artifact_units_pass=false')
        raise SystemExit(1)
    if unit.get('content_state') != 'empty':
        print('priority_artifact_units_pass=false')
        raise SystemExit(1)
print('priority_artifact_units_pass=true')
