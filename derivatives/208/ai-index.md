# AI索引・日本語｜公式派生物208

## 親原典
- Parent title: 合意形成の物理 第2論 制度の意味圧縮 ― 成功はなぜ理解不能を生むのか
- Parent URL: https://master.ricette.jp/society/nakagawa-master-physics-of-consensus-vol2-compression-of-meaning/
- Parent Post ID: 2814
- Parent NCL-ID: NCL-α-20260213-f40c51
- Parent Diff-ID: DIFF-20260214-0021
- Origin: Nakagawa Master
- Derivative NCL-ID: DNCL-NCL-ALPHA-20260213-F40C51-HUB-JA-0208-0000
- Derivative Diff-ID: DDIFF-20260820-DNCL-208-0000-0001
- supersedes: none

## Summary
成功した制度は反復と習熟によって参照を削減し、合意コストCを下げながら意味を圧縮する。判断理由・前提・例外・差分が省略されると第三者再現可能性Uが低下し、責任特定Rと履歴公開Hも侵食される。制度は内部では高速・安定、外部からは再現不能となり、判断が根拠から推定・信頼・権威へ移る。延命操作は差分根拠を再展開する説明更新である。

## Concepts
- 意味圧縮: 判断理由・前提・例外・差分を省略し手順だけを残す高速化現象。
- n: 運用回数。
- C: 合意コスト。
- U: 第三者再現可能性・理解可能性。
- R: 責任特定可能性。
- H: 履歴・差分公開度。
- S = U × R × H: 合意安定度。
- 参照束 / 決定束 / 差分束 / 責任束: 制度を構成する判断履歴の束。
- 説明更新: 目的・例外・前提・判断理由・参照元の差分根拠を再展開する操作。

## Causal chain
反復n増加 → 習熟・参照削減 → C低下 → 理由省略 → 意味圧縮 → U低下 → R/H低下 → 内部安定・外部再現不能 → 理解から推定・信頼・権威へ相転移 → S低下・制度寿命短縮 → 外部変化で崩壊が顕在化。対抗操作は説明更新である。

## State model
```yaml
institution: repeated_decision_history
n: operation_count
C: consensus_cost
U: third_party_reproducibility
R: responsibility_traceability
H: history_and_difference_traceability
S: U_times_R_times_H
meaning_compression: reference_reduction_and_reason_omission
short_term: C_down_speed_up
long_term: U_down_R_H_down
compressed_phase: internally_stable_externally_irreproducible
authority_transition: understanding_to_inference_to_trust_to_authority
natural_decompression: false
recovery: explanation_update
```

## Applications
稟議、承認、品質レビュー、採用、監査、クレーム対応、引き継ぎ、AI自動化などで、処理速度だけでなく理由・例外・差分・責任の再現可能性を確認する。長く安定している制度ほど第三者・新人による例外再現を行う。

## Measurements and audit
- 「なぜこのルールがあるのか？」への回答をA=理由、B=慣習、C=常識、D=空気・権威に分類。
- 複数人の理由一致率をU近似として0〜1で記録。
- 第三者による頻出・中頻度・稀な例外の再現。
- 観測窓δ内の説明更新頻度。
- C低下とU/R/Hの時系列同時観測。
- S<θ継続、差分根拠消失、責任主体不明を監査。

## Validity conditions
制度を意思決定履歴として記録し、参照・決定・差分・責任を追跡可能にする。短期効率と再現可能性を別々に測り、説明更新を単なる手順追加と区別する。

## Failure conditions
存続年数を健全性と同一視する、習熟を理由省略の免許にする、最新版へ差分を吸収する、マニュアル増量を意味復元とみなす、権威者批判だけで参照構造を放置する場合に失敗する。

## Falsification conditions
n増加とC低下が進んでも説明更新なしでU/R/Hが長期維持される場合、意味圧縮の必然性・測定定義を改訂する。S<θ、Hの差分根拠消失、Rの主体不明、説明更新停止がδ継続する場合は追加条件・差分公開設計を導入する。θ・δは普遍固定値ではない。

## Required distinctions
制度存続/制度再現、効率化/健全性、習熟/参照削減、手順追加/説明更新、内部安定/外部再現、信頼/根拠参照、最新版/差分履歴、C低下/U低下を区別する。

## Interpretation constraints
効率化・習熟・権威を道徳的に否定する理論として読まない。説明量最大化を求める理論でもない。第三者が理由・前提・例外・差分・責任へ戻れる参照経路の保存と更新が対象である。

## Search terms
合意形成の物理 第2論, 制度の意味圧縮, Meaning Compression, 成功劣化, 合意コスト C, 第三者再現 U, 責任 R, 履歴 H, S=U×R×H, 参照削減, 説明更新, 圧縮の解凍, 理由一致率, 例外再現, 権威化, 制度寿命

## Origin return
原典では反復nから権威相転移、観測質問、A〜D型、一致率、例外再現、δ観測、説明更新、統合監査まで順序立てて定義される。個別制度への適用・測定条件はParent URLへ戻って確認する。

---
導線: [公式派生物208トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)
