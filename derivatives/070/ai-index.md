# AI索引・日本語｜公式派生物070

## 親原典
- タイトル: 中川式 接続基本権憲章──接続社会の権利・義務・手続の最小核
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-bill-of-rights/
- Parent Post ID: 299
- Parent NCL-ID: NCL-α-20251102-e18ffd
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-E18FFD-HUB-JA-0070-0000
- derivative_diff_id: DDIFF-20260815-DNCL-070-0000-0002
- supersedes: DDIFF-20260804-DNCL-070-0000-0001

## 1. Summary
接続基本権憲章は、接続履歴・評価・ネットワーク位置が配分、信用、参加、生活機会へ影響する社会で、人間の尊厳、自己決定、平等、手続的公正を守る最小権利体系である。接続する権利だけでなく、接続しない権利、目的・範囲限定、理解可能な説明、異議、訂正、退出、忘却、再接続、人間審査、救済を、通知・理由提示・暫定保護・独立審査・補償・再発防止を伴う実行可能な手続として扱う。

## 2. Concepts
- 接続権 / 非接続権: 接続する自由と接続しない自由。
- Self-determination: 相手、目的、範囲、期間を本人が選ぶこと。
- Explanation right: 記録、利用、判断理由を理解できること。
- Objection / correction: 誤記録・誤評価・目的外利用へ異議を述べ訂正できること。
- Exit / forgetting / reconnection: 離脱、不要記録の削除・非活性化、新条件での再接続。
- Human review: AI・自動判断に対する人間審査。
- Remedy: 暫定停止、訂正、再計算、権利回復、補償、再発防止。
- Non-discrimination / accommodation: 権利行使による報復を防ぎ、必要な合理的配慮を提供すること。

## 3. Causal chain
```text
接続履歴・評価が配分・信用・参加・機会へ影響
→ 権利境界がなければ接続強制・排除・監視・訂正不能が起きる
→ 接続 / 非接続 / 範囲限定 / 説明 / 異議 / 訂正 / 退出 / 忘却 / 再接続を基本権として定める
→ 各権利へ運営者・監査者・AI支援者の義務を対応させる
→ 通知・理由提示・暫定停止・独立審査・救済・期限を手続化する
→ 接続履歴や指標による基本権・生活機会の不当な剥奪を防ぐ
→ 接続制度を尊厳・自己決定・平等・手続的公正へ従属させる
```

## 4. State model
```yaml
connection_rights_case:
  person_or_group: []
  connection_context: []
  asserted_rights: []
  responsible_operator: []
  automated_systems_used: []
  notice_delivered: []
  explanation_delivered: []
  objection_received: []
  provisional_relief: []
  independent_review: []
  correction_requested: []
  deletion_or_deactivation: []
  exit_requested: []
  reconnection_terms: []
  remedy: []
  compensation: []
  recurrence_prevention: []
  deadline: []
  state: REQUESTED | PROVISIONALLY_PROTECTED | UNDER_REVIEW | CORRECTED | REMEDIED | CLOSED | REOPENED
```
状態集合は権利案件の手続状態を表す分類であり、本人の信用、人格、価値、成熟度を評価するスコアではない。

## 5. Applications
- 接続価値制度: 評価理由、異議、訂正、暫定停止、再計算、救済を権利として実装する。
- オンラインコミュニティ: 匿名・仮名、モデレーション異議、退出後データ、再参加条件を明示する。
- AIエージェント: 代理範囲、停止権、説明権、人間審査、訂正、責任主体を保障する。
- 行政・雇用・教育: 接続履歴・ネットワーク指標による基本機会の不当な選別を防ぐ。
- 支援が必要な利用者: 言語、障害、年齢、代理関係に応じた合理的配慮を提供する。

