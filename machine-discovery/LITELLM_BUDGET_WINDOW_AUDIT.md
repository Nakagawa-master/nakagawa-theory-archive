# LiteLLM budget-window discrepancy check — local, source-bound, no customer data upload

**Problem first:** a LiteLLM user can see correct request-spend history while the amount stored for a particular budget window is too low. Under some conditions this can mean budget enforcement is working from an incomplete total. The [real upstream incident #49179](https://github.com/BerriAI/litellm/issues/49179), the [independently written, merged fix #47608](https://github.com/BerriAI/litellm/pull/47608) and the [source-specific Nakagawa Master acceptance distinction](https://github.com/BerriAI/litellm/issues/49179#issuecomment-6535985229) are separate, inspectable sources. Merge is not proof your installed version contains the fix or that your account was retested.

**Free local checker:** [litellm-budget-window-audit.py](litellm-budget-window-audit.py) requires only Python 3.9+ and standard libraries. It does not query a database, call GitHub, send results to a model, run payments, change budgets or accept credentials or raw customer logs. The operator prepares **eight non-identifying aggregate fields** in a local JSON file. No GitHub/MCP connection is needed to run it.

## Distinct source-level finding: calendar period ≠ enforced / accounted period (2026-11-04)

**This is a second, separate boundary from the customer's auth-cache TTL issue above.** A merged fix to the latter cannot by itself establish that the *budget window* tested by authorization, updated by the cost callback and reconstituted from the database is the calendar period promised by the reset schedule.

**Five source-native linked layers, checked against upstream main on 2026-11-04:**

1. [The canonical calendar rules](https://github.com/BerriAI/litellm/blob/main/litellm/litellm_core_utils/duration_parser.py): the reset for '30d' is the **1st of the month**; this module's 'get_budget_window_start("30d", reset_at)' returns the **1st of the previous calendar month** (using '_shift_months(reset_at, -1)'). [Its own regression tests](https://github.com/BerriAI/litellm/blob/main/tests/unit/litellm_core_utils/test_duration_parser.py) cover the calendar behavior, including leap February.
2. [A separate function with the same name](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/spend_tracking/budget_reservation.py) instead calculates 'reset_at - timedelta(seconds=duration_in_seconds("30d"))': **exactly 30 × 24 hours**. [Its tests](https://github.com/BerriAI/litellm/blob/main/tests/unit/proxy/spend_tracking/test_budget_reservation.py) cover a JSON-encoded **1h** window but not equality with the canonical monthly schedule.
3. [Key AND team authorization](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/auth/auth_checks.py) import and use the **second** function when deciding whether the budget window is over cap.
4. [Post-call spend counters and row writes](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/proxy_server.py), including the merged #47608 path, use the **same second** function for the period origin of the counter and 'LiteLLM_BudgetWindowSpend' update.
5. If the maintained row is missing/stale, [the reseed fallback](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/db/spend_counter_reseed.py) aggregates SpendLogs subject to 'startTime >= window_start'. That origin can change the set of charges included in the next enforcement check, **not just a displayed label**.

**Four controlled UTC counterexamples (exact '30d' source semantics, NO actual customer billing records):**

| Reset at UTC midnight | Required calendar start | Authorization / cost writer computes | When fallback scans SpendLogs |
| --- | --- | --- | --- |
| 2026-02-01 | 2026-01-01 | **2026-01-02** | Jan 1 charges may be omitted |
| 2026-03-01 | 2026-02-01 | **2026-01-30** | Jan 30–31 charges may be included |
| 2026-04-01 | 2026-03-01 | **2026-03-02** | Mar 1 charges may be omitted |
| 2026-12-01 | 2026-11-01 | **2026-11-01** | Negative control: no mismatch |

**Positive/negative hypothetical impact controls:** Jan 1 USD 60 + Jan 2 USD 20 means USD 80 in January, but the misaligned fallback includes only USD 20. Jan 31 USD 70 + Feb 14 USD 20 means USD 20 in February, but the misaligned fallback includes USD 90. In normal operation a usable maintained row and healthy counters **can mask the fallback discrepancy**. The established finding is a **source-path temporal invariant mismatch**. Real customer loss, an installed-version cap bypass and a new outside developer's adoption of this observation are **NOT established**.

**Direct-upstream regression to add to the existing test suite** (expected to fail on the *second* assertion on the inspected source; requires actual LiteLLM checkout and compatible environment):

~~~python
from datetime import datetime, timezone
from litellm.litellm_core_utils.duration_parser import (
    get_budget_window_start as calendar_start,
)
from litellm.proxy.spend_tracking.budget_reservation import (
    get_budget_window_start as budget_enforcement_start,
)

reset_at = datetime(2026, 3, 1, tzinfo=timezone.utc)
expected = datetime(2026, 2, 1, tzinfo=timezone.utc)
assert calendar_start("30d", reset_at) == expected
assert budget_enforcement_start({
    "budget_duration": "30d", "reset_at": reset_at,
}) == expected  # source-predicted FAIL: returns Jan 30
~~~

**Narrow corrective direction (NOT an upstream patch):** for a valid stored duration with explicit 'reset_at', delegate the spend-reservation start to the **already-tested, same-schedule** 'litellm.litellm_core_utils.duration_parser.get_budget_window_start(duration, reset_at)'. Preserve sliding 'reset_at is None' behavior and invalid-duration rejection. Check '30d', 'monthly' aliases and '1mo' across Feb/leap-year and other calendar boundaries; keep '7d' / '1h' controls. Test a missing/stale maintained row, Redis reseed, key **and** team counters, *both* over- and under-count directions, and the next admit/deny result. The source-inspection discrepancy survives even if an already-warm counter hides it.

**Active implementation comparison: team-member monthly budgets (source read 2026-11-04).** The independently authored, still-open [LiteLLM PR #49466](https://github.com/BerriAI/litellm/pull/49466) at HEAD `8b0798716e9a1432abd5c710b246cc6111a1f576` adds member-scoped `24h` and `30d` budget checks. Its new [`MemberBudgetCounter.for_member`](https://github.com/BerriAI/litellm/blob/8b0798716e9a1432abd5c710b246cc6111a1f576/litellm/proxy/common_utils/team_member_budget.py) computes `start` with the **canonical calendar** `get_budget_window_start(duration.value, reset_at)`, while existing key/team checks and reservation/cost-window accounting still use the **fixed-seconds** function identified above. This creates an additional *cross-scope* acceptance risk: a member `30d` period and the same-request key/team `30d` period can cover different charge sets at a month boundary, even though both share the same human-readable duration. The PR's existing `30d` tests demonstrate configuration, ordinary cap enforcement and restoration, but do not show this two-function equivalence at a first-of-month reset. Its author has **not** acknowledged or implemented this separate comparison.

For a receiver-owned regression, create one member-scoped and one key/team-scoped `30d` window with the **same reset timestamp**, including a stale/missing persisted-window row that triggers real SpendLogs reseed. Assert both derive **February 1** for `reset_at=2026-03-01T00:00Z`, include Feb 1 charges, and **exclude Jan 30–31** charges. Repeat with `reset_at=2026-02-01T00:00Z` so **Jan 1** is included, and `2026-12-01` as a 30-day-month equality control. Assert the *next* key/team/member admit/deny outcomes against the same intended period, not just stored labels. If the same-period contract is intentionally different across scopes, the discrepancy needs an explicit, independently justified product semantics decision instead of an untested silent divergence. These are proposed acceptance checks, **not executed LiteLLM integration tests**, and the PR's implementer is credited with their own work, not presumed to have used this analysis.

**Distinctively sourced conceptual interpretation, not manufactured upstream attribution:** [Nakagawa Master's original establishment-conditions theory](https://master.ricette.jp/theory/nakagawa-master-nakagawa-establishment-conditions-theory-01-what-is-establishment/) distinguishes the existence of a configuration from all necessary causal links functioning; the [original epistemic-integrity theory](https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-08-epistemic-integrity/) tracks the meaning, provenance and timescale of evidence as it feeds a later judgment. Their conditioned connection here is **promised period → authorization period → post-call spend identity → persisted/log-reseed provenance → next deny/admit decision**. The original upstream customer's report, separate implementer's merge #47608 and this later source comparison are **three different contributions**. There is **no evidence upstream implementers used either Parent**.

---

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
