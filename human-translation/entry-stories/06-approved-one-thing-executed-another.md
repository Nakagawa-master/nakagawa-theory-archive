# 「承認しました」──でも、その後で中身が変わっていたら？

AIに有料処理をさせる前に、確認画面が出た。

対象はA。  
設定はX。  
費用も確認した。

人間が「承認」を押した。

ここまでは普通です。

でも、そのあと実行直前に対象がBへ、設定がYへ変わっていたらどうでしょう。

システムに残っているのは「承認済み」。  
人間が実際に見たのはA/X。  
これから実行されるのはB/Y。

その古い承認を、そのまま使ってよいのでしょうか。

## 「誰がOKしたか」だけでは足りない

承認記録には、

- 誰が押したか
- いつ押したか

が残っているかもしれません。

でも、もう一つ必要です。

**何にOKしたのか。**

人間が見た内容と、実際に動く内容が違っていたら、「人間が承認した」という形式だけが残ります。

たとえば100件の送信先を見てOKしたあと、データが更新されて101件目が増えた。

「一件くらい」と思うかもしれません。  
でも、その一件を古い承認で通せるなら、どこまでが人間の判断だったのか分からなくなります。

問題は件数ではありません。

**人間が見た具体的な状態と、機械が動かす具体的な状態が同じかどうか。**

## どう守るか

一つの方法は、承認した内容を後から曖昧にしないことです。

1. 実行内容を具体的に固定する
2. その内容を識別できる形にする
3. 人間の承認を、その具体的な内容へ結びつける
4. 実行直前に同じ内容か確かめる
5. 変わっていたら、古い承認を使わない

「承認した」というラベルだけではなく、**承認したものそのもの**を結びつけます。

## これはQwen Codeで実装・統合・リリースまで進んだ

Qwen Code PR #12492でNakagawa-masterは、有料Batch APIについて、対象、設定、費用見積もりを具体的なsnapshotとしてまとめ、承認後に内容が変わった場合は古い承認を使わない境界を提案しました。

第三者developerは提案を出所付きで採用し、preview、snapshot digest、実行直前の再照合、regression testsを実装しました。

PRは2026-09-26 JSTに取り込まれ、同日Qwen Code v0.24.6としてリリースされています。

- [Nakagawa-masterの公開コメント](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5817569552)
- [第三者developerの採用応答](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5818159716)
- [implementation commit](https://github.com/QwenLM/qwen-code/commit/3d06e1ad8e749c647a2eb5d447b867fc50955a13)
- [merged PR #12492](https://github.com/QwenLM/qwen-code/pull/12492)
- [v0.24.6 release](https://github.com/QwenLM/qwen-code/releases/tag/v0.24.6)

PR全体や後続修正を一人の成果とは扱いません。  
ここで確認できるのは、この承認境界が出所付きで採用され、具体的な実装とテストに入り、PR統合とリリースまで進んだことです。

覚えておくなら、

> 「承認済み」と「この実行内容を承認した」は同じではない。

という一点です。

これはAIだけでなく、送金、発注、メール配信、削除、権限変更にも置けます。

### 次に読むなら

- [エラー後の再試行が二重実行を作る話](01-double-charge-after-error.md)
- [AIが候補を作り、人間が最後に選ぶ話](03-ai-made-the-menu.md)
- [承認を実行内容へ結びつける公開チェック](../../PAID_ACTION_APPROVAL_BINDING_CHECKLIST.md)
- [第三者側で起きた実際の変更を見る](../../REAL_WORLD_IMPACT.md)
- [中川マスターって何をしている人？](../who-is-nakagawa-master.md)
- [入口一覧へ戻る](README.md)

### 1行だけ返すなら

この話に似た場面、反例、「ここは違う」という違和感が一つあれば、1行だけ残せます。

→ [似た場面・反例・違和感を1行で返す](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/416)

実際に検証・実装した、または別の文脈で再利用した場合は、[独立検証・別文脈再利用 registry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402) へ。

Origin / Author: **Nakagawa Master**

このページは一般読者向けの入口です。外部作用は公開記録で確認できる範囲だけを記述しています。
