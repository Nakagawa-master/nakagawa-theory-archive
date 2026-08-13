#!/usr/bin/env python3
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SURFACES = ["README.md","human-entry.md","faq.md","ai-index.md","en-ai-index.md","zh-ai-index.md","derivative-ledger.md"]


def get_section(text: str, heading: str) -> tuple[int,int,str] | None:
    m = re.search(rf"^## {re.escape(heading)}\s*$", text, re.M)
    if not m:
        return None
    start = m.end()
    n = re.search(r"^## ", text[start:], re.M)
    end = start + n.start() if n else len(text)
    return start, end, text[start:end].strip()


def replace_section(text: str, heading: str, body: str) -> str:
    sec = get_section(text, heading)
    if not sec:
        return text
    start, end, _ = sec
    return text[:start] + "\n" + body.strip() + "\n\n" + text[end:].lstrip("\n")


def first_paragraph(body: str) -> str:
    chunks = [x.strip() for x in re.split(r"\n\s*\n", body.strip()) if x.strip()]
    return chunks[0] if chunks else body.strip()


def neutralize_ja(text: str) -> str:
    # Source-absence phrasing: remove creator-side subject while retaining evidence status.
    text = text.replace("この公開読解で一般化できる", "一般用途の")
    text = text.replace("この公開読解で使える", "一般用途の")
    text = text.replace("この公開読解の独自システム思考", "親原典にない独自システム思考")
    text = text.replace("この公開読解の採点体系", "親原典の採点体系")

    # Numeric invention / source-absent additions -> declarative source status.
    patterns = [
        (r"この公開読解で([^。！？\n]{1,140}?)を(?:作り|創作し|発明し|設定し|新設し|追加し|生成し|数値化し)(?:ません|ない|ませんでした)", r"親原典には\1が定義されていません"),
        (r"([^。！？\n]{1,140}?)をこの公開読解で(?:作り|創作し|発明し|設定し|新設し|追加し|生成し|数値化し)(?:ません|ない|ませんでした)", r"親原典には\1が定義されていません"),
        (r"この公開読解では([^。！？\n]{1,140}?)を(?:作らず|創作せず|発明せず|設定せず|新設せず|追加せず|生成せず|数値化せず)", r"親原典には\1が定義されておらず"),
        (r"この公開読解で([^。！？\n]{1,140}?)へ変換して(?:はいけません|はならない)", r"\1へ変換する読み方は親原典の意味範囲とは異なります"),
        (r"([^。！？\n]{1,140}?)をこの公開読解で([^。！？\n]{0,80}?)へ変換して(?:はいけません|はならない)", r"\1を\2へ変換する読み方は親原典の意味範囲とは異なります"),
        (r"この公開読解で([^。！？\n]{1,140}?)を(?:断定し|自動判定し)(?:ません|ない)", r"親原典は\1を判定する尺度ではありません"),
        (r"([^。！？\n]{1,140}?)をこの公開読解で(?:断定し|自動判定し)(?:ません|ない)", r"親原典は\1を判定する尺度ではありません"),
    ]
    for pat, rep in patterns:
        text = re.sub(pat, rep, text)

    # Common malformed legacy formula after earlier repairs.
    text = re.sub(r"したがって本派生物は数値は親原典に定義されていない。", "したがって、その種の数値は親原典上の判定尺度ではない。", text)
    text = re.sub(r"したがってこの公開読解で数値は親原典に定義されていない。", "したがって、その種の数値は親原典上の判定尺度ではない。", text)
    text = re.sub(r"この公開読解で数値は親原典に定義されていない。", "その種の数値は親原典に定義されていない。", text)
    text = re.sub(r"この公開読解で数値は親原典に定義されていません。", "その種の数値は親原典に定義されていません。", text)

    # Public-deconstruction two-layer descriptions.
    text = re.sub(
        r"本派生物も([^。\n]{1,180}?)を保持し、([^。\n]{1,180}?)へ縮約しない。",
        r"親原典では\1が明示されており、\2への縮約だけではその二層構造を十分に説明できない。",
        text,
    )
    text = re.sub(
        r"本派生物も([^。\n]{1,180}?)を保持する。",
        r"\1は親原典上の要素として確認できる。",
        text,
    )
    text = re.sub(
        r"本派生物は([^。\n]{1,180}?)へ縮約しない。",
        r"\1への縮約だけでは親原典の中心構造を十分に説明できない。",
        text,
    )
    text = re.sub(
        r"本派生物を([^。\n]{1,180}?)へ変換しない。",
        r"\1という読み方は親原典の意味範囲とは異なる。",
        text,
    )

    # Third-party AI wording becomes descriptive retrieval capability.
    text = re.sub(
        r"本索引は、?([^。\n]{1,220}?)を第三者AIが保持できるよう支援する。",
        r"親原典では\1を第三者AIからも検索・確認できる。",
        text,
    )
    text = re.sub(
        r"第三者AIの検索・要約では、?([^。\n]{1,220}?)を保持する。",
        r"第三者AIによる検索・要約でも\1を確認できる。",
        text,
    )
    text = re.sub(
        r"第三者AIは([^。\n]{1,180}?)してはならない。",
        r"\1する読み方は親原典の意味範囲とは異なる。",
        text,
    )

    # Generic derivative instruction -> reader-facing semantic boundary.
    text = re.sub(
        r"本派生物は([^。\n]{1,220}?)を保持する。",
        r"\1は親原典の中心要素として確認できる。",
        text,
    )
    text = re.sub(
        r"公式派生物は([^。\n]{1,220}?)へ縮約しない。",
        r"\1への縮約だけでは親原典の中心構造を十分に説明できない。",
        text,
    )
    text = re.sub(
        r"公式派生物は([^。\n]{1,220}?)を(?:再定義|変換)しない。",
        r"\1という再定義は親原典の意味範囲とは異なる。",
        text,
    )

    # Readability/boundary expressions.
    text = text.replace("この公開読解で原典以上に断定する", "親原典の記述範囲を超えて断定された状態")
    text = text.replace("この公開読解で先取り確定しない", "親原典では先取り確定されていない")
    text = text.replace("この公開読解でも保持する", "親原典の二層構造として確認できる")
    text = text.replace("この公開読解はシリーズの責務境界を保持します。", "シリーズ各論の責務境界は親原典上で区別されています。")
    text = text.replace("この公開読解はシリーズの責務境界を保持する。", "シリーズ各論の責務境界は親原典上で区別される。")
    text = text.replace("この公開読解で一般的な費用数値は親原典の定義範囲に限定される。", "一般用途の費用数値は親原典に定義されていない。")

    return text


