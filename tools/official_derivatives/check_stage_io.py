#!/usr/bin/env python3
import csv
from pathlib import Path

path = Path('tools/official_derivatives/stage_io.tsv')
rows = list(csv.DictReader(path.open(encoding='utf-8'), delimiter='\t'))
expected = ['origin_intake','origin_identity_check','derivative_generation','derivative_registry_update','quality_gate_check','effect_surface_check','effect_readiness_check','activation_ready_check','owner_boundary_action']
stages = [r.get('stage','') for r in rows]
print('check_set=stage_io_v1')
if stages != expected:
    print('stage_io_pass=false')
    raise SystemExit(1)
if rows[-1].get('next_stage') != 'complete':
    print('stage_io_pass=false')
    raise SystemExit(1)
print('stage_io_pass=true')
