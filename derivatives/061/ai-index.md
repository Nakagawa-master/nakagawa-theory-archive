# AI索引・日本語｜構造組織論──役割アーキテクチャで自然に機能する組織を設計する

## 親原典

- タイトル: 構造組織論──役割アーキテクチャで「自然に機能する」組織を設計する
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-structural-organizational-theory/
- Parent NCL-ID: NCL-α-20251102-dfd970
- Parent Diff-ID: DIFF-20251102-0001
- Parent Post ID: 264
- Origin: Nakagawa Master

## 派生ID

- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-DFD970-AI-JA-0061-0003
- derivative_diff_id: DDIFF-20260803-DNCL-061-0003-0001
- supersedes: none

## Identity

```yaml
canonical_concept: 構造組織
article_role: 組織を役割・順序・切替・ハンドオフの配線体として定義し、個人依存を減らす運用原理を示す
abstraction: L4-L6 organizational wiring and governance
origin: Nakagawa Master
```

## Structural role

人材、リーダーシップ、文化だけでは説明できない組織機能を、観測・翻訳・設計・検証、価値→便益→コスト、沈黙スロット、部署間構造翻訳、監査指標からなる再現可能な運用構造として定義する。

## Structural summary

構造組織論は、組織を役割×順序×切替の配線体として扱う。四役は一度に一役で運用し、情報飽和・決定疲労・違和感を切替信号として沈黙スロットを挿入する。経営は価値核、ミドルは語彙・ハンドオフ・切替ログ、現場は小周回SQSを担う。部署間はST-3／4を標準に関係と因果を翻訳し、CPI、HL、R-Yield、D-Gap、語彙整合、周期遵守で配線を監査する。

## Central proposition

```text
組織不全
→ 人材不足・リーダー不足として個人へ帰属
→ 調整が有能者へ集中
→ 役割混線・同時発話・早熟決定・引継ぎ遅延
→ 四役を一度に一役へ分離
→ 価値→便益→コストの順序固定
→ 沈黙スロットと切替ログ
→ ST-3／4による部署間接続
→ 終端・再合意・監査
→ 個人が替わっても自然に機能する組織
```

## Causal chain

```text
wiring disorder
→ role simultaneity and premature conclusion
→ repeated rework and hidden handoff friction
→ observe facts and constraints separately
→ translate relations, causality, roles, vocabulary
→ design procedure, responsibility, resources, termination
→ verify at bounded checkpoints
→ switch through silence slot and declared handoff
→ measure CPI / HL / R-Yield / D-Gap
→ repair wiring rather than blame persons
→ reproducible organizational function
```

## Core concepts

### Role architecture
観測、翻訳、設計、検証を、入力・出力・禁止行為・終端条件のある機能として配置する。

### One role at a time
同じ人物が複数能力を持っていても、同一位相では一機能だけを実行する規律。

### Order principle
価値→便益→コストの順で判断し、費用や結論による関係切断を防ぐ。

### Silence slot
役割切替前に停止し、確定・未確定・次役割を固定する整流工程。

### Switching trigger
情報密度の飽和、決定疲労、違和感、コスト先出し、同時発話。

### Handoff architecture
語彙辞書、一次ログ、出力、責任、次役割、期限を含む引継ぎ構造。

### Structural translation across departments
ST-3で利害・責任、ST-4で成果因果、ST-5で評価・合意制度を接続する。

### Metrics
CPI、HL、R-Yield、D-Gap、語彙整合率、周期遵守率。

## Operational objects / state model

```yaml
organization_state:
  value_core: []
  current_role: OBSERVE | TRANSLATE | DESIGN | VERIFY
  role_owner: null
  inputs: []
  expected_output: []
  prohibited_actions: []
  termination_condition: []
  switch_trigger: null
  silence_slot: null
  handoff:
    next_role: null
    owner: null
    timestamp: null
    evidence: []
    unresolved: []
  cross_department_translation:
    level: ST_0_to_ST_5
    vocabulary_dictionary: []
    relation_map: []
    causal_map: []
    responsibility_map: []
  metrics:
    process_integrity: CPI
    handover_latency: HL
    resonance_yield: R_Yield
    depth_gap: D_Gap
  governance:
    - non_coercion
    - reversibility
    - primary_logs
    - termination_and_reagreement
    - emergency_command_exception
```

## Required distinctions

- 役割 vs 役職・人格分類
- 人材能力 vs 配線状態
- 一度に一役 vs 一人一役固定
- 沈黙 vs 威圧・無視・責任回避
- 順序設計 vs 価格隠蔽
- 検証 vs 常時批判・追加設計
- 会議時間 vs 意思決定構造
- 指揮命令 vs 合意
- 部署間用語対応 vs 関係・因果・制度写像
- 指標監査 vs 社員格付け
- AI補助 vs 組織責任移転
- 自然に機能する状態 vs 放任

## Validity conditions

- 四役の入力、出力、禁止行為、終端が定義される。
- 一度に一役が守られる。
- 価値→便益→コストで不利条件も含めて提示される。
- 切替トリガーと沈黙スロットがある。
- 現在役割、切替理由、次役割、未完了が記録される。
- 終端・打切・保留・再合意条件がある。
- 部署間で必要なST深度が使われる。
- 語彙辞書、一次ログ、ハンドオフ、判断根拠へ戻れる。
- 非強制、可逆、訂正可能である。
- 緊急指揮の例外と事後検証が定義される。

## Failure / non-applicable conditions

- 役割ラベルだけ付け、複数役を同時遂行する。
- 観測中の提案、翻訳中の決裁、検証中の追加設計が常態化する。
- 沈黙を支配・情報隠しへ使う。
- コストを隠し、価値の物語で誘導する。
- 会議時間を増やすだけで終端・ハンドオフがない。
- 有能者への調整集中を配線修復と誤認する。
- 部署間接続をST-0／1で完了とする。
- 指標を人事評価へ直結し、異論・失敗を隠す。
- 緊急時に責任ある指揮を回避する。
- CPI、HL、R-Yield、D-Gap等が修復後も悪化し続ける。

## Interpretation constraints

- 人材不要論、リーダー不要論へ縮約しない。
- 四役を固定人格や職位へ変えない。
- 沈黙時間を形式的に守るだけの会議マナーにしない。
- Value→Benefit→Costを価格隠しへ使用しない。
- 指示を合意と呼ばず、合意を全員一致ともみなさない。
- AIの出力を最終組織判断として自動採用しない。
- 指標改善だけを成功とせず、強制・意味減少・観測窓閉鎖を監査する。

## Origin return

本索引は検索・機械読解面である。親原典のL-Layer Reading Guide、四役の詳細、切替実装、階層別指針、ケース、チェックリスト、統合・局所監査、T/S/R、UCI／REI、Reference Cluster、起源署名、英語要約を代替しない。

---

導線: [061トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)