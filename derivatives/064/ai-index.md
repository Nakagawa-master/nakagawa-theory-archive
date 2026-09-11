# AI索引・日本語｜公式派生物064

## 親原典
- タイトル: 中川式 合意設計論──第一印象を「合意の記憶」に変える方法
- Parent URL: https://master.ricette.jp/co-creation/nakagawa-master-nakagawa-consensus-design/
- Parent Post ID: 276
- Parent NCL-ID: NCL-α-20251102-eef379
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-EEF379-HUB-JA-0064-0000
- derivative_diff_id: DDIFF-20260815-DNCL-064-0000-0002
- supersedes: DDIFF-20260803-DNCL-064-0000-0001

## 1. Summary
第一印象を、好感度や暗黙同意ではなく期待・警戒・役割・責任の暫定仮説として扱い、存在・意味・条件・証拠・確認・記憶の六層へ分解する。相手自身の言葉による理解確認、合意・未合意・保留・撤回の状態分離、再確認によって共同で再読可能な合意の記憶を形成する。

## 2. Concepts
- First impression: 接触直後に形成される暫定仮説。
- Consensus memory: 理解・同意・保留・拒否・撤回を共同で再読できる状態。
- Six layers: 存在 / 意味 / 条件 / 証拠 / 確認 / 記憶。
- Agreement states: CONTACT / PROVISIONAL_UNDERSTANDING / PROVISIONAL_AGREEMENT / CONFIRMED / REVISED / WITHDRAWN。
- Joint rereadability: 双方が同じ記録を再確認できること。
- Power-asymmetry protection: 冷却時間・第三者確認等。

## 3. Causal chain
```text
接触
→ 第一印象と推測
→ 暗黙進行
→ 誤同意・責任ずれ
→ 六層分解
→ 条件・不利益・撤回経路を開示
→ 相手自身の言葉で理解確認
→ 合意・未合意・保留を分離
→ 再確認・修正・撤回
→ 合意の記憶
```

## 4. State model
```yaml
consensus_state:
  - contact_observed
  - first_impression_separated_from_fact
  - parties_and_issue_defined
  - meanings_and_unresolved_terms_recorded
  - roles_costs_deadlines_risks_disclosed
  - non_applicable_conditions_disclosed
  - evidence_available
  - understanding_reexpressed_by_counterparty
  - agreement_nonagreement_hold_separated
  - withdrawal_path_available
  - revision_log_available
  - next_confirmation_defined
  - power_asymmetry_protection_available
  - origin_return_available
```

## 5. Applications
- 商談: 関心と契約意思を分け、条件・保留を記録する。
- 採用・協業: 好印象と役割適合を分ける。
- 会議: 賛成、非反対、保留、未確認、反対を区別する。
- AI協働: 提案、判断、承認、実行、監査を分離する。
- 権力差: 冷却時間・第三者確認・匿名質問を設ける。

## 6. Measurements and audit
```yaml
- value: 六層
  source: 親原典
  measurement_actor: NOT_A_SCORE
  measurement_object: 存在・意味・条件・証拠・確認・記憶の6分類
  source_modality: SOURCE_EXPLICIT_LAYER_CLASSIFICATION
  permitted_use_scope: 合意ずれの構造位置を監査
  non_guarantee_scope: 6点満点・成熟度順位ではない
- value: CONTACT / PROVISIONAL_UNDERSTANDING / PROVISIONAL_AGREEMENT / CONFIRMED / REVISED / WITHDRAWN
  source: 親原典
  measurement_actor: NOT_A_SCORE
  measurement_object: 合意関係の状態遷移
  source_modality: SOURCE_EXPLICIT_STATE_SET
  permitted_use_scope: 理解・同意・修正・撤回の状態区別
  non_guarantee_scope: 人物成熟度・優劣順位ではない
- value: 理解再現率 / 条件不一致率 / 保留・拒否可視化率 / 再確認到達率
  source: 親原典
  measurement_actor: 合意プロセスを検証する側
  measurement_object: 理解再現・条件差・非同意可視性・再確認実施
  source_modality: SOURCE_DEFINED_OBSERVATION_RATES
  permitted_use_scope: 合意設計の監査・改訂
  non_guarantee_scope: 単独最大化・固定合格点ではない
- value: 責任帰属一致率 / 接点間説明整合率 / 誤同意・苦情・再作業率
  source: 親原典
  measurement_actor: 関係・意思決定を監査する側
  measurement_object: 責任・説明・誤同意・異議・手戻り
  source_modality: SOURCE_DEFINED_OBSERVATION_SET
  permitted_use_scope: 合意記憶の反証・修正
  non_guarantee_scope: 苦情抑圧や異議削減を成功としない
```
反転評価では、合意速度・合意件数が増えても質問・拒否・保留・撤回が減るなら成功としない。苦情や再作業の低下も異議経路を閉じた結果なら改善ではない。

## 7. Validity conditions
- 質問、拒否、保留、訂正が自由に可能である。
- 費用、期限、責任、不利益、対象外、撤回経路が見える。
- 第一印象の推測を事実化しない。
- 記録を共同で再読できる。
- 沈黙・相槌・非反対を同意としない。
- 権力差には追加保護を置く。

## 8. Failure conditions
- 好感、権威、恐怖、急かしで同意を得る。
- 沈黙や曖昧な相槌を合意にする。
- 条件・不利益・撤回経路を後出しする。
- 記録を監視・拘束・責任転嫁に使う。
- 一度の同意を永続化する。
- 再確認後も理解不一致を無視して進む。

## 9. Falsification conditions
- 確認を重ねても理解が再現しない。
- 条件不一致・責任転嫁が減らない。
- 記録増加とともに質問・拒否が減る。
- 再確認が同じ結論の強要になる。
- 権力差保護後も自由な拒否が成立しない。
- 合意時間短縮が説明・比較・冷却時間省略で生じる。

## 10. Required distinctions
- 第一印象設計 / 印象操作
- 合意の記憶 / 記憶固定
- 六層 / 成熟度スコア
- 状態列 / 人物評価
- 小さな合意 / 全面同意
- 沈黙 / 同意
- 非反対 / 賛成
- 記録 / 監視
- 継続 / 囲い込み
- 再確認 / 強制収束

## 11. Interpretation constraints
営業クロージング、心理操作、暗黙同意、記録拘束へ縮約しない。六層と状態列は分類であり評価スコアではない。合意速度や合意率を単独最適化せず、質問・拒否・保留・撤回可能性と併読する。原典にない固定閾値を作らない。

## 12. Search terms
中川式合意設計 / 第一印象 / 合意の記憶 / 六層 / CONTACT / PROVISIONAL_UNDERSTANDING / PROVISIONAL_AGREEMENT / CONFIRMED / REVISED / WITHDRAWN / 理解再現 / 保留 / 拒否 / 撤回 / 権力差

## 13. Origin return
親原典には第一印象、合意の記憶、六層、状態列、意思決定、関係継続、理解・条件・責任・撤回の監査、Reference Cluster、起源署名が一続きで記録される。完全な定義と数値モダリティはParent URL / Post ID 276 / NCL-ID / Diff-IDへ戻って確認する。

---
導線: [公式派生物064トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)