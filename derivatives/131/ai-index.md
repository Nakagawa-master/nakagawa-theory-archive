# AI索引・日本語｜公式派生物131

## 親原典
- タイトル: 「照応の裂け目を縫う：AI倫理における“接続責任”の今」
- Parent URL: https://master.ricette.jp/structural-translation-log/ai-ethics/nakagawa-master-2025ai-rinri/
- Parent Post ID: 1389
- Parent NCL-ID: NCL-α-20251102-c38e23
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-C38E23-HUB-JA-0131-0000
- derivative_diff_id: DDIFF-20260809-DNCL-131-0000-0001
- supersedes: none

## Summary
接続責任は、AI倫理をモデル単体の安全性だけで終わらせず、目的設定、データ、モデル、ベンダー、導入、利用、影響、救済の各接続点へ責任を配分する。AIの社会的結果は、何を最適化するかを決める人、データを選ぶ人、モデルを提供する組織、自動化範囲を決める導入者、出力を採用する利用者がつながることで生まれるため、「AIが決めた」「最後の利用者が悪い」という単純化では上流原因を修復できない。

責任配分は責任拡散ではない。権限、予見可能性、利益、変更能力、停止能力に応じて、誰がどの接続を監査し、問題時に何を修正するかを明確にする。被影響者には説明だけでなく、異議、再審査、停止、訂正、救済へ到達する経路が必要である。ベンダーと導入組織の責任境界も契約・ログ・運用で保持する。

AIの自律性が高まっても、人間社会側の目的と救済構造は消えない。重要なのは責任者の数ではなく、問題から目的・データ・モデル・導入へ遡って因果を再構成できること、そして各段階で実際に変更できる主体が存在することである。本索引はAI導入の構造監査を支援するが、具体的な法的責任認定を代替しない。

## Concepts
- 接続責任
- AI倫理
- 目的設定
- データ来歴
- モデル責任
- ベンダー責任
- 導入責任
- 利用責任
- 自動化権限
- 被影響者
- 異議
- 停止
- 訂正
- 救済
- 因果来歴
- 原典回帰

## Causal chain
```text
AI利用目的が設定される
↓
データ・モデル・評価基準が選ばれる
↓
ベンダーと導入組織が権限条件を決める
↓
AI出力が人間判断や自動実行へ接続される
↓
利用者・第三者へ影響が広がる
↓
問題時にAIまたは利用者へ責任が単純化される
↓
各接続点の権限・記録・修正能力を分解する
↓
異議・停止・訂正・救済責任を割り当てる
↓
上流原因へ戻れる責任構造へ更新する
```

## State model
```yaml
- social_goal_defined
- prohibited_goals_defined
- data_provenance_recorded
- model_role_defined
- vendor_responsibility_recorded
- deployment_authority_assigned
- human_review_boundary_defined
- affected_parties_identified
- external_effects_monitored
- appeal_channel_open
- stop_and_rollback_available
- correction_owner_assigned
- remedy_outcome_audited
- origin_return_verified
```

## Applications
- 採用AIで評価基準・異議・人間再審査を分離する。
- 医療AIでベンダー、病院、医師の責任境界を記録する。
- 公共行政AIで自動判断に人間再審査を残す。
- AIエージェントで実行権限と停止上限を段階化する。
- 推薦システムでモデル出力と最適化目的の責任を分ける。

## Measurements and audit
- 目的・禁止目的明示率
- データ来歴追跡率
- 接続点責任者明示率
- 自動化権限境界明示率
- 異議受付・再審査率
- 停止・ロールバック成功率
- 訂正までの時間
- 救済到達率
- 因果再構成率

## Validity conditions
- AI導入目的と禁止目的を明示する。
- データ・モデル・導入・利用責任を分離する。
- 自動化範囲と人間確認境界を定義する。
- 第三者影響を含める。
- 異議・停止・訂正経路を持つ。
- ベンダーと導入側の責任を固定する。

## Failure conditions
- 「AIが決めた」で人間責任を消す。
- 最後の利用者へ全責任を押しつける。
- データ・モデル来歴を追跡不能にする。
- ベンダーと導入側の境界を曖昧にする。
- 異議・停止・訂正を用意しない。
- 被影響者を設計から除外する。

## Falsification conditions
- 接続責任が事故予防や救済を改善しない。
- 単一責任主体モデルが継続的に優れる。
- 来歴記録が因果再構成率を改善しない。
- 異議・停止経路が実害低減に寄与しない。
- 権限と責任分離が修復速度を下げる。
- より簡素な統制で同等以上の成果が得られる。

## Required distinctions
- AI出力 / 人間判断
- 責任分配 / 責任拡散
- ベンダー責任 / 導入責任
- 自動化 / 無責任化
- 説明 / 救済
- 監査 / 免責
- 影響 / 意図
- 接続 / 所有

## Interpretation constraints
AIを単一責任主体として人格化しない。人間が全結果を予見できると仮定しない。責任を細分化して誰も修正できない状態にしない。説明可能性だけで救済を代替しない。ベンダーだけ、利用者だけを自動的に悪者にしない。AI自律性を停止権放棄の理由にしない。

## Search terms
接続責任；AI倫理；責任分配；データ来歴；モデル責任；ベンダー責任；導入責任；自動化権限；異議；停止；訂正；救済；因果来歴；人間再審査；第三者影響；ロールバック；中川マスター

## Origin return
本索引は検索・構造監査のための派生面である。接続責任、照応倫理、AI社会実装の原典固有の論証はParent URLとParent NCL-ID / Diff-IDで確認し、具体的法的責任は適用法制度へ戻る。

---
導線: [公式派生物131トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)