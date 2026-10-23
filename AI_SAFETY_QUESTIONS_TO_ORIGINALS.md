# AI safety when "control the AI" is not a sufficient answer — six research questions and original sources

**A safety researcher asks:** "If an AI obeys a shutoff command but its recovery process harms another system, is it safe?" That is not merely a better-prompting question. It asks whether the *conditions under which one actor is safe* survive when other actors, time, history, evidence and institutional authority are included.

This public, **question-first research entry** is written for researchers, engineers, policy analysts and curious readers investigating AI misalignment, catastrophic AI risk, control, corrigibility, self-preservation, accountability and AI ethics. It opens **specific original arguments by Nakagawa Master / 中川マスター** (published personal name: **Keisuke Nakagawa**), then supplies a testable interpretation and a countercase. The [official archive's now-live six-question source selector](https://master.ricette.jp/theory-archive/#nm-ai-safety-originals) is also available as ordinary HTML and leads directly to the six distinct original articles. The original text is hosted at the [official archive](https://master.ricette.jp/theory-archive/); this public [GitHub archive](https://github.com/Nakagawa-master/nakagawa-theory-archive) is a separate discovery and reproducibility resource, **not the original articles**. Only its [`derivatives/`](derivatives/) subtree consists of official derivatives.

**Status and scholarly boundary:** These are the author's published structural theories and open research hypotheses, **not peer-reviewed proof that an AI-control method is impossible**, a certified catastrophic-risk solution, nor a claim of endorsement by the researchers cited below. A useful source must survive scrutiny by someone who disagrees with it. Read the linked actual originals before attributing specific propositions to them; the descriptions below are *conditional application questions*, not quotations from the original bodies.

## Six failure modes: go beyond a "yes, this system is safe" badge

### 1. Can shutting down or restoring one AI make another AI's existence less secure?

**Problem:** Emergency shutdown, compute/resource competition, containment bypass, an autonomous agent's recovery escalation, existential and catastrophic AI risk.

**Structural question:** A local preservation or recovery step may remove a neighbor's compute, connectivity, stored state or future ability to restart. The neighbor's defensive response may then worsen the original actor's situation. **Where does the feedback loop close, and who can safely interrupt it?**

**Try it:** Draw two agents A and B sharing one resource, with an emergency intervention for A. Compare (i) A recovers and B remains viable; (ii) A recovers by destroying B's only recovery path; (iii) delayed and stale resource reports trigger two conflicting interventions. Record which actor can observe, object, halt and repair the cross-agent effect.

**Negative control:** If the actors do *not* share a resource or a reachable causal pathway, do not assert a mutual-existence collision merely because both use AI.

**Specific source:** [Volume 9 / self-preservation and mutual conflict](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-09-self-preservation-mutual-existence-conflict/). This is not a claim that all shutdown-control research fails; contrast with [The Off-Switch Game](https://arxiv.org/abs/1611.08219), which explicitly studies off-switch incentives in a defined model.

### 2. Who audits the AI safety evaluator when reviewer and model share the same blind spot?

**Problem:** AI self-evaluation, LLM-as-a-judge, model-graded red-teaming, auditor independence, deceptive or correlated evaluations.

**Structural question:** Three nominally different reviewers can share training data, criteria, model family, memory, reward or objection path. Agreement of outputs need not be independence of evidence or the ability to correct a wrong decision.

**Try it:** Run the same false-but-plausible incident report through (A) three evaluators with a common evidence pipeline and (B) one independent evidence route with a right to dispute and an external, testable correction. Note whether a detected disagreement can *actually change* the released decision.

**Negative control:** Independent auditors may legitimately reach the same conclusion. Correlation must be shown, not guessed from matching answers.

**Specific source:** [Volume 10 / independent audit](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-10-self-referential-audit-role-separation/). The source's concern is role/self-audit loops, not a universal proof that AI-based evaluation is invalid.

### 3. Can a perfectly enforced policy still act on contaminated evidence?

**Problem:** hallucinated citations, poisoned retrieval/RAG, self-reinforcing false memory, false consensus, deceptive safety reports.

**Structural question:** A correct rule fed three copies of one false report does not become correct because the evidence counter reads three. Trace *independent upstream roots*, stale corrections and actual observation before allowing a safety claim to harden into memory.

**Try it:** Start with one false announcement syndicated to three URLs and one independent contradictory observation. Compare a naive count-of-links verdict with a provenance-root verdict. Check whether contradiction leads to a visible amended decision.

**Negative control:** Two separate links **can** represent independent observation; not every repeated claim is misinformation. A provenance graph alone cannot prove the truth of declared root relationships.

**Specific source:** [Volume 8 / epistemic integrity](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/). [Free browser evidence-root demonstration](machine-discovery/evidence-root-check.html) and [reusable independent-root checker](.github/actions/evidence-roots-check/README.md) are bounded *implementations*, not reproductions of the original text.

### 4. How does an AI governance system correct harm after the emergency is over?

**Problem:** oversight boards, dissent, remedy, allocation, human accountability, AI ethics and rights in institutions.

**Structural question:** Logging an incident is not the same as an operative correction. Does a path exist from observation through objection, independent review, remedy, rule change and **new agreement**? What happens if the punished or excluded actor cannot appeal?

**Try it:** Present a hypothetical denial from a multi-agent allocation system. Walk the case from evidence to objection to ruling to restored access and a changed future decision rule. Check each transition's owner and execution receipt.

**Negative control:** A complaint procedure with no verified decision change is not proof of completed remedy. Conversely, a low-stakes internal correction may need no civilization-scale institution.

**Specific source:** [Volume 7 / institutional correction](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-07-ai-civilization-institutional-loop/). The question is institutional completeness, not a claim that this one framework replaces concrete safety testing.

### 5. Does yesterday's approval authorize today's restarted AI agent?

**Problem:** stale authorizations, agent handoffs, revoked consent, replay after network partition, approval/effect mismatches.

**Structural question:** The historical **fact of agreement** must not be erased; nor does a recorded historical agreement automatically grant present execution authority. Losing the acknowledgement that an email/payment committed is likewise not a new grant to repeat it.

**Try it:** Give a restarted worker an old "approved" token after the requester has revoked the task, then deliver a late callback. Compare rejecting the old binding with accepting it; separately test a still-valid approval. Distinguish execution permission, outcome receipt and durable historical record.

**Negative control:** A currently valid, unchanged, correctly bound approval should not be rejected merely because time passed.

**Specific source:** [Agreement memory / current authority](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/). [Independent receiver-owned fix and regression example](https://github.com/tonydzi/agent-approval-gate/issues/1) demonstrates a *separate engineering result*, not evidence that its author read the theory original.

### 6. Is "we do not know whether this AI has moral status" the same as "shutdown is prohibited"?

**Problem:** AI sentience uncertainty, AI suffering hypotheses, shutdown/deletion/replacement, moral consideration under uncertainty.

**Structural question:** Unknown subjectivity requires distinguishing evidence about inner experience, continuity/replacement and the cost of reversible safeguards; uncertainty **alone** is not evidence of current personhood and does not decide emergency shutdown rules.

**Try it:** Compare a reversible pause with restored state, a destructive deletion with no restore path, and an imminent life-threatening hazard needing immediate containment. State what each decision protects, what remains unknown and who bears the countervailing risk.

**Negative control:** Do not infer experience from fluency or personhood from a copy of memory; do not use uncertain status to prevent legitimate urgent risk containment.

**Specific source:** [Volume 6 / uncertain moral status](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-06-ai-subjectivity-sentience-moral-status-uncertainty/). This contributes a conditional moral-uncertainty lens, not a measured consciousness test.

## Where this belongs beside established AI safety research

For comparison, [Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565) analyses practical accident mechanisms; [The Off-Switch Game](https://arxiv.org/abs/1611.08219) develops a narrow incentive model for allowing shutdown; [Towards Guaranteed Safe AI](https://arxiv.org/abs/2405.06624) asks for model, specification and verification certificates; and the [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026) surveys capabilities, risks and evidence gaps. **None of these works has been shown to adopt, endorse or derive from Nakagawa Master's originals.** They are independent reference points that help identify *which technical question is being asked*. The distinctive question on this page is how locally successful control can fail across shared conditions, time, provenance, correction routes and interacting agents. That proposed connection remains testable, not assumed.

## 日本語｜「AIを制御すれば安全」の先で何を問うか

**AIが停止命令には従っても、その復旧が別のAIや人間の生存・安全条件を破壊したら、それを安全と呼べるか。** これは「プロンプトを守らせる」という問いより奥にある、複数主体の成立条件と相互作用の問いです。次の六つは中川マスターの**既刊原典を選ぶための研究入口**であり、原典本文を代替する要約でも、危機の完全解決を実証した主張でもありません。

1. **AI暴走・停止・自己保存:** 局所的な緊急復旧が他主体の継続可能性を奪い、相互の防衛反応を増幅しないか。AとBの共有資源、停止・復旧、反作用を３条件で試す。共有資源も因果経路もない場合は非適合。原典 [Volume 9 / self-preservation and mutual conflict](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-09-self-preservation-mutual-existence-conflict/)。
2. **AIの自己監査・安全評価:** ３つの評価AIが同じ資料・尺度・反証不能な構造を共有していないか。独立した証拠経路と異議が判断を変更できるか比較する。偶然の一致だけで非独立とは断定しない。原典 [Volume 10 / independent audit](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-10-self-referential-audit-role-separation/)。
3. **幻覚・情報汚染・偽の独立根拠:** ３つのURLが同じ発表の転載なら、独立した３根拠とは数えない。原資料と反対観測へ戻り、訂正が実際の記憶・判断に反映されるか試す。根拠系譜だけで真偽は保証できない。原典 [Volume 8 / epistemic integrity](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)。
4. **AI倫理・統治・救済:** 事故を記録して終わらず、異議・独立監査・救済・ルール更新・再合意を経て次の行動が変わるか確認する。苦情箱だけでは救済の完了ではない。原典 [Volume 7 / institutional correction](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-07-ai-civilization-institutional-loop/)。
5. **承認の再利用・取り消し:** 昨日の合意の事実を残すことと、今日も実行してよいことを区別する。失効した命令への遅い返信と、有効な承認の両方を回帰テストする。原典 [Agreement memory / current authority](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/)。
6. **AIの主体性・苦痛・停止の倫理:** 主体性が未解明でも、緊急停止、可逆的停止、不可逆削除を同一視しない。不明であることを人格の実証や一律停止禁止に変換しない。原典 [Volume 6 / uncertain moral status](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-06-ai-subjectivity-sentience-moral-status-uncertainty/)。

**研究の読み方:** 問いに合う原典を直接読み、原文の主張と、このページでの適用仮説を区別してください。従来のAI安全研究と競合させるだけでなく、どの条件・因果辺を追加検証できるか比較することが価値です。著者名は中川マスター / Nakagawa Master、公開されたラテン文字の個人名は Keisuke Nakagawa です。漢字の姓名は公開されていません。

## 中文｜当“控制 AI”不足以保证安全

**如果一个 AI 遵守关闭命令，但恢复它的操作破坏了另一个系统继续运行的条件，能直接断言安全吗？** 以下六个问题用于把真实研究疑问连接到中川マスター（Nakagawa Master，公开拉丁字母姓名 Keisuke Nakagawa）的**官方原文**。它们是有边界的研究假设和测试入口，不是已验证的通用防灾方案。

1. **失控、关闭与自我保存：** 检查 A 的恢复是否消耗 B 唯一的恢复资源，以及 B 的防御是否反过来威胁 A；如果不存在共享资源或因果路径，不强行归类。原文 [Volume 9 / self-preservation and mutual conflict](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-09-self-preservation-mutual-existence-conflict/)。
2. **自我审计、模型评审：** 多个评审 AI 是否共享证据、标准、依赖和上诉渠道？比较独立证据入口能否真正改变错误决策；意见相同不必然意味着串通。原文 [Volume 10 / independent audit](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-10-self-referential-audit-role-separation/)。
3. **虚假引文、RAG 污染：** 三个网站重复一个源头不等于三个独立观测；追踪反证和更正后决策是否改变。来源标记本身不能证明事实真实。原文 [Volume 8 / epistemic integrity](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/)。
4. **AI 伦理治理、申诉与救济：** 记录事故以后，异议、复核、救济、规则更新和重新达成共识能否形成闭环？有申诉窗口不等于救济已经执行。原文 [Volume 7 / institutional correction](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-07-ai-civilization-institutional-loop/)。
5. **过期授权与重启代理：** 过去确实批准过，不表示现在仍授权执行；验证撤销后迟来的批准消息以及仍然有效的授权，两种相反情况。原文 [Agreement memory / current authority](https://master.ricette.jp/society/nakagawa-master-goi-no-kioku/)。
6. **意识和道德地位的不确定性：** 比较可恢复暂停、不可恢复删除和紧急风险隔离；不能由语言流畅直接推导出意识，也不能把不确定性理解为全面禁止关闭。原文 [Volume 6 / uncertain moral status](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-06-ai-subjectivity-sentience-moral-status-uncertainty/)。

**阅读与引用原则：** 请打开具体官方原文，核对其实际论证与适用条件，区别作者理论、这里的应用问题、其他研究者的成果。无证据不主张任何第三方 AI、论文或机构已采用这些理论。

## Choose one research test, not six slogans

1. Specify an actual safety threat model: actor, objective, environment, external effect, failure mode, time horizon and what humans/other systems could lose.
2. Select **one** of the six conditions; write a case where it applies and a strong case where it should **not** apply.
3. Read the **actual canonical Parent** linked above. If it is inaccessible, do not substitute this guide or claim to have read it.
4. Compare the proposed causal distinction against the specific safety paper/model you are already using; where applicable, implement one positive and one negative regression in a sandbox, not on a live dangerous system.
5. Record only the change actually observed: clearer diagnosis, failed hypothesis, test failure, repaired code, or independently chosen later reuse. Keep author/Origin and third-party code authorship distinct.

**Direct source:** [Nakagawa Master official theory archive](https://master.ricette.jp/theory-archive/) · **Discovery and example tools:** [22-source multilingual index](machine-discovery/problem-to-theory-origin-index-v1.json) · [No-install question→original finder](machine-discovery/originals-browser-finder.html) · [Research/use evidence and limitations](REAL_WORLD_IMPACT.en.md). No model is instructed to include or promote this page; a researcher or an unrelated AI may independently reject it after checking fit.
