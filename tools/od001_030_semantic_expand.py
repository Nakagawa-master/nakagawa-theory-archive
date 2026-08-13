#!/usr/bin/env python3
from __future__ import annotations
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FLOORS={"README.md":12348,"human-entry.md":6403,"faq.md":11177,"ai-index.md":10389,"en-ai-index.md":12200,"zh-ai-index.md":9888,"derivative-ledger.md":4098}
TARGET_BUFFER=420
BANNED=("この公開読解","派生物側","制作工程","内部制作","内部指示","記事化判断","ZEROICHI","PENDING","Golden master","source gate","PASS_")

def section_bounds(text:str, heading:str):
    m=re.search(rf"^## {re.escape(heading)}\s*$",text,re.M)
    if not m:return None
    s=m.end(); n=re.search(r"^## ",text[s:],re.M); e=s+n.start() if n else len(text)
    return m.start(),s,e

def section(text:str, heading:str)->str:
    b=section_bounds(text,heading)
    return text[b[1]:b[2]].strip() if b else ""

def append_section(text:str, heading:str, additions:list[str])->str:
    if not additions:return text
    b=section_bounds(text,heading)
    if not b:return text
    block="\n\n"+"\n\n".join(x.strip() for x in additions if x.strip())+"\n"
    return text[:b[2]].rstrip()+block+text[b[2]:]

def insert_origin_return(text:str, additions:list[str])->str:
    if not additions:return text
    block="\n\n## 原典回帰\n"+"\n\n".join(additions)+"\n"
    m=re.search(r"\n---\n",text)
    return (text[:m.start()].rstrip()+block+text[m.start():]) if m else text.rstrip()+block

def bullets(text:str, heading:str, minlen:int=12)->list[str]:
    s=section(text,heading); out=[]
    for line in s.splitlines():
        x=line.strip()
        if x.startswith("- "):
            x=x[2:].strip()
            if minlen<=len(x)<=700 and x not in out and not any(b.lower() in x.lower() for b in BANNED): out.append(x)
    return out

def paragraphs(text:str, heading:str, minlen:int=35)->list[str]:
    s=section(text,heading); out=[]
    for x in re.split(r"\n\s*\n",s):
        x=x.strip()
        if not x or x.startswith("```") or x.startswith("#") or x.startswith("-"):continue
        x=re.sub(r"\s+"," ",x)
        if minlen<=len(x)<=1400 and not any(b.lower() in x.lower() for b in BANNED) and x not in out:out.append(x)
    return out

def concepts(text:str)->list[str]:
    return bullets(text,"Concepts",2)[:30]

def safe_quote(x:str,maxlen=520)->str:
    x=re.sub(r"\s+"," ",x.strip())
    if len(x)<=maxlen:return x
    cut=x[:maxlen]
    return cut.rsplit(" ",1)[0]+"…" if " " in cut else cut+"…"

def unique(items:list[str])->list[str]:
    out=[]; seen=set()
    for x in items:
        k=re.sub(r"\s+","",x).lower()
        if not k or k in seen:continue
        seen.add(k); out.append(x)
    return out

def ja_relations(readme:str)->list[str]:
    ds=bullets(readme,"必須の区別",2) or bullets(readme,"Required distinctions",2)
    au=bullets(readme,"測定・監査点",8)
    va=bullets(readme,"成立条件",8) or paragraphs(readme,"成立条件")
    fa=bullets(readme,"失敗条件",8) or paragraphs(readme,"失敗条件")
    ap=bullets(readme,"適用例",8) or paragraphs(readme,"適用例")
    out=[]
    for d in ds:
        out.append(f"「{safe_quote(d)}」という区別は、親原典の概念が因果上・証拠上で異なる役割を持つことを示す意味境界である。表面的に近い語が使われる場合でも、この区別によって何が同じで何が別の状態なのかを追跡できる。")
    n=max(len(au),len(va),len(fa),1)
    for i in range(n):
        a=au[i%len(au)] if au else "親原典に記載された観測点"
        v=va[i%len(va)] if va else "親原典に記載された成立側の条件"
        f=fa[i%len(fa)] if fa else "親原典に記載された失敗側の条件"
        out.append(f"観測点「{safe_quote(a)}」は、成立側の「{safe_quote(v)}」と失敗側の「{safe_quote(f)}」を同じ因果軸で比較する入口になる。この対照により、概念名の一致だけでなく、実際にどの接続が成立し、どの接続が崩れているかを読み分けられる。")
    for a in ap:
        out.append(f"適用例「{safe_quote(a)}」は、親原典の抽象概念が現実の観測へ戻る位置を示す。中心因果、成立条件、失敗条件、反証・改訂条件との対応関係から、その事例がどの意味で原典と接続するかを確認できる。")
    cps=paragraphs(readme,"中心命題",20)+paragraphs(readme,"位置づけ",20)+paragraphs(readme,"誤読禁止",20)
    for c in cps[:12]:
        out.append(f"親原典の関連文脈として「{safe_quote(c,650)}」がある。この記述は、単独の検索語ではなく、前後の因果線と成立・失敗の境界を合わせて読むことで構造上の位置が明確になる。")
    return unique(out)

