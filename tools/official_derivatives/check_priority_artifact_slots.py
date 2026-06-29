#!/usr/bin/env python3
import csv
from pathlib import Path
rows = list(csv.DictReader(Path('tools/official_derivatives/priority_artifact_slots_candidate_05_09.tsv').open(encoding='utf-8'), delimiter='\t'))
print('check_set=priority_artifact_slots_v2')
expected_slots = ['005','006','007','008','009']
expected_folders = ['ncl-alpha-20260511-e243be','ncl-alpha-20260416-0b1b93','ncl-alpha-20260418-11c3d8','ncl-alpha-20260607-7e87f5','ncl-alpha-20260613-007d94']
if len(rows) != 5:
    print('priority_artifact_slots_pass=false')
    raise SystemExit(1)
if [r.get('slot_id') for r in rows] != expected_slots:
    print('priority_artifact_slots_pass=false')
    raise SystemExit(1)
if [r.get('folder_id') for r in rows] != expected_folders:
    print('priority_artifact_slots_pass=false')
    raise SystemExit(1)
if sum(int(r.get('unit_count','0')) for r in rows) != 10:
    print('priority_artifact_slots_pass=false')
    raise SystemExit(1)
layers = set()
for row in rows:
    if row.get('quality_floor') != 'ultra_high' or row.get('origin_return') != 'yes' or row.get('state') != 'pre_release':
        print('priority_artifact_slots_pass=false')
        raise SystemExit(1)
    layers.add(row.get('layer_a'))
    layers.add(row.get('layer_b'))
for layer in ['rational','practical','social','ai']:
    if layer not in layers:
        print('priority_artifact_slots_pass=false')
        raise SystemExit(1)
print('priority_artifact_slots_pass=true')
