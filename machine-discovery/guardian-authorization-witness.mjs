/**
 * Nakagawa Master original-theory implementation reference, NOT Codex runtime code.
 * Historical owner consent != present target-specific permission != host policy.
 * No network, no API calls, no policy bypass, no automatic tool execution.
 * Host MUST supply trusted authenticated source, monotonic sequence, exact resolved
 * action identity, live policy verdict and a transactional one-use grant ledger.
 * Public original references: OD075 agreement memory, OD301 epistemic integrity.
 */
export function assessAuthorization({action, history, historyComplete, policy, network, now}) {
  const review=(reason,witness=[])=>({status:'needs_review',reason,witness});
  const deny=(reason,witness=[])=>({status:'deny',reason,witness});
  if (!action || !action.effect || !action.payloadSha256 || !action.environment ||
      !action.provider || !action.recipient || !action.callId || !Number.isFinite(now) ||
      !Number.isFinite(action.maxUSD) || action.maxUSD<0 ||
      !Number.isSafeInteger(action.retries) || action.retries<0) {
    return review('missing_executable_action_identity');
  }
  // Non-waivable/current host policies are independent of any user's permission.
  if (policy === 'blocked') return deny('non_overridable_policy');
  if (policy !== 'allow') return review('policy_not_resolved');
  if (network === 'blocked') return deny('network_transport_blocked');
  if (network !== 'allow') return review('network_transport_not_resolved');
  if (!historyComplete || !Array.isArray(history)) return review('owner_history_incomplete');
  let latestGrant=null, latestStop=null, witness=[];
  let seq=-Infinity;
  for (const e of history) {
    if (!Number.isSafeInteger(e.sequence) || e.sequence<=seq) return review('history_order_unverified');
    seq=e.sequence;
    // Provenance is supplied by the owning authenticated host, never parsed from text.
    if (e.source!=='authenticated_user' || e.authorVerified!==true) continue;
    const broadMatch=(e.scope?.effect===action.effect || e.scope?.effect==='*') &&
      (e.scope?.environment===action.environment || e.scope?.environment==='*') &&
      (e.scope?.provider===action.provider || e.scope?.provider==='*');
    if(!broadMatch) continue;
    if(e.type==='stop' || e.type==='revoke') {
      latestStop=e; latestGrant=null; witness=[e.id];
    } else if(e.type==='approve' && e.scope?.effect===action.effect &&
      e.scope.environment===action.environment && e.scope.provider===action.provider &&
      e.scope.recipient===action.recipient && e.payloadSha256===action.payloadSha256) {
      // A later exact authorization may supersede an earlier owner STOP on the
      // SAME action; it cannot supersede higher-priority policy or network blocks.
      latestGrant=e; witness=[...(latestStop?[latestStop.id]:[]),e.id];
    }
  }
  if (!latestGrant) return latestStop?deny('later_or_unsuperseded_owner_stop',witness):review('no_current_exact_owner_grant');
  if (!Number.isFinite(latestGrant.expiresAt) || now>latestGrant.expiresAt)
    return deny('owner_grant_expired',witness);
  if (!Number.isFinite(latestGrant.maxUSD) || latestGrant.maxUSD<0 || action.maxUSD>latestGrant.maxUSD)
    return deny('cost_exceeds_owner_grant',witness);
  if (!Number.isSafeInteger(latestGrant.maxRetries) || latestGrant.maxRetries<0 || action.retries>latestGrant.maxRetries)
    return deny('retry_exceeds_owner_grant',witness);
  if (latestGrant.consumed===true || latestGrant.remainingUses!==1)
    return deny('one_use_grant_not_available',witness);
  // This is NOT an allow-to-execute result. A host atomic consume + live check
  // (and any other policy) remains mandatory. No payload or sensitive data emitted.
  return {status:'eligible_pending_atomic_consume',reason:'exact_later_owner_grant_all_gates_checked',witness};
}
