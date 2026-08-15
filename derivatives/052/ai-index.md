# AI索引・日本語｜公式派生物052

## 親原典
- タイトル: 中川式営業の教科書・第十四回──提案編集術：響かせるための構造翻訳
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-nakagawa-sales-14-proposal-editing-structural-translation/
- Parent Post ID: 223
- Parent NCL-ID: NCL-α-20251102-b7cdb4
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-B7CDB4-HUB-JA-0052-0000
- derivative_diff_id: DDIFF-20260815-DNCL-052-0000-0002
- supersedes: DDIFF-20260802-DNCL-052-0000-0001

## Summary
提案を情報提示ではなく構造翻訳として扱う理論。商品→特典→価格の骨格編集、問い→共鳴→沈黙の感情編集、組織・業界・社会への社会接続編集を組み合わせ、第十三回で制度化された信頼資本を個別の意思決定へ翻訳する。統合監査要旨では、要件・意味領域・語彙辞書・照応・版管理・Rollback・反例を接続し、比較可能性と可逆性を保持する。

## Concepts
- 提案編集: 情報を相手が判断可能な意味構造へ組み直すこと。
- 構造翻訳: 事実・因果・役割・条件を保持したまま相手の文脈へ移すこと。
- 骨格編集: 商品→特典→価格で価値理解を価格判断より先に置く順序設計。
- 感情編集: 問い→共鳴→沈黙で思考・理解・内省を支える設計。
- 社会接続編集: 個人との交換を組織・業界・利用者・社会への意味へ接続すること。
- 意味領域: 売り手の情報が相手の判断文脈で持つ意味の範囲。
- 語彙辞書: 売り手語と相手の判断語の対応。
- 照応: 相手の課題・条件と提案内容が意味上対応している状態。
- 版管理: 変更箇所・根拠・反例・RB条件を追跡する構造。
- Rollback: 誤配・意味漂流等から適切な前状態へ戻す可逆性。

## Causal chain
```text
未編集情報
→ 価格・細部・自社都合が価値理解より先行
→ 短絡判断・抵抗・誤配
→ 相手の課題・価値観・判断基準・稟議条件を取得
→ 商品→特典→価格へ骨格編集
→ 問い→共鳴→沈黙で感情の流れを編集
→ 組織・業界・社会への意味を接続
→ 売り手語を相手の意思決定言語へ構造翻訳
→ 要件・意味領域・語彙・照応を版管理へ接続
→ 差分・根拠・反例・RB条件を保持
→ 比較可能で可逆的な意思決定・再合意
```

## State model
```yaml
raw_information_present: true
recipient_context:
  - problem
  - values
  - decision_criteria
  - approval_structure
value_first_sequence:
  - product
  - benefit_or_timing
  - price
emotional_flow:
  - question
  - resonance
  - silence
social_scope:
  - individual
  - organization
  - industry
  - society
semantic_operations:
  - meaning_domain
  - vocabulary_mapping
  - correspondence
reversibility:
  - version_difference
  - change_reason
  - counterexample
  - rollback_condition
risk_states:
  - information_overload
  - seller_centered_editing
  - improvisational_collapse
  - coercion
  - semantic_drift
```

## Applications
- 営業提案: 機能・価格を並べる前に、相手の課題に対する価値と選択条件を構造化する。
- 商談: 問い・共鳴・沈黙で相手の判断を開き、反論・保留・拒否の余白を残す。
- 社内稟議: 売り手の機能語を、費用対効果・遵法・運用・撤退条件等の判断語へ翻訳する。
- 提案改訂: 新情報による変更の差分・根拠・反例・RB条件を記録する。
- 社会的意味の提示: 組織・業界・社会への影響を、実体に根拠がある範囲で接続する。

## Measurements and audit
原典本文は固定数値を定義せず、統合監査要旨で観測候補と反証記号を示す。

