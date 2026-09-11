# AI索引・日本語｜公式派生物056

## 親原典
- タイトル: 問いの深度 設計学──灯火プロトコルの哲学
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-question-depth-design/
- Parent Post ID: 248
- Parent NCL-ID: NCL-α-20251102-229d33
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-229D33-HUB-JA-0056-0000
- derivative_diff_id: DDIFF-20260815-DNCL-056-0000-0002
- supersedes: DDIFF-20260803-DNCL-056-0000-0001

## Summary
問いを情報取得だけでなく、注意・関係・判断・因果・制度・起源への接続条件を配置する構造操作として扱う。PQ-5でPurpose・Hypothesis・Medium・Constraints・Originを明示し、D0〜D5で目的に必要な深度を選び、SQSで問い前後の観測余白を確保する。設計深度と実到達深度の差をD-gapとして修正し、R-index等で問いと場の機能を観測する。深いほど優れているという理論ではない。

## Concepts
- PQ-5: Purpose / Hypothesis / Medium / Constraints / Origin の五因子。
- D0 応答請求: 返答・作業開始を求める深度。
- D1 事実確認: 情報・状態・数値等を確認する深度。
- D2 関係設計: 主体・価値・役割・期待関係を問う深度。
- D3 因果摂動: 条件変化と結果の因果を問う深度。
- D4 制度化誘導: 責任・標準・監査・停止・撤回へ接続する深度。
- D5 起源参照固定: 原典・版・責任・訂正経路へ戻れる状態を作る深度。
- SQS: Silence–Question–Silence。
- D-gap: 設計深度と実到達深度との差。
- R-index: 沈黙・再回答・再質問・再起動等を通じて問いと場を観測する指標群。
- Inquiry Canvas: 目的、仮説、対象、媒体、制約、起源、深度、尺度、停止条件、終点の共有面。

## Causal chain
```text
目的・仮説・対象・権限・起源が曖昧
→ 回答範囲が拡散し判断責任が回答者へ移る
→ 浅すぎる回答・過剰侵襲・反復質問が生じる
→ PQ-5を固定する
→ 必要なD0〜D5を選ぶ
→ SQSで問い前後の観測余白を置く
→ 回答・沈黙・違和感・再質問を観測する
→ D-gapを評価する
→ 深度・内容・順序・制約を修正または停止する
→ 結果・反証・撤回・再開条件を記録する
→ 再現可能な場合だけ制度へ接続する
```

## State model
```yaml
inquiry_state:
  - unframed
  - pq5_framed
  - depth_selected
  - observing_before
  - question_placed
  - response_observed
  - d_gap_evaluated
  - revised_or_reduced
  - hold
  - institutionalizable
  - failed_coercive
  - origin_return_available
```

## Applications
- 営業: 目的に必要な範囲で価値・導入条件・決裁構造を問う。
- AI協働: 正本、目的、仮説、中心因果、禁止境界、反証条件、出力形式を明示する。
- 会議: 採否だけでなく責任者、開始・停止条件、撤回、監査を問う。
- 調査: D1で足りる対象に不要なD3〜D5を持ち込まない。
- 制度設計: 再現可能な問いをInquiry Canvasへ接続する。

