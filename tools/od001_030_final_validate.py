#!/usr/bin/env python3
from __future__ import annotations
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SURFACES=["README.md","human-entry.md","faq.md","ai-index.md","en-ai-index.md","zh-ai-index.md","derivative-ledger.md"]
FLOORS={"README.md":12348,"human-entry.md":6403,"faq.md":11177,"ai-index.md":10389,"en-ai-index.md":12200,"zh-ai-index.md":9888,"derivative-ledger.md":4098}
AI_HEADINGS=["Summary","Concepts","Causal chain","State model","Applications","Measurements and audit","Validity conditions","Failure conditions","Falsification conditions","Required distinctions","Interpretation constraints","Search terms","Origin return"]
HUMAN_HEADINGS=["親原典","派生ID","15秒説明","なぜ必要になるのか","実務工程","適用例","成功判定","限界","誤読防止"]
INTERNAL_TOKENS=["PENDING","TO_BE_RECORDED","READY_TO_RECORD","next_cursor","branch_fresh_read_required","main_publish_required","COMPLETE_CONTENT_PENDING","owner_review","PASS_PENDING","public_pr","public_rebuild_pr","merge_commit","FACTORY","Golden master","closure_status","Repository-side synchronization","Updated at JST","source_result","source gate receipt","PASS_SOURCE_VERIFIED_AFTER_REPAIR","制作工程","内部制作","内部指示","記事化判断","記事構成への翻訳","article-construction decision","article-structure translation","production process","internal production","internal instruction","文章化判断","文章结构翻译"]
JA_CREATOR=re.compile(r"(?:この公開読解|本派生物|公式派生物|公開派生物|本索引|派生物側).{0,180}(?:してはならない|してはいけない|してはいけません|すべき|しなければならない|保持する|保持します|保持できるよう|生成しない|追加しない|作らない|作りません|発明しない|設定しない|限定する|変換しない|縮約しない|再定義しない|置き換えない|代弁しない|削除しない)")
JA_AI=re.compile(r"第三者AI.{0,180}(?:してはならない|してはいけない|すべき|しなければならない|保持する|保持します|生成しない|追加しない|限定する)")
JA_PUBLIC_SUBJECT=re.compile(r"この公開読解")
EN_LINE_START=re.compile(r"^\s*(?:[-*]\s*)?(?:Preserve|Do not|Don't|Keep|Retain|Avoid|Return|Never|Always|Must|Should)\b",re.I)
EN_CREATOR=re.compile(r"\b(?:this|the) (?:official )?(?:derivative|index|public reading)\b.{0,180}\b(?:must|should|shall|do not|must not|should not|preserve|retain|keep|add|generate|limit)\b",re.I)
# Only direct modal instructions to AI are flagged. Descriptive sentences such as "AI use ... does not prove X" are ordinary public theory prose.
EN_AI=re.compile(r"\b(?:third[- ]party )?AI(?:s)?\s+(?:must|should|shall|must not|should not|do not|don't)\b",re.I)
ZH_CREATOR=re.compile(r"(?:本公开读解|本衍生物|官方衍生物|本索引|第三方AI).{0,180}(?:不得|必须|应该|应当|不应|保持|保留|生成|添加|限定|删除)")
FAQ_BAD=re.compile(r"^### Q\d+\..*(?:この公開読解|派生物側|公開派生物|保持すべき|追加すべき|削除すべき|どう作るべき|してはいけない)")
FOOTER_LINKS=["README.md","human-entry.md","faq.md","ai-index.md","en-ai-index.md","zh-ai-index.md","derivative-ledger.md"]

def section(text, heading):
    m=re.search(rf"^## {re.escape(heading)}\s*$",text,re.M)
    if not m:return ""
    s=m.end(); n=re.search(r"^## ",text[s:],re.M)
    e=s+n.start() if n else len(text)
    return text[s:e].strip()

