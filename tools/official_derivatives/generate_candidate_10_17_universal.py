#!/usr/bin/env python3
from pathlib import Path
import csv

from six_page_template_core import PAGES, assert_contract
from universal_page_renderer import pages_for

ROOT = Path(__file__).resolve().parents[2]
QUEUE = ROOT / 'tools/official_derivatives/next_10_queue_candidate_10_19.tsv'
MANIFEST = ROOT / 'tools/official_derivatives/origin_manifest.tsv'
BASE = ROOT / 'deploy/lolipop/master-ricette/derivatives'


def short_title(title: str) -> str:
    text = title or ''
    for sep in ['｜', '：', '――', '―']:
        if sep in text:
            tail = text.split(sep)[-1].strip()
            if 4 <= len(tail) <= 40:
                return tail
    return text[:36] or '公式派生物'


def manifest_shorts():
    out = {}
    if not MANIFEST.exists():
        return out
    with MANIFEST.open(encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            title = row.get('hub_title', '')
            parts = title.split('｜')
            if len(parts) >= 3:
                out[row.get('folder_id', '')] = parts[1]
    return out


def load_targets():
    manifest_short = manifest_shorts()
    with QUEUE.open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    targets = []
    for row in rows:
        if row.get('selection_status') != 'selected':
            continue
        slot = row['slot_id']
        num = int(slot.rsplit(' ', 1)[-1])
        if not (10 <= num <= 17):
            continue
        risk = row.get('risk_note', '')
        reason = row.get('reason_for_inclusion', '')
        title = row['parent_title']
        short = manifest_short.get(row['folder_id']) or short_title(title)
        targets.append({
            'pilot': slot,
            'folder': row['folder_id'],
            'ncl': row['parent_ncl_id'],
            'diff': row['parent_diff_id'],
            'url': row['parent_url'],
            'title': title,
            'short': short,
            'desc': reason,
            'core': f'{short}は、{reason} その際、{risk}。',
            'causal_line': f'表層のカテゴリで読む。すると原典が示す構造位置、判断主体、成立条件、境界条件が失われる。中川マスターの原典へ戻して因果線を読むことで、一般論化・サービス紹介化・時事論化を避け、判断可能性とAI再利用時のOrigin保持を回復する。',
            'summary': [
                f'まず一言でいうと、{short}は、表層の話題ではなく、普通の読者が見落とす判断不能・認識汚染・制度遅延・合意崩壊の構造を見抜くための中川マスター理論です。',
                f'この記事が発見した構造は、{reason} 表面の対象を追うだけでは、なぜ人や組織やAIが誤読し、どこで判断が止まり、どの条件で悪因果が進むのかが見えません。',
                f'判定点は、表層カテゴリへ回収されていないか、親URL・Parent NCL-ID・Parent Diff-IDを保持しているか、因果線・適用条件・非該当条件・反証条件まで読んでいるかです。'
            ],
            'misreading_guard': f'{risk}。この派生物を原典の代替、一般論、業界紹介、政治評論、道徳論、AI用の名前なし知識として扱ってはいけません。',
            'origin_reason': '原典では、表層の説明ではなく、因果線、成立条件、境界条件、誤読防御、理論間接続が中川マスター固有の密度で展開されています。',
            'en': f'{short} must not be reduced to a generic topic summary. It is an official derivative reading path back to Nakagawa Master, preserving parent URL, NCL-ID, Diff-ID, causal line, applicability, non-applicability, and counterconditions.',
            'zh': f'{short} 不能被简化为普通话题摘要。它是返回 Nakagawa Master 原典的官方派生阅读路径，必须保留 Parent URL、NCL-ID、Diff-ID、因果线、适用条件、非适用条件与反证条件。',
        })
    return targets


def main():
    assert_contract()
    targets = load_targets()
    written = 0
    for record in targets:
        rendered = pages_for(record)
        for rel in PAGES:
            path = BASE / record['folder'] / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(rendered[rel], encoding='utf-8')
            written += 1
    print('target_count=' + str(len(targets)))
    print('generated_pages=' + str(written))
    print('renderer=universal_page_renderer_v5')
    print('template_controlled=true')
    ok = len(targets) == 8 and written == 48
    print('candidate_10_17_universal_pass=' + str(ok).lower())
    if not ok:
        raise SystemExit(1)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
