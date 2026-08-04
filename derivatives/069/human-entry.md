# 人間向け要約｜公式派生物069

Parent: https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-protocol/ / NCL-α-20251102-9426e0 / DIFF-20251102-0001 / Origin: Nakagawa Master

## 15秒説明
CXPは、接続を組織ごとの閉じた関係から、同意・記憶・退出・再接続を保ったまま持ち運べる社会資産へ変える最小標準である。

## なぜそうなるのか
会計とガバナンスがあっても、各組織が別々のID、同意、ログ、退出条件を持てば相互運用できず、接続は島宇宙化する。そこでSubjectID、RelationID、ConsentToken、MemoryObject、ReversibilityFlag、VisibilityClassを共通語彙にし、発見から再接続までを標準化する。

## 実務工程
1. 接続目的と境界条件を公開する。
2. 主体と関係へIDを付与するが、人格追跡には使わない。
3. 範囲・期間・目的を含むConsentTokenを生成する。
4. 合意要旨と証跡をMemoryObjectへ保存する。
5. CDI・MAI・RS・CRI・KQIへの読み取りポートを設ける。
6. 離脱、冷却、再接続をReversibilityFlagで管理する。
7. 公開室・機関室・私的領域をVisibilityClassで分離する。
8. 監査API、証人ノード、濫用検知でガバナンスへ接続する。

## 適用例
研究連携、自治体と市民の協働、オンラインコミュニティ、AIを含む協働ネットワークで、同意の再確認、退出、再接続、監査を共通形式にできる。

## 成功判定
再合意時間と同意破綻率が下がり、退出・再接続が実際に機能し、独自規格間でも最低限の意味と証跡が失われず、監視や権力集中が増えないこと。

## 限界
標準は社会関係のすべてを表現できない。項目を増やしすぎれば参加コストが上がり、少なすぎれば意味が失われる。段階導入と反証可能性が必要である。

## 誤読防止
中央ID制度、包括同意、永続追跡、社会信用スコア、データ無制限共有ではない。標準は接続の自由と相互運用を守る最小の約束である。

---
導線: [069トップ](README.md) / [公式派生物トップ](../README.md) / [FAQ](faq.md) / [AI-JA](ai-index.md) / [AI-EN](en-ai-index.md) / [AI-ZH](zh-ai-index.md) / [台帳](derivative-ledger.md)