#!/usr/bin/env python3
import csv
import subprocess
import sys
from pathlib import Path

P = Path('tools/official_derivatives/next_batch_intake_schema.tsv')
NEEDED = ['batch_id','slot_id','parent_url','parent_ncl_id','parent_diff_id','folder_id','canonical_url','quality_gate_status','export_status']
EXTRA = ['check_derivative_registry_rows.py','check_derivative_registry_identity.py','check_derivative_registry_canonical.py','check_derivative_registry_page_parity.py','check_derivative_registry_boundary.py','check_effect_surface_map.py','check_effect_readiness.py','check_effect_force_keys.py','check_scale_keys.py','check_layer_keys.py','check_flow.py']


def main():
    with P.open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    fields = [x.get('field','') for x in rows]
    bad = [x for x in NEEDED if x not in fields]
    print('check_set=next_batch_schema_v14')
    if bad:
        print('next_batch_schema_pass=false')
        return 1
    for name in EXTRA:
        script = Path('tools/official_derivatives') / name
        if script.exists():
            result = subprocess.run([sys.executable, str(script)])
            if result.returncode != 0:
                print('next_batch_schema_pass=false')
                return result.returncode
    print('schema_fields=' + str(len(fields)))
    print('next_batch_schema_pass=true')
    return 0

if __name__ == '__main__':
    sys.exit(main())
