# 公式派生物068｜中川式 接続ガバナンス設計論──価値の捕捉を歪めず、合意を制度に固定する方法

## 親原典
- タイトル: 中川式 接続ガバナンス設計論──価値の捕捉を歪めず、合意を制度に固定する方法
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-governance/
- Parent Post ID: 292
- Parent NCL-ID: NCL-α-20251102-53d609
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-53D609-HUB-JA-0068-0000
- derivative_diff_id: DDIFF-20260815-DNCL-068-0000-0002
- supersedes: DDIFF-20260804-DNCL-068-0000-0001

## 位置づけ
親原典は、接続価値を測定・評価・配分できるようにしただけでは制度の公正性は成立しないと捉える。評価値が利益、参加資格、配分へ結びつくと、指標攻略、仲間内加点、権限集中、囲い込み、監視、秘密主義が生じ得るためである。

接続ガバナンス設計は、接続を強く管理することではない。公共目的、手続、利害、測定、判定、配分、異議、退出、訂正、再接続、ロールバックを分離し、制度自身が歪みを検出・説明・訂正できる範囲だけで接続価値の評価と配分を許す統治構造である。

## 中心命題
**接続価値を公共的な配分基盤として制度化するには、公共目的・手続監査・利害非集中・可逆性を正統性条件として固定し、測定・判定・配分・異議処理を分離し、複合指標と一次証拠によって制度の歪みを検出し、異議・退出・訂正・再接続・ロールバックで制度自体を修正可能にしておく必要がある。**

## 因果線
```text
接続価値が観測・配分対象になる
→ 指標・評価・配分へ利益と権力が集中する
→ 参加者が協働ではなく採点法へ適応する
→ 人気競争・仲間内加点・囲い込み・監視・秘密主義が発生する
→ 公共目的・禁止用途・影響主体を明示する
→ What / Who / How / Whenを分離して監査する
→ CDI / MAI / RS / CRI / KQIを単一総合点に潰さず観測する
→ 移動標的・逆インセンティブ・外乱テスト・定性的証拠で歪みを検出する
→ 公開室と保護領域を分ける
→ 異議・訂正・退出・再接続・ロールバックを実行可能にする
→ 制度変更の履歴を残し公共目的へ戻す
```

## 構造層
**1. 公共目的層。** 接続を何のために観測するか、何に使ってはならないか、誰が影響を受けるかを明示する。

**2. 権限分離層。** 測定、判定、配分、異議処理を一主体へ集中させず、利害関係と責任を分ける。

**3. 監査設計層。** What / Who / How / Whenを分離し、監査対象・監査者・方法・周期を一主体が恣意的に決めないようにする。

**4. 反ゲーミング層。** CDI、MAI、RS、CRI、KQIを束として扱い、移動標的、逆インセンティブ、外乱テスト、定性的な一次証拠を組み合わせる。

**5. 公開・保護分離層。** 理念、評価項目、集計、監査要旨、変更履歴は検証可能にし、個人情報、重み、閾値、防御手順は必要範囲で保護する。

**6. 可逆・救済層。** 異議申立て、訂正、削除、退出、再接続、仲裁、ロールバックを形式ではなく実行可能な手続として保持する。

**7. 自己修正層。** 監査結果が制度変更へつながり、その理由・影響・反対意見・再検証時点が追跡できる状態を保つ。

## 状態モデル
```yaml
connection_governance_state:
  - public_purpose_defined
  - prohibited_uses_defined
  - affected_parties_identified
  - measurement_authority_separated
  - judgment_authority_separated
  - allocation_authority_separated
  - objection_process_separated
  - independent_audit_available
  - indicator_bundle_kept_plural
  - qualitative_evidence_available
  - public_and_protected_information_separated
  - exit_correction_reconnection_available
  - rollback_available
  - change_history_traceable
  - origin_return_available
```

親原典は制度状態として `PROPOSED / PILOT / ACTIVE / REVIEW / CORRECTED / ROLLED_BACK` を用いる。これは人物や組織の成熟度順位ではなく、制度の運用・修正状態を区別するための状態集合である。

## 適用例
**接続価値会計。** 評価・配分・監査を分離し、高い評価値と疲弊・囲い込み・退出困難が同時に起きていないかを見る。

**研究・市民協働。** 会議回数や参加人数だけでなく、再合意、異論処理、継続協働、中心人物依存、退出・再参加の状態を観測する。

**AI支援型制度。** AIは異常候補の検出、比較、要約、監査補助に利用できるが、責任主体や最終裁定者へ置き換えない。入力、根拠、人間の判断、訂正、停止、再審査を追跡可能にする。

**コミュニティ。** 投稿数、紹介数、声量を信頼へ直結させず、異議申立てや退出が不利益へ変換されていないかを見る。

