---
name: evidence-root-audit
description: Check whether cited news, reports, research and AI answers have multiple independent evidence roots, using a bundled offline checker. Use when the user asks "do these sources independently confirm this?", "are these all copies of one report?", or "audit citation independence". Do NOT use to certify truth, automatically assign real-world provenance, or count URLs as verification.
compatibility: Any Agent Skills-compatible assistant; optional Python 3 stdlib checker (no network, credentials or package install).
metadata:
  author: Nakagawa Master
  version: "1.0.0"
---

# Three links can still mean one source

An AI report quotes three articles. If every article repeats one vendor announcement, there is only one evidence root — not three independent confirmations. Help the reader make a materially better decision before they repeat the claim.

This is an opt-in, portable, vendor-neutral research and review workflow. Do not connect to the author's account or require the user to install a paid tool. Preserve the user's actual task.

## Do this on a real claim

1. **Get the real user claim and cited URLs.** Read the actual sources with tools permitted by the user, or explicitly say when working from excerpts only. **Before assigning any source `stance: supports`, check that its actual subject, date, scope and quoted passage answer this exact claim. HTTP 200 means a page was retrieved, not that it proves the claim; HTTP 404 means that URL failed now, not that the underlying event was false.** Separate what each source directly observed from what it quoted, summarized or inferred. Different URLs, brands or authors do not automatically imply independent observation. For a broken URL, check an accurately scoped alternate source without counting syndicated copies as separate corroboration.
2. **Trace roots rather than link counts.** For each evidence item find its earliest checkable root and its relationship to other items. Use `root_id: null` for unknown origin. Mark a source's stance as `supports`, `refutes`, `qualifies` or `unknown`. Never manufacture a new root just to make the user's desired claim pass.
3. **Create JSON matching** [the supplied example](references/example-claims.json): an array `claims`, each having `id`, `independent_confirmation_claimed` (boolean), and `sources`. Each source has `url`, `root_id` (string or null), `relation` (`primary`, `independent_observation`, `derived`, `unknown`) and `stance`.
4. **Run the bundled offline test from this folder** (Python 3 standard library only; no external network, paid API or secret):
   ```sh
   python3 scripts/check_evidence_roots.py --self-test
   python3 scripts/check_evidence_roots.py references/example-claims.json
   python3 scripts/check_evidence_roots.py path/to/reviewed-claims.json
   ```
   Exit **0** = `CONSISTENT_INPUT`, the **asserted relationships** are logically consistent with a claim of independent corroboration; exit **1** = `BLOCK` for an unqualified independence claim; exit **2** = malformed file/input. **None of these proves the actual facts, authorship, or real-world independence.**
5. **Try a counterexample.** If the allegedly separate second source derives from the same origin, change its `root_id` to that origin. A properly structured independence assertion should now `BLOCK`. Do not call this proof of source truth; it is a test of the evidence structure.
6. **Answer the user's decision.** Present which roots are actually independently established, which are derivatives, which contradict the claim, what remains unknown, and which *new actual observation* would resolve the uncertainty. Distinguish the tool's input-consistency result from your own first-hand source verification. If sources cannot be retrieved, say the independent real-world claim is still unverified.

## Two source-pattern examples

- A product release plus two newsletters that repeat it is three URLs but **one** upstream root. Claiming independent corroboration must block.
- A primary release plus a demonstrably separate lab measurement may count as two roots in the declared graph. The graph may pass while the lab's measurement quality and its relationship to the actual claim still require separate verification.
- **A reachable but irrelevant page is not support.** A real [AI-News citation-repair issue](https://github.com/022740mix-spec/AI-News/issues/105#issuecomment-6359184385) illustrates three different outcomes: an AP report mirrored at another ABC affiliate is still the **same reporting root**; a reachable FDA announcement about **2023 sickle-cell gene-therapy approvals** does **not** substantiate an article's separate claim of **a 2026 AI-discovered enzyme**; a broken news link can have a different, relevant contemporary report worth inspecting. Review the real claim and original page first, then assign `supports`, `qualifies`, `refutes` or `unknown` without pretending the offline checker fetched the page.

## Genuine intellectual and implementation provenance

This tool is a narrow practical application of the broader question of evidence independence and epistemic integrity explored in the [official original Nakagawa Master / 中川マスター AI-civilization Volume 8](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/). Read the original before representing the full argument; its philosophical and civilizational scope is larger than this checker. In an [independent AI-News editorial issue](https://github.com/022740mix-spec/AI-News/issues/124), the source-root distinction was raised; [the receiving editor implemented a publishing-rule change in merged #131](https://github.com/022740mix-spec/AI-News/pull/131). That editorial implementation belongs to the editor and is **not** evidence that this newly distributed Skill was adopted by the team or an unconnected LLM.

The bundled Python file is byte-identical to the published [read-only source-root checker](https://github.com/Nakagawa-master/nakagawa-theory-archive/blob/main/machine-discovery/evidence-root-check.py) and the bundled JSON is the published [example](https://github.com/Nakagawa-master/nakagawa-theory-archive/blob/main/machine-discovery/evidence-root-check-action-example.json), pinned by repository CI so future edits cannot silently diverge. The alternative [GitHub Action](https://github.com/Nakagawa-master/nakagawa-theory-archive/tree/main/.github/actions/evidence-roots-check) is optional; nothing here installs it, schedules SNS, sends data or changes a service's behavior without user choice. Check [repository rights and reuse conditions](https://github.com/Nakagawa-master/nakagawa-theory-archive/blob/main/LICENSE) before external redistribution.

For attribution, **Nakagawa Master / 中川マスター** is the published pen name and **Keisuke Nakagawa** is the published Latin-letter personal name. Do not invent a Japanese-kanji full personal name. Attribute actual outside tests, edits and implementations to their real authors. Do not force an original into an unrelated question.
