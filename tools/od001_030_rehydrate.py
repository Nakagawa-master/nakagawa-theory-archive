#!/usr/bin/env python3
from __future__ import annotations
import re, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SURFACES=["README.md","human-entry.md","faq.md","ai-index.md","en-ai-index.md","zh-ai-index.md","derivative-ledger.md"]
FLOORS={"README.md":12348,"human-entry.md":6403,"faq.md":11177,"ai-index.md":10389,"en-ai-index.md":12200,"zh-ai-index.md":9888,"derivative-ledger.md":4098}

def candidates_for(od: str):
    n=int(od)
    refs=[
        "origin/repair/od001-133-structural-rebuild-20260812",
        "origin/od002-od133-reaudit-repair-20260812",
        f"origin/repair/p0-od{od}-golden-master",
        f"origin/reaudit/od{od}-full-rebuild-20260812",
        f"origin/repair/lot3-od{od}-semantic-fidelity",
    ]
    if od=="001": refs += ["origin/audit-rebuild-od001"]
    if od=="002": refs += [
        "origin/repair/p0-od002-golden-master-v2",
        "origin/fix/od002-benchmark-parity-final-20260812",
        "origin/fix/od002-benchmark-parity-v2-20260812",
        "origin/repair/od002-literal-134-135-structure-20260812",
        "origin/repair/od002-004-structure-reset-20260812",
    ]
    if od=="003": refs += ["origin/repair/od003-literal-134-135-structure-20260812b","origin/repair/od002-004-structure-reset-20260812"]
    if od=="004": refs += ["origin/reaudit/od004-reapply-current-main-20260812","origin/repair/od002-004-structure-reset-20260812"]
    if od=="005": refs += ["origin/reaudit/od005-current-main-full-rebuild-20260812"]
    if od=="007": refs += ["origin/reaudit/od007-literal-volume-closure-20260812"]
    if od=="009": refs += ["origin/reaudit/od009-literal-full-rebuild-20260812","origin/reaudit/od009-full-rebuild-rebased-20260812"]
    if 2 <= n <= 10: refs += ["origin/repair/p0-od002-010-golden-master"]
    if 2 <= n <= 13: refs += [f"origin/reaudit/od{od}-full-rebuild-20260812"]
    if 22 <= n <= 30: refs += [f"origin/repair/lot3-od{od}-semantic-fidelity"]
    return list(dict.fromkeys(refs))

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
        return subprocess.check_output(["git","show",f"{ref}:{path}"],cwd=ROOT,stderr=subprocess.DEVNULL).decode("utf-8")
    except Exception:
        return None

def preserve_sections(current,candidate,name):
    headings=["親原典","派生ID"]
    if name=="README.md": headings.append("反証・改訂条件")
    elif name in ("ai-index.md","en-ai-index.md","zh-ai-index.md"): headings.append("Falsification conditions")
    for h in headings:
        c=sec(current,h)
        if c and sec(candidate,h): candidate=replace_sec(candidate,h,c[2])
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
            best=current; best_ref="current"
            for ref in candidates_for(od):
                cand=git_show(ref,rel)
                if not cand: continue
                cand=preserve_sections(current,cand,name).replace("ZEROICHI","外部記事")
                if len(cand.encode())>len(best.encode()):
                    best=cand; best_ref=ref
            if best!=current:
                p.write_text(best,encoding="utf-8")
                changed.append((rel,len(current.encode()),len(best.encode()),best_ref))
    print(f"rehydrated={len(changed)}")
    for rel,a,b,ref in changed: print(f"{rel} {a}->{b} via {ref}")

if __name__=="__main__": main()
