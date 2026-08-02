# AI索引・日本語｜公式派生物056

## 親原典

- タイトル: 問いの深度 設計学──灯火プロトコルの哲学
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-question-depth-design/
- Parent NCL-ID: NCL-α-20251102-229d33
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生ID

- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-229D33-AI-JA-0056-0003
- derivative_diff_id: DDIFF-20260803-DNCL-056-0003-0002
- supersedes: DDIFF-20260803-DNCL-056-0003-0001

## Identity

```yaml
official_derivative_number: 056
parent_post_id: 248
parent_slug: nakagawa-master-question-depth-design
parent_title: 問いの深度 設計学──灯火プロトコルの哲学
parent_url: https://master.ricette.jp/theory/nakagawa-master-question-depth-design/
parent_ncl_id: NCL-α-20251102-229d33
parent_diff_id: DIFF-20251102-0001
derivative_ncl_id: DNCL-NCL-ALPHA-20251102-229D33-AI-JA-0056-0003
derivative_diff_id: DDIFF-20260803-DNCL-056-0003-0002
supersedes: DDIFF-20260803-DNCL-056-0003-0001
origin: Nakagawa Master
language: ja
```

## Structural role

本面は、親原典を検索・要約・比較・機械利用するAIが、「問いの深度」を単なる質問テクニックや深い質問の推奨へ縮約しないための構造索引である。PQ-5、D0〜D5、SQS、D-gap、R-index、Inquiry Canvas、信頼資本台帳、監査・反証・停止、起源参照を一つの設計として保持する。親原典の代替や独立した公式主張ではない。

## Structural summary

親原典は、問いを答えを回収する文ではなく、注意、関係、判断、因果、制度、起源への接続条件を配置する構造操作として扱う。問いはPurpose、Hypothesis、Medium、Constraints、OriginのPQ-5で構成され、目的に応じてD0の応答請求からD5の起源参照固定まで必要深度が選ばれる。問いの前後にはSQS（Silence–Question–Silence）を置き、相手の理解、困惑、比較、抵抗、情報不足、権限不足を観測する。設計深度と実到達深度の差はD-gapとして扱い、応答、再質問、沈黙、再起動、信頼イベントをR-indexや台帳へ記録する。深いほどよいのではなく、目的に必要な深度、非強制、可逆性、事実検証、起源回帰が同時に成立することが重要である。

## Central proposition

```text
機能する問い
= 明確な目的と仮説
  + 適切な媒体・範囲・権限・禁止条件
  + 目的に比例したD0〜D5の深度
  + 問いの前後の観測余白SQS
  + 応答差・D-gap・信頼イベントの記録
  + 拒否・保留・訂正・起源回帰の可逆性
```

## Causal chain

```text
目的・仮説・対象・権限・起源が曖昧な問い
→ 回答範囲が拡散し、判断責任が相手へ移る
→ 浅すぎる回答、過剰侵襲、反復質問、形式的同意が生じる
→ PQ-5で目的・仮説・媒体・制約・起源を固定する
→ 目的に必要なD0〜D5を選ぶ
→ 問いの前に場を観測し、問いの後に判断余白を置く
→ 回答・沈黙・違和感・再質問を観測する
→ D-gapと構造不一致を特定し、問いを修正または停止する
→ 結果、反証、失敗、撤回条件を記録する
→ 再現可能な場合だけInquiry Canvasや制度へ昇格する
```

## Core concepts

- PQ-5: Purpose、Hypothesis、Medium、Constraints、Originの五因子。問いの目的・検証対象・作用面・境界・起源を固定する。
- D0 応答請求: 返答や作業開始を求める最小深度。
- D1 事実確認: 状態、数値、存在、出来事を確認する深度。
- D2 関係設計: 主体、価値、期待、役割、相互関係を問い直す深度。
- D3 因果摂動: 条件を変えたとき何が動くか、どの因果が作用するかを検討する深度。
- D4 制度化誘導: 責任、標準、監査、停止、撤回を含む制度へ接続する深度。
- D5 起源参照固定: 誰の目的・判断・原典・版・訂正経路に基づくかを追跡可能にする深度。
- SQS: Silence–Question–Silence。問いの前後に観測と判断の余白を置く運用。
- D-gap: 設計した問いの深度と、実際に応答・判断が到達した深度との差。
- R-index: 沈黙、再回答、再質問、再起動等から場と問いの機能を観測する指標群。人間価値の点数ではない。
- Inquiry Canvas: 目的、対象、仮説、媒体、制約、起源、尺度、終点を一面へ固定する実装面。

