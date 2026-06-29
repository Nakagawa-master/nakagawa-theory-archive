#!/usr/bin/env python3
from pathlib import Path
import csv
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TARGETS = HERE / 'targets.tsv'
WORKFLOW = ROOT / '.github/workflows/official-derivative-generation-check.yml'
PREFIX = 'deploy/lolipop/master-ricette/derivatives/'
ARTIFACT_NAME = 'official-derivatives-candidate-05-09'


def staged_folders():
    with TARGETS.open(encoding='utf-8', newline='') as f:
        return {r['folder_id'] for r in csv.DictReader(f, delimiter='\t') if r.get('export_status') == 'staged'}


def workflow_paths():
    lines = WORKFLOW.read_text(encoding='utf-8').splitlines()
    paths = []
    in_artifact = False
    in_path = False
    for line in lines:
        stripped = line.strip()
        if stripped == 'name: ' + ARTIFACT_NAME:
            in_artifact = True
            continue
        if in_artifact and stripped == 'path: |':
            in_path = True
            continue
        if in_path:
            if stripped.startswith(PREFIX):
                paths.append(stripped)
                continue
            if stripped and not stripped.startswith(PREFIX):
                break
    return paths


def main():
    expected = staged_folders()
    paths = workflow_paths()
    found = {p[len(PREFIX):].split('/', 1)[0] for p in paths}
    errors = []
    if found != expected:
        errors.append('artifact_scope_mismatch')
        errors.append('expected=' + ','.join(sorted(expected)))
        errors.append('found=' + ','.join(sorted(found)))
    if len(paths) != len(expected):
        errors.append('artifact_path_count_mismatch')
    print('check_set=workflow_artifact_scope_v1')
    print('staged_targets=' + str(len(expected)))
    print('artifact_paths=' + str(len(paths)))
    if errors:
        print('\n'.join(errors))
        print('workflow_artifact_scope_pass=false')
        return 1
    print('workflow_artifact_scope_pass=true')
    return 0


if __name__ == '__main__':
    sys.exit(main())
