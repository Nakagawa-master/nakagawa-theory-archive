# 公式派生物069｜中川式 接続プロトコル標準論──ID・同意・記憶・可逆を貫く社会API

## 親原典
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-protocol/
- Parent Post ID: 295
- Parent NCL-ID: NCL-α-20251102-9426e0
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-9426E0-HUB-JA-0069-0000
- derivative_diff_id: DDIFF-20260804-DNCL-069-0000-0001
- supersedes: none

## 位置づけ
接続価値会計が測り、接続ガバナンスが守るなら、接続プロトコルは異なる組織・地域・システムの間で接続を持ち運び、再接続可能にする「つなぐ技術」である。本派生物はCXPを中央規格、単なる契約API、個人追跡IDへ誤読せず、最小性・同意・記憶・可逆性・監査可能性を一体で読む入口である。

## 中心命題
接続を社会資産として流通させるには、主体、関係、同意、合意の記憶、接続状態、公開範囲を記述する最小データモデルと、発見から同意・記憶化・評価連携・退出・再接続までの標準手順が必要である。標準は権力集中の道具ではなく、島宇宙化を防ぐ公共的な約束である。

## 因果線
```text
各組織が独自制度を作る
→ 接続価値が閉鎖系に分断される
→ 持ち運び・再接続・監査が困難になる
→ 最小共通語彙とデータモデルを定める
→ 発見・意図表明・同意・記憶化・評価連携を標準化する
→ 離脱・冷却・再接続を仕様に埋め込む
→ 会計の読み取りポートとガバナンス監査APIを接続する
→ 透明性・プライバシ・反ゲーミングを両立する
→ 接続が組織横断で再利用可能な公共資産になる
```

## 構造層
1. **原理層**: 最小性、可逆性、一次情報性、監査可能性、反ゲーミング。
2. **識別層**: SubjectID、RelationID。
3. **同意・記憶層**: ConsentToken、MemoryObject。
4. **状態・可視性層**: ReversibilityFlag、VisibilityClass。
5. **ハンドシェイク層**: 発見、意図表明、同意生成、記憶化、評価連携。
6. **相互運用層**: 会計読み取りポート、監査API、第三者証人ノード、権限分散。
7. **移行層**: CXPログ導入、会計・監査統合、接続基準運用への段階移行。

## 状態モデル
```yaml
cxp_connection:
  subject_ids: []
  relation_id: null
  purpose: null
  boundary_conditions: []
  consent_token: null
  consent_scope: []
  consent_period: null
  memory_object: null
  evidence_hashes: []
  reversibility_flag: DISCOVERED | CONSENTED | ACTIVE | COOLED | EXITED | RECONNECTED
  visibility_class: PUBLIC | INSTITUTIONAL | PRIVATE
  accounting_read_port: []
  audit_api: []
  witness_nodes: []
  abuse_signals: []
  correction_history: []
```

## 適用例
- 研究コンソーシアムで主体・関係・合意条件を共通形式にし、再合意時間を短縮する。
- 自治体と市民団体の連携で、目的・期間・公開範囲・退出手順を明確にする。
- オンラインコミュニティで、強制的囲い込みを検出し、退会後の再参加を保障する。
- AIを含む協働で、AIを責任主体とせず、役割、同意、ログ、監査窓口を明示する。

## 測定・監査点
- 同意破綻率、再合意時間、Rollback Cost、退出成功率、再接続成功率。
- SubjectIDやRelationIDが人格追跡や横断監視へ転用されていないか。
- ConsentTokenの範囲・期間・目的が実運用と一致するか。
- MemoryObjectが改ざんされず、過剰な個人情報を含まないか。
- 会計指標との連携が単一スコア化を招いていないか。
- 監査APIと証人ノードが独立性を保っているか。
- VisibilityClassが隠蔽または過度な公開に使われていないか。

## 成立条件
- 最小データ項目だけで相互運用できる。
- 同意の目的・範囲・期間を明示する。
- 離脱・冷却・再接続を仕様として持つ。
- 一次ログと意味定義を保持する。
- 会計とガバナンスの接続点を分離して設計する。
- 公開室と機関室を区別する。
- 権限と証人ノードを分散する。
- 段階導入と既存制度とのデュアル運用を行う。

## 失敗条件
- 単一企業がID、同意、ログ、監査を独占する。
- ConsentTokenを包括同意や撤回不能契約へ変える。
- MemoryObjectを人格評価や広告追跡へ使う。
- 接続報酬と貨幣を自由交換させる。
- 退出履歴を制裁や差別へ利用する。
- 標準が過剰に複雑化し、参加を阻害する。
- 独自拡張が互換性を壊し、島宇宙化を再生する。
- 監査APIが形式だけで訂正不能になる。

## 反証条件
導入後も再合意時間、同意破綻率、Rollback Cost、誤配、囲い込み、ゲーミングが改善せず、相互運用より監視・複雑性・権力集中が増える場合、CXP設計は改訂または棄却する。

## 必須の区別
```text
標準 ≠ 中央支配
SubjectID ≠ 恒久的人格番号
ConsentToken ≠ 包括同意
MemoryObject ≠ 個人監視記録
可逆性 ≠ 履歴消去
相互運用 ≠ データ無制限共有
社会API ≠ 技術APIだけ
公開室 ≠ 全情報公開
```

## 誤読禁止
- 接続を技術仕様だけへ縮約しない。
- IDを人間価値や信用点数に使わない。
- 同意を一度取得すれば永続すると扱わない。
- 再接続を過去条件の自動復活にしない。
- 標準準拠を強制的囲い込みへ使わない。
- 原典を置き換える完成仕様として扱わない。

## 親原典へ戻る理由
本派生物はCXPの構造を検索・比較しやすくした入口である。各フィールド、ハンドシェイク、会計・ガバナンス連携、Phase 1〜3、参照束の正確な関係は親原典で確認する必要がある。

---
導線: [公式派生物トップ](../README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)