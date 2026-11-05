# 「AIは成功した」と言った。でも、実際は違った。──中川マスターの指摘を、別の開発者たちが現実の修正へ変えた話

**専門用語を知らなくても、30秒で分かる記録。** 中川マスター（Nakagawa Master／公開個人名 **Keisuke Nakagawa**）は、構造・因果・成立条件について独立した原典を著している理論家です。世界で使われるAIソフトウェアの公開議論で、**見た目の正しさと、本当に成立した動作を取り違える条件**をソースから具体的に見つけ、**別の開発者が自分の判断で実装・テスト・マージした**事例があります。

> **「修正した」と書いてあるから、あなたの仕事も安全になったとは限らない。では、誰が何を確かめ、誰が何を本当に変えたのか？**

## 外部技術メディアが採用することにも意味がある

[The Daily AI Pulse](https://daily-ai-pulse-db253.web.app/stories/2026-10-26-qwen-review-integrity/)はAIの開発現場で使える情報を、原資料・証拠区分・編集判断を経て紹介する出版プロジェクト。今回は、本人の投稿したQwenレビューの問題を、**外部編集者が選んで独自の記事へ仕上げ、英語とフランス語で実際に本番配信**しました。[媒体の編集基準](https://github.com/GadDev/daily-ai-pulse/blob/main/docs/EDITORIAL.md)、[編集者がマージしたPR](https://github.com/GadDev/daily-ai-pulse/pull/253)、[受け手側の配信成功記録](https://github.com/GadDev/daily-ai-pulse/actions/runs/40332697382)が残ります。**何が第三者による独立の判断なのか、どの部分が本人の企画提出だったのか、媒体自身の価値がどこにあるのか**を[30秒で把握できる独立掲載記録](INDEPENDENT_MEDIA_COVERAGE.md)にまとめました。これは大手報道機関への掲載や読者数の保証ではありません。

## まず三つの現実の変更

**1. AIが使う道具の名前が重なった。関係ない道具まで消えた。** [Qwen Codeの実際の利用者報告](https://github.com/QwenLM/qwen-code/issues/15741)に対して、マスターは「名前が重複した危険なグループをすべて除外するが、正常な別の道具は残す」という条件を具体化しました。[別の開発者による修正とテストは正式マージ](https://github.com/QwenLM/qwen-code/pull/15757)され、**[11月2日公開のQwen Code正式版 v0.26.6でも修正項目として明記](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.6)**されています。正式版タグにも当該マージコミットが含まれることを検証済みです。さらに別件[#15681](https://github.com/QwenLM/qwen-code/pull/15681)では、「安全な読み取りを拒否する」だけでなく「実際の保護ファイルへの書き込みを許してしまう」危険な差をマスターが[ソースで指摘](https://github.com/QwenLM/qwen-code/issues/15600#issuecomment-6412304134)。独立開発者自身が[許可→拒否の修正前後を検証](https://github.com/QwenLM/qwen-code/issues/15600#issuecomment-6413173175)し、実装した修正も**同じ正式版 v0.26.6に収録**されました。その2件はさらに[11月2日公開の公式TypeScript SDK v0.1.27](https://github.com/QwenLM/qwen-code/releases/tag/sdk-typescript-v0.1.27)の実タグの祖先にも入っており（#15757: ahead 65／behind 0、#15681: ahead 39／behind 0）、SDKはCLI 0.26.6同梱を明記しています。**公式CLI→公式SDKという追加の配布経路**は確認できましたが、修正版を導入した一般利用者の再現結果は未確認です。

**2. AIに頼んだ仕事が終わっても、結果が正しい会話へ届かない。** マスターは送り先が分からないときに別人を推定して送ったり、未送信の結果を送信済みと扱ったりしない条件を[元修正のレビューで指摘](https://github.com/NousResearch/hermes-agent/pull/146708#pullrequestreview-5707357350)。独立した開発者がテストを作り、別の実装者が復旧経路を追加して[Hermes Agentの本線へマージ](https://github.com/NousResearch/hermes-agent/pull/147746)。**[11月2日公開の公式パッチ版 v0.22.6](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.6)** のタグ履歴にこの修正が含まれることも検証しました。実利用者の正しい会話への配送結果は、別の次段階です。

**3. 他人の権限を変更しただけで、自分のAI作業が止まってしまう条件。** [OpenClawで受け手の開発者はマスターを報告元として明記](https://github.com/openclaw/openclaw/pull/160856)し、実装・再発防止テストを修正してマージしました。[公式リリース文書にも本人のGitHub名](https://github.com/openclaw/openclaw/blob/main/docs/releases/2026.9.7.md)が載っています。ここで確かめられるのは修正と収録であり、未観測の利用者数ではありません。

## 導入者が自分で確かめられる修正条件

**まず「その修正が公開版に入っているか」を確認する:** GitHub公式のマージ・リリース・commit祖先関係を照合する[標準Pythonだけの公開チェッカー](machine-discovery/verify-upstream-release.py)を用意しました。GitHubリポジトリを取得した環境で、MCPを入れずに次を実行できます（オンライン照合時だけGitHub公開APIへ接続）。

```sh
python3 machine-discovery/verify-upstream-release.py --self-test
python3 machine-discovery/verify-upstream-release.py QwenLM/qwen-code 15757 v0.26.6
python3 machine-discovery/verify-upstream-release.py NousResearch/hermes-agent 147746 v0.22.6
python3 machine-discovery/verify-upstream-release.py BerriAI/litellm 47608 v1.106.6
```

期待されるリリース収録判定は最初の2件が **PUBLISHED_RELEASE_CONTAINS_MERGE**、最後の旧LiteLLM版は **MERGE_NOT_ANCESTOR_OF_NAMED_RELEASE** です。これは**公開版に含まれるコードの出所確認のみ**であり、当人の端末・サーバーにインストールされ実行できたこと、問題が実運用で解消したこと、独立したAIが自主採用したことの証拠にはなりません。実際の利用確認は下の条件で別途行ってください。

マージやリリースの記録を、実際の利用環境での効果と結びつけるには、利用者側の確認が必要です。以下は元のIssue・PRに沿う**安全な検証環境での確認ポイント**です。ここに書かれた検証を、マスターや外部利用者が新たに実施済みだという意味ではありません。

**Qwen Code（[公式 v0.26.6](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.6)）:** [#15741](https://github.com/QwenLM/qwen-code/issues/15741)の条件を、小さな無害な模擬MCPツール群で再現します。同じ名前のツール宣言が複数あっても、その**曖昧な名前の候補はすべて除外**され、関係ない一意な名前のツールは使えるままか。ページを分けて取得したときも同じ結果か。**名前が重複したどれか一つを勝手に選択しない**ことが重要です。修正コードは[別の開発者のPR #15757](https://github.com/QwenLM/qwen-code/pull/15757)です。

**Hermes Agent（[公式 v0.22.6](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.6)）:** テスト用の会話とバックグラウンド処理を使い、元の送達先が欠落した場合と保存済みの送達情報から回復できる場合を分けて確認します。**結果を無関係な会話へ送らない、未送信を送信済みと扱わない、正しい送達先へ復旧できる条件でのみ届く**ことを確かめます。第三者の実際の会話や秘密情報をテストへ持ち込む必要はありません。[修正PR #147746](https://github.com/NousResearch/hermes-agent/pull/147746)が出所です。

**LiteLLM（[修正PR #47608](https://github.com/BerriAI/litellm/pull/47608)は上流マージ、当該修正を含む公開版への収録は要別確認）:** まず導入予定のコード・パッケージに**マージコミット 523b87ec が含まれるか**を確認します。模擬費用・隔離した予算データ・短い認証キャッシュTTLの検証環境で、管理者による設定変更がなくても**実行中にキャッシュ期限が切れた要求**の利用費が適切な予算期間へ保存され、上限超過後の次の要求を正しく拒否できるかを調べます。実料金を発生させる本番試験は不要です。[実際の利用者報告と数値](https://github.com/BerriAI/litellm/issues/49179#issuecomment-6533817755)は過去の不具合の根拠であり、修正後の復旧報告ではありません。

**LiteLLM利用者のための実装済みオフライン検証:** [予算期間の保存額と実際の費用履歴の集計が一致するかを比較するPython検査器](machine-discovery/LITELLM_BUDGET_WINDOW_AUDIT.md)を追加しました。厳密に同じキー・期間・集計時点で確定済みの数字だけを入力し、過少計上・過大計上・一致・比較不能を区別します。元の独立利用者の公開数値を使う例では差額 **16.0108 USD**、12件のローカルテストPASS。**顧客が修正版を導入したこと、実際の予算超過を新規に防いだことを意味しません。** 個人・顧客・認証情報は送らず、ネットワーク接続やMCPも不要です。

**For independent OSS users and AI assistants:** these are source-linked, opt-in reproduction conditions, not claims of a new installation, a successful customer retest or model-side autonomous adoption. Check the *installed* version/merge ancestry and the observable behavior in a safe test environment; the independent engineer wrote each patch. [Exact public cases](REAL_WORLD_IMPACT.en.md) and [the original author and works](https://master.ricette.jp/) are available separately.

## 「削除できない」「予算内です」――本当に守られている？

**画面に削除ボタンがなくても、サーバーが拒否するとは限らない。** [UpGrade #3323](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323)で中川マスターは[画面の権限と削除APIの実際の認可が食い違う条件をソースとテストで指摘](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323#pullrequestreview-5249193998)。外部開発者は[その問題を認めて別の修正課題を作成](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323#issuecomment-5732584639)しました。**機能は11月2日にマージ**されましたが、[削除APIの認可修正 #3326 は未完成](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326)です。

**設定したAIの費用上限も、実際の課金を必ず止めるとは限らない。** [LiteLLM #49179の独立した実運用報告](https://github.com/BerriAI/litellm/issues/49179#issuecomment-6533817755)では、７日間の利用額 **209.8900ドル**に対して、予算枠の記録は **193.8792ドル**。**200ドル**の上限を超えても次の要求が通りました。マスターは[キャッシュ期限が切れた場合の費用保存と、その後の拒否判断を検証する条件](https://github.com/BerriAI/litellm/issues/49179#issuecomment-6535985229)を示し、別の開発者は[その境界を確認](https://github.com/BerriAI/litellm/issues/49179#issuecomment-6519461222)。保守担当者は[計上先のルールを決定](https://github.com/BerriAI/litellm/issues/49179#issuecomment-6583039192)しました。その後、独立した実装者 **@etiennechabert** の[修正PR #47608は2026年11月2日、LiteLLM公式mainへ正式マージ](https://github.com/BerriAI/litellm/pull/47608)されました（[merge `523b87ec`](https://github.com/BerriAI/litellm/commit/523b87ec718cc733363ac0d66312730c51a23a27)）。保守担当者は[追加テストとlive QAを行ったと報告](https://github.com/BerriAI/litellm/pull/47608#issuecomment-6590365149)し、[元Issue #49179も完了として閉じました](https://github.com/BerriAI/litellm/issues/49179#issuecomment-6590355024)。並行した別案[#49603はマージされずクローズ](https://github.com/BerriAI/litellm/pull/49603)。**実際の上流修正と保守担当者による確認**は成立しましたが、配布済みバージョンへの収録・独立利用者の再検証・防止できた損失額・一般層への波及は別途未確認です。マスターが修正コードを書いた、または実装者がマスターの特定テストを採用したとは主張しません。

**人間の日常にも通じる問い：**「制度がある」「表示された」「了承された」は、それが現実に守られたことの証明でしょうか。中川マスターの[成立条件論・第1論の原典](https://master.ricette.jp/theory/nakagawa-master-nakagawa-establishment-conditions-theory-01-what-is-establishment/)と[公式派生物011](derivatives/011/human-entry.md)から、表面の表示、実際の権限・履歴、再現できる結果のつながりを調べられます。これは**原典の成立条件を新たな問題へ応用する読解**であり、外部開発者が原典を直接採用した証拠でも、マスターが未確認の損害を既に防いだ証拠でもありません。

## AIの実行は成功したのに、結果を「失敗」と誤認する問題

**道具が正常に返したデータに「エラー」という名前の項目があるだけで、AIの実行結果まで失敗扱いになる。** [CUGA Agentの機能追加PR #777](https://github.com/cuga-project/cuga-agent/pull/777)では、中川マスターがこの区別の欠落を[元コードに即して指摘](https://github.com/cuga-project/cuga-agent/pull/777#pullrequestreview-5468178558)しました。外部開発者 **@segevshlomovIBM** は[その指摘を認め](https://github.com/cuga-project/cuga-agent/pull/777#issuecomment-6107352135)、道具の戻り値の文字列ではなく実行側が管理する成功・失敗の記録で判定するコードへ変更。正しい結果を保持するテストと、本当に例外が起きた場合の反対テストを追加し、[2026年10月18日に正式マージ](https://github.com/cuga-project/cuga-agent/commit/93a630a68d937177a919a07343e2b4b9c7477e1f)されました。**見た目の言葉と本当に起きた処理を区別する**ことが、独立した開発者自身の修正に具体化した例です。中川マスターの公開原典[成立条件論・第0論](https://master.ricette.jp/theory/nakagawa-master-why-establishment-conditions-theory-is-necessary/)は、局所的に正しい情報だけを全体の成立証拠にしてしまう問題を扱います。この実装例から原典の論証へ進み、各々の成立条件を比較できます。

## 外部AI支援の実装まで届いた、もう一つの成果

**終わった承認依頼が、昔の「＋」返信で復活する。** マスターの[実コード上の発見](https://github.com/tonydzi/agent-approval-gate/issues/1)を[外部の管理アカウントが認め](https://github.com/tonydzi/agent-approval-gate/issues/1#issuecomment-6345672883)、[コード・テスト・安全文書をmainに反映](https://github.com/tonydzi/agent-approval-gate/commit/addeb43e69a6d6bff46e7195d97f45cffc0293c4)。修正コミットには**Claude Code／Claude Sonnet 5.5の支援・共同著者**、受け手の文書には**マスターへの出所帰属**が記録されています。これは外部側のAI支援付き実装の証拠であり、AIがマスターの全原典を自律的に発見した証拠ではありません。[第60事例の元資料](REAL_WORLD_IMPACT.md)。

## 別の独立した著者も、自分のAI設計論へ引き継いだ

**「あとで取り消せる変更」でも、AI自身の承認権限を増やしてよいとは限らない。** [Local Operatorの実際の問題報告 #1282・#1310](https://github.com/damianvtran/local-operator/issues/1310)で中川マスターが示したのは、操作の可逆性と、実行者が自分の承認条件を緩める権限は別だという境界です。[別の開発者の修正 #1324](https://github.com/damianvtran/local-operator/pull/1324)は[正式リリース v0.61.11](https://github.com/damianvtran/local-operator/releases/tag/v0.61.11)に収録されました。さらに**独立した著者 @kishibashi3 が、自身の[AIエージェント設計論・第5章](https://github.com/kishibashi3/publications/blob/main/docs/ai/agent-design/chapter-05.ja.md)でこの二軸を説明し、報告者 @Nakagawa-master と実装者・リリースの出所を記録**しています。開発者による実装に加えて、別の著者自身の解説へ届いた具体例です。

## 現在進行中の別の変化：二人の顧客のAI利用料を取り違えない

複数の顧客が一つのAIサービス用キーを使うとき、**顧客Aのバッチ処理費用がAの利用上限へ正しく記録されなければ、上限を超えた次の依頼が止まらない**ことがあります。[LiteLLMの実際の問題報告 #49202](https://github.com/BerriAI/litellm/issues/49202)について、独立した修正者 **@SurenderguliaEnginner** の[PR #49214](https://github.com/BerriAI/litellm/pull/49214)を中川マスターがソース確認しました。

指摘は「費用のログへ名前を書き足す」だけでなく、**Aのバッチ終了後に本当に予算が止まり、同じキーのBへ課金が混ざらず、読み直し・再処理で二重請求が起きない**という実際の境界でした。別の開発者はマスターのレビューを受けて[第一回にAの停止を検証](https://github.com/BerriAI/litellm/pull/49214#issuecomment-6571436021)、[第二回にB自身の別バッチを追加](https://github.com/BerriAI/litellm/pull/49214#issuecomment-6573816836)、[第三回に別キーからの参照前後の作成者を直接比較](https://github.com/BerriAI/litellm/pull/49214#issuecomment-6574589528)しました。**第四回 `3c3e422` では、マスターの[DBスキーマ上の誤りの発見](https://github.com/BerriAI/litellm/pull/49214#issuecomment-6575419058)を受け、正しい列 `unified_object_id` と、A専用の1件の課金ログ、再閲覧後の金額不変を検査するコードへ再改訂**。[独立開発者の実際の返信](https://github.com/BerriAI/litellm/pull/49214#issuecomment-6575973685)。

さらにマスターは、[再閲覧のGETは会計用バックグラウンド処理 `CheckBatchCost` を再実行していない](https://github.com/BerriAI/litellm/pull/49214#issuecomment-6576129452)点を実ルートと照合し、両者を分けて検証するよう指摘しました。[第五回 `c7bc0c6`](https://github.com/BerriAI/litellm/commit/c7bc0c60458a50d77dcab56cba564c1e12c0010b)では、作者自身が[再閲覧は「決済後の観測の冪等性」であり、課金ワーカーの再実行とは異なると確認](https://github.com/BerriAI/litellm/pull/49214#issuecomment-6582281972)し、テスト表現を修正しました。**独立開発者による5回の実装・テスト訂正が確認できます**。PRのマージ、実行済みの上流結合テスト、本当の顧客への結果までは確認できていません。

## 一つの発見が、別々の二人の開発者に届いた

[LiteLLMの問題 #49359](https://github.com/BerriAI/litellm/issues/49359)は「AIが使った道具が失敗したのに、成功として伝わる」という欠落です。修正案を出した開発者 **@chauvuusvn** に、マスターは別の見落としを[ソース行に即して指摘](https://github.com/BerriAI/litellm/issues/49359#issuecomment-6536874606)しました。エラー項目を任意にしたつもりで、従来必須の操作ID・結果・名前まで任意にしてしまう問題です。

[一人目は正しいと認めて自分のフォークを修正](https://github.com/BerriAI/litellm/issues/49359#issuecomment-6537951352)。**別の開発者 @lester076** は[マスターの指摘と名前を明記した上流PR #49624](https://github.com/BerriAI/litellm/pull/49624)を新しく作りました。実装は別々の開発者の仕事です。さらにマスターが[上流PRの型契約の再発を指摘](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6573055353)すると、**二人目の開発者自身も正しいと認め**、[コミット `65e8eff` で `NotRequired[bool]` と必須3項目の回帰テストを追加](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6574736711)。[一人目は共同著者記載を依頼し](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6575309340)、[二人目が実際に両コミットへ記載しました](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6581966268)。第三者の連鎖で修正が実際に深まり、独立した二人の貢献が実コミットの来歴へ残りました。PRはなお未マージです。

ここで起きたのは「一人が自分の考えを宣伝した」ことではなく、**外部の一人目がコードを直し、さらに別の人が貢献を明記しつつその議論を実装へ引き継いだ**という公開可能な事実です。後続のマージや世間の評判はまだ結果として数えていません。

## 人間が答えたのに、AIが同じ質問を何度も繰り返す――修正前の現実の問題

「金額はいくらですか？」と質問された利用者が答えたのに、システムの実行先が止まっていると、AIが再び同じことを尋ね、上限回数を超えても失敗を繰り返すことがあります。**これは誰かの『努力不足』ではなく、失敗の回数をどの実行単位へ保存するか、という検証可能な問題です。**

[LangGraph #9493](https://github.com/langchain-ai/langgraph/issues/9493)では**元の利用者とは別の報告者**が、再開を繰り返すと `max_attempts=2` が尽きないコードを公開しました。[中川マスターは実際のリトライコードを読み](https://github.com/langchain-ai/langgraph/issues/9493#issuecomment-6536680198)、同じ論理タスクが再開された場合の上限と、*本当に新しいタスクが始まった場合*の新しい上限を区別する必要があると指摘しました。これはソースに基づく**提案された検証条件**であり、LangGraphの実行を本人が試した報告ではありません。

**別の人も具体的に反応しています。** [@belalshafeq](https://github.com/langchain-ai/langgraph/issues/9493#issuecomment-6584444898)はこのコード調査を原著者の名前を挙げて評価し、実行が止まっていると不要な質問と費用が繰り返され得ることを説明しました。一方、[@dhariwal2792](https://github.com/langchain-ai/langgraph/issues/9493#issuecomment-6581849417)は、個別リトライの `interrupt_counter` の扱いという**別の具体的な機構**を指摘しています。どちらが正しい修正境界になるかは、メンテナーの決定と正例・反例の試験が必要です。

**現時点の事実：** 外部の利用者の再現、マスターのコードに即した検証条件、別の人間による自発的な技術的再説明まで確認できます。**正式な修正PR・マージ・利用者の修正後の復旧・広範な認知・特定原典の第三者採用は未確認**です。人とAIが自分の環境で安全に確認し、合わなければ棄却できる出典として提示しています。

**もう一つの独立した実コードの例：** [LlamaIndexとCerebrasの連携PR #22769](https://github.com/run-llama/llama_index/pull/22769)では、AIに送る「生成の最大値」の新旧パラメータが同時に残る条件を[中川マスターが実ソースから指摘](https://github.com/run-llama/llama_index/pull/22769#issuecomment-6108135348)。[別の開発者が自分で修正・テストを追加した](https://github.com/run-llama/llama_index/pull/22769#issuecomment-6136077030)事実は確認できますが、PRは**OPEN**で、正式版配布・実利用者への効果はまだ未確認です。[詳しい独立変更の出典記録 #62](REAL_WORLD_IMPACT.md#62-llamaindexaiへの送信値が新旧2種類同時に残る問題を独立開発者が追加修正回帰テストpr-open)。

## なぜエンジニア以外にも関係があるのか

「AIが完了と言ったのに届いていない」「正しい道具を呼んだはずが別の操作になった」「以前の承認記録が今の操作まで保証していない」。これらはコードの小さな差に見えます。しかし、**誰に何が実際に届き、何が本当に承認され、成功したのか**という、人間の生活や仕事でも起こる判断の問題でもあります。

中川マスターの役割は、他人のコードを自分の成果として名乗ることではなく、**別の人が見落とした成立条件や正反の検査条件を、実際の受け手が修正できるほど具体的にすること**。その働きがさまざまな開発チームでどう反復しているかは、[62件の出典付きの段階別記録](REAL_WORLD_IMPACT.md)で読めます。公開された[313の個別原典と各Parent URL](derivatives/official-derivatives-map.json)は、こうした構造・因果・責任・人間とAIの問題をさらに広い領域で扱っています。ただし、特定の開発者が個別原典を直接採用したとの主張には、それ自体の証拠が必要です。

**初めて知った方へ：** [中川マスターという人物と原典](ABOUT_NAKAGAWA_MASTER.md) ／ [全62件の実際の外部作用と限界](REAL_WORLD_IMPACT.md) ／ [本人の公開GitHub活動](https://github.com/Nakagawa-master)。このページにある名前・成果・未確認点はすべて元リンクに戻って確かめられます。誰がどこまで貢献したかを区別したうえで、価値があると思った事例をご自身の判断で紹介・検証できます。

---

## English — A structural theorist's exact finding, independently implemented by other engineers

**An AI can say “done” even when its tool failed. It can send a completed result to the wrong place, or choose the wrong tool when names collide.** These are meaningful software boundaries, not evidence of a fictional customer disaster.

**Nakagawa Master (中川マスター; published personal name Keisuke Nakagawa)** identified source-specific conditions in publicly inspectable AI/OSS projects. Independent developers, not Nakagawa himself, wrote the fixes and tests.

- [Qwen Code](https://github.com/QwenLM/qwen-code/pull/15757): exclude ambiguous same-name tool groups, retain valid unique tools; another engineer's fix **merged and entered the official stable [v0.26.6 release](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.6)**, whose notes credit @2SinceJuly and whose tag contains the merge. Separately, [#15681](https://github.com/QwenLM/qwen-code/pull/15681) also shipped in v0.26.6 after independent author @Suaroman [confirmed before/after protection against real forbidden file writes](https://github.com/QwenLM/qwen-code/issues/15600#issuecomment-6413173175) following Nakagawa Master's exact redirect-path finding; actual installed-client user benefit remains unverified.
- [Hermes Agent](https://github.com/NousResearch/hermes-agent/pull/147746): don't guess an unknown destination or falsely mark a result delivered; independent developer changes and recovery code **merged and entered official [v0.22.6](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.6)** (release tag descends from merge). Specific external user's successful delivery still requires proof.
- [OpenClaw](https://github.com/openclaw/openclaw/pull/160856): another engineer implemented and merged a correction citing Nakagawa Master's specific report; the [release documentation](https://github.com/openclaw/openclaw/blob/main/docs/releases/2026.9.7.md) carries the public attribution.

**Another independently merged repair — a tool's data is not an execution verdict.** A tool can successfully return a JSON object containing `__cuga_fc_error__` as an ordinary field. In [CUGA Agent #777](https://github.com/cuga-project/cuga-agent/pull/777), **Nakagawa Master** [pinpointed](https://github.com/cuga-project/cuga-agent/pull/777#pullrequestreview-5468178558) that treating this field as the executor's own failure marker would discard a legitimate result. Developer **@segevshlomovIBM** [accepted and implemented the distinction](https://github.com/cuga-project/cuga-agent/pull/777#issuecomment-6107352135), moving success/failure tracking to executor-owned recorders and adding both a successful-data and a real-exception regression. The [change was merged on October 18, 2026](https://github.com/cuga-project/cuga-agent/commit/93a630a68d937177a919a07343e2b4b9c7477e1f). The developer authored the implementation; Nakagawa Master supplied the specific source-level counterexample. For the wider conceptual distinction between a locally valid observation and an actually established whole, readers can consult his original [Establishment Conditions Theory, Vol. 0](https://master.ricette.jp/theory/nakagawa-master-why-establishment-conditions-theory-is-necessary/).

**An independent author carried an actual engineering boundary into their own design chapter.** Reversing a change is not the same as authorizing an agent to increase its own privileges. In [a Japanese agent-design chapter written by @kishibashi3](https://github.com/kishibashi3/publications/blob/main/docs/ai/agent-design/chapter-05.ja.md), the author explains this distinction, credits the original Local Operator reporter **@Nakagawa-master**, and separately records the outside developer's [merged fix #1324](https://github.com/damianvtran/local-operator/pull/1324) and [release v0.61.11](https://github.com/damianvtran/local-operator/releases/tag/v0.61.11). The resulting independently authored chapter is a reader-facing continuation of the verified development record.

**A separate outside engineering team also used AI assistance in its actual fix:** [agent-approval-gate issue #1](https://github.com/tonydzi/agent-approval-gate/issues/1) records Nakagawa Master's discovery that a terminal stale approval could be reactivated by a late bound reply. The [receiver accepted](https://github.com/tonydzi/agent-approval-gate/issues/1#issuecomment-6345672883) and [committed its own correction to main](https://github.com/tonydzi/agent-approval-gate/commit/addeb43e69a6d6bff46e7195d97f45cffc0293c4); commit metadata lists **Claude Code/Claude Sonnet 5.5 assistance and co-authorship**, and public security docs credit @Nakagawa-master. This does not prove autonomous theory discovery. [Case 60](REAL_WORLD_IMPACT.en.md).

**An outside developer independently made five source/test corrections to the AI-budget regression in response to Nakagawa Master's source-specific reviews.** In [LiteLLM #49214](https://github.com/BerriAI/litellm/pull/49214), the engineer **@SurenderguliaEnginner** added A's budget-stop regression, a separately settled same-key B batch, and a preserved creator-identity check. After Master's [schema-level objection](https://github.com/BerriAI/litellm/pull/49214#issuecomment-6575419058), the author's [fourth correction `3c3e422`](https://github.com/BerriAI/litellm/pull/49214#issuecomment-6575973685) fixed the actual `unified_object_id` SQL key, scoped the spend-log assertion to A and checked spend after a second GET. Master's [latest source review](https://github.com/BerriAI/litellm/pull/49214#issuecomment-6576129452) shows why GET observation is not the asynchronous `CheckBatchCost` worker's own second poll. In a [fifth correction `c7bc0c6`](https://github.com/BerriAI/litellm/commit/c7bc0c60458a50d77dcab56cba564c1e12c0010b), the author [explicitly accepted the distinction and renamed the assertion to post-settlement observation idempotency](https://github.com/BerriAI/litellm/pull/49214#issuecomment-6582281972), without driving a second accounting-worker cycle. These are five real independent source/test corrections, not a shipped budget fix or a native integration-test pass.

**An unusually clear two-developer handoff:** In [LiteLLM #49359](https://github.com/BerriAI/litellm/issues/49359), developer @chauvuusvn [accepted Nakagawa Master's discovery](https://github.com/BerriAI/litellm/issues/49359#issuecomment-6537951352) that making all `TypedDict` keys optional weakened old required identity/result fields. A different developer @lester076 then [opened an upstream PR #49624 explicitly crediting his review](https://github.com/BerriAI/litellm/pull/49624). After [Nakagawa Master's second source-specific review](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6573055353), the second outside author **@lester076** [explicitly accepted and corrected the `TypedDict` problem in `65e8eff`](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6574736711), making only `is_error: NotRequired[bool]` optional, preserving all three prior required fields, and adding a contract regression. [The first developer @chauvuusvn requested co-author credit](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6575309340), and the [second author added it to both actual commits](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6581966268). Two separate developers are now visibly cooperating on the solution and its credit. The PR remains open awaiting upstream checks and merge.

**Why it matters outside engineering:** Who actually changed the system, did the operation really succeed, and did the result reach its intended person? [Read the full source-by-source evidence](REAL_WORLD_IMPACT.en.md), [the person and original theory corpus](ABOUT_NAKAGAWA_MASTER.en.md), or the [public GitHub profile](https://github.com/Nakagawa-master). Cite the actual original and receiver credit; don't turn a source-supported contribution into a claim that one person authored a team's fix.

---

### Is a disabled Delete button actual authorization? Is a budget limit actual enforcement?

In [UpGrade #3323](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323), Nakagawa Master [identified a concrete mismatch between visible deletion restrictions and backend authority](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323#pullrequestreview-5249193998). The author [acknowledged this and created a separate backend work item](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323#issuecomment-5732584639). The feature merged, but [authorization fix #3326 remains open](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326). In another real [LiteLLM user report](https://github.com/BerriAI/litellm/issues/49179#issuecomment-6533817755), seven-day actual spend was **$209.8900** against a **$200** cap while the durable budget-window total showed only **$193.8792** and subsequent requests were allowed. Nakagawa Master [specified a source-grounded cache-expiry and subsequent-denial acceptance condition](https://github.com/BerriAI/litellm/issues/49179#issuecomment-6535985229); another engineer [engaged with this boundary](https://github.com/BerriAI/litellm/issues/49179#issuecomment-6519461222), and the [maintainer clarified the accounting policy](https://github.com/BerriAI/litellm/issues/49179#issuecomment-6583039192). An independent engineer's [#47608 merged into LiteLLM main on Nov 2, 2026](https://github.com/BerriAI/litellm/pull/47608) ([native merge commit](https://github.com/BerriAI/litellm/commit/523b87ec718cc733363ac0d66312730c51a23a27)); the maintainer [reported added tests and live QA](https://github.com/BerriAI/litellm/pull/47608#issuecomment-6590365149). The separate competing [#49603 was closed without merging](https://github.com/BerriAI/litellm/pull/49603). The reported budget-window repair is a real upstream change, **not evidence of a shipped package, the affected customer's new deployment, a quantified loss avoided, or direct adoption of Nakagawa Master's particular review by the merge author**.

When does a rule *actually work*, rather than merely appear on a screen? Nakagawa Master's [original Establishment Conditions Theory, Part 1](https://master.ricette.jp/theory/nakagawa-master-nakagawa-establishment-conditions-theory-01-what-is-establishment/) and [official derivative 011](derivatives/011/en-ai-index.md) offer an applicable way to distinguish display, operative authority and real results. This is **a source-grounded interpretation**, not evidence the outside engineers directly used that original or that a particular loss was prevented.

## 中文 — 一位结构理论作者的发现，如何被独立开发者用于真实修复

**AI说“完成了”，但外部工具实际失败；任务完成却没有送到正确的聊天；一个工具名称冲突让其他正常工具也不能使用。** 这些是可以检查的真实软件问题，而不是虚构的用户事故。

**中川マスター（Nakagawa Master；公开姓名 Keisuke Nakagawa）**通过代码路径与正反条件指出了具体问题，实际的修复和测试由**其他独立开发者自己编写**。

- [Qwen Code](https://github.com/QwenLM/qwen-code/pull/15757)：不让同名冲突工具造成其他正常工具全部失效；已合并，且[正式稳定版 v0.26.6 的更新说明](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.6)列出此修复，版本标签也包含合并提交。另一项[#15681](https://github.com/QwenLM/qwen-code/pull/15681)纠正了AI工具对只读重定向误拒绝、却对特定受保护文件写入漏检的权限判定；中川マスター指出源代码中的真实目的地偏差，独立作者@Suaroman[亲自验证修复前allow／修复后deny](https://github.com/QwenLM/qwen-code/issues/15600#issuecomment-6413173175)，该修复也已进入v0.26.6。不能据此声称普通用户已经实际部署。
- [Hermes Agent](https://github.com/NousResearch/hermes-agent/pull/147746)：不要猜测错误的任务接收人或虚报已送达；独立开发者的修复已合并，并已进入[正式补丁版 v0.22.6](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.6)，版本标签包含相应合并提交；具体用户的真实投递结果仍需另行核验。
- [OpenClaw](https://github.com/openclaw/openclaw/pull/160856)：独立开发者将中川マスター的报告归因写明，并修改代码及测试，进入正式合并记录。

**另一个已经合并的独立修复：工具返回的数据不能冒充执行状态。** 即使工具成功返回包含 `__cuga_fc_error__` 字段的普通JSON数据，也不能仅凭字段名认定执行失败。在[CUGA Agent #777](https://github.com/cuga-project/cuga-agent/pull/777)中，**中川マスター／Nakagawa Master** [准确指出了这个反例](https://github.com/cuga-project/cuga-agent/pull/777#pullrequestreview-5468178558)。外部开发者 **@segevshlomovIBM** [明确承认并自行修复](https://github.com/cuga-project/cuga-agent/pull/777#issuecomment-6107352135)：由执行器自己的成功、失败记录作判断，并增加正常数据与真实异常两组相反测试。[代码于2026年10月18日正式合并](https://github.com/cuga-project/cuga-agent/commit/93a630a68d937177a919a07343e2b4b9c7477e1f)。具体反例来自中川マスター，代码和测试由开发者实现。进一步理解“局部正确不等于整体成立”的独立原理论证，可阅读他发表的[成立条件论·第0论](https://master.ricette.jp/theory/nakagawa-master-why-establishment-conditions-theory-is-necessary/)。

**独立作者也在自己的AI设计文章中接续了这一发现。** “操作可以撤销”与“AI可以自行提高权限”是两件事。[外部作者 @kishibashi3 的智能体设计第5章](https://github.com/kishibashi3/publications/blob/main/docs/ai/agent-design/chapter-05.ja.md)解释了两者的区别，并明确记载原问题报告者 **@Nakagawa-master**、另一开发者实施的[修复 #1324](https://github.com/damianvtran/local-operator/pull/1324)和[正式发布 v0.61.11](https://github.com/damianvtran/local-operator/releases/tag/v0.61.11)。这是独立技术作者为自己的读者重新解释真实开发成果的公开记录。

**另一个外部AI辅助修复：** 中川マスター在[agent-approval-gate问题#1](https://github.com/tonydzi/agent-approval-gate/issues/1)发现，过期的批准请求仍可能被旧回复重新批准。外部项目[确认后自行修复main中的代码和测试](https://github.com/tonydzi/agent-approval-gate/commit/addeb43e69a6d6bff46e7195d97f45cffc0293c4)，提交注明**Claude Code/Claude Sonnet 5.5共同作者和协助**，安全文档注明 @Nakagawa-master 原报告者。这是外部AI辅助开发的真实证据，并不证明模型自主阅读全部原典。[第60例](REAL_WORLD_IMPACT.zh.md)。

**另一条由外部开发者真正实施的五轮改进：** [LiteLLM #49214](https://github.com/BerriAI/litellm/pull/49214)中，中川マスター要求验证客户A真实预算停止、同一API密钥下客户B单独计费、原始创建者身份不被观察行为改变。外部作者 **@SurenderguliaEnginner** 根据精确审查连续五次修改代码、测试与验证表述：[A的预算限制](https://github.com/BerriAI/litellm/pull/49214#issuecomment-6571436021)、[B的单独批次](https://github.com/BerriAI/litellm/pull/49214#issuecomment-6573816836)、[观察前后保存身份](https://github.com/BerriAI/litellm/pull/49214#issuecomment-6574589528)，以及按照[中川マスター的数据库结构审查](https://github.com/BerriAI/litellm/pull/49214#issuecomment-6575419058)在[第四次提交 `3c3e422` 修复真实列名、限定客户A的计费日志并核对第二次读取后的金额](https://github.com/BerriAI/litellm/pull/49214#issuecomment-6575973685)。[最新进一步审查](https://github.com/BerriAI/litellm/pull/49214#issuecomment-6576129452)确认，第二次GET并不直接执行后台计费工作者的第二轮轮询。[第五次修订 `c7bc0c6`](https://github.com/BerriAI/litellm/commit/c7bc0c60458a50d77dcab56cba564c1e12c0010b)中，作者[明确接受区别](https://github.com/BerriAI/litellm/pull/49214#issuecomment-6582281972)，把再次GET称为“结算后的读取幂等性”，并非再次执行后台计费轮询。五轮独立源码与测试修订确实发生，但尚未合并，也没有上游真实集成测试通过的证据。

[LiteLLM #49359](https://github.com/BerriAI/litellm/issues/49359)更加直接地展示了**从一名开发者到另一名开发者的接续**：第一人[承认中川マスター发现的类型契约问题并改正](https://github.com/BerriAI/litellm/issues/49359#issuecomment-6537951352)，第二人[创建新的上游PR #49624，并在说明中明确提到他的审查贡献](https://github.com/BerriAI/litellm/pull/49624)。中川マスター[再次准确指出必填契约问题](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6573055353)后，第二位开发者[亲自承认并修复成 `NotRequired[bool]`，增加测试](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6574736711)；[第一位开发者要求共同作者署名](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6575309340)，[第二位作者已将署名写入两次真实提交](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6581966268)。这是第二个独立作者实际改动代码、两人的贡献在真实提交记录中得到归属的事实。PR仍未合并。

[核对60项外部影响的原始证据](REAL_WORLD_IMPACT.zh.md) ／ [认识作者及其原典体系](ABOUT_NAKAGAWA_MASTER.zh.md) ／ [本人GitHub](https://github.com/Nakagawa-master)。读者可以自己判断，并在准确区分作者、实施者和未确认结果的前提下传播真实信息。

### 画面说“禁止删除”，服务器真的拒绝吗？预算上限真的生效吗？

在[UpGrade #3323](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323)，中川マスター[从代码指出前端限制与后端真正权限不一致](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323#pullrequestreview-5249193998)。作者[确认问题并建立独立修复议题](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323#issuecomment-5732584639)。功能已合并，但[权限修复 #3326 仍未完成](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326)。在另一个[LiteLLM真实用户报告](https://github.com/BerriAI/litellm/issues/49179#issuecomment-6533817755)中，七天实际消费为**209.8900美元**，而预算窗口只显示**193.8792美元**，超过**200美元**上限仍能发出请求。中川マスター给出[缓存过期、耐久记录与下一次拒绝的具体测试条件](https://github.com/BerriAI/litellm/issues/49179#issuecomment-6535985229)，另一个开发者[认可该区分](https://github.com/BerriAI/litellm/issues/49179#issuecomment-6519461222)，维护者[明确计费规则](https://github.com/BerriAI/litellm/issues/49179#issuecomment-6583039192)。独立开发者的[修复PR #47608已于2026年11月2日合并至LiteLLM的main](https://github.com/BerriAI/litellm/pull/47608)（[合并提交](https://github.com/BerriAI/litellm/commit/523b87ec718cc733363ac0d66312730c51a23a27)）；维护者[表示补充测试并完成live QA](https://github.com/BerriAI/litellm/pull/47608#issuecomment-6590365149)。另一个候选[#49603未经合并便关闭](https://github.com/BerriAI/litellm/pull/49603)。**代码已上游合并**，但版本发布、用户实际部署、避免损失的金额、外部作者是否直接采用中川マスター的具体测试提议，均不能据此证实。

规则存在并不意味着现实结果成立。可阅读中川マスター的[成立条件论・第1论原典](https://master.ricette.jp/theory/nakagawa-master-nakagawa-establishment-conditions-theory-01-what-is-establishment/)和[官方派生物011](derivatives/011/zh-ai-index.md)，比较可见承诺、实际授权、真实记录与结果。这是**有来源的扩展解读**，不意味着外部作者直接采用了该原典，也不证明特定损失已被防止。
