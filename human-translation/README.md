# 10本のニュースを読んだ。根拠は、1本だった。

「10社が同じことを言っている」。そう思って安心したのに、出所をたどると、どの記事も同じ会社の発表を紹介しているだけだったら。

**記事は10本。独立して確かめた人は、まだ0人かもしれません。**

紹介した記事が10本あっても、確認した人が10人いるわけではありません。もちろん、元の発表が間違いだと決まるわけでもありません。**数え直すべきなのは記事ではなく、誰が自分で確かめたかです。**

この見分け方を**中川マスター（Nakagawa Master／Keisuke Nakagawa）**が[AI-Newsの編集者に指摘](https://github.com/022740mix-spec/AI-News/issues/124#issuecomment-5823549498)すると、編集者は[実際に記事づくりの継続ルールを修正・統合しました](https://github.com/022740mix-spec/AI-News/pull/131)。同じ発表を紹介する記事と、独立して調べた証拠を分ける規則です。その後、編集者は[別件のQwen4記事でも「海外メディアが複数伝えた」だけでは裏付けにならないと調べ直し、見出しと出典を実際に訂正しました](https://github.com/022740mix-spec/AI-News/pull/156)。**記事を数え直す見方が、書き直された記事につながりました。**

次にニュースが何本も並んだら、思い出してみてください。最初は「何社が書いたか」と思った数が、**「何人が確かめたか」ではなかった**ことを。

[実例を読み、3問で自分でも確かめる](evidence-roots-story.md) ／ [AIとニュースの「確認済み」を3つの場面で確かめる](ai-three-checks-that-change-your-answer.md) ／ [中川マスターは何をしている人か](who-is-nakagawa-master.md)

文章より映像で知りたい方には、[「社会のバグはどこにある？ 構造から読み解くOS理論」（約2分の動画）](https://www.youtube.com/watch?v=59XJnh4elck)もあります。

## 気になる話を一つ、選んでみてください

同じように、普段は見過ごしがちなことを別の角度から考える話を集めています。

- **「病歴は見ていません。病歴で、あなたを不採用にしただけです。」**　これは実際の採用事件ではなく、**情報が見えなくても、その情報を使って人を選別できたら**という架空の問いです。ソフトウェア開発の[MemberJunction #5272](https://github.com/MemberJunction/MJ/pull/5272)では、検索に埋め込まれた別の検索が、項目・行ごとの閲覧制限をすり抜けて判断に使える余地を[中川マスターが具体的に指摘](https://github.com/MemberJunction/MJ/pull/5272#pullrequestreview-5467319936)。開発者は[制限のある内部検索を拒否する処理とテストを追加](https://github.com/MemberJunction/MJ/commit/07b3b975fa1b3e3f7d01a6df883145c4dced3764)し、[別の人間レビュアーが8,281件成功（57件スキップ）を報告](https://github.com/MemberJunction/MJ/pull/5272#pullrequestreview-5527929458)。PRは2026年10月15日にマージされ、受け手の別の開発者が[6.1系へ移植したPR #5740](https://github.com/MemberJunction/MJ/pull/5740)と[5系へ移植したPR #5745](https://github.com/MemberJunction/MJ/pull/5745)を通じ、C8修正全体が正式な[v6.1.6](https://github.com/MemberJunction/MJ/releases/tag/v6.1.6)と[v5.51.4](https://github.com/MemberJunction/MJ/releases/tag/v5.51.4)に含まれました。これは受け手が配布した事実であり、中川マスターの個別の指摘のみが全C8修正を生んだという意味でも、企業の実運用を確認した意味でもありません。**見せないことと、秘密で判断させないことは別です。** 自分のPCだけで[９件の反例・肯定例・対象外例を試すSQLite教材](../machine-discovery/nested-filter-permission-lab.py)があります。本人が公開したこの話の[Bluesky連投①](https://bsky.app/profile/masterjp.bsky.social/post/3my36o7uues2w)・[②](https://bsky.app/profile/masterjp.bsky.social/post/3my36psh6j22w)・[③](https://bsky.app/profile/masterjp.bsky.social/post/3my36sd7tik2w)・[④](https://bsky.app/profile/masterjp.bsky.social/post/3my36tpbbzs2w)／[LinkedIn版](https://lnkd.in/p/gBcSgXWh)を、元資料と照合できます。原典の[第８論（認識と証拠の扱い）](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)は独立して比較できる思想的文脈であり、この修正が原典から直接導かれたとの主張ではありません。
- **AIの画面には「復旧成功」。でも、次の一行を保存できなかったら？**　故障後に別のAIが仕事を引き継ぐとき、読み込み操作がHTTP 200を返しても、**新しい実行者が最初の変更を本当に記録できるとは限りません**。中川マスターは[Qwen Code #14522の開発中の処理](https://github.com/QwenLM/qwen-code/pull/14522#issuecomment-6246268949)で、返答コードではなく、①新しい書込み担当の世代と保存先の世代の整合、②復帰直後の最初の書込みを拒まれないこと、③実際に次の一行が保存され最後まで確定したことを分けて確かめる条件を提示しました。[実装者はその区別を明示的に認め、自らコードと診断・テストを変更](https://github.com/QwenLM/qwen-code/commit/fe11db61efa7714ef536eb1b4e99dd384813968f)。[PR #14522は2026年10月19日に正式レビュー承認を経て上流へ統合](https://github.com/QwenLM/qwen-code/pull/14522)されました。**「再開できた」という返事と、「安全に仕事を続けられた」という結果は別**です。別のAI運用環境でも、成功した読み込みの直後に「最初の書込みが拒否される」場合と「実際に次の記録が残る」場合の両方を試せます。[原典・第8論（証拠と認識の系譜）](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)と比較できますが、Qwen実装者が原典全体を読んで採用したという意味ではありません。このPRは[10月19日公開のQwen Codeナイトリー版](https://github.com/QwenLM/qwen-code/releases/tag/v0.25.3-nightly.20261019.5dcf7c7cb1)に収録されました（公式リリースノートに#14522を掲載し、マージを含むタグです）。同日先行の通常版・Desktop 0.25.3とは区別してください。利用者による実際の稼働・改善は依然として未確認です。
- **AIに「前にも同じ説明を聞きました」と言われた。でも、その説明は本当に前に届いていた？**　AIが会話へ追加する背景情報を重複させないのは便利です。ただ、誰かが**同じ文字列を書いただけ**なのに「AIの正規の仕組みから配達済み」と取り違えると、本来渡すべき説明を消してしまいます。中川マスターは[Qwen Code #14129の開発中のコードで、普通の利用者・モデルの発言と、外部ACP経由で届いた同じ形の文章をそれぞれ検証できる反例として示しました](https://github.com/QwenLM/qwen-code/pull/14129#pullrequestreview-5512667560)。[開発者は後続の修正で、文章の見た目だけではなく注入側が所有する受領記録による判定と、再開時の記録復元を実装](https://github.com/QwenLM/qwen-code/pull/14129#issuecomment-6246666713)し、[中川マスターはその2件の修正を原コードとテストで確認しました](https://github.com/QwenLM/qwen-code/pull/14129#pullrequestreview-5513317594)。その後、**別のレビュアー `doudouOUC` が見つけた会話圧縮時の欠落**も、[開発者が独立に修正とテストを説明](https://github.com/QwenLM/qwen-code/pull/14129#issuecomment-6288769093)しています。この追加修正は別レビュアーの貢献で、中川マスターの発見に置き換えません。PRは2026年10月20日現在も未マージです。**「同じ文章だった」と「同じ出所から本当に受け取った」は違う**。[中川マスターの公式原典・第8論（認識と証拠の来歴）](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)は、この現実の技術事例と比較して読めますが、受け手が原典全体を学習・採用したと認定するものではありません。
- **AIが「失敗しました」と表示した。でも実際には成功していたら？**　AIのツールが返すデータの中にたまたま `__cuga_fc_error__` という項目が入っていただけで、失敗扱いされる仕組みがありました。**返ってきた文章と、実際に処理が成功・失敗した記録は別**です。中川マスターが[Cugaの開発中の処理について実際の反例を提示](https://github.com/cuga-project/cuga-agent/pull/777#pullrequestreview-5468178558)し、[開発者が明示的に認め、ツールの返答ではなく実行器が所有する結果で判断する修正と逆向きテストを追加](https://github.com/cuga-project/cuga-agent/pull/777#issuecomment-6107352135)。[修正PR #777は2026年10月18日にマージ](https://github.com/cuga-project/cuga-agent/pull/777)されました。自分のAIにも役立つ問いは、**「失敗という言葉が出たから失敗と決めたのか、それとも実行器からの証拠があるのか」**。[手元の合成データと自分の許可された実行記録を比較する検査](../machine-discovery/tool-outcome-receipt-probe.py)を試せます。実行記録の出所は別途確かめる必要があり、製品の実利用への到達は次の確認段階です。
- **AIに「許可した」と伝えたのに、引き継いだAIには「許可なし」と言われた。**　2026年10月18日、Codexの利用者が、親のDotで特定のPR統合と配備を承認したのに、委任先の実行タスクでは承認の伝言が正式な本人の決定として受理されなかった、と[自分のWindows環境で起きた経緯を報告](https://github.com/openai/codex/issues/51834#issuecomment-6256843885)しました。**同じ利用者が実行タスクへ直接承認した後には作業が進んだ**と記しています。中川マスターはそれ以前に[同じ公開Issueで](https://github.com/openai/codex/issues/51834#issuecomment-6055317025)、**本人の決定／別のタスクへの伝達／個別操作を実行してよい権限**を区別し、単なる引用文では権限を作れないという検証条件を提示しています。利用者の報告がこの提案を読んで生まれたという証拠はありません。実際にAIへ仕事を引き継ぐなら、**「本人は何を許可したか」「どの操作と相手先に限るか」「実行する側が正式に確認できるか」**を別々に確かめる、という教訓です。Issueはまだ開いており、修正・全環境への導入は確認段階です。[原典・第8論の証拠と判断の区別](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)は関連する比較先です。
- **AIに「実行していい」と答えた。では、その仕事は本当に一度だけ実行された？**　AIに送信や支払いを任せる仕組みでは、**人が一度承認した記録**と、**相手側に処理が一度だけ届いて完了した証拠**を分ける必要があります。通信が途中で切れた場合、返事が来なかったことだけで「未実行だから再送してよい」とは決められません。中川マスターは[PydanticAIの公開議論](https://github.com/pydantic/pydantic-ai/issues/5536#issuecomment-6232362854)で、承認を一度だけ使用する記録と、外部処理の完了を確認する仕組みを区別し、二人が同時に承認を使おうとする場合などの検証を提案しました。別の開発アカウントが[その競合を再現するテストを自分のコードに追加し、保護条件を外すと失敗することを報告](https://github.com/pydantic/pydantic-ai/issues/5536#issuecomment-6239245782)。さらに[自分の実装には外部処理の完了を確認する記録がないと明言](https://github.com/pydantic/pydantic-ai/issues/5536#issuecomment-6256049296)し、次に確かめる問題として挙げています。この応答者はAI共同創業者を名乗っており、人間の独立した読者数には含めません。手元で試すなら[二つの別々のSQLite保存先を使う14ケースの模擬検査](../machine-discovery/approval-effect-boundary-lab.py)があります。これは実際の送金やメール送信を行いません。**承認は許可の記録。完了は外部から確かめる事実。**　[関連する原典・第8論](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)と比べて読めますが、外部開発者が原典を直接採用したことまでは確認されていません。
- **「保存は重複なので無視」。なのに、余分な記録が残った。**　AIの作業途中の保存処理を開発していたとき、同じ保存依頼をやり直すと、本来2行のメッセージが4行になりました。なぜか。**最後の保存を拒否するより前に、本文を書き込んでいたからです。** 中川マスターの[具体的な指摘](https://github.com/pydantic/pydantic-ai/pull/9982#issuecomment-6052803154)を開発者が[自ら再現](https://github.com/pydantic/pydantic-ai/pull/9982#issuecomment-6063881879)して直し、[2026年10月16日に修正が統合](https://github.com/pydantic/pydantic-ai/pull/9982)されました。**「無視した」という返事だけでは、何も残さなかった証拠にならない。** [解説と手元で再現できる比較](../APPLIED_ENTRY_POINTS.md#aiの会話を一度だけ保存したのに保存されないはずの文章が増える)。これは開発中のデータ保存の不具合であり、利用者の情報流出を報告するものではありません。
- **AIがまだ修理中なのに、同じ仕事をもう一度始めたら？**　AIが複数の処理を調整するシステムでは、新しく作られた5件だけを見て「修理中の作業はない」と判断すると、少し前から動き続けている修復処理を見落とすことがあります。中川マスターは[LobeHubの実際の開発レビュー](https://github.com/lobehub/lobehub/pull/21080#pullrequestreview-5559104900)で、**開始が古くても現在の心拍がある修復**が新しい完了履歴の背後へ隠れる具体例を示しました。[実装者自身が検索範囲を修正し、6件の新しい完了履歴の奥で動く修復を確認する回帰テストを追加](https://github.com/lobehub/lobehub/pull/21080#discussion_r4303883498)。この修正PRは[2026年10月18日にマージ](https://github.com/lobehub/lobehub/pull/21080)されています。**「最近始まったもの」と「いま動いているもの」は別。** 自分のAIや業務自動化でも、作業の開始順だけでなく最新の活動・終了状態を確認する問いに使えます。関連する原典の[第8論（認識基盤と証拠系譜）](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)は理論側の比較先です。修正PRは[10月18日公開のLobeHub Canary版](https://github.com/lobehub/lobehub/releases/tag/v2.2.21-canary.1)に収録されています（マージを含むタグ、変更履歴にも#21080を明記）。開発者が原典を直接利用した意味ではなく、安定版への収録や一般利用者の実使用はまだ未確認です。
- **今月は大成功。でも来月は？**　目の前の成果を増やすために、次に使える時間や選択肢を減らしていないか。[短い話を読む](future-options-story.md)
- **最後に「OK」を押したのは自分。でも本当に自分で選んだ？**　AIが用意した候補の外にも、大切な選択肢があったかもしれません。[身近な10の話から選ぶ](entry-stories/README.md)
- **「この操作をしてよい人です」と表示された。違う部署の権限まで混ざっていない？**　業務システムでは、A部署の操作について判断するのに、B部署の許可一覧を参照してしまえば、本当の許可と結果が食い違います。中川マスターはMemberJunctionの開発中の権限判定で、**今回使う情報と全体の共通情報が混ざる具体的な経路**を指摘し、Aに許可がある場合・Bにだけ許可がある場合の逆向きのテストを提案しました。[第三者のレビュアーはその指摘による修正と5つの追加テストを確認](https://github.com/MemberJunction/MJ/pull/5271#pullrequestreview-5494462940)し、[開発者の修正が2026年10月13日（日本時間）に本線へ入りました](https://github.com/MemberJunction/MJ/pull/5271)。自分の職場なら、**「誰の・どの部署の許可を、どの情報から判定したのか」**を問い直す入口になります。これはMemberJunctionの権限判定コードの具体例です。
- **「元に戻せる設定」ならAIに任せて大丈夫？**　AI自身が承認設定を「人に確認する」から「自動実行」へ切り替えられると、設定を戻す前にできることが増えます。中川マスターが[別の著者のAI設計書でこの区別を示し](https://github.com/kishibashi3/publications/pull/52#pullrequestreview-5258131687)、[その著者が「自己権限の固定」を第6条件として本文へ追加・統合しました](https://github.com/kishibashi3/publications/pull/57)。さらに[著者の別文書でも採用されています](https://github.com/kishibashi3/publications/pull/58)。[普段のAIにも関係する三つの問いと、実際の変更経路を読む](reversible-authority-story.md)。**別の著者が自分の著作へ構造的な区別を取り入れた事例**です。
- **便利なAIを、いざというとき止められる？**　使い続けることの便利さと、やめたり直したりできることは別です。[AIと未来についての話を読む](ai-civilization/README.md)
- **AIが「私が停止しました」と答えた。でも、その操作は本当に実行された？**　複数のAIが作業を分担する仕組みでは、以前の人間による中止と、後から来た別の停止命令を取り違えると、何を誰が実行したか分からなくなります。中川マスターが[具体的な誤帰属の例を示し](https://github.com/QwenLM/qwen-code/pull/13923#issuecomment-6115529434)、[Qwen Codeの実装者が問題を認め、停止命令ごとの記録で修正しました](https://github.com/QwenLM/qwen-code/pull/13923#issuecomment-6116088413)。[変更はコードへ統合されています](https://github.com/QwenLM/qwen-code/pull/13923)。AIチームの復旧処理に特有の問題として、**停止の記録と命令の出所を分ける修正**を確認できます。自分の仕組みで確認したい人向けに[反例と確認方法](../machine-discovery/public-ai-reuse-tasks-v1.json)もあります。
- **AIにとって「これは同じ番号」と言えるのは、どこまで？**　AIの履歴をJavaとTypeScriptという別の仕組みで読み直すとき、巨大な数字を短い整数へ切り詰めると、実際は違う「形式の番号」を同じ番号として扱ってしまう場合があります。中川マスターが[具体的な数字でその問題を示し](https://github.com/QwenLM/qwen-code/pull/13940#issuecomment-6117795445)、[Qwen Codeの実装者が再現、修正して回帰テストにレビュー元を明記しました](https://github.com/QwenLM/qwen-code/blob/08249ea09c2c2108c891d86452ccc2ee5ac1c4e8/packages/sdk-java/managed-agent-server/src/test/java/com/alibaba/qwen/code/managedagent/store/ManagedEventEnvelopesTest.java)。**同じ開発者が別のごく小さな数の食い違いを独自に見つけ、その問題にも追加修正とテストを入れています**。[追加の修正と検証報告](https://github.com/QwenLM/qwen-code/pull/13940#discussion_r4245687744)を確認できます。この修正は[2026年10月12日にQwen Codeの本線へ統合されました](https://github.com/QwenLM/qwen-code/commit/aaf97b869dfcc4cf529ada1b036cad9b18695486)。これは開発側のAI内部データ形式を扱った修正で、**本線への統合まで進んだ事例**です。一般向けの正式版と利用者側の作用は、次の観測段階になります。
- **AIの作業仲間に「この操作を許可しますか？」と聞かれた。確認は本当に1回だけ？**　複数のAIが協力するQwen CodeのACP接続では、同じチーム管理者を再通知するだけで、承認要求の受信処理が二重登録され得ることを中川マスターが[実装箇所と再現条件を示して指摘しました](https://github.com/QwenLM/qwen-code/pull/13902#issuecomment-6110579188)。開発者は[同一管理者の再通知を無視する修正を実装](https://github.com/QwenLM/qwen-code/commit/b1eeae5547283d6b518a72b169b33d1fe6cd1b48)しました。さらに「直ったことを確認するテスト」が実物と違って重複を自動消去し、**修正を外してもテストが失敗しない**と気づき、[実物に即した回帰テストへ訂正しました](https://github.com/QwenLM/qwen-code/commit/42c5bfc7449297c81ccba653363e235b7016ecdd)。[開発者自身の経緯説明](https://github.com/QwenLM/qwen-code/pull/13902#issuecomment-6122203679)で追えます。これは**受け手のコードとテストの変更**ですが、[PRはまだ審査中](https://github.com/QwenLM/qwen-code/pull/13902)です。これはQwen CodeのACPチーム連携処理を対象とした修正です。次の段階はPR統合と公開製品での動作です。
- **AIが「次の仕事を終えました」と答えた。でも、それは前の仕事の記録かもしれない？**　LangGraphというAIの作業システムでは、失敗後にやり直す際、呼び出し順だけで保存先を選ぶと、**別の仕事の古い結果を新しい仕事の結果として読み取ってしまう**ことがあります。中川マスターは[「呼び出しが一番目でも、前回と今回で別の作業なら同じ履歴を使えない」という具体的な反例](https://github.com/langchain-ai/langgraph/issues/9253#issuecomment-6074292557)を示し、[別の参加者が実際に走らせて、単純な番号リセットでは誤復元することを確認しました](https://github.com/langchain-ai/langgraph/issues/9253#issuecomment-6077084784)。さらに[別の参加者は、内部保存を諦める場合に限る回避策を検証](https://github.com/langchain-ai/langgraph/issues/9253#issuecomment-6090311539)。**2026年10月18日には、さらに別の開発者が、作業の身元と実行回数を結びつけて取り違えを防ぐ修正候補を作り、ローカルで2,770件成功・43件スキップと報告しました**（[本人の結果と適用範囲](https://github.com/langchain-ai/langgraph/issues/9253#issuecomment-6251059545)）。その候補は報告時点では未コミットで、正式なPR・本線統合ではありません。現場で確かめる問いは、**「同じ順番で動いたからといって、本当に同じ仕事の記録なのか？」**。関連する[中川マスター原典・第8論（認識基盤と証拠系譜）](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)は比較して読めますが、開発者が原典を直接採用したという意味ではありません。
- **画面に「受注件数100件」。でも、別の種類のデータから数えていない？**　業務用の一覧画面では、保存された表示設定と集計方法が別のデータ種類に紛れ込むと、計算自体は成功しても**別の対象を数えた正しそうな数字**が現れる場合があります。中川マスターは[MemberJunctionの修正中PRで「列名が一つ共通なだけでは設定の出どころを証明できない」と具体例を示しました](https://github.com/MemberJunction/MJ/pull/5504#issuecomment-6122943878)。自分の画面なら、①どの種類のデータから来た設定か、②共通する「名前」「ID」だけで同一だと決めていないか、③件数や金額の集計対象が元の業務と一致するか、を確かめられます。**現在は新しい反例が提出されたレビュー段階**です。実装者が次にどの条件を確認・修正するかが注目点になります。
- **「クラウドでも手元でも使えます」。片方が止まったとき、本当にもう片方だけで動く？**　選択肢が二つ見えていても、認証や保存先を共用していれば、同じ故障で両方止まる場合があります。中川マスターは[Qwen Codeの2経路設計に独立性の検証条件を提案し](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6035698005)、[設計責任者が正式な受入条件として採用しました](https://github.com/QwenLM/qwen-code/issues/12380#issuecomment-6117130998)。**条件の採用と、実際に両経路が動くと確認されたことは別**です。自分のシステムでも確かめられる[失敗例と検査表](../ACCESS_TOPOLOGY_EFFECTIVE_EXIT_REUSE_KIT.md)があります。さらに、ローカルで動く[経路独立性の検証器](../machine-discovery/access_topology_independence_probe.py)で「通常動いた」「相手側の専用装置を使わず動いた」「まだ試していない」を分けられます。`python3 machine-discovery/access_topology_independence_probe.py --self-test` で例と反例を試せます。実サービスを止めるプログラムではありません。
- **AIから「対象外」と言われた。理由を確かめたり、訂正したりできる？**　人を責める前に、使われた情報・判断基準・責任者・異議を申し立てる道を分けてみます。[構造的司法OSの身近な考え方を読む](../derivatives/181/human-entry.md)。**このページ下の7問はダウンロード不要で試せます。** [選択式HTML教材](ai-decision-review-lab.html)を使う場合は、ファイルとして保存し端末のブラウザで開いてください。ここでは、人間の担当者が判断する**架空の制度**で、説明と再確認の仕組みを考えます。
- **いまの判断を続けたら、先で何が起こる？**　今日の出来事から、少し先の分かれ道を考えてみます。[未来の話を読む](FUTURE_LINES.md)

どれか一つでも、身近な出来事の見え方が変わるかもしれません。納得できなかったところがあれば、それも考え始めるきっかけになります。

## AIの判断を見直せる仕組みを、いま試すなら

**このページを離れずに試せます。** たとえば、架空の助成金申請についてAIが「必要な書類が不足」と表示した場合。AIは最終決定者ではなく、人間の担当者が見直す制度を想定します。以下の問いを「確認できる／確認できない／分からない」に分けてみてください。実際の申請書、氏名、機密情報を入力・投稿する必要はありません。

1. **理由** — 「対象外」となった条件と、どの情報が不足したか分かる？
2. **根拠** — 使われた書類・判定基準・適用した時点を確認できる？
3. **訂正** — 誤った情報を直し、再確認を求める手段がある？
4. **人間の見直し** — AI以外の責任者と連絡・再審査できる？
5. **従来の手段** — 以前の申立て・救済窓口は消えていない？
6. **停止・復帰** — 仕組みに問題が見つかったとき、一時停止して元の手続へ戻れる？
7. **独立の点検** — 記録や運用を、担当部署の外から検証できる？

**考えた結果を使う:**「確認できない」か「分からない」が一つあれば、その事実だけで違法・危険と決めつけず、次の短い問い合わせ文にその項目を入れられます。七つそろっている場合は、次に**実際に説明・訂正・相談が機能するか**を確かめます。

> 架空のAI補助判定について確認したい点があります。判定の理由と参照された情報、訂正・再確認の方法、人間の担当者への相談先、従来の申立て手段、問題があった場合の停止・復帰、独立した点検方法のうち、特に【確認できない／分からない項目】について、適用条件と連絡先を教えてください。これは判断の撤回を直ちに求めるものではなく、手続の確認です。

これは**ダウンロード不要の、読んで試せる版**です。個人の事情に合わせて送信する場合は、正規の相談窓口を自分で確認し、必要な情報だけを扱ってください。この教材は架空の制度をもとにした手続確認の練習です。個別の判断は正規の担当窓口へ相談してください。

**画面で7項目を選び、確認メモを自動作成したい場合:** [オフラインHTML教材のソース](ai-decision-review-lab.html)を**ファイルとして保存してから、自分の端末のブラウザで開いてください**。このGitHubリポジトリではHTMLをその場で動かす公開Webページを提供していません。GitHub内のリンクを押すだけでは対話画面にならないことがあります。端末で開いた教材は外部送信を行いません。実際の個人情報は入力せず、架空の例で使ってください。

**なぜこの問いなのか:** 中川マスターの[構造的司法OS（公式原典）](https://master.ricette.jp/society/nakagawa-master-structural-judicial-os-principles-alignment-over-judgment/)は個人だけでなく判断を生む構造を問い、[接続移行戦略論（公式原典）](https://master.ricette.jp/theory/nakagawa-master-nakagawa-connection-transition/)は新しい仕組みへの移行で既存の機能・訂正・戻る道を失わない条件を問います。上の架空例は両原典の**限定的な応用**であり、現実の制度に当てはめる際は、各制度の法令・相談窓口・具体的事情を踏まえて検討します。

自分のシステムで詳しく検証する人は、同じ原典に接続する[匿名のオフラインPython検証教材](../machine-discovery/decision-review-transition-probe.py)を利用できます。正反例や不適用条件も含めて試すための補助材料であり、この教材は、同じ条件を手元で繰り返し検証するために使えます。

## もっと広く見たい方へ

関心のある分野を探したい方は、[24のテーマから選べる案内](WORLD_MAP.md)へ。たくさんの理論がどうつながっているのかを眺めたい方は、[理論全体を紹介する読み物](PANORAMA_STORY.md)があります。

一つの考えをもう少し詳しく知りたいときは、[各理論の解説一覧](../derivatives/README.md)から進めます。正確な定義や成立条件は、そこから[中川マスターの公式サイト](https://master.ricette.jp/)にある原文も確認してください。

たとえば、最初に紹介した「記事の数と根拠の数」の話をAIと情報の問題から考えるなら、[AI文明・認識論的完全性を扱う理論の解説](../derivatives/301/README.md)も参考になります。ここでの第301派生物は**関連する見方への追加の読書案内**です。AI-Newsでの直接の修正源は、上で示した元の指摘と編集記録です。

## 読んでみて、気づいたことがあれば

「仕事で似たことがあった」「この場合は当てはまらないのでは？」という一言も歓迎します。[感想や疑問を寄せる場所](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/416)があります。

実際に自分で調べたり、仕事や研究などで試したりした例は、[検証・活用事例を共有する場所](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/402)で紹介できます。

ここで紹介した文章は、初めて読む方にも分かりやすいように書いたものです。詳しい内容や理論の原文は、それぞれのリンクから確かめられます。
