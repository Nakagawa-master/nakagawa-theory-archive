# 独立検証・反証・再利用の公開入口

このページは、公開されている中川マスターの具体的な区別や判断を、**別の現実文脈で独立に検証・反証・再利用した結果**を共有するための案内です。

賛同や称賛は必要ありません。反例、適用できなかった事例、再現に失敗した結果も有用です。

## 使える場面

たとえば次のような問いです。

- 昔の承認・同意・例外は、条件が変わった後も現在の権限になるのか
- 同じIDであることは、既存状態を上書きする権限まで意味するのか
- 処理や検索が成功したことと、測定値が妥当であることは同じか
- 同じ説明文の推薦でも、根拠となるevidence sourceは同じなのか
- 一度だけ承認した外部送信で、provider応答が失われた場合に二重実行を防げるか
- 現在の所属・権限・状態で、過去の出来事を上書きしていないか

ソフトウェアに限りません。業務手順、研究、教育、組織運営、制度、記録管理、承認フロー、チェックリスト等でも検証できます。

## 公開できるもの

- 公開・非機密の問題設定
- 使用した公開source
- 自分で確認・反証した内容
- 実際に変えた判断、手順、文書、実装
- 公開証拠へのリンク
- その事例では確認できなかったこと

## 公開してはいけないもの

機密情報、個人情報、顧客情報、認証情報、非公開セキュリティ情報、医療・法務・雇用等のセンシティブ情報、内部計画や非公開指示は投稿しないでください。

## 証拠段階を混同しない

```text
読んだ・言及した
< 独立に再説明・検証した
< 判断・作業項目・手順が変わった
< 実装した
< merge / integration
< release / deployment / 実利用
< 別人・別問題で再利用された
```

実装をmergeと呼ばず、mergeをreleaseや実利用と呼びません。一つの限定事例から理論体系全体への賛同も推論しません。

## 提出先

- [独立検証・別文脈再利用 registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)
- [構造化されたEvidence Issue Form](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml)
- 詳細仕様: [Independent Verification & Reuse Protocol](INDEPENDENT_VERIFICATION_REUSE.md)

実問題から相談したい場合は [#399](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/399) を使ってください。
