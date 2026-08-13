#!/usr/bin/env python3
from __future__ import annotations
import re, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SURFACES=["README.md","human-entry.md","faq.md","ai-index.md","en-ai-index.md","zh-ai-index.md","derivative-ledger.md"]
FLOORS={"README.md":12348,"human-entry.md":6403,"faq.md":11177,"ai-index.md":10389,"en-ai-index.md":12200,"zh-ai-index.md":9888,"derivative-ledger.md":4098}
CANDIDATES=["origin/repair/od001-133-structural-rebuild-20260812"]

def sec(text,h):
    m=re.search(rf"^## {re.escape(h)}\s*$",text,re.M)
    if not m:return None
    s=m.end(); n=re.search(r"^## ",text[s:],re.M); e=s+n.start() if n else len(text)
    return (m.start(),e,text[m.start():e].rstrip())

def replace_sec(text,h,replacement):
    x=sec(text,h)
    if not x:return text
    return text[:x[0]]+replacement+"\n\n"+text[x[1]:].lstrip("\n")

def git_show(ref,path):
    try:
        return subprocess.check_output(["git","show",f"{ref}:{path}"],cwd=ROOT).decode("utf-8")
    except Exception:
        return None

def preserve_sections(current,candidate,name):
    # Keep the branch-current source identity and source-derived falsification sections.
    headings=["親原典","派生ID"]
    if name=="README.md": headings.append("反証・改訂条件")
    elif name in ("ai-index.md","en-ai-index.md","zh-ai-index.md"): headings.append("Falsification conditions")
    for h in headings:
        c=sec(current,h)
        if c and sec(candidate,h): candidate=replace_sec(candidate,h,c[2])
    # Keep current navigation footer, which is already seven-link verified.
    m=re.search(r"\n---\n(?:導線|Navigation|导线):.*\Z",current,re.S)
    if m:
        candidate=re.sub(r"\n---\n(?:導線|Navigation|导线):.*\Z",m.group(0),candidate,flags=re.S)
    return candidate

def main():
    changed=[]
    for i in range(1,31):
        od=f"{i:03d}"
        for name in SURFACES:
            p=ROOT/"derivatives"/od/name
            current=p.read_text(encoding="utf-8")
            if len(current.encode())>=FLOORS[name]: continue
            rel=f"derivatives/{od}/{name}"
            best=current
            for ref in CANDIDATES:
                cand=git_show(ref,rel)
                if not cand: continue
                cand=preserve_sections(current,cand,name)
                if len(cand.encode())>len(best.encode()): best=cand
            if best!=current:
                # Explicit media-name repetition is not part of public derivative prose.
                best=best.replace("ZEROICHI","外部記事")
                p.write_text(best,encoding="utf-8")
                changed.append((rel,len(current.encode()),len(best.encode())))
    print(f"rehydrated={len(changed)}")
    for rel,a,b in changed: print(f"{rel} {a}->{b}")

if __name__=="__main__": main()
