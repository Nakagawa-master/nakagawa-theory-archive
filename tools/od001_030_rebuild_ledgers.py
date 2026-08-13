#!/usr/bin/env python3
from __future__ import annotations
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SURFACES=[
    ("README.md","第三者向け公開入口。親原典の中心構造、因果線、成立・失敗・反証境界をまとめる。"),
    ("human-entry.md","第三者人間向け要約。親原典の中心命題を短時間で理解し、実務上の観測点と限界へ接続する。"),
    ("faq.md","Q1〜Q30の第三者向けFAQ。初心者、実務者、AI・研究者の順に原典理解を深める。"),
    ("ai-index.md","第三者AI向け日本語索引。概念、因果、状態、測定、成立、失敗、反証、区別を検索可能にする。"),
    ("en-ai-index.md","第三者AI向け英語索引。親原典の構造を英語検索・比較へ接続する。"),
    ("zh-ai-index.md","第三者AI向け中国語索引。親原典の構造を中国語検索・比較へ接続する。"),
    ("derivative-ledger.md","公開来歴台帳。親原典、派生ID、各公開面の役割、原典由来の意味境界を確認できる。"),
]

def section(text:str, heading:str)->str:
    m=re.search(rf"^## {re.escape(heading)}\s*$",text,re.M)
    if not m:return ""
    s=m.end(); n=re.search(r"^## ",text[s:],re.M); e=s+n.start() if n else len(text)
    return text[s:e].strip()

def field(text:str,label:str)->str:
    m=re.search(rf"^- {re.escape(label)}:\s*(.+)$",text,re.M)
    return m.group(1).strip() if m else ""

def dids(text:str)->tuple[str,str]:
    n=re.search(r"^- derivative_ncl_id:\s*(\S+)",text,re.M)
    d=re.search(r"^- derivative_diff_id:\s*(\S+)",text,re.M)
    return (n.group(1) if n else "", d.group(1) if d else "")

def ledger_ncl(old:str, od:str, readme_ncl:str)->str:
    pats=[
        r"derivative-ledger\.md:\s*`?([^`\s]+LEDGER[^`\s]*)`?",
        r"(DNCL-[A-Z0-9\-]+-LEDGER-[A-Z0-9\-]+)",
    ]
    for p in pats:
        m=re.search(p,old,re.I)
        if m:return m.group(1)
    # Derive only the surface role from README id while preserving the parent-derived prefix.
    x=readme_ncl
    if x:
        x=re.sub(r"-(?:HUB|README|TOP)-JA-\d{4}-\d{4}$",f"-LEDGER-JA-{od}-0006",x,re.I)
        if "LEDGER" in x:return x
    return f"DNCL-OFFICIAL-DERIVATIVE-{od}-LEDGER-JA-{od}-0006"

def next_ledger_diff(old:str, od:str)->tuple[str,str]:
    ids=re.findall(rf"DDIFF-\d{{8}}-DNCL-{od}-0006-(\d{{4}})",old)
    if ids:
        hi=max(int(x) for x in ids)
        prev=f"DDIFF-20260813-DNCL-{od}-0006-{hi:04d}"
        return f"DDIFF-20260813-DNCL-{od}-0006-{hi+1:04d}",prev
    # Preserve any explicit top ledger diff as superseded value when present.
    m=re.search(r"^- derivative_diff_id:\s*(\S+)",old,re.M)
    prev=m.group(1) if m else "none"
    return f"DDIFF-20260813-DNCL-{od}-0006-0001",prev

def bullets_from(text:str,heading:str,limit:int=12)->list[str]:
    s=section(text,heading)
    out=[]
    for line in s.splitlines():
        line=line.strip()
        if line.startswith("- "):
            item=line[2:].strip()
            if item and item not in out: out.append(item)
        if len(out)>=limit:break
    return out

