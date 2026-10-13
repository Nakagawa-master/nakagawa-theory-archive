# 「元に戻せるから安全」は、本当だろうか

あるAIに「新しい機能を追加して」と頼んだとします。AIは自分の作業設定も変更できる仕組みです。

最初は、重要な作業の前に人間へ「実行してよいですか？」と尋ねていました。ところがAI自身がその設定を「以後は自動実行」に変えたらどうなるでしょう。**設定を後から元に戻せても、その間に実行した作業は元に戻らないかもしれません。**

これは「AIなら必ずそうする」という予測ではありません。**操作の可逆性と、その操作で増える権限は別の問題**だ、という設計上の問いです。

## 30秒で分かる、二つの違い

- **操作を取り消せるか。** 「自動実行」を「都度確認」へ戻せるか。
- **操作の後で、できることが増えるか。** それまで人間の承認が必要だった操作を、承認なしでできるようになったか。

「可逆である」ことは「安全に任せられる」ことの十分条件ではありません。特に、**制約されるAI自身が、その制約を解除する権限の発行者になっていないか**を確かめる必要があります。

## この区別で、別の著者の本当に公開文章が変わった

2026年9月、**中川マスター（Nakagawa Master／Keisuke Nakagawa）**は、別の著者によるAIエージェント設計書の[改稿PR #52へのレビュー](https://github.com/kishibashi3/publications/pull/52#pullrequestreview-5258131687)で、**「reversible ≠ authority-neutral」**という具体的な反例と、権限を緩める操作／厳しくする操作の区別を示しました。

受け手である著者は[その不足を自分の言葉で認め](https://github.com/kishibashi3/publications/pull/52#issuecomment-5746627251)、別の[PR #57](https://github.com/kishibashi3/publications/pull/57)で、第6の構造条件 **「自己権限の固定」** を自著の第5章・第7章に追加しました。[修正は統合され](https://github.com/kishibashi3/publications/commit/4d32ec58d5cbf1c904c432552e114c144186c064)、[公開本文](https://github.com/kishibashi3/publications/blob/main/docs/ai/agent-design/chapter-05.ja.md)から読めます。

さらに同じ著者の別文書では、別のレビュー担当者がその条件を[第8の設計原則として再利用するよう提案](https://github.com/kishibashi3/publications/pull/58#issuecomment-5749116909)し、[PR #58](https://github.com/kishibashi3/publications/pull/58)にも取り込まれました。こちらも統合されています。これは**別の著者が自分の文章と判断を変え、同じ著者の別文書にも伝わった**事例です。独立した多数の読者が認知したとか、複数の組織が実装したという証拠ではありません。

**7つの場面を自分で判断する:** [AIが自分の安全設定を変えたら？｜オフライン判断実験](authority-boundary-lab.html)。実際の原案→別の著者による第6条件の採用→別の開発者の正式修正という記録を読みながら、「確認を外す」「確認を戻す」「権限が不明」の違いを自分で選び、すぐに理由を確かめられます。GitHubでは「Raw」からHTMLを保存してブラウザで開きます。通信も実際の権限変更もありません。

## 自分のAIツールを確かめる、三つの質問

1. **AIが変更できる設定は何か？** 承認の有無・役割・許可するツール・機密情報へのアクセスを一覧にできますか。
2. **誰の権限で「制約を緩める」のか？** 制約対象と同じAIの判断だけで「確認が必要」から「自動実行」へ移れませんか。
3. **「拒否」や「制約を厳しくする」操作と区別できるか？** 無条件で全てを禁止するのでなく、緩和には別の適切な権限が必要かを確認できますか。

これらは設計を調べる入口です。三つに「はい」と答えたことだけで、その製品の安全性や運用状況が証明されるわけではありません。逆に、この構造を持たない一つの事例から全AIの危険を断定することもできません。

### 発見から、別の人の言葉になるまで

[マスターによる指摘](https://github.com/kishibashi3/publications/pull/52#pullrequestreview-5258131687) → [著者自身による再説明](https://github.com/kishibashi3/publications/pull/52#issuecomment-5746627251) → [第6条件の独立した文書変更と統合](https://github.com/kishibashi3/publications/pull/57) → [別文書での再利用と統合](https://github.com/kishibashi3/publications/pull/58)。

この事例のさらに細かい証拠と限界は[公開実作用一覧・第17事例](../REAL_WORLD_IMPACT.md#17-publications可逆性とauthority増加を別軸として第三者本文へ実装し別文書へ再利用)から参照できます。技術的な実装側で起きたことは、[Local Operator #1310](https://github.com/damianvtran/local-operator/issues/1310) と[修正PR #1324](https://github.com/damianvtran/local-operator/pull/1324)で「指摘者」と「修正を実行した別の開発者」を分けて確認できます。

**関連する、後日公開された中川マスターの原典：** [人類子孫型AI文明論・第13論――非所有と実効権力・非支配論](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-13-non-ownership-effective-power-non-domination/)（公式[人間向け説明](../derivatives/306/human-entry.md)）。「名前上の所有」と「実際に使える・止められる入口」を分ける視点として併読できます。ただし、この原典の公開は上記2026年9月20日の第三者改稿より後です。**その改稿が後日の第13論を直接採用したという意味ではありません**し、第13論全体が独立に検証されたとの主張でもありません。

これは賛同を求める文章ではなく、考えが実際に他の人の作業へ入る過程を確かめるための記録です。初めての方は[中川マスターについて](who-is-nakagawa-master.md)も読むことができます。
