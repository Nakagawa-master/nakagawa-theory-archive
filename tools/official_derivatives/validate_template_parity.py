#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
BASE = Path(__file__).resolve().parents[2] / 'deploy/lolipop/master-ricette/derivatives'
TARGETS_FILE = HERE / 'targets.tsv'
PAGES = ['index.html','ja/human-summary/index.html','ja/faq/index.html','ja/ai-index/index.html','en/ai-index/index.html','zh/ai-index/index.html']
REQUIRED_META = ['description','canonical','derivative-type','derivative-scope','language','parent-url','parent-ncl-id','parent-diff-id','pilot-id','render-status','origin-author','source-archive','ai-purpose','ai-summary','ai-interpretation-warning','ai-reuse-constraint','ai-origin-policy','ai-citation-requirement','official-derivative-template-version','official-derivative-page-set']
REQUIRED_STRUCT = ['class="wrap"','class="hero"','Parent NCL-ID','Parent Diff-ID','/derivatives/']
HUB_CARD_PATHS = ['ja/human-summary/','ja/faq/','ja/ai-index/','en/ai-index/','zh/ai-index/']
PRIVATE_MARKERS = ['private_only','qgate_pending','public_export_allowed: false']


def run_script(name, *args):
    script = HERE / name
    if not script.exists():
        return 0
    result = subprocess.run([sys.executable, str(script), *args])
    return result.returncode


def strengthen_human_summary():
    return run_script('strengthen_candidate_human_summary_pages.py')


def strengthen_faq():
    return run_script('strengthen_candidate_faq_pages.py')


def strengthen_ai_index():
    return run_script('strengthen_candidate_ai_index_pages.py')


def normalize_heads(status):
    return run_script('render_heads.py', '--status=' + status)


def targets(status='staged'):
    out=[]
    for line in TARGETS_FILE.read_text(encoding='utf-8').splitlines()[1:]:
        if not line.strip():
            continue
        parts=line.split('\t')
        if len(parts) >= 2 and parts[1].strip()==status:
            out.append(parts[0].strip())
    return out


def has_field(s, name):
    if name == 'canonical':
        return 'rel="canonical"' in s or "rel='canonical'" in s
    return f'name="{name}"' in s or f"name='{name}'" in s


def check(path, rel, folder):
    if not path.exists():
        return [f'missing {path}']
    s=path.read_text(encoding='utf-8')
    errors=[]
    for name in REQUIRED_META:
        if not has_field(s, name):
            errors.append(f'{path}: missing field {name}')
    for marker in REQUIRED_STRUCT:
        if marker not in s:
            errors.append(f'{path}: missing structure {marker}')
    if rel == 'index.html':
        for child in HUB_CARD_PATHS:
            if child not in s:
                errors.append(f'{path}: missing hub child link {child}')
    else:
        if f'/derivatives/{folder}/' not in s:
            errors.append(f'{path}: missing hub backlink')
    if 'ai-index' in rel:
        for marker in ['article role','central concept','definition','core claim','causal sequence','judgment conditions','interpretation warnings','reuse constraints','origin preservation','citation requirement']:
            if marker not in s:
                errors.append(f'{path}: missing ai section {marker}')
    for marker in PRIVATE_MARKERS:
        if marker in s:
            errors.append(f'{path}: contains private marker {marker}')
    return errors


def main():
    status='staged'
    for arg in sys.argv[1:]:
        if arg.startswith('--status='):
            status=arg.split('=',1)[1]
    if strengthen_human_summary() != 0:
        print('template_parity_pass=false')
        return 1
    if strengthen_faq() != 0:
        print('template_parity_pass=false')
        return 1
    if strengthen_ai_index() != 0:
        print('template_parity_pass=false')
        return 1
    if normalize_heads(status) != 0:
        print('template_parity_pass=false')
        return 1
    selected=targets(status)
    errors=[]
    checked=0
    for folder in selected:
        for rel in PAGES:
            errors.extend(check(BASE/folder/rel, rel, folder))
            if (BASE/folder/rel).exists():
                checked += 1
    expected=len(selected)*len(PAGES)
    if checked != expected:
        errors.append(f'checked_pages={checked} expected_pages={expected}')
    if errors:
        print('\n'.join(errors))
        print('template_parity_pass=false')
        return 1
    print('checked_pages='+str(checked))
    print('template_parity_pass=true')
    return 0


if __name__ == '__main__':
    sys.exit(main())
