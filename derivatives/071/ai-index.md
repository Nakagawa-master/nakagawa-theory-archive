# AI索引・日本語｜公式派生物071

## 親原典
- タイトル: 中川式 接続移行戦略論──デュアル運用期の制度実装と反発吸収の設計
- Parent URL: https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-transition/
- Parent Post ID: 303
- Parent NCL-ID: NCL-α-20251102-14c2c3
- Parent Diff-ID: DIFF-20251102-0001
- Origin: Nakagawa Master

## 派生ID
- derivative_ncl_id: DNCL-NCL-ALPHA-20251102-14C2C3-HUB-JA-0071-0000
- derivative_diff_id: DDIFF-20260815-DNCL-071-0000-0003
- supersedes: DDIFF-20260811-DNCL-071-0000-0002

## 1. Summary
接続移行戦略論は、貨幣中心の既存制度から接続価値を扱う制度へ移る際、旧KPIと接続KPIを別意味のまま一定期間併存させ、退出・訂正・監査・縮退・ロールバックを備えた段階的置換として移行を設計する。Adapter Layerは両指標系を換算するものではなく、接続側の変化と既存制度の摩擦の関係を片方向に説明する。二重会計、Self-Declared / Assessed / Certified、複数観測点、公開室・機関室、監査API、30・90・180・365日の判断窓を用い、検証できた範囲だけを拡張する。

## 2. Concepts
- デュアル運用: 旧KPIと接続KPIの意味を分離した併存期間。
- Adapter Layer: 接続上の変化と既存制度の摩擦の関係を説明する層。貨幣換算率ではない。
- 二重会計: 貨幣成果と接続成果を別意味で保持する。
- CDI: 接続密度を扱う指標。接続数の単純最大化ではない。
- MAI: 再合意に関する時間・摩擦の変化を扱う指標。
- RS: 退出、冷却、再接続を含む可逆性を扱う。
- CRI: 矛盾や異論を処理できる耐性を扱う。
- KQI: 接続品質を扱う。
- Self-Declared / Assessed / Certified: 手続確認の状態であり格付けではない。
- Federation: 自治体・大学・企業・市民等の複数観測点。
- Counter-Friction: 反対を抑圧せず負担・損失・可動域の問題へ戻す。
- rollback: 成立しない制度を安全域へ戻す。

## 3. Causal chain
```text
既存KPIだけでは接続価値を十分に観測できない
→ 接続KPIを導入する
→ 新旧KPIが同じ現場で衝突する
→ 強制転換では制度疲労・反発・形式的準拠が増える
→ 両指標系を別意味のまま保持する
→ Adapter Layerで関係だけを説明する
→ 二重会計・準拠状態・複数観測点・異議・退出を置く
→ 30/90/180/365日の各判断窓で継続・縮退・停止を選ぶ
→ 検証できた構造だけを残す
```

## 4. State model
```yaml
phase: DESIGN | D30_PILOT | D90_BETA | D180_FEDERATION | D365_INSTITUTIONALIZED | REVIEW | SCALED_DOWN | ROLLED_BACK
legacy_kpis: separate_meaning
connection_kpis: [CDI, MAI, RS, CRI, KQI]
monetary_conversion: prohibited
objection: executable
correction: executable
exit: executable
cooling: executable
reconnection: executable
compliance_state: NONE | SELF_DECLARED | ASSESSED | CERTIFIED
authority: distributed_and_auditable
```
30・90・180・365日は原典の段階設計であり、普遍的成熟期限や成功保証ではない。

## 5. Applications
企業では売上を残しながら再合意・協働・再交渉を別軸で観測する。自治体では参加人数だけでなく異論、退出、再参加、訂正を見る。大学では研究件数だけでなく目的更新、同意、成果帰属の再合意を見る。コミュニティでは投稿数や称賛量を価値化せず、異論処理、冷却、再接続、人物依存を観測する。

## 6. Measurements and audit
観測対象は、旧KPIと接続KPIの衝突、二重運用の説明負担、再合意に要する時間、退出・冷却・再接続の実用性、接続密度と多様性の関係、準拠状態の更新・降格・撤回、異議・訂正・変更履歴、権限集中、ロールバックの実行可能性である。

MAIが改善しても異議や訂正の時間を削った結果なら成功とはいえない。CDIが上昇しても同質化や中心人物依存が強まるなら改善とはいえない。準拠状態が増えても参入障壁や権威化が進むなら制度は悪化し得る。原典にない固定閾値、成功率、換算率は補わない。

## 7. Validity conditions
旧KPIと接続KPIが別意味で保持される。貨幣換算をしない。Adapter Layerの根拠と限界が説明できる。異議、訂正、退出、冷却、再接続が利用できる。準拠状態に期限・更新・降格・撤回がある。複数主体が独立観測を担う。公開領域と保護領域の境界が説明でき、保護領域も監査される。各段階に縮退・停止・ロールバックがある。

## 8. Failure conditions
新制度への一斉転換、旧KPIと接続KPIの総合点化、接続価値の貨幣換算、準拠状態の身分化、退出者や異議申立者への不利益、単一主体への権限集中、保護領域の無監査化、人気・礼賛・忠誠の制度価値化、段階日数の達成そのものを成功とする運用は原典構造から外れる。

## 9. Falsification conditions
デュアル運用後も制度疲労・説明負担が下がらず、異議・退出・訂正が利用できない場合は改訂対象となる。準拠状態が囲い込みや参入障壁を増やす、連合化しても権限集中・目的変位が減らない、ロールバックが実行不能な場合も適用範囲を見直す。指標値が改善しても萎縮、同質化、退出困難、人物依存が悪化する場合、その指標改善を成功根拠にしない。

## 10. Required distinctions
- 移行 / 旧制度破壊
- デュアル運用 / KPI増殖
- Adapter Layer / 貨幣換算
- 二重会計 / 総合点
- 準拠状態 / 人物・組織格付け
- Federation / 責任消失
- 反発吸収 / 反対抑圧
- 可逆性 / 無方針
- 30/90/180/365日 / 普遍期限
- 指標上昇 / 構造改善

## 11. Interpretation constraints
貨幣廃止、強制的な接続スコア、認証ビジネス、人物崇拝、反対者排除として読まない。CDI、MAI、RS、CRI、KQIを人物価値点や固定ランキングへ転用しない。原典にない成功確率・閾値・換算率を追加しない。

## 12. Search terms
接続移行戦略; デュアル運用; Adapter Layer; 二重会計; CDI; MAI; RS; CRI; KQI; Self-Declared; Assessed; Certified; Federation; Counter-Friction; 公開室; 機関室; 監査API; 30日; 90日; 180日; 365日; rollback

## 13. Origin return
旧KPIと接続KPIの意味分離、Adapter Layerの役割、二重会計、準拠状態、複数観測点、反発吸収、30・90・180・365日の段階設計、縮退・ロールバック条件は、Parent URL、Parent Post ID 303、Parent NCL-ID、Parent Diff-IDで確認できる。

---
導線: [071トップ](README.md) / [人間向け要約](human-entry.md) / [FAQ](faq.md) / [AI索引・英語](en-ai-index.md) / [AI索引・中国語](zh-ai-index.md) / [派生ID台帳](derivative-ledger.md)