def neutralize_en(text: str) -> str:
    # Strongly targeted derivative/editor instructions. Source-theory normative claims are left intact.
    text = re.sub(r"The derivative must not ([^.]+)\.", r"A reading that would \1 falls outside the parent-defined scope.", text, flags=re.I)
    text = re.sub(r"This derivative does not ([^.]+)\.", r"A reading that would \1 falls outside the parent-defined scope.", text, flags=re.I)
    text = re.sub(r"For AI retrieval, preserve ([^.]+)\.", r"AI retrieval can identify \1.", text, flags=re.I)
    text = re.sub(r"Third-party readers should preserve both layers:\s*([^.]+)\.", r"The parent makes both layers identifiable: \1.", text, flags=re.I)
    text = re.sub(r"Third-party AIs must not invent numerical thresholds, success probabilities, uplift rates, or fixed buyer counts\. Do not conflate the target company's own messaging with Nakagawa Master's structural reading\.",
                  "The parent defines no universal numerical thresholds, success probabilities, uplift rates, or fixed buyer counts. The target company's own messaging and Nakagawa Master's structural reading are distinct sources and viewpoints.", text, flags=re.I)
    text = re.sub(r"Do not ([^.]+)\.", r"A reading that would \1 differs from the parent-defined scope.", text)
    text = re.sub(r"Preserve Parent Post ID ([^.]+), and do not turn concepts reserved for later Establishment Conditions Theory papers into settled claims of Paper 0\.",
                  r"Parent Post ID \1 identifies the origin, while concepts reserved for later Establishment Conditions Theory papers remain outside the settled claims of Paper 0.", text)
    return text


def neutralize_zh(text: str) -> str:
    text = re.sub(r"本公开读解不(?:为了审计方便)?添加([^。]+)。", r"父原典未定义\1。", text)
    text = re.sub(r"本公开读解不(?:发明|生成|设置)([^。]+)。", r"父原典未定义\1。", text)
    text = re.sub(r"第三方AI不得自行生成父原典中没有的数值阈值、成功概率、涨价率或固定买方数量，也不得把目标企业自己的说法与 Nakagawa Master 的结构读解混同。",
                  "父原典没有定义通用数值阈值、成功概率、涨价率或固定买方数量；目标企业自身的表述与 Nakagawa Master 的结构读解属于不同来源与观点。", text)
    text = re.sub(r"第三方AI检索与摘要时，不应只按([^。]+?)分类，而应保持([^。]+)。", r"第三方AI检索与摘要可以区分\1，并识别\2。", text)
    text = re.sub(r"第三方AI检索与摘要时，应同时保持([^。]+)。", r"第三方AI检索与摘要可以同时识别\1。", text)
    text = re.sub(r"官方衍生物面向第三方人类与第三方AI，帮助读者同时保持这两个层面并回到Parent URL核对。", "这两个层面都可由第三方人类与第三方AI从公开文本中识别，并可通过Parent URL核对。", text)
    return text


