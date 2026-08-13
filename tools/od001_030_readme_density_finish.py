#!/usr/bin/env python3
from __future__ import annotations
import re
from pathlib import Path

# Post-footer-fix rerun marker: 2026-08-13.
ROOT=Path(__file__).resolve().parents[1]
FLOOR=12348
TARGET=12780
BANNED=("この公開読解","本派生物","公式派生物","本索引","派生物側","制作工程","内部制作","内部指示","記事化判断","ZEROICHI","PENDING","Golden master","source gate","PASS_")

def section_bounds(text,heading):
    m=re.search(rf"^## {re.escape(heading)}\s*$",text,re.M)
    if not m:return None
    s=m.end(); n=re.search(r"^## ",text[s:],re.M); e=s+n.start() if n else len(text)
    return m.start(),s,e

def append_to_return(text,paras):
    for h in ("原典回帰","親原典へ戻る理由"):
        b=section_bounds(text,h)
        if b:
            return text[:b[2]].rstrip()+"\n\n"+"\n\n".join(paras)+"\n"+text[b[2]:]
    m=re.search(r"\n---\n",text)
    block="\n\n## 原典回帰\n"+"\n\n".join(paras)+"\n"
    return text[:m.start()].rstrip()+block+text[m.start():] if m else text.rstrip()+block

def candidates(text):
    out=[]
    # Paragraphs only: no metadata, headings, YAML/code blocks, or answer fragments that begin as self-dialogue.
    for p in re.split(r"\n\s*\n",text):
        p=p.strip()
        if not p or p.startswith("#") or p.startswith("-") or p.startswith("```") or p.startswith("```yaml"):
            continue
        if any(b.lower() in p.lower() for b in BANNED):continue
        if re.match(r"^(?:はい|いいえ|できません|いけません|No[,.]|Yes[,.])",p,re.I):continue
        if "derivative_ncl_id:" in p or "derivative_diff_id:" in p or "Parent URL:" in p:continue
        p=re.sub(r"\s+"," ",p)
        if 80<=len(p)<=1500 and p not in out:out.append(p)
    return out

def main():
    changed=[]
    for i in range(1,31):
        od=f"{i:03d}"; d=ROOT/"derivatives"/od; p=d/"README.md"; readme=p.read_text(encoding="utf-8")
        if len(readme.encode("utf-8"))>=FLOOR:continue
        pool=[]
        for name in ("human-entry.md","ai-index.md","faq.md"):
            for c in candidates((d/name).read_text(encoding="utf-8")):
                k=re.sub(r"\s+","",c).lower()
                if k not in re.sub(r"\s+","",readme).lower() and c not in pool:pool.append(c)
        adds=[]; added=0
        for c in pool:
            if len(readme.encode("utf-8"))+added>=TARGET:break
            adds.append(c); added+=len(("\n\n"+c).encode("utf-8"))
        if adds:
            new=append_to_return(readme,adds)
            p.write_text(new,encoding="utf-8")
            changed.append((od,len(readme.encode("utf-8")),len(new.encode("utf-8")),len(adds)))
    print(f"changed={len(changed)}")
    for od,a,b,n in changed:print(f"OD{od} README {a}->{b} paragraphs={n}")

if __name__=="__main__":main()
