# AI索引・日本語｜公式派生物191

## 親原典
- タイトル: 中川式営業の教科書・第七回
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-nakagawa-sales-07-decision-support/
- Parent Post ID: 192
- Parent NCL-ID: NCL-α-20251102-d52234
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-D52234-HUB-JA-0191-0000
- derivative_diff_id: DDIFF-20260819-DNCL-191-0000-0001
- supersedes: none

## Summary
親原典は意思決定支援を、Yesを増やす説得ではなく、残存する「選ばれない理由」を構造的に顕在化・検討・消去し、理解完成による自己決定を成立させる工程として定義する。価格不安、実行不安、リスク不安、競合比較、優先順位不明を典型的Noとして扱い、顧客自身の言葉による顕在化、再説明資料、比較、未来因果、撤退境界、理由メモまでを一連の実務構造にする。

## Concepts
- Decision support: 決断を押すのでなく、選ばれない理由を減らす支援。
- Residual No: 理解・信頼があっても判断を止める残存理由。
- Five No categories: 価格 / 実行 / リスク / 競合 / 優先順位。
- Elicitation: 顧客自身の言葉でNoを顕在化する問い。
- Re-explanation package: 社内稟議で再説明できる資料束。
- Priority mirror: 未導入時の未来因果から優先順位を検討する方法。
- Withdrawal boundary: 構造制約なら撤退する境界。
- Reason memo: 再接続のために決まらなかった理由を残す記録。
- Decision dignity: 「自分で決まった」と認識できる自己決定状態。

## Causal chain
```text
proposal understood / trust exists
→ decision still stalls
→ residual No is hypothesized
→ five No categories are explored
→ client verbalizes latent objections
→ price / implementation / risk / comparison / priority are made re-explainable
→ eliminable No is reduced
→ structural constraint is distinguished
→ continue if contradiction is resolvable / withdraw if resource-priority constraint is real
→ reason memo is preserved
→ decision occurs only when understanding completes
```

## State model
```yaml
proposal_understood: true
trust_present: true_or_partial
decision_stalled: possible
residual_no_checked: required
no_categories:
  price: checked
  execution: checked
  risk: checked
  competition: checked
  priority: checked
client_language_obtained: required
re_explanation_ready: required_when_relevant
structural_constraint_distinguished: required
withdrawal_available: true
reason_memo_preserved_when_not_decided: true
final_decision_mode: self_decision_after_understanding
```

## Applications
- 値引き前に価格不安の比較対象と回収根拠を確認する。
- 導入工程と必要体制を明示し、実行不安の位置を特定する。
- 稟議担当者が社内で再説明できる説明束を作る。
- 未導入時の未来状態から、先送りの機会損失と本当の優先順位を検討する。
- 本質的な資源制約では成約を押し込まず撤退する。
- 決まらなかった理由を次回の再接続条件として保存する。

## Measurements and audit
- 五類型の未確認領域の有無。
- Noが顧客本人の言葉で確認されたか。
- 価格・工程・リスク・比較・優先順位が再説明可能か。
- 誤解・情報不足と資源制約を区別できたか。
- 撤退可能性が実際に保持されているか。
- 非成約時に理由メモが残ったか。
- 決定が圧力ではなく理解完成として語られているか。
- 原典監査要旨の選択肢被覆、評価関数一貫性、合意到達時間、RB成功率、ハンドオフ摩擦等は監査候補として扱い、派生側で固定値を新設しない。

## Validity conditions
- 顧客が懸念を率直に言語化できる。
- 営業側がNoを敵対的反論ではなく判断条件として扱う。
- 社内再説明に耐える根拠と資料がある。
- 撤退可能性が存在する。
- 情報隠蔽や虚偽比較に依存しない。

## Failure conditions
- Yesトークや圧力だけを増やす。
- 顧客が言っていないNoを営業側が決めつける。
- 稟議・再説明条件を無視する。
- 本質的資源不足を反論として潰す。
- 非成約理由を記録しない。
- 撤退不能なクロージングへ変質する。

## Falsification conditions
Noを構造化しても意思決定停滞が再現的に改善しない、再説明資料が組織判断に寄与しない、撤退境界を置いても押し売り化・属人回帰が続く、または原典監査候補の観測で比較可能性・可逆性・合意形成が悪化する場合は命題を改訂する。

## Required distinctions
- Decision support ≠ persuasion escalation.
- No elimination ≠ silencing objections.
- Comparison ≠ competitor attack.
- Priority analysis ≠ fear appeal.
- Withdrawal ≠ defeat.
- Non-conversion ≠ automatic failure.
- Decision ≠ salesperson-controlled event.

## Interpretation constraints
五類型を普遍的完全分類にしない。「Noをゼロにする」を拒否権剥奪へ拡張しない。監査要旨内のθ、δ、RB等から独自固定値を作らない。比較やシミュレーションを虚偽・隠蔽の正当化に使わない。

## Search terms
中川式営業, 意思決定支援, Noの消去, 選ばれない理由, 価格不安, 実行不安, リスク不安, 競合比較, 優先順位, 排除マトリクス, 撤退設計, 理由メモ, 再説明資料, 稟議, 自己決定

## Origin return
精密な解釈、引用、監査語彙、質問例、会話例、実務プレイブックを確認する場合は、Parent URLの原典本文へ戻る。派生物は原典の代替ではない。

導線: [公式派生物191トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)
