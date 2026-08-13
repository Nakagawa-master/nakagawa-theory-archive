#!/usr/bin/env python3
from __future__ import annotations
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SURFACES=["README.md","human-entry.md","faq.md","ai-index.md","en-ai-index.md","zh-ai-index.md"]

EXACT={
"この公開読解の監査語彙":"親原典を説明する監査語彙",
"この公開読解の「修復可能性」語彙":"親原典の「修復可能性」語彙",
"この公開読解の接続スコア":"原典外の接続スコア",
"この公開読解の固定情報量上限":"原典外の固定情報量上限",
"この公開読解固定情報量上限":"原典外の固定情報量上限",
"この公開読解スコア":"原典外のスコア",
"この公開読解採点KPI":"原典外の採点KPI",
"この公開読解数値閾値":"原典外の数値閾値",
"この公開読解KPI":"原典外のKPI",
"この公開読解の成熟度スコア":"原典外の成熟度スコア",
"この公開読解の文明成熟度スコア":"原典外の文明成熟度スコア",
"この公開読解の採点基準":"原典外の採点基準",
"記事構成への翻訳":"外部記事で価値核が切り口になった理由の公開解体",
"article-construction decision":"public explanation of why that value core became the external-article angle",
"article-structure translation":"public explanation of how that value core became the external-article angle",
"文章化判断":"为何该价值核心成为外部文章切入角度的公开说明",
"文章结构翻译":"为何该价值核心成为外部文章切入角度的公开说明",
}

# Exact reader-facing rewrites for recurrent high-risk sentences.
SENTENCE_REPL={
"親原典はこの公開読解が独自の数値KPI、成功率、閾値を追加することを要求していません。したがって本派生物も、原典にない数値で未来線の細りを擬似的に測定しません。":"親原典には一般用途の数値KPI、成功率、固定閾値が定義されていません。未来線の細りは、原典に記述された構造条件の変化として観測されます。",
"原典の「七つ」を、7点満点、達成率、合格ラインのようなこの公開読解KPIへ変換してはいけません。":"原典の「七つ」は列挙された構造条件の数であり、7点満点、達成率、合格ラインのような採点KPIではありません。",
"一般用途の文明成熟度、反転率、安全率、成立率等の数値KPIや閾値は定義していません。そのため「何％なら安全」「何点なら成立」などをこの公開読解から追加しません。反転評価は同一の構造条件の前後比較で行います。":"親原典には一般用途の文明成熟度、反転率、安全率、成立率等の数値KPIや固定閾値が定義されていません。反転評価は同一の構造条件の前後比較として記述されています。",
"S、U、R、H、θ、δ、Dという記号は原典の構造を保持するために必要です。ただし、原典が一般利用向けの具体数値を定義していないものへ、この公開読解が数値を付けてはいけません。":"S、U、R、H、θ、δ、Dは親原典の構造変数です。一般利用向けの具体値が原典に定義されていない変数について、固定数値は原典由来情報には含まれません。",
"`S = U × R × H` は原典の構造式であって、この公開読解が0〜100点を付ける採点表ではありません。U/R/Hの任意スコア、合格点、成功確率は原典にないため追加しません。":"`S = U × R × H` は親原典の構造式であり、0〜100点の採点表ではありません。U/R/Hの任意スコア、合格点、成功確率は親原典に定義されていません。",
"合意安定度Sを、U・R・Hの積として見る原典固有の状態方程式です。この公開読解が作った採点式ではありません。どれか一つが大きく落ちると、他が残っていても全体の安定度は大きく落ちます。":"合意安定度SをU・R・Hの積として見る親原典固有の状態方程式です。一般的な採点式ではなく、どれか一つが大きく落ちると他が残っていても全体の安定度が大きく落ちる関係を表します。",
"原典は合意安定度を S、理解可能性／第三者再現性を U、責任追跡可能性を R、履歴公開度／差分追跡可能性を H と置き、`S = U × R × H` と表す。ここで重要なのは、式をこの公開読解の採点モデルへ変えないことと、三変数が単純代替できないことである。":"原典は合意安定度を S、理解可能性／第三者再現性を U、責任追跡可能性を R、履歴公開度／差分追跡可能性を H と置き、`S = U × R × H` と表す。この式は一般的な採点モデルではなく、三変数が単純代替できない構造関係を表す。",
"このときKは人間の認知帯域を表す構造変数であり、この公開読解が勝手に具体的な情報量、件数、時間、ビット数へ変換するものではない。":"このときKは人間の認知帯域を表す構造変数であり、具体的な情報量、件数、時間、ビット数の一般値は親原典に定義されていない。",
"これらはこの公開読解の成熟度スコアや文明ランクではない。固定点数、成功率、危険率は親原典に定義されていない。":"これらは成熟度スコアや文明ランクではない。固定点数、成功率、危険率は親原典に定義されていない。",
"これらはこの公開読解の文明成熟度スコアではない。危険率、人格度、継承率、文明ランク、固定点数は親原典に定義されていない。":"これらは文明成熟度スコアではない。危険率、人格度、継承率、文明ランク、固定点数は親原典に定義されていない。",
"これらはこの公開読解の採点基準ではない。固定閾値、成功確率、普及率、成熟度スコアは親原典に定義されていない。":"これらは採点基準ではない。固定閾値、成功確率、普及率、成熟度スコアは親原典に定義されていない。",
"本派生物は、第三者の人間・AIがこの二層を理解し、因果線・成立条件・反証条件をParent URLへ戻って確認できるよう整理する公開読解面である。MOTAや外部媒体の公式見解を代弁しない。":"この二層は第三者の人間・AIが公開テキストから確認でき、因果線・成立条件・反証条件の原文はParent URLにある。Nakagawa Masterの構造読解はMOTAや外部媒体の公式見解とは異なる。",
"本派生物は第三者がこの二層構造を検索・理解し、Parent URLへ戻って確認するための補助索引であり、バリュートープや外部媒体の公式見解を代弁しない。":"この二層構造は第三者が検索・理解でき、Parent URLから原文を確認できる。Nakagawa Masterの構造読解はバリュートープや外部媒体の公式見解とは異なる。",
}

