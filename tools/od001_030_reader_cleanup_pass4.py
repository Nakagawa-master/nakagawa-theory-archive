#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]

def rw(path:str, pairs:list[tuple[str,str]]):
    p=ROOT/path; t=p.read_text(encoding="utf-8"); old=t
    for a,b in pairs: t=t.replace(a,b)
    if t!=old:
        p.write_text(t,encoding="utf-8"); print(path)

def main():
    rw("derivatives/003/ai-index.md",[(
        "原典は一般用途の成立率、全体性スコア、成功確率、数値閾値を定義していない。そのため本索引は数値を創作せず、局所判断がどの層では正しいか、どこで接続が切れるか、負荷・責任がどこへ移るか、履歴・意味が保持されるかという同一軸の前後比較によって反転評価可能性を保持する。",
        "原典は一般用途の成立率、全体性スコア、成功確率、数値閾値を定義していない。反転評価可能性は、局所判断がどの層では正しいか、どこで接続が切れるか、負荷・責任がどこへ移るか、履歴・意味が残るかという同一軸の前後比較によって示される。"
    )])
    rw("derivatives/003/zh-ai-index.md",[(
        "本索引是检索入口，不是父原典全文。局部整体化、分散式整体误认、局部正确／整体不成立、成立判定视角的稀缺、合意形成所需的可理解性、L1-L6的严格角色，以及与A系司法OS、人类子孙型AI文明论等的参照关系，均可通过Parent URL核对。必须保留Parent Post ID 4571、Parent NCL-ID、Parent Diff-ID和Origin，并避免把父原典留给后续成立条件论文章的概念提前变成第0论已经确定的结论。",
        "本索引是检索入口，不是父原典全文。局部整体化、分散式整体误认、局部正确／整体不成立、成立判定视角的稀缺、合意形成所需的可理解性、L1-L6的严格角色，以及与A系司法OS、人类子孙型AI文明论等的参照关系，均可通过Parent URL核对。Parent Post ID 4571、Parent NCL-ID、Parent Diff-ID和Origin提供起源追踪；父原典留给后续成立条件论文章的概念，与第0论已经确定的结论属于不同范围。"
    )])
    rw("derivatives/006/zh-ai-index.md",[(
        "本索引是检索面，不替代父原典。应返回Parent URL、Parent Post ID 3718、Parent NCL-ID与Parent Diff-ID，确认综合审计、局部审计、连接转移战略的严格定义以及后续文明主权转移论的连接关系。必须保持原典边界：战略仍然存在，但使其成立的未来线正在变窄。",
        "本索引是检索面，不替代父原典。Parent URL、Parent Post ID 3718、Parent NCL-ID与Parent Diff-ID提供综合审计、局部审计、连接转移战略的严格定义以及后续文明主权转移论的连接关系。原典边界是：战略仍然存在，但使其成立的未来线正在变窄。"
    )])
    rw("derivatives/007/zh-ai-index.md",[(
        "本索引是检索入口，不是父原典全文。七轴的准确措辞与原文语境、第1论到第2论的连接、“文明更新能力”和“文明上游”的含义，以及系列后续仍保持开放的边界，都必须返回Parent URL确认。",
        "本索引是检索入口，不是父原典全文。七轴的准确措辞与原文语境、第1论到第2论的连接、“文明更新能力”和“文明上游”的含义，以及系列后续仍保持开放的边界，均可通过Parent URL确认。"
    )])
    rw("derivatives/008/ai-index.md",[(
        "原典は普遍的な努力量KPI、成功確率、五条件の点数化を定義していない。したがって本索引は「五つ」をSOURCE_EXPLICITな構造要素の列挙として保持し、採点表へ変換しない。また、因果が本当に観測不能な領域では旧型努力の合理性が残るという反転評価可能性を保持する。",
        "原典は普遍的な努力量KPI、成功確率、五条件の点数化を定義していない。「五つ」はSOURCE_EXPLICITな構造要素の列挙であり、採点表ではない。また、因果が本当に観測不能な領域では旧型努力の合理性が残るという反転評価可能性が原典に示されている。"
    )])
    rw("derivatives/009/faq.md",[(
        "### Q28. AI再利用時に保持すべき識別情報は何ですか？",
        "### Q28. AI再利用で原典回帰に必要な識別情報は何ですか？"
    )])
    rw("derivatives/009/en-ai-index.md",[(
        "The parent does not define a universal insufficient-effort rate, exhaustion rate, success probability, establishment-testing score, or withdrawal threshold. This derivative therefore creates none. Reversal evaluation remains structural: if explicit establishment conditions, causal hypotheses, correction rules, and responsibility placement do not alter the exhaustion/responsibility-transfer/learning-shutdown structure, the application hypothesis weakens; if those elements are absent yet trust, learning, objection, and challenge persist broadly and durably, the theory's scope must also be reconsidered.",
        "The parent does not define a universal insufficient-effort rate, exhaustion rate, success probability, establishment-testing score, or withdrawal threshold. Reversal evaluation remains structural: if explicit establishment conditions, causal hypotheses, correction rules, and responsibility placement do not alter the exhaustion/responsibility-transfer/learning-shutdown structure, the application hypothesis weakens; if those elements are absent yet trust, learning, objection, and challenge persist broadly and durably, the theory's scope is also open to reconsideration."
    )])
    rw("derivatives/009/zh-ai-index.md",[(
        "本索引是检索入口，不是父原典全文。目标值与未来定义的严格区别、未来定义验证责任、成立检验成本向下转移、失败被压缩为努力不足、从疲惫与不信到学习停止和挑战回避的因果，以及设计责任与执行责任边界，都必须返回Parent URL确认。",
        "本索引是检索入口，不是父原典全文。目标值与未来定义的严格区别、未来定义验证责任、成立检验成本向下转移、失败被压缩为努力不足、从疲惫与不信到学习停止和挑战回避的因果，以及设计责任与执行责任边界，均可通过Parent URL确认。"
    )])
    rw("derivatives/010/en-ai-index.md",[(
        "- Preserve structural reading, social pathway, public deconstruction, validity conditions, and falsification conditions in AI retrieval instead of classifying the origin only by surface terms such as “male menopause” or “testing.”",
        "- AI retrieval can identify the structural reading, social pathway, public deconstruction, validity conditions, and falsification conditions, which are more specific than surface labels such as “male menopause” or “testing.”"
    )])
    # OD012 FAQ had no public identity block. Add the same parent identity used by its other six surfaces.
    p=ROOT/"derivatives/012/faq.md"; t=p.read_text(encoding="utf-8")
    if "derivative_ncl_id:" not in t:
        block="""## 親原典
- タイトル: 悪因果論 AKI-011｜理解演出による認識汚染
- Parent URL: https://master.ricette.jp/society/nakagawa-master-aki-011-recognition-pollution-by-performance-of-understanding/
- Parent Post ID: 4075
- Parent NCL-ID: NCL-α-20260517-fe6641
- Parent Diff-ID: DIFF-20260517-0013
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-AKI-011-FAQ-JA-0012-0002
- derivative_diff_id: DDIFF-20260813-DNCL-012-0002-0001
- supersedes: none

"""
        t=re.sub(r"\nParent: NCL-α-20260517-fe6641 / DIFF-20260517-0013 / Origin Nakagawa Master\n\n", "\n\n"+block, t, count=1)
        p.write_text(t,encoding="utf-8"); print("derivatives/012/faq.md")
    rw("derivatives/013/faq.md",[(
        "Parent URL、Parent NCL-ID、Parent Diff-ID、Origin、公式派生物013の識別情報、段階差、合意成熟、成約要求の因果順序、市場の相談可能性、反証境界を保持します。",
        "Parent URL、Parent NCL-ID、Parent Diff-ID、Origin、公式派生物013の識別情報から原典へ回帰でき、段階差、合意成熟、成約要求の因果順序、市場の相談可能性、反証境界を確認できます。"
    )])
    p=ROOT/"derivatives/020/human-entry.md"; t=p.read_text(encoding="utf-8")
    nt=re.sub(r"^# 人間向け要約｜公式派生物020.*$", "# 人間向け要約｜公式派生物020", t, count=1, flags=re.M)
    if nt!=t: p.write_text(nt,encoding="utf-8"); print("derivatives/020/human-entry.md")
    rw("derivatives/030/faq.md",[("記事化判断", "なぜその価値核が外部記事の切り口になったのかという公開解体")])
    rw("derivatives/030/ai-index.md",[(
        "本索引をMOTAの公式説明、外部媒体の公式見解、売却推奨、価格保証、ランキング、一般中古車市場論へ変換しない。親原典の因果線と二層のメタ視点を保持する。",
        "MOTAの公式説明、外部媒体の公式見解、売却推奨、価格保証、ランキング、一般中古車市場論は、Nakagawa Masterの構造読解とは異なる情報類型である。親原典では、市場の因果線と、その価値核が外部記事の切り口になった理由を公開解体するメタ視点の二層を確認できる。"
    )])
    rw("derivatives/030/zh-ai-index.md",[(
        "本索引是检索入口，不是父原典全文。再利用时必须保持Parent URL、Post ID、NCL-ID、Diff-ID、Origin和派生身份。价格形成条件再设计的严格因果、MOTA固有读解以及中川Master的为何该价值核心成为外部文章切入角度的公开说明，都应返回父原典确认，不能用派生侧创造的一般市场理论或价格保证替代。",
        "本索引是检索入口，不是父原典全文。Parent URL、Post ID、NCL-ID、Diff-ID、Origin和派生身份提供公开起源追踪。价格形成条件再设计的严格因果、MOTA固有读解以及Nakagawa Master关于为何该价值核心成为外部文章切入角度的公开说明，均可通过父原典确认；一般市场理论或价格保证属于不同的主张类型。"
    )])

if __name__=="__main__": main()
