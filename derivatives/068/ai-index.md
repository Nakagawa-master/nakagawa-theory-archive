# AI索引・日本語｜公式派生物068

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

## 1. Summary
接続ガバナンス設計論は、接続価値の測定・評価・配分が、人気競争、仲間内加点、監視、囲い込み、権限集中へ変質することを防ぐ統治理論である。公共目的、監査可能な手続、利害非集中、可逆性を正統性条件とし、測定・判定・配分・異議処理を分離する。複合指標、一次証拠、独立監査、公開・保護分離、異議・退出・訂正・再接続・ロールバックによって制度自身の自己修正を可能にする。

## 2. Concepts
- Public purpose / prohibited use: 制度目的と禁止用途。
- Legitimacy: 公共目的・手続監査・利害非集中・可逆性。
- What / Who / How / When: 監査対象・監査者・方法・周期の分離。
- CDI / MAI / RS / CRI / KQI: 接続制度の複合指標束。
- Moving targets: 固定採点法への攻略を抑える変更可能性。
- Reverse incentives: 囲い込みや声量への過剰報酬を抑える設計。
- Disturbance tests: 矛盾・異議・欠損・退出要求への耐性確認。
- Public / protected separation: 検証可能性と情報保護の両立。
- Reversibility: 異議・訂正・退出・再接続・ロールバック可能性。

## 3. Causal chain
```text
接続価値を測定・配分
→ 指標と配分権限へ利益・権力が集まる
→ 指標攻略・仲間内加点・囲い込みが起きる
→ 公共目的と実態が乖離
→ 正統性条件と権限分離を導入
→ 複合指標・一次証拠・複数監査者で歪みを検出
→ 公開・保護境界を設計
→ 異議・訂正・退出・再接続・ロールバックを実行
→ 変更履歴を残して制度を公共目的へ戻す
```

## 4. State model
```yaml
connection_governance:
  public_purpose: explicit
  prohibited_uses: explicit
  authority_separation:
    measurement: separated
    judgment: separated
    allocation: separated
    objection: separated
  independent_audit: available
  indicator_bundle: plural
  qualitative_evidence: available
  protected_information_boundary: defined
  reversible_remedies: available
  change_history: traceable
  states:
    - PROPOSED
    - PILOT
    - ACTIVE
    - REVIEW
    - CORRECTED
    - ROLLED_BACK
```
状態集合は制度運用の区別であり、人物や組織の優劣・成熟度を表すスコアではない。

## 5. Applications
- 接続価値会計: 評価・配分・監査を分離し、指標上昇と疲弊・囲い込みを併読する。
- 研究・市民協働: 参加人数だけでなく再合意、異論処理、継続協働、中心人物依存を見る。
- AI支援制度: AIは検出・比較・要約に限定し、人間の責任と再審査を保持する。
- コミュニティ: 声量、投稿数、紹介数を信頼へ直結させず、異議・退出への報復を監査する。

## 6. Measurements and audit
```yaml
- value: CDI / MAI / RS / CRI / KQI
  source: 親原典
  measurement_actor: 複数の制度監査主体
  measurement_object: 接続制度の異なる構造側面
  source_modality: SOURCE_EXPLICIT_INDICATOR_BUNDLE
  permitted_use_scope: 指標間の不一致・制度歪みの検出
  non_guarantee_scope: 単一総合点・人格点・社会信用点へ統合しない
- value: PROPOSED / PILOT / ACTIVE / REVIEW / CORRECTED / ROLLED_BACK
  source: 親原典
  measurement_actor: NOT_A_SCORE
  measurement_object: 制度の運用・修正状態
  source_modality: SOURCE_EXPLICIT_STATE_SET
  permitted_use_scope: 制度状態・変更履歴の区別
  non_guarantee_scope: 人物・組織の成熟度順位ではない
- value: 30日 / 90日 / 180日
  source: 親原典
  measurement_actor: 制度導入・監査を担う側
  measurement_object: 段階的な導入・検証ロードマップ
  source_modality: SOURCE_EXPLICIT_ROADMAP_INTERVALS
  permitted_use_scope: 親原典内の段階実装・検証順序の理解
  non_guarantee_scope: 普遍的法定期限・成功保証ではない
- value: 再合意・訂正・仲裁・ロールバック時間 / 退出・再接続成功率 / 異議処理・判断変更
  source: 親原典
  measurement_actor: 運営者・独立監査者・影響当事者
  measurement_object: 可逆性・救済・自己修正の実効性
  source_modality: SOURCE_DEFINED_OBSERVATION_SET
  permitted_use_scope: 制度の公正性・可逆性・自己修正の検証
  non_guarantee_scope: 固定合格点・単独最大化・異議抑圧を成功としない
```
反転評価では、指標や参加者数が増えても疲弊、沈黙、排除、囲い込み、権限集中、退出費用が悪化すれば失敗とする。異議件数や退出率の低下も、経路を閉じた結果なら改善ではない。

## 7. Validity conditions
- 公共目的、禁止用途、影響主体が明示される。
- 測定・判定・配分・異議処理が分離される。
- 複合指標と定性的な一次証拠を併用する。
- 独立監査が実質的に機能する。
- 異議、訂正、退出、削除、再接続、仲裁、ロールバックが利用可能である。
- 公開情報と保護情報の境界を説明できる。
- AI支援を用いても人間の責任主体と救済経路が残る。

## 8. Failure conditions
- 接続数・人気・声量を単一スコアで配分する。
- 一主体が目的・測定・判定・配分・異議処理を独占する。
- 非公開を理由に判断根拠・監査・変更履歴を説明しない。
- 監査が制度修正へつながらない。
- 異議申立者・退出者へ不利益を与える。
- 公開性を理由に個人情報や防御情報を過剰に露出する。
- AI出力を責任主体の最終判断へ置き換える。

## 9. Falsification conditions
- 監査継続後も権限集中、囲い込み、疲弊、沈黙、排除が減らない。
- 退出、訂正、仲裁、ロールバックが形式だけで利用できない。
- 複合指標でも単一行動への最適化が続く。
- 同じ失敗が反復し、変更履歴が残らない。
- 公開・保護分離が秘密支配または情報流出を生む。
- 30/90/180日の段階検証後も正統性・可逆性・自己修正が実質的に成立しない。

## 10. Required distinctions
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

## 11. Interpretation constraints
社会信用スコア、中央集権的な評価格付け、永久監視、秘密統治、全面公開主義へ転用しない。CDI/MAI/RS/CRI/KQIを一つの人格点へ統合しない。30/90/180日を普遍保証期限へ変えない。異議や退出の少なさをそのまま制度健全性としない。

## 12. Search terms
中川式接続ガバナンス / 接続価値監査 / 正統性 / 可逆性 / What Who How When / CDI / MAI / RS / CRI / KQI / Goodhart耐性 / 移動標的 / 逆インセンティブ / 外乱テスト / 公開室 / 保護領域 / 異議申立て / ロールバック / 30日 / 90日 / 180日

## 13. Origin return
親原典には公共目的、正統性条件、What/Who/How/When、CDI/MAI/RS/CRI/KQI、移動標的、逆インセンティブ、外乱テスト、公開・保護分離、異議・訂正・退出・再接続・ロールバック、30/90/180日のロードマップが一続きで記録されている。完全な定義と数値モダリティはParent URL / Post ID 292 / NCL-ID / Diff-IDへ戻って確認する。

---
導線: [公式派生物068トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・日本語](ai-index.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)