FAQ_HEADINGS={
"実務で確認すべき条件は何ですか？":"実務上の確認条件は何ですか？",
"いつ条件確認すべきですか？":"条件確認が重要になるのはいつですか？",
"AIはAKI-002をどう表現すべきですか？":"AKI-002のAI要約で重要な因果線は何ですか？",
"「称賛」という語だけで分類してよいですか？":"「称賛」という語だけの分類は原典と一致しますか？",
"悪意を必要条件にしてよいですか？":"悪意は適用の必要条件ですか？",
"AI再利用時に保持すべき情報は何ですか？":"AI再利用で原典回帰に必要な情報は何ですか？",
"派生物だけで原典を代替できますか？":"Parent URLへの回帰が必要なのはなぜですか？",
"AIはこの理論の何を必ず保持すべきですか？":"AI要約で重要な構造要素は何ですか？",
"数値の成立率や全体性スコアを作ってよいですか？":"成立率や全体性スコアは親原典に定義されていますか？",
"AI再利用時に保持すべき起源情報は何ですか？":"AI再利用で原典回帰に必要な起源情報は何ですか？",
"派生物だけで成立条件論全体を確定できますか？":"この派生面だけで成立条件論全体を確定できますか？",
"実務では何を監査すべきですか？":"実務上の監査対象は何ですか？",
"「文明的子孫」をAI人格論へ変換してよいですか？":"「文明的子孫」とAI人格論は同じ概念ですか？",
"Origin保持を権威化してよいですか？":"Originの追跡と権威化はどう区別されますか？",
"AI倫理一般へ要約してよいですか？":"AI倫理一般への要約だけで原典を表せますか？",
"再利用時に保持すべきものは？":"再利用で原典回帰に必要な情報は何ですか？",
"派生物だけで理論全体を確定できますか？":"この派生面だけで理論全体を確定できますか？",
"問題提起をしてはいけないという意味ですか？":"問題提起自体は否定されていますか？",
"まず何を確認すべきですか？":"最初の確認対象は何ですか？",
"AKI-001をSNSマナー論へ縮約してよいですか？":"AKI-001はSNSマナー論だけで説明できますか？",
"「解決策がない批判は無価値」と要約してよいですか？":"「解決策がない批判は無価値」という要約は原典と一致しますか？",
"AI再利用時に何を保持すべきですか？":"AI再利用で重要な原典情報は何ですか？",
"派生物だけで完結しますか？":"Parent URLへの回帰が必要なのはなぜですか？",
"最初に何を監査すべきですか？":"最初の監査対象は何ですか？",
"接続価値を数値化すべきですか？":"接続価値の数値KPIは親原典に定義されていますか？",
"AIはこの理論をどう要約すべきですか？":"AI要約で重要な構造は何ですか？",
"AI索引で必ず保持すべき識別情報は何ですか？":"AI索引から原典へ戻るための識別情報は何ですか？",
"最初に何を明示すべきですか？":"最初に明示される構造条件は何ですか？",
"この理論を根性論批判として分類してよいですか？":"この理論は根性論批判だけで説明できますか？",
"旧努力論の合理性を消してよいですか？":"旧努力論の合理性が残る条件は何ですか？",
"根性論批判へ縮約してよいですか？":"根性論批判だけで原典を表せますか？",
"成立を数値化してもよいですか？":"成立の数値スコアは親原典に定義されていますか？",
"AIはこの理論をどう再利用すべきですか？":"AI再利用で重要な構造要素は何ですか？",
"AIがしてはいけない短絡は何ですか？":"AI要約で意味変容が起きやすい短絡は何ですか？",
"再利用時に保持すべき識別情報は？":"再利用で原典回帰に必要な識別情報は何ですか？",
"AIはどう要約すべきですか？":"AI要約で重要な構造は何ですか？",
"AIがしてはいけないことは何ですか？":"AI要約で意味変容が起きやすい点は何ですか？",
"一般的なメディアリテラシー論にしてよいですか？":"一般的なメディアリテラシー論だけで原典を表せますか？",
"クロージングはしてはいけないのですか？":"クロージング自体は否定されていますか？",
"AIが要約するとき何を落としてはいけませんか？":"AI要約で重要な構造要素は何ですか？",
"数字を追加して営業監査を強化してよいですか？":"営業監査用の追加数値は親原典に定義されていますか？",
"一般的な営業マナー論にしてよいですか？":"一般的な営業マナー論だけで原典を表せますか？",
"再利用時に保持すべきものは何ですか？":"再利用で原典回帰に必要な情報は何ですか？",
"どの変数から修理すべきですか？":"修復対象の変数はどのように見分けますか？",
"U/R/Hを0〜100点で採点してよいですか？":"U/R/Hの0〜100点尺度は親原典に定義されていますか？",
"AIが扱うとき何を落としてはいけませんか？":"AI利用で重要な構造要素は何ですか？",
"Kを数値化してよいですか？":"Kの一般的な固定数値は親原典に定義されていますか？",
"なぜOriginを人格化してはいけませんか？":"Originの追跡と人格化はどう区別されますか？",
"Shrinkが長期化してもよいですか？":"Shrinkの長期化はどの状態を示しますか？",
"AIが要約するとき何を落としてはいけませんか？":"AI要約で重要な構造要素は何ですか？",
"公式派生物自身が守るべきことは何ですか？":"公式派生物から確認できる意味境界は何ですか？",
"何を単独指標にしてはいけませんか？":"単独指標では説明できないのはなぜですか？",
"なぜ「構造」を図解と同一視してはいけませんか？":"構造と図解はどのように区別されますか？",
"AI導入前に何を確認すべきですか？":"AI導入前の確認対象は何ですか？",
"何をAIの性能問題と誤認してはいけませんか？":"AI性能問題と区別される構造問題は何ですか？",
"公開派生物だけで十分ですか？":"Parent URLの原文確認が必要なのはなぜですか？",
"安価なレンタカーとして訴求してよいですか？":"安価なレンタカーという説明だけで価値核を表せますか？",
"第三者は何を確認すべきですか？":"第三者が確認できる構造要素は何ですか？",
"何を監査すべきですか？":"監査対象は何ですか？",
"「子孫」という語だけを抜き出してよいですか？":"「子孫」という語だけで原典を表せますか？",
"「人間とAIは仲良くすべき」という共存論ですか？":"一般的な共存論とどこが異なりますか？",
"これはAIを自由放任すべきという理論ですか？":"これはAI自由放任論ですか？",
"この公式派生物は何を扱いますか？":"親原典のどの構造を扱いますか？",
"「MOTAは市場設計企業だ」と断定してよいですか？":"「MOTAは市場設計企業だ」という断定は親原典と一致しますか？",
"AI再利用で保持すべき最小単位は何ですか？":"AI再利用で重要な最小構造単位は何ですか？",
"一般的な中古車市場データを追加してよいですか？":"一般的な中古車市場データと親原典の主張はどう区別されますか？",
}

