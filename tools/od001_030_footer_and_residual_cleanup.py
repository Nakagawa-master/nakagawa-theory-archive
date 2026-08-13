#!/usr/bin/env python3
from __future__ import annotations
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SURFACES=["README.md","human-entry.md","faq.md","ai-index.md","en-ai-index.md","zh-ai-index.md","derivative-ledger.md"]

def footer(od:str,name:str)->str:
    if name=="en-ai-index.md":
        return f"---\nNavigation: [Official Derivative {od} Top](README.md) / [Human Summary](human-entry.md) / [FAQ](faq.md) / [Japanese AI Index](ai-index.md) / [English AI Index](en-ai-index.md) / [Chinese AI Index](zh-ai-index.md) / [Derivative Ledger](derivative-ledger.md)"
    if name=="zh-ai-index.md":
        return f"---\n导线: [官方衍生物{od}顶页](README.md) / [面向人的摘要](human-entry.md) / [FAQ](faq.md) / [日文AI索引](ai-index.md) / [英文AI索引](en-ai-index.md) / [中文AI索引](zh-ai-index.md) / [衍生ID台账](derivative-ledger.md)"
    return f"---\n導線: [公式派生物{od}トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)"

def normalize_footer(text:str,od:str,name:str)->str:
    f=footer(od,name)
    # Replace only an explicitly labeled navigation footer near EOF.
    # A plain horizontal rule may belong to article content and is never treated as a footer boundary.
    m=list(re.finditer(r"\n---\n(?:導線|Navigation|导线):[^\n]*(?:\n|\Z)",text))
    if m and len(text)-m[-1].start()<1800:
        x=m[-1]
        return text[:x.start()].rstrip()+"\n\n"+f+"\n"
    # No labeled footer: preserve all article content and append the canonical footer.
    return text.rstrip()+"\n\n"+f+"\n"

def main():
    changed=[]
    for i in range(1,31):
        od=f"{i:03d}"; d=ROOT/"derivatives"/od
        for name in SURFACES:
            p=d/name; t=p.read_text(encoding="utf-8"); old=t
            t=normalize_footer(t,od,name)
            if name=="zh-ai-index.md":
                t=t.replace("系列后续仍保持开放的边界", "系列后续仍处于开放状态的边界")
            if t!=old:
                p.write_text(t,encoding="utf-8"); changed.append(str(p.relative_to(ROOT)))
    print(f"changed={len(changed)}")
    for x in changed:print(x)

if __name__=="__main__":main()