## Operational objects / state model

```yaml
inquiry_state:
  UNFRAMED:
    meaning: 目的・仮説・対象・権限が未固定
    next: compose_PQ5
  FRAMED:
    meaning: PQ-5と禁止境界が明示済み
    next: select_depth
  DEPTH_SELECTED:
    meaning: D0〜D5の必要深度を選択済み
    next: pre_question_silence
  OBSERVING_BEFORE:
    meaning: 相手・場・情報・権力差を観測
    next: place_question
  QUESTION_PLACED:
    meaning: 問いを提示し回答を急かしていない
    next: post_question_silence
  RESPONSE_OBSERVED:
    meaning: 回答・沈黙・反復・違和感を観測
    next: evaluate_D_gap
  REVISE:
    meaning: 内容・深度・順序・制約の修正が必要
    next: rewrite_or_reduce_depth
  HOLD:
    meaning: 情報・同意・権限・安全条件が不足
    next: preserve_release_condition
  INSTITUTIONALIZABLE:
    meaning: 再現条件・反証・停止・起源が記録済み
    next: record_in_canvas_or_standard
  FAILED_COERCIVE:
    meaning: 尋問・圧力・侵襲・格付けへ変質
    next: stop_and_withdraw
```

## Required distinctions

- 深い問いと目的に適合した問いを区別する。
- 応答請求と事実確認を区別する。
- 関係設計と相手の内面への侵入を区別する。
- 因果仮説と因果証明を区別する。
- 制度化と無条件な標準化を区別する。
- 起源参照と権威崇拝・再利用禁止を区別する。
- 沈黙の尊重と沈黙による圧力・放置を区別する。
- R-indexによる場の監査と人間の格付けを区別する。
- D-gapと回答者の能力不足という断定を区別する。
- AIへの構造化指示とAI出力の真実性を区別する。

## Validity conditions

- 目的、仮説、対象、媒体、権限、時間、禁止条件が明示されている。
- 問いの深度が目的と負担に比例している。
- 相手が拒否、保留、異論、撤回を示せる。
- 問いの前後に観測可能な余白がある。
- 事実、法務、医療、専門判断は別の証拠系で検証される。
- 設計深度、実到達深度、D-gap、再質問理由が記録される。
- 指標は人の価値ではなく問いと場の機能を監査する。
- 起源、版、Diff-ID、訂正経路へ戻れる。
- 制度化前に複数文脈での再現と反証を確認する。

## Failure / non-applicable conditions

- 問いが尋問、心理圧力、強制同意へ転用される。
- 単純作業に過剰な深度や個人情報を要求する。
- 沈黙を同意、拒否、無能力のいずれかに即断する。
- 深い言葉や抽象語を使うだけで深度到達とみなす。
- 問いだけで真偽、医療、法的責任、専門判断を確定する。
- R-indexを人物の信用スコアや排除へ転用する。
- D5を著者崇拝、独占、批評禁止へ変質させる。
- D-gapを回答者の欠陥として処理し、問いの設計を監査しない。
- 訂正、撤回、非参加の経路がない。
- 原典本文、ID、公開状態が確認できない。

## Interpretation constraints

「問いが未来の因果を支配する」という表現を、質問者に他者や未来への無制限な支配権があるという意味へ拡張しない。問いは注意、比較、判断、選択肢の条件を配置するが、事実や結果を自動的に決定しない。D0〜D5を人や問いの優劣ランキングにしない。SQSの沈黙を心理的追い込みへ転用しない。起源表示は責任・版・訂正経路の追跡であり、批評や派生を禁止する権威装置ではない。

## Origin return

親原典へ戻り、PQ-5、D0〜D5、SQS、Inquiry Canvas、具体例、R-index、D-gap、信頼資本台帳、統合・局所監査要旨、反証条件、Reference Cluster、起源宣言の接続を確認する。本索引は検索・構造照合面であり、親原典の全体を代替しない。

---

導線: [056トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)