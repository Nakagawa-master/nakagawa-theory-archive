#!/usr/bin/env python3
from pathlib import Path
import sys

BASE = Path(__file__).resolve().parents[2] / 'deploy/lolipop/master-ricette/derivatives'
TARGETS_FILE = Path(__file__).resolve().with_name('targets.tsv')
PAGES = ['index.html','ja/human-summary/index.html','ja/faq/index.html','ja/ai-index/index.html','en/ai-index/index.html','zh/ai-index/index.html']
COMMON = ['<main class="wrap">','<p class="pilot">','Parent NCL-ID:','Parent Diff-ID:','/derivatives/">公式派生物一覧へ戻る']
HUB = ['<section class="hero">','<p class="status">公式派生物一覧</p>','<section class="grid">','<article class="card"><h2>人間向け要約</h2>','<article class="card"><h2>FAQ</h2>','<article class="card"><h2>日本語AI索引</h2>','<article class="card"><h2>English AI Index</h2>']
CHILD = ['<p class="status">公式派生物</p>','<header>','<article>','<nav aria-label="Derivative navigation">','</section></main></body></html>']
AI = ['article role','central concept','definition','core claim','causal sequence','judgment conditions','interpretation warnings','reuse constraints']

def targets(status='staged'):
    out=[]
    for line in TARGETS_FILE.read_text(encoding='utf-8').splitlines()[1:]:
        parts=line.split('\t')
        if len(parts) >= 2 and parts[1].strip()==status:
            out.append(parts[0].strip())
    return out

def check(path, rel):
    if not path.exists():
        return [f'missing {path}']
    s=path.read_text(encoding='utf-8')
    markers=list(COMMON)
    markers += HUB if rel=='index.html' else CHILD
    if 'ai-index' in rel:
        markers += AI
    errors=[]
    for marker in markers:
        if marker not in s:
            errors.append(f'{path}: missing {marker}')
    if '<meta name="parent-ncl-id"' not in s or '<meta name="parent-diff-id"' not in s:
        errors.append(f'{path}: missing origin metadata')
    return errors

def main():
    errors=[]
    selected=targets('staged')
    for target in selected:
        for rel in PAGES:
            errors.extend(check(BASE/target/rel, rel))
    if errors:
        print('\n'.join(errors))
        print('template_parity_pass=false')
        return 1
    print('checked_pages='+str(len(selected)*len(PAGES)))
    print('template_parity_pass=true')
    return 0

if __name__ == '__main__':
    sys.exit(main())
