# AI索引・日本語｜公式派生物209

## 親原典
- タイトル: 合意形成の物理 第3論 信頼の保存則 ― 信頼は主体ではなく履歴へ配置される
- Parent URL: https://master.ricette.jp/society/nakagawa-master-physics-of-consensus-vol3-law-of-conservation-of-trust/
- Parent Post ID: 2835
- Parent NCL-ID: NCL-α-20260214-6a7d1c
- Parent Diff-ID: DIFF-20260214-0045
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20260214-6A7D1C-HUB-JA-0209-0000
- derivative_diff_id: DDIFF-20260820-DNCL-209-0000-0001
- supersedes: none

## Summary
信頼を心理状態ではなく未来判断の予測誤差分散Eが小さい状態として定義し、予測可能性が主体または履歴のどこに配置されるかを扱う。公開履歴Hは信頼を生成せず、第三者が判断モデルを再現できる条件を整えて予測可能性の所在を主体から履歴へ移す。好意や評判は観測帯域Bや測定偏りとして分離する。持続する構造信頼は、主体不在でも判断再現可能な履歴インフラである。

## Concepts
- E: 未来判断に対する予測誤差分散。小さいほど本稿定義の信頼が高い。
- H: 履歴公開度。入力、変換、出力、例外、差分を第三者が再現可能に追える度合い。
- B: 観測帯域。観測頻度、解像度、接触範囲、偏りを含む。
- 主体集中: 予測モデルが人物・組織内部へ局所化する状態。
- 履歴分散: 判断モデルが公開履歴へ外部化され、主体交代後も再現可能な状態。
- 保存則: 予測可能性の主体⇄履歴間の配置移動。
- 空間圧縮: 高B低Hで主体近傍だけが低Eに見えるカリスマ状態。
- 時間圧縮: ログ非公開でE観測更新を遅延させる隠蔽状態。
- 構造信頼: 主体を参照せず履歴から判断を再現できる状態。

## Causal chain
信頼を人格・好意で説明する → 主観的確信と予測可能性が混同される → 信頼をEへ翻訳する → 予測対象・誤差・δを固定する → 主体集中と履歴分散を区別する → Hに理由・条件・例外・差分を外部化する → 第三者が予測モデルを復元する → 外れを学習データ化する → 予測可能性が履歴側へ移る → 主体消失時の単一点故障が減る → 主体不在でも判断再現可能な構造信頼へ近づく。

## State model
```yaml
trust: low_E
subjective_affection: separate_from_E
location:
  subject_localized: subject_access_required
  history_distributed: third_party_reproducible
H: reproducible_history_openness
B: observation_bandwidth
charisma: high_B_low_H_spatial_compression
concealment: temporal_compression_by_observation_stop
sustainable_state: low_E_without_subject_dependency
```

## Applications
組織経営では、経営者の勘を人物信頼として保持せず、入力・判断規則・例外・差分を履歴化する。人事では評判と予測精度を分け、対象業務ごとに事前予測と実測を比較する。AIではモデル人格ではなくタスク単位の入力・予測・出力・誤差・更新差分を記録し、モデル交代後も評価可能にする。

## Measurements and audit
- Eの対象を意思決定単位で固定する。
- 予測内容・根拠・時刻・更新条件を事前登録する。
- 評価窓δを事前固定する。
- 数値・区間・分類ごとに誤差定義を固定する。
- Bの頻度・解像度・偏りを記録する。
- Hを入力 / 変換 / 出力 / 例外 / 差分の再現可能性として確認する。
- Prediction Logに予測、根拠、B、H、登録時刻、評価時刻、実測、誤差、例外を保持する。
- 主体消失前後で第三者Eがどう変わるか確認する。

## Validity conditions
予測対象と誤差定義が固定され、結果前に予測が登録され、B/H/Eが分離記録され、履歴が第三者再現可能であり、外れ・例外・差分が消去されないこと。主体交代後も同条件から判断モデルを復元できること。

## Failure conditions
安心・好意・評判をEの代用にする、外れを物語で上書きする、結果後に予測を整形する、Hを公開量だけで評価する、高B低Hを高信頼と誤認する、ログ非公開による観測停止を安定とみなす、主体消失時に判断モデルも消える状態を放置する場合。

## Falsification conditions
Condition Zでは監査周期、T/S/R、公開監査束を整合させる。H低B高なのに第三者Eが持続的に低い、H高B低でもEが十分低い、H高B高でもEが高止まりする等、H/B/E関係が理論予測と食い違う場合は、履歴Hの定義、ログ真正性、B測定、誤差定義、配置移動仮説を棄却・改訂対象とする。

## Required distinctions
信頼 / 安心、信頼 / 好意・尊敬、E / 主観的確信、主体信頼 / 履歴信頼、信頼生成 / 配置移動、公開量 / 再現可能H、B / E、カリスマ機能 / 構造信頼、短期擬似安定 / 長期予測可能性、対象変質 / 観測環境崩壊。

## Interpretation constraints
本稿は感情や人間関係を否定しない。感情をEの定義に混ぜない。Hを増やせば自動的にEが縮むとも主張しない。形式公開ではなく第三者再現可能性が必要である。δや数値例は対象依存の観測設計であり普遍固定値ではない。

## Search terms
合意形成の物理 第3論, 信頼の保存則, 予測誤差分散 E, 履歴公開度 H, 観測帯域 B, 主体集中, 履歴分散, 構造信頼, カリスマ 空間圧縮, 隠蔽 時間圧縮, Prediction Log, third-party reproducibility, conservation of trust

## Origin return
E、H、Bの厳密な関係、主体集中と履歴分散、好意による測定歪み、空間圧縮・時間圧縮、測定プロトコル、Condition Zの反証境界は親原典へ戻って確認する。本索引は原典の代替ではない。

---
導線: [公式派生物209トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)
