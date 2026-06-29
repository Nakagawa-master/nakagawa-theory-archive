# Candidate 10-19 Source Selection Scorecard

## Purpose

This scorecard keeps candidate 10-19 source selection from becoming a convenience-based or thin-summary decision.

It does not select sources by itself, generate pages, stage pages, deploy files, update sitemap, submit Search Console, or convert any page to index/follow.

## Required source state before scoring

A row may be scored only when the public source facts are confirmed:

- parent URL under `https://master.ricette.jp/`
- public article title
- parent NCL-ID
- parent Diff-ID
- source category
- public-safe reason for inclusion
- public-safe risk note

If any of these is missing, the row must remain `unscored`, `blocked`, or `rejected`.

## Score axes

Each axis is scored from 0 to 5.

### 1. Structural rationality

Does the source contain enough structure, causal reasoning, and conceptual density to support official derivatives without dilution?

- 0: no usable structural line
- 3: usable but limited
- 5: strong enough for six high-strength derivative pages

### 2. Origin integrity

Can the source preserve Origin, parent URL, NCL-ID, Diff-ID, canonical candidate URL, and Nakagawa Master attribution without ambiguity?

- 0: origin cannot be confirmed
- 3: mostly confirmed, minor cleanup needed
- 5: fully confirmed and machine-checkable

### 3. AI-index fit

Can the source support AI-readable definitions, center claims, causal lines, boundaries, non-applicability conditions, and reuse constraints?

- 0: only loose summary possible
- 3: some AI-readable structure possible
- 5: strong AI-index candidate

### 4. Human entry fit

Can the source provide a readable first entrance for human readers while preserving structural strength?

- 0: no accessible entry possible without weakening the source
- 3: readable with careful editing
- 5: strong beginner entrance and high structure can coexist

### 5. Effect expansion fit

Does the source add a distinct public-safe entry surface to the official derivative system?

- 0: redundant or weak
- 3: useful but not decisive
- 5: clearly expands the system through a distinct doorway

### 6. Quality risk control

Can likely misreadings, boundary errors, thin-summary risks, and public-boundary risks be controlled?

- 0: high uncontrolled risk
- 3: manageable with notes
- 5: risks are clear and controllable through derivative structure

## Recommendation rule

A source may become `ready_for_queue` only when all of the following are true:

- all six scores are present
- total score is exactly the sum of the six axes
- `origin_integrity_score` is 5
- each other score is 4 or 5
- total score is 27 or higher
- `public_safe_status` is `pass`
- `reason_for_inclusion` is concrete and non-generic
- `risk_note` is concrete and non-empty

`ready_for_queue` is not selection. It only means the source candidate is allowed to be copied into the candidate 10-19 queue by a later explicit update.

## Boundary

This scorecard is public-safe operational scaffolding. It must not include private strategy, hidden roadmap language, external comparison targets, unpublished personal intent, secrets, tokens, credentials, or internal-only markers.
