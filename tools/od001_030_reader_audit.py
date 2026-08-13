#!/usr/bin/env python3
from __future__ import annotations
import re, urllib.request, html
from pathlib import Path

# Re-run marker: post-cleanup verification 2026-08-13.
ROOT = Path(__file__).resolve().parents[1]
SURFACES = ["README.md","human-entry.md","faq.md","ai-index.md","en-ai-index.md","zh-ai-index.md","derivative-ledger.md"]

SUSPECT_PATTERNS = [
    ("creator_subject_public_reading", re.compile(r"この公開読解(?:は|では|で)")),
    ("derivative_side", re.compile(r"派生物側")),
    ("third_party_ai_instruction", re.compile(r"第三者AI.{0,100}(?:してはならない|すべき|保持|生成|追加|限定)")),
    ("derivative_instruction_ja", re.compile(r"(?:本派生物|公式派生物|この派生物).{0,140}(?:してはならない|すべき|保持する|生成しない|追加しない|限定する|削除しない|作らない|置き換えない|変換しない|縮約しない)")),
    ("public_reading_instruction_ja", re.compile(r"(?:公開読解|公開派生).{0,140}(?:してはならない|すべき|保持する|生成しない|追加しない|限定する|削除しない|作らない|置き換えない|変換しない|発明してはいけない|設定しない)")),
    ("internal_editorial_terms_ja", re.compile(r"(?:制作工程|内部制作|内部指示|記事化判断|記事構成への翻訳|特定媒体名を前景化しない)")),
    ("internal_workflow_tokens", re.compile(r"(?:PENDING|TO_BE_RECORDED|READY_TO_RECORD|next_cursor|branch_fresh_read_required|main_publish_required|COMPLETE_CONTENT_PENDING|owner_review|PASS_PENDING|public_pr|public_rebuild_pr|merge_commit|FACTORY|Golden master|closure_status|Repository-side synchronization|Updated at JST|source_result|source gate receipt|PASS_SOURCE_VERIFIED_AFTER_REPAIR)")),
    ("derivative_instruction_en", re.compile(r"\b(?:this|the) (?:official )?derivative\b.{0,180}\b(?:must|should|shall|do not|does not|preserve|retain|keep|add|generate|limit)\b", re.I)),
    ("third_party_ai_instruction_en", re.compile(r"\b(?:third[- ]party )?AIs?\b.{0,180}\b(?:must|should|shall|do not|preserve|retain|keep|add|generate|limit)\b", re.I)),
    ("internal_editorial_terms_en", re.compile(r"(?:production process|article-construction decision|article-structure translation|inward-facing|internal production|internal instruction)", re.I)),
    ("derivative_instruction_zh", re.compile(r"(?:官方衍生物|本衍生物|本公开读解|第三方AI).{0,160}(?:必须|不得|应该|应当|保持|保留|生成|添加|限定|删除)")),
    ("internal_editorial_terms_zh", re.compile(r"(?:内部制作|内部指令|文章化判断|文章结构翻译)")),
]

def fetch_html(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0 OD-reader-audit"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read().decode("utf-8", errors="replace")

def strip_tags(raw: str) -> str:
    raw = re.sub(r"(?is)<script.*?</script>|<style.*?</style>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</p>|</li>|</h[1-6]>", "\n", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    raw = html.unescape(raw)
    raw = re.sub(r"[ \t\r\f\v]+", " ", raw)
    raw = re.sub(r"\n\s*\n+", "\n", raw)
    return raw.strip()

def integrated_audit_text(raw_html: str) -> str:
    idx = raw_html.find("統合監査要旨")
    if idx < 0:
        return ""
    window = raw_html[idx: idx + 30000]
    ends = [x for x in (window.find("局所監査要旨", 20), window.find("Reference Cluster", 20), window.find("参照束", 20)) if x > 0]
    if ends:
        window = window[:min(ends)]
    return strip_tags(window)

def parent_url(readme: str) -> str | None:
    m=re.search(r"^- Parent URL:\s*(https?://\S+)", readme, re.M)
    return m.group(1) if m else None

def section(text: str, heading: str) -> str:
    m=re.search(rf"^## {re.escape(heading)}\s*$", text, re.M)
    if not m: return ""
    start=m.end(); n=re.search(r"^## ", text[start:], re.M)
    end=start+n.start() if n else len(text)
    return text[start:end].strip()

def source_falsification(audit_text: str) -> str:
    flat = re.sub(r"[ \t]+", " ", audit_text)
    m = re.search(r"反証条件[:：]\s*(.+?)(?=(?:署名[:：]|\n|$))", flat)
    if m and ("棄却" in m.group(1) or "改訂" in m.group(1) or "適用" in m.group(1)):
        return m.group(1).strip(" -・/\t")
    candidates=[]
    for line in flat.splitlines():
        if any(k in line for k in ("棄却", "改訂", "適用しない", "適用外")) and 15 <= len(line) <= 1800:
            candidates.append(line.strip(" -・\t"))
    return min(candidates, key=len) if candidates else ""

def main() -> int:
    suspects=[]; source_rows=[]; missing=[]
    for i in range(1,31):
        od=f"{i:03d}"; d=ROOT/"derivatives"/od
        for name in SURFACES:
            p=d/name
            if not p.exists():
                missing.append(str(p.relative_to(ROOT))); continue
            text=p.read_text(encoding="utf-8")
            for lineno,line in enumerate(text.splitlines(),1):
                for label,rx in SUSPECT_PATTERNS:
                    if rx.search(line):
                        suspects.append((od,name,lineno,label,line.strip()))
        readme=(d/"README.md").read_text(encoding="utf-8")
        url=parent_url(readme); cur=section(readme,"反証・改訂条件")
        if not url:
            source_rows.append((od,"NO_PARENT_URL","",cur)); continue
        try:
            audit=integrated_audit_text(fetch_html(url))
            source_rows.append((od,url,source_falsification(audit),cur))
        except Exception as e:
            source_rows.append((od,url,f"FETCH_ERROR:{type(e).__name__}:{e}",cur))

    print("=== SOURCE FALSIFICATION AUDIT ===")
    for od,url,sf,cur in source_rows:
        print(f"OD{od}\nPARENT={url}\nSOURCE={sf}\nCURRENT_README={cur}\n---")
    print("=== SUSPECT PUBLIC-TEXT LINES ===")
    for od,name,lineno,label,line in suspects:
        print(f"OD{od} {name}:{lineno} [{label}] {line}")
    print("=== COUNTS ===")
    print(f"source_rows={len(source_rows)} suspects={len(suspects)} missing={len(missing)}")
    if missing:
        print("MISSING:", *missing, sep="\n")
    return 0 if not missing else 2

if __name__ == "__main__":
    raise SystemExit(main())