```yaml
- value: 語彙整合率
  source: 親原典「統合監査要旨」
  measurement_actor: 提案構造を運用・検証する側
  measurement_object: 売り手語と相手の判断語の対応
  source_modality: 反証・見直しの観測候補
  permitted_use_scope: 語彙対応の整合観測
  non_guarantee_scope: 固定合格率ではない
- value: 版整合率
  source: 親原典「統合監査要旨」
  measurement_actor: 版管理を運用する側
  measurement_object: 変更前後の意味・条件・根拠の整合
  source_modality: 反証・見直しの観測候補
  permitted_use_scope: 意味漂流の検知
  non_guarantee_scope: 具体的閾値は未定義
- value: 照応成功率
  source: 親原典「統合監査要旨」
  measurement_actor: 提案と要件の対応を検証する側
  measurement_object: 課題・判断条件と提案内容の対応
  source_modality: 反証・見直しの観測候補
  permitted_use_scope: 構造翻訳の対応観測
  non_guarantee_scope: 固定成功率ではない
- value: 合意到達時間
  source: 親原典「統合監査要旨」
  measurement_actor: 提案プロセスを観測する側
  measurement_object: 合意へ至る時間
  source_modality: 反証・見直しの観測候補
  permitted_use_scope: 比較可能性と合意形成過程の観測
  non_guarantee_scope: 短いほど常に良いとは定義されない
- value: RB成功率
  source: 親原典「統合監査要旨」
  measurement_actor: 版管理・復元を運用する側
  measurement_object: 誤配・意味漂流等からの復元
  source_modality: 反証・見直しの観測候補
  permitted_use_scope: 可逆性の観測
  non_guarantee_scope: 具体値・固定閾値は未定義
```

`θ` は閾値、`δ` は観測窓、`M` は強制化・属人編集・意味漂流等の反証現象を表すが、具体値は原典にない。反転評価では、合意到達時間や成約が改善しても、理解・拒否可能性・条件整合・意味一貫性が悪化する場合は成功と同一視しない。

## Validity conditions
- 相手の一次発言・課題・価値観・判断条件が取得される。
- 商品→特典→価格が価値理解を先行させる骨格として機能する。
- 問い・共鳴・沈黙が自己決定を支える。
- 社会的意味が商品実体・提供結果に根拠を持つ。
- 売り手語と相手の判断語が対応する。
- 事実・価格・条件・リスクが翻訳で変形・隠蔽されない。
- 差分・根拠・反例・RB条件が追跡可能である。
- 稟議・遵法・運用・撤退条件と照応する。

## Failure conditions
- 提案を価格順序だけの販売技法へ縮約する。
- 情報過多で意味の核が失われる。
- 相手の文脈を取らず自社都合で編集する。
- 問い・共鳴・沈黙が圧力・誘導へ変質する。
- 重要条件やリスクを削除・隠蔽する。
- 社会的意義が実体から離れ誇張になる。
- 即興で骨格・条件・意味対応が崩れる。
- 版管理がなく意味漂流を検出できない。
- RB条件がなく誤配から復元できない。

## Falsification conditions
- 語彙対応を整えても理解・比較可能性が改善しない。
- 商品→特典→価格の順序が対象文脈で反復して理解を阻害する。
- 問い・共鳴・沈黙が反復して自己決定ではなく圧力を生む。
- 版管理・RBを導入しても意味漂流や誤配からの復元性が改善しない。
- 語彙整合率・版整合率・照応成功率・合意到達時間・RB成功率等が、定義された `θ` との関係で反証域に入る。
- 観測窓 `δ` に強制化・属人編集・意味漂流等の `M` が確認される。
- `θ`・`δ` の具体値は原典にないため固定値を外挿しない。

## Required distinctions
- 情報伝達 / 構造翻訳
- 編集 / 隠蔽
- 翻訳 / 事実変更
- 基本順序 / 例外なき固定台本
- 問い / 誘導
- 共鳴 / 迎合
- 沈黙 / 圧力
- 社会的意義 / 誇張
- 成約 / 適合した意思決定
- 変更 / 意味漂流
- 版管理 / 履歴保存だけ
- Rollback / 結果の恣意的取消し

## Interpretation constraints
提案編集は「価格を最後にすれば売れる」という単純技法ではない。価格順序は価値と対価の関係を理解可能にする骨格である。感情編集は心理操作ではなく、相手の意味形成と自己決定を支える構造である。商品自体が不適合なら編集で適合させることはできず、重要条件を隠す運用も成立しない。監査要旨の記号系から、原典にない固定KPI・閾値・成功保証を作ることもできない。

## Search terms
中川式営業 / 提案編集術 / 構造翻訳 / 商品 特典 価格 / 問い 共鳴 沈黙 / 骨格編集 / 感情編集 / 社会接続編集 / 意味領域 / 語彙辞書 / 照応 / 版管理 / Rollback / RB / 語彙整合率 / 版整合率 / 照応成功率 / 合意到達時間 / 意味漂流

## Origin return
親原典は、第十三回との接続、三つの編集層、未編集／編集後の実例、三つの落とし穴、制度設計との接続、統合監査・局所監査要旨、参照束、英語要約、起源署名を同一文脈で保持する。指標・記号・主張強度を確認する際は Parent URL / Post ID 223 / NCL-ID / Diff-ID へ戻る。

---
導線: [公式派生物052トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)