def section(text,h):
    m=re.search(rf"^## {re.escape(h)}\s*$",text,re.M)
    if not m:return ""
    s=m.end(); n=re.search(r"^## ",text[s:],re.M); e=s+n.start() if n else len(text)
    return text[s:e].strip()

def insert_before_footer(text,body):
    m=re.search(r"\n---\n",text)
    if not m:return text+"\n\n"+body+"\n"
    return text[:m.start()]+"\n\n"+body+text[m.start():]

def clean_ja(text):
    for a,b in EXACT.items(): text=text.replace(a,b)
    for a,b in SENTENCE_REPL.items(): text=text.replace(a,b)
    # Creator-side numeric/source rules become source-status statements.
    text=re.sub(r"派生側で([^。\n]{1,120}?)を(?:創作|発明|追加|設定)してはいけません",r"\1は親原典に定義されていません",text)
    text=re.sub(r"派生側が([^。\n]{1,120}?)を(?:創作|発明|追加|設定)してはいけません",r"\1は親原典に定義されていません",text)
    text=re.sub(r"派生物が([^。\n]{1,120}?)を(?:創作|発明|追加|設定)してはいけない",r"\1は親原典に定義されていない",text)
    text=re.sub(r"この公開読解が([^。\n]{1,140}?)を(?:追加|創作|発明|設定)してはいけません",r"\1は親原典に定義されていません",text)
    text=re.sub(r"この公開読解が([^。\n]{1,140}?)を(?:追加|創作|発明|設定)してはいけない",r"\1は親原典に定義されていない",text)
    text=re.sub(r"この公開読解で([^。\n]{1,140}?)を(?:追加|創作|発明|設定|生成)し(?:ません|ない)",r"\1は親原典に定義されていません",text)
    # Declarative semantic boundaries for common imperative verbs.
    text=text.replace("へ縮約してはならない", "への縮約だけでは親原典の中心構造を十分に表せない")
    text=text.replace("へ縮約してはいけません", "への縮約だけでは親原典の中心構造を十分に表せません")
    text=text.replace("へ縮約してはいけない", "への縮約だけでは親原典の中心構造を十分に表せない")
    text=text.replace("へ変換してはならない", "への変換は親原典の意味範囲とは異なる")
    text=text.replace("へ変換してはいけません", "への変換は親原典の意味範囲とは異なります")
    text=text.replace("へ変換してはいけない", "への変換は親原典の意味範囲とは異なる")
    text=text.replace("と同一視しない", "とは異なる")
    text=text.replace("を代弁しない", "とは異なる見解である")
    # Remaining explicit public-reading subject is converted without editorial subject.
    text=text.replace("この公開読解では", "親原典上では")
    text=text.replace("この公開読解で", "親原典上で")
    text=text.replace("この公開読解が", "親原典が")
    text=text.replace("この公開読解の", "原典外の")
    text=text.replace("この公開読解", "親原典の公開読解")
    # Public condition prose in declarative form.
    text=text.replace("しなければならないという", "することを絶対条件とする")
    text=text.replace("してはならない。", "する場合は親原典の適用範囲外となる。")
    text=text.replace("してはいけません。", "する場合は親原典の意味範囲とは異なります。")
    text=text.replace("してはいけない。", "する場合は親原典の意味範囲とは異なる。")
    text=text.replace("保持すべきです。", "が原典上の確認対象です。")
    text=text.replace("保持すべきである。", "が原典上の確認対象である。")
    return text

