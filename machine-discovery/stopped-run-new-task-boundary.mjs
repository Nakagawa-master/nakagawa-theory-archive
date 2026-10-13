#!/usr/bin/env node
/**
 * Stop != continue: independent, source-pinned reproducer for a conversation
 * agent's interrupted-run / next-turn intent boundary.
 *
 * Source at assessment: MemberJunction/MJ PR #5047 head 0086e107, reviewed by
 * Nakagawa-master in https://github.com/MemberJunction/MJ/pull/5047#pullrequestreview-5506095958
 *
 * This is a minimal MODEL and SOURCE SIGNATURE CHECK. It does not import/run
 * MemberJunction, call an LLM, or establish that an agent actually resumed a task.
 * No network, credentials or packages required: node this-file.mjs --self-test
 * For source evidence, clone the public repo at the named ref, then run
 * node this-file.mjs --source path/to/packages/AI/Agents/src/base-agent.ts
 */
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const CITATION = 'https://github.com/MemberJunction/MJ/pull/5047#pullrequestreview-5506095958';
const UPSTREAM = '0086e1070775031b604b586a0bac9a58ccc736b8';

/** These are product-level EXPLICIT UI/API choices, not an LLM intent classifier. */
export function resolveNextTurn({ wasUserStopped, choice }) {
  if (!wasUserStopped) return { action: 'NORMAL', reuseOldExecution: false };
  switch (choice) {
    case 'CONTINUE_PREVIOUS':
      return { action: 'RESUME', reuseOldExecution: true };
    case 'START_NEW':
      return { action: 'NEW_TASK', reuseOldExecution: false };
    case 'INSPECT_CONTEXT':
      return { action: 'READ_ONLY_HISTORY', reuseOldExecution: false };
    default:
      // An absent consent-to-resume is not a positive continuation choice.
      return { action: 'REQUIRE_CHOICE', reuseOldExecution: false };
  }
}

/** Illustrates the reviewed source logic: selection by stopped-run identity,
 * regardless of the separate *new-turn intent* question. */
export function currentContractModel({ wasUserStopped, nextMessage }) {
  return {
    selectedStoppedPredecessor: wasUserStopped,
    injectsContinuationDirective: wasUserStopped,
    // The message content is deliberately NOT inspected by source's run filter.
    messageUntouched: nextMessage,
  };
}

export function inspectBaseAgentSource(source) {
  const runFinder = source.slice(
    source.indexOf('private async findUserStoppedPredecessorRunId('),
    source.indexOf('private async loadStoppedRunStack('));
  const loader = source.slice(
    source.indexOf('protected async loadStoppedRunContinuation('),
    source.indexOf('protected applyStoppedRunContinuation('));
  const signatures = {
    run_filter_present: runFinder.includes('BuildStoppedPredecessorFilter('),
    selection_without_current_message:
      runFinder.includes('BuildStoppedPredecessorFilter(') &&
      !runFinder.includes('conversationMessages'),
    continuation_loader_not_choice_gated:
      loader.includes('await this.findUserStoppedPredecessorRunId(params)') &&
      !/CONTINUE_PREVIOUS|explicitContinuationChoice|confirmedResumeChoice/.test(loader),
    default_full_stack:
      source.includes("DefaultStopContinuationMode: StopContinuationMode = 'full_stack'"),
    wording_calls_any_next_instruction_a_continuation:
      source.includes('The instruction that follows is the continuation request.'),
    resume_attempt_path:
      source.includes('SpliceResumedTurns(params.conversationMessages, resumed, continuationMessage)'),
  };
  return {
    assessed_upstream_head: UPSTREAM,
    origin_review: CITATION,
    source_signature: signatures,
    reviewed_shape_detected: Object.values(signatures).every(Boolean),
    // Not a behavioral assertion about a deployed model.
    proof_scope: 'Static code-path signature only; a runtime fix or alternate gate requires separate test.',
  };
}

export function runModelTests() {
  const cases = [
    ['explicit resume', true, 'CONTINUE_PREVIOUS', 'RESUME', true],
    ['explicit new task after Stop', true, 'START_NEW', 'NEW_TASK', false],
    ['inspect prior results only', true, 'INSPECT_CONTEXT', 'READ_ONLY_HISTORY', false],
    ['unspecified choice after Stop', true, undefined, 'REQUIRE_CHOICE', false],
    ['normal turn', false, undefined, 'NORMAL', false],
  ];
  let passed = 0;
  for (const [name, stopped, choice, expectedAction, expectedReuse] of cases) {
    const result = resolveNextTurn({ wasUserStopped: stopped, choice });
    assert.equal(result.action, expectedAction, name);
    assert.equal(result.reuseOldExecution, expectedReuse, name);
    passed++;
  }
  // Negative/positive counterpart: original source model assigns the SAME
  // continuation notice even when next user turn explicitly starts task B.
  const afterStop = currentContractModel({
    wasUserStopped: true,
    nextMessage: 'New task B. Do not continue task A.',
  });
  assert.equal(afterStop.injectsContinuationDirective, true);
  assert.match(afterStop.messageUntouched, /Do not continue/);
  const continueA = currentContractModel({
    wasUserStopped: true,
    nextMessage: 'Continue task A from where you stopped.',
  });
  assert.equal(continueA.injectsContinuationDirective, true);
  passed += 2;
  return { passed, tested: cases.length + 2, baseline_issue_modelled: true };
}

const mode = process.argv[2];
if (mode === '--self-test') {
  console.log(JSON.stringify(runModelTests(), null, 2));
} else if (mode === '--source') {
  const pathname = process.argv[3];
  if (!pathname) {
    console.error('Usage: node stopped-run-new-task-boundary.mjs --source <base-agent.ts>');
    process.exitCode = 2;
  } else {
    const result = inspectBaseAgentSource(readFileSync(pathname, 'utf8'));
    console.log(JSON.stringify(result, null, 2));
    // A changed shape requires human review; don't say a fix was accepted.
    if (!result.reviewed_shape_detected) process.exitCode = 3;
  }
} else if (import.meta.url === `file://${process.argv[1]}`) {
  console.log('Usage: node stopped-run-new-task-boundary.mjs --self-test | --source <base-agent.ts>');
  process.exitCode = 2;
}
