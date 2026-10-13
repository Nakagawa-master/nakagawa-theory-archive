#!/usr/bin/env node
/**
 * Agent budget scope vs admission — a dependency-free, local exercise.
 *
 * Direct engineering source:
 *   https://github.com/BerriAI/litellm/issues/43190
 *   https://github.com/BerriAI/litellm/pull/43410
 *   Nakagawa Master's distinction: scope identity != budget admission.
 *
 * Original-theory lens, NOT a claim about the developer's historical inspiration:
 *   Nakagawa Master, Human-Descendant AI Civilization Theory, Volume 11 / OD304.
 *   https://master.ricette.jp/theory/nakagawa-master-human-descendant-ai-civilization-theory-11-compute-capability-resource-class-formation/
 *
 * This is an isolated teaching MODEL. It does not import or execute LiteLLM,
 * Redis, provider billing, its tests, or the deployed code. Never describe the
 * assertions below as an independent measurement of LiteLLM's production state.
 *
 * Run: node examples/litellm_agent_budget_scope_admission.mjs --self-test
 *      node examples/litellm_agent_budget_scope_admission.mjs --self-test --json
 */
import assert from "node:assert/strict";

function finiteNonnegative(x) {
  if (typeof x !== "number" || !Number.isFinite(x) || x < 0) {
    throw new RangeError("budget and cost must be finite nonnegative numbers");
  }
  return x;
}
function scopeKey(agentId, sessionId) {
  if (!agentId || !sessionId) throw new Error("agent and session identities are required");
  return JSON.stringify([agentId, sessionId]);
}

class RecordedSpendStopThreshold {
  constructor() { this.spend = new Map(); }
  current(agent, session) { return this.spend.get(scopeKey(agent, session)) ?? 0; }
  admits(agent, session, limit) {
    finiteNonnegative(limit);
    return this.current(agent, session) < limit;
  }
  settleSuccess(authenticatedAgent, session, cost) {
    finiteNonnegative(cost);
    const key = scopeKey(authenticatedAgent, session);
    this.spend.set(key, this.current(authenticatedAgent, session) + cost);
  }
}

class ReserveBeforeForward {
  constructor() { this.spent = new Map(); this.reserved = new Map(); }
  state(agent, session) {
    const key = scopeKey(agent, session);
    return { key, spent: this.spent.get(key) ?? 0, reserved: this.reserved.get(key) ?? 0 };
  }
  reserve(agent, session, limit, maximumCost) {
    finiteNonnegative(limit); finiteNonnegative(maximumCost);
    const state = this.state(agent, session);
    // The check + reservation is one model operation. Real distributed systems
    // would need to perform it atomically in shared storage.
    if (state.spent + state.reserved + maximumCost > limit) return false;
    this.reserved.set(state.key, state.reserved + maximumCost);
    return true;
  }
  settle(agent, session, reservedMaximum, actualCost, terminalKind) {
    finiteNonnegative(reservedMaximum); finiteNonnegative(actualCost);
    const state = this.state(agent, session);
    if (terminalKind !== "success" && terminalKind !== "failure") throw new Error("terminal kind");
    if (reservedMaximum > state.reserved + 1e-10) throw new Error("missing reservation");
    // Strict guarantees need the reservation to bound possible eventual cost.
    if (actualCost > reservedMaximum + 1e-10) throw new Error("actual cost exceeded reserved maximum");
    this.reserved.set(state.key, Math.max(0, state.reserved - reservedMaximum));
    if (terminalKind === "success") this.spent.set(state.key, state.spent + actualCost);
  }
}