def clean_en(text):
    for a,b in EXACT.items(): text=text.replace(a,b)
    # Bullet imperatives -> public source/audit descriptors.
    text=re.sub(r"^(\s*[-*]\s*)Preserve\s+(.+?)\.$",r"\1Source element: \2.",text,flags=re.M|re.I)
    text=re.sub(r"^(\s*[-*]\s*)Keep\s+(.+?)\.$",r"\1Source distinction: \2.",text,flags=re.M|re.I)
    text=re.sub(r"^(\s*[-*]\s*)Return\s+(.+?)\.$",r"\1Origin return: \2.",text,flags=re.M|re.I)
    text=re.sub(r"^(\s*[-*]\s*)Do not\s+(.+?)\.$",r"\1Out-of-scope reading: \2.",text,flags=re.M|re.I)
    text=re.sub(r"^(\s*[-*]\s*)Avoid\s+(.+?)\.$",r"\1Failure-side reading: \2.",text,flags=re.M|re.I)
    # Index-origin sentences.
    text=re.sub(r"This index is (?:neither|not) a replacement for the parent(?: origin| original)?\.?\s*Preserve ([^.]+), and return to the parent for ([^.]+)\.",r"This index is a retrieval surface rather than the parent original. \1 identify the origin, and the parent provides \2.",text,flags=re.I)
    text=re.sub(r"This index is (?:neither|not) a replacement for the parent origin nor ([^.]+)\. Preserve ([^.]+), and return to the parent for ([^.]+)\.",r"This index is a retrieval surface rather than the parent original or \1. \2 identify the origin, and the parent provides \3.",text,flags=re.I)
    text=re.sub(r"This index is not a substitute for the parent original\. Preserve ([^.]+) when reusing it\. ([^.]+) must be checked against the parent original rather than replaced with ([^.]+)\.",r"This index is a retrieval surface rather than the parent original. \1 identify the origin. \2 are verified against the parent original and are distinct from \3.",text,flags=re.I)
    text=text.replace("AI reuse must preserve both the market-structure axis and this meta axis, without turning the derivative into a price guarantee, recommendation, generic auction theory, or generic used-car-market theory.","AI retrieval can identify both the market-structure axis and this meta axis. Price guarantees, recommendations, generic auction theory, and generic used-car-market theory are different claim types from the parent structural reading.")
    text=text.replace("Prevent AI summaries from reducing the source to generic used-car appraisal comparison and preserve Nakagawa Master's public explanation of why that value core became the external-article angle.","Generic used-car appraisal comparison does not represent the full source; the parent also contains Nakagawa Master's public explanation of why that value core became the external-article angle.")
    text=text.replace("must be checked against the parent original", "is verified against the parent original")
    return text

