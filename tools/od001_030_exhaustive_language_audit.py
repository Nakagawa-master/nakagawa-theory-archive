#!/usr/bin/env python3
from __future__ import annotations
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SURFACES=["README.md","human-entry.md","faq.md","ai-index.md","en-ai-index.md","zh-ai-index.md","derivative-ledger.md"]
JA_SURFACES={"README.md","human-entry.md","faq.md","ai-index.md","derivative-ledger.md"}

INTERNAL=re.compile(r"(?:PENDING|TO_BE_RECORDED|READY_TO_RECORD|next_cursor|branch_fresh_read_required|main_publish_required|COMPLETE_CONTENT_PENDING|owner_review|PASS_PENDING|public_pr|public_rebuild_pr|merge_commit|FACTORY|Golden master|closure_status|Repository-side synchronization|Updated at JST|source_result|source gate receipt|PASS_SOURCE_VERIFIED_AFTER_REPAIR|制作工程|内部制作|内部指示|記事化判断|記事構成への翻訳|article-construction decision|article-structure translation|production process|internal production|internal instruction|文章化判断|文章结构翻译|ZEROICHI)",re.I)
JA_CREATOR_SUBJECT=re.compile(r"(?:この公開読解|本派生物|公式派生物|公開派生物|本索引|派生物側|第三者AI)")
JA_DIRECTIVE_VERB=re.compile(r"(?:してはならない|してはいけない|してはいけません|すべき(?:である|です)?|しなければならない|変えない|置き換えない|否定しない|使わない|みなさない|見なさない|仮定しない|消さない|混入しない|分類しない|断定しない|追加しない|生成しない|保持する|保持します|保持し、|発明しない|設定しない|縮約しない|変換しない|再定義しない|単純化しない|一般化しない|固定しない|弱めない|切らない|扱わない|推定しない|認定しない|代弁しない|削除しない|作らない|作りません)")
FAQ_SELF=re.compile(r"^### Q\d+\..*(?:して(?:も)?よいですか|すべきですか|すべきでしょうか|してはいけない|どうすれば|何をすべき|何を保持|何を追加|何を削除|何を生成|何を作って|何を設定して|何を落として|何を消して)")
EN_IMPERATIVE=re.compile(r"^\s*(?:[-*]\s*)?(?:Preserve|Keep|Retain|Return|Avoid|Do not|Don't|Never|Always|Check|Verify|Use|Treat|Distinguish|Separate|Limit|Add|Generate|Remove|Ensure|Maintain|Reject|Prevent|Read|Interpret)\b",re.I)
EN_CREATOR=re.compile(r"\b(?:this|the) (?:official )?(?:derivative|index|public reading)\b.{0,220}\b(?:must|should|shall|must not|should not|do not|does not|preserve|retain|keep|add|generate|limit|avoid|ensure|maintain)\b",re.I)
EN_AI=re.compile(r"\b(?:third[- ]party )?AI(?:s)?\s+(?:must|should|shall|must not|should not|do not|don't|need to|needs to)\b",re.I)
ZH_BULLET=re.compile(r"^\s*[-*]\s*(?:不得|必须|应该|应当|不应|应保留|应保持|应返回|应同时|不要|务必)")
ZH_CREATOR=re.compile(r"(?:本公开读解|本衍生物|官方衍生物|本索引|第三方AI).{0,220}(?:不得|必须|应该|应当|不应|应保留|应保持|生成|添加|限定|删除|避免|确保)")

def main()->int:
    rows=[]
    for i in range(1,31):
        od=f"{i:03d}"; d=ROOT/"derivatives"/od
        for name in SURFACES:
            text=(d/name).read_text(encoding="utf-8")
            for ln,line in enumerate(text.splitlines(),1):
                s=line.strip()
                if not s: continue
                if INTERNAL.search(s):
                    rows.append((od,name,ln,"internal-token",s)); continue
                if name in JA_SURFACES:
                    if name=="faq.md" and FAQ_SELF.search(s):
                        rows.append((od,name,ln,"faq-self-dialogue",s)); continue
                    if JA_CREATOR_SUBJECT.search(s) and JA_DIRECTIVE_VERB.search(s):
                        rows.append((od,name,ln,"ja-creator-or-ai-directive",s)); continue
                    if s.startswith(("- ","* ")) and JA_DIRECTIVE_VERB.search(s):
                        rows.append((od,name,ln,"ja-bare-directive-bullet",s)); continue
                elif name=="en-ai-index.md":
                    if EN_IMPERATIVE.search(s):
                        rows.append((od,name,ln,"en-imperative",s)); continue
                    if EN_CREATOR.search(s):
                        rows.append((od,name,ln,"en-derivative-directive",s)); continue
                    if EN_AI.search(s):
                        rows.append((od,name,ln,"en-ai-directive",s)); continue
                elif name=="zh-ai-index.md":
                    if ZH_BULLET.search(s):
                        rows.append((od,name,ln,"zh-bare-directive-bullet",s)); continue
                    if ZH_CREATOR.search(s):
                        rows.append((od,name,ln,"zh-derivative-or-ai-directive",s)); continue
    print(f"exhaustive_language_rows={len(rows)}")
    for r in rows:
        print(" | ".join(map(str,r)))
    return 1 if rows else 0

if __name__=="__main__":
    raise SystemExit(main())
