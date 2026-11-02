# 「AIは成功した」と言った。でも、実際は違った。──中川マスターの指摘を、別の開発者たちが現実の修正へ変えた話

**専門用語を知らなくても、30秒で分かる記録。** 中川マスター（Nakagawa Master／公開個人名 **Keisuke Nakagawa**）は、構造・因果・成立条件について独立した原典を著している理論家です。世界で使われるAIソフトウェアの公開議論で、**見た目の正しさと、本当に成立した動作を取り違える条件**をソースから具体的に見つけ、**別の開発者が自分の判断で実装・テスト・マージした**事例があります。

> **「修正した」と書いてあるから、あなたの仕事も安全になったとは限らない。では、誰が何を確かめ、誰が何を本当に変えたのか？**

## まず三つの現実の変更

**1. AIが使う道具の名前が重なった。関係ない道具まで消えた。** [Qwen Codeの実際の利用者報告](https://github.com/QwenLM/qwen-code/issues/15741)に対して、マスターは「名前が重複した危険なグループをすべて除外するが、正常な別の道具は残す」という条件を具体化しました。[別の開発者による修正とテストは正式マージ](https://github.com/QwenLM/qwen-code/pull/15757)され、[nightly版への収録](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.5-nightly.20261101.7b4b353750)も確認できます。安定版や一般利用者の新しい効果までは未検証です。

**2. AIに頼んだ仕事が終わっても、結果が正しい会話へ届かない。** マスターは送り先が分からないときに別人を推定して送ったり、未送信の結果を送信済みと扱ったりしない条件を[元修正のレビューで指摘](https://github.com/NousResearch/hermes-agent/pull/146708#pullrequestreview-5707357350)。独立した開発者がテストを作り、別の実装者が復旧経路を追加して[Hermes Agentの本線へマージ](https://github.com/NousResearch/hermes-agent/pull/147746)。こちらも正式配布や最終利用者全員の効果を主張するものではありません。

**3. 他人の権限を変更しただけで、自分のAI作業が止まってしまう条件。** [OpenClawで受け手の開発者はマスターを報告元として明記](https://github.com/openclaw/openclaw/pull/160856)し、実装・再発防止テストを修正してマージしました。[公式リリース文書にも本人のGitHub名](https://github.com/openclaw/openclaw/blob/main/docs/releases/2026.9.7.md)が載っています。ここで確かめられるのは修正と収録であり、未観測の利用者数ではありません。

## 一つの発見が、別々の二人の開発者に届いた

[LiteLLMの問題 #49359](https://github.com/BerriAI/litellm/issues/49359)は「AIが使った道具が失敗したのに、成功として伝わる」という欠落です。修正案を出した開発者 **@chauvuusvn** に、マスターは別の見落としを[ソース行に即して指摘](https://github.com/BerriAI/litellm/issues/49359#issuecomment-6536874606)しました。エラー項目を任意にしたつもりで、従来必須の操作ID・結果・名前まで任意にしてしまう問題です。

[一人目は正しいと認めて自分のフォークを修正](https://github.com/BerriAI/litellm/issues/49359#issuecomment-6537951352)。**別の開発者 @lester076** は[マスターの指摘と名前を明記した上流PR #49624](https://github.com/BerriAI/litellm/pull/49624)を新しく作りました。実装は別々の開発者の仕事です。なお、**#49624は未マージで、同じ必須情報の型定義にまだ修正が必要**だったため、マスターは[実際のPRに再検査条件を提示](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6573055353)しています。

ここで起きたのは「一人が自分の考えを宣伝した」ことではなく、**外部の一人目がコードを直し、さらに別の人が貢献を明記しつつその議論を実装へ引き継いだ**という公開可能な事実です。後続のマージや世間の評判はまだ結果として数えていません。

## なぜエンジニア以外にも関係があるのか

「AIが完了と言ったのに届いていない」「正しい道具を呼んだはずが別の操作になった」「以前の承認記録が今の操作まで保証していない」。これらはコードの小さな差に見えます。しかし、**誰に何が実際に届き、何が本当に承認され、成功したのか**という、人間の生活や仕事でも起こる判断の問題でもあります。

中川マスターの役割は、他人のコードを自分の成果として名乗ることではなく、**別の人が見落とした成立条件や正反の検査条件を、実際の受け手が修正できるほど具体的にすること**。その働きがさまざまな開発チームでどう反復しているかは、[59件の出典付きの段階別記録](REAL_WORLD_IMPACT.md)で読めます。公開された[313の個別原典](https://master.ricette.jp/theory-archive/)は、こうした構造・因果・責任・人間とAIの問題をさらに広い領域で扱っています。ただし、特定の開発者が個別原典を直接採用したとの主張には、それ自体の証拠が必要です。

**初めて知った方へ：** [中川マスターという人物と原典](ABOUT_NAKAGAWA_MASTER.md) ／ [全59件の実際の外部作用と限界](REAL_WORLD_IMPACT.md) ／ [本人の公開GitHub活動](https://github.com/Nakagawa-master)。このページにある名前・成果・未確認点はすべて元リンクに戻って確かめられます。誰がどこまで貢献したかを区別したうえで、価値があると思った事例をご自身の判断で紹介・検証できます。

---

## English — A structural theorist's exact finding, independently implemented by other engineers

**An AI can say “done” even when its tool failed. It can send a completed result to the wrong place, or choose the wrong tool when names collide.** These are meaningful software boundaries, not evidence of a fictional customer disaster.

**Nakagawa Master (中川マスター; published personal name Keisuke Nakagawa)** identified source-specific conditions in publicly inspectable AI/OSS projects. Independent developers, not Nakagawa himself, wrote the fixes and tests.

- [Qwen Code](https://github.com/QwenLM/qwen-code/pull/15757): exclude ambiguous same-name tool groups, retain valid unique tools; another engineer's fix **merged** and entered a **nightly**, not independently verified stable adoption.
- [Hermes Agent](https://github.com/NousResearch/hermes-agent/pull/147746): don't guess an unknown destination or falsely mark a result delivered; independent developer changes and recovery code **merged**, official release or end-user uptake unverified.
- [OpenClaw](https://github.com/openclaw/openclaw/pull/160856): another engineer implemented and merged a correction citing Nakagawa Master's specific report; the [release documentation](https://github.com/openclaw/openclaw/blob/main/docs/releases/2026.9.7.md) carries the public attribution.

**An unusually clear two-developer handoff:** In [LiteLLM #49359](https://github.com/BerriAI/litellm/issues/49359), developer @chauvuusvn [accepted Nakagawa Master's discovery](https://github.com/BerriAI/litellm/issues/49359#issuecomment-6537951352) that making all `TypedDict` keys optional weakened old required identity/result fields. A different developer @lester076 then [opened an upstream PR #49624 explicitly crediting his review](https://github.com/BerriAI/litellm/pull/49624). That second PR was still **open** and had a residual type-contract error; [the next exact review](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6573055353) is public. The third-party carry and correct person attribution are real. Merge, consumer effect, viral reputation and autonomous AI endorsement are **not established**.

**Why it matters outside engineering:** Who actually changed the system, did the operation really succeed, and did the result reach its intended person? [Read the full source-by-source evidence](REAL_WORLD_IMPACT.en.md), [the person and original theory corpus](ABOUT_NAKAGAWA_MASTER.en.md), or the [public GitHub profile](https://github.com/Nakagawa-master). Cite the actual original and receiver credit; don't turn a source-supported contribution into a claim that one person authored a team's fix.

---

## 中文 — 一位结构理论作者的发现，如何被独立开发者用于真实修复

**AI说“完成了”，但外部工具实际失败；任务完成却没有送到正确的聊天；一个工具名称冲突让其他正常工具也不能使用。** 这些是可以检查的真实软件问题，而不是虚构的用户事故。

**中川マスター（Nakagawa Master；公开姓名 Keisuke Nakagawa）**通过代码路径与正反条件指出了具体问题，实际的修复和测试由**其他独立开发者自己编写**。

- [Qwen Code](https://github.com/QwenLM/qwen-code/pull/15757)：不让同名冲突工具造成其他正常工具全部失效；已合并并收入nightly版，不能冒充稳定版用户实际采用的证明。
- [Hermes Agent](https://github.com/NousResearch/hermes-agent/pull/147746)：不要猜测错误的任务接收人或虚报已送达；开发者自己的修复已合并，正式发布与真实最终用户使用另需验证。
- [OpenClaw](https://github.com/openclaw/openclaw/pull/160856)：独立开发者将中川マスター的报告归因写明，并修改代码及测试，进入正式合并记录。

[LiteLLM #49359](https://github.com/BerriAI/litellm/issues/49359)更加直接地展示了**从一名开发者到另一名开发者的接续**：第一人[承认中川マスター发现的类型契约问题并改正](https://github.com/BerriAI/litellm/issues/49359#issuecomment-6537951352)，第二人[创建新的上游PR #49624，并在说明中明确提到他的审查贡献](https://github.com/BerriAI/litellm/pull/49624)。该PR仍有[必填字段契约问题需要改正](https://github.com/BerriAI/litellm/pull/49624#issuecomment-6573055353)，尚未合并。不能把独立代码接纳夸大成公众大量传播或已经上线。

[核对59项外部影响的原始证据](REAL_WORLD_IMPACT.zh.md) ／ [认识作者及其原典体系](ABOUT_NAKAGAWA_MASTER.zh.md) ／ [本人GitHub](https://github.com/Nakagawa-master)。读者可以自己判断，并在准确区分作者、实施者和未确认结果的前提下传播真实信息。