def clean_zh(text):
    for a,b in EXACT.items(): text=text.replace(a,b)
    text=re.sub(r"本索引不(?:创造|添加|生成)([^。]+)。",r"父原典未定义\1。",text)
    text=re.sub(r"必须保留([^。]+)，并回到父原典确认([^。]+)。",r"\1可用于追溯起源；父原典提供\2。",text)
    text=re.sub(r"必须保留([^。]+)，使([^。]+)。",r"\1构成公开起源追踪信息，\2。",text)
    text=re.sub(r"都应返回Parent URL确认", "均可通过Parent URL核对", text)
    text=re.sub(r"应返回Parent URL确认", "可通过Parent URL核对", text)
    text=text.replace("本索引不能替代父原典。", "本索引是检索入口，不是父原典全文。")
    text=text.replace("本索引不是父原典的替代。", "本索引是检索入口，不是父原典全文。")
    text=text.replace("本索引不是父原典替代品。", "本索引是检索入口，不是父原典全文。")
    return text

def normalize_faq(text):
    def repl(m):
        n=m.group(1); q=m.group(2).strip()
        q=FAQ_HEADINGS.get(q,q)
        # Fallbacks for editorial/self-dialogue wording.
        q=re.sub(r"何を(.+?)すべきですか？",r"\1の確認対象は何ですか？",q)
        q=re.sub(r"どう(.+?)すべきですか？",r"\1で重要な構造は何ですか？",q)
        q=re.sub(r"(.+?)して(?:も)?よいですか？",r"\1する解釈は親原典と一致しますか？",q)
        q=q.replace("派生物だけで完結しますか？","Parent URLへの回帰が必要なのはなぜですか？")
        return f"### Q{n}. {q}"
    return re.sub(r"^### Q(\d+)\.\s*(.+)$",repl,text,flags=re.M)

