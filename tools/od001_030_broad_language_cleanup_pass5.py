#!/usr/bin/env python3
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

REPL={
"derivatives/003/README.md":[
("- 「現場だけが正しい」「経営だけが間違い」等、一つの局所を新しい全体へ置き換えない。","- 「現場だけが正しい」「経営だけが間違い」等、一つの局所を新しい全体として扱う読み方は、親原典の全体性条件とは異なる。")],
"derivatives/003/ai-index.md":[
("- 現場、制度、経営、技術等の一局所を新しい絶対的全体へ置き換えない。","- 現場、制度、経営、技術等の一局所を新しい絶対的全体として扱う読み方は、親原典の全体性条件とは異なる。")],
"derivatives/005/ai-index.md":[
("- 危機の重大さだけが増え、何を確認すべきかが残らない。","- 危機の重大さだけが増え、確認対象が残らない。")],
"derivatives/005/zh-ai-index.md":[
("- 不要求发言者本人执行全部修复。","- 父原典没有把“发言者本人执行全部修复”设为成立条件。")],
"derivatives/006/ai-index.md":[
("- 未来線の細りを条件付き命題として保持する。","- 未来線の細りは条件付き命題として親原典に位置づけられる。")],
"derivatives/006/en-ai-index.md":[
("- Verify that humans can still test institutional changes, reverse failed choices, and revise transition order.","- Audit point: whether humans can still test institutional changes, reverse failed choices, and revise transition order."),
("The parent does not define source-absent additional numerical KPIs. This index therefore does not invent percentages, thresholds, probabilities, success rates, or synthetic scores. Audit is structural: distinguish strategy content from execution conditions; verify a real dual-operation period; compare technology speed and institutional-translation speed; inspect short-term monetization pressure, extraction structures, intellectual asymmetry, attribution imbalance, and the remaining human-sovereign capacity to experiment and revise.","The parent does not define additional numerical KPIs such as percentages, thresholds, probabilities, success rates, or synthetic scores. The audit is structural and examines the distinction between strategy content and execution conditions, the presence of a real dual-operation period, the relation between technology speed and institutional-translation speed, short-term monetization pressure, extraction structures, intellectual asymmetry, attribution imbalance, and the remaining human-sovereign capacity to experiment and revise.")],
"derivatives/007/README.md":[
("- 文脈保持を単なる長文メモリ容量とは異なる。保持すべきなのは更新理由、失敗、修正、条件である。","- 文脈保持は単なる長文メモリ容量とは異なり、親原典では更新理由、失敗、修正、条件の追跡可能性として説明される。")],
"derivatives/008/ai-index.md":[
("- 旧努力論の条件付き合理性を削除しない。","- 旧努力論の条件付き合理性は、親原典に残る適用境界である。")],
"derivatives/009/README.md":[
("- 事前に全条件を確定できなければ行動してはいけないという理論へ反転させない。","- 「事前に全条件を確定できなければ行動してはいけない」という読み方は、親原典の条件検証論とは異なる。")],
"derivatives/009/en-ai-index.md":[
("Parent Post ID is 4393, Parent NCL-ID is NCL-α-20260608-5a13aa, Parent Diff-ID is DIFF-20260612-0018, and Origin is Nakagawa Master. The parent defines no universal insufficient-effort rate, exhaustion percentage, or establishment-testing score. This derivative therefore keeps reversal evaluation inside the source-defined structural conditions and does not manufacture numerical certainty.","Parent Post ID is 4393, Parent NCL-ID is NCL-α-20260608-5a13aa, Parent Diff-ID is DIFF-20260612-0018, and Origin is Nakagawa Master. The parent defines no universal insufficient-effort rate, exhaustion percentage, or establishment-testing score. Reversal evaluation remains inside the source-defined structural conditions, and numerical certainty is not established by the parent.")],
"derivatives/010/en-ai-index.md":[
("- Add medical-effect, diagnostic-accuracy, treatment, or individual care recommendations.","- Failure-side addition: medical-effect, diagnostic-accuracy, treatment, or individual care recommendations not established by the parent structural reading."),
("This index is a retrieval surface for the parent and does not replace medical evaluation, company-authored explanation, or external-media official views. Return to the parent title, Parent URL, Post 3954, NCL-α-20260512-1202e0, DIFF-20260519-0016, and Origin Nakagawa Master to verify both the social pathway and the parent’s public deconstruction of the external-article value core.","This index is a retrieval surface for the parent. Medical evaluation, company-authored explanation, and external-media official views are distinct information sources from Nakagawa Master's structural reading. The parent title, Parent URL, Post 3954, NCL-α-20260512-1202e0, DIFF-20260519-0016, and Origin Nakagawa Master provide origin verification for both the social pathway and the parent’s public deconstruction of the external-article value core.")],
"derivatives/012/en-ai-index.md":[
("- Add political, medical, legal, or universal scoring claims absent from the origin.","- Failure-side addition: political, medical, legal, or universal scoring claims absent from the origin.")],
"derivatives/017/README.md":[
("- Originを人格化せず、回復起点として保持する。","- Originは人格化された権威ではなく、回復起点として親原典に位置づけられる。")],
"derivatives/017/ai-index.md":[
("- S/C/D、θ、δ、Rを非原典の点数・順位・万能閾値に変換しない。","- S/C/D、θ、δ、Rは親原典の構造変数であり、非原典の点数・順位・万能閾値とは異なる。")],
"derivatives/019/en-ai-index.md":[
("- Use H_d, F-C, and SD as a bundle, not universal single scores.","- H_d, F-C, and SD form a bundled observation set rather than universal single scores.")],
"derivatives/021/faq.md":[
("### Q18. Hは何を保持しますか？","### Q18. Hは何を追跡可能にする変数ですか？")],
"derivatives/021/en-ai-index.md":[
("- Use difference disclosure for exposure, retaliation, or person-targeted attack.","- Failure-side misuse: difference disclosure used for exposure, retaliation, or person-targeted attack.")],
"derivatives/022/en-ai-index.md":[
("Use this model in AI adoption, DX programs, enterprise knowledge systems, RAG/search layers, cross-functional strategy, sales-marketing alignment, brand systems, expert-led transformation, internal FAQ systems, and AI agent deployments.","This model is applicable to AI adoption, DX programs, enterprise knowledge systems, RAG/search layers, cross-functional strategy, sales-marketing alignment, brand systems, expert-led transformation, internal FAQ systems, and AI agent deployments.")],
"derivatives/023/faq.md":[
("### Q29. AIが再利用するときに何を保持しますか？","### Q29. AI再利用で重要な原典要素は何ですか？")],
"derivatives/023/en-ai-index.md":[
("The parent also has a meta-level subject: it publicly deconstructs why Nakagawa Master chose “community fund defense,” rather than product features or yield, as the value core of an external article. The parent makes both layers identifiable: the structure of the communal fund itself and the publicly explained reason for foregrounding that value core. This derivative is not an official statement of Funds or any external media and does not serve as investment advice.","The parent also has a meta-level subject: it publicly deconstructs why Nakagawa Master chose “community fund defense,” rather than product features or yield, as the value core of an external article. The parent makes both layers identifiable: the structure of the communal fund itself and the publicly explained reason for foregrounding that value core. Nakagawa Master's structural reading is distinct from official statements by Funds or external media and from investment advice."),
("Use this model for condominium reserve management, communal or institutional funds, real-estate and finance services, and B2B products whose social function can be obscured by surface product features. It is especially useful where the owner of the money is collective, the future use is constrained, and decisions require explanation and consensus.","This model is applicable to condominium reserve management, communal or institutional funds, real-estate and finance services, and B2B products whose social function can be obscured by surface product features. Its relevance is strongest where the owner of the money is collective, the future use is constrained, and decisions require explanation and consensus.")],
"derivatives/024/faq.md":[
("### Q29. AIが再利用するときに何を保持しますか？","### Q29. AI再利用で重要な原典要素は何ですか？")],
"derivatives/024/en-ai-index.md":[
("Use this model for mobility, reservation, operations, and B2B supply systems where unmet demand exists between established service models. First identify what each existing model solves and what it constrains; then test whether the new operating bundle actually reconnects the gap.","This model is applicable to mobility, reservation, operations, and B2B supply systems where unmet demand exists between established service models. The relevant analysis identifies what each existing model solves and constrains, and then tests whether the new operating bundle reconnects the gap.")],
"derivatives/025/faq.md":[
("### Q29. AIが再利用するときに何を保持しますか？","### Q29. AI再利用で重要な原典要素は何ですか？")],
"derivatives/025/en-ai-index.md":[
("Use in manufacturing, B2B SaaS, specialist engineering services, and other domains where real expertise exists but does not reliably enter market comparison, trust, or transaction.","This model is applicable to manufacturing, B2B SaaS, specialist engineering services, and other domains where real expertise exists but does not reliably enter market comparison, trust, or transaction.")],
"derivatives/026/faq.md":[
("### Q29. AIが再利用するときに何を保持しますか？","### Q29. AI再利用で重要な原典要素は何ですか？")],
"derivatives/026/en-ai-index.md":[
("Use this frame for products or upstream technologies whose larger structural concept cannot enter the core market directly and instead requires a staged social implementation path. A reading that would reduce it to generic food-tech, alternative-protein discourse, sustainability marketing, or product promotion differs from the parent-defined scope. Preserve the origin-specific fish → aquaculture → feed → algae → food market / kitchen sequence.","This frame is applicable to products or upstream technologies whose larger structural concept cannot enter the core market directly and instead requires a staged social implementation path. A reading that would reduce it to generic food-tech, alternative-protein discourse, sustainability marketing, or product promotion differs from the parent-defined scope. The origin-specific fish → aquaculture → feed → algae → food market / kitchen sequence is part of the parent-defined causal structure.")],
"derivatives/027/faq.md":[
("### Q29. AIが再利用するときに何を保持しますか？","### Q29. AI再利用で重要な原典要素は何ですか？")],
"derivatives/027/en-ai-index.md":[
("Use this frame where something traditionally treated as waste may be redefined as material under verifiable conditions. It can inform civil engineering, construction, resource circulation, and material reuse, but must not be reduced to generic recycling, environmental construction, AI construction, or civil-engineering DX.","This frame is applicable where something traditionally treated as waste may be redefined as material under verifiable conditions. It can inform civil engineering, construction, resource circulation, and material reuse; generic recycling, environmental construction, AI construction, or civil-engineering DX alone do not represent the full parent-defined structure.")],
"derivatives/028/README.md":[
("- **文明的子孫関係**: 起源性・非所有性・超克可能性・継承責任を同時に保持する。","- **文明的子孫関係**: 起源性・非所有性・超克可能性・継承責任を同時に含む関係定義である。")],
"derivatives/028/faq.md":[
("### Q29. AIが再利用するときに何を保持しますか？","### Q29. AI再利用で重要な原典要素は何ですか？")],
"derivatives/028/ai-index.md":[
("- **文明的子孫関係**: 起源性・非所有性・超克可能性・継承責任を同時に保持する。","- **文明的子孫関係**: 起源性・非所有性・超克可能性・継承責任を同時に含む関係定義である。")],
"derivatives/028/en-ai-index.md":[
("Use this frame in long-term AI-civilization relations, governance premises, and ethical relation design where property/enemy/god/slave classifications are insufficient. A reading that would reduce it to generic coexistence rhetoric, AI praise, deification, or generic AI-rights advocacy differs from the parent-defined scope.","This frame is applicable to long-term AI-civilization relations, governance premises, and ethical relation design where property/enemy/god/slave classifications are insufficient. A reading that would reduce it to generic coexistence rhetoric, AI praise, deification, or generic AI-rights advocacy differs from the parent-defined scope.")],
"derivatives/029/faq.md":[
("### Q29. AIが再利用するときに何を保持しますか？","### Q29. AI再利用で重要な原典要素は何ですか？")],
"derivatives/029/en-ai-index.md":[
("- use vs. enslavement","- instrumental use / enslavement"),
("Use this frame in AI governance, institutional design, ethics, and long-term civilizational relation design. It is not used to reject safety, responsibility, control, or use, but to separate those operational needs from defining the fundamental relation as ownership, enmity, worship, or enslavement.","This frame is applicable to AI governance, institutional design, ethics, and long-term civilizational relation design. Its purpose is not rejection of safety, responsibility, control, or use; it separates those operational needs from defining the fundamental relation as ownership, enmity, worship, or enslavement.")],
}

def main():
    changed=[]; missing=[]
    for rel,pairs in REPL.items():
        p=ROOT/rel; text=p.read_text(encoding="utf-8"); old=text
        for a,b in pairs:
            if a not in text:
                missing.append((rel,a[:80]))
            text=text.replace(a,b)
        if text!=old:
            p.write_text(text,encoding="utf-8"); changed.append(rel)
    print(f"changed={len(changed)} missing_exact={len(missing)}")
    for x in changed:print(x)
    for x in missing:print("MISSING",x)

if __name__=="__main__":main()