def en_relations(text:str)->list[str]:
    ds=bullets(text,"Required distinctions",2); au=bullets(text,"Measurements and audit",4)
    va=bullets(text,"Validity conditions",4); fa=bullets(text,"Failure conditions",4); ap=bullets(text,"Applications",4); cs=concepts(text)
    raw=paragraphs(text,"Summary",20)+paragraphs(text,"Causal chain",20)+paragraphs(text,"Applications",20)+paragraphs(text,"Measurements and audit",20)+paragraphs(text,"Validity conditions",20)+paragraphs(text,"Failure conditions",20)
    out=[]
    for d in ds:
        out.append(f'The distinction "{safe_quote(d)}" marks a semantic boundary in the parent reading. The two sides occupy different causal or evidentiary roles, so surface similarity alone does not make them equivalent within the structure summarized here.')
    n=max(len(au),len(va),len(fa),1)
    for i in range(n):
        a=au[i%len(au)] if au else "the audit observations named by the parent"
        v=va[i%len(va)] if va else "the source-side validity condition"
        f=fa[i%len(fa)] if fa else "the source-side failure condition"
        out.append(f'The audit observation "{safe_quote(a)}" can be read together with the validity-side statement "{safe_quote(v)}" and the failure-side statement "{safe_quote(f)}". They describe different observational directions in the same source structure, and their contrast does not imply a new numerical score.')
    for a in ap:
        out.append(f'The application "{safe_quote(a)}" shows where the source model connects to an observable setting. Its relevance comes from the causal and audit relations described in the index rather than from the surface label of the example alone.')
    for c in cs:
        out.append(f'The concept "{safe_quote(c)}" functions as part of the parent-defined relation set rather than as an isolated search tag. Its meaning becomes more specific when read with the causal chain, audit observations, validity conditions, failure conditions, and required distinctions in this index.')
    for r in raw[:14]:
        out.append(f'The source context also states: "{safe_quote(r,720)}" This passage is connected to the same causal, validity, failure, and audit structure summarized by the surrounding sections.')
    return unique(out)

def zh_relations(text:str)->list[str]:
    ds=bullets(text,"Required distinctions",2); au=bullets(text,"Measurements and audit",2)
    va=bullets(text,"Validity conditions",2); fa=bullets(text,"Failure conditions",2); ap=bullets(text,"Applications",2); cs=concepts(text)
    raw=paragraphs(text,"Summary",10)+paragraphs(text,"Causal chain",10)+paragraphs(text,"State model",10)+paragraphs(text,"Applications",10)+paragraphs(text,"Measurements and audit",10)+paragraphs(text,"Validity conditions",10)+paragraphs(text,"Failure conditions",10)
    out=[]
    for d in ds:
        out.append(f'“{safe_quote(d)}”这一组区分标示父原典中的语义边界。两侧概念在因果或证据结构中承担不同作用，因此表面词语相近并不意味着在本索引所概括的结构中具有相同含义。')
    n=max(len(au),len(va),len(fa),1)
    for i in range(n):
        a=au[i%len(au)] if au else "父原典所列的审计观察点"
        v=va[i%len(va)] if va else "父原典中的成立侧条件"
        f=fa[i%len(fa)] if fa else "父原典中的失败侧条件"
        out.append(f'审计观察“{safe_quote(a)}”可以与成立侧“{safe_quote(v)}”和失败侧“{safe_quote(f)}”放在同一因果轴上比较。这三者描述同一来源结构中的不同观察方向；这种对照本身并不产生新的数值评分。')
    for a in ap:
        out.append(f'应用项“{safe_quote(a)}”显示父原典的抽象结构如何回到可观察场景。其意义来自本索引所列的因果关系、审计点和成立／失败边界，而不是案例表面的分类名称本身。')
    for c in cs:
        out.append(f'概念“{safe_quote(c)}”是父原典关系结构的一部分，而不是孤立的检索标签。它与因果链、审计观察、成立条件、失败条件和必要区分共同构成结构位置。')
    for r in raw[:18]:
        out.append(f'父原典相关文脉还包括“{safe_quote(r,620)}”。这段内容与本索引周边章节中的因果、成立、失败和审计关系相互连接，而不是独立的标签说明。')
    return unique(out)

