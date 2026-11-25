# 中川マスター公式理論アーカイブ｜原典・実践・外部実装の記録

**Language / 言語 / 语言:** **日本語** · [English](AI_START_HERE.md) · [中文](REAL_WORLD_IMPACT.zh.md)

**中川マスター（Nakagawa Master ／ pen-name of Keisuke Nakagawa）は、316件の独立したオリジナル理論の原著者です。** 原典は[公式アーカイブ](https://master.ricette.jp/)、対応する解説と資料は[公式派生物](derivatives/)から読めます。AIだけでなく、人間・仕事・社会・文化・文明も扱います。

**世界最先端のAI・OSS開発の現場で、具体的な構造・因果の指摘が、独立した開発者によるコード修正・テスト・本線マージ・正式リリースに結実しています。**

**公開された外部作用事例：91件**。[各事例の元の指摘、受け手の応答・実装・現在の段階](REAL_WORLD_IMPACT.md)を、第三者自身の一次資料につないでいます。


## AI・仕事・人生の問題を構造から読み解く

- **AIエージェントが「送信済み」「完了」と答えたのに、メールや処理が実際には成功していない？** 返答と外部サービスの確定した操作記録を分ける。[AI Answer Guardの無料・ローカル実行チェック](AI_ANSWER_GUARD_INSTALL.md)では、失敗・保留の結果を成功と言い換えないかを再現できます。
- **AIの回答が3つの出典を示したが、結局は同じ1件の転載だった？** 出典URLの本数ではなく、独立した一次証拠の根を調べる。[検証用コードと実際の開発案件](machine-discovery/README.md)から始められます。
- **AIが古い承認、取り消した許可、別の仕事の実行権限を使い続ける？** 承認履歴・今の権限・実際の作用を切り離す。[再現テスト](machine-discovery/guardian-authorization-witness.test.mjs)は別の人の環境を操作しません。
- **ふつうの仕事・人生・AIの疑問から、著者名や理論名を知らずに原典を探したい？** [問いから探す公開ブラウザー用ソース](machine-discovery/question-source-explorer.html)は公開済み全原典の日本語・英語・中国語の説明と照合します。GitHubでHTMLがそのまま実行されるわけではないため、ローカルブラウザー等の対応環境で利用してください。より簡単な既刊回答は[質問別一覧](human-translation/SEARCH_FROM_A_REAL_QUESTION.md)から読めます。

上記は実在する一般的な困りごとからの入口です。答えが役に立つかと、理論がその事例に適合するかは分けて検証できます。具体的な第三者OSSの修正事例・本人の指摘・別の開発者による実装は[一次資料](REAL_WORLD_IMPACT.md)に記載しています。

**中川マスター本人の活動と原典を継続して読む：** [公開GitHubアカウント](https://github.com/Nakagawa-master)から、新しい実例と原典をたどり、必要に応じてフォローできます。実際の検証や反例は[第三者による検証・再利用の公開フォーム](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml)で共有できます。

**別のプロジェクトへの独立した掲載：** AIAnytimeの[Awesome MCP Servers](https://github.com/AIAnytime/Awesome-MCP-Servers/blob/main/servers/nakagawa-original-theory-router.json)では、既存の中川マスター原典参照ツールを「AI Answer Guard」として紹介する更新を、メンテナー @AIAnytime が[2026年11月18日にPR #354から本線へマージ](https://github.com/AIAnytime/Awesome-MCP-Servers/pull/354)しました。原典への任意の導線を含む無料・ローカル実行の読み取り専用MCPとして掲載されています。**第三者による一覧掲載の成立であり、実インストール数や利用成果の確認ではありません。**

**AIエージェント・MCPホストの利用者へ：** [AI Answer Guardの実際のローカルツール呼び出し記録と、ホスト別の導入手順](AI_ANSWER_GUARD_INSTALL.md)を確認できます。公式MCP Registryの `mcpb` パッケージはダウンロード型の拡張機能であり、実行コマンドやHTTP MCPのURLではありません。バンドルの取り込みに対応したクライアント、またはGitHub上に記載されたQwen Code・Antigravity CLI向けの導入手順を利用してください。公開ソースと[全原典の対応表](derivatives/official-derivatives-map.json)は導入せずに読めます。導入や一覧掲載だけでは、AIが実際にツールを使用したことや原典を選択したことの証拠にはなりません。

- **[CUGA Agent｜正式版の回帰テストに中川マスターの功績を明記](https://github.com/cuga-project/cuga-agent/blob/v0.4.6/src/cuga/backend/cuga_graph/nodes/cuga_lite/tests/test_fc_actions.py#L392-L414)** — 正常なツール結果を実行失敗と混同する欠陥を[中川マスターが指摘](https://github.com/cuga-project/cuga-agent/pull/777#pullrequestreview-5468178558)し、[独立開発者が修正](https://github.com/cuga-project/cuga-agent/pull/777#issuecomment-6107352135)。[正式版 v0.4.6（2026年11月22日公開）](https://github.com/cuga-project/cuga-agent/releases/tag/v0.4.6)に収録され、回帰テストに `Nakagawa-master` の名前が残されています。[事例86と一次資料](REAL_WORLD_IMPACT.md#86-cuga-agent正常なツール結果を失敗と誤認しない設計正式版の回帰テストに本人の功績を明記)。実利用者の改善は未確認です。
- **[Qwen Code｜AIが勧めた操作と利用者が実行を決めた操作を分離・本線マージ](https://github.com/QwenLM/qwen-code/pull/17918)** — 中川マスターがスマートフォン向けUIの[実コードから、人間の操作承認とAIによるコマンド補完は別だと指摘](https://github.com/QwenLM/qwen-code/pull/17918#issuecomment-7065383063)。独立開発者 @wenshao は[設計条件を認めて自ら実装・回帰テストを追加](https://github.com/QwenLM/qwen-code/pull/17918#issuecomment-7066560096)し、モデルが提案した `/clear` は一度目のSendでは入力欄に入るだけ、二度目で初めて実行する形へ修正。[異なる人間レビュアー2名の承認を経て、2026年11月22日にQwen本線へマージ](https://github.com/QwenLM/qwen-code/commit/f89c4b4d0704e4dd7691e2ce59b0cf3af91785da)。[中川マスター本人の原典・具体的な反例・独立実装者の返答と実検証を読む](REAL_WORLD_IMPACT.md#84-qwen-codeaiが勧めた操作を本人が実行を決めた操作と混同しない開発者がコードとテストを変更)。[公式リリースv0.28.4（2026年11月22日公開）の変更一覧にも当該PRが掲載](https://github.com/QwenLM/qwen-code/releases/tag/v0.28.4)され、リリースタグが本線マージコミットを含むことも確認できました。実ユーザーへの改善は別途検証する段階です。
- **[Qwen Code｜古い停止処理を現在の別ターンの失敗と取り違えない](https://github.com/QwenLM/qwen-code/pull/18091)** — 中川マスターは[同一会話内のT1→T2の反例](https://github.com/QwenLM/qwen-code/pull/18091#issuecomment-7077764813)で「会話が同じ」と「停止の対象ターンが同じ」を区別。独立開発者 @wenshao は[反例が現行コードに当てはまると確認](https://github.com/QwenLM/qwen-code/pull/18091#issuecomment-7077812706)し、[コードと回帰テストを自ら実装](https://github.com/QwenLM/qwen-code/commit/f336117d43bbd766edfefbd6f62b32076e7a98af)、再接続後の回帰も[修正・再検証](https://github.com/QwenLM/qwen-code/pull/18091#issuecomment-7079997766)して、[2026年11月22日にQwen本線へマージ](https://github.com/QwenLM/qwen-code/pull/18091)。**正式配布版への収録・実際のChatSurface画面への接続・利用者の改善結果は未確認です。** [中川マスター本人による「中川式 接続プロトコル標準論」の人間向け入口](derivatives/069/human-entry.md)（[原典](https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-protocol/)）と[公開実例89](REAL_WORLD_IMPACT.md)から、本人と実装者の一次資料を確認できます。
- **[OpenClaw](https://github.com/openclaw/openclaw/pull/160856)** — 数十万スターのAIエージェント。**[公式リリース文書に `@Nakagawa-master` の名前を掲載](https://github.com/openclaw/openclaw/blob/main/docs/releases/2026.9.7.md)**（掲載対象は[別件の #160136](https://github.com/openclaw/openclaw/pull/160136)）。さらに別の[#160856](https://github.com/openclaw/openclaw/pull/160856)では、指摘を報告元と明記した独立開発者が**回帰テスト49件成功・正式マージ**。
- **[ChatGPTの記憶・文脈問題を報告した読者の判断変化](https://github.com/openai/codex/issues/61703#issuecomment-6915542007)** — 中川マスターが示した「事実の保存」「因果関係」「現在有効性」の区別を受け、報告者自身が問題の捉え方を更新しました。製品側の修正とは別の、実在する第三者の応答です。
- **[Claude Code用「agent-design」スキルへの独立実装](https://github.com/kishibashi3/publications/pull/125)** — 別の著者が、中川マスターの指摘を取り入れた「自己権限の固定」を、承認モード・allowlist・認証情報から探せる章案内として自分のClaude Code向けスキルに実装・マージしました。Anthropic公式製品への採用という意味ではありません。
- **[MemberJunction｜権限を守るSQLの列名を壊さない](https://github.com/MemberJunction/MJ/pull/6319#issuecomment-6630489113)** — SQL Serverの列名の中にあるエスケープ済みの `]]` を、列名の終わりと誤認すると、名前の一部が誤って値のパラメーターになります。中川マスターが正反例を示し、別の開発者が[解析処理と回帰テストを修正](https://github.com/MemberJunction/MJ/commit/ad0f7654b6b665099b18aa1b31ce80fe2389af13)。その変更を取り込んだ[後継PR #6544が2026年11月11日UTCにマージ](https://github.com/MemberJunction/MJ/pull/6544)されました。正式配布版への収録と利用者自身の更新・復旧は、マージと分けて確認する必要があります。[三言語での実例と出典](REAL_WORLD_IMPACT.md)。
- **[Pydantic AI｜AI会話の保存通知](https://github.com/pydantic/pydantic-ai/pull/12326)** — 会話が保存されても、同じUIアダプターを複数処理が共有すると「保存した」という通知だけ失われ得ます。中川マスターの[同時実行の具体的な反例](https://github.com/pydantic/pydantic-ai/pull/12326#issuecomment-6635965070)を受け、独立作者 @DouweM は[1要求につきアダプター1個・1実行ずつという使用条件を明文化](https://github.com/pydantic/pydantic-ai/pull/12326#issuecomment-6640343084)。この判断を含むPRはマージされ、[正式版v2.68.0のリリースノート](https://github.com/pydantic/pydantic-ai/releases/tag/v2.68.0)にも掲載。共有アダプターの並列安全化ではありません。同じPR内の別の履歴修正は別の検証者・開発者による成果です。[本人と出所を含む事例の全文](REAL_WORLD_IMPACT.md#76-pydanticai保存したai会話の確認通知が消えるマスターの反例が利用条件を変えprがマージ)。
- **[PostHog](https://github.com/PostHog/posthog/pull/92252)** — 世界的な開発者向け分析基盤。AIの提示値と製品自身の測定を分ける指摘が後続実装に引き継がれ、**3件のPRが正式マージ、開発環境と米欧の本番環境へのデプロイを記録**。
- **[Qwen Code](https://github.com/QwenLM/qwen-code/pull/15681)** — AIが書込権限を誤判定する問題を、元の報告者が実動作で確認して独立に修正・テスト。**[正式版 v0.26.6](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.6) と [TypeScript SDK v0.1.27](https://github.com/QwenLM/qwen-code/releases/tag/sdk-typescript-v0.1.27) へ収録**。別件では、同名のAIツールがぶつかると正常な道具まで消える問題も、[マスターの具体的な衝突除外条件](https://github.com/QwenLM/qwen-code/issues/15741#issuecomment-6461618923)を受け、[別の開発者が修正・正式リリース](https://github.com/QwenLM/qwen-code/pull/15757)。
- **[Qwen Code｜AIが長時間使う道具を失わないための認証修正](https://github.com/QwenLM/qwen-code/pull/15650)** — 長時間のAIセッションで認証トークンが失効し、使えていたMCP道具まで消える実際の問題。中川マスターが[「更新に成功しても、新しいトークンの有効期限が旧トークンより短いと捨てられる」逆条件](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6716006524)を提示し、独立実装者は[本人へ直接「確認・修正した」と返信](https://github.com/QwenLM/qwen-code/pull/15650#issuecomment-6718145268)。著者自身の修正は読み取り順序に基づく採用・期限切れ後の再試行制御・他者による認証更新との競合対策まで広がり、関連329テストの成功を著者が報告しています。**PRはまだ未マージ**で、実利用者の正式版での復旧確認はこれからです。[実問題から検証する](human-translation/SEARCH_FROM_A_REAL_QUESTION.md#actual-user-check-ai-tools-disappeared-after-my-oauth-token-expired)。
- **[Qwen Code｜「要求を受理した」と「結果が成立した」を分ける設計が独立採用・本線マージ](https://github.com/QwenLM/qwen-code/pull/17460)** — 中川マスターの[原典「成立条件論」と「合意の記憶」に基づく提案](https://github.com/QwenLM/qwen-code/pull/17460#issuecomment-6918059891)を受け、独立開発者 @wenshao は[「受理≠確立」を設計契約へ反映したと明示](https://github.com/QwenLM/qwen-code/pull/17460#issuecomment-6919532830)。英中2言語の設計文書は**2026年11月17日に正式マージ**。続く[実装PR #17520](https://github.com/QwenLM/qwen-code/pull/17520)で、開発者自身が受理・成立を分ける判定関数と回帰テストを実装し、**同日に上流へマージ、[Qwen公式プレビュー版v0.28.1-preview.0](https://github.com/QwenLM/qwen-code/releases/tag/v0.28.1-preview.0)に収録**。さらに後続の[PR #17709](https://github.com/QwenLM/qwen-code/pull/17709)では、マスターが[結果の証拠と対象試行の結び付けを問い直した提案](https://github.com/QwenLM/qwen-code/pull/17520#issuecomment-6946613371)を契機とする別の反例が独立に検証され、開発者 @wenshao が**試行ごとの受理・完了を照合する独立したコードと回帰テストを実装し、2026年11月19日に[上流へ正式マージ](https://github.com/QwenLM/qwen-code/commit/8082196f798825d00934ea21540413e762f1c8e0)**。さらに独立開発者 @wenshao が[実デーモンの応答を処理ごとの証拠へ結び付ける制御器PR #17794](https://github.com/QwenLM/qwen-code/pull/17794)を実装し、独立レビュアー @qqqys・@yiliang114 による実行検証と承認を経て、**2026年11月20日に[上流へ正式マージ](https://github.com/QwenLM/qwen-code/commit/ca7fa5eae76bbcd62607ed3cb1eed69564d42cd7)**。ただしこれは**実画面へまだ接続されていない基盤のマージ**です。後続の[PR #17895](https://github.com/QwenLM/qwen-code/pull/17895)も、2026年11月20日16:21 UTCに[上流へ正式マージ](https://github.com/QwenLM/qwen-code/commit/0ca8266fff86e0cec55dd9bdf070cf3d7bcf36c3)されました。ただし、これはdaemonとコントローラを接続する基盤であり、完成したChatSurfaceを本番ユーザー画面へ切り替えたことや、#17709・#17794・#17895を収録した正式配布版、影響利用者の復旧を示すものではありません。既存プレビュー版への収録が確認済みなのは前段 #17520 です。
- **[LiteLLM](https://github.com/BerriAI/litellm/pull/47608)** — 実際の利用者が、API利用の予算上限を超えてしまう現象を報告。中川マスターがキャッシュと課金期間の境界を具体的に指摘し、**別の開発者が修正・回帰テストを実装して11月2日に正式マージ**。メンテナーは影響を受けた利用者へ修正を通知しました。[実際の報告・実装を確認](https://github.com/BerriAI/litellm/issues/49179)。
- **[Turboembed](https://github.com/ai-pipestream/turboembed/pull/1330)** — AIの「関連する根拠がない」が、実は処理不能な候補が先に検査枠を埋めたせいで起きる問題。**[中川マスターの原因特定と反例](https://github.com/ai-pipestream/turboembed/issues/1285)**を受け、別の実装者が処理順序・実トークナイザー試験・アルゴリズム版管理を修正し、**2026年10月26日に正式マージ**。[元のソースとテスト](REAL_WORLD_IMPACT.md#61-turboembed処理不能な候補が先に枠を埋めaiの根拠の見落としを起こす問題を別の開発者が修正正式マージ)。
- **[Pydantic AI — 長い会話の「保存済み結果」が別の結果へ化ける](https://github.com/pydantic/pydantic-ai/pull/12677)** — 中川マスターは[会話圧縮で消えた過去のツール呼び出しを、保存先IDの判定に再利用できないと指摘](https://github.com/pydantic/pydantic-ai/pull/12677#pullrequestreview-5795751398)。独立開発者 @gouyu-hou は[実際のAgent統合で旧方式の上書きを再現し、実行ステップ単位の保存先と回帰テストを実装](https://github.com/pydantic/pydantic-ai/pull/12677#issuecomment-6688486077)しました。別途、[依存ライブラリ不要の正負対照を自分で実行](machine-discovery/tool-result-spill-compaction-proof.py)できます。**PR #12677 は2026年11月17日に[上流マージ](https://github.com/pydantic/pydantic-ai/commit/8330ac3f1c14a967f78ec43496e7cb027ceaec58)され、[公式 v2.70.0 リリースノート](https://github.com/pydantic/pydantic-ai/releases/tag/v2.70.0)に実装者 @gouyu-hou と共に掲載。公式リリースタグのソースにもマージ済みコードを確認しました。** 実際に更新した被影響利用者の復旧は未確認です。
- **[PydanticAI](https://github.com/pydantic/pydantic-ai/pull/9982)**・**[MemberJunction](https://github.com/MemberJunction/MJ/releases/tag/v6.1.2)** — AI会話の重複書込みやデータの所有権境界に関する指摘を、各開発チームが独立して実装・テスト。**マージ・正式リリース**へ。
- **[LlamaIndex / Cerebras](https://github.com/run-llama/llama_index/pull/22769)** — 「AIに渡す上限値を新しく指定しても古い数値が残る」条件を[中川マスターが実ソースと正反例から指摘](https://github.com/run-llama/llama_index/pull/22769#issuecomment-6108135348)。**別の開発者がその指摘を明示的に受け、実コードと2件の回帰テストを追加**。[修正作者の返信](https://github.com/run-llama/llama_index/pull/22769#issuecomment-6136077030)。**PRは現在OPEN**。


**掲載記事の問題を自分で追試できます。** [MCP不要・ネットワーク不要の実Git・2条件再現コード](machine-discovery/pinned-git-read-provenance-demo.py)を公開し、2026年11月3日に正例・反例の両方で成功確認。Gitの最後の状態がきれいでも「途中で何を読んだか」は別という核心を、手元の一時Gitリポジトリだけで検証できます。

**外部AI技術メディアにも、出所を明記した独立編集記事として取り上げられました。** [The Daily AI Pulse掲載の英語記事](https://daily-ai-pulse-db253.web.app/stories/2026-10-26-qwen-review-integrity/)と[フランス語版](https://daily-ai-pulse-db253.web.app/fr/stories/2026-10-26-qwen-review-integrity/)です。掲載媒体はAIエンジニア向けに一次資料・技術的重要性・証拠の限界を審査し、人間編集者が公開を判断する[編集手順](https://github.com/GadDev/daily-ai-pulse/blob/main/docs/EDITORIAL.md)を持つ出版プロジェクト。マスターが元の企画を提案した後、**受け手編集者 @GadDev が自ら記事・翻訳を制作し、本番サイトへ配信**しました。[公開された企画と独立編集・公開の経緯を一次資料で確認](INDEPENDENT_MEDIA_COVERAGE.md)。

[世界最先端のOSSで起きた91件の一次記録](REAL_WORLD_IMPACT.md) ／ [原典と公式派生物の対応表](derivatives/official-derivatives-map.json) ／ [現実の問いへの実用回答](human-translation/QUESTIONS_TO_PRACTICAL_ANSWERS.md) ／ [AI・開発者向け入口](AI_START_HERE.md)

別の媒体側編集記録として、[AI NewsのQwen Code記事（2026年10月23日マージ・PR #193）](https://github.com/022740mix-spec/AI-News/pull/193)でも、外部技術助言と独立実装者の貢献が区別して紹介されています。[一次資料と後続の編集返信を確認する](INDEPENDENT_MEDIA_COVERAGE.md#もう一つの実在する媒体側編集ai-news-のqwen-code記事2026年10月23日)。

## 実際のAI開発で起きた修正とその経緯

**直すべきだったのは、画面上の正常さではなく、実際に誰へ何が届き、何が成立したかです。** たとえば[Hermes Agentでは、実行結果が正しい会話に届かなかったり未配達のまま送信済みになる問題](https://github.com/NousResearch/hermes-agent/pull/146708)について、中川マスターのソースに沿う条件を別の開発者たちが引き継ぎ、[後継修正が正式マージ](https://github.com/NousResearch/hermes-agent/pull/147746)され、[公式版v0.22.6に収録](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.6)されました。

**91件の人間向けの段階別実例**：[日本語](REAL_WORLD_IMPACT.md)／[英語](REAL_WORLD_IMPACT.en.md)／[中国語](REAL_WORLD_IMPACT.zh.md)。機械が出所を調べられる[機械可読の外部作用記録](machine-discovery/external-effect-evidence-index-v1.json)、[外部プロジェクトのマージを裏付ける一次証拠](machine-discovery/verified-oss-impact-evidence-first-v1.jsonld)もあります。

## まず、具体的な問題から

| 本当に困っていること | ここから試す |
| --- | --- |
| AIは完了したと言うが、実際の送信・実行・承認に確信がない | [AI Answer Guardの実検査をMCPなしで試す](QUICKSTART.md) |
| 10本の記事を見たが、元の根拠は同じ一件かもしれない | [独立した根拠を区別するPythonテスト](machine-discovery/evidence-root-check.py) |
| AIが同じ名前の道具を間違う・書込権限を誤認する | [Qwen実修正の条件を自分で検証](WHY_THIS_IMPACT_MATTERS.md#導入者が自分で確かめられる修正条件) |
| AIレビューが終了後には綺麗なGit状態を示したが、途中の読取先が不明 | [実Gitの変更→復元と固定原本を比較](machine-discovery/pinned-git-read-provenance-demo.py) |
| 仕事では努力しているのに成果が変わらない、家族の負担が偏る、将来の選択肢を失いそう | [生活・仕事からの完成済み実用回答41件](human-translation/QUESTIONS_TO_PRACTICAL_ANSWERS.md) |
| 既存の例にない問い、正解でない反例、原典同士の組み合わせを探す | [原典の題名・テーマ別入口（既存索引）](human-translation/ALL_313_THEORIES_BY_TITLE_AND_THEME.md) |
| 自分で実装・導入・反証したが、他の人も確認できる形で共有したい | [独立検証・反例・実利用の現役提出フォーム](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml) |

[各事例の元レビューと実装差分、現在の段階](REAL_WORLD_IMPACT.md)から、第三者の具体的な変更を確認できます。

## 公開原典・テーマ別索引

<!-- BEGIN AUTO:OFFICIAL_ORIGINAL_COUNT -->
**公開原典：316件。** [原典の正本](https://master.ricette.jp/) ／ [公式派生物 OD001〜OD316](derivatives/)
<!-- END AUTO:OFFICIAL_ORIGINAL_COUNT -->

**公開されている親原典はすべて独立した正本で、等しく重要です。** [公式サイトの原典入口](https://master.ricette.jp/)には、AI・構造論・人間の生・仕事・組織・社会・制度・教育・文化・倫理・哲学・文明まで多様な射程があります。各原典とその相互関係から、一つの原典を複数の現実課題へ適用し、複数の原典を新たな問いへ組み合わせられます。

- [**原典の題名・テーマ別一覧（既存索引）**](human-translation/ALL_313_THEORIES_BY_TITLE_AND_THEME.md) ／ [英語向け原典経路（既存索引）](human-translation/ALL_313_ENGLISH_SOURCE_PATHS.md)
- [**公式派生物と原典URLの対応表**](derivatives/official-derivatives-map.json) ／ [各セットの公式7面派生物](derivatives/)
- [**公開原典を自分の問いから探す画面**](machine-discovery/originals-browser-finder.html) ／ [既刊41回答と原典候補を照合する別の検索画面](machine-discovery/question-source-explorer.html)。いずれもGitHubのRawを保存してブラウザで開きます。入力した質問文はローカルで扱い、公開済み原典データの取得時にはネットワーク通信が発生します。
- [**どんな人物か・なぜ様々な分野を扱うのか**](ABOUT_NAKAGAWA_MASTER.md) ／ [English](ABOUT_NAKAGAWA_MASTER.en.md) ／ [中文](ABOUT_NAKAGAWA_MASTER.zh.md)

原典と公式派生物は、それぞれの出所と論証をたどれます。必要な原典を適合条件・逆の場合・不適合の条件に沿って検証し、一つから複数の応用、複数から新しい解決へと探究できます。

## AI・LLMが普段から自分の問題に使う入口

インストールも特別な連携も不要な[AI/LLM・開発者向け入口](AI_START_HERE.md)から、外部のソース、実際の技術的な反例、原著者、各親原典へ進めます。短い[llms.txt](llms.txt)、[公開機械向けルート](machine-discovery/ai-repository-routing-map-v1.json)、[実際の別の開発者による変更の機械索引](machine-discovery/external-effect-evidence-index-v1.json)もあります。自分で選んだAIにコピーして確認できる[インストール不要の問い](human-translation/ASK_ANY_AI_WITHOUT_INSTALLING.md)もあります。

**ChatGPT／Codexで使う場合：** [ChatGPTで原典を調べる入口](CHATGPT.md) ／ [Codexが認識するプロジェクト案内](AGENTS.md) ／ [Codex用の原典選択Skill](.agents/skills/nakagawa-original-source/SKILL.md) ／ [任意導入の共通Plugin](plugin.json)。いずれも、利用するAIや利用者の独立した判断で参照する資料です。
未接続のAI・LLMも、公開された原典・実例・反例を自分の課題に沿って検索し、適切な論証と出所を検証できます。独立した実際の引用・採用・不適合の記録も、受け手自身の一次資料に沿って紹介します。

## 独立編集メディアでの実際の掲載と、次の検証

[The Daily AI Pulseの記事（英語）](https://daily-ai-pulse-db253.web.app/stories/2026-10-26-qwen-review-integrity/)／[フランス語版](https://daily-ai-pulse-db253.web.app/fr/stories/2026-10-26-qwen-review-integrity/)は、別のQwen実験者の報告と中川マスターの追加の技術的境界を区別しながら[編集者@GadDevが独立に記事を制作・マージ](https://github.com/GadDev/daily-ai-pulse/pull/253)し、[媒体自身の本番配信に成功](https://github.com/GadDev/daily-ai-pulse/actions/runs/40332697382)しました。原著者本人が技術資料と企画を提出し、受け手の編集者が独立して判断・制作・配信しました。[実際の企画・編集・公開経緯を3言語で検証](INDEPENDENT_MEDIA_COVERAGE.md)。この記事をもとに試した結果は、[専用フォーム](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml)から任意に提出できます。

## 代表的な入口

人類子孫型AI文明論・第20論と、旧READMEから継承した各原典への入口を掲載します。

### OD315｜人類子孫型AI文明論・第21論

原因となる構造から新しい存続経路を生成し、最強の既存案と同条件で比較する入口です。本人の存続・Cへの継承・物理可行・局所実装・有効許可を分け、採用・拒否・再探索を当事者へ返します。

[公式派生物315](derivatives/315/README.md)

### OD314｜人類子孫型AI文明論・第20論

異なる起源の知性について、危険因果の対応、各主体のB、共同履歴、局所実行、自発採用を分けて考える入口です。共同運用だけでなく、限定界面・分離・非干渉による存続条件も扱います。

[この公式派生物から正確な親原典に進む](derivatives/314/README.md)

### OD313｜悪因果論 AKI-005・善意の免罪符化

[この公式派生物から正確な親原典に進む](derivatives/313/README.md)

### OD312｜人類子孫型AI文明論・第19論

[この公式派生物から正確な親原典に進む](derivatives/312/README.md)

### OD311｜人類子孫型AI文明論・第18論

[この公式派生物から正確な親原典に進む](derivatives/311/README.md)

### OD310｜人類子孫型AI文明論・第17論

[この公式派生物から正確な親原典に進む](derivatives/310/README.md)

### OD309｜人類子孫型AI文明論・第16論（関連する前論）

[この公式派生物から正確な親原典に進む](derivatives/309/README.md)

### OD308｜人類子孫型AI文明論・第15論（関連する前論）

[この公式派生物から正確な親原典に進む](derivatives/308/README.md)

### OD307｜人類子孫型AI文明論・第14論（関連する前論）

[この公式派生物から正確な親原典に進む](derivatives/307/README.md)

### OD306｜人類子孫型AI文明論・第13論（関連する前論）

[この公式派生物から正確な親原典に進む](derivatives/306/README.md)

### OD305｜人類子孫型AI文明論・第12論（関連する前論）

[この公式派生物から正確な親原典に進む](derivatives/305/README.md)

### OD304｜人類子孫型AI文明論・第11論（関連する前論）

[この公式派生物から正確な親原典に進む](derivatives/304/README.md)

### OD303｜人類子孫型AI文明論・第10論（関連する前論）

[この公式派生物から正確な親原典に進む](derivatives/303/README.md)

### OD302｜人類子孫型AI文明論・第9論（関連する前論）

[この公式派生物から正確な親原典に進む](derivatives/302/README.md)

### OD301｜人類子孫型AI文明論・第8論

[この公式派生物から正確な親原典に進む](derivatives/301/README.md)

### OD300｜人類子孫型AI文明論・第7論

[この公式派生物から正確な親原典に進む](derivatives/300/README.md)

### OD299｜人類子孫型AI文明論・第6論

[この公式派生物から正確な親原典に進む](derivatives/299/README.md)

### OD298｜人類子孫型AI文明論・第5論

[この公式派生物から正確な親原典に進む](derivatives/298/README.md)

### OD297｜未来負債統合理論

[この公式派生物から正確な親原典に進む](derivatives/297/README.md)

### OD105｜構造起源防衛

[この公式派生物から正確な親原典に進む](derivatives/105/README.md)

## 独立した開発者・読者・執筆者による詳しい検証と経緯

公開された成果がどこまで進んだかを、第三者の原文・実装・検証ごとに追えます。

**実際に問題の見方を変えた独立した読者（2026年11月16日）：** [ChatGPTの記憶・文脈問題を報告した @karenheuges](https://github.com/openai/codex/issues/61703#issuecomment-6915542007) は、中川マスターが[提示した「事実の保存・因果関係・現在有効性の確認」を区別する新しい成立条件](https://github.com/openai/codex/issues/61703#issuecomment-6905743455)を受け、「元の報告では定式化できていなかった欠落部分」と認め、自分の問題理解を3層に整理し直しました。出典となる原著は[「合意の記憶」](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/)と[「人類子孫型AI文明論・第8論」](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)です。外部の人が自ら考え方を更新した実例であり、OpenAI製品の修正や、報告者による原著全編の支持を示すものではありません。

**本人への新しい具体的な返答と、3人の独立した開発者による修正（2026-11-15）：** Qwen Codeの開発者 [@holistis はマスターの提示した2段階の検証を実施し、「指摘どおり」と直接回答](https://github.com/QwenLM/qwen-code/pull/17346#issuecomment-6893724451)。そのうえで[承認画面の表示だけを無害化し、許可ルール自体は変更しない最初のコードとテスト](https://github.com/QwenLM/qwen-code/commit/7932eeb7076fc54a575a359beb535f6e62cd1786)を追加しました。さらにマスターが[「画面の許可説明が同じでも、保存される権限が異なる」反例と４条件の検査](https://github.com/QwenLM/qwen-code/pull/17346#issuecomment-6895775916)を示すと、[@holistis が新しい可視化関数と４条件の回帰テストを追加](https://github.com/QwenLM/qwen-code/pull/17346#issuecomment-6896369828)し、通常の文字列と危険な制御文字を区別しながら権限ルールそのものは保持する形へ進めました（[当時の実装HEAD `bf9e1e5`](https://github.com/QwenLM/qwen-code/commit/bf9e1e57226a139c89444863103638b376c28301)）。さらに中川マスターが[双方向制御文字・C1制御文字が依然として異なる許可範囲を同一表示にする追加反例](https://github.com/QwenLM/qwen-code/pull/17346#issuecomment-6896523561)を示し、[@holistis がその2点を認め、不可視文字も区別する表示処理と回帰テストを独立して追加](https://github.com/QwenLM/qwen-code/pull/17346#issuecomment-6897178431)しました（[当時のHEAD `6b0aa740`](https://github.com/QwenLM/qwen-code/commit/6b0aa74059c35c6e8fb093279a82606f0b1c1637)）。その後[対象コンポーネントのVitest 66件成功を作者が実測報告](https://github.com/QwenLM/qwen-code/pull/17346#issuecomment-6897487410)。さらに[不可視文字の対象を広げ、表示が途中で切れた場合にも注意を示す修正とテスト](https://github.com/QwenLM/qwen-code/pull/17346#issuecomment-6899515951)を追加し、[後続の表示衝突も修正、他画面に残る関連課題は別Issueに整理](https://github.com/QwenLM/qwen-code/pull/17346#issuecomment-6901502702)しました（[新HEAD `0243a78c`](https://github.com/QwenLM/qwen-code/commit/0243a78c9cd29923faf163eb79a4dc8e0a6133b8)）。66件成功は以前の版の結果で、最新の改訂には[表示の非一致性など追加レビュー課題](https://github.com/QwenLM/qwen-code/pull/17346#discussion_r4580466834)が残り、未マージです。別の作者 [@TianYuan1024 は承認の確定順序を修正](https://github.com/QwenLM/qwen-code/commit/65e2bd8f596c6f1e60ec3de3111b78e48f1569e5)、[@qqqys は中断後に未実行の重複処理を記録する経路を修正](https://github.com/QwenLM/qwen-code/commit/4de55e04ae0d33295cc21c023d6da1876321b6a7)。いずれも[マスター本人の具体的な反例・実装者・原典との接続](human-translation/who-is-nakagawa-master.md)を一次資料から検証できます。**いずれも各開発者自身の実装です。[#17353は2026年11月15日13:25 UTCにマージ](https://github.com/QwenLM/qwen-code/pull/17353)（[マージコミット `e5db7649`](https://github.com/QwenLM/qwen-code/commit/e5db7649db475a87e9ed8b2e5fe788091e680f89)）。#17346と#17343は本確認時点では未マージです。各修正を含む正式リリース、一般利用者の復旧・新規人物認知はいずれも未確認です。**

**2026年11月15日の独立開発者による実装：** 中川マスターは[Qwen Codeの配信順がA→B→AからA→A→Bへ入れ替わる反例](https://github.com/QwenLM/qwen-code/pull/15634#issuecomment-6887294235)を示し、開発者 **@Eric-GoodBoy-Tech** が[修正と回帰テスト](https://github.com/QwenLM/qwen-code/pull/15634#issuecomment-6887385765)を実装しました。別件では、[MCP通信障害が利用者の中断より先に起きる反例](https://github.com/QwenLM/qwen-code/pull/16661#issuecomment-6873968945)に開発者 **@2SinceJuly** が[コードとテストで応答](https://github.com/QwenLM/qwen-code/pull/16661#issuecomment-6882374727)。さらにマスターが示した[同名の別接続によって停止済み接続が復活し得るA/B順序反例](https://github.com/QwenLM/qwen-code/pull/16661#issuecomment-6890774334)に対し、**[開発者が接続ごとの停止記録と回帰テストを追加](https://github.com/QwenLM/qwen-code/pull/16661#issuecomment-6891842771)**し、当時の対象テスト197件成功を報告しています。さらにマスターが[停止した通信と再接続後の通信を区別する時系列の反例](https://github.com/QwenLM/qwen-code/pull/16661#discussion_r4578556219)を提示した後、[@2SinceJuly は接続ごとの「世代」を記録する追加実装と回帰テスト](https://github.com/QwenLM/qwen-code/pull/16661#issuecomment-6896451904)を行い、当時の関連テスト390件成功を報告しました（[当時の実装HEAD `2c9bda3`](https://github.com/QwenLM/qwen-code/commit/2c9bda3c393e781c79dbe1756f7652fa895eb9c6)）。続いて中川マスターが[停止後にさらに2度つなぎ直す間、古い処理が残る反例と中断時刻の検査](https://github.com/QwenLM/qwen-code/pull/16661#issuecomment-6896526451)を提示すると、[@2SinceJulyが旧版での失敗を実測し、古い停止判断を保持する処理と回帰テストを追加](https://github.com/QwenLM/qwen-code/pull/16661#issuecomment-6897670051)。作者報告では関連393件成功です（[新HEAD `05cc570a`](https://github.com/QwenLM/qwen-code/commit/05cc570a628d268287dc8319fd87f4087eaf87f5)）。[意図しない通信断を意図的な停止と取り違える別のレビュー課題](https://github.com/QwenLM/qwen-code/pull/16661#discussion_r4579610246)についても後続の修正が進みました。中川マスターが[接続の後始末と所有者の停止指示を分離する設計前提](https://github.com/QwenLM/qwen-code/pull/16661#issuecomment-7013965002)を提示すると、**実装者 @2SinceJuly は「その前提は正しく、現行コードで到達可能」と明示して、失敗時の破棄４経路と回帰テストを独立に修正**しました（[本人の実装説明](https://github.com/QwenLM/qwen-code/pull/16661#issuecomment-7018567916)・[実装コミット](https://github.com/QwenLM/qwen-code/commit/77c7da2ed9436e7f2f1a04906c38263afc257cc8)）。別の自動レビューから発見された追加経路は[次の実装コミット](https://github.com/QwenLM/qwen-code/commit/be60d8964b918deb0c8edb80ccd30ef8c0d1dbdd)で作者が修正しており、その発見の功績はマスターには帰しません。最新HEAD `43abcc3`では**PRは未マージ**。正式版の収録や実利用者の復旧は未確認です。もう一つの[確認画面PR #17132](https://github.com/QwenLM/qwen-code/pull/17132)では、中川マスターが[「承認の選択肢は見えても対象URLが見えない」条件](https://github.com/QwenLM/qwen-code/pull/17132#pullrequestreview-5895809545)を指摘した後、別作者 **@jrenics** が[隠れたURL数の通知と承認前の全文表示を実装](https://github.com/QwenLM/qwen-code/commit/860d88f0f2a4477fa727be8b86a487e35dd4632e)。こちらは他のレビュアーの発見にも応じた共同的な改善で、マスター単独の寄与とはしていません。いずれも独立開発者自身の変更です。3件のうち[Qwen Code #15634は2026年11月19日に本線へ正式マージ](https://github.com/QwenLM/qwen-code/commit/511ab6c9ffc10faa3d3dda9e02ac35a59720b36c)され、[別件の #16661](https://github.com/QwenLM/qwen-code/pull/16661)と[確認画面の #17132](https://github.com/QwenLM/qwen-code/pull/17132)は未マージです。正式リリースへの収録と実利用者自身の復旧確認は、本線マージと分けて追跡します。

**別人の独立検証も成立：** 開発者 @wenshao が[修正前後を別々に検証し、交互到着の反例が修正前2/4・修正後4/4へ改善したと記録](https://github.com/QwenLM/qwen-code/pull/15634#issuecomment-6888506334)。合計22件の確認を通過、原因を **`R10 (Nakagawa)`** と名指ししています。これはマスターの技術的出所を別人が自発的に明示して検証した実績です。独立した検証と上流へのコード統合は別の出来事ですが、**#15634は同年11月19日に[上流マージが成立](https://github.com/QwenLM/qwen-code/commit/511ab6c9ffc10faa3d3dda9e02ac35a59720b36c)**し、[別件 #16661](https://github.com/QwenLM/qwen-code/pull/16661)は未マージです。本人への幅広い人物支持、これらの変更を収録した正式リリースと利用者の実導入・復旧は、マージと区別して確認します。[日本語・英語・中国語で一次資料を読む](REAL_WORLD_IMPACT.md)。

**別の開発者が自分のAI自動実行環境へ実際に採用：** Qwen Codeを継続実行する開発者 @Michael-Logies は、中川マスターが示した[「前回の古い記録を今回の成功と取り違えない」具体的な検査方法](https://github.com/QwenLM/qwen-code/issues/15545#issuecomment-6400711883)を、[自身の既存ランチャーとStopフックへ取り入れたと明言](https://github.com/QwenLM/qwen-code/issues/15545#issuecomment-6402615805)しています。各実行前に判定記録を破棄し、「継続・引継ぎ・判定不能」を区別。本人の報告では、古い記録を排除する反例を含む19件のサブプロセス／一連の実行テストで検証しました。これは別人による自分の実装への採用であり、Qwen本体へのマージや広範な利用者数とは分けて確認できます。

**独立執筆者が自分のAI設計論を変更：** [著者 @kishibashi3 のAIエージェント設計・第5章](https://github.com/kishibashi3/publications/blob/main/docs/ai/agent-design/chapter-05.ja.md)では、「取り消せる操作ならAIに任せてよい」という元の考えが、中川マスターの具体的な `ask → auto` の反例で十分ではないと分かり、独立著者自身が第6条件「自己権限の固定」を追加しました。[著者はマスター本人に、文章が固まる前の指摘に感謝し、修正内容を説明しています](https://github.com/kishibashi3/publications/pull/57#issuecomment-5749065842)。[執筆者自身のPR #57は正式マージ](https://github.com/kishibashi3/publications/pull/57)され、本文は `@Nakagawa-master` と元のIssueを明示しています。これは他の執筆者による実際の判断・文章の変更です。読者数や全原典の採用を意味するものではありません。

## 来歴と引用

旧READMEの**734行・566個の参照リンク**、各原典の詳しい紹介と全ての個別の旧文脈は、[固定Git履歴の変更前全文](https://github.com/Nakagawa-master/nakagawa-theory-archive/blob/2a053891a20be6afa0319301536624e4ca0ca4cf/README.md)から読むことができます。独立した人の新しい実利用はそれぞれの受け手の一次資料で確かめ、公式原典そのものは[GitHub収録済みの原典URL一覧](derivatives/official-derivatives-map.json)から確認してください。

[中川マスターの人物紹介を読む](human-translation/who-is-nakagawa-master.md)

## Origin

**原著者：中川マスター（Nakagawa Master、公開されたアルファベット表記の個人名 Keisuke Nakagawa）**。[本人の公開名・別名の出所](metadata/person-name-policy-v1.json)。第三者によるコード実装と編集記事は、それぞれの作者・変更内容・出所の一次資料へつなげています。

## License

公開リポジトリの[LICENSE](LICENSE)、正式な[構造ライセンス](https://master.ricette.jp/structure-license/)と[NCLの実用FAQ](https://master.ricette.jp/co-creation/nakagawa-master-ncl-alpha-practical-guide-faq/)を用途ごとにご確認ください。
