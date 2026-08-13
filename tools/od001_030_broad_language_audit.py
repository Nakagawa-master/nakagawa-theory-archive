#!/usr/bin/env python3
from __future__ import annotations
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SURFACES=["README.md","human-entry.md","faq.md","ai-index.md","en-ai-index.md","zh-ai-index.md","derivative-ledger.md"]
JA_TERMS=re.compile(r"(?:してはならない|してはいけない|してはいけません|すべき(?:である|です)?|しなければならない|保持する|保持します|生成しない|追加しない|作らない|作りません|発明しない|設定しない|限定する|削除しない|置き換えない|変換しない|縮約しない)")
JA_ATTR=re.compile(r"(?:親原典|原典|本文|第\d+論).{0,80}(?:では|は|が|によれば|において|とする|とされ|と述べ|と定義)")
FAQ_SELF=re.compile(r"^### Q\d+\..*(?:して(?:も)?よいですか|すべきですか|すべきでしょうか|してはいけない|どうすれば|何をすべき|何を保持|何を追加|何を削除|何を生成)")
EN_MODAL=re.compile(r"\b(?:must|should|shall|must not|should not|do not|don't|never|always)\b",re.I)
EN_ATTR=re.compile(r"\b(?:the parent|the source|the original|Paper \d+|Vol\. ?\d+)\b.{0,120}\b(?:states?|defines?|describes?|argues?|treats?|requires?|positions?|specifies?|says?)\b",re.I)
EN_IMP=re.compile(r"^\s*(?:[-*]\s*)?(?:Preserve|Keep|Retain|Return|Avoid|Do not|Don't|Never|Always|Check|Verify|Use|Treat|Distinguish|Separate|Limit|Add|Generate)\b",re.I)
ZH_MODAL=re.compile(r"(?:必须|不得|应该|应当|不应|应在|应返回|应同时|应保留|应保持|不能|不要)")
ZH_ATTR=re.compile(r"(?:父原典|原典|本文|第[一二三四五六七八九十0-9]+论).{0,80}(?:规定|定义|说明|认为|指出|记载|将|把|中|里)")
INTERNAL=re.compile(r"(?:PENDING|TO_BE_RECORDED|READY_TO_RECORD|next_cursor|branch_fresh_read_required|main_publish_required|COMPLETE_CONTENT_PENDING|owner_review|PASS_PENDING|public_pr|public_rebuild_pr|merge_commit|FACTORY|Golden master|closure_status|Repository-side synchronization|Updated at JST|source_result|source gate receipt|PASS_SOURCE_VERIFIED_AFTER_REPAIR|制作工程|内部制作|内部指示|記事化判断|article-construction decision|article-structure translation|文章化判断|文章结构翻译|ZEROICHI)",re.I)

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
                    if JA_TERMS.search(s) and not JA_ATTR.search(s):rows.append((od,name,ln,"ja-bare-normative/editorial",s))
                elif name=="en-ai-index.md":
                    if EN_IMP.search(s):rows.append((od,name,ln,"en-imperative",s))
                    elif EN_MODAL.search(s) and not EN_ATTR.search(s):rows.append((od,name,ln,"en-bare-modal",s))
                elif name=="zh-ai-index.md":
                    if ZH_MODAL.search(s) and not ZH_ATTR.search(s):rows.append((od,name,ln,"zh-bare-modal",s))
    print(f"broad_language_rows={len(rows)}")
    for r in rows:print(" | ".join(map(str,r)))
    return 1 if rows else 0

if __name__=="__main__":raise SystemExit(main())