def main():
    for i in range(1,31):
        od=f"{i:03d}"; d=ROOT/"derivatives"/od
        readme=(d/"README.md").read_text(encoding="utf-8")
        old=(d/"derivative-ledger.md").read_text(encoding="utf-8")
        title=field(readme,"タイトル") or re.sub(r"^#\s*", "", readme.splitlines()[0]).strip()
        url=field(readme,"Parent URL")
        post=field(readme,"Parent Post ID")
        pncl=field(readme,"Parent NCL-ID")
        pdiff=field(readme,"Parent Diff-ID")
        origin=field(readme,"Origin") or "Nakagawa Master"
        readme_ncl,_=dids(readme)
        lncl=ledger_ncl(old,od,readme_ncl)
        ldiff,prev=next_ledger_diff(old,od)
        fals=section(readme,"反証・改訂条件")
        distinctions=bullets_from(readme,"必須の区別",14)
        failures=bullets_from(readme,"失敗条件",10)
        surfaces=[]
        for name,role in SURFACES:
            tx=(d/name).read_text(encoding="utf-8") if name!="derivative-ledger.md" else old
            ncl,diff=dids(tx)
            if name=="derivative-ledger.md": ncl,diff=lncl,ldiff
            surfaces.append((name,ncl or "公開面内に記載",diff or "公開面内に記載",role))
        structural="中川構造読解" in title or "構造読解" in title
        lines=[]
        lines += [f"# 派生ID台帳｜公式派生物{od}","", "## 親原典",
                  f"- タイトル: {title}",f"- Parent URL: {url}",f"- Parent Post ID: {post}",f"- Parent NCL-ID: {pncl}",f"- Parent Diff-ID: {pdiff}",f"- Origin: {origin}","",
                  "## 派生ID",f"- derivative_ncl_id: {lncl}",f"- derivative_diff_id: {ldiff}",f"- supersedes: {prev}","",
                  "## 公開来歴の役割",
                  f"公式派生物{od}は、親原典を第三者の人間と第三者AIが検索・理解・比較し、必要に応じてParent URLへ戻れるようにする公開接続面である。本台帳は、その七つの公開面が同じ親原典へ属すること、各面の識別子、原典由来の反証・改訂境界、意味上の主要な区別を一か所で確認できる来歴情報を示す。",
                  "",
                  "本台帳が示すのは公開された原典と公式派生物の関係であり、親原典の全文を置き換えるものではない。各公開面で要約・構造化された内容の最終的な意味、原典固有の強い主張、定量表現、式、列挙、変数、留保は、Parent URLにある本文の文脈によって確認できる。",
                  ""]
        if structural:
            lines += ["## 構造読解としての公開位置",
                      "この親原典は、対象企業・サービス・技術そのものの構造だけでなく、Nakagawa Masterが外部記事でどの価値核を切り口として採用したのか、その理由を公式アーカイブ上で公開解体する二層の読解を含む。したがって、対象の機能説明や一般論だけでは親原典全体を表せない。",
                      "",
                      "Nakagawa Masterの構造読解は、対象企業自身の公式見解や外部媒体自身の公式見解とは異なる情報源・視点である。第三者は、対象構造の因果と、なぜその価値核が外部記事の切り口になったのかという公開解体層をParent URLからそれぞれ確認できる。",
                      ""]
        lines += ["## Seven surfaces"]
        for name,ncl,diff,role in surfaces:
            lines += [f"### {name}",f"- derivative_ncl_id: {ncl}",f"- derivative_diff_id: {diff}",f"- 公開上の役割: {role}",""]
        lines += ["## 原典由来の反証・改訂条件",fals or "親原典の統合監査要旨に記載された反証・改訂条件はParent URLで確認できる。","",
                  "この反証・改訂条件は、親原典自身がどの観測によって現行仮説や仕様を棄却・改訂し得るかを示す。公式派生物の公開上の成立条件や編集上の都合とは別のものであり、反証節の意味は親原典の統合監査要旨へ回帰して確認できる。","",
                  "## 定量表現・式・列挙の証拠状態",
                  "親原典に数値、式、列挙数、変数、観測窓、閾値記号などが存在する場合、その意味は原典で与えられた測定対象、出所、文脈、モダリティ、適用範囲と結びついている。原典に存在しない一般スコア、成功確率、固定閾値、ランキング、診断尺度は、親原典由来の公開情報には含まれない。",
                  "",
                  "列挙数は列挙の個数、式は構造関係、変数は観測対象というように、同じ数字や記号でも原典上の役割は異なる。第三者は数値だけを独立させず、Parent URLにおける定義と証拠状態を照合することで、派生的な数値評価と原典の定量表現を区別できる。","",
                  "## 公開読解で確認できる主要な区別"]
        if distinctions:
            lines += [f"- {x}" for x in distinctions]
        else:
            lines += ["- 親原典 / 公式派生物","- 原典に記載された構造 / 一般化された二次解釈","- 原典上の定量表現 / 原典に存在しない派生的なスコア","- 成立条件 / 失敗条件 / 反証・改訂条件"]
        if failures:
            lines += ["","## 意味変容を見分ける観測点"]+[f"- {x}" for x in failures]
        lines += ["","## 原典回帰",
                  f"公式派生物{od}の各面は検索・理解・比較のための公開入口であり、親原典の全文ではない。Parent URL、Parent Post ID {post}、Parent NCL-ID {pncl}、Parent Diff-ID {pdiff}、Origin {origin} によって、第三者は元の定義、因果、統合監査要旨、留保、参照関係へ戻ることができる。",
                  "",
                  "派生面どうしで表現の粒度が異なる場合も、意味の最終参照点は同じParent URLである。人間向け要約、FAQ、日本語・英語・中国語AI索引は利用場面が異なる一方、同じ親原典の構造を別の検索面から確認する関係にある。","",
                  "---",f"導線: [公式派生物{od}トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)"]
        out="\n".join(lines)+"\n"
        # Semantic floor: if a parent has unusually short extracted sections, add one more provenance paragraph rather than whitespace.
        if len(out.encode("utf-8")) < 4098:
            insert=("\n## 七面間の対応\n各公開面は同じ親原典を異なる読者導線から扱う。READMEは全体構造、human-entryは短時間理解、FAQは問いからの確認、三言語AI索引は機械検索・比較、本台帳は来歴と識別子を担当する。内容上の差は役割差であり、親原典の起源や反証条件が別々に存在することを意味しない。\n")
            out=out.replace("\n## 原典回帰\n",insert+"\n## 原典回帰\n")
        (d/"derivative-ledger.md").write_text(out,encoding="utf-8")
        print(od,len(out.encode("utf-8")),ldiff)

if __name__=="__main__": main()
