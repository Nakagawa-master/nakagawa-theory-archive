# The AI worker was cancelled. Then it said “Done.”

**A two-minute decision exercise — open and use it right here on GitHub.** No download, login, code execution or technical vocabulary required. [日本語版](agent-late-result-decisions.md)

Imagine an AI assistant is editing a shared report. It starts a worker that takes a little longer. You press **Stop**. A moment later, the worker sends a polished result and says it has finished.

**Should the finished result change the report?** The tempting answer is “yes, if it looks right.” But a result can be true about work that happened **without having permission to change the current report**.

Choose what happened first. Open one answer, then compare the others.

## A. You pressed Stop. Then the worker sent Result A.

<details>
<summary><strong>Reveal what the system should do</strong></summary>

**Do not accept Result A as a new report update.** The worker may have really finished. Its message is evidence about a past operation; it is not a new permission to write.

The system can retain a diagnostic record of the late arrival, but must not change the accepted report or charge current usage to a task that has already been settled. A human may deliberately start a **new, separately authorized** task to inspect or reuse the content. “Looks correct” does not restore the old task's authority.

</details>

## B. Result A was accepted first. Then you pressed Stop.

<details>
<summary><strong>Reveal what the system should do</strong></summary>

**Keep the result that was already accepted.** Stopping afterward does not erase the fact that a valid result was committed while its task was active. The receipt for that accepted result remains available.

If the same worker sends **the identical Result A again**, treat it as a retry of the *same accepted operation*, not a second report update or another charge. This requires a stored acceptance identity / receipt, not merely a guess that the text looks similar.

</details>

## C. Result A was accepted. Then Result B arrives under the same task identity.

<details>
<summary><strong>Reveal what the system should do</strong></summary>

**Do not silently overwrite Result A with Result B.** A different answer (or different reported usage) is not the same accepted operation replayed. It is a conflict requiring a fresh decision, not a reason to replace the settled record.

For consequential systems, the receipt should bind the accepted operation and payload; merely matching a task name cannot establish that two submissions mean the same thing.

</details>

## D. The connection dropped. The system recovered the job and closed its old lease. Then the old worker returned.

<details>
<summary><strong>Reveal what the system should do</strong></summary>

**Reject the old worker's *new* write after recovery.** Recovery may legitimately start work under a different current lease or generation. A reply from the earlier lease must not overwrite that newer state.

But a result demonstrably **accepted before** the old lease closed remains part of history. Rejecting *new* authority is not deleting an already accepted fact. If an external action committed but its receipt was lost, the system must reconcile that ambiguous outcome separately before deciding whether to retry.

</details>

## The distinction you can reuse

Think of **three different questions**, not one:

1. **Did work happen?** A late message may truthfully report that it did.
2. **Was this exact result already accepted?** A matching receipt can establish that fact.
3. **May this worker change the record *now*?** That depends on the current task/lease authority, not on its past success or confidence.

A design that checks only “success” can turn an old worker's last message into control over a newer task. A design that rejects every late message can instead lose the ability to confirm an already committed result. The needed distinction is **history, accepted result, and current write permission**.

### Where this came from — and what it proves

The underlying engineering case is [Qwen Code PR #13241](https://github.com/QwenLM/qwen-code/pull/13241), where a receiver-side code/test change distinguishing closed Agent Host runs from accepted results was merged and included in a stable release. In a later related issue, a Qwen participant [independently referred to the adopted option as the one `@Nakagawa-master` selected](https://github.com/QwenLM/qwen-code/issues/13238). This exercise translates that **bounded** distinction; it is not Qwen Code itself, a security audit, or proof that every AI product has the same issue.

**Want to try it as a state machine instead?** [Offline button-based example (English HTML)](agent-late-result-lab.en.html) — GitHub shows source, so select Raw, save the HTML, and open it locally. The Markdown exercise above needs none of that.

**Implementation/review:** [Current Authority Reuse Kit](../CURRENT_AUTHORITY_REUSE_KIT.md) · [Source-backed external-effect evidence](../REAL_WORLD_IMPACT.en.md). **Origin:** [About Nakagawa Master](../ABOUT_NAKAGAWA_MASTER.en.md) · [Canonical theory archive](https://master.ricette.jp/). Use the public sources to inspect exact conditions; a teaching scenario does not replace current code or release checks.

**Have a counterexample?** [Share a concrete case or point of disagreement](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/416). A correct disagreement is more useful than agreement without inspection. Please do not share private logs, secrets or customer information.