def main():
    issues=[]; counts={k:0 for k in ["missing","underfloor","structure","language","falsification","footer","identity"]}
    sizes=[]
    for i in range(1,31):
        od=f"{i:03d}"; d=ROOT/"derivatives"/od
        files={}
        for name in SURFACES:
            p=d/name
            if not p.exists():
                issues.append((od,name,"missing","file missing"));counts["missing"]+=1;continue
            text=p.read_text(encoding="utf-8"); files[name]=text
            b=len(text.encode("utf-8")); sizes.append((od,name,b,FLOORS[name]))
            if b<FLOORS[name]:
                issues.append((od,name,"underfloor",f"bytes={b} floor={FLOORS[name]} deficit={FLOORS[name]-b}"));counts["underfloor"]+=1
            for tok in INTERNAL_TOKENS:
                if tok.lower() in text.lower():
                    issues.append((od,name,"language",f"internal token: {tok}"));counts["language"]+=1
            for ln,line in enumerate(text.splitlines(),1):
                bad=None
                if name in ("README.md","human-entry.md","faq.md","ai-index.md","derivative-ledger.md"):
                    if JA_CREATOR.search(line): bad="JA creator instruction"
                    elif JA_AI.search(line): bad="JA third-party-AI instruction"
                    elif JA_PUBLIC_SUBJECT.search(line): bad="creator-side subject この公開読解"
                    if name=="faq.md" and FAQ_BAD.search(line): bad="FAQ internal/editorial question"
                elif name=="en-ai-index.md":
                    if EN_LINE_START.search(line): bad="EN imperative line"
                    elif EN_CREATOR.search(line): bad="EN derivative/index instruction"
                    elif EN_AI.search(line): bad="EN AI instruction"
                elif name=="zh-ai-index.md":
                    if ZH_CREATOR.search(line): bad="ZH derivative/AI instruction"
                if bad:
                    issues.append((od,name,"language",f"L{ln} {bad}: {line.strip()}"));counts["language"]+=1
            if not all(link in text[-900:] for link in FOOTER_LINKS):
                issues.append((od,name,"footer","7-link footer incomplete"));counts["footer"]+=1
            if "derivative_ncl_id:" not in text or "derivative_diff_id:" not in text:
                issues.append((od,name,"identity","derivative identity field missing"));counts["identity"]+=1
        if set(files)!=set(SURFACES): continue
        faq=files["faq.md"]
        qs=[int(x) for x in re.findall(r"^### Q(\d+)\.",faq,re.M)]
        if qs!=list(range(1,31)):
            issues.append((od,"faq.md","structure",f"FAQ sequence={qs}"));counts["structure"]+=1
        hum=files["human-entry.md"]
        if not re.search(rf"^# 人間向け要約｜公式派生物{od}\s*$",hum,re.M):
            issues.append((od,"human-entry.md","structure","human title not benchmark form"));counts["structure"]+=1
        for h in HUMAN_HEADINGS:
            if not re.search(rf"^## {re.escape(h)}\s*$",hum,re.M):
                issues.append((od,"human-entry.md","structure",f"missing human heading {h}"));counts["structure"]+=1
        for name in ("ai-index.md","en-ai-index.md","zh-ai-index.md"):
            tx=files[name]; pos=[]
            for h in AI_HEADINGS:
                ms=list(re.finditer(rf"^## {re.escape(h)}\s*$",tx,re.M))
                if len(ms)!=1:
                    issues.append((od,name,"structure",f"heading {h} count={len(ms)}"));counts["structure"]+=1
                else: pos.append(ms[0].start())
            if len(pos)==13 and pos!=sorted(pos):
                issues.append((od,name,"structure","AI heading order wrong"));counts["structure"]+=1
        rf=section(files["README.md"],"反証・改訂条件")
        jf=section(files["ai-index.md"],"Falsification conditions")
        if not rf or not jf:
            issues.append((od,"README/ai-index","falsification","missing falsification section"));counts["falsification"]+=1
        elif re.sub(r"\s+","",rf)!=re.sub(r"\s+","",jf):
            issues.append((od,"README/ai-index","falsification","JA falsification differs from README"));counts["falsification"]+=1
        for name in ("README.md","ai-index.md","en-ai-index.md","zh-ai-index.md"):
            head="反証・改訂条件" if name=="README.md" else "Falsification conditions"
            fs=section(files[name],head)
            if any(x.lower() in fs.lower() for x in ["派生物側","この公開読解","this derivative","the derivative","本公开读解","本衍生物"]):
                issues.append((od,name,"falsification","derivative-created/meta wording in falsification"));counts["falsification"]+=1
        for name,tx in files.items():
            if "ZEROICHI" in tx:
                issues.append((od,name,"language","explicit external-media name ZEROICHI"));counts["language"]+=1
    print("=== COUNTS ===")
    print(" ".join(f"{k}={v}" for k,v in counts.items()))
    print(f"total_issues={len(issues)}")
    print("=== UNDERFLOOR ===")
    for od,name,b,floor in sizes:
        if b<floor: print(f"OD{od} {name} bytes={b} floor={floor} deficit={floor-b}")
    print("=== NON-SIZE ISSUES ===")
    for row in issues:
        if row[2]!="underfloor": print(" | ".join(map(str,row)))
    return 1 if issues else 0

if __name__=="__main__":
    raise SystemExit(main())