function runCases() {
  const cases = [];
  const check = (id, meaning, fn) => {
    fn();
    cases.push({ id, result: "PASS", meaning });
  };

  check("SCOPE-1", "A and B can share a trace without sharing their agent-local budget", () => {
    const l = new RecordedSpendStopThreshold();
    l.settleSuccess("A", "trace-7", 1.00);
    assert.equal(l.admits("A", "trace-7", 1), false);
    assert.equal(l.admits("B", "trace-7", 1), true);
  });
  check("SCOPE-2", "An agent's separate session does not inherit its other session's spend", () => {
    const l = new RecordedSpendStopThreshold();
    l.settleSuccess("A", "trace-7", 1);
    assert.equal(l.admits("A", "trace-8", 1), true);
  });
  check("SCOPE-3", "An authenticated caller is billed to itself, not a delegated target agent", () => {
    const l = new RecordedSpendStopThreshold();
    const authenticatedCaller = "A", delegatedTarget = "B";
    l.settleSuccess(authenticatedCaller, "trace-9", .75);
    assert.equal(l.current(authenticatedCaller, "trace-9"), .75);
    assert.equal(l.current(delegatedTarget, "trace-9"), 0);
  });
  check("ADMISSION-1", "Two concurrent calls can both pass a post-settlement stop threshold", () => {
    const l = new RecordedSpendStopThreshold();
    l.settleSuccess("A", "trace-10", .75);
    const first = l.admits("A", "trace-10", 1);
    const second = l.admits("A", "trace-10", 1);
    assert.equal(first && second, true);
    l.settleSuccess("A", "trace-10", .20);
    l.settleSuccess("A", "trace-10", .20);
    assert.ok(l.current("A", "trace-10") > 1);
    assert.equal(l.admits("A", "trace-10", 1), false);
  });
  check("ADMISSION-2", "A truly reserved ceiling rejects the second known-maximum request", () => {
    const l = new ReserveBeforeForward();
    assert.equal(l.reserve("A", "trace-11", 1, .75), true);
    l.settle("A", "trace-11", .75, .75, "success");
    assert.equal(l.reserve("A", "trace-11", 1, .20), true);
    assert.equal(l.reserve("A", "trace-11", 1, .20), false);
    l.settle("A", "trace-11", .20, .20, "success");
    assert.equal(l.state("A", "trace-11").spent, .95);
  });
  check("ADMISSION-3", "Failure refunds an unused reservation without charging spend", () => {
    const l = new ReserveBeforeForward();
    assert.equal(l.reserve("A", "trace-12", 1, .7), true);
    l.settle("A", "trace-12", .7, 0, "failure");
    assert.equal(l.state("A", "trace-12").reserved, 0);
    assert.equal(l.reserve("A", "trace-12", 1, 1), true);
  });
  check("ADMISSION-4", "A claimed hard cap must reject an actual cost above the reservation bound", () => {
    const l = new ReserveBeforeForward();
    assert.equal(l.reserve("A", "trace-13", 1, .4), true);
    assert.throws(() => l.settle("A", "trace-13", .4, .6, "success"), /exceeded reserved maximum/);
  });
  check("NONFIT-1", "An intentionally shared trace-wide cap is a different policy than agent-local caps", () => {
    const l = new RecordedSpendStopThreshold();
    l.settleSuccess("A", "trace-14", 1);
    assert.equal(l.admits("B", "trace-14", 1), true);
    // A separate, explicitly owned trace-global rule would be required to block B.
  });
  check("BOUNDARY-1", "Invalid or missing resource identity cannot silently become a scope", () => {
    assert.throws(() => scopeKey("", "trace-15"), /required/);
    assert.throws(() => finiteNonnegative(Number.POSITIVE_INFINITY), /finite/);
    assert.throws(() => finiteNonnegative(-1), /finite/);
  });

  return cases;
}

if (process.argv.includes("--self-test")) {
  try {
    const cases = runCases();
    if (process.argv.includes("--json")) {
      process.stdout.write(JSON.stringify({
        kind: "isolated_exercise", status: "PASS", assertions: cases.length, cases,
        external_product_tested: false, independent_theory_adoption_observed: false
      }, null, 2) + "\n");
    } else {
      for (const c of cases) console.log(c.id + " PASS — " + c.meaning);
      console.log("9/9 isolated model checks PASS; no LiteLLM/runtime/release/adoption claim.");
    }
  } catch (error) {
    console.error(error);
    process.exitCode = 1;
  }
} else {
  console.log("Run with --self-test. No network, credentials, or side effects.");
}
