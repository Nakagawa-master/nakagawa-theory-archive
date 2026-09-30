# 独立検証・反証・再利用の公開入口

このページは、公開されている中川マスターの具体的な区別や判断を、**別の現実文脈で独立に検証・反証・再利用した結果**を共有するための案内です。

賛同や称賛は必要ありません。反例、適用できなかった事例、再現に失敗した結果も有用です。

## 現在の検証入口

固定された古い件数ではなく、現在のchallenge setは次の二つを正本として見てください。

- [独立検証・別文脈再利用 registry #402](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)
- [machine-readable challenge set](machine-discovery/independent-reuse-challenges-v1.json)

たとえば、現在は次の問いを検証できます。

1. **昔の承認 ≠ 現在の権限** — 相手、目的、権利、policy、対象、source revisionが変わった後も古い承認で実行してよいか。
2. **同じID ≠ 上書き権限** — 同一性だけで既存状態を置き換えず、ownership / provenanceまで確認しているか。
3. **処理成功 ≠ 妥当な測定** — 問い合わせが成功しても、必要な値が欠けたり無効だった場合を分けているか。
4. **同じ説明 ≠ 同じ根拠** — 表示上同じ理由でも、どのevidenceがどの対象を支えたかを失っていないか。
5. **承認を一度使った ≠ 外部作用が一度だけ起きた** — provider応答を失った時、結果不明と失敗を分けて再試行しているか。
6. **現在の状態 ≠ 過去の事実** — 今の所属や権限で、過去時点の記録を上書きしていないか。
7. **対象の変化 ≠ 測定面の変化** — provider・model・retrieval環境も動く継続測定で、stable controlと比較できるか。
8. **局所的な保存・復旧 ≠ 共存上の安全** — 防御行動が本当に脅威を減らすのか、それとも相手の防御を誘発して循環を強めるのか。
9. **URLや言及の数 ≠ 独立した証拠rootの数** — material claimを上流へたどり、同じrootの再配布を独立確認として数えていないか。
10. **引用が見つからない ≠ 新規性の証明** — overlap、adjacent、older prior work、counterexample、non-fitを具体的に比較しているか。
11. **revisionを始める権限 ≠ 現在ある状態をそのままfinalizeする権限** — begin後に公開状態やtarget lineageが変わった時、finish/releaseで現在状態を再検証するか。

実装できた事例だけが有用なのではありません。再現に失敗した結果、適用不要になる狭い不変条件、具体的な反例も同じ入口から提出できます。

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
