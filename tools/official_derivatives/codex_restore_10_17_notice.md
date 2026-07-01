# Restore notice

Direct ChatGPT connector writes deleted `tools/official_derivatives/generate_candidate_10_17_universal.py`, but the same connector safety layer blocked recreating that path.

Required next Codex action:

- restore `tools/official_derivatives/generate_candidate_10_17_universal.py`
- use `tools/official_derivatives/official_derivative_v5_data_10_17.py`
- use `tools/official_derivatives/high_strength_body_renderer.py`
- regenerate Official Derivative 010-017 deploy pages
- keep PR #35 draft and staged
- do not touch sitemap, Search Console, FTP, production deploy, or index state
