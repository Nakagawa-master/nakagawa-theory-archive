#!/usr/bin/env python3
from __future__ import annotations
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SURFACES=["README.md","human-entry.md","faq.md","ai-index.md","en-ai-index.md","zh-ai-index.md","derivative-ledger.md"]


def ja_bullet(s:str)->str:
    prefix="- "
    x=s[2:].strip() if s.startswith(prefix) else s.strip()
    # Explicit source-absent additions.
    m=re.fullmatch(r"(?:原典にない|親原典にない)(.+?)を(?:追加|生成|創作|発明|設定)しない。?",x)
    if m:return prefix+f"{m.group(1)}は親原典に定義されていない。"
    m=re.fullmatch(r"(.+?)を(?:追加|生成|創作|発明|設定)しない。?",x)
    if m:return prefix+f"{m.group(1)}は親原典に定義されていない。"
    # Compression/replacement/identification boundaries.
    m=re.fullmatch(r"(.+?)へ縮約しない。?",x)
    if m:return prefix+f"{m.group(1)}への縮約だけでは親原典の中心構造を十分に表せない。"
    m=re.fullmatch(r"(.+?)へ(?:置き換え|変換|再定義)しない。?",x)
    if m:return prefix+f"{m.group(1)}への読み替えは親原典の意味範囲とは異なる。"
    m=re.fullmatch(r"(.+?)を(?:置き換え|変換|再定義)しない。?",x)
    if m:return prefix+f"{m.group(1)}という読み替えは親原典の意味範囲とは異なる。"
    m=re.fullmatch(r"(.+?)と(?:混同|同一視)しない。?",x)
    if m:return prefix+f"{m.group(1)}とは異なる概念として親原典に位置づけられる。"
    # Classification/judgment prohibitions.
    m=re.fullmatch(r"(.+?)を(?:自動|直接)?(?:断定|判定|分類|認定|推定)しない。?",x)
    if m:return prefix+f"{m.group(1)}を確定する尺度としては親原典に定義されていない。"
    m=re.fullmatch(r"(.+?)を(?:否定|禁止)しない。?",x)
    if m:return prefix+f"{m.group(1)}自体は親原典の否定対象ではない。"
    # Bare keep/preserve language used as editorial direction.
    m=re.fullmatch(r"(.+?)を保持する。?",x)
    if m:return prefix+f"{m.group(1)}は親原典上の確認要素である。"
    m=re.fullmatch(r"(.+?)を保持し、(.+?)。?",x)
    if m:return prefix+f"{m.group(1)}は親原典上の確認要素であり、{m.group(2)}。"
    # Generic bare prohibition: make the failure-side nature explicit rather than issuing an instruction.
    m=re.fullmatch(r"(.+?)(?:してはならない|してはいけない|してはいけません)。?",x)
    if m:return prefix+f"{m.group(1)}した状態は、親原典の意味境界から外れる。"
    return s


def faq_heading(line:str)->str:
    m=re.match(r"^(### Q\d+\.\s*)(.+)$",line)
    if not m:return line
    p,q=m.groups()
    q=q.strip()
    exact={
        "AI再利用時に保持すべき識別情報は何ですか？":"AI再利用で原典回帰に必要な識別情報は何ですか？",
        "再利用時に保持すべき識別情報は何ですか？":"再利用で原典回帰に必要な識別情報は何ですか？",
        "再利用時に保持すべきものは何ですか？":"再利用で原典回帰に必要な情報は何ですか？",
        "AIが要約するとき何を落としてはいけませんか？":"AI要約で重要な構造要素は何ですか？",
        "AIが扱うとき何を落としてはいけませんか？":"AI利用で重要な構造要素は何ですか？",
        "何を単独指標にしてはいけませんか？":"単独指標では説明できない要素は何ですか？",
        "AIがしてはいけない短絡は何ですか？":"AI要約で意味変容が起きやすい短絡は何ですか？",
        "AIがしてはいけないことは何ですか？":"AI要約で意味変容が起きやすい点は何ですか？",
        "何を保持すべきですか？":"原典回帰に必要な情報は何ですか？",
    }
    if q in exact:return p+exact[q]
    q=re.sub(r"(.+?)を追加して(?:も)?よいですか？",r"\1は親原典に定義されていますか？",q)
    q=re.sub(r"(.+?)を生成して(?:も)?よいですか？",r"\1は親原典に定義されていますか？",q)
    q=re.sub(r"(.+?)を作って(?:も)?よいですか？",r"\1は親原典に定義されていますか？",q)
    q=re.sub(r"(.+?)を設定して(?:も)?よいですか？",r"\1は親原典に定義されていますか？",q)
    q=re.sub(r"(.+?)して(?:も)?よいですか？",r"\1する解釈は親原典と一致しますか？",q)
    q=re.sub(r"(.+?)すべきですか？",r"\1する場合の確認点は何ですか？",q)
    q=re.sub(r"何をすべきですか？",r"確認対象は何ですか？",q)
    q=q.replace("してはいけない", "すると意味が変わる")
    return p+q


