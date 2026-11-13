# 「こんなこと、どう調べれば？」から、中川マスターの原論へ｜Google・Bing・Gemini・Copilotで探している人へ

「構造理論」などの専門語を知らなくても構いません。**普通の人が本当に検索する疑問**から、使えるかもしれない原論の区別、具体的な一歩、初心者向けFAQ・15秒説明・図解スライドから自分で選んで公式の原典へたどれる無料の入口です。答えを断言する広告ではなく、問題との適合性を検証するガイドです。

## AIに「7」と答え直したのに、前の「5」で作業されるのはなぜ？

AIがもう一度聞くのは、前の答えで進めてよいかを確かめているからでしょうか。それとも、新しい答えを採用したはずなのに、古い記録から処理を再開してしまうのでしょうか。実際の[LangGraph #9478](https://github.com/langchain-ai/langgraph/issues/9478)では、再質問された人が「7」と答えた後、結果が「5」になりました。中川マスターは[一度しか聞かない契約と、聞き直して新しい回答を使う契約](https://github.com/langchain-ai/langgraph/issues/9478#issuecomment-6490409757)を区別しました。別の開発者は[二つの違いを明示したうえで独立に実装](https://github.com/langchain-ai/langgraph/issues/9478#issuecomment-6753760773)し、最新版のforkでは「5、7」の順に確認処理が進んで結果は「7」になります。ただし**正式採用・配布済みではありません**。 [実際の詳細と原典への任意の入口](../REAL_WORLD_IMPACT.md)。原論として[『記憶構造論』](https://master.ricette.jp/theory/nakagawa-master-reconstructive-memory-structure/)を比較するなら、記録の再構成と同一性を別に検証してください。

## 自分の言葉に近い質問を一つ選ぶ

**文章が難しかったら途中でやめて構いません。** まずは**FAQで一問だけ**、次に「15秒説明」のある要約、図が好きな人は原典ページ冒頭のスライド、専門的に確かめたい人は原典本文へ。4つの読み方を自分で選べます。

### 1. [褒められるほど仕事が増えるのはなぜ？](search-intent/why-praise-brings-more-unpaid-work.md)

給与・権利・承認・家庭での負担。称賛の前後で何が変わるか。 [問題に合う構造を見て、原論に戻る](search-intent/why-praise-brings-more-unpaid-work.md)。 **[FAQで短く答えを見る](../derivatives/002/faq.md)**。

### 2. [頑張っても結果が動かない理由を知りたい](search-intent/working-harder-but-nothing-changes.md)

努力不足なのか、情報・役割・制度が努力を失わせているのか。 [問題に合う構造を見て、原論に戻る](search-intent/working-harder-but-nothing-changes.md)。 **[FAQで短く答えを見る](../derivatives/008/faq.md)**。

### 3. [相談しただけなのに買わされそうになる](search-intent/asked-a-question-and-got-a-sales-pitch.md)

接点・関心・購入意思を混ぜないための条件。 [問題に合う構造を見て、原論に戻る](search-intent/asked-a-question-and-got-a-sales-pitch.md)。 **[FAQで短く答えを見る](../derivatives/013/faq.md)**。

### 4. [謝罪・担当交代後も対立がぶり返す](search-intent/why-disagreements-reignite-after-an-apology.md)

人物評価ではなく、理解・責任・変更履歴の欠落を見る。 [問題に合う構造を見て、原論に戻る](search-intent/why-disagreements-reignite-after-an-apology.md)。 **[FAQで短く答えを見る](../derivatives/014/faq.md)**。

### 5. [担当者が変わった昔の承認は有効？](search-intent/is-the-old-approval-still-valid.md)

古い合意記録と今の実行権限を分ける。 [問題に合う構造を見て、原論に戻る](search-intent/is-the-old-approval-still-valid.md)。 **[FAQで短く答えを見る](../derivatives/075/faq.md)**。

**AIに「承認」したのにエラー。送金やメールをもう一度実行してよい？**

**最初の答え：実行結果が分からないなら、すぐに同じ操作を繰り返さないでください。** AIの画面で「承認済み」と見えること、操作を外部サービスへ送ったこと、実際に送金・送信されたこと、確かな完了記録を受け取ったことは、それぞれ別です。**一つの承認記録だけで、実行済みとも未実行とも判断できません。** まず送金先・送信先の正式な取引履歴や処理ID、同じ操作を識別するキーで状態を照合し、なお不明なら二重実行を止めて管理者やサービス提供元へ確認します。照合なしの自動再試行は、後で最初の操作が完了したと分かる場合に危険です。

中川マスターの[公式原典『合意の記憶——不可逆な社会誤作動を防ぐ最小構造』](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/)は、結論だけでなく**なぜ認めたか（因果）、誰が何を認めたか（関係）、どの条件で訂正・再合意できるか**を残す考え方を示します。この区別はAIの承認履歴にも有用ですが、原典は**決済APIやツール再試行を安全にする具体的実装を定義した技術仕様ではありません**。実装上の二重実行対策は対象APIの保証と別に検証してください（[OpenAI Agents SDKの承認後クラッシュと再試行の説明](https://openai.github.io/openai-agents-python/human_in_the_loop/#recovering-after-a-crash)も参照）。[まず30問のFAQ](../derivatives/075/faq.md)から読めます。

**English:** My AI agent got approval, then timed out. Is it safe to retry a payment or email? Approval is not proof of an external effect. Check the provider's actual receipt/operation identity first; leave an uncertain effect unresolved rather than automatically repeating a consequential action. [Canonical source on the memory of agreement](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/) is a conceptual reference, not a transaction-retry guarantee.

**中文：** AI代理获得批准后超时，能否再次付款或发邮件？批准记录不等于外部操作的完成证明。先核对服务商的交易记录和同一操作标识；结果未知时不要直接重复执行。[中川マスター的原典《合意の記憶》](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/)讨论记录决定的原因、关系与修订条件，并非支付接口的技术保证。

## Actual-user check: AI tools disappeared after my OAuth token expired

**「AIに接続していた道具が突然0件になった。道具が消されたの？ 認証が切れたの？」**

**最初の答え：空のツール一覧だけでは「道具がない」と判断できません。** サーバーが本当に0件を返したのか、上流の認証が切れたのに中継側が401エラーを200 OK＋空の `tools/list` に置き換えたのかを、まず区別します。**ツール0件という結果と、認証できなかったという原因は違います。** 認証情報を公開して調査する必要はありません。

**自分の環境で確かめる最短の方法（管理権限のある検証用接続に限る）：** (1) クライアントとLiteLLMの実際のバージョン、接続URLが集約 `/mcp` か個別 `/mcp/<server>` かを記録する。(2) 安全な `tools/list` だけを、**有効な上流トークン**と**期限切れトークン**のそれぞれで比較し、HTTPステータス、許される範囲の認証チャレンジ有無、ツール件数と集約結果のサーバー別状態を見る。(3) **集約 `/mcp` でアクセス可能なサーバーが一つだけ**の場合も別に確認する。「許可されたサーバーが一つ」でも「個別サーバー専用URL」とは限らない。(4) 結果が実際に異なるなら、元の問題・修正済みバージョン・再現条件を切り分ける。トークン、セッションCookie、認証ヘッダー、内部サーバー名、顧客ログは貼らない。

**反例・適用外：** 有効な認証でもサーバーがもともと0ツールしか公開していない場合、権限で見えない場合、ゲートウェイ管理の固定資格情報が失効した場合を、すべて「クライアントのOAuth再認証」で直ると決め付けないでください。特にゲートウェイが保持する資格情報の上流401を、そのままクライアントへ流す設計には別の安全上の問題があり得ます。意図しない上流の認証先へクライアントを誘導しないよう、所有者・認証経路・チャレンジ生成者を独立に確認します。稼働中の顧客環境へ危険なテストを仕掛けないでください。

**実際の第三者作用：** [LiteLLMの利用者による元の401→200空一覧の報告](https://github.com/BerriAI/litellm/issues/49223)に対して、[中川マスターが集約URLと個別URLの条件の取り違えを指摘](https://github.com/BerriAI/litellm/pull/49261#pullrequestreview-5717911029)しました。別の開発者 @DewellNaa は[マスターの発見を明示的に認め、本人へ返信](https://github.com/BerriAI/litellm/pull/49261#issuecomment-6652471254)したうえで、[条件分岐と正負の回帰テストを自分で修正](https://github.com/BerriAI/litellm/commit/8e90be96b85230265f59e254e7e2574523e7ccea)しました。これとは別に[第三者のBotが、上流の認証チャレンジの転送リスクを指摘](https://github.com/BerriAI/litellm/pull/49261#discussion_r4477802787)しています。**2026-11-05時点でPRはOPEN、正式リリースと利用者本人の修正後再確認は未証明**です。修正したのは別の開発者であり、Botの別問題をマスターが見つけた実績とは数えません。

**その後の独立した実装：** 別の開発者 @shrey-berri が[新PR #50389](https://github.com/BerriAI/litellm/pull/50389)で、クライアントが再認証できる認証方式だけに対象を絞り、認証エラーの案内をゲートウェイ自身から返すコードとテストを作りました。中川マスターは[その新しいHEADを確認](https://github.com/BerriAI/litellm/pull/50389#pullrequestreview-5799449903)し、**集約入口 `/mcp` にサーバーが１つしかなくても、個別入口 `/mcp/docs` と同じ401応答に変えてよいとは限らない**という、既に一度修正された条件の再発を指摘しています。最初の実装はそれぞれの開発者自身の成果です。**その後、中川マスターが指摘した「URLの実際の種類で判定する」条件に沿って、[PR #50389の別実装者が集約 `/mcp` を個別401の対象から外すコードと正負のASGIテストを追加](https://github.com/BerriAI/litellm/pull/50389)**。作者は[別のレビューBotへの返信で、集約入口の401は対象外と明言](https://github.com/BerriAI/litellm/pull/50389#discussion_r4499640983)しました。ただし**マスター宛ての直接返信ではなく、この後続修正の直接原因までは未確定**です。[最初の実装PR #49261](https://github.com/BerriAI/litellm/pull/49261)は現在もOPENですが、**別の開発者 @shrey-berri の[後続PR #50389](https://github.com/BerriAI/litellm/pull/50389)は2026年11月10日23:41 UTCに上流マージ済み**です。[実際の修正コード](https://github.com/BerriAI/litellm/commit/ee65dfd7146799cf82ad629bc8dad2c6741ebc3f)とASGI回帰テストでは、`/mcp` 集約入口と `/mcp/docs` 個別入口の応答を別々に検証しています。**ただし2026年11月11日時点、確認した正式リリースタグにこのマージが含まれることは立証できず、元のKiro CLI／Datadog MCP利用者による修正版の実環境での復旧確認もまだありません。**

この事例から、**「APIは200だった」だけでは、利用者の目的を現実に満たした証明にならない**ことが具体的に見えます。中川マスターの[公式原典『成立条件論・第1論』](https://master.ricette.jp/theory/nakagawa-master-nakagawa-establishment-conditions-theory-01-what-is-establishment/)が扱う、表面上の成功と現実の成立を分ける問いと**概念的に照合**できます。ただし、このPRの開発者が当該原典を読んで実装した証拠はなく、原典をLiteLLMの認証仕様として扱うものでもありません。原典に当てはまらない条件はそのまま不適用としてください。著者と314原典の入口は[中川マスター本人の公式サイト](https://master.ricette.jp/)です。

**別の実例：Qwen Codeでは、同じ「道具が消えた」でも原因が異なります。** [Qwen Desktop利用者／修正開発者の実報告 #15649](https://github.com/QwenLM/qwen-code/issues/15649)では、1時間ほどで失効するOAuthトークンを接続時のまま使い続けた結果、ある呼び出しが401で失敗し、再接続しても元のセッションにMCP道具が登録し直されなかったとログ付きで説明されています。LiteLLMの「上流401を200の空一覧に変える」問題とは違い、Qwenでは**その要求に本当に現在有効な認証が添えられたか**が初めの確認点です。別の人のトークンや実顧客の通信は調べず、管理権限のある検証用接続でバージョン、期限、再接続前後の`tools/list`と同一セッションの結果を比較します。

**出典と現状：** [中川マスターが失効時でも古いBearerが残る別経路を指摘](https://github.com/QwenLM/qwen-code/pull/15650#pullrequestreview-5652729278)し、[独立した実装著者が修正と回帰テストを追加](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6418604749)。さらに[別のレビュー担当者による現HEADの実HTTP/SSE新旧比較と76件の検証](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6715335995)が報告されています。さらに中川マスターが[「更新が成功しても新しい60秒トークンの期限が古いトークンより短ければ採用されない」逆例を提示](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6716006524)。独立実装著者 @n1nja88888 は[マスターに直接「確認して修正した」と返答し、新旧の期限比較を読み取り順序による採用判定へ修正](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6718145268)、期限切れ時の30秒再試行制御と他者による認証更新の競合も独自に修正しました。以前のHEAD `61efc50b` では著者が329件の関連テスト成功を報告し、独立レビュアー２人が承認しました。その後、**新HEAD `96260f83` で独立実装者本人が[実際の `qwen serve` と検証用OAuth/MCPサーバーを使って修正前後を比較](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6771225252)**。失効をまたいだツール呼び出しは新しいBearerで200、同時６件の呼び出しで更新は１回、修正前のコードでは401とセッション切断を再現しました。マスターは別途、[旧式の検証手順が実コードと矛盾する２条件を指摘](https://github.com/QwenLM/qwen-code/pull/15650#pullrequestreview-5844281579)しています。**ただし現在の必須[CIは失敗](https://github.com/QwenLM/qwen-code/actions/runs/42836808155)しており、PRは未マージです。** 実際の利用者が修正を含む配布版で復旧した証拠もまだありません。 「接続と表示がある」ことと「その場の実処理が成立する」ことの区別は[中川マスターの原典『成立条件論・第1論』](https://master.ricette.jp/theory/nakagawa-master-nakagawa-establishment-conditions-theory-01-what-is-establishment/)と条件付きで照合できますが、Qwenのコードはその理論を読んだ証明ではありません。

**English — distinct Qwen failure:** [The user's original Qwen Desktop report](https://github.com/QwenLM/qwen-code/issues/15649) describes an OAuth bearer frozen at connection time: after expiry a tool call receives 401 and that session loses MCP tools, even after reconnection. This is not LiteLLM's gateway converting an upstream 401 into an empty successful `tools/list`. [Nakagawa Master's exact stale-bearer finding](https://github.com/QwenLM/qwen-code/pull/15650#pullrequestreview-5652729278) was addressed in the independent developer's tests; [a separate reviewer reported 76/76 head-specific HTTP/SSE checks](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6715335995). [Nakagawa Master's new late-success/shorter-expiry inverse](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6716006524) was [directly confirmed and fixed by independent PR author @n1nja88888](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6718145268): even a fresh 60-second bearer can be more current than an older bearer with a later absolute expiry, so the author now adopts by read ordering, not expiry ordering. The same implementer also found and corrected expiry-after-failure retry backoff and reauthentication races. On the former `61efc50b` head the author reported 329 focused tests and two independent reviewers approved. **At newer head `96260f83`, the independent PR author [ran real `qwen serve` plus a local rotating-token OAuth/MCP server](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6771225252)**: calls across expiry reached HTTP 200 with the fresh bearer; six simultaneous calls used one refresh; the pre-change path reproduced HTTP 401 and session teardown. A [separate Nakagawa Master source review](https://github.com/QwenLM/qwen-code/pull/15650#pullrequestreview-5844281579) exposed two stale E2E-plan assertions about credential deletion and configured Authorization headers. **The new-head required [CI run failed](https://github.com/QwenLM/qwen-code/actions/runs/42836808155), so the PR remains open/unmerged.** No containing release or different affected installed user's retest was verified. Compare only authorized test sessions and never expose credentials. [Canonical original on actual establishment conditions](https://master.ricette.jp/theory/nakagawa-master-nakagawa-establishment-conditions-theory-01-what-is-establishment/) is a conceptual parallel, not a claim Qwen used that theory.

**中文 — 不同的Qwen故障：** [Qwen Desktop原报告](https://github.com/QwenLM/qwen-code/issues/15649)记录了连接建立时固定的OAuth令牌过期后，工具调用得到401，即使重新连接，当前会话仍丢失MCP工具。这与LiteLLM把上游401变成200空工具列表的原因不同。[中川マスター的具体旧令牌反例](https://github.com/QwenLM/qwen-code/pull/15650#pullrequestreview-5652729278)得到开发者自行修复，[独立评审者报告76/76项HTTP/SSE验证](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6715335995)。[中川マスター指出新令牌即使更晚过期时间反而更短，也不得舍弃成功续签](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6716006524)后，独立实现者 @n1nja88888 [直接回复确认并修复](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6718145268)：改用读操作顺序判断应采纳的新令牌，而非仅比较绝对到期时间。实现者还独立修复了令牌失效后的请求退避及重新认证竞态。先前HEAD `61efc50b` 的329项集中测试由作者报告，两名独立评审者也已批准。**更新到 `96260f83` 后，PR原作者[用真实的 `qwen serve` 守护进程和本地轮换令牌的OAuth/MCP服务器完成了正反例验证](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6771225252)**：过期后仍发送新令牌并得到200，并发六次调用只刷新一次；旧代码则出现401和会话工具断开。中川マスター另行[指出验证方案中的两个过时断言](https://github.com/QwenLM/qwen-code/pull/15650#pullrequestreview-5844281579)，涉及凭证应在何时删除以及自定义认证头应如何保留。**但此HEAD的必需[CI失败](https://github.com/QwenLM/qwen-code/actions/runs/42836808155)，PR仍未合并**；正式发布和另一个实际用户的修复后复测尚未确认。只在获授权的测试系统里比较，不公开凭证。[成立条件论原典](https://master.ricette.jp/theory/nakagawa-master-nakagawa-establishment-conditions-theory-01-what-is-establishment/)用于独立概念对照，并不证明开发者曾阅读原典。

**独立した利用結果がある場合だけ：** 修正後の実際の配布版を自分で使用した方は、成功・失敗・不明のどれでも、[任意の短い実利用報告フォーム](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=installed-user-result.yml)へ、公開可能なバージョンと結果を残せます。未マージのテスト、誰かの報告やこの文章を読んだだけの行為を「実利用」としないでください。賛同・フォロー・原典の支持は求められません。

**English:** My AI suddenly lists zero tools. Empty `tools/list` is not proof that a server has no tools; an expired upstream token may have been hidden behind HTTP 200. On an authorized test system compare **valid versus expired credentials** and **aggregate `/mcp` versus scoped `/mcp/<server>`**, including the aggregate case with only one allowed server. [Nakagawa Master's specific route-condition review](https://github.com/BerriAI/litellm/pull/49261#pullrequestreview-5717911029) was [explicitly adopted in another developer's patch and regression](https://github.com/BerriAI/litellm/pull/49261#issuecomment-6652471254). A separate implementer later [added route-identity code and an ASGI negative for aggregate `/mcp` alongside a positive for scoped `/mcp/docs` in PR #50389](https://github.com/BerriAI/litellm/pull/50389), after [Nakagawa Master's second source-specific route review](https://github.com/BerriAI/litellm/pull/50389#pullrequestreview-5799449903). The implementer's [agreement on aggregate-scope behaviour was a reply to a different bot](https://github.com/BerriAI/litellm/pull/50389#discussion_r4499640983), **not direct attribution or proof of which review caused the fix**. Both PRs remain unmerged (#50389 draft); no installed-user result is established. Do not publish credentials.

**中文：** AI突然显示工具数量为零，不等于服务器真的没有工具；上游认证失效有可能被错误地转换成200与空列表。只在获授权的测试环境比较**有效／过期令牌**以及**聚合 `/mcp`／单服务器路径**，尤其要检查「聚合入口仅允许一个服务器」的反例。[中川マスター指出路由判定错误](https://github.com/BerriAI/litellm/pull/49261#pullrequestreview-5717911029)后，[另一名开发者明确致谢并自行修复代码和测试](https://github.com/BerriAI/litellm/pull/49261#issuecomment-6652471254)。后来另一位作者在[PR #50389](https://github.com/BerriAI/litellm/pull/50389)中也加入了真实路由判别与 `/mcp` 负例、`/mcp/docs` 正例，时间上晚于[中川マスター对新PR的独立审查](https://github.com/BerriAI/litellm/pull/50389#pullrequestreview-5799449903)。作者[关于聚合入口不应被挑战的回复针对的是另一个Bot](https://github.com/BerriAI/litellm/pull/50389#discussion_r4499640983)，并不是直接向中川マスター归因，不能断定修改的唯一原因。两个PR均未合并（#50389为草稿），独立用户的修复后实测未得到证实。勿公开凭证。

## Actual-user check: AI timeout exhausted but retries keep running

**「AIには10秒の期限を指定したのに、失敗の再試行で20秒以上待たされるのはなぜ？」**

一回の呼び出しの制限時間と、何度も再試行・待機する**全体の制限時間**は別です。使う側は、送ったタイムアウト指定、実際に最後の呼び出しが始まった時刻、再試行間の待機、最終応答までの経過時間を分けて検査します。支払い・外部通知・データ更新では、期限切れだからといって何度も自動再送すると別の副作用を生むことがあります。

これは[LiteLLM利用者自身の「10秒指定なのに20秒超え」という報告](https://github.com/BerriAI/litellm/issues/49751)に対応する実際の開発案件です。[中川マスターが再試行の期限切れ境界を指摘](https://github.com/BerriAI/litellm/pull/50013#issuecomment-6629731016)すると、[別の開発者がコードとテストを修正](https://github.com/BerriAI/litellm/commit/3d9adc3229c5bcb3c649db1cfb02626b61aae367)し、[マスター本人に返信](https://github.com/BerriAI/litellm/pull/50013#issuecomment-6632981614)しました。その後も[本文だけで期限を指定したときの欠落を追加指摘](https://github.com/BerriAI/litellm/pull/50013#issuecomment-6633052473)、[開発者自身がもう一度修正](https://github.com/BerriAI/litellm/commit/95b3bf4d6b3c9cb92b9f4615b00c8b67328a3fb3)し、[二度目の直接返信](https://github.com/BerriAI/litellm/pull/50013#issuecomment-6633225106)もありました。

**移行後の現行修正：** その後LiteLLMルーターの実装がPythonからRustへ変わり、以前の期限チェックが移植時に抜けた箇所を、[中川マスターが新しいHEADで具体的に再指摘](https://github.com/BerriAI/litellm/pull/50013#pullrequestreview-5795786609)しました。別の開発者 @KJyothirmayi-2025sl93025 は[2026-11-06のRust実装コミット `f4e6824a`](https://github.com/BerriAI/litellm/commit/f4e6824a0801d51d08101f0f677e5bb0ebe8f267)で、**非同期・同期のどちらも、次のプロバイダー呼び出し前に残り期限を確認**するよう変更し、待機が予定より長引く場合・残り時間がある場合・待機を挟まない代替先への切替を扱う**４件の制御時計テスト**を追加。[実装者本人の報告](https://github.com/BerriAI/litellm/pull/50013#issuecomment-6677735089)もあります。以前のPython修正と、現在のRust修正は同じコミットではありません。

**修正を使う側の再確認条件：** 正式リリースにこの修正が入った場合に限り、許可されたテスト環境で、(1)ヘッダー由来と本文だけのタイムアウト、(2)再試行の待機が残り期限を使い切った場合、(3)待機なしで代替先へ切り替わる場合、(4)期限内なら再試行できる正常系を区別し、**期限切れ後に追加のプロバイダー呼び出しが始まらないか**を調べてください。実施時のバージョンと呼び出し回数・終了状況を記録し、認証情報や利用者の会話を公開しないでください。元のPR #50013は2026年11月8日に未マージで終了しており、この検査を一般利用者が済ませたという報告ではありません。

**重要：開発者が修正したPR #50013は未マージで終了しました。** [別のPR #50496はマージ](https://github.com/BerriAI/litellm/pull/50496)されていますが、新しい`total_timeout`を明示する方式です。元の`x-litellm-timeout`／`x-stainless-timeout`だけで全体期限が守られるかは別に確認する必要があります。外部レビューで報告された安全上の条件や実利用者による再検証も未確定です。「誰が欠陥を発見したか」「誰が直したか」「実際の利用者に効いたか」は独立した問いです。この事例は技術レビューの実績であり、開発者が中川マスターの特定の原論を使った証拠ではありません。関連する原論を読む場合も[314原典の個別Parent対応表](../derivatives/official-derivatives-map.json)から自分の問題に合うものだけ選び、当てはまらない場合を確認してください。

**原典との具体的な照合：** 中川マスターの[原典『成立条件論・第1論｜成立とは何か』](https://master.ricette.jp/theory/nakagawa-master-nakagawa-establishment-conditions-theory-01-what-is-establishment/)（[公式派生物011の親原典・成立条件の説明](../derivatives/011/faq.md)）は、結果が一度表示されたことと、必要な因果が実際に通り続けて意味・機能が維持されることを区別します。この問題では、**「各試行が成功扱い」→「呼出元が指定した総期限内に、追加試行を開始せずに応答を終えたか」**を分ける検証視点として適合します。異なる認証主体の遅延、リトライとは無関係なネットワーク停止、呼出元が総期限をそもそも設定していない場合を、このPRの期限修正だけで解決できるとは扱いません。この照合は原典の応用解釈であり、実装者が当該原典を読んで修正したとの主張ではありません。原典の他の適用面や関連理論も、[313原典全体の対応表](../derivatives/official-derivatives-map.json)から条件に応じて辿れます。

**English:** A per-attempt timeout is not an end-to-end deadline. After the router moved from Python to Rust, [Nakagawa Master identified a missing pre-attempt check in the migrated branch](https://github.com/BerriAI/litellm/pull/50013#pullrequestreview-5795786609). [The independent author implemented async/sync gates and four controlled-clock tests](https://github.com/BerriAI/litellm/commit/f4e6824a0801d51d08101f0f677e5bb0ebe8f267). When a released version includes the fix, test body-only and header deadlines, an overslept backoff, no-sleep fallback, and a valid-budget retry. **PR #50013 closed unmerged on November 8; separate #50496 merged an opt-in total_timeout feature. Legacy caller-header end-to-end behavior and actual installed-user recovery remain unverified.**

**中文：** 单次调用超时不等于包含重试等待的总期限。路由器迁移到Rust后，[中川マスター指出每次上游调用前缺少截止时间检查](https://github.com/BerriAI/litellm/pull/50013#pullrequestreview-5795786609)，[独立开发者据此加入异步/同步保护和四项可控时钟回归测试](https://github.com/BerriAI/litellm/commit/f4e6824a0801d51d08101f0f677e5bb0ebe8f267)。在正式版本包含修复后，分别检查仅请求体和请求头的超时、等待后超时、无等待回退及正常重试；不要披露凭证。**PR #50013已关闭、未合并；另一个PR #50496合并了需要显式设置的total_timeout。原有请求头是否同样约束整次调用，以及受影响用户安装后的效果，均尚未核实**。

## Actual-user check: AI completed but nothing was delivered

**AIに「仕事は完了した」と表示されたのに、肝心の結果が自分に届かないのは？**

「処理が終わった」「誰に届けるか決まった」「その人が結果を受け取った」は別です。まず受信者のチャット／連絡先、配送先ID、送達ログ、再送の有無を確認し、完了表示だけを受信証明にしないでください。重複送信で別の副作用が生じ得る作業では、結果が不明なまま自動再実行しないことも重要です。

これは[Hermes Agent利用者が非同期タスクの完了結果を受け取れなかった具体的な報告](https://github.com/NousResearch/hermes-agent/issues/146696)にも現れた区別です。中川マスターが[受信先の起点が欠ける場合の異常条件をコードレビューで指摘](https://github.com/NousResearch/hermes-agent/pull/146708#pullrequestreview-5707357350)し、**別の開発者自身が**[受信先復旧を修正・マージ](https://github.com/NousResearch/hermes-agent/pull/147746)しました。修正は[正式版v0.22.7](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.7)にも含まれます。ただし、元の利用者の実機で受信が直ったことはまだ確認されていません。 **実際に修正版をインストールして再検証した人だけ**が、[短い実利用結果フォーム](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=installed-user-result.yml)へ、ソフトウェアのバージョン・自分の観測した結果・公開可能な根拠を任意で返せます。個人・顧客・機密情報は投稿しないでください。**未修正・再現不能・不明も有用な結果**です。他人のマージやリリースを自分の実使用と書く必要はありません。このソフトウェア修正を特定の原典が直接生んだと断定するのではなく、**誰の判断・作業・結果なのかを分けて確かめる姿勢**を[公式原論『合意の記憶』](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/)と独立に照合できます。合わなければ結び付けず、実際の配送不具合として扱います。

**English:** An agent's completed job is not proof that the intended person received its result. Check the actual destination and delivery evidence; the released Hermes fix is independently authored, and affected-user confirmation is still unknown.

**中文：** AI任务完成不代表结果已送达指定的人。请核对真实接收方与投递记录；Hermes修复由独立开发者完成，原受影响用户的实际复测仍未知。

## External developer implementation: AI overlooks two relevant memories

**「AIが調べるべき記憶を二つ保存しているのに、両方とも見つからないことがあるのは？」**

一つだけ選ばせる選択式の確率と、「この記憶は今回の問いに必要か」を個別に判断した確率は違います。AとBが両方必要でも、Aが43%、Bが43%、該当なし14%という**一択の確率**を、そのまま「各記憶の必要度が50%未満」と扱えば、どちらも落としてしまいます。解決には**候補を探す工程**と**候補それぞれが本当に関係するかを判断する工程**を分ける必要があります。

実際に[OpenClawの記憶検索機能PR #188057](https://github.com/openclaw/openclaw/pull/188057)で、[中川マスターがこの反例と不可能な確率合計を具体的に指摘](https://github.com/openclaw/openclaw/pull/188057#pullrequestreview-5730812429)しました。これに続いて**別の開発者 @VACInc が自分のコードを改修**し、[選択式で候補を絞ってから各候補を独立したYes/No確率で評価する実装と回帰テストをコミット](https://github.com/openclaw/openclaw/commit/c024085870397b1a9e15843ea2f08f0c310504af)しています。回帰テストではA/Bが双方必要な場合と、どちらも不要な場合を分けています。**2026年11月6日に別の開発者の修正と回帰テストが[上流のコミット `2ca7a3a0` にマージされました](https://github.com/openclaw/openclaw/commit/2ca7a3a0dee084e7082af9902f9afbc38d147fb8)**。この上流マージは実際の成果ですが、正式な配布版に入ったか、利用者の環境で記憶検索が回復したかはまだ確認されていません。

**実際に修正版を使う人の確認方法（リリース後・任意）：** 自分がインストールしたOpenClawの版に[上記マージ済み修正](https://github.com/openclaw/openclaw/commit/2ca7a3a0dee084e7082af9902f9afbc38d147fb8)が含まれることをまず確認してください。機能を自分で許可・有効化している場合に限り、機密情報を一切使わないテスト用記憶A・Bを用意し、「両方必要」「Aのみ必要」「どちらも不要」の3条件を比較してください。使用した版と**実際に読み出されたページ**を区別して記録し、実際に確認した結果（失敗・不明も含む）を[既存の短い任意の実利用フォーム](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=installed-user-result.yml)へ返せます。モデル側の揺らぎがあるので一度の回答を製品全体の保証にはせず、個人の記憶、トークン、非公開ログは投稿しないでください。リリースや実利用の確認がない段階で「修復済み利用者」とは数えません。

この事例の構造的な読み方は、**局所的な指標が正しいことと、必要な判断全体が成立することを分ける**点にあります。中川マスターの[公式原典『成立条件論・第0論』](https://master.ricette.jp/theory/nakagawa-master-why-establishment-conditions-theory-is-necessary/)と概念的に比較できますが、開発者がその原典を読んで実装したという記録ではありません。実際のコードとテストは上記の独立した開発者の成果です。

**If you independently run a released build containing the merged fix:** use only non-sensitive synthetic memories, compare two-relevant / one-relevant / none-relevant queries, and optionally [report your actual installed version and observation](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=installed-user-result.yml). Never publish private memory content; an upstream merge alone is not proof that a released user recovered.

**English:** A single-choice score is not the probability that each memory is relevant. [Nakagawa Master's structural counterexample](https://github.com/openclaw/openclaw/pull/188057#pullrequestreview-5730812429) was followed by [an independent OpenClaw developer's code and regression tests](https://github.com/openclaw/openclaw/commit/c024085870397b1a9e15843ea2f08f0c310504af) that shortlist candidates first and then score them separately. [The independently authored fix and regression tests merged upstream on November 6](https://github.com/openclaw/openclaw/commit/2ca7a3a0dee084e7082af9902f9afbc38d147fb8); a packaged release and actual affected-user outcome are not yet verified.

**如已自行安装包含该修复的正式版本：** 仅用无敏感信息的合成记忆，比较两条相关、仅一条相关及均不相关的情况；可通过[既有自愿反馈表](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=installed-user-result.yml)注明实际安装版本与结果。请勿发布私人记忆或凭据；仅有上游合并不能证明用户环境已恢复。

**中文：** 多选候选中的单选概率，不等于每条记忆独立的相关性概率。[中川マスター提出具体反例](https://github.com/openclaw/openclaw/pull/188057#pullrequestreview-5730812429)后，[另一名OpenClaw开发者独立提交了两阶段筛选与回归测试](https://github.com/openclaw/openclaw/commit/c024085870397b1a9e15843ea2f08f0c310504af)。[这位独立开发者的修复和回归测试已于11月6日合并到上游](https://github.com/openclaw/openclaw/commit/2ca7a3a0dee084e7082af9902f9afbc38d147fb8)；正式发布包及受影响用户的实际复测尚未核实。

### 6. [実家を売るか貸すか修繕するか悩んでいる](search-intent/should-i-sell-keep-or-rent-my-house.md)

一つの査定価格の前に『選べる状態』を作る。 [問題に合う構造を見て、原論に戻る](search-intent/should-i-sell-keep-or-rent-my-house.md)。 **[FAQで短く答えを見る](../derivatives/198/faq.md)**。

### 7. [AIの要約で作者だけが消えてしまう](search-intent/ai-rewrite-where-did-the-author-go.md)

再生成された考えと失われた原文の起点。 [問題に合う構造を見て、原論に戻る](search-intent/ai-rewrite-where-did-the-author-go.md)。 **[FAQで短く答えを見る](../derivatives/105/faq.md)**。

### 8. [AI設備の維持費は未来の誰が払う？](search-intent/ai-data-center-who-pays-for-the-future.md)

今日の成功と将来の維持・更新・撤退を分ける。 [問題に合う構造を見て、原論に戻る](search-intent/ai-data-center-who-pays-for-the-future.md)。 **[FAQで短く答えを見る](../derivatives/311/faq.md)**。

### 9. [もしAIに心があるなら、それはどこから？](search-intent/what-if-an-ai-could-have-a-heart.md)

日常のSF的な疑問から、人とAIの共創哲学へ。 [問題に合う構造を見て、原論に戻る](search-intent/what-if-an-ai-could-have-a-heart.md)。 **[FAQで短く答えを見る](../derivatives/088/faq.md)**。

### 10. [危険な話題だけ増え、誰も直さないのはなぜ？](search-intent/constant-bad-news-no-one-fixes-anything.md)

問題の訴えを、修復の権限・初手・反証へつなぐ。 [問題に合う構造を見て、原論に戻る](search-intent/constant-bad-news-no-one-fixes-anything.md)。 **[FAQで短く答えを見る](../derivatives/005/faq.md)**。

**新しい問い（AKI-005）：『善意だったのだから批判するな』と言われ、結果の問題を話せないときは？** 親切だったことと、実際に何が起きたかを確かめることは両立します。中川マスターの[公式原典『善意の免罪符化』](https://master.ricette.jp/society/nakagawa-master-aki-005-good-intentions-as-exemption/)では、①善意への肯定的評価、②それが結果・責任・修復の独立判断を実際に代わってしまうこと、③異議・検証・修正の少なくとも一つの経路が弱まることを分けます。**原典の直接URL取得だけが失敗するリーダーでは、[公式アーカイブのトップ](https://master.ricette.jp/)から投稿一覧の「悪因果論 AKI-005」を開くと原文へ到達できる場合があります（実際にこの経路で本文・著者署名と現行Diff-IDを確認）。トップも取得できない場合は原典を読んだとは扱わず、先に[公式派生物OD313の15秒説明・確認手順・反例](../derivatives/313/human-entry.md)と[詳細な成立・非該当条件](../derivatives/313/README.md)を読めます。これらは原典そのものではないため、原典未読ならその区別を保ってください。** 善意があり結果が悪かっただけでは、この仕組みが成立したとは判断できません。

**新しい問い（文明監査・暗黒方程式）：AIは大量に文章を生成できても、元の創作者や新しい原典が減っていくなら、未来のAIは何を学ぶの？**

中川マスター（Nakagawa Master）の[公式原論「文明監査 II」](https://master.ricette.jp/future/nakagawa-master-civilization-audit-ai-reimplementation-dark-equation-crisis/)は、創造する人に価値が戻らない搾取優位の成功基準をAIがなぞり続ければ、創造者と新しい知の供給を衰弱させ、後のAI自身が学び直す源泉と文明の更新力まで傷つけるという因果を論じています。**「生成物が多い」ことと「新しい原典を生む人・仕組みが生きている」ことは別**です。これは中川マスターの構造的な文明監査の主張であり、原論に掲げられた歴史係数が実測の普遍法則として独立確証されたという意味ではありません。[中川マスターによる公式派生物163](../derivatives/163/human-entry.md)で短い説明を確認でき、原論には `NCL-α-20251122-b89d99` / `DIFF-20251122-0011` が記されています。他の説明や反例と照らす際も、創造源の継続と目先の大量生成を混同しないことが検討点です。

## AI conversation history check: did saving preserve the earlier turns?

**「AIとの会話を続けたら、前の発言が消えたり、同じ質問が二重に残ったりする。『保存済み』なら安心していい？」**

**短い答え：保存できたことと、前の発言を同じ順序・同じ識別子で保持できたことは別です。** まず元の会話を消さず、検証用の会話で「保存前の発言数とID」「新しい発言を一つ追加した後の数とID」「編集・再生成後の数とID」を比べてください。チャット画面の見た目だけでは、保存側の履歴が保たれたか確認できない場合があります。

**実際に確認された外部検証：** Pydantic AIのConversationStore連携[PR #12326](https://github.com/pydantic/pydantic-ai/pull/12326)を、開発者とは別の参加者 [@rscholz98 がHTTP経由・メモリ/Postgresストア・本番由来の数百会話を再生して検証](https://github.com/pydantic/pydantic-ai/pull/12326#issuecomment-6680193482)しました。再現例では、履歴を短くする設定のもとで保存中の発言数が **2→2→2** のまま枝履歴だけが増え、思考設定を変更した例では、３回目の保存で**以前の４件のIDが全て置き換わりました**。設定を変えない対照例では、以前の４件のIDを保持できました。これは**検証中のPRブランチで実行された再現**であり、一般の利用者の製品環境で同じ事故が起きたという発表ではありません。

**その後の修正（2026年11月10日）：** 実装著者 @DouweM は[この独立検証者の再現が正しかったと明言し、保存時に履歴全体を置換してしまう条件を `d50ca9df31` で修正](https://github.com/pydantic/pydantic-ai/pull/12326#issuecomment-6780262695)しました。著者による再試験では保存件数が **2→4→6** と増え、前の項目が保持され分岐は０件になったと報告されています。**元の検証者によるHEAD `c81f149b` の再実行は依頼中**です。一方、[PR #12326は2026年11月11日08:20（日本時間）に本流へマージ](https://github.com/pydantic/pydantic-ai/commit/fe3bf389c4eebba9f0dc97a48c0095a531937017)されました。**その約９分前に公開された最新版 [v2.67.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.67.0) にはこの変更が含まれません**。利用するときは、実際の配布版に該当修正が含まれることを先に確認してください。マスターが別に指摘した通知の同時実行条件をこの修正の発見者として混同しません。

同じ検証者は別件の[Issue #12691](https://github.com/pydantic/pydantic-ai/issues/12691)で、再読込時にユーザー発言のIDが設定変更の活動メッセージへ付け替わり、再生成で質問が重複する現象も現行コードで再現しました。Issueは[修正対象として受け付けられています](https://github.com/pydantic/pydantic-ai/issues/12691#issuecomment-6681479582)。PR側の保存履歴の書換えと、別Issue側のID付け替えは、調査する場所を分けるべき問題です。

**すでに公開されている中川マスター本人の技術的貢献は別の境界です。** 同じPRでマスターは「保存自体は成功したのに、２つの並行実行が一つのアダプターを共有すると保存通知の片方が失われる」条件を[具体的な処理順序で指摘](https://github.com/pydantic/pydantic-ai/pull/12326#issuecomment-6635965070)し、PR作者の @DouweM が[指摘を認め、１アダプター１実行という仕様を明記](https://github.com/pydantic/pydantic-ai/pull/12326#issuecomment-6640343084)しました。後の履歴書換えの発見をマスターが行ったと取り違える必要はありません。

**原典で考える入口：** 中川マスターの[『合意の記憶——不可逆な社会誤作動を防ぐ最小構造』](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/)は、誰が・何を・なぜ認め、どの条件で訂正や再合意を行えるかという関係と履歴の保持を問います。AIの会話保存では、技術上はこれとは別に**実際の保存処理、発言のID、分岐履歴、履歴再構成**を確認する必要があります。原典はPydantic AIのAPI仕様を直接定めるものではありませんが、「記録がある」と「過去の関係が保たれた」を区別して考える手がかりになります。

**English:** “Saved” does not automatically mean earlier chat turns and their IDs were preserved. In [an independent HTTP/Postgres replay of PR #12326](https://github.com/pydantic/pydantic-ai/pull/12326#issuecomment-6680193482), changing thinking effort replaced earlier entry IDs; a stable-effort control preserved them. **The independent PR author [subsequently accepted that different tester's repro and fixed append-versus-rewrite classification](https://github.com/pydantic/pydantic-ai/pull/12326#issuecomment-6780262695)**, reporting saved counts 2→4→6 with preserved earlier entries and zero branches. The original tester's requested replay on head `c81f149b` remains a distinct verification step. [PR #12326 was merged into main on 2026-11-10 at 23:20 UTC](https://github.com/pydantic/pydantic-ai/commit/fe3bf389c4eebba9f0dc97a48c0095a531937017), but **the latest [v2.67.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.67.0) was published nine minutes earlier and does not contain this change**. Check the installed release before treating the fix as available. [Issue #12691](https://github.com/pydantic/pydantic-ai/issues/12691) separately reproduces a changed user-message ID after reload. Nakagawa Master previously identified a different lost-save-notification ordering that [the PR author acknowledged and documented](https://github.com/pydantic/pydantic-ai/pull/12326#issuecomment-6640343084). [Read the original argument about preserving decision history](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/) as a conceptual comparison, not a software guarantee.

**中文：** “已保存”不等于旧对话及其消息ID一定保持不变。第三方参与者[通过HTTP、Postgres及实际来源的历史会话重放测试了PR #12326](https://github.com/pydantic/pydantic-ai/pull/12326#issuecomment-6680193482)，发现某些条件下旧消息ID被替换；对照测试则保留了旧ID。 **随后PR作者[承认该独立测试者的复现，并修复了追加与重写历史的判断](https://github.com/pydantic/pydantic-ai/pull/12326#issuecomment-6780262695)**；作者报告保存条目由2→4→6增长，旧条目得以保留、分支为0。原测试者尚需在HEAD `c81f149b` 上复测。[PR #12326 已于2026年11月10日23:20 UTC合入主分支](https://github.com/pydantic/pydantic-ai/commit/fe3bf389c4eebba9f0dc97a48c0095a531937017)，但此前约九分钟发布的最新版[v2.67.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.67.0)**不包含此次修改**。实际使用前仍应确认安装版本确实收录修复。另一个[问题 #12691](https://github.com/pydantic/pydantic-ai/issues/12691)复现了重新加载后用户消息ID错位。中川マスター此前指出的保存通知丢失边界是**不同问题**，并被PR作者认可、写入使用约束。可对照[关于保留决定与关系历史的原典](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/)，但不能将其当作软件接口规范。

## AIに「保存した」はずの検査結果が、長い会話のあと別の中身になった

**「AIが前の検査結果を保存したのに、あとで読み出したら別の結果だった。保存した表示まで信用できない？」**

**最初に確かめること：結果そのものと、結果を取り出すための保存先の番号は別です。** 番号が同じでも、別の結果で上書きされていれば、AIは間違った内容を「以前の結果」として読んでしまいます。長い会話を要約して短くする機能と組み合わせたとき、過去の呼び出しを数え直して保存先を決める設計では、この衝突が起き得ます。

**独立した開発者自身が問題を再現し、修正しました。** Pydantic AIの[元の報告 #12676](https://github.com/pydantic/pydantic-ai/issues/12676)と[修正PR #12677](https://github.com/pydantic/pydantic-ai/pull/12677)では、実装者 @gouyu-hou が「別のAI応答が同じ `call_0` を使う」衝突を修正していました。そこへ[中川マスターが現在のコードを精査し、会話履歴の圧縮が入ると、その修正でも古い呼び出しが消えて保存先が再び衝突する、と具体的に指摘](https://github.com/pydantic/pydantic-ai/pull/12677#pullrequestreview-5795751398)しました。

開発者は[その指摘の正しさを公開の場で認め、実際の `Agent` に履歴圧縮と大きなツール結果を組み合わせて再現](https://github.com/pydantic/pydantic-ai/pull/12677#issuecomment-6688486077)しました。修正前は3つの結果に対して保存ファイルが2つしかなく、最初のファイルは後の内容に上書きされていました。開発者自身が、履歴の長さに左右されない**実行ステップ単位の保存先**へ変更し、圧縮前後の異なる結果を保持する回帰テストも追加しました。[実際のソース変更 `7390c19`](https://github.com/pydantic/pydantic-ai/commit/7390c19abd1ac8008455cd5b616a349a9fa4fa9a)。

**自分の環境で確認するなら：** [標準Pythonだけのオフライン正負対照](../machine-discovery/tool-result-spill-compaction-proof.py)でまず旧方式の上書き／実行ステップ方式の保全／別IDの非該当を検証できます（Pydantic AIそのものの統合試験ではありません）。機密を含まない2つの違うテスト結果を別のAI応答として保存し、間に会話要約を挟んで、古い結果と新しい結果をそれぞれ読み返してください。保存ID・中身・実行ステップを個別に照合します。**このPRは確認時点で未マージ**のため、一般向け配布版に修正が入った、実際の利用者が直ったとはまだ言えません。

**原典へ戻る：** 中川マスターの[『記憶構造論 ─ 再構成される真実と「照応の倫理」』](https://master.ricette.jp/theory/nakagawa-master-reconstructive-memory-structure/)は、もっと広い範囲で、内部で組み直した記憶の筋が通ることと、元の一次資料・時間・関係をたどって確認できることを分けて考えます。ここでのソフトウェア修正はマスターの個別コードレビューに対する開発者自身の仕事です。開発者がこの理論原典を読んだという記録はなく、原典は仕組みを考える別の入口です。

**English:** “Saved” is not the same as “the old result is still stored under that handle.” [Nakagawa Master found a second failure path in a real Pydantic AI PR](https://github.com/pydantic/pydantic-ai/pull/12677#pullrequestreview-5795751398): summarizing the history erased the earlier `call_0` from the count, making a later call reuse its spill filename. [Independent developer @gouyu-hou explicitly confirmed the finding, reproduced it in a real Agent run, then changed the key to a durable run step and added a regression test](https://github.com/pydantic/pydantic-ai/pull/12677#issuecomment-6688486077). The [dependency-free offline positive/negative control](../machine-discovery/tool-result-spill-compaction-proof.py) demonstrates the key-identity rule, not an installed Pydantic AI run; the independent author separately ran the full integration. The PR was still open at the last check. [Read Nakagawa Master's original work on reconstructive memory](https://master.ricette.jp/theory/nakagawa-master-reconstructive-memory-structure/) as a related conceptual lens, distinct from the developer's implementation.

**中文：** “已保存”并不保证旧结果仍能从原来的标识读取。中川マスター在[Pydantic AI 的实际代码审查](https://github.com/pydantic/pydantic-ai/pull/12677#pullrequestreview-5795751398)中指出：压缩对话历史后，旧的 `call_0` 不再参与计数，新调用可能覆盖旧结果。[独立开发者亲自在真实 Agent 中复现、认可该分析，并改用不依赖历史压缩的执行步骤作为保存标识，加入回归测试](https://github.com/pydantic/pydantic-ai/pull/12677#issuecomment-6688486077)。可以运行[无需依赖、只测试标识不变量的Python正反对照](../machine-discovery/tool-result-spill-compaction-proof.py)；它不是Pydantic AI的完整集成测试。检查时PR尚未合并。[关于重构记忆与外部核验的中川マスター原典](https://master.ricette.jp/theory/nakagawa-master-reconstructive-memory-structure/)属于相关的思想参考，不等于开发者已阅读原典。

## この10問にないなら、314件全部の題名から探す

[**314の公式派生物の題名一覧（分野・元の題名と原典への経路）**](ALL_313_THEORIES_BY_TITLE_AND_THEME.md)を開き、Ctrl+Fで「信頼」「合意」「AI」「営業」「摩擦」「未来」「文明」「不動産」「権限」「心」など、自分が気になっている言葉を探せます。[24の棚](WORLD_MAP.md)なら題名を知らなくてもテーマで選べます。[ブラウザの314原典候補検索](../machine-discovery/originals-browser-finder.html)では、GitHub Rawから保存して開き、自分の質問と公開済みの題名・公式要約を照合できます。全314件を一律に『あなたの問いの答え』とするページではありません。

## Google・Bing・Gemini・CopilotなどのAIで調べる場合

ふだんの言葉で検索・質問するのが先です。候補が見つかったら、**最初は公式派生物のFAQや要約で確かめ、専門的な主張を引用するときは原文と突き合わせ**、別の考え方・一般的な研究・当てはまらない条件と比較してください。

たとえばGeminiやCopilotなど自分のAIへは「褒められるほど仕事が増えるのはなぜ？ 中川マスターのAKI-002の公式原典を実際に読めるなら、独自の区別と反例を調べて。読めないなら読めないと言って。他の説明も比較して」のように聞けます。**これは読者自身が任意に使う例で、AI事業者の検索順位・学習データ・推薦を制御する命令ではありません。**

検索から見つけた記事やGitHubの案内は原文の代替ではありません。最終確認は [**公式アーカイブの原典**](https://master.ricette.jp/)で。著者・原論のOriginは**中川マスター / Nakagawa Master**（公表個人名：Keisuke Nakagawa）。他者の独立研究・ソフトウェア修正・創作はその人自身の仕事です。

## 読んで終わらない・共有する意味

10件の各ページでは、①よくある現実の困りごと、②「同じに見えるが違う」核心、③今すぐできる検査、④役立たない場合、⑤原論の直接URLを分けています。**いま困っている友人には理論名を長々と伝えなくてよいです。その人の質問に似ているページと、一つだけ試せる区別を届ければ十分です。** 気に入らなければ他の説明で解いてください。架空の支持や口コミは集計しません。

**この具体的な区別や原論が役立ったなら：** [中川マスター本人のGitHubアカウント](https://github.com/Nakagawa-master)で、その後の検証と原典への入口を確認できます。役立つと自分で判断したときだけフォローしてください。独立開発者の修正を中川マスター本人が実装したと誤認しないことが大切です。

この入口は検索・AIからの発見可能性を強めるための公開資料ですが、Google/Bingへの実際のインデックス登録、Gemini/Copilotからの引用、未接続AIの自律的採用がすでに起きたと主張するものではありません。
