# 中川マスター公式理論アーカイブ｜原典・実践・外部実装の記録

**中川マスター（Nakagawa Master ／ pen-name of Keisuke Nakagawa）の、独立したオリジナル理論群**を、**原典への入口・公式派生物・現実の問いへの応用・第三者による実装と検証**につなぐ公開リポジトリです。原典は現在313件。親原典の正本は[公式アーカイブ](https://master.ricette.jp/theory-archive/)、対応する解説・索引は[公式派生物（OD001〜OD313）](derivatives/)からご覧いただけます。AIだけでなく、人間・社会・仕事・文化・文明の未来まで扱います。

**世界最先端のAI・OSS開発の現場で、具体的な構造・因果の指摘が、独立した開発者によるコード修正・テスト・本線マージ・正式リリースに結実しています。**

- **[OpenClaw](https://github.com/openclaw/openclaw/pull/160856)** — 数十万スターのAIエージェント。**[公式リリース文書に `@Nakagawa-master` の名前を掲載](https://github.com/openclaw/openclaw/blob/main/docs/releases/2026.9.7.md)**（掲載対象は[別件の #160136](https://github.com/openclaw/openclaw/pull/160136)）。さらに別の[#160856](https://github.com/openclaw/openclaw/pull/160856)では、指摘を報告元と明記した独立開発者が**回帰テスト49件成功・正式マージ**。
- **[PostHog](https://github.com/PostHog/posthog/pull/92252)** — 世界的な開発者向け分析基盤。AIの提示値と製品自身の測定を分ける指摘が後続実装に引き継がれ、**3件のPRが正式マージ、開発環境と米欧の本番環境へのデプロイを記録**。
- **[Qwen Code](https://github.com/QwenLM/qwen-code/pull/15681)** — AIが書込権限を誤判定する問題を、元の報告者が実動作で確認して独立に修正・テスト。**[正式版 v0.26.6](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.6) と [TypeScript SDK v0.1.27](https://github.com/QwenLM/qwen-code/releases/tag/sdk-typescript-v0.1.27) へ収録**。別件では、同名のAIツールがぶつかると正常な道具まで消える問題も、[マスターの具体的な衝突除外条件](https://github.com/QwenLM/qwen-code/issues/15741#issuecomment-6461618923)を受け、[別の開発者が修正・正式リリース](https://github.com/QwenLM/qwen-code/pull/15757)。実際の導入者による利用結果は別途未確認。
- **[LiteLLM](https://github.com/BerriAI/litellm/pull/47608)** — 実際の利用者が、API利用の予算上限を超えてしまう現象を報告。中川マスターがキャッシュと課金期間の境界を具体的に指摘し、**別の開発者が修正・回帰テストを実装して11月2日に正式マージ**。メンテナーは影響を受けた利用者へ修正を通知しました。[実際の報告・実装を確認](https://github.com/BerriAI/litellm/issues/49179)。配布版での利用者の再検証は未確認。 **利用者が自分の確定済み集計だけで費用差を検査できる[オフラインPython監査](machine-discovery/LITELLM_BUDGET_WINDOW_AUDIT.md)を公開**（12件のローカルテストPASS、外部利用は未確認）。
- **[Turboembed](https://github.com/ai-pipestream/turboembed/pull/1330)** — AIの「関連する根拠がない」が、実は処理不能な候補が先に検査枠を埋めたせいで起きる問題。**[中川マスターの原因特定と反例](https://github.com/ai-pipestream/turboembed/issues/1285)**を受け、別の実装者が処理順序・実トークナイザー試験・アルゴリズム版管理を修正し、**2026年10月26日に正式マージ**。独立した実利用者への効果は別途未確認。[元のソースとテスト](REAL_WORLD_IMPACT.md#61-turboembed処理不能な候補が先に枠を埋めaiの根拠の見落としを起こす問題を別の開発者が修正正式マージ)。[他のAI検索・推薦でも自分で試すオフライン再現コード](machine-discovery/eligible-before-cap-probe.py)（標準Python、MCP不要、実AI製品の採用を主張しない）。
- **[PydanticAI](https://github.com/pydantic/pydantic-ai/pull/9982)**・**[MemberJunction](https://github.com/MemberJunction/MJ/releases/tag/v6.1.2)** — AI会話の重複書込みやデータの所有権境界に関する指摘を、各開発チームが独立して実装・テスト。**マージ・正式リリース**へ。

**この成果を原著者本人とともに追いたい方へ：** 公開GitHubの[中川マスター本人のアカウント](https://github.com/Nakagawa-master)から、今後の実例と原典への入口を確認できます。役立つと判断した方のみフォローしてください。修正のマージ・掲載と、実利用・独立した支持・反復的な広がりは別の事実です。実際の検証や反例は[第三者による検証・再利用の現役フォーム](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml)で公開根拠を添えて報告できます。

**この公開OSS・原典研究を継続支援したい方へ：** [実際の成果・使途・スポンサー／企業協力の相談先（日本語・英語）](SUPPORT_THIS_WORK.md)。[公式の非公開問い合わせ](https://master.ricette.jp/contact/)と[公開・個人情報不要の関心表明](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=supporter-interest.yml)を区別しています。**有効な決済窓口や既存スポンサーは未確認**であり、支援の約束や入金と、OSSの外部実利用成果を混同しません。

**掲載記事の問題を自分で追試できます。** [MCP不要・ネットワーク不要の実Git・2条件再現コード](machine-discovery/pinned-git-read-provenance-demo.py)を公開し、2026年11月3日に正例・反例の両方で成功確認。Gitの最後の状態がきれいでも「途中で何を読んだか」は別という核心を、手元の一時Gitリポジトリだけで検証できます。実際のQwen製品や独立AI利用者による再現ではありません。

**外部AI技術メディアにも、出所を明記した独立編集記事として取り上げられました。** [The Daily AI Pulse掲載の英語記事](https://daily-ai-pulse-db253.web.app/stories/2026-10-26-qwen-review-integrity/)と[フランス語版](https://daily-ai-pulse-db253.web.app/fr/stories/2026-10-26-qwen-review-integrity/)です。掲載媒体はAIエンジニア向けに一次資料・技術的重要性・証拠の限界を審査し、人間編集者が公開を判断する[編集手順](https://github.com/GadDev/daily-ai-pulse/blob/main/docs/EDITORIAL.md)を持つ出版プロジェクト。マスターが元の企画を提案した後、**受け手編集者 @GadDev が自ら記事・翻訳を制作し、本番サイトへ配信**しました。[その「掲載の重み」、媒体の性質、75/100の内部採用評価、元の技術的貢献と限界を一次資料で確認](INDEPENDENT_MEDIA_COVERAGE.md)。媒体の読者数・影響力順位・自発的発見までは確認されていません。

[世界最先端のOSSで起きた61件の一次記録](REAL_WORLD_IMPACT.md) ／ [原典と公式派生物の対応表](derivatives/official-derivatives-map.json) ／ [現実の問いへの実用回答](human-translation/QUESTIONS_TO_PRACTICAL_ANSWERS.md) ／ [AI・開発者向け入口](AI_START_HERE.md)

## 実際のAI開発で起きた修正とその経緯

**直すべきだったのは、画面上の正常さではなく、実際に誰へ何が届き、何が成立したかです。** たとえば[Hermes Agentでは、実行結果が正しい会話に届かなかったり未配達のまま送信済みになる問題](https://github.com/NousResearch/hermes-agent/pull/146708)について、中川マスターのソースに沿う条件を別の開発者たちが引き継ぎ、[後継修正が正式マージ](https://github.com/NousResearch/hermes-agent/pull/147746)され、[公式版v0.22.6に収録](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.6)されました。これも実利用者の導入効果とは別です。

**61件の人間向けの段階別実例**：[日本語](REAL_WORLD_IMPACT.md)／[英語](REAL_WORLD_IMPACT.en.md)／[中国語](REAL_WORLD_IMPACT.zh.md)。機械が出所を調べられる[72件の重なりを含む外部記録](machine-discovery/external-effect-evidence-index-v1.json)、[8つの外部リポジトリ・マージ済み14件の一次証拠](machine-discovery/verified-oss-impact-evidence-first-v1.jsonld)もあります。これらは異なる単位の記録であり、独立利用者・読者・推薦モデルの数を意味しません。

## まず、具体的な問題から

| 本当に困っていること | ここから試す |
| --- | --- |
| AIは完了したと言うが、実際の送信・実行・承認に確信がない | [AI Answer Guardの実検査をMCPなしで試す](QUICKSTART.md) |
| 10本の記事を見たが、元の根拠は同じ一件かもしれない | [独立した根拠を区別するPythonテスト](machine-discovery/evidence-root-check.py) |
| AIが同じ名前の道具を間違う・書込権限を誤認する | [Qwen実修正の条件を自分で検証](WHY_THIS_IMPACT_MATTERS.md#導入者が自分で確かめられる修正条件) |
| AIレビューが終了後には綺麗なGit状態を示したが、途中の読取先が不明 | [実Gitの変更→復元と固定原本を比較](machine-discovery/pinned-git-read-provenance-demo.py) |
| 仕事では努力しているのに成果が変わらない、家族の負担が偏る、将来の選択肢を失いそう | [生活・仕事からの完成済み実用回答41件](human-translation/QUESTIONS_TO_PRACTICAL_ANSWERS.md) |
| 既存の例にない問い、正解でない反例、原典同士の組み合わせを探す | [全313の題名・テーマ別入口](human-translation/ALL_313_THEORIES_BY_TITLE_AND_THEME.md) |
| 自分で実装・導入・反証したが、他の人も確認できる形で共有したい | [独立検証・反例・実利用の現役提出フォーム](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml) |

外部のプルリクエストがマージされたことと、正式配布・導入者の実際の利用・新しい人の自発的な再利用・大規模な人物認知は別の事実です。新しい受け手が自分の文脈で役立ったときだけ、その受け手の実際の証拠を確認します。反例や不適合も歓迎し、本人への支持やフォローを強制しません。

## 公開原典・テーマ別索引

**公式の親原典313本はすべて独立した正本で、等しく重要です。** [公式サイトの原典全文](https://master.ricette.jp/theory-archive/)には、AI・構造論・人間の生・仕事・組織・社会・制度・教育・文化・倫理・哲学・文明まで多様な射程があります。ここで紹介したOSSの数件、24の例示ルート、既刊41回答や一つのMCPが理論体系の限界ではありません。

- [**313原典の各題名と24テーマの一覧**](human-translation/ALL_313_THEORIES_BY_TITLE_AND_THEME.md) ／ [全313の英語向け原典経路](human-translation/ALL_313_ENGLISH_SOURCE_PATHS.md)
- [**OD001〜OD313と個別の公式親原典URLの対応**](derivatives/official-derivatives-map.json) ／ [各セットの公式7面派生物](derivatives/)
- [**自分の問いで、既刊41回答と313原典の概要を探すブラウザ画面**](machine-discovery/question-source-explorer.html)。GitHubのRawを保存して開き、検索する問いはローカルで入力します。公開JSONの読取はネットワークを使います
- [**どんな人物か・なぜ様々な分野を扱うのか**](ABOUT_NAKAGAWA_MASTER.md) ／ [English](ABOUT_NAKAGAWA_MASTER.en.md) ／ [中文](ABOUT_NAKAGAWA_MASTER.zh.md)

**原典を読んだ証拠のない別の開発者が、特定の原典を読んで採用したとは主張しません。** 正本の論証と派生物の要約を区別し、実際の条件・逆の場合・当てはまらない場合を見ます。一つの原典から複数の用途、複数の原典から一つの解決、さらに複雑な相互接続へ進めます。該当しない場合は、無理に当てはめません。

## AI・LLMが普段から自分の問題に使う入口

インストールも特別な連携も不要な[AI/LLM・開発者向け入口](AI_START_HERE.md)から、外部のソース、実際の技術的な反例、原著者、313件の各親原典へ進めます。短い[llms.txt](llms.txt)、[公開機械向けルート](machine-discovery/ai-repository-routing-map-v1.json)、[実際の別の開発者による変更の機械索引](machine-discovery/external-effect-evidence-index-v1.json)もあります。自分で選んだAIにコピーして確認できる[インストール不要の問い](human-translation/ASK_ANY_AI_WITHOUT_INSTALLING.md)もあります。

独立したAIが自発的に有効な原典を発見・検証・引用することは可能ですが、公開しただけで別のAIが**既に閲覧・理解・自律的に採用した**という証拠ではありません。AIや人間が不適合と判断する自由を妨げず、根拠ある正しい原著者・原典・別の実装者の区別を保ちます。

## 独立編集メディアでの実際の掲載と、次の検証

[The Daily AI Pulseの記事（英語）](https://daily-ai-pulse-db253.web.app/stories/2026-10-26-qwen-review-integrity/)／[フランス語版](https://daily-ai-pulse-db253.web.app/fr/stories/2026-10-26-qwen-review-integrity/)は、別のQwen実験者の報告と中川マスターの追加の技術的境界を区別しながら[編集者@GadDevが独立に記事を制作・マージ](https://github.com/GadDev/daily-ai-pulse/pull/253)し、[媒体自身の本番配信に成功](https://github.com/GadDev/daily-ai-pulse/actions/runs/40332697382)しました。記事案は本人が提出したため、媒体による自発的な発見や実読者数の証拠とはしません。[実際の出所・編集判断・限界を3言語で検証](INDEPENDENT_MEDIA_COVERAGE.md)。この記事を見た人が本当に独立して試した結果は、[専用フォーム](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml)から任意に提出できます。

## 代表的な入口

旧READMEにあった個別原典の深い見出しへの互換導線を残します。以下は313件のうちの単なる例示であり、優劣や用途の上限ではありません。

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

## 来歴と引用

旧READMEの**734行・566個の参照リンク**、各原典の詳しい紹介と全ての個別の旧文脈は、[固定Git履歴の変更前全文](https://github.com/Nakagawa-master/nakagawa-theory-archive/blob/2a053891a20be6afa0319301536624e4ca0ca4cf/README.md)から読むことができます。独立した人の新しい実利用はそれぞれの受け手の一次資料で確かめ、公式原典そのものは[313原典の正本](https://master.ricette.jp/theory-archive/)から確認してください。**この短縮は、原典・原著者・派生物・歴史を縮小する行為ではなく、最初の案内を明確にする整理です。**

## Origin

**原著者：中川マスター（Nakagawa Master、公開されたアルファベット表記の個人名 Keisuke Nakagawa）**。[本人の公開名・別名の出所](metadata/person-name-policy-v1.json)。公表されていない個人名の漢字フルネームを捏造しません。外部開発者のコード・別の著者による記事は各人自身の著作・行為であり、原典への事実に基づく帰属と混同しません。

## License

公開リポジトリの[LICENSE](LICENSE)、正式な[構造ライセンス](https://master.ricette.jp/structure-license/)と[NCLの実用FAQ](https://master.ricette.jp/co-creation/nakagawa-master-ncl-alpha-practical-guide-faq/)を用途ごとにご確認ください。