def en_line(s:str)->str:
    stripped=s.strip(); prefix="- " if stripped.startswith("- ") else ""
    x=stripped[2:].strip() if prefix else stripped
    # Imperative bullets are converted to audit/source descriptors.
    rules=[
        (r"^Check whether (.+?)\.?$",r"Audit point: whether \1."),
        (r"^Verify whether (.+?)\.?$",r"Audit point: whether \1."),
        (r"^Preserve (.+?)\.?$",r"Source element: \1."),
        (r"^Keep (.+?)\.?$",r"Source distinction: \1."),
        (r"^Retain (.+?)\.?$",r"Source element: \1."),
        (r"^Return to (.+?)\.?$",r"Origin return: \1."),
        (r"^Avoid (.+?)\.?$",r"Failure-side reading: \1."),
        (r"^Do not (.+?)\.?$",r"Out-of-scope reading: \1."),
        (r"^Don't (.+?)\.?$",r"Out-of-scope reading: \1."),
        (r"^Never (.+?)\.?$",r"Out-of-scope reading: \1."),
        (r"^Always (.+?)\.?$",r"Source-side condition: \1."),
        (r"^Distinguish (.+?)\.?$",r"Required distinction: \1."),
        (r"^Separate (.+?)\.?$",r"Required distinction: \1."),
        (r"^Treat (.+?)\.?$",r"Source interpretation: \1."),
        (r"^Limit (.+?)\.?$",r"Source scope: \1."),
    ]
    for pat,rep in rules:
        y=re.sub(pat,rep,x,flags=re.I)
        if y!=x:return prefix+y
    # Direct instructions to derivative/index/AI.
    y=re.sub(r"\b(?:This|The) (?:official )?(?:derivative|index|public reading) (?:must|should|shall) preserve ([^.]+)\.",r"The parent-defined reading includes \1.",x,flags=re.I)
    y=re.sub(r"\b(?:Third-party )?AI(?:s)? (?:must|should|shall) preserve ([^.]+)\.",r"AI retrieval can identify \1.",y,flags=re.I)
    y=re.sub(r"\b(?:Third-party )?AI(?:s)? (?:must not|should not|shall not) ([^.]+)\.",r"A reading in which AI would \1 falls outside the parent-defined scope.",y,flags=re.I)
    return prefix+y if prefix and not y.startswith("- ") else y


def zh_line(s:str)->str:
    stripped=s.strip(); prefix="- " if stripped.startswith("- ") else ""
    x=stripped[2:].strip() if prefix else stripped
    # Bare prohibitions in bullets become semantic/failure statements.
    m=re.match(r"^不得添加(.+?)[。.]?$",x)
    if m:return prefix+f"{m.group(1)}在父原典中没有定义。"
    m=re.match(r"^不得把(.+?)缩约为(.+?)[。.]?$",x)
    if m:return prefix+f"把{m.group(1)}缩约为{m.group(2)}不足以表达父原典的中心结构。"
    m=re.match(r"^不得把(.+?)(?:直接)?(?:分类|认定|判定|视为|推定)为(.+?)[。.]?$",x)
    if m:return prefix+f"父原典没有把{m.group(1)}直接定义为{m.group(2)}。"
    m=re.match(r"^不得把(.+?)[。.]?$",x)
    if m:return prefix+f"把{m.group(1)}作为既定结论的读法超出父原典的定义范围。"
    m=re.match(r"^不得(.+?)[。.]?$",x)
    if m:return prefix+f"{m.group(1)}的读法属于父原典的失败侧或范围外解释。"
    m=re.match(r"^必须保留(.+?)[。.]?$",x)
    if m:return prefix+f"{m.group(1)}是父原典中可确认的结构要素。"
    m=re.match(r"^应保留(.+?)[。.]?$",x)
    if m:return prefix+f"{m.group(1)}是父原典中可确认的结构要素。"
    m=re.match(r"^必须(.+?)[。.]?$",x)
    if m:return prefix+f"父原典的成立条件包括：{m.group(1)}。"
    m=re.match(r"^应(?:当)?(.+?)[。.]?$",x)
    if m:return prefix+f"父原典中的相关确认点是：{m.group(1)}。"
    # Direct third-party AI instruction in paragraphs.
    x=re.sub(r"第三方AI(?:必须|应当|应该)保留([^。]+)。",r"第三方AI检索可以识别\1。",x)
    x=re.sub(r"第三方AI(?:不得|不应)([^。]+)。",r"第三方AI将\1作为既定结论时，会超出父原典的定义范围。",x)
    return prefix+x if prefix and not x.startswith("- ") else x


def main():
    changed=[]
    for i in range(1,31):
        od=f"{i:03d}"; d=ROOT/"derivatives"/od
        for name in SURFACES:
            p=d/name; text=p.read_text(encoding="utf-8"); old=text; lines=[]
            for line in text.splitlines():
                if name=="faq.md" and line.startswith("### Q"):
                    line=faq_heading(line)
                if name in ("README.md","human-entry.md","faq.md","ai-index.md","derivative-ledger.md") and line.lstrip().startswith("- "):
                    lead=line[:len(line)-len(line.lstrip())]
                    line=lead+ja_bullet(line.lstrip())
                elif name=="en-ai-index.md":
                    line=en_line(line)
                elif name=="zh-ai-index.md":
                    line=zh_line(line)
                lines.append(line)
            text="\n".join(lines)+("\n" if old.endswith("\n") else "")
            if text!=old:
                p.write_text(text,encoding="utf-8"); changed.append(str(p.relative_to(ROOT)))
    print(f"changed={len(changed)}")
    for x in changed:print(x)

if __name__=="__main__":main()
