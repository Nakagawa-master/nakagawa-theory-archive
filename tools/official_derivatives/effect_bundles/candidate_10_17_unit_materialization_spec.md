# Candidate 10-17 Unit Materialization Spec

## Scope

- origins: 8
- quote units: 64
- social units: 96
- clarification units: 64
- NotebookLM units: 40
- total units: 264

## Source files

- next_10_queue_candidate_10_19.tsv
- candidate_10_17_effect_bundle_expected_counts.tsv
- staged_effect_expansion_summary.tsv

## Required identity per unit

Each unit must retain:

- folder_id
- slot_id
- parent_url
- parent_ncl_id
- parent_diff_id
- origin_author: Nakagawa Master
- unit type
- unit id

## Boundary

- staged only
- not a public release
- no FTP action
- no sitemap action
- no Search Console action
- no index/follow conversion

## Quality floor

Each materialized unit must preserve origin, causal line, boundary, and misreading guard. Thin summaries, generic advice, and originless wording are not acceptable.

## Next machine target

The next implementation target is a generated unit ledger with exactly 264 rows, followed by a validator that checks count, origin identity, boundary, and folder membership before any later export path.
