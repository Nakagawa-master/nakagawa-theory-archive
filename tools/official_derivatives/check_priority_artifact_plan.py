#!/usr/bin/env python3
import csv
from pathlib import Path
plan = list(csv.DictReader(Path('tools/official_derivatives/priority_artifact_plan.tsv').open(encoding='utf-8'), delimiter='\t'))
impact = list(csv.DictReader(Path('tools/official_derivatives/impact_execution_map.tsv').open(encoding='utf-8'), delimiter='\t'))
impact_artifacts = {r.get('required_artifact','') for r in impact}
expected = ['quote_pack','sns_text_pack','rebuttal_pack','notebooklm_prompt_pack']
print('check_set=priority_artifact_plan_v1')
if [r.get('artifact','') for r in plan] != expected:
    print('priority_artifact_plan_pass=false')
    raise SystemExit(1)
for row in plan:
    if row.get('artifact') not in impact_artifacts:
        print('priority_artifact_plan_pass=false')
        raise SystemExit(1)
    if row.get('quality_floor') != 'ultra_high' or row.get('origin_return') != 'yes':
        print('priority_artifact_plan_pass=false')
        raise SystemExit(1)
    if not row.get('required_fields') or not row.get('minimum_units'):
        print('priority_artifact_plan_pass=false')
        raise SystemExit(1)
print('priority_artifact_plan_pass=true')
