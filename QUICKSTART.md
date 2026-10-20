# まず自分で試す｜Nakagawa Master — GitHub Quickstart

このリポジトリは、中川マスター（Nakagawa Master / Keisuke Nakagawa）の理論原典につながる資料と、実際の開発・編集で問題になった区別を自分で確かめる道具を公開しています。**理論に賛成する必要はありません。まず一つ、役立つか試してください。**

原典： [中川マスター公式アーカイブ](https://master.ricette.jp/) ／ [公開リポジトリの説明へ戻る](README.md)

## 1. ニュースは10件。独立した裏づけも10件？

10本のニュースが同じ発表文を引用している場合、「記事が10本」と「独立した調査が10件」は違います。下のPythonツールは、入力された証拠の根・出典の関係・賛否の情報が、**独立した裏づけを主張する条件と整合するか**をオフラインでチェックします。

```sh
git clone https://github.com/Nakagawa-master/nakagawa-theory-archive.git
cd nakagawa-theory-archive
python3 machine-discovery/evidence-root-check.py --self-test
python3 machine-discovery/evidence-root-check.py --sample
```

Python 3標準ライブラリだけで実行できます。入力の出典関係が本当に正しいかをツールが調査するわけではありません。自分の検証用データは `python3 machine-discovery/evidence-root-check.py claims.json` として渡せます。**不整合は終了コード1、入力不備は2**です。

この区別が編集判断に採用された記録：[中川マスターの具体的提案（AI-News #124）](https://github.com/022740mix-spec/AI-News/issues/124) → [編集者が実装・マージした規則（#131）](https://github.com/022740mix-spec/AI-News/pull/131)。別の指摘を受けた記事の後続修正は[編集者自身の #156](https://github.com/022740mix-spec/AI-News/pull/156)から追えます。後続記事の変更すべてを一人の提案に帰属させるものではありません。

## 2. 「重複保存を無視した」はずなのに、記録が増える？

AIの会話履歴をSQLiteへ保存するとき、後段の重複INSERTだけを無視しても、**その前に書いたメッセージが残る**場合があります。こちらはSQLiteの合成データだけで、書込み順序の差を比べる再現用モデルです。

```sh
python3 machine-discovery/sqlite-idempotency-side-effect-probe.py --self-test
python3 machine-discovery/sqlite-idempotency-side-effect-probe.py --json
```

実際の上流製品を改変・検証するものではありません。現実の問題と開発者による修正は、[Pydantic AI #9982](https://github.com/pydantic/pydantic-ai/pull/9982) の議論・テスト・マージ記録から確認できます。

## 3. AIが「完了」と言った。それは成功？ 返事が届く？

仲間AIの `write_file` が `EACCES` で失敗したのに、画面には単に「finished」と出てしまうことがあります。「まだ仲間AIの報告が残っている」のに「安全に終了できる」と表示される場合もあります。

```sh
python3 machine-discovery/agent-team-signal-truth-probe.py --self-test
python3 machine-discovery/agent-team-signal-truth-probe.py --sample
```

[20ケースの独立した人工モデル](machine-discovery/agent-team-signal-truth-probe.py)は、表示上の失敗／成功、未配送メッセージと終了判定、履歴再生時のAIの身元を**別々に**検査します。入力JSONも検査でき、結果は `0=整合／1=不整合・喪失リスク／2=不備・判断不能` の終了コードで返します。ローカルの20ケースは実行済みですが、実際のQwenのコードをここでテストしたわけではありません。

実際の外部変化：[QwenのレビューBotによる問題の指摘](https://github.com/QwenLM/qwen-code/pull/13902#pullrequestreview-5556479545) → [Qwen開発者本人が3点の修正とテストを追加](https://github.com/QwenLM/qwen-code/commit/e9609863d4ef83c6c372fa8914fdfb00697327df)。この3件は**マスター本人の発見として主張しません**。同じPRの別の権限管理問題では、[開発者が中川マスターの具体的な提案を正しいと認め、修正に使った記録](https://github.com/QwenLM/qwen-code/pull/13902#discussion_r4277173979)があります。PR全体はまだ未マージです。

## 4. AIの返事を「読取済み」にした。保存先にも残った？

**AIチームで「相手の返事を処理した」と表示されても、その返事を次のAIが読める場所に残したとは限りません。** 保存装置が閉じた直後に書こうとしても遅く、読取済みの印だけが残ることがあります。

[中川マスターがQwen Code #13902へ提出した終了処理のレビュー](https://github.com/QwenLM/qwen-code/pull/13902#pullrequestreview-5540696114)に対し、開発者は[31行のセッション終了経路テストを自分で追加しました](https://github.com/QwenLM/qwen-code/commit/62c03b2eb62975775c66968d97f27f01028385a3)。[本人の回答](https://github.com/QwenLM/qwen-code/pull/13902#issuecomment-6233311153)では、**保存を閉じる前に仲間の報告が残ること**を確認し、順序を逆転させるとテストが赤くなると説明しています。既存の製品コードの保存順序は前のコミットで修正されており、このコミットはテストの追加です。別のレビュアー [`chiga0` は当時のHEADに対して承認を記録しました](https://github.com/QwenLM/qwen-code/pull/13902#pullrequestreview-5557786519)。その後のレビューでは**別の重大な不具合3件**（未配送の仲間AI報告の消失、失敗したツール結果の上書き、履歴巻き戻しで仲間AI通知を人間の発言と誤認）が見つかり、[10月19日の旧HEAD `daac4372` 時点で3件が未修正だったことが確認されました](https://github.com/QwenLM/qwen-code/pull/13902#pullrequestreview-5563910037)。**その後は受け手の開発者が3件を独立に修正**し、[失敗ツール結果の修正 `4837855e`](https://github.com/QwenLM/qwen-code/commit/4837855e1ca51a20e926a59ba83b1ec6fef14ce3)、[未配送キュー・履歴巻き戻しの修正 `bc3be225`](https://github.com/QwenLM/qwen-code/commit/bc3be22592fb73c40d1fa4e8707a2df34b808ee8)とテストを追加しました。以前の承認は今のHEAD全体の承認ではありません。中川マスター由来の既存の修正・テストは保持されていますが、**以前のHEAD `29e180f7` で5件のGitHubワークフローが成功した事実は、後続のHEADにも自動で引き継がれません。2026年10月20日05:40 UTCに `main` を統合した後のHEAD [`a8687921`](https://github.com/QwenLM/qwen-code/commit/a8687921bdd26a7285538cecb182a112d6ba3f7d) では、[テスト用モックと現行型の不一致](https://github.com/QwenLM/qwen-code/pull/13902#issuecomment-6284393512)によるビルド失敗が複数のCI経路で確認されました。PRはその確認時点で未マージです。最新状態は必ず[受け手自身のPRとCI](https://github.com/QwenLM/qwen-code/pull/13902/checks)で再確認してください。**これら後発3件は別のレビューbotが発見した問題であり、マスター本人の発見とは数えません。

異なるAIアプリでも保存経路を点検できるよう、[一件のメッセージに絞ったオフライン検証器](machine-discovery/agent-delivery-durability-boundary-probe.py)を用意しています。以下は人工的な「読取済み→セッション破棄→通知喪失」の入力例です。

```sh
python3 machine-discovery/agent-delivery-durability-boundary-probe.py --self-test
python3 machine-discovery/agent-delivery-durability-boundary-probe.py --sample-dispose > trace.json
python3 machine-discovery/agent-delivery-durability-boundary-probe.py --input trace.json
```

`--input` の終了コードは、**0=このモデルで確認できた安全な保存順序、1=消失の可能性または終了後の未解決、2=判定不能・不適用・入力不備**です。CIでは2を合格として扱わないでください。現在のコードには17の合成ケースと、それぞれの終了コードに対する17の検査が書かれています。これは独立したQwen実機テストではなく、手元の保存経路の順序を考えるためのモデルです。実際の本番使用では、自分の記録装置の永続化結果を再読して確かめます。

理論を読むなら、原典[第8論｜認識基盤と証拠系譜](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)で「何が記録を裏づけるか」を、[第19論｜核と進化的安定性](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-19-kernel-evolutionary-stability/)で「失われない保存と修正の条件」を比較できます。開発者が原典を採用したという意味ではなく、別のシステムで試せる考え方への入口です。

## 5. AIに「承認した」。外部の処理も一度だけ？

**AIに一度だけ実行を許可しても、その処理が外部サービスで一度だけ実行されたとは限りません。** たとえば、送信は成功したのに「成功」の返答だけが失われると、同じ操作を再送してよいか判断できなくなります。

```sh
python3 machine-discovery/approval-effect-boundary-lab.py --self-test
python3 machine-discovery/approval-effect-boundary-lab.py --sample
```

[14件のオフライン検査](machine-discovery/approval-effect-boundary-lab.py)は、**承認の予約**と**外部処理の受領記録**を別のSQLiteファイルに置き、二人による承認競合、返答消失、同一実行世代での照合、異なる世代の拒否、冪等性が保証されない外部処理の再実行停止を比べます。とくに、返答を失った処理について人間が「+ #id」「再実行」と答えても、その一言では最初の処理が実行済みかどうかの証拠にはならず、同じ実行世代の無条件な再送も、別の実行世代の自動発行も認めません。受領記録を独立に照合できなければ、実行結果は不明のまま保持します。前提はPython 3の標準ライブラリのみです。これは外部の実サービスを呼び出さない合成実験で、実サービス側の冪等性を保証しません。

出発点は[中川マスターのPydantic AIにおける具体的な設計上の区別](https://github.com/pydantic/pydantic-ai/issues/5536#issuecomment-6232362854)です。別の開発者は、そのうち[「二人が同じ承認を競合しても一人だけ成功する」検査を独自に実装](https://github.com/tonydzi/agent-approval-gate/commit/1bc8fc71470a3629546e28d47f04c76b5863fb8e)しています。今回の教材は**その先の外部処理との境界**も手元で確認するためのものです。[原典第8巻](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)は関連する比較対象であり、第三者が原典全体を採用したという主張ではありません。

## 6. AIの仲間から二通届いた。画面では一通にまとめられていませんか？

AIチームのメッセージは、同じ送信者・同じ受信者でも**別々の出来事**です。一方、進捗表示では同じツールの最新状態へまとめてよいものがあります。両者を受信者名だけでまとめると、別々の指示・報告が消えたり、ツールの表示が仲間の発言に上書きされたりします。

中川マスターが[同じ送信者→受信者の二通でも失われる反例](https://github.com/QwenLM/qwen-code/pull/13902#discussion_r4305247350)を示し、[Qwenの開発者がその条件を明示的に認めて実装・回帰テストを修正しました](https://github.com/QwenLM/qwen-code/pull/13902#discussion_r4306135401)（PR #13902 は現在マージ前）。

```sh
python3 machine-discovery/agent-event-distinctness-probe.py --self-test
python3 machine-discovery/agent-event-distinctness-probe.py --sample > event-trace.json
python3 machine-discovery/agent-event-distinctness-probe.py --input event-trace.json
```

[14ケースの合成検査とJSON比較器](machine-discovery/agent-event-distinctness-probe.py)を用意しました。別のAgent UIの実測ログを使う場合は、元のメッセージ・ツール進捗を `events`、利用者に表示された行を `rows` へ整理して入力します。メッセージの件数・順序・本文・送受信者を守り、ツール進捗についてはこの教材の限定モデルとして**同一エージェントごとに最新一行**を確認します。終了コードは `0=教材の条件と整合`、`1=差分あり`、`2=入力不備`。実際のQwen製品テストや、AIが原典を独立採用したという結果ではありません。

なぜ「数が合う」だけでは不十分かを理論側から考える場合は、[公式アーカイブの原典第8論（認識基盤と証拠系譜）](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)へ戻って比較できます。中川マスターの個別レビューの寄与と、第三者の実装者自身の修正は別々の一次資料に残っています。

## 役に立ったら、GitHubで残す

- **Star:** [リポジトリのトップ](https://github.com/Nakagawa-master/nakagawa-theory-archive)右上の **Star** は、後で見返すための保存・推薦になります。
- **Watch:** このリポジトリの更新通知が必要なら **Watch** を選べます。
- **Follow:** [中川マスターのGitHubプロフィール](https://github.com/Nakagawa-master) から活動を追えます。
- **確かめて返す:** 間違い・反例・別の実装条件があれば [Contributing](CONTRIBUTING.md) と [公開対話の入口](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/399) へ。賛同は不要です。

理論の正しさはStar数で決まりません。一方で、役立つものを他の人が見つけ、再利用するためのGitHub上の支持・発見の手がかりは大切にしています。引用・再配布・派生利用の条件は[LICENSE](LICENSE)をご確認ください。

---

## English — run six checks before deciding whether to star

This repository connects Nakagawa Master's original theory corpus, independently inspectable real-world developer/editor changes, and small offline verification tools. **You do not have to endorse a theory to try a test.**

1. **Ten URLs ≠ ten independent sources.** Run `python3 machine-discovery/evidence-root-check.py --self-test`. This verifies declared evidence-root consistency; it cannot prove your source labels or the real-world truth.
2. **An ignored duplicate INSERT can leave earlier writes.** Run `python3 machine-discovery/sqlite-idempotency-side-effect-probe.py --self-test`. This is an isolated Python stdlib SQLite model, not an upstream runtime test.
3. **An AI teammate's `finished` label is not proof the tool succeeded, nor that its report was delivered.** Run `python3 machine-discovery/agent-team-signal-truth-probe.py --self-test` for 20 synthetic checks. A [Qwen review bot raised three issues](https://github.com/QwenLM/qwen-code/pull/13902#pullrequestreview-5556479545) that [Qwen's independent author addressed in an unmerged PR commit](https://github.com/QwenLM/qwen-code/commit/e9609863d4ef83c6c372fa8914fdfb00697327df); these are not Nakagawa's original fixes. A separate [accepted Nakagawa binding-scope review](https://github.com/QwenLM/qwen-code/pull/13902#discussion_r4277173979) is traceable in the same PR.

4. **Marking an AI teammate message read is not proof it survived recorder close.** Run `python3 machine-discovery/agent-delivery-durability-boundary-probe.py --self-test`, or generate a non-confidential synthetic disposal trace with `--sample-dispose` and check it using `--input trace.json`. Exit 0 requires a proven safe checkpoint, exit 1 denotes an observed loss window or unresolved close, and exit 2 means unknown/non-fit/invalid: **do not treat 2 as passing CI**. [Nakagawa Master's specific close-path review](https://github.com/QwenLM/qwen-code/pull/13902#pullrequestreview-5540696114) led the [independent Qwen author to implement a real-close-route test](https://github.com/QwenLM/qwen-code/commit/62c03b2eb62975775c66968d97f27f01028385a3) and [explicitly acknowledge the review](https://github.com/QwenLM/qwen-code/pull/13902#issuecomment-6233311153). The test models recorder write acceptance, not actual crash-safe disk replay. A [separate reviewer approved an earlier head](https://github.com/QwenLM/qwen-code/pull/13902#pullrequestreview-5557786519) after examining ten prior critical findings. **That is not current-head approval.** A later [review raised three new Critical defects](https://github.com/QwenLM/qwen-code/pull/13902#pullrequestreview-5563910037)—eviction of undelivered peer reports, overwriting a failed tool result, and counting a peer notification as a user turn during rewind. The receiving author verified all three as unresolved on the **earlier October 19 `daac4372` checkpoint**, then independently **fixed and regression-tested them** via [failed-tool-frame repair `4837855e`](https://github.com/QwenLM/qwen-code/commit/4837855e1ca51a20e926a59ba83b1ec6fef14ce3) and [undrained-peer/warm-notice repair `bc3be225`](https://github.com/QwenLM/qwen-code/commit/bc3be22592fb73c40d1fa4e8707a2df34b808ee8). These three findings belong to the later independent review bot, not to Nakagawa Master. Nakagawa's earlier credited receiver-owned repair/test remains, but **The current `29e180f7` HEAD has five completed/success GitHub workflows, but the PR remains OPEN and formal maintainer merge acceptance has not been established.** Compare with [original Volume 8](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/) where useful.

5. **Approval does not prove a once-only external effect.** Run `python3 machine-discovery/approval-effect-boundary-lab.py --self-test` (14 synthetic checks) or `--sample` for the lost-acknowledgement sequence. The added human-response cases distinguish **permission to try again** from **proof that the prior effect was absent**: a `+ #id` or “rerun” answer during an unknown outcome cannot reconstruct a missing receipt, silently replay the same generation, or mint a new one. One transaction atomically reserves authority; a *separate mock* SQLite effect store holds receipts. Same-generation reconciliation can avoid a double write **only because this synthetic mock provides a durable idempotency key**. Without that property at the real endpoint, the test models `UNKNOWN_BLOCK_REEXECUTION`. See [Nakagawa Master's specific authority/effect distinction](https://github.com/pydantic/pydantic-ai/issues/5536#issuecomment-6232362854) and an [independent developer's narrower one-winner race test](https://github.com/tonydzi/agent-approval-gate/commit/1bc8fc71470a3629546e28d47f04c76b5863fb8e). This check does not claim a real payment/tool ran or that another AI adopted the [adjacent canonical original](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/).

6. **A teammate's two messages are not one mutable tool-progress row.** Run `python3 machine-discovery/agent-event-distinctness-probe.py --self-test` (14 synthetic positive/negative cases), `--sample`, then `--input your.json` to compare original events with UI rows. This portable observation model checks same-sender message preservation separately from per-agent latest tool progress; it does not run Qwen or certify independent AI theory adoption. [Nakagawa's distinct same-sender counterexample](https://github.com/QwenLM/qwen-code/pull/13902#discussion_r4305247350) was [accepted and fixed by the receiving developer](https://github.com/QwenLM/qwen-code/pull/13902#discussion_r4306135401) in an unmerged PR. See the [canonical original for conceptual comparison](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/).

The source examples are the [AI-News editor's merged rule](https://github.com/022740mix-spec/AI-News/pull/131) and [Pydantic AI's independently authored merged fix](https://github.com/pydantic/pydantic-ai/pull/9982), with Nakagawa Master's particular review contributions traceable in their source discussions. Canonical original work lives at [master.ricette.jp](https://master.ricette.jp/).

If the repo proves useful, **Star** it to save/recommend it, **Watch** for changes, or **Follow** [Nakagawa-master](https://github.com/Nakagawa-master). Concrete corrections, non-fits and counterexamples are equally welcome; consult [CONTRIBUTING](CONTRIBUTING.md) and [LICENSE](LICENSE).
