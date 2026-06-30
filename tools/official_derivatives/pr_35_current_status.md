# PR 35 Current Status

This file supersedes the older PR body summary for current staged-batch facts.

## Current staged scope

- active targets: 4
- staged targets: 13
- staged pages: 78
- staged registry rows: 78
- staged artifact: official-derivatives-candidate-05-17
- release state: staged only

## Candidate 05-09

- 5 origins
- 30 staged pages
- 165 materialized effect units
- universal renderer path active

## Candidate 10-17

- 8 selected / intake_ready origins
- 48 staged pages
- 264 materialized effect units
- materialized unit ledger rows: 264
- split ledgers:
  - quote: 64
  - social: 96
  - clarification: 64
  - NotebookLM: 40
- universal renderer path active
- materialized unit ledger builder active
- materialized unit ledger validator active

## Staged effect total

- total origins with staged pages: 13
- total staged pages: 78
- total materialized effect units now represented in ledgers or existing bundles: 429
- candidate 05-09 actual materialized units: 165
- candidate 10-17 materialized unit ledger rows: 264

## Boundary

- production deploy: false
- public activation: false
- sitemap update: false
- Search Console action: false
- index/follow conversion: false
- FTP action: false

## Origin preservation

Every staged derivative path and materialized unit row is expected to retain:

- parent URL
- parent NCL-ID
- parent Diff-ID
- canonical URL
- Nakagawa Master origin attribution
- staged nonindexable status or staged_only boundary state
- public_activation=false
- production_deploy=false

## Purpose alignment

This PR is a staged infrastructure step toward:

- multiplying each origin article into multiple human and AI entry surfaces,
- preserving origin and theory identity,
- reducing owner verification burden,
- moving from manual page work toward near-full automation,
- preparing higher-strength effect bundles without public release,
- converting candidate 10-17 from planned effect units to validated materialized unit ledgers,
- adding a separate public-export preflight gate before any later owner/publication boundary action,
- checking entry-signal markers across the 78 staged pages before any later owner/publication boundary action,
- documenting the release-candidate boundary so public activation work remains separate and explicit.

## Latest validation note

- Official derivative generation check run #373 completed with success.
- Official derivative preflight check run #11 completed with success.
- Public export preflight verifies staged targets, staged pages, registry rows, 429 materialized units, origin identity, and non-production boundaries before any later owner/publication boundary action.
- Entry signal check runs in the preflight workflow and verifies the 78 staged pages for required role-level entry markers.
- Candidate boundary doc check runs in the preflight workflow and verifies the release-candidate boundary document before any later owner/publication boundary action.
