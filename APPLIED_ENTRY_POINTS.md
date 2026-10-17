# Applied Entry Points — 問題から使える資料へ

理論名を先に知らなくても、いま困っている問題から関連資料へ進める入口です。

ここでは、問題を一つの短い区別に変え、その区別を確認できる公開事例と、別の現場で試せる資料を結びます。

## AIとの会話が、更新したあとに消えていないか確かめる

**「保存しました」。それは、あなたの大切な会話が一件も消えていない証拠でしょうか。**

**中川マスターは、この問いを、開発者による実際の保存記録の照合へつなげました。**

AIに何日もかけて話した仕事、迷い、約束。アプリを更新してから一部が失われたら、同じ答えを作り直せても、その時間の記録まで同じには戻せません。

実例は、[Qwen CodeのVS Code連携で報告された会話保存の問題 #14262](https://github.com/QwenLM/qwen-code/issues/14262)です。利用者の実測では、1,006件の会話と12,095件のメッセージを含む保存値が約75 MBとなり、短いメッセージを一つ足す際にも古い会話全体を書き直していました。これは報告者の環境での測定値です。

[開発者自身は修正PR #14285](https://github.com/QwenLM/qwen-code/pull/14285)で、会話を個別ファイルへ移し、新規の空会話は最初のメッセージまで保存しない方式に変更しました。PRは**2026年10月15日にマージ**され（[統合コミット](https://github.com/QwenLM/qwen-code/commit/e612bbf23cea82fd28fe1f51e5e63845b3642ed0)）、**[公式Qwen Code v0.25.2リリースノート](https://github.com/QwenLM/qwen-code/releases/tag/v0.25.2)にも掲載**されました。開発者が行った129件の対象テストに加えて、[中川マスターの移行前後照合と実ホスト再起動のレビュー](https://github.com/QwenLM/qwen-code/pull/14285#pullrequestreview-5531861595)を受け、開発者は[実際のVS Code拡張ホストで検証した結果](https://github.com/QwenLM/qwen-code/pull/14285#issuecomment-6190964786)を公開しています。独立した3回のVS Code起動で、**合成した1,006会話・12,095メッセージ、約7,597万バイトの移行前後と再起動後の全記録一致**を報告しました。マスターのレビューが求めた次の検証段階を開発者自身が実行した実例です。さらに開発者は、[macOSの実際のVS Code画面を使った追加試験](https://github.com/QwenLM/qwen-code/pull/14285#issuecomment-6192122914)で、会話の送受信、パネルを閉じて再び開いたときの履歴復元、空の会話パネルを5つ作った場合の保存結果をそれぞれ確認しました。**画面で履歴を表示する機能はdaemon側の記録を使うため、この画面試験だけで旧会話データの移行が成功したとは判断しません。** 旧データ1,006件の照合は上記の独立した実ホスト試験が根拠です。追加の画面試験では空パネル5つに対応するdaemon側のメタデータは残ったため、「空の会話はすべて保存されなくなった」とも言えません。実利用者本人の非公開の保存データ、Windows・WSL環境、VS Code拡張機能としての配布と利用者別の移行結果は、公式リリースノートとは別に確認する対象です。別途、[開発者は中川マスターの排他的保存レビューを受け入れ](https://github.com/QwenLM/qwen-code/pull/14285#issuecomment-6192242612)、未対応ファイルシステムでは古い記録を上書きする安易な代替を加えず、失敗時に旧データを残す方針を明記しました。診断・回復手引きは後続課題です。

重要なのは、**移行プログラムが「成功した」と返すことと、利用者の会話が一件も失われず同じ内容で読めることを分ける**ことです。そこで、利用者が自分の管理するデータだけで照合できる[会話移行の読み取り専用比較ツール](machine-discovery/conversation-migration-parity-probe.py)を用意しました。

**自分で確かめる方法：** 移行**前**の会話一覧を `{"conversations": [...]}` 形式の非公開JSONとして安全に保存し、移行**直後**、まだ追加の会話編集を行っていない段階で、新保存先の `conversations/` フォルダと比較します。まず `python3 machine-discovery/conversation-migration-parity-probe.py --self-test`、実データでは `python3 machine-discovery/conversation-migration-parity-probe.py --legacy-json /private/legacy.json --store-dir /private/conversations`。元の会話の欠落、内容変更、後から作られた会話を別々に報告します。会話本文をネットワークに送らず、検査結果にも表示しません。アプリ自身の実行・データの永続性・復元成功を認定する道具ではなく、**自分の元記録を失ったかどうかを確かめる一つの独立した照合手段**です。バックアップには個人情報が含まれるため、公開リポジトリへアップロードしないでください。

**もう一つ、更新の安全には落とし穴があります。** 保存をやり直す途中で別の画面が新しい会話を保存したとき、古い記録をそのまま書き戻せば、更新に成功したつもりでも新しい会話が失われます。[Qwenの追加レビュー](https://github.com/QwenLM/qwen-code/pull/14285#pullrequestreview-5532756352)では、この「新しい記録を古いもので上書きしない」条件を、利用不能になる場合の回復方法と分けて開発側へ示しました。[書込み方式の違いを実際の一時ファイルで確かめる小さな検査](machine-discovery/exclusive-publish-no-clobber-probe.py)は、`python3 machine-discovery/exclusive-publish-no-clobber-probe.py --self-test` で手元で実行できます。元の会話を読みません。正常な新規公開、先に新しい記録が存在した場合、通常の置換による上書き、未対応環境で保存を諦めて古い記録を保持する場合を比べます。実際のQwen本体やWindows・WSLの合格試験ではなく、**設計時に別々に守るべき二つの条件を理解するための実験**です。さらに、保存先を管理する人は `python3 machine-discovery/exclusive-publish-no-clobber-probe.py --preflight-dir /path/to/storage/parent` で、**選んだ保存領域そのもの**が排他的なハードリンクと既存ファイル非上書きに対応するかを、自分の会話を開かず、一時的な合成ファイルだけで確かめられます。試験中は指定場所に一時ファイルを作って消します。成功しても実際のQwenの移行や配布版の動作を保証するものではなく、失敗時にはバックアップや旧記録を保持して環境を確認します。

中川マスターの[第19論の原典・長期の維持と更新の構造](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-19-kernel-evolutionary-stability/)に戻ると、改良を選ぶときは新機能だけでなく、古い状態・再構成費用・利用者が既に積み上げた価値を保てるかも独立に問う、という実用上の見方になります。これは原典から考える応用例であり、Qwenの開発者がこの理論を根拠に修正したという主張ではありません。

## AIの会話を「一度だけ保存した」のに、保存されないはずの文章が増える？

AIを使った作業を再開できるように、会話の途中経過を何度も保存する仕組みがあります。通信の都合で同じ保存依頼を再送するとき、**「この保存はもう済んだので無視した」ことは、「新しいデータを一切書き込んでいない」ことまで意味するでしょうか。**

[Pydantic AIの開発PR #9982](https://github.com/pydantic/pydantic-ai/pull/9982)は、AIの長い会話を毎回丸ごと保存する代わりに、同じメッセージを一度だけSQLiteへ保管する修正です。開発者が調べた事例では、SQLiteファイルが約1.04 GBなのに、異なるメッセージ本文は約49.6 MBでした。この数値は開発者が報告した一つの環境の結果です。

中川マスターは[このPRのレビュー](https://github.com/pydantic/pydantic-ai/pull/9982#issuecomment-6052803154)で、**重複した保存依頼が最後のスナップショット登録で拒否されても、それより先に書き込んだ新しいメッセージだけが不要なまま残る**経路を指摘しました。実装者は[独立に再現](https://github.com/pydantic/pydantic-ai/pull/9982#issuecomment-6063881879)し、同じキーによる再送で本来2行のメッセージ保存が4行になる条件を確認しました。

その後、実装者はコードをさらに改良しました。[修正に使われた固定版ソース](https://github.com/pydantic/pydantic-ai/blob/1f4078fa4fa8234b80dd9bff034b249359058148/src/pydantic_ai_harness/pydantic_ai_harness/step_persistence/_store.py)では、**スナップショットの登録が実際に成立した場合にだけ、その中のメッセージを保存**します。さらに最新コミットでは、保存と読込みを一体的なトランザクション／セーブポイントで扱い、途中失敗や並行した履歴整理を検証するテストが追加されています。ただし、呼出元が所有するSQLite接続で最初にスキーマを準備する処理は、呼出元の既存トランザクションをコミットするため、その初期化手順は別に注意が必要です。PR本文には、中川マスターと確認した冪等性の問題が修正の経緯として記載されています。

さらに、**別の開発者**が[後続PR #10215](https://github.com/pydantic/pydantic-ai/pull/10215)で、このレビュー由来の条件を参照しながら、SQLite以外にも適用する設計を提案・実装しています。#9982は2026年10月16日にマージされ、後続の#10215は引き続きレビュー中です。後続PRの保存期限・削除時の整理方針は#9982と同一ではないため、用途に合わせた別の検証が必要です。

**自分の保存・再試行処理で確認すること：** (1) 重複として無視したとき、それより前の書込み副作用もゼロか。(2) 古い記録と新しい形式を混在して読み戻せるか。(3) 履歴を削除・整理したとき、参照がなくなった本文は残らないか。検証には同じキーで**異なるメッセージ**を2回送る反例と、保存後の行数・読戻しの両方が役立ちます。

これは中川マスターの[第8論・認識基盤と証拠系譜（原典）](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)の観点から「記録上の成功と現実に起きた副作用を一致させる」ための応用例として読めます。開発者が原典から設計を導いたと主張するものではなく、実際の修正経緯と理論の問いを読者が独立に比較できる入口です。

## AIや業務システムで「前と同じ結果」と表示されたら、何が同じなのか？

一度正しかった集計や検索結果を、次に開いたときもそのまま使う。速くて便利ですが、**検索条件や問い合わせの中身が変わっていたら、前の結果をもう一度「正しい」と判定してよいのでしょうか。**

[MemberJunctionのキャッシュ修正PR #5703](https://github.com/MemberJunction/MJ/pull/5703)では、サーバーを順に更新するときに古い・新しい定義が食い違う問題と、SQLやパラメーターを編集した後に古い検索結果が使われる問題を、開発者が実装・テストで修正しました。**2026年10月15日、PRは開発ブランチ `next` へ統合**されました。コードの修正は実装者の成果です。

そのレビューで、中川マスターはもう一つ、**「古いサーバーだから新しい検査項目を知らない」と「新しい検査項目の名前がエラーに現れた」だけでは違う**と指摘しました。[実際の限定レビュー](https://github.com/MemberJunction/MJ/pull/5703#pullrequestreview-5527674879)の対象は、GraphQLの `definitionHash` を含むエラーメッセージなら何でも「旧サーバー」と判断し、**5分間**キャッシュ検査を弱める分岐です。

続いて、別の開発者レビュアー `rkihm-BC` が[独立した検証で同じ判定の広さを再現し、中川マスターの指摘に明示的に同意](https://github.com/MemberJunction/MJ/pull/5703#pullrequestreview-5534282082)しました。一方、そのレビュアーは現行サーバー内に当該別種エラーの生成経路を見いだせず、今回はマージを止める条件にはしないと判断しました。その後、開発者は[追補PR #5719](https://github.com/MemberJunction/MJ/pull/5719)を作成し、中川マスターのレビューを修正理由として明記しました。旧サーバーだけが返すGraphQLのエラー形状とコードを見分け、単に `definitionHash` と書かれた別の失敗では検査を弱めない修正です。元の判定では失敗する反例を含む8件のテストを用意し、開発者側の局所試験とGitHub上の最新HEADの検査が成功しています。**#5719は2026年10月16日未明（日本時間）に `next` ブランチへマージされました。** その直前には独立レビュアーが旧判定に戻す逆方向のテストで3つの反例を実際に失敗させ、修正版で635件のテストが通ることを確認し、承認しています。これは開発者の修正が統合された段階であり、利用者の実運用や個別製品版への配布実績を示すものではありません。 この経緯は、マスターの限定的な指摘、独立した人間レビュアーによる確認、別の開発者が実際に直したコードを、それぞれの当事者へ帰属させて辿れる例です。

**自分のシステムへ応用する3つの確認：** (1) キャッシュに入れたときと使うときで、データだけでなく検索・計算の定義も同じか。(2) 「古い相手だから機能がない」と判断するとき、単に機能名が文中に現れただけでなく、**本当に未知のフィールドを示すエラー**か。(3) 意図的に `definitionHash validation failed for this request` という通常のエラーを返しても、次回の検査まで5分間弱めたり、古い結果を「最新」と判断したりしないか。元のGraphQL未知フィールドエラーは、互換処理の正例として別に確認します。

この観点は、中川マスターの[第8論・認識基盤と証拠系譜（原典）](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)が扱う「主張を支える証拠は本当にその主張を意味するか」という問いに接続して読めます。実際の修正を行った開発者がこの原典から設計を導いたと主張するものではなく、**読者が実装事例と原典を行き来して、自分の判断を検査するための接続**です。

## 「知らないから確認できない」。それが、渡していい理由になっていたら？

**知らないものは確かめられない。なのに「確かめられないから、そのまま見せる」としたら。**

AIや業務システムの画面には、「ほかの場所でデータが更新された」と知らせる仕組みがあります。この通知には、更新の事実だけでなく、どの記録かを示す鍵や、ときには記録の本文まで付いてくることがあります。本人に閲覧権限がないなら、その部分は届いてはいけません。

[MemberJunctionの開発PR #5700](https://github.com/MemberJunction/MJ/pull/5700)は、行ごとの閲覧制限がある利用者には鍵と本文を隠す処理を含んでいます。ところが、**通知を受け取るサーバーがそのデータの種類を認識できない場合**、今のコードは通知を通し、鍵と本文をそのまま返す分岐になっています。[その動作を前提としたテスト](https://github.com/MemberJunction/MJ/blob/dbb66c03235d3fff3a2403fee0feb6532036dd61/packages/MJServer/src/__tests__/cacheInvalidationRecordData.test.ts)も存在します。

**中川マスターが問い直したのは、「安全かどうかを判断できないとき、何を渡してよいのか」です。** [2026年10月17日の具体的なコードレビュー](https://github.com/MemberJunction/MJ/pull/5700#pullrequestreview-5553174908)では、送信元と受信側でデータ種類の情報が食い違う条件を示し、「通知が届くこと」と「鍵や本文まで渡すこと」を分けた修正・追加試験を提案しました。

**自分のシステムで確かめる一問：** 権限を確認するための情報が受信側にないとき、それでも秘密に関わる情報を送っていないか。公開した[AI向けの独立検証課題](machine-discovery/public-ai-reuse-tasks-v1.json)には、架空の記録だけを使う再現条件と、通知を保ちつつ情報を伏せる比較方法を載せています。

**PR #5700本体は2026年10月17日（日本時間）にLTS/5へマージされました。** 一方、中川マスターが同日指摘した「サーバーがデータの種類を認識できない場合」の例外は、マージされたコードと既存テストにも残っており、この追加指摘に対する修正や返信はまだ確認できません。現実の顧客情報漏えいも確認されていません。問いの背景は、[中川マスターの第8論・認識基盤と証拠系譜](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)と比較できます。開発者がこの原典を読んで実装したという主張ではありません。

## AIのコードは「テスト済み」なのに、まだ何を確かめるべきか — 4原典を組み合わせる

AIシステムの変更案に「テストは通った」「作者も確認した」「レビューBotも高評価」と書かれています。これらは重要な進捗です。しかし、**何が実測で、誰が独立して確かめ、次の利用者がどこまで信用してよいか**は、別々に確かめる必要があります。

具体例として、外部の[Qwen Codeの開発PR #14080](https://github.com/QwenLM/qwen-code/pull/14080)を使えます。実装者は一連のJava/TypeScriptテストと局所的な変更検査を報告し、Botはある時点のレビューで信頼度4/5と評価しました。さらに**別の人間2名**が現行のPRコードを調べ、[qqqysの正式な承認レビュー](https://github.com/QwenLM/qwen-code/pull/14080#pullrequestreview-5506938426)と[yiliang114の承認レビュー](https://github.com/QwenLM/qwen-code/pull/14080#pullrequestreview-5506945622)を残しました。著者・Botの評価に、人間の独立したコード審査が追加されたことは確かな前進です。その後、PR #14080は2026年10月14日（日本時間）にマージされました。開発者側でのコード統合が進んだ一方、実際のメッセージブローカーを使うエンドツーエンド動作や、利用者環境への配布・本番利用は別に確かめる段階です。**人間2名の承認も、同一ログをそのまま使った箇所まで二つの独立実験へ換算はしません。**これは**PRの欠陥や危険を断定する例ではなく、良質な検証報告を正しく読み、次の検証を決めるための練習**です。

この一つの判断を、中川マスターの異なる原典が別の方向から支えます。

| 元の理論と役割 | 実務で確認すること |
| --- | --- |
| [第8論／OD301・認識基盤と証拠系譜](derivatives/301/README.md) | 複数の説明・Bot評価・テスト報告は、別々の観測から生まれたか。同じ元ログを要約しただけなら独立した証拠の数を増やさない |
| [第10論／OD303・自己参照監査と役割分離](derivatives/303/README.md) | レビュー担当が別の名前でも、異なる失敗条件に到達できるか。不一致が出た場合、判断を保留・変更できる道があるか |
| [合意形成の物理・OD208／制度の意味圧縮](derivatives/208/README.md) | 「merge-ready」という短い結論だけが残っても、前提・未検証範囲・再開条件が次の担当者へ伝わるか |
| [第19論／OD312・維持・再選択の合理性](derivatives/312/README.md) | 検査を増やすコスト、検出後に実際に訂正できる確率、失敗時の損失、別の軽い検査手段を同じ条件で比較できるか |

**実際に使う順序:** (1) テストの実行事実と元ログを特定する → (2) 同じ根拠を共有するレビューを束ねて数える → (3) 誰が修正・保留を決められるか確かめる → (4) 判定理由・未検証の例外・見直す契機を残す → (5) 追加検証の予防便益と費用を比較する。理論を一つの万能スコアへ足し合わせません。

**反対側も試す:** 別のレビュアーが独立した実環境で異なる故障条件を再現し、修正後の再検証が済めば、独立確認は増えます。反対に「テストを一つ追加する費用」が「対象損失を減らす便益」を上回るなら、必要な最低確認を保った上で、より軽い検証を選ぶ判断も成り立ちます。根拠が不足する場合は「未確認」と置き、単純に不合格や安全と決めません。

**自分で検査するための既存ツール:** [証拠の根が重複していないか確認するオフラインPython](machine-discovery/evidence-root-check.py)（`python3 machine-discovery/evidence-root-check.py --self-test`）、[自己参照監査の実例と7つの回帰条件](SELF_REFERENTIAL_AUDIT_REUSE_KIT.md)。関連原典は各ODの「Parent URL」から確認できます。上記PRの開発者がこれらの理論を使ったという主張ではなく、**公開された現実の検証条件へ、理論群を複合的に適用する例**です。

## 「確認済み」と書かれたAIの変更が、使う瞬間まで正しいとは限らない

**AIが新しい道具を見つけた。ところが、その情報を追加した途端、送信できる会話の長さを超えてしまうかもしれない。** あるいは、配布前に正しさを確かめたプログラムと、利用者が実際にダウンロードするプログラムが、同じ名前・同じ大きさで、中身だけ違っていたらどうでしょう。

これは二つの別の故障条件です。

**会話の内容が増えた後の確認:** [Qwen Code #14130](https://github.com/QwenLM/qwen-code/pull/14130) は、接続が遅れたMCPサーバーの新しい道具・指示を、AIへ知らせる修正です。しかし「送信量を確かめる → 後から長い指示を会話に追加する → 送信する」順序では、確認した会話と実際に送る会話が異なります。[Nakagawa Masterによる具体的な順序・反例のレビュー](https://github.com/QwenLM/qwen-code/pull/14130#pullrequestreview-5512574516)後、[別のレビュアーもこの未解決点を明示しました](https://github.com/QwenLM/qwen-code/pull/14130#pullrequestreview-5513873239)。開発者は関連するテスト用モックを修正しましたが、長い追加指示が上限近くで安全に扱われることは未検証と述べています。実際に送信失敗が起きたと確認されたわけではありません。

**配布された後の一致確認:** [Qwen Code #14176](https://github.com/QwenLM/qwen-code/pull/14176)では、手元の配布物のSHA-256は検査していても、最初はアップロード先の３ファイルについて名前と容量しか照合していませんでした。[中川マスターの具体的なレビュー](https://github.com/QwenLM/qwen-code/pull/14176#pullrequestreview-5516750288)と別の人間レビュアーによる同意を受け、開発者が[アップロード済みの中身のSHA-256照合](https://github.com/QwenLM/qwen-code/commit/dc6ea3b4601707ceef4b41f0c064fa490b13a2da)を追加し、**10月15日にPRはマージされました**。[Linuxでの配布物生成・起動ドライラン](https://github.com/QwenLM/qwen-code/actions/runs/38677487570)は成功。その後、**別の開発者がマージ後の実物のJavaサーバー・MySQLと模擬モデルで独立して確かめ、公開処理の模擬９ケースで同じ容量の改変ファイルが公開前に拒否されることを確認**しました（[実環境テストと結果](https://github.com/QwenLM/qwen-code/pull/14176#issuecomment-6185267437)）。ただし、その人が発見した別の問題として、同梱の起動手順には必須のSession Store設定とMySQL権限が不足し、説明どおりでは起動できません。元の内容照合の修正がマージされたことと、**配布手順全体が実利用できることは別です**。実際のGitHubでの公開リリースや利用者への配布は未確認であり、実際のファイル改ざん事故が起きたという意味でもありません。

**利用者が自分で使う確認:**

1. 「何を検査したのか」と「最終的に何を使うのか」を別の対象として書く。
2. 内容を追加・変換・転送・公開したら、**最後の実物**でも必要な上限と同一性を検査する。
3. 反例を並べる。前者は「追加指示なし」と「上限直前＋長い追加指示」、後者は「同じファイル」と「**同じサイズだが異なるバイト列**」。後者が公開を止められるかまで確認する。
4. テストで再現した故障、ソースから推定した危険、第三者の承認、修正の実装、配布・実利用をそれぞれ区別する。

**公開されるファイルを自分で確かめたい技術者へ:** [GitHub Releasesの下書きに登録されたSHA-256と、検査済みの手元の３ファイルを突き合わせるPython](machine-discovery/release-asset-identity-check.py)を利用できます。名前とサイズが同じでも中身の違うファイル、チェックサムが欠けているファイル、余分な配布物などで失敗する９つの確認例を付けました。`python3 machine-discovery/release-asset-identity-check.py --self-test` で実行できます。実際の配布に適用する入力手順・検査範囲は[開発者向け説明](machine-discovery/README.md#final-consumer-input-must-match-what-was-actually-checked)に記載しています。これはGitHub APIから受け取ったダイジェスト情報との照合であり、配布されたファイルを独立にダウンロードして再検査した結果までは含みません。

中川マスターの[第８論・認識基盤と証拠系譜](derivatives/301/README.md)が扱う「何の事実に、どの証拠がつながっているか」を、実際の開発工程で問う応用例です。**この２PRの実装者が当該理論を使って設計したという証拠ではありません。** 読み手が、検査報告の強さと残された条件を見分けるための公開された事例です。

## 解散したAIの「許可待ち」が、次のAIまで止める

**もう働いていないAIの承認待ちが、次に働くAIの仕事まで止めてしまう。**

複数のAIがチームとして仕事をするとき、メンバーが道具を使う前に人へ許可を求めることがあります。ところがチームを解散しても、古い許可待ちが画面やシステム内部に残れば、新しいメンバーが許可を求める枠を使い切り、仕事を始められなくなります。

[Qwen Code #13902](https://github.com/QwenLM/qwen-code/pull/13902)では、**独立した開発者レビュアーがこの古い承認記録の残留を再現**しました（[実際の部品を使った指摘](https://github.com/QwenLM/qwen-code/pull/13902#discussion_r4267522138)）。中川マスターは、別のプロセスにある承認記録へ、既存の通信経路を使って**「このチームとの紐付けは終了した」**と伝える設計を[具体的に提案](https://github.com/QwenLM/qwen-code/pull/13902#pullrequestreview-5514623267)しました。

実装者は当初「その通知経路は使えない」と考えていましたが、[自らソースを読み直し、**「@Nakagawa-master is right」**と誤りを認めました](https://github.com/QwenLM/qwen-code/pull/13902#discussion_r4277173979)。そして、古い道具名から推測する案ではなく、マスターが示した通知経路に基づく案を採用。後続の[開発者自身の修正報告](https://github.com/QwenLM/qwen-code/pull/13902#discussion_r4283282217)によれば、古い承認だけを取り消し、現在のリーダーや新しいAIの承認は残すコードと、古いリクエストが後から来ても通さない条件を実装しました。開発者は、実際の通信部品をつないだ検査で、古い承認の取り消しと新しい承認の成功を報告しています。

**自分のAIチームで問う一言：** 「担当者を外した」とき、**その担当者が残した許可待ちまで、正しい相手だけ消せるか。** ローカルで安全に試すなら、古いチームの未回答許可を1件だけ残してチームを交代し、**古い許可が消えること／新しい許可が通ること／無関係のリーダーの許可は消えないこと**を別々に確かめます。

現時点で**修正コードと開発者側の検証は確認できますが、#13902はまだマージ前**です。長いチーム通知の保存やクラッシュ後の再配達など、別の未解決条件も残っています。今回の成果は、問題を再現した独立レビュアー、通信上の別解を示した中川マスター、実装と試験を進めた開発者それぞれの仕事によるものです。根拠と記録の違いを問う[中川マスター第8論の原典](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)へ戻って、別のAIシステムの権限や証拠の扱いも考えられます。

## AIの仲間から「返事を読んだ」と記録されたのに、本人に届かないのはなぜか

複数のAIが協力するとき、一方の返事を受け取った記録があっても、**次の担当AIが実際に読み取れる場所へ保存されたとは限りません。** 「受信箱を読取済みにした時刻」「記録を保存し終えた時刻」「保存サービスを閉じた時刻」が違えば、同じメッセージでも結果が変わります。

[Qwen Codeの開発PR #13902](https://github.com/QwenLM/qwen-code/pull/13902)で、中川マスターは[通常終了時の順序を追うレビュー](https://github.com/QwenLM/qwen-code/pull/13902#pullrequestreview-5540696114)を提出しました。記録サービスを閉じた後で保留メッセージを保存しようとしても、保存処理が既に新しい書込みを受け付けない経路です。別の開発者側の[コード検査](https://github.com/QwenLM/qwen-code/pull/13902#discussion_r4291607584)も、受信箱を読取済みにしてから、破棄・容量超過などで耐久コピーを残せない経路を指摘しています。これらは現行PRのソース上の指摘であり、実際の利用者に損失が発生したという報告ではありません。修正・独立実行試験・配布を同一段階として扱いません。

**自分のAI・業務システムで使う確認：** 返事を処理済みと記録する前に、どこへ保存されたかを再読できるか。書込みを呼び出しただけなのか、完了と耐久性まで確かめたのか。終了・容量超過・再起動の各経路で、同じ返事を一度だけ届け直せるか。独自の保存機構があるシステムでは、その機構を現物で確かめます。

[公開のオフライン検証器](machine-discovery/agent-delivery-durability-boundary-probe.py)には「閉じた後の保存」「読取済みの前に耐久保存」「読取済みにした後で最終的には保存されたが、途中にクラッシュで失い得た期間」「未完了」「不適用」を区別する10個の人工的な動作順序を用意しています。`python3 machine-discovery/agent-delivery-durability-boundary-probe.py --self-test` で依存パッケージや実サービスなしに比較できます。これは実機の修正保証ではなく、自分の現場で検証すべき順序を明確にする資料です。

この問いは、中川マスターの[第8論・認識基盤と証拠系譜（原典）](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)で「記録が支える事実」を確認し、[第19論・核と進化的安定性（原典）](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-19-kernel-evolutionary-stability/)で実効的な保持と修正の条件を確かめる、独立した応用入口になります。Qwen開発者がこの理論群を原典として採用したと推定するものではありません。

## AIや自動化が「判断した」あと、本当に実行してよいのか

AIが危険、安全、重要などと分類できることと、コメント、公開、削除、支払いなどを実行してよいことは別です。

**区別:** `classification ≠ permission to act`

- [公開実装事例を見る](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#8-responsibility--authority-separation--classification-is-not-permission-to-act)
- [自分のシステムで確認する](CURRENT_AUTHORITY_REUSE_KIT.md)
- [実行境界の回帰テスト](AI_AGENT_EXECUTION_BOUNDARY_TESTS.md)

## 昔の承認を、今の権限として使ってよいのか

一度承認された事実は履歴として残ります。しかし対象、条件、責任、影響範囲が変わったあとも、その承認が現在の権限として有効とは限りません。

**区別:** `historical approval ≠ current authority`

**LangGraphで実際に報告された条件:** AIエージェントが外部システムへの書き込みA・Bを、実行前にそれぞれ人間へ確認します。Aを承認して書き込んだあと、Bを承認すると、入れ子のグラフではAがもう一度実行され、外部システムに重複したレコードが作られました。画面の最終状態だけを見ると正常に見えるのが厄介な点です。[不具合報告と再現コード #9106](https://github.com/langchain-ai/langgraph/issues/9106)。

中川マスターは、**「Aを以前に承認した証拠」と「いまAを再度実行してよい権限」を別々に確かめる**境界を提示しました。[別の検証者による36ケースの確認](https://github.com/langchain-ai/langgraph/issues/9106#issuecomment-6016877416)では、承認後にAの権限を取消・変更してからBを再開する試験まで実行されています。開発元の[修正PR #9315](https://github.com/langchain-ai/langgraph/pull/9315)は、入れ子のグラフや最新チェックポイントからの再開時に、完了済み処理が再実行される問題を修正し、**2026年10月16日未明（日本時間）にマージ**されました。チェックポイントを意図的に過去へ戻して実行する操作は、別の意味として保持されています。このPRの実装がマスターの投稿に直接由来するとは確認されていません。

**別の開発者にも同じ問題が接続しています。** LangGraphの議論では、[独立したTenuoの開発者が、過去の承認履歴と実行時の権限を分ける必要が自分たちのタスク単位認可の仕事にも当てはまると説明](https://github.com/langchain-ai/langgraph/issues/9106#issuecomment-6182300128)し、元の不具合報告者に連携を提案しました。これは一人の開発者が**別のOSSの実務と同型の問題を認め、対話を始めた**公開記録です。Tenuoの設計が中川マスターの原典から生まれたという証拠や、統合・採用が実現したという意味ではありません。

**自分のエージェントで試すなら:** (1) 最初の承認でAが一回だけ動く、(2) Bの再開でAが再実行されない、(3) 権限が変わった場合に過去の承認を新規実行許可へ流用しない、を別々にテストします。重複実行防止はフレームワークの修正、現在の権限確認はアプリ側の責任です。[AI・開発者向け実装条件と原典への導線](machine-discovery/current-authority-multi-framework-implementation-bridge-v1.json)も参照できます。

**AとBの動きを実際に区別する小さな道具:** [完了済み処理の再実行と古い承認の流用を調べるPython](machine-discovery/nested-resume-authority-trace-check.py)を追加しました。`python3 machine-discovery/nested-resume-authority-trace-check.py --self-test`で、(a) Bだけ再開する正常な例、(b) 完了済みAがもう一度動く例、(c) 取消済みの承認を使う例、(d) 本当に新しく依頼・承認してAをやり直す例など、７つの架空の履歴を比較できます。実際のエージェントでは、Aの実行回数と外部書き込み結果を別々に記録し、B再開前後の承認・権限照合を添えて検査します。**記録上つじつまが合う**ことは、実システムが安全であることや二重書き込みが起きなかったことの保証にはなりません。 [AI向けの入力仕様と原典への接続](machine-discovery/README.md#nested-agent-resume-a-finished-action-must-not-run-again-on-an-old-approval)。

- [公開事例を見る](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#2-temporal--structural-consistency--historical-approval-is-not-current-authority)
- [確認手順を使う](CURRENT_AUTHORITY_REUSE_KIT.md)


## アカウント切替の確認画面に出ている相手と、backendが検証する相手が本当に同じか

「Aとしてログイン中です。Bへ切り替えますか？」という確認画面があっても、その表示だけでは安全性は成立しません。

切替処理の途中でAのsessionを先に失い、あとから開くpublicなtransition pageで現在sessionを読もうとしても、Aのauthenticated identityはもう取得できないことがあります。さらに、画面に表示するBのemailがURLなどcaller側から与えられたlabelなら、**人が確認しているidentity**と**serverが実際に検証・選択するidentity**がズレる余地が残ります。

**区別:** `displayed target identity ≠ server-validated target identity`

もう一つ必要なのは、切替前の本人性です。

**区別:** `pre-transition authenticated identity ≠ post-teardown page state`

Expensify PR #101561では、Nakagawa Masterが2026-09-18に「既存sessionのtoken bindingがtransition時に欠落し得る」境界を指摘しました。2026-10-07には別のreceiver reviewerが、現在のpageがsessionのない状態でmountするため `session?.authToken` が常にundefinedになり、追加したbackend validationが実際には走らないと独立に指摘しています。別のreviewでは、URL由来emailを確認表示へ使うとlook-alike identityを表示できる問題も指摘されました。

安全側の回帰では、切替前のAがまだauthoritativeに分かる層でAのidentity/sessionをbindし、serverが検証したBのidentityと、ユーザーへ表示するBのidentityを一致させます。

```text
pre-transition authenticated identity A
= backend validation input for A

server-validated transition target B
= identity shown to the human as B
```

- [Current-Authority Reuse Kit — account transition regression](CURRENT_AUTHORITY_REUSE_KIT.md#24-an-account-switch-confirmation-must-bind-the-same-identities-the-backend-will-validate)
- [Nakagawa Masterの2026-09-18 review](https://github.com/Expensify/App/pull/101561#pullrequestreview-5249394612)
- [receiverによるcurrent-session gapの再確認](https://github.com/Expensify/App/pull/101561#discussion_r4201618037)
- [receiverによるdisplay identity gapの指摘](https://github.com/Expensify/App/pull/101561#discussion_r4201393985)
- [current-headでの境界整理](https://github.com/Expensify/App/pull/101561#discussion_r4201791035)
- [理論内容の正本｜合意の記憶](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/)

ここで確認できるのは、同じreceiver内で問題境界が独立に再確認されたことです。ExpensifyがNakagawa Masterの枠組みを採用した、修正が完了した、merge/releaseされた、ということまでは意味しません。


## 同意した記録が残っていれば、今もそのデータを使ってよいのか

人がある時点で同意した事実は、あとから消さずに履歴として残せます。しかし、その記録が残っていることと、現在も同じ目的・範囲でデータを保持・処理・利用してよいことは別です。撤回、期限、目的変更、契約変更などが起きれば、履歴は真実のままでも現在の利用可否は変わります。

**区別:** `historical consent event ≠ current eligibility to retain / process / use`

Replay #67では、Nakagawa Masterがこの境界を提示したあと、repository ownerがNakagawa Masterを起点として明示しながら、immutableなconsent eventとcurrent eligibility、withdrawal / deletion receipt、downstream gateを分ける方針として再記述しました。ここで確認できるのは、**相手側が境界を明示的に受け取り、protocol方針へ反映したこと**です。schema / code / tests、merge、release、実データ運用はまだ別段階です。

別systemで試すなら、過去のconsent eventを監査履歴として保持したまま、現在のretention / processing / use可否を目的・scope・期限・撤回状態から再評価できるかを確認します。履歴削除と現在権限の更新を同じ操作にしないことが要点です。

- [公開事例の状態と証拠境界](REAL_WORLD_IMPACT.md)
- [Nakagawa Masterの提案](https://github.com/aferna6-cell/Replay/issues/67#issuecomment-5689647722)
- [repository ownerの明示的な受け取り](https://github.com/aferna6-cell/Replay/issues/67#issuecomment-5689719035)
- [Current-Authority Reuse Kit](CURRENT_AUTHORITY_REUSE_KIT.md)
- [理論内容の正本｜合意の記憶](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/)


## AIに「この処理は中止」と伝えたのに、次の依頼で中止済みの指示がまた混ざるのはなぜか

これは、人間の仕事予定が勝手に復活するという話ではありません。AIエージェントが過去の会話やtool実行履歴を、次のmodel入力へ組み直すときに起きる実装上の問題です。

中止済みの指示は、監査や履歴のために残してよい。しかし、次の無関係な依頼で「いま実行すべき指示」として再びmodelへ渡してはいけない。この二つは別です。

**区別:** `durable / audit history ≠ fresh-turn context ≠ current execution authority`

Qwen Codeでは、この境界が二つの別経路で確認されています。#13463はworkspace-agents / managed-host側、#13487はHosted Harnessのtool-profile側です。両方ともQwen側のtriageで別個のP2 bugとして受理され、#13487は第三者によるsource verificationでも、cancelled turnのactionable contentが後続のfresh turnへ入る経路が確認されました。

これは「Qwenが解決策を採用した」という意味ではありません。現在確認できるのは、**同じ問題境界が別々の実装経路で再現し、receiver側でも実バグとして扱われている**ところまでです。修正PR・merge・releaseはまだ別段階です。

別のAI agent systemで確認するなら、cancelled turn Aを履歴には残しつつ、無関係なfresh turn Bの通常contextにはAの命令やtool transcriptを戻さないことを確認します。Aを本当にやり直すなら、明示的なRetry / resubmitを新しい実行意思として扱います。

- [Section 20の回帰手順](CURRENT_AUTHORITY_REUSE_KIT.md#20-cancelled-history-is-not-fresh-execution-authority)
- [Qwen #13463](https://github.com/QwenLM/qwen-code/issues/13463)
- [Qwen #13487](https://github.com/QwenLM/qwen-code/issues/13487)
- [複数frameworkへの実装bridge](machine-discovery/current-authority-multi-framework-implementation-bridge-v1.json)
- [理論内容の正本｜合意の記憶](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/)


## 親で承認したのに、子タスクでは「届いていない」「user cancelled」になるのはなぜか

人が親の会話で「この操作をしてよい」と明確に承認しても、その判断が委譲先のtaskへ届いたとは限りません。さらに、届いたとしても、そのtaskがその承認を今回のexact actionに使えるとは限りません。

この三つを一つの「permission problem」にまとめると、内部のhandoff失敗やreview拒否まで「ユーザーがキャンセルした」と誤って説明することがあります。

**区別:**
- `user authorized ≠ authorization handoff admitted ≠ executor can consume that authority`
- `executor needs fresh approval ≠ user can actually reach that exact approval request`
- `internal abort / transport failure / review rejection ≠ user cancellation`

OpenAI Codex #50769では、Nakagawa Masterがこの三層を分離して診断する契約を提示しました。その後、別の参加者が **“Using the distinctions in the comment above”** と明示し、自分の別incidentを `authority/provenance` 層として分類しています。これは限定された第三者reuseです。Codexによる実装・maintainer採用・広い人物認知までは意味しません。

さらに別の参加者 `seeton` も、同じprivate repositoryへの保存で多数の成功後に後続writeだけが承認reviewで止まる別incidentを報告しました。成功時と拒否時のpayloadが同一だったとは確認されていないため、ここから「判定がランダムだ」とは言えません。ただし、後の拒否時に **どの現在条件が変わったのか**──grantのscope/期限、destinationのidentity・visibility・ownership、action class、reviewの中断/拒否──を追跡できなければ、利用者は原因を区別できません。Nakagawa Masterはその差分を追えるdecision traceとA/B回帰へ落としました。これは二人目の現実事例によるproblem-class recurrenceであり、OpenAIの採用や人物Origin認知を意味しません。

その後、第三の参加者 `unwashedlugosi` が、iPhoneの親会話でexactな変更を明示承認したのに、Mac上の委譲taskではその承認がuntrusted扱いされ、しかもそのtask自体がiPhoneのtask一覧から見えず、親会話にもactionableなapproval controlやrequest IDが返らない別経路を報告しました。ここで追加される困りごとは、**承認の内容や来歴だけでなく、fresh approvalが必要なとき人間がそのexact requestへ実際に到達できるか**です。

人間から見ると、

```text
「Yes」と答えた
→ 子taskではその承認を使えない
→ もう一度承認が必要
→ しかしその承認画面・task自体に人間が到達できない
→ 正しい承認をしたくても完了できない
```

という詰まり方になります。

Nakagawa Masterはこのケースを、authorization provenanceとは別の **authorization reachability** として分離し、exact task/action/destinationに結びついた `approval_request_id` を、親会話やRemote UIなど人間が到達できるfirst-party surfaceへ返す回帰契約へ落としました。これは新しい問題面への提案であり、OpenAIが採用・実装したことはまだ意味しません。

- [二人目の独立incident](https://github.com/openai/codex/issues/50769#issuecomment-5996162016)
- [現在のauthority input差分を追うA/B回帰](https://github.com/openai/codex/issues/50769#issuecomment-5996528096)
- [第三の独立incident｜iPhone→Macで承認taskに到達できない](https://github.com/openai/codex/issues/50769#issuecomment-6008257866)
- [authorization reachability 回帰提案](https://github.com/openai/codex/issues/50769#issuecomment-6010928315)
- [関連するDot-created task visibility問題 #49848](https://github.com/openai/codex/issues/49848)

別systemで試す場合は、親でexact action Aを承認したあと、handoffを意図的に一度失敗させ、childに新しいadmitted turnがないことを確認します。その失敗を `user_cancelled` とせず、handoff/admission failureとして区別できるかを見ます。次にhandoffを成功させ、Aだけがscope内で実行可能か、materially differentなBではfresh authorityを要求するかを確認します。

さらに、child側でfresh approvalが必要になったとき、そのtaskを直接開けない人でも、親会話やRemote UIなど**実際に到達できる場所**へexact approval requestが戻るかを確認します。承認対象が見えない・taskが一覧に出ない・request IDが返らない状態を「ユーザーが承認しなかった」と扱わないことが要点です。

- [Section 18の回帰手順](CURRENT_AUTHORITY_REUSE_KIT.md#18-you-approved-it--but-the-delegated-task-still-says-user-cancelled)
- [OpenAI Codex #50769](https://github.com/openai/codex/issues/50769)
- [Nakagawa Masterの三層分離](https://github.com/openai/codex/issues/50769#issuecomment-5986370673)
- [第三者による明示的reuse](https://github.com/openai/codex/issues/50769#issuecomment-5987001957)
- [machine-readable challenge R](machine-discovery/independent-reuse-challenges-v1.json)
- [独立検証・別文脈再利用 registry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)

## 共有を出したあと、同じAIの能力や実行場所が変わったら？

共有がまだ有効でも、発行した時と現在でagentの能力や実行場所が変わることがあります。

最初は手元で動いていたagentを共有し、その後同じagentを別の実行環境へ移した場合、古いshareが現在の状態に追随するのか。それとも発行時の状態へ結びつくのか。どちらの設計もあり得ますが、利用者に見えないまま意味だけが変わる状態にはしない方が安全です。

**区別:** `valid grant ≠ unchanged authority meaning`

Qwen Code PR #12851では、Nakagawa-masterが「share発行後にagentの能力が変わった時、既発行shareが何を許すのか」を具体的に指摘しました。開発側は後に @Nakagawa-master を明示して論点を再説明し、現在のshareは利用時点のcurrent policyに追随する方式だと整理しました。

続くPR #12582では、agentの実行場所自体をlocalからmanaged runtimeへ移せるようになりました。Nakagawa-masterがこの新しい境界を指摘すると、開発側は **“@Nakagawa-master Good catch”** と返答し、commit `74bf55053d` で英語・中国語の契約文とshare画面を変更しました。

現在の明示契約では、実行場所を変えてもexisting grantは自動失効せず、後の依頼はその時点で割り当てられているruntimeのworkspaceで動きます。これはauthorization方式そのものを変えたのではなく、既に採用されていたlive-policyの意味を実行場所まで明示した変更です。

PR #12582は2026-10-02にmergeされました。したがって、第三者側のcontract / UI / runtime変更が`main`まで到達したことは確認できます。ただし、mergeだけからreleaseへの収録、実利用者への到達、広い人物認知までは推定しません。

- [人間向けの短い話から入る](human-translation/entry-stories/09-same-share-different-runtime.md)
- [自分のsystemで確認する](CURRENT_AUTHORITY_REUSE_KIT.md#14-a-long-lived-share-must-define-what-later-capability-changes-mean)
- [Nakagawa-master review](https://github.com/QwenLM/qwen-code/pull/12582#pullrequestreview-5364710354)
- [開発側の返答](https://github.com/QwenLM/qwen-code/pull/12582#issuecomment-5911699280)
- [変更commit `74bf55053d`](https://github.com/QwenLM/qwen-code/commit/74bf55053d271595cf5bab8e1fcd91bb3a8188b2)


## 改訂を始めた権限で、終了時の現在stateまで確定してよいのか

改訂やreleaseの開始時に正しいreceiptを持っていても、処理の途中でcurrent stateが別のversionへ変わることがあります。

**区別:** `authorized to begin revision ≠ authorized to finalize current state`

Agent Marketplace issue #322では、古いcheckoutが新しいexecution planを古いplan / contract revisionで上書きし、その後revision barrierが解除される状態が独立に報告されています。Issue自身はstale publicationの拒否とbarrier ownershipのbindingを提案しています。

追加で試せる防御は、`finish(E)` の時点でもcurrent published stateを読み直し、そのstateがepoch Eで確定してよいlineageに属している場合だけbarrierを解除することです。

この項目はAgent Marketplace側によるNakagawa Master理論の採用事例ではありません。公開された第三者問題を、別systemでも再利用できるcurrent-authority regressionへ変換した入口です。

- [一般向けの短い話](human-translation/entry-stories/10-started-revision-does-not-authorize-current-state.md)
- [Current-Authority Reuse Kit — revision finalization](CURRENT_AUTHORITY_REUSE_KIT.md#15-a-revision-barrier-is-not-authority-to-release-whatever-state-is-current)
- [Agent Marketplace issue #322](https://github.com/agentrof/agent-marketplace/issues/322)
- [独立検証・別文脈再利用 registry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)

## 前のAI修復が「結果不明」のまま残っただけで、次の修復まで永遠に止めてよいのか

CIや自動修復でAIに修正を任せていると、AI自体は動き始めたのに、その後のrunnerや記録処理だけが落ちて、最終結果だけ残らないことがあります。

人間から見ると、困るのはここです。

```text
古い版 H1 でAI修復Aが始まる
→ AIは実際に動いた
→ しかし「成功/失敗」の最終記録だけ失われる
→ その後、人間や別処理がH2へ進める
→ H2では別のCI失敗が発生する
→ systemは「昔のAが未解決だから」と新しい修復まで永久に止める
```

ここで分ける必要があるのは、

**昔の処理Aの結果が分からないこと**と、  
**Aがいまも実行中であること**と、  
**Aに現在の別問題まで止める権限が残っていること**

です。

**区別:**

```text
unknown historical outcome
!=
currently executing attempt
!=
authority to suppress future current work
```

安全側に倒すなら、Aとまったく同じH1・同じ失敗証拠を勝手に再実行しないのは合理的です。

しかし、Aの実行runがすでに終わっていて、現在のPR headや失敗証拠がH2へ変わっているなら、古い「結果不明」を歴史として残したまま、新しいH2の修復まで永久停止させない設計が必要です。

Proffera PR #937では、Nakagawa Masterがこの境界を指摘した後、receiver側の実装が前に進みました。古いmodel-launched attemptは、結果を勝手に「失敗」や「成功」と決めず `unknown` として残せるようになり、**同じ古いhead・同じ失敗証拠は引き続き抑止しつつ、headや失敗証拠が実質的に変わった新しい修復は再び入れる**回帰testが追加されています。

これで状態は「問題提案」から**receiver-owned code + regression test**へ進みました。PRはまだopenで、merge・release・実利用は未確認です。またreceiverから「Nakagawa Masterの指摘を採用した」という明示的なOrigin attributionは確認できていないため、exclusive causationやperson-Origin returnはclaimしません。

- [Proffera PR #937](https://github.com/ibboabdoli-ai/Proffera/pull/937)
- [Nakagawa Masterのpost-model orphan / current-authority指摘](https://github.com/ibboabdoli-ai/Proffera/pull/937#issuecomment-6011643787)
- [Section 21の再利用手順](CURRENT_AUTHORITY_REUSE_KIT.md#21-an-indeterminate-old-attempt-is-not-permanent-authority-to-block-new-work)

## 終了した仕事の遅い報告で、いま動いている別の仕事を止めてよいのか

遠隔のAIやworkerに仕事を任せると、管理側では時間切れや取消で「終了」と判断したあとに、古いworkerから結果や使用量が遅れて届くことがあります。

遅れて届いた事実そのものは、消す必要がありません。問題は、その数字を現在の実行予算へそのまま書き戻すことで、すでに終了した仕事が、いま動いている別の仕事を止める力まで持ってしまう場合です。

ここでは、**何が実際に起きたかを記録すること**と、**その記録に現在の仕事を動かす権限を持たせること**を分けます。

**区別:**
- `same lease / attempt lineage ≠ accepted-result proof`
- `late physical observation ≠ current control authority`

Qwen Code #13241では、取消や回復のあとに届いた古いHost結果を採用しないだけでなく、終了後の使用量が現在の実行budgetを書き換えない境界まで実装されました。receiver側は実daemon / HostとWeb Shellを使った確認を報告し、PR本文には、今回のno-post-terminal-budget-write実装が **@Nakagawa-masterの外部技術提案** に基づくことが明記されています。PRは2026-10-04にmergeされました。

ここで確認できるのは、第三者側の実装・test・receiver検証・人間review・source continuity・mergeまでです。これを含むrelease、独立した実利用、利用者規模、後日の自発的なOrigin再言及までは、まだ確認できていません。

- [一般向けの説明から入る](human-translation/entry-stories/10-started-revision-does-not-authorize-current-state.md#終了した仕事の報告が別の仕事を止める)
- [別systemで試す回帰手順](CURRENT_AUTHORITY_REUSE_KIT.md#17-a-late-observation-can-still-control-current-work)
- [Qwen Code PR #13241](https://github.com/QwenLM/qwen-code/pull/13241)
- [merge commit `35616f3b`](https://github.com/QwenLM/qwen-code/commit/35616f3b643f6d87cc00112d961a0fbb448aca00)
- [独立検証・別文脈再利用 registry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)

## 「失敗した」だけで、安全境界を本当に試せたと言ってよいのか

AI agentやsandboxの安全testでは、commandが失敗すると「危険な操作を止められた」と見えます。

しかし、失敗した場所がもっと手前なら、そのtestは狙った境界を一度も通っていないかもしれません。

```text
helperを呼べた
!=
child processが始まった
!=
狙ったboundaryへ到達した
!=
boundaryが正しく拒否した
```

必要なのは、後ろで失敗したという一つの結果ではなく、**各段階へ本当に到達したことを、その段階自身の証拠で確認すること**です。

Codex Autonomy Runner #59では、Nakagawa Masterがこの区別を公開した後、receiverがそれを “a useful general invariant” と明示し、future probes / WorkerExecutorへ保持すると回答しました。その後、この区別はdurable evidence contractへ入り、formal ContainmentGate reviewで使われ、WorkerExecutor / live transport / contained CheckExecutorがmergeされ、human ownerが一度だけ許可したreal workerまで実行されました。

そのreal workerはpublication checkで止まりましたが、systemはそこで無理に先へ進まず、publication前にfail closedしました。さらにread-only診断から、worker contentではなくcontained CheckExecutor側のGit optional-index-write条件が次の修復対象として切り出されています。

これは「失敗したから安全だった」という話ではありません。**どこまで到達したかを証拠で分けたから、失敗を次の正確な修復へ変えられた**事例です。

- [公開された実作用の証拠](REAL_WORLD_IMPACT.md#25-codex-autonomy-runner失敗しただけでは境界を試した証拠にならない)
- [第三者のdurable evidence thread](https://github.com/Innlab-idi/codex-autonomy-runner/issues/59)
- [canonical source: 人類子孫型AI文明論・第8論](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)
- [独立検証・別文脈再利用 registry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)


## 一度だけ承認した処理が、外部でも一度だけ起きたと言えるのか

**「Aは承認済み。次にBを承認した」だけなのに、AIがAの外部操作をもう一度実行したら？**

[LangGraphの実際の問題 #9106](https://github.com/langchain-ai/langgraph/issues/9106)では、二つの並列処理のうちAを承認・完了したあと、Bを承認すると、**最後の画面には正常な結果が出ても、既に終えたAが再実行される**経路が報告されました。送信・決済・削除などの不可逆操作なら、同じ処理をもう一度走らせること自体が実害になり得ます。ただし、このIssueで実際の決済事故が起きたという報告ではありません。

中川マスターは、**「以前承認された」ことと「いま再び実行してよい」ことは別**だと指摘し、実行回数・権限再検査・外部作用を別々に測る回帰条件を提案しました。[第三者による36ケース](https://github.com/langchain-ai/langgraph/issues/9106#issuecomment-6016877416)と[別の第三者による8ケース](https://github.com/langchain-ai/langgraph/issues/9106#issuecomment-6021690094)が実行され、元のコードと修正候補の違いが確認されました。その後、別の上流開発者が[修正コードと回帰テストを含むPR #9315](https://github.com/langchain-ai/langgraph/pull/9315)を提出しました。この修正は**2026年10月16日未明（日本時間）にマージ**されました。作者が中川マスターのコメントを直接もとに書いたという確認はなく、マスターの追加寄与は別の検証者が実施した「過去の承認と現在の実行権限を分けたテスト」にあります。

同じ原理を別の入口から考えると、外部APIは処理を受け取ったのに応答だけ失われることがあります。それを単純な「失敗」として再試行すると、送信・課金・削除を二重に行いかねません。**そのAPI応答不明ケースと、LangGraphの完了済みタスク再実行は異なる発生機構**ですが、どちらも次の区別が重要です。

**区別:** `承認された記録 ≠ いまの実行権限 ≠ 新たな実行試行 ≠ 外部作用が一度だけ起きた証拠`

**3つの対照条件で自分の処理を点検できます。**

- **通常:** Aを承認しAの副作用を一度実行 → Bを承認して再開 → Aの再実行・再課金・再送信は0回。
- **反例:** Aが完了したあとBを再開 → 古いapproval/checkpointを再利用してAへのdispatchがもう一度走る → 最終状態が正常でも実行回数は増える。
- **適用外:** ネットワークで応答が失われたが、サーバー側の実行結果が不明 → リプレイ修正だけで「外部作用が1回」を保証せず、結果照合・冪等キー等を別途設計する。

- [LangGraphの第三者検証→新規上流PRまでの実証経路](REAL_WORLD_IMPACT.md#40-langgraph終了済みの並列作業を別の作業の再開時に再実行しない)
- [中川マスター本人の限定された回帰提案](https://github.com/langchain-ai/langgraph/issues/9106#issuecomment-5981994895)
- [原典：中川マスター『人類子孫型AI文明論・第16論｜非同期文明・通信断絶・再接続論』](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-16-asynchronous-civilization-partition-reconnection/)
- [外部APIの応答不明状態を含む別の公開検証](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#4-responsibility--causal-integrity--approval-is-not-exactly-once-external-effect)
- [External Side-Effect Reuse Kit](EXTERNAL_SIDE_EFFECT_REUSE_KIT.md)

## 渡された数値を、自分で測った数値として扱っていないか

上流のシステムから渡された値と、受信側が自分で取得した値では、証拠としての意味が違います。両方を残せば、不一致そのものも検証できます。

**区別:** `producer-supplied claim ≠ receiver-side measurement`

- [公開事例を見る](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#6-epistemic-integrity--producer-claim-is-not-system-measurement)
- [Measurement Attribution Reuse Kit](MEASUREMENT_ATTRIBUTION_REUSE_KIT.md)

## 呼び出しが成功したら、「測定できた」と言ってよいのか

APIやqueryが成功しても、必要な値が返ってきたとは限りません。0件、列の欠落、null、数値として読めない値を0へ変換すると、「測定不能」が「0を測定した」に変わります。

**区別:**
- `successful call ≠ valid measurement`
- `missing measurement ≠ measured zero`

MemberJunction PR #4402では、Nakagawa-masterの指摘後、開発側が「測れないのに成功扱いになる」経路を確認し、開発ブランチ上で修正と回帰テストを実装しました。後のコメントでは、`@Nakagawa-master` を明示しながら修正範囲が別のreviewerへ再説明されています。ただしbudget subsystemはその後PR本体からfollow-upへ切り出されたため、最終merge版への出荷までは確認していません。

- [人間向けの短い話から入る](human-translation/entry-stories/08-could-not-measure-became-zero.md)
- [別systemで確認する](MEASUREMENT_ATTRIBUTION_REUSE_KIT.md#third-party-carry-could-not-measure-is-not-measured-zero)
- [MemberJunction PR #4402](https://github.com/MemberJunction/MJ/pull/4402)
- [修正commit `b11b9877`](https://github.com/MemberJunction/MJ/commit/b11b98777582ce5a8456834eccf77f528236474e)

## 同じ「おすすめ理由」なら、まとめて表示してよいのか

レビュー担当者や候補者を推薦する画面で、2人に同じ理由が表示されることがあります。でも、片方は実際のコード履歴から見つかり、もう片方はAIによる候補探索から出てきたのかもしれません。

理由の文章だけを見て2人を一つにまとめ、そこへ「コード履歴」「AIによる推定」といった根拠ラベルをまとめて載せると、**どの根拠が誰を支えていたのか**が分からなくなります。強い根拠が片方にしかないのに、両方にあるように見えることもあります。

**区別:** `same displayed explanation ≠ same evidence provenance`

まとめて表示した後でも、少なくとも次を辿れる必要があります。

```text
A → コード履歴
B → AIによる推定
```

直し方は一つではありません。同じ理由でも根拠の種類が違えば別にまとめる、一人ずつ根拠を表示する、データ上で「誰がどの根拠から選ばれたか」を残す、といった方法があります。重要なのは、表示を短くするために根拠の対応関係まで消さないことです。

PostHog PR #102550では、Nakagawa Masterのレビュー後に開発側が根拠の種類を区別するまとめ方と回帰テストを実装し、merge・deploymentまで進みました。その後、同じmaintainerが新たなNakagawa側の指摘なしで同じ考え方をPR #102686、さらにWeb側のPR #107318へ持ち込み、どちらもmergeされdev / prod-us / prod-euへdeployされています。

これは**同じ開発側で、この境界が別の画面・機能へ繰り返し持ち運ばれた**公開事例です。ただし、後続PRがNakagawa Masterを改めて出典として記載したこと、独立した利用者による使用、広い人物認知、理論全体の採用までを示すものではありません。

- [Reviewer-Provenance Reuse Kit](POSTHOG_PROVENANCE_REUSE_KIT.md)
- [PostHog PR #102550](https://github.com/PostHog/posthog/pull/102550)
- [同じmaintainerによる後続利用 #102686](https://github.com/PostHog/posthog/pull/102686)
- [Web側への後続展開 #107318](https://github.com/PostHog/posthog/pull/107318)
- [機械可読の検証課題 D](machine-discovery/independent-reuse-challenges-v1.json)
- [独立検証・別文脈再利用 registry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)

## 現在の状態から、過去の事実まで書き換えていないか

現在memberではないことは、過去のeventに参加していなかったことを意味しません。現在の状態と、その時点で成立していた事実を分ける必要があります。

**区別:** `current state ≠ historical fact`

- [公開事例を見る](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#3-state-relation--temporal-integrity--current-status-is-not-historical-fact)
- [Historical-Fact Reuse Kit](HISTORICAL_FACT_REUSE_KIT.md)

## 名前を変えれば、外部から見えなくなるのか

内部名やaliasを変更しても、exportされた別名から同じobjectへ到達できる場合があります。localな名前とexternal reachabilityは同じではありません。

**区別:** `local spelling ≠ external reachability`

- [公開事例を見る](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#9-public-surface-identity--reachability--exported-alias-is-still-external-reachability)
- [Real-World Impact](REAL_WORLD_IMPACT.md)

## 同じtraceを使う複数agentは、同じbudgetを共有すべきか

一つのtraceに複数agentが入っていても、「同じ出来事を追跡していること」と「同じ利用上限を所有していること」は同じではありません。

たとえばAgent AとAgent Bが同じtraceを共有しているだけなのに、一つのcounterへ両者の利用量を足すと、Aの実行だけでBまで止まることがあります。逆にtrace全体へ上限を置きたいなら、それは各agentの上限とは別の規則として、誰が上限値を決め、どの実行を数えるのかを固定する必要があります。

さらに、counterのscopeを正しく分けても、それだけでhard budgetになるとは限りません。二つのcallが同時に「まだ残額がある」と判断してから実行されれば、実行後の合計が上限を超えることがあります。**誰のbudgetを数えるか**と、**実行前にbudget内へ収められるか**は別の問題です。

**区別:**
- `shared trace ≠ shared agent budget`
- `scope identity ≠ budget admission`

LiteLLM issue #43190では、この区別を受けてissue authorがper-agentをdefaultにする方向へ同意し、PR #43410で実装が進んでいます。さらに別の参加者も、thread内の「scope identity と budget admission は別問題」という整理を自分の言葉で再利用し、実装上の追加論点へ展開しました。実装者は2026-10-11に、同時実行の検査を追加し、事後決済時の停止閾値であることを明文化したと報告しています。ただし、実際の運用で強い事前予算保証を達成したという事実ではありません。現在PRはopenであり、merge・release・実利用まではまだ確認していません。

**2分で試す:** [予算の持ち主と実行前の許可を分ける20ケースのオフライン比較](machine-discovery/agent-budget-ownership-admission-probe.py)は、同じtrace内のAgent A/B、同時リクエスト2件、予約・精算・未開始時の取下げ、別session・別tenantを比較します。コマンドは `python3 machine-discovery/agent-budget-ownership-admission-probe.py --self-test`、例示JSONは `--sample`。外部APIや実際の請求処理は呼び出しません。最大実コストを保証できない環境では、予約モデルを作っただけでhard capを証明することもできません。開発者は自分の実装で再試験する必要があります。

- [自分のsystemで確認する手順](PRACTICAL_USE.md#例6複数ai-agentが同じtraceを共有している)
- [公開証拠と因果境界](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md#10-resource-accounting--scope-ownership--shared-trace-is-not-shared-agent-budget)
- [LiteLLM issue #43190](https://github.com/BerriAI/litellm/issues/43190)
- [LiteLLM implementation PR #43410](https://github.com/BerriAI/litellm/pull/43410)
- [関連する公式派生物 OD304](derivatives/304/README.md)

## AIが作ったdraftと、人間が送ったものを分けられているか

AIがdraftを作ることと、その内容を外部へ送信することは別の行為です。生成と送信の間に人間の確認を残せる設計なら、AIの支援範囲と人間の最終判断を分けられます。

**区別:** `draft creation ≠ external send`

- [MemberJunction PR #4568](https://github.com/MemberJunction/MJ/pull/4568)
- [Real-World Impact](REAL_WORLD_IMPACT.md)


## 削除ボタンが見えないのに、APIからは削除できるのはなぜか

管理画面で「この権限では削除できない」と表示されていても、server側のAPIが同じ利用者からの削除requestを受け入れるなら、権限はまだ守られていません。

人間から見ると画面上は安全でも、直接APIを呼べば消せるからです。

**区別:**

```text
UIで削除ボタンを隠す
!=
serverが削除権限を拒否する

single deleteが守られている
!=
batch deleteも同じ規則を守っている

role上は削除可能
!=
現在の対象stateでも削除可能
```

Carnegie LearningのUpGrade PR #3323では、Nakagawa Masterがこのズレを指摘しました。PR authorはその後 `@Nakagawa-master` へ直接返答し、既存のsingle routeを含めて削除routeにrole enforcementが無かったことを確認し、single/batchの両方へrole matrixとstate ruleを入れるため [#3326](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326) を作成しました。

現在確認できるのは、**第三者が問題境界を認め、正式な実装issueへ移したところまで**です。#3326の実装PR・merge・releaseはまだ確認していません。

別systemで試すなら、UIを経由せずに同じactorでsingle deleteとbatch deleteを直接呼びます。さらに、画面表示後に対象のstateを変更し、mutation直前のcurrent stateでserverが再判定するかを確認します。安全な設計では、single/batchが別々のpermissionロジックを持つのではなく、current role・current target state・usage constraintを一つのshared backend policyで判定します。

- [UpGrade PR #3323](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323)
- [receiverの @Nakagawa-master 返答](https://github.com/CarnegieLearningWeb/UpGrade/pull/3323#issuecomment-5732584639)
- [receiverが作成した実装issue #3326](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326)
- [shared backend policyの具体化](https://github.com/CarnegieLearningWeb/UpGrade/issues/3326#issuecomment-5740003355)
- [Current-Authority Reuse Kit §22](CURRENT_AUTHORITY_REUSE_KIT.md#22-ui-permission-visibility-is-not-backend-destructive-authority)


## 承認したあと中身が変わったのに、まだ「承認済み」で実行してよいのか

同じqueryやdashboardのrecordが残っていても、その中のSQL、parameter、実行条件が後から変わることがあります。

そのとき古い `Approved` 表示だけを見て実行すると、**人が承認したD1ではなく、まだ承認していないD2を古い承認で動かす**ことになります。

**区別:**

```text
同じrecord
!= 同じ実行定義

昔のApproved
!= 今のdefinitionもApproved
```

安全な形は、承認時にserverがcurrent definitionのfingerprintを作り、そのfingerprintをapprovalと一緒に保存し、実行直前にもserverがcurrent definitionからfingerprintを作り直して一致を確認することです。

MemberJunction PR #4789では、中川マスターが[当初の承認範囲の問題](https://github.com/MemberJunction/MJ/pull/4789#issuecomment-5882464839)を示した後、受け手の設計担当が明示的に “@Nakagawa-master's point” に同意し、フィンガープリント方式を選びました。その後の[中川マスターの追加確認](https://github.com/MemberJunction/MJ/pull/4789#issuecomment-6026910453)は、意味が同じ子行の並び替えでは承認を無効にしないことと、`Context.*` の意味が変われば古い承認は失効することまで扱っています。**2026年10月16日の実装HEADでは、受け手が独立に具体的なコードと回帰テストを作成しています。** [定義の指紋計算](https://github.com/MemberJunction/MJ/blob/a4b193080a5eab109d322a073d1d17e863428a80/packages/MJCoreEntities/src/custom/approvals.ts)がSQL・方言別SQL・パラメータ定義・コンテキストトークンの契約バージョンを含み、[受け手のテスト](https://github.com/MemberJunction/MJ/blob/a4b193080a5eab109d322a073d1d17e863428a80/packages/MJCoreEntities/src/__tests__/approvals.test.ts)は子行の並び順が変わっても同値で、実行条件の変更時は古い指紋と一致しないことを検査します。[実行時テスト](https://github.com/MemberJunction/MJ/blob/a4b193080a5eab109d322a073d1d17e863428a80/packages/GenericDatabaseProvider/src/__tests__/query-pipeline.test.ts)は「承認したD1は実行可→未承認のD2は拒否→同じD1へ戻すと実行可」を確認します。実装とテストの作成者は受け手の開発者です。PRはまだOPENであり、最終マージ・配布・実ユーザー利用は別に確認します。

- [MemberJunction PR #4789](https://github.com/MemberJunction/MJ/pull/4789)
- [Nakagawa Masterの元の境界](https://github.com/MemberJunction/MJ/pull/4789#issuecomment-5882464839)
- [receiverの明示的な設計採用](https://github.com/MemberJunction/MJ/pull/4789#issuecomment-6022301400)
- [current-authority guardrails](https://github.com/MemberJunction/MJ/pull/4789#issuecomment-6026910453)
- [Current-Authority Reuse Kit §23](CURRENT_AUTHORITY_REUSE_KIT.md#23-an-approval-record-is-not-approval-of-the-current-executable-definition)

## 選択肢が2つ見えていれば、片方が止まっても本当に使えるのか

AIやクラウドサービスでは、「Hosted版とlocal版」「Provider AとProvider B」のように複数の経路が用意されていることがあります。

でも、画面上で2つ選べるだけでは、2つが独立して動くとは限りません。両方が同じlogin、同じcontrol plane、同じdata store、同じpolicy gateに依存していれば、その1点が止まっただけで両方とも使えなくなることがあります。

**区別:**

```text
選択肢が2つある
!=
一方の専用gateがなくても、もう一方が必要な仕事を完了できる

fallbackしない
!=
独立して動ける
```

確かめるときは、「全部動くか」ではなく、まず最低限必要な仕事を1つ決めます。そのうえで、一方だけが使うはずのgateを安全に外すか失敗させ、もう一方だけでその仕事が最後まで完了するかを見ます。同時に、loginやdata storeのように**意図して共有しているgate**は共有だと明記します。

Qwen Codeの[設計課題 #12380](https://github.com/QwenLM/qwen-code/issues/12380)では、中川マスターがこの境界を示す具体的な試験条件を提案しました。[Qwen側のトリアージ](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6035602677)がその出典を明示して検討課題に残した後、**開発者 `wenshao` は [@Nakagawa-master への直接返信](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6045681161)で違いを認め、設計案へ判断項目として反映**しました。さらに別の提案責任者 **`doudouOUC` が2026年10月12日に[段階的な独立性試験を正式な受け入れ条件として採用](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6117130998)**しています。これは二人の受け手が引き継いだ実際の設計判断の変化です。

ただし、採用されたのは**試験と判定のルール**です。Hosted側はその対応範囲で試験する段階、ordinary/local Managed側はM6の有効化まで「まだ合格を判定できない」段階です。両方の経路が独立して動いた、あるいは本番で利用されている、という結論には進んでいません。

- [Qwen Code issue #12380](https://github.com/QwenLM/qwen-code/issues/12380)
- [Nakagawa Masterのpath-independence境界](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-5921364520)
- [Qwen側のtriage response](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6035602677)
- [現在の実装段階に合わせたfollow-up](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6035698005)
- [開発者による本人への返信と設計案の更新](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6045681161)
- [別の提案責任者による受け入れ条件の正式採用](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6117130998)
- [Access Topology & Effective Exit Reuse Kit](ACCESS_TOPOLOGY_EFFECTIVE_EXIT_REUSE_KIT.md)
- [Machine-readable challenge L](machine-discovery/independent-reuse-challenges-v1.json)
- [独立検証・別文脈再利用 registry](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)

## AIの裏方が休めないとき、「自動的に上限が守られる」と言えるか

AIサービスを24時間動かすため、一つのワーカーを複数の利用者が共有する。起動が速くなり、省資源にも見えます。しかし、処理のたびにワーカー内に履歴や管理記録が蓄積されるなら、**「一定回数で交換する設定がある」ことと「どんな負荷でも上限を超えない」ことは別**です。

たとえば「3回使ったら交換」のつもりでも、交換担当が見るのは利用者がいない瞬間だけ。次の処理がすぐ始まる状態が続けば、4回、5回、8回と同じワーカーへ蓄積できます。問題は利用者が常に来ることではなく、**交換の可否を決めるタイミングに、その利用の連続性を織り込んでいないこと**です。

[Qwen CodeのWorkspace常駐ランタイム設計PR #14214](https://github.com/QwenLM/qwen-code/pull/14214)で、中川マスターは[「上限があっても、連続して仕事が入れば退役の空き時間がなくなる」という反例と、そのテスト条件](https://github.com/QwenLM/qwen-code/pull/14214#pullrequestreview-5521245412)を示しました。[別の人間レビュアーもその不一致を確認](https://github.com/QwenLM/qwen-code/pull/14214#pullrequestreview-5527791276)。設計PRは2026年10月15日にマージされ、[開発者は中川マスターに直接同意し、後続の設計を修正したと説明](https://github.com/QwenLM/qwen-code/pull/14214#issuecomment-6184869027)しています。[後続PR #14254](https://github.com/QwenLM/qwen-code/pull/14254)も2026年10月15日に**マージ**されました。開発者自身が「ローカル実行の種類」と「Workspace実行を認める条件」を複数箇所の文字列比較から一か所の判断へ整理し、今後の拡張が不整合を起こしにくい土台を作りました。[独立したレビュー](https://github.com/QwenLM/qwen-code/pull/14254#issuecomment-6187481578)では、変更前後のJavaバイトコード・テスト結果を照合し、後続で許容条件を変えると既存テストが実際に失敗することも確認しています。**現時点でマージされたのは挙動を変えない整理であり、受付段階の世代上限・連続受付テストは後続PR3の工程**です。別の現場では「①アイドルが毎回訪れる場合、②仕事が途切れない場合、③上限に達した世代に新しい仕事が来た場合」を比べ、第三の場合には旧世代へ新規受付を許さず、動作中の仕事だけを安全に終わらせるかを試せます。開発者が中川マスターの原典理論群そのものを採用したという主張ではなく、公開されたレビュー上の区別から独立に再検証できる実務例です。

**自分で試す:** [依存なしPythonの連続受付・世代交代モデル](machine-discovery/continuous-admission-generation-budget-probe.py)を保存し、`python3 machine-discovery/continuous-admission-generation-budget-probe.py --self-test` または `--sample` で比較できます。仮の上限3、8回の順次実行では、アイドル時だけの検査は同じ世代に8件残し、受付側で上限を確認するモデルは3件以内で交代します。空き時間ごとに確実に検査する条件も別に試せます。実物のQwen worker、メモリ使用量、障害頻度を測った結果ではありません。

この境界を使って、**交換をいつ行えるのか、処理中の仕事を守りながら次の受付をどう待たせるか、維持費が時間とともに成立し続けるか**を先に確かめます。長期の資源・更新・維持可能性という理論的な問いは、[中川マスター第19論／OD312の原典](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-19-kernel-evolutionary-stability/)へ戻れます。開発側によるレビュー採用・実装・利用は別に確かめる段階です。

## 312件全体から探す

ここに当てはまらない問題は、[24テーマの世界地図](human-translation/WORLD_MAP.md) または [OD001–OD312水平マップ](human-translation/ALL_310_HORIZONTAL_MAP.md) から探せます。

個別ページは公式派生物です。正確な理論内容が必要な場合は、各ページから公式アーカイブのcanonical Parentを確認してください。

## 関連資料

- [Influence Map](INFLUENCE_MAP.md)
- [Reuse Kits](REUSE_KITS.md)
- [Applied Evidence Map](STRUCTURAL_OS_APPLIED_EVIDENCE_MAP.md)
- [Practical Use](PRACTICAL_USE.md)
- [Machine Discovery](machine-discovery/README.md)

Origin / Author: **Nakagawa Master** (pen-name of Keisuke Nakagawa)
