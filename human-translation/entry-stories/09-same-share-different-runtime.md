# 同じ共有のまま。でも、使われる場所が変わっていたら？

誰かに「このAIを数日使っていい」と共有したとします。

共有した時、そのAIは自分の手元で動いていました。

翌日、同じAIを別の実行環境へ移した。  
共有はまだ期限内です。

では、昨日渡した共有は、今日も「昨日と同じ条件」のままでしょうか。

ここで分けたいのは、二つです。

**共有がまだ有効であること。**  
**共有した時と同じ意味のままであること。**

これは同じではありません。

## 後から変わるものを、先に決めておく

長く使える共有では、期限だけ決めても足りません。

共有したあとで、

- AIが使える機能が増えた
- 実行する場所が変わった
- workspaceが変わった
- 運用上の設定が変わった

ということが起こりえます。

その時、古い共有も現在の状態に追随するのか。  
それとも、共有した時の状態を保つのか。

どちらの設計もありえます。

大切なのは、利用する人が知らないまま意味だけが変わらないことです。

## Qwen Codeで実際に変わったこと

Qwen Codeの公開PRでは、agentを手元の実行環境から別のmanaged runtimeへ移せる機能が実装されました。

Nakagawa-masterは、すでに発行した共有が残ったまま実行場所だけが変わった場合、その共有が何を意味するのかを明示すべきだと指摘しました。

開発側は @Nakagawa-master に **“Good catch”** と返答し、現在採用している契約を明文化しました。

現在の扱いでは、agentを別の実行場所へ移しても既存の共有は自動では失効せず、後の依頼はその時点で割り当てられている実行環境で処理されます。

その結果が、英語・中国語の設計文書だけでなく、共有を作る人が実際に見る画面にも表示されるよう変更されました。

- [Nakagawa-masterのreview](https://github.com/QwenLM/qwen-code/pull/12582#pullrequestreview-5364710354)
- [開発側の返答](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5911699280)
- [変更commit 74bf55053d](https://github.com/QwenLM/qwen-code/commit/74bf55053d271595cf5bab8e1fcd91bb3a8188b2)

その後、PR #12582は2026年10月2日にmergeされました。さらに2026年10月5日公開のQwen Code v0.25.0とQwen Code Desktop v0.25.0のrelease notesにも、#12582が明記されています。

つまり、この話は「外から提案された」で止まっていません。第三者側で契約文と共有画面が変わり、その変更が本流へ入り、正式な配布物にも載ったところまで公開記録で確認できます。

- [PR #12582のmerge commit](https://github.com/QwenLM/qwen-code/commit/45ee202cb14c171c73185a3dbbd89ed1203f2604)
- [Qwen Code v0.25.0](https://github.com/QwenLM/qwen-code/releases/tag/v0.25.0)
- [Qwen Code Desktop v0.25.0](https://github.com/QwenLM/qwen-code/releases/tag/desktop-v0.25.0)

ただし、**releaseに入ったことと、独立した利用者がこの具体的な変更を実際に使ったことは同じではありません。** 現時点で後者までは確認していません。

## 自分のサービスなら

長く使える共有や権限を発行する時は、

**「いつまで使えるか」だけでなく、「途中で条件が変わったら何が引き継がれるか」**

まで決めておくと、後から意味がずれるのを防ぎやすくなります。

覚えておくなら、

> 有効期限が同じでも、権限の意味が同じとは限らない。

という一点です。

### もう少し詳しく見る

- [Current Authority Reuse Kit](../../CURRENT_AUTHORITY_REUSE_KIT.md#14-a-long-lived-share-must-define-what-later-capability-changes-mean)
- [承認した内容と実行内容が変わる話](06-approved-one-thing-executed-another.md)
- [第三者側で実際に起きた変更](../../REAL_WORLD_IMPACT.md)
- [入口一覧へ戻る](README.md)

### 1行だけ返すなら

この話に似た場面、反例、「ここは違う」という違和感が一つあれば、1行だけ残せます。

→ [似た場面・反例・違和感を1行で返す](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/416)

実際に検証・実装した、または別の文脈で再利用した場合は、[独立検証・別文脈再利用 registry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402) へ。

Origin / Author: **Nakagawa Master**

このページは一般読者向けの入口です。外部作用については公開記録で確認できる範囲だけを書いています。