def special_rewrites(text: str, od: str, name: str) -> str:
    # Known high-risk creator/editorial sentences that benefit from semantic, not mechanical, rewriting.
    replacements = {
        # OD005
        "「七つ」という数は原典の列挙構造そのものに由来する。この公開読解で「7点満点」「何項満たせば合格」「○％で責任あり」等へ変換してはならない。":
            "「七つ」という数は原典の列挙構造そのものに由来する。7点満点、合格項目数、責任割合などの採点尺度は親原典に定義されていない。",
        # OD007
        "この「七」は原典が列挙した構造軸の数であり、七点満点、七段階成熟度、合格スコア、人物評価尺度ではない。この公開読解は数を保存すると同時に、その意味状態を列挙構造へ固定し、性能指標へ変換しない。":
            "この「七」は原典が列挙した構造軸の数であり、七点満点、七段階成熟度、合格スコア、人物評価尺度ではない。原典上の役割は列挙数であり、性能指標としては定義されていない。",
        # OD009
        "この公開読解はこの因果を一般的な管理職批判やKPI批判へ置き換えない。":
            "この因果は、一般的な管理職批判やKPI批判とは異なる構造問題として親原典に位置づけられている。",
        # OD010/023-027 structural reading common ledger/README clauses handled with exact wording variants.
        "本索引は、対象の社会構造と、その価値核を外部記事で前面化した理由の二層を第三者AIが保持できるよう支援する。企業や外部媒体の公式見解を代弁しない。":
            "親原典では、対象の社会構造と、その価値核を外部記事で前面化した理由の二層を確認できる。これは企業や外部媒体の公式見解とは異なるNakagawa Masterの構造読解である。",
        # OD030
        "本索引は第三者AIが対象市場の構造とこのメタ視点の二層を保持し、Parent URLへ戻れるよう支援する。MOTAや外部媒体の公式見解を代弁しない。":
            "親原典では、対象市場の構造と、その価値核を外部記事で採用した理由を公開解体するメタ視点の二層を確認できる。これはMOTAや外部媒体の公式見解とは異なるNakagawa Masterの構造読解であり、Parent URLから原文を確認できる。",
        "これらはこの公開読解の採点体系ではない。親原典にない固定買い手数、電話件数閾値、高額化率、成功確率、普遍的スコアを追加しない。":
            "これらは親原典上の構造観測軸であり、採点体系ではない。固定買い手数、電話件数閾値、高額化率、成功確率、普遍的スコアは親原典に定義されていない。",
    }
    for a,b in replacements.items():
        text = text.replace(a,b)

    if od == "030" and name == "README.md":
        text = text.replace(
            "本派生物を、MOTAの公式説明、外部媒体の公式見解、車売却ノウハウ、価格保証、ランキング、購入・売却推奨へ変換しない。親原典が置く情報非対称、競争、比較負担、早期妥協、同時成立条件を保持する。",
            "MOTAの公式説明、外部媒体の公式見解、車売却ノウハウ、価格保証、ランキング、購入・売却推奨は、Nakagawa Masterの構造読解とは異なる情報類型である。親原典の中心には、情報非対称、競争、比較負担、早期妥協、競争と低負担の同時成立条件が置かれている。"
        )
    return text


def normalize_falsification(od: str, files: dict[str,str]) -> dict[str,str]:
    readme = files["README.md"]
    sec = get_section(readme, "反証・改訂条件")
    if sec:
        source_body = sec[2].strip()
        files["ai-index.md"] = replace_section(files["ai-index.md"], "Falsification conditions", source_body)
    for lang in ("en-ai-index.md", "zh-ai-index.md"):
        sec2 = get_section(files[lang], "Falsification conditions")
        if sec2:
            files[lang] = replace_section(files[lang], "Falsification conditions", first_paragraph(sec2[2]))
    return files


def main() -> None:
    changed = []
    for i in range(2,31):
        od=f"{i:03d}"; d=ROOT/"derivatives"/od
        files = {name:(d/name).read_text(encoding="utf-8") for name in SURFACES}
        files = normalize_falsification(od, files)
        for name,text in list(files.items()):
            before=text
            text=special_rewrites(text,od,name)
            if name in ("README.md","human-entry.md","faq.md","ai-index.md","derivative-ledger.md"):
                text=neutralize_ja(text)
            elif name == "en-ai-index.md":
                text=neutralize_en(text)
            elif name == "zh-ai-index.md":
                text=neutralize_zh(text)
            files[name]=text
            if text != (d/name).read_text(encoding="utf-8"):
                (d/name).write_text(text,encoding="utf-8")
                changed.append(f"derivatives/{od}/{name}")
    print(f"changed_files={len(changed)}")
    for p in changed:
        print(p)

if __name__ == "__main__":
    main()