## 6. Measurements and audit
```yaml
- value: REQUESTED / PROVISIONALLY_PROTECTED / UNDER_REVIEW / CORRECTED / REMEDIED / CLOSED / REOPENED
  source: 親原典
  measurement_actor: NOT_A_SCORE
  measurement_object: 権利案件の手続状態
  source_modality: SOURCE_EXPLICIT_STATE_SET
  permitted_use_scope: 申立て・暫定保護・審査・訂正・救済・終了・再開の区別
  non_guarantee_scope: 本人の信用点・成熟度順位ではない
- value: 初動時間 / 暫定停止までの時間 / 最終解決時間
  source: 親原典
  measurement_actor: 運営者・独立審査者・影響当事者
  measurement_object: 権利行使と救済の応答性
  source_modality: SOURCE_DEFINED_REMEDY_TIME_OBSERVATION
  permitted_use_scope: 被害拡大防止と手続実効性の検証
  non_guarantee_scope: 短いほど常に良いとは限らず、審査省略・不十分説明で短縮してはならない
- value: 訂正 / 削除 / 非活性化 / 退出要求の実行率 / 人間審査移行率
  source: 親原典
  measurement_actor: 権利手続を運営・監査する側
  measurement_object: 権利が宣言ではなく実行可能か
  source_modality: SOURCE_DEFINED_RIGHTS_EXECUTION_OBSERVATION
  permitted_use_scope: 権利アクセス・履行・人間審査の実効性を検証
  non_guarantee_scope: 高率そのものを目的化せず、不要な申立て誘発や形式的処理を成功としない
- value: 拒否・範囲限定者への不利益 / 救済後の差別・排除・目的外利用の再発
  source: 親原典
  measurement_actor: 独立監査者・影響当事者・責任主体
  measurement_object: 報復、不当差別、再発防止の実効性
  source_modality: SOURCE_DEFINED_NONRETALIATION_AND_RECURRENCE_OBSERVATION
  permitted_use_scope: 権利行使が不利益へ変換されていないかの検証
  non_guarantee_scope: 件数の低さだけで健全性を保証せず、申立て不能・検出不能を区別する
```
反転評価では、権利行使件数が少なくても窓口不明・手続困難・報復懸念による萎縮なら成功ではない。救済時間が短くても説明・独立審査・必要な補償を省略しているなら改善ではない。退出率が低くても退出へ不利益があるなら権利保障とはいえない。

## 7. Validity conditions
- 権利が宣言ではなく操作可能な手続として実装される。
- 接続拒否、範囲限定、退出、異議による報復がない。
- 審査主体が元の判断主体から一定程度独立する。
- 説明が本人の言語・能力・状況に応じて理解可能である。
- 緊急停止、暫定救済、人間審査、訂正、削除、補償が利用できる。
- 訂正、削除、退出が全接続先へ反映される。
- AI・委託先を使っても責任主体が消えない。
- 支援が必要な人へ合理的配慮を提供する。

## 8. Failure conditions
- 接続参加を事実上強制する。
- 権利手続を有料・複雑・長期化して利用を妨げる。
- 退出後も評価、権限、データ利用が残る。
- 忘却を理由に必要な監査証拠まで無説明で消す。
- AI判断を理由に説明、審査、責任を拒む。
- 接続履歴で公共的権利や生活機会を不当に制限する。
- 異議申立者を低信頼者として扱う。
- 権利文書だけを公開し救済窓口・期限・責任主体を設けない。

## 9. Falsification conditions
- 権利を定めても異議、訂正、退出の実効性が改善しない。
- 接続拒否者、退出者、異議申立者への不利益が減らない。
- 救済が長期化し暫定被害が拡大する。
- AI、委託先、プラットフォーム間で責任主体が消える。
- 忘却と監査の境界が定まらず監視または証拠消失が続く。
- 手続費用・複雑性・言語や能力上の障壁によって権利が実質利用不能である。

## 10. Required distinctions
- 接続する権利 / 接続を強制される義務
- 退出権 / 既存責任の無条件放棄
- 忘却権 / 監査証拠の無条件消去
- 説明権 / アルゴリズム全文公開
- 平等 / 合理的配慮を欠く画一処理
- AI支援 / 人間審査の廃止
- 再接続 / 過去の被害の抹消
- 権利宣言 / 権利を実行できる手続
- 権利行使件数の少なさ / 制度健全性
- 救済の速さ / 手続の十分性

## 11. Interpretation constraints
象徴的な権利一覧だけへ縮約しない。接続機会の提供だけで十分としない。退出者・異議申立者を低信頼者として扱わず、忘却を証拠隠滅へ使わず、安全を理由に無期限監視を正当化しない。AIの自動判断を最終決定へしない。権利行使件数の少なさや救済時間の短さを単独で制度健全性へ変換しない。

## 12. Search terms
中川式接続基本権 / 接続しない権利 / 自己決定 / 範囲限定 / 説明権 / 異議申立て / 暫定停止 / 独立審査 / 訂正権 / 退出権 / 忘却権 / 再接続権 / 非差別 / 人間審査 / 救済 / 再発防止

## 13. Origin return
親原典には権利と対応義務、通知、理由提示、暫定停止、独立審査、訂正、削除、補償、再発防止、忘却と監査の境界、合理的配慮、Reference Clusterが一続きで記録されている。完全な定義と観測モダリティはParent URL / Post ID 299 / NCL-ID / Diff-IDへ戻って確認する。

---
導線: [公式派生物070トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)