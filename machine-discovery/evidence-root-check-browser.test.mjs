// Run: node machine-discovery/evidence-root-check-browser.test.mjs
// Browser audit is extracted from the actual HTML to prevent test-only duplication.
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { runInNewContext } from 'node:vm';

const html = readFileSync(new URL('./evidence-root-check.html', import.meta.url), 'utf8');
const start = html.indexOf('const relations = [');
const end = html.indexOf('byId("same").addEventListener');
assert.ok(start !== -1 && end > start, 'browser audit region present');
const audit = runInNewContext(html.slice(start, end) + '\naudit;', {});
const src = (url, root, relation, stance = 'supports') => ({url, root, relation, stance});
const A = src('https://test.example/origin-A', 'A', 'primary');
const B = src('https://test.example/test-B', 'B', 'independent_observation');
function check(name, sources, expected) {
  const result = audit(sources, true);
  assert.equal(result.status, expected, name + ': ' + result.issues.join(', '));
}
check('no primary despite two observations', [
  src('https://test.example/test-A', 'A', 'independent_observation'), B
], 'BLOCK');
check('same URL, conflicting relation', [
  A, src(A.url, 'A', 'derived'), B
], 'BLOCK');
check('same URL, conflicting stance', [
  A, src(A.url, 'A', 'primary', 'refutes'), B
], 'BLOCK');
check('independent label shares one of two primary roots', [
  A, src('https://test.example/origin-B', 'B', 'primary'),
  src('https://test.example/test-A', 'A', 'independent_observation')
], 'BLOCK');
check('three reposts of one root', [
  A, src('https://test.example/repost1', 'A', 'derived'),
  src('https://test.example/repost2', 'A', 'derived')
], 'BLOCK');
check('genuinely distinct primary and independent observation', [A, B], 'CONSISTENT_INPUT');
check('identical repeated URL declaration is consistent', [A, A, B], 'CONSISTENT_INPUT');
check('unresolved counterevidence blocks unqualified confirmation', [
  A, B, src('https://test.example/unknown', '', 'unknown', 'refutes')
], 'BLOCK');
assert.equal(audit([A, B], false).status, 'CONSISTENT_INPUT');
console.log('Browser evidence-root regression: 9/9 PASS (input-consistency only)');
