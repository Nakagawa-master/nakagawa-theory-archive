#!/usr/bin/env python3
from __future__ import annotations
import re, sys, urllib.request
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
SURFACES = ["README.md","human-entry.md","faq.md","ai-index.md","en-ai-index.md","zh-ai-index.md","derivative-ledger.md"]

# These are public-text patterns, not every occurrence of words such as 保持 in source theory content.
SUSPECT_PATTERNS = [
    ("creator_subject_public_reading", re.compile(r"この公開読解(?:は|では|で)")),
    ("derivative_side", re.compile(r"派生物側")),
    ("third_party_ai_instruction", re.compile(r"第三者AI.{0,80}(?:してはならない|すべき|保持|生成|追加|限定)")),
    ("derivative_instruction_ja", re.compile(r"(?:本派生物|公式派生物|この派生物).{0,120}(?:してはならない|すべき|保持する|生成しない|追加しない|限定する|削除しない|作らない|置き換えない)")),
    ("public_reading_instruction_ja", re.compile(r"(?:公開読解|公開派生).{0,120}(?:してはならない|すべき|保持する|生成しない|追加しない|限定する|削除しない|作らない|置き換えない)")),
    ("internal_editorial_terms_ja", re.compile(r"(?:制作工程|内部制作|内部指示|記事化判断|記事構成への翻訳|特定媒体名を前景化しない)")),
    ("internal_workflow_tokens", re.compile(r"(?:PENDING|TO_BE_RECORDED|READY_TO_RECORD|next_cursor|branch_fresh_read_required|main_publish_required|COMPLETE_CONTENT_PENDING|owner_review|PASS_PENDING|public_pr|public_rebuild_pr|merge_commit|FACTORY|Golden master|closure_status|Repository-side synchronization|Updated at JST|source_result|source gate receipt|PASS_SOURCE_VERIFIED_AFTER_REPAIR)")),
    ("derivative_instruction_en", re.compile(r"(?:this|the) (?:official )?derivative.{0,140}\b(?:must|should|shall|do not|does not|preserve|retain|keep|add|generate|limit)\b", re.I)),
    ("ai_instruction_en", re.compile(r"(?:third[- ]party )?AI.{0,120}\b(?:must|should|shall|do not|preserve|retain|keep|add|generate)\b", re.I)),
    ("internal_editorial_terms_en", re.compile(r"(?:production process|article-construction decision|article-structure translation|inward-facing|internal production|internal instruction)", re.I)),
    ("derivative_instruction_zh", re.compile(r"(?:官方衍生物|本衍生物|本公开读解|第三方AI).{0,120}(?:必须|不得|应该|应当|保持|保留|生成|添加|限定|删除)")),
    ("internal_editorial_terms_zh", re.compile(r"(?:内部制作|内部指令|文章化判断|文章结构翻译)")),
]

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]
    def handle_data(self, data):
        if data.strip(): self.parts.append(data.strip())

def fetch_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0 OD-reader-audit"})
    with urllib.request.urlopen(req, timeout=25) as r:
        raw = r.read().decode("utf-8", errors="replace")
    p=TextExtractor(); p.feed(raw)
    return "\n".join(p.parts)

def parent_url(readme: str) -> str | None:
    m=re.search(r"^- Parent URL:\s*(https?://\S+)", readme, re.M)
    return m.group(1) if m else None

def section(text: str, heading: str) -> str:
    m=re.search(rf"^## {re.escape(heading)}\s*$", text, re.M)
    if not m: return ""
    start=m.end(); n=re.search(r"^## ", text[start:], re.M)
    end=start+n.start() if n else len(text)
    return text[start:end].strip()

def source_falsification(page_text: str) -> str:
    # Prefer explicit 反証条件; otherwise use the shortest sentence-like span containing 棄却/改訂.
    flat=re.sub(r"[ \t]+", " ", page_text)
    m=re.search(r"反証条件[:：]\s*([^\n]{10,900}?)(?=(?:署名[:：]|\n\s*局所監査要旨|\n\s*参照束|$))", flat)
    if m:
        return m.group(1).strip(" -・/\t")
    candidates=[]
    for line in flat.splitlines():
        if ("棄却" in line or "改訂" in line) and len(line) < 1400:
            candidates.append(line.strip())
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
        rp=d/"README.md"; readme=rp.read_text(encoding="utf-8")
        url=parent_url(readme)
        cur=section(readme,"反証・改訂条件")
        if not url:
            source_rows.append((od,"NO_PARENT_URL","",cur)); continue
        try:
            src_text=fetch_text(url)
            sf=source_falsification(src_text)
            source_rows.append((od,url,sf,cur))
        except Exception as e:
            source_rows.append((od,url,f"FETCH_ERROR:{type(e).__name__}:{e}",cur))

    print("=== SOURCE FALSIFICATION AUDIT ===")
    for od,url,sf,cur in source_rows:
        print(f"OD{od}\nPARENT={url}\nSOURCE={sf}\nCURRENT_README={cur}\n---")
    print("=== SUSPECT PUBLIC-TEXT LINES ===")
    for row in suspects:
        od,name,lineno,label,line=row
        print(f"OD{od} {name}:{lineno} [{label}] {line}")
    print("=== COUNTS ===")
    print(f"source_rows={len(source_rows)} suspects={len(suspects)} missing={len(missing)}")
    if missing:
        print("MISSING:", *missing, sep="\n")
    # Audit is diagnostic: do not fail merely because suspects exist.
    return 0 if not missing else 2

if __name__ == "__main__":
    raise SystemExit(main())