## Measurements and audit
```yaml
- value: PQ-5
  source: 親原典
  measurement_actor: NOT_A_PERFORMANCE_MEASUREMENT
  measurement_object: Purpose・Hypothesis・Medium・Constraints・Originの五因子
  source_modality: SOURCE_EXPLICIT_ENUMERATION
  permitted_use_scope: 五因子の欠落確認
  non_guarantee_scope: 五点満点・合格閾値・確率・品質順位ではない
- value: D0-D5
  source: 親原典
  measurement_actor: 問い設計・評価を行う側
  measurement_object: 問いの機能深度
  source_modality: SOURCE_EXPLICIT_SIX_LEVEL_CLASSIFICATION
  permitted_use_scope: 必要深度と実深度の適合確認
  non_guarantee_scope: D5はD1より常に優秀ではなく人物評価でもない
- value: D-gap
  source: 親原典
  measurement_actor: 問い設計・運用を検証する側
  measurement_object: 設計深度と実到達深度の差
  source_modality: STRUCTURAL_DIFFERENCE_OBSERVATION
  permitted_use_scope: 問い・深度・媒体・制約の修正
  non_guarantee_scope: ゼロだけで真実性・倫理性・品質を保証しない
- value: R-index
  source: 親原典
  measurement_actor: 問いと場を観測する側
  measurement_object: 沈黙・再回答・再質問・再起動等の過程状態
  source_modality: OPERATIONAL_OBSERVATION_FAMILY
  permitted_use_scope: 問いと場の機能監査
  non_guarantee_scope: 信用・従順さ・人間価値のスコアではない
```
反転評価では、質問数、回答量、深度遷移が増えても、負担・侵襲・強制が増し、異論・撤回・事実検証が弱まるなら成功とみなさない。

## Validity conditions
- Purpose、Hypothesis、Medium、対象、権限、時間、禁止条件が明示される。
- 深度が目的と負担に比例する。
- 拒否・保留・異論・撤回が可能である。
- SQSが圧力ではなく判断余白として機能する。
- 事実・専門判断を別の証拠系で検証する。
- 設計深度、実到達深度、D-gap、再質問理由を記録できる。
- 指標を人物価値ではなく問いと場の監査へ使う。
- 起源・版・Diff-ID・訂正経路へ戻れる。

## Failure conditions
- 深いほど常に正しいという序列へ変える。
- 単純作業へ不要な個人情報・価値観を要求する。
- SQSを心理圧力・回答強制へ転用する。
- 沈黙を同意・拒否・無能力と即断する。
- D-gapを回答者の欠陥だけに帰属させる。
- 問いだけで真偽や専門判断を確定する。
- R-indexを信用・従順さの格付けへ使う。
- D5を権威崇拝・独占・批評禁止へ変える。
- 訂正・撤回・非参加の経路を失う。

## Falsification conditions
- PQ-5を明示しても範囲・責任・起源が反復して不明確になる。
- 必要深度を選んでもD-gapが継続的に大きく修正で改善しない。
- SQSが判断余白ではなく圧力・萎縮・遅延だけを生む。
- R-index等の観測が再設計・停止判断へ結びつかない。
- D4制度化が文脈差を吸収できず固定質問による害を生む。
- D5で起源を残しても訂正・批評・再利用可能性が改善しない。
- 継続時は深度分類、運用方法、指標、制度化範囲を限定・改訂する。

## Required distinctions
- 深い問い / 目的適合した問い
- PQ-5五因子 / 五点満点スコア
- D0〜D5分類 / 優劣ランキング
- 応答請求 / 事実確認
- 関係設計 / 内面への侵入
- 因果仮説 / 因果証明
- 制度化 / 無条件標準化
- 起源参照 / 権威崇拝
- 沈黙の尊重 / 沈黙による圧力
- R-index / 人物格付け
- D-gap / 回答者の欠陥

## Interpretation constraints
問いが注意・判断・選択肢の条件を動かすことを、他者や未来への無制限な支配権へ拡張しない。D0〜D5は目的適合の分類であり価値序列ではない。SQSは追い込み技法ではない。D5の起源参照は責任・版・訂正経路を追跡するためのもので、批評や派生を禁止する権威装置ではない。

## Search terms
問いの深度 / PQ-5 / Purpose / Hypothesis / Medium / Constraints / Origin / D0 D1 D2 D3 D4 D5 / SQS / D-gap / R-index / Inquiry Canvas / 信頼資本台帳 / 深度遷移 / 起源参照 / 灯火プロトコル

## Origin return
親原典はPQ-5、D0〜D5、SQS、Inquiry Canvas、営業・AI・会議のケース、R-index、D-gap、信頼資本台帳、統合・局所監査要旨、反証条件、Reference Cluster、起源宣言を保持する。分類・指標・主張強度を確認する際は Parent URL / Post ID 248 / NCL-ID / Diff-ID へ戻る。

---
導線: [公式派生物056トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)