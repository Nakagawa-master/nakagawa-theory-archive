# Codex restore and complete task: Official Derivative 010-017 v5 body phase

This task record preserves the PR #35 recovery requirement for Official Derivative 010-017.

## Required state

- Restore `generate_candidate_10_17_universal.py` if missing.
- Load exactly 8 records from `official_derivative_target_adapter.load_render_candidate_10_17()`.
- Generate exactly 48 staged pages: 8 origins × 6 pages.
- Use `six_page_template_core.PAGES`, `assert_contract()`, and `high_strength_body_renderer.pages_for_high_strength(record)`.
- Preserve staged/noindex boundaries and do not publish, sitemap, Search Console, FTP, or index/follow any generated page.

## Body quality gate

- Human summary keeps the seven-section structure from the v3.1 execution standard.
- FAQ keeps the three-layer structure: beginner, structural understanding, and misreading/counterargument/boundary conditions.
- JA/EN/ZH AI indexes preserve Origin, Parent NCL-ID, Parent Diff-ID, causal line, applicability, non-applicability, counterconditions, citation requirements, AI reuse cautions, and AI reading lock.

## Public boundary

PR #35 remains staged/draft. Generated files are internal staged outputs until a separate owner decision promotes them.