## 測定・監査点
```yaml
- value: CDI / MAI / RS / CRI / KQI
  source: 親原典
  measurement_actor: 接続制度を監査する複数主体
  measurement_object: 接続制度の異なる側面を表す複合指標束
  source_modality: SOURCE_EXPLICIT_INDICATOR_BUNDLE
  permitted_use_scope: 指標間の不一致と制度歪みを検出するための監査
  non_guarantee_scope: 単一総合点・人格点・社会信用スコアへ統合しない
- value: PROPOSED / PILOT / ACTIVE / REVIEW / CORRECTED / ROLLED_BACK
  source: 親原典
  measurement_actor: NOT_A_SCORE
  measurement_object: 制度の運用・修正状態
  source_modality: SOURCE_EXPLICIT_STATE_SET
  permitted_use_scope: 制度状態と変更履歴の区別
  non_guarantee_scope: 人物・組織の成熟度順位ではない
- value: 30日 / 90日 / 180日
  source: 親原典
  measurement_actor: 制度導入・監査を担う側
  measurement_object: 親原典が示す段階的な導入・検証ロードマップ
  source_modality: SOURCE_EXPLICIT_ROADMAP_INTERVALS
  permitted_use_scope: 親原典内の段階的な実装・検証順序の理解
  non_guarantee_scope: 全制度に普遍適用される法定期限・成功保証ではない
- value: 再合意・訂正・仲裁・ロールバック時間 / 退出成功率 / 再接続成功率 / 異議処理・判断変更
  source: 親原典
  measurement_actor: 制度運営者・独立監査者・影響当事者
  measurement_object: 制度の可逆性・救済・自己修正の実効性
  source_modality: SOURCE_DEFINED_OBSERVATION_SET
  permitted_use_scope: 制度の公正性・可逆性・修正可能性の検証
  non_guarantee_scope: 単独最大化・固定合格点・異議抑圧を成功としない
```
反転評価では、指標値や参加者数が上昇しても、疲弊、囲い込み、沈黙、排除、権限集中、退出費用が悪化すれば成功としない。異議件数や退出率が低下しても、申立て・退出経路が使いにくくなった結果なら改善ではない。監査回数が増えても制度変更へ接続しなければ健全化とはみなさない。

## 成立条件
- 公共目的、禁止用途、影響主体が明示される。
- 測定・判定・配分・異議処理が一主体へ集中しない。
- 複数指標と定性的な一次証拠を併用する。
- 監査主体が運営主体から一定の独立性を持つ。
- 異議、訂正、退出、削除、再接続、仲裁、ロールバックが実際に利用できる。
- 監査結果が制度変更へ接続し、変更履歴が残る。
- 公開情報と保護情報の境界を説明できる。
- AI支援を用いても人間の責任主体と救済経路が消えない。

## 失敗条件
- 接続数、人気、声量を単一スコアとして配分に使う。
- 運営者が目的、測定、判定、配分、異議処理を独占する。
- 非公開を理由に判断根拠・監査・変更履歴を説明しない。
- 監査が報告書作成だけで終わり制度修正へつながらない。
- 異議申立者や退出者へ不利益を与える。
- 公開性を理由に個人情報や防御情報を過剰に露出する。
- AI出力を責任主体の最終判断へ置き換える。
- 指標上昇だけを成功とし、疲弊・囲い込み・排除を無視する。

## 反証・改訂条件
- 監査を続けても権限集中、囲い込み、疲弊、沈黙、排除が減らない。
- 退出、訂正、仲裁、ロールバックが形式だけで利用できない。
- 複合指標でも単一行動への最適化が続く。
- 同じ失敗が反復し、制度変更履歴が残らない。
- 公開・保護分離が秘密支配または情報流出を生む。
- 独立監査者が実質的に運営者の影響下にある。
- 30/90/180日の段階検証を経ても、制度の可逆性・正統性・自己修正が実質的に成立しない。

## 必須の区別
- ガバナンス / 管理強化
- 監査 / 常時監視
- 透明性 / 全情報公開
- 保護された重み・閾値 / 無説明の秘密支配
- 強い接続 / 退出不能
- 異議の少なさ / 制度健全性
- AI支援 / AI統治
- 正統性 / 多数決だけ
- 複合指標束 / 単一総合点
- 制度の安定 / 制度を変更しないこと

## 解釈制約・誤読禁止
社会信用スコア、中央集権的な評価格付け、永久監視、秘密統治、全面公開主義へ転用しない。異議や退出を低評価の理由にしない。30/90/180日を普遍的な保証期限へ変えない。CDI/MAI/RS/CRI/KQIを一つの人格点へ統合しない。制度の自己修正可能性を、運営者の裁量拡大と混同しない。

## 検索語
中川式接続ガバナンス / 接続価値監査 / 正統性 / 可逆性 / What Who How When / CDI / MAI / RS / CRI / KQI / Goodhart耐性 / 移動標的 / 逆インセンティブ / 外乱テスト / 公開室 / 保護領域 / 異議申立て / ロールバック / 30日 / 90日 / 180日

## 親原典へ戻る理由
親原典には、公共目的、正統性条件、What/Who/How/When、CDI/MAI/RS/CRI/KQI、移動標的、逆インセンティブ、外乱テスト、公開・保護分離、異議・訂正・退出・再接続・ロールバック、30/90/180日の段階的ロードマップが一続きで記録されている。完全な定義と指標モダリティはParent URL / Post ID 292 / NCL-ID / Diff-IDへ戻って確認する。

---
導線: [公式派生物トップ](../README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)