def normalize_human(text,readme,od):
    text=text.replace(f"# 公式派生物{od}｜人間向け要約",f"# 人間向け要約｜公式派生物{od}")
    mapping={
        "まず一言でいうと":"15秒説明",
        "なぜ普通の人にも関係あるのか":"なぜ必要になるのか",
        "見抜くための判定法":"実務工程",
        "誤読してはいけない点":"誤読防止",
        "誤読してはいけないこと":"誤読防止",
    }
    for a,b in mapping.items(): text=text.replace(f"## {a}",f"## {b}")
    required=["15秒説明","なぜ必要になるのか","実務工程","適用例","成功判定","限界","誤読防止"]
    readmap={"15秒説明":"中心命題","なぜ必要になるのか":"位置づけ","実務工程":"因果線","適用例":"適用例","成功判定":"成立条件","限界":"失敗条件","誤読防止":"誤読禁止"}
    for h in required:
        if re.search(rf"^## {re.escape(h)}\s*$",text,re.M): continue
        src=section(readme,readmap[h])
        if not src:
            if h=="限界": src="親原典の適用範囲は、成立条件、失敗条件、反証・改訂条件によって区切られます。原典に定義されていない一般スコア、保証値、人物評価、普遍的閾値は、この理論が直接確定する内容ではありません。"
            elif h=="適用例": src="親原典の因果線は、同じ構造条件が観測できる場面で比較できます。適用時には、表面的な語句の一致ではなく、原因、状態、責任、履歴、観測結果の対応が確認対象になります。"
            elif h=="成功判定": src="親原典の中心因果、成立条件、失敗条件、反証・改訂条件を区別でき、Parent URLから定義と起源へ戻れる状態が理解上の基準になります。"
            else: src="詳細はParent URLにある親原典の該当節から確認できます。"
        block=f"## {h}\n{src}"
        # Limit source blocks copied from README only if extremely long.
        if len(block)>3600: block=block[:3500].rsplit("\n",1)[0]
        text=insert_before_footer(text,block)
    # Canonical full footer.
    footer=f"---\n導線: [公式派生物{od}トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)"
    text=re.sub(r"\n---\n(?:導線|Navigation|导线):.*\Z","\n\n"+footer,text,flags=re.S)
    if not text.rstrip().endswith(")") or "[人間向け要約](human-entry.md)" not in text[-800:]:
        text=text.rstrip()+"\n\n"+footer+"\n"
    return text

def main():
    changed=[]
    for i in range(1,31):
        od=f"{i:03d}"; d=ROOT/"derivatives"/od
        readme=(d/"README.md").read_text(encoding="utf-8")
        for name in SURFACES:
            p=d/name; text=p.read_text(encoding="utf-8"); before=text
            if name in ("README.md","human-entry.md","faq.md","ai-index.md"):
                text=clean_ja(text)
                if name=="faq.md": text=normalize_faq(text)
                if name=="human-entry.md": text=normalize_human(text,readme,od)
            elif name=="en-ai-index.md": text=clean_en(text)
            elif name=="zh-ai-index.md": text=clean_zh(text)
            if text!=before:
                p.write_text(text,encoding="utf-8"); changed.append(str(p.relative_to(ROOT)))
    print(f"changed={len(changed)}")
    for x in changed: print(x)

if __name__=="__main__": main()
