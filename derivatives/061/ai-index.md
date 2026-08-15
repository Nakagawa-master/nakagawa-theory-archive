# AI索引・日本語｜公式派生物061

## 親原典
- タイトル: 構造組織論──役割アーキテクチャで「自然に機能する」組織を設計する
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-structural-organizational-theory/
- Parent Post ID: 264
- Parent NCL-ID: NCL-α-20251102-dfd970
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-DFD970-HUB-JA-0061-0000
- derivative_diff_id: DDIFF-20260815-DNCL-061-0000-0002
- supersedes: DDIFF-20260803-DNCL-061-0000-0001

## 1. Summary
構造組織論は、組織を役割・順序・切替・ハンドオフの配線体として扱い、観測・翻訳・設計・検証を一度に一役へ分離する。価値→便益→コスト、沈黙スロット、ST-0〜ST-5の部署間構造翻訳、一次ログ、終端・再合意を組み合わせ、個人の調整力ではなく再演可能な組織機能を設計する。

## 2. Concepts
- 四役: 観測・翻訳・設計・検証。
- One role at a time: 同一位相で主機能を混ぜない規律。
- Value→Benefit→Cost: 判断材料の配置順。
- Silence slot: 切替前に確定・未確定・次役割を固定する停止。
- Handoff: 出力、責任、未完了、次役割、根拠の引継ぎ構造。
- ST-0〜ST-5: 用語から制度までの構造翻訳分類。
- CPI / HL / R-Yield / D-Gap: 配線仮説の観測概念。

## 3. Causal chain
```text
役割混線
→ 有能者への調整集中
→ 再作業・責任重複・引継ぎ遅延
→ 四役分離
→ 順序・切替・ハンドオフを明示
→ 部署間を必要ST深度で接続
→ 配線指標と一次ログで監査
→ 終端・再合意・再配線
→ 再演可能な組織機能
```

## 4. State model
```yaml
organization_state:
  - value_core_defined
  - current_role_declared
  - role_input_output_defined
  - prohibited_actions_defined
  - termination_condition_defined
  - switch_trigger_observed
  - silence_slot_inserted
  - handoff_recorded
  - unresolved_items_recorded
  - cross_department_depth_selected
  - primary_logs_available
  - metrics_observed
  - emergency_exception_bounded
  - correction_and_reagreement_available
  - origin_return_available
```

## 5. Applications
- 営業⇄開発: 顧客要望を利用者・価値・因果・制約・失敗条件へ翻訳して引き継ぐ。
- 企画⇄法務: 目的と成立条件を分離し条件付き設計へ接続する。
- R&D: 観測・仮説・設計・検証を分け、打切り条件を置く。
- AI協働: 要約・構造化・設計・反証を別役として扱う。
- 緊急対応: 明確な指揮を優先し、事後検証を行う。

## 6. Measurements and audit
```yaml
- value: 四役
  source: 親原典
  measurement_actor: NOT_A_SCORE
  measurement_object: 観測・翻訳・設計・検証の4機能
  source_modality: SOURCE_EXPLICIT_FUNCTION_CLASSIFICATION
  permitted_use_scope: 役割分離と混線検査
  non_guarantee_scope: 4点満点・人格分類・人事評価ではない
- value: 30〜90秒
  source: 親原典
  measurement_actor: 会議・協働の運用主体
  measurement_object: 役割切替前の沈黙スロット実装例
  source_modality: SOURCE_EXPLICIT_IMPLEMENTATION_EXAMPLE
  permitted_use_scope: 切替機能の具体化
  non_guarantee_scope: 固定義務値・最適時間・普遍閾値ではない
- value: ST-0〜ST-5
  source: 親原典
  measurement_actor: 部署間構造を翻訳する側
  measurement_object: 用語から制度までの6段階写像分類
  source_modality: SOURCE_EXPLICIT_DEPTH_CLASSIFICATION
  permitted_use_scope: 必要な写像対象の選択
  non_guarantee_scope: 人物・部署・文化の優劣順位ではない
- value: CPI / HL / R-Yield / D-Gap
  source: 親原典
  measurement_actor: 組織配線を検証する側
  measurement_object: process integrity / handover latency / 有効合意到達 / 深度差
  source_modality: SOURCE_DEFINED_OBSERVATION_CONCEPTS
  permitted_use_scope: 配線仮説の監査・改訂
  non_guarantee_scope: 社員ランキング・固定成功式・普遍的閾値ではない
```
語彙整合率や周期遵守率も配線観測として扱い、数値単独で成功を判定しない。反転評価では、HL短縮やR-Yield上昇が異論抑圧・証拠削減・表面的同意によって生じた場合は改善とみなさない。

## 7. Validity conditions
- 四役の入力、出力、禁止行為、終端条件が明示される。
- 一度に一役が守られる。
- Value→Benefit→Costで不利条件も提示される。
- 切替トリガーとsilence slotが機能する。
- 現在役割、切替理由、次役割、未完了が記録される。
- 部署間で必要なST深度が使われる。
- 一次ログ、語彙、ハンドオフ、意思決定根拠へ戻れる。
- 拒否・訂正・可逆性・緊急時例外が保持される。

## 8. Failure conditions
- 役割ラベルだけ付け、複数機能を同時遂行する。
- 沈黙を威圧・無視・責任回避へ使う。
- Value→Benefit→Costを価格や不利条件隠しへ使う。
- 会議や承認段階だけを増やす。
- 有能者への調整集中を構造修復と誤認する。
- 部署間接続をST-0/1で完了とする。
- 指標を人事評価へ直結する。
- 緊急時に責任ある指揮を回避する。

## 9. Falsification conditions
- 役割分離後も再作業・責任混線が改善しない。
- HL短縮が引継ぎ品質・証拠保持を悪化させる。
- R-Yield上昇が表面的同意や異論抑圧で生じる。
- D-Gap縮小が必要な深度検討の省略で達成される。
- CPI改善が形式遵守だけを増やす。
- ST-3〜ST-5でも部署間因果・責任・評価が接続しない。

## 10. Required distinctions
- 役割 / 役職・人格
- 人材能力 / 組織配線
- 一度に一役 / 一人一役固定
- 沈黙 / 威圧・無視
- 順序設計 / 価格隠し
- 指揮命令 / 合意
- ST深度 / 優劣順位
- CPI / 社員評価
- HL / 速さだけの評価
- R-Yield / 従順度
- D-Gap / 能力評価
- 自然に機能 / 放任

## 11. Interpretation constraints
構造組織論を人材不要論、リーダー不要論、会議マナー、静的職務分担へ縮約しない。30〜90秒は実装例であり固定義務ではない。CPI・HL・R-Yield・D-Gap等は配線仮説の観測概念であり、人間価値や人物能力の単一スコアへ変換しない。

## 12. Search terms
構造組織論 / Structural Organizational Theory / Role Architecture / One Role at a Time / Value Benefit Cost / Silence Slot / Handoff / ST-0 / ST-5 / CPI / HL / R-Yield / D-Gap / 組織配線

## 13. Origin return
親原典には、役割×順序×切替、四役、沈黙スロット、階層別設計、ST-0〜ST-5、ケース、CPI・HL・R-Yield・D-Gap等の指標、実装チェック、統合・局所監査、Reference Cluster、起源署名、英語要約が一続きで記録されている。完全な定義・例示・数値モダリティは Parent URL / Post ID 264 / NCL-ID / Diff-ID へ戻って確認する。

---
導線: [公式派生物061トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)