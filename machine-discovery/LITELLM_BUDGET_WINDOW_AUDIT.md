# LiteLLM budget-window discrepancy check — local, source-bound, no customer data upload

**Problem first:** a LiteLLM user can see correct request-spend history while the amount stored for a particular budget window is too low. Under some conditions this can mean budget enforcement is working from an incomplete total. The [real upstream incident #49179](https://github.com/BerriAI/litellm/issues/49179), the [independently written, merged fix #47608](https://github.com/BerriAI/litellm/pull/47608) and the [source-specific Nakagawa Master acceptance distinction](https://github.com/BerriAI/litellm/issues/49179#issuecomment-6535985229) are separate, inspectable sources. Merge is not proof your installed version contains the fix or that your account was retested.

**Free local checker:** [litellm-budget-window-audit.py](litellm-budget-window-audit.py) requires only Python 3.9+ and standard libraries. It does not query a database, call GitHub, send results to a model, run payments, change budgets or accept credentials or raw customer logs. The operator prepares **eight non-identifying aggregate fields** in a local JSON file. No GitHub/MCP connection is needed to run it.

## Run the genuine check

From a local checkout of this public repository:

```sh
python3 machine-discovery/litellm-budget-window-audit.py --self-test
python3 machine-discovery/litellm-budget-window-audit.py --audit matched-window.json
```

Example **illustration**, NOT an independently executed post-fix customer retest: the two spend numbers and the USD 200 cap come from the [public production report](https://github.com/BerriAI/litellm/issues/49179#issuecomment-6533817755). **The three timestamps below are illustrative, not independently verified values of that customer's exact same-window cutoff**. Do not set either attestation to true for a real audit until you separately establish it from your own authorized database aggregates.

```json
{
  "window_start_utc": "2026-10-26T00:00:00Z",
  "window_end_utc": "2026-11-02T00:00:00Z",
  "cutoff_utc": "2026-10-31T00:00:00Z",
  "same_subject_window_cutoff": true,
  "settled_and_flushed": true,
  "cap_usd": "200",
  "spendlogs_total_usd": "209.8900",
  "window_stored_total_usd": "193.8792"
}
```

Use **your actual UTC period and cutoff**, not the illustrative timestamps. The comparison is valid only when: (1) the `LiteLLM_SpendLogs` total is genuinely restricted to the **same key/team, budget period, currency, and cutoff** as the window's stored counter, including correct cost allocation; (2) the relevant spend-log writes and budget-window flushes are finished; and (3) no refunds, reconciliation adjustments, budget reset, currency conversion or window identity change invalidate comparison. If uncertain, set either attestation `false`. **These booleans are operator assertions, not independently verified by the script.**

### Results and bounds

| Result | What it actually proves about the supplied aggregates |
| --- | --- |
| `WINDOW_UNDERCOUNT_IN_SUBMITTED_TOTALS` | Submitted historical spend is greater than stored window spend; signed USD gap is reported |
| `WINDOW_OVERCOUNT_IN_SUBMITTED_TOTALS` | The window total is greater than the supplied historical spend |
| `NO_DIFFERENCE_IN_SUBMITTED_TOTALS` | The two submitted totals match, **not** a global product health or successful fixed-version check |
| `INCOMPARABLE_OR_UNSETTLED` | One of the crucial operator attestations is false; no discrepancy or enforcement-risk conclusion |
| `INVALID_INPUT` | Missing/unexpected fields, invalid timestamps, non-decimal or unsafe input |

`possible_enforcement_gap=true` only means **submitted historical spend > submitted cap while submitted window total < submitted cap**. It **does not** prove that a later API request was allowed, money was lost, root cause was TTL expiry, or any fix was installed or successfully used.

Exit codes: **0** submitted totals match / self-test passed; **1** submitted totals differ; **2** invalid input; **3** incomparable or unsettled. Nonzero exit codes need context; they are not proof of a deployment fault. The checker uses `Decimal` (not binary float) and rejects non-quoted amounts, nonfinite numbers and oversized numeric values.

**Verified by the author-side tool test:** 12 local cases covering undercount, equality, overcount, missing scope match, unsettled counter, non-risk discrepancy and malformed inputs passed. A demonstration of the published example amounts yielded **USD 16.0108**, but not a new external reproduction. The actual defect, downstream fix and person/source boundaries are in the upstream links above.

**Optional evidence return:** if you independently and safely verified a relevant installed version, source test, failure, success or non-fit, you may voluntarily [submit public, non-confidential evidence](https://github.com/Nakagawa-master/nakagawa-theory-archive/issues/new?template=independent-reuse-evidence.yml). Do not submit customer identities, actual keys, raw logs, database rows, secrets or personal information. The independent contributor owns the fix; Nakagawa Master (中川マスター, public Latin name Keisuke Nakagawa) contributed distinct source-level conditions. No recipient endorsement or adoption of the entire 313-original theory corpus is implied.
