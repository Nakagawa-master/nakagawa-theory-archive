# 「承認しました」──でも、その後で中身が変わっていたら？

AIに有料処理をさせる前に、画面へ確認内容が出た。

対象はA。  
設定はX。  
金額も確認した。

人間が「承認」を押した。

ここまでは普通です。

でも、そのあと実行直前に対象がBへ、設定がYへ変わっていたら？

システムに残っているのは「承認済み」。

人間が実際に見たのはA/X。

実行されるのはB/Y。

それでも、同じ承認を使ってよいでしょうか。

---

## 「誰がOKしたか」だけでは足りない

承認記録には、

- 誰が押したか
- いつ押したか

が残っているかもしれません。

でも、本当に必要なのはもう一つです。

**何にOKしたのか。**

人間が見た内容と、実際に動く内容が同じでなければ、「人間が承認した」という形式だけが残ります。

## たった1件の追加でも、意味は変わる

100件の送信先を見てOKした。

そのあとデータが更新され、101件目が増えた。

「一件くらい」と思うかもしれません。

でも、その一件を許す仕組みなら、どこまでが人間の判断だったのか後から分からなくなります。

大事なのは件数ではありません。

**人間が見た具体的な状態と、機械が動かす具体的な状態が結びついているか。**

## どう守るか

一つの方法は、

1. 実行内容を具体的なsnapshotにする
2. その内容からdigestを作る
3. 人間の承認をそのdigestへ結びつける
4. 実行直前にもう一度同じ内容か確認する
5. 変わっていたら古い承認を使わない

という形です。

「承認した」というラベルではなく、**承認したものそのもの**を固定します。

## これはQwen Codeで実装・merge・releaseまで進んだ

Qwen Code PR #12492で Nakagawa-master は、有料Batch APIについて、

- exact item set
- frozen settings
- cost estimate

を具体的なsnapshotへ束ね、承認後に内容が変われば古い承認を無効にする境界を提案しました。

第三者developerは提案を出所付きで採用し、preview、snapshot digest、実行直前の再照合とregression testsを実装しました。

PRは2026-09-26 JSTにmergeされ、同日 Qwen Code v0.24.6 としてreleaseされています。

- [Nakagawa-masterの公開コメント](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5817569552)
- [第三者developerの採用応答](https://github.com/QwenLM/qwen-code/pull/12492#issuecomment-5818159716)
- [implementation commit](https://github.com/QwenLM/qwen-code/commit/3d06e1ad8e749c647a2eb5d447b867fc50955a13)
- [merged PR #12492](https://github.com/QwenLM/qwen-code/pull/12492)
- [v0.24.6 release](https://github.com/QwenLM/qwen-code/releases/tag/v0.24.6)

PR全体や後続修正を一人の成果とはしません。ここで確認できるのは、**この承認境界が出所付きで採用され、具体的な実装とtestへ入り、merge/releaseされたこと**です。

## この一文を持って帰る

> 「承認済み」と「この実行内容を承認した」は同じではない。

これはAIだけでなく、送金、発注、配信、削除、権限変更にも置けます。

## 次に読む

- [承認を実行内容へ結びつける公開チェック](../../PAID_ACTION_APPROVAL_BINDING_CHECKLIST.md)
- [エラー後の再試行が二重実行を作る話](01-double-charge-after-error.md)
- [AIが候補を作り、人間が最後に選ぶ話](03-ai-made-the-menu.md)
- [第三者projectで実際に変わった公開記録](../../REAL_WORLD_IMPACT.md)
- [7つの入口へ戻る](README.md)

## この一枚から、どこまで広がるか

ここで分けたのは「承認したという記録」と「この具体的な実行内容を承認したという事実」です。

この境界は、Qwen Codeの有料Batch APIで出所付きの提案として採用され、実装・regression tests・mergeを経てv0.24.6 releaseまで進みました。

つまり、このページで読んだ区別は、抽象的な心得だけではなく、**第三者の実装境界として実際に使われた公開記録**があります。

同じ問いは、送金、発注、メール配信、削除、権限変更、AI agentの外部作用にも置けます。

**中川マスターという人を知る**  
→ [3分で読む人物入口](../who-is-nakagawa-master.md)

**他の第三者作用も確認する**  
→ [Real-World Impact](../../REAL_WORLD_IMPACT.md)

**別の物語へ横移動する**  
→ [7つの物語入口](README.md)

**正式な理論・実務資料へ降りる**  
→ [公式派生物・再利用資料を探す](../../derivatives/CATEGORIES.md)

**最新の短い投稿を追う**  
→ [Bluesky｜@masterjp.bsky.social](https://bsky.app/profile/masterjp.bsky.social)

Origin / Author: **Nakagawa Master**

このページは一般読者向けの公開翻訳面です。外部作用は公開記録で確認できる範囲だけを記述しています。