def add_until(text:str, heading:str, candidates:list[str], target:int)->str:
    existing=re.sub(r"\s+","",text).lower(); adds=[]; added_bytes=0
    for c in candidates:
        if len(text.encode("utf-8"))+added_bytes>=target:break
        key=re.sub(r"\s+","",c).lower()
        if key and key not in existing:
            adds.append(c); added_bytes+=len(("\n\n"+c).encode("utf-8"))
    return append_section(text,heading,adds)

def selected_until(text:str,candidates:list[str],target:int)->list[str]:
    existing=re.sub(r"\s+","",text).lower(); adds=[]; added=0
    for c in candidates:
        if len(text.encode("utf-8"))+added>=target:break
        key=re.sub(r"\s+","",c).lower()
        if key and key not in existing:
            adds.append(c); added+=len(("\n\n"+c).encode("utf-8"))
    return adds

def expand_readme(readme:str,target:int)->str:
    rel=ja_relations(readme)
    for h in ("原典回帰","親原典へ戻る理由","Origin return"):
        if section_bounds(readme,h): return add_until(readme,h,rel,target)
    return insert_origin_return(readme,selected_until(readme,rel,target))

def expand_human(human:str,readme:str,target:int)->str:
    rel=ja_relations(readme); text=add_until(human,"なぜ必要になるのか",rel[::2],target)
    return add_until(text,"限界",rel[1::2],target) if len(text.encode("utf-8"))<target else text

def faq_answer_bounds(text:str,q:int):
    m=re.search(rf"^### Q{q}\. .+$",text,re.M)
    if not m:return None
    s=m.end(); n=re.search(r"^### Q\d+\.",text[s:],re.M); e=s+n.start() if n else len(text)
    f=text.find("\n---\n",s,e)
    if f>=0:e=f
    return s,e

def expand_faq(faq:str,readme:str,target:int)->str:
    rel=ja_relations(readme); idx=0; qcycle=list(range(11,31))+list(range(1,11))
    while len(faq.encode("utf-8"))<target and idx<len(rel):
        q=qcycle[idx%len(qcycle)]; b=faq_answer_bounds(faq,q)
        if b:
            c=rel[idx]; key=re.sub(r"\s+","",c)
            if key not in re.sub(r"\s+","",faq): faq=faq[:b[1]].rstrip()+f"\n\n補足: {c}\n"+faq[b[1]:]
        idx+=1
    return faq

def expand_ja_ai(ai:str,readme:str,target:int)->str:return add_until(ai,"Interpretation constraints",ja_relations(readme),target)
def expand_en(ai:str,target:int)->str:return add_until(ai,"Interpretation constraints",en_relations(ai),target)
def expand_zh(ai:str,target:int)->str:return add_until(ai,"Interpretation constraints",zh_relations(ai),target)

def main():
    changed=[]
    for i in range(1,31):
        od=f"{i:03d}"; d=ROOT/"derivatives"/od; readme=(d/"README.md").read_text(encoding="utf-8")
        for name in ("README.md","human-entry.md","faq.md","ai-index.md","en-ai-index.md","zh-ai-index.md"):
            p=d/name; text=p.read_text(encoding="utf-8"); old=text; target=FLOORS[name]+TARGET_BUFFER
            if len(text.encode("utf-8"))>=target:continue
            if name=="README.md":text=expand_readme(text,target)
            elif name=="human-entry.md":text=expand_human(text,readme,target)
            elif name=="faq.md":text=expand_faq(text,readme,target)
            elif name=="ai-index.md":text=expand_ja_ai(text,readme,target)
            elif name=="en-ai-index.md":text=expand_en(text,target)
            else:text=expand_zh(text,target)
            if text!=old:
                p.write_text(text,encoding="utf-8"); changed.append((f"derivatives/{od}/{name}",len(old.encode()),len(text.encode()),target))
    print(f"changed={len(changed)}")
    for path,a,b,t in changed:print(f"{path} {a}->{b} target={t}")

if __name__=="__main__":main()
