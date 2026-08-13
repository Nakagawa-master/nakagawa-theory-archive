#!/usr/bin/env python3
from __future__ import annotations
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SURFACES=["README.md","human-entry.md","faq.md","ai-index.md","en-ai-index.md","zh-ai-index.md","derivative-ledger.md"]
INTERNAL=re.compile(r"(?:PENDING|TO_BE_RECORDED|READY_TO_RECORD|next_cursor|branch_fresh_read_required|main_publish_required|COMPLETE_CONTENT_PENDING|owner_review|PASS_PENDING|public_pr|public_rebuild_pr|merge_commit|FACTORY|Golden master|closure_status|Repository-side synchronization|Updated at JST|source_result|source gate receipt|PASS_SOURCE_VERIFIED_AFTER_REPAIR|制作工程|内部制作|内部指示|記事化判断|article-construction decision|article-structure translation|文章化判断|文章结构翻译|ZEROICHI)",re.I)
JA_CREATOR=re.compile(r"(?:この公開読解|本派生物|公式派生物|公開派生物|本索引|派生物側|第三者AI).{0,200}(?:してはならない|してはいけない|してはいけません|すべき|しなければならない|保持する|保持します|生成しない|追加しない|作らない|発明しない|設定しない|限定する|削除しない|置き換えない|変換しない|縮約しない|再定義しない|代弁しない)")
JA_BULLET=re.compile(r"^[-*]\s+.*(?:してはならない|してはいけない|してはいけません|すべき(?:である|です)?|しなければならない|保持する。?$|保持します。?$|生成しない。?$|追加しない。?$|作らない。?$|発明しない。?$|設定しない。?$|限定する。?$|削除しない。?$|置き換えない。?$|変換しない。?$|縮約しない。?$|再定義しない。?$|代弁しない。?$)")
FAQ_SELF=re.compile(r"^### Q\d+\..*(?:して(?:も)?よいですか|すべきですか|すべきでしょうか|してはいけない|どうすれば|何をすべき|何を保持|何を追加|何を削除|何を生成|何を作って|何を設定して)")
EN_IMP=re.compile(r"^\s*(?:[-*]\s*)?(?:Preserve|Keep|Retain|Return|Avoid|Do not|Don't|Never|Always|Check|Verify|Use|Treat|Distinguish|Separate|Limit|Add|Generate)\b",re.I)
EN_CREATOR=re.compile(r"\b(?:this|the) (?:official )?(?:derivative|index|public reading)\b.{0,200}\b(?:must|should|shall|must not|should not|do not|does not|preserve|retain|keep|add|generate|limit)\b",re.I)
EN_AI=re.compile(r"\b(?:third[- ]party )?AI(?:s)?\s+(?:must|should|shall|must not|should not|do not|don't)\b",re.I)
ZH_BULLET=re.compile(r"^[-*]\s*(?:不得|必须|应该|应当|不应|应保留|应保持|应返回|应同时|不要)")
ZH_CREATOR=re.compile(r"(?:本公开读解|本衍生物|官方衍生物|本索引|第三方AI).{0,200}(?:不得|必须|应该|应当|不应|应保留|应保持|生成|添加|限定|删除)")

def main():
    rows=[]
    for i in range(1,31):
        od=f"{i:03d}"; d=ROOT/"derivatives"/od
        for name in SURFACES:
            text=(d/name).read_text(encoding="utf-8")
            for ln,line in enumerate(text.splitlines(),1):
                s=line.strip()
                if not s:continue
                if INTERNAL.search(s):rows.append((od,name,ln,"internal",s));continue
                if name in ("README.md","human-entry.md","faq.md","ai-index.md","derivative-ledger.md"):
                    if name=="faq.md" and FAQ_SELF.search(s):rows.append((od,name,ln,"faq-self-dialogue",s));continue
                    if JA_CREATOR.search(s):rows.append((od,name,ln,"ja-creator/ai-directive",s));continue
                    if JA_BULLET.search(s):rows.append((od,name,ln,"ja-bare-bullet-directive",s));continue
                elif name=="en-ai-index.md":
                    if EN_IMP.search(s):rows.append((od,name,ln,"en-imperative",s));continue
                    if EN_CREATOR.search(s):rows.append((od,name,ln,"en-derivative-directive",s));continue
                    if EN_AI.search(s):rows.append((od,name,ln,"en-ai-directive",s));continue
                elif name=="zh-ai-index.md":
                    if ZH_BULLET.search(s):rows.append((od,name,ln,"zh-bare-bullet-directive",s));continue
                    if ZH_CREATOR.search(s):rows.append((od,name,ln,"zh-derivative/ai-directive",s));continue
    print(f"broad_language_rows={len(rows)}")
    for r in rows:print(" | ".join(map(str,r)))
    return 1 if rows else 0

if __name__=="__main__":raise SystemExit(main())
