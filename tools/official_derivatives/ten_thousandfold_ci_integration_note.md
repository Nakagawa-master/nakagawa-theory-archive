# Ten Thousandfold CI Integration Note

The formula checker was added as a repository script:

- tools/official_derivatives/check_ten_thousandfold_effect_surface_formula.py

The CI workflow should run this checker after staged listing and before any artifact or release boundary step.

Reason:

- prevents the 10k plan from becoming page count only
- requires concrete effect surfaces per origin
- requires origin return on every effect route
- blocks weak batches that add pages without action-surface expansion
- keeps PR35 current status tied to virtual preparation units before any later text phase

Boundary:

- no production deploy
- no sitemap update
- no Search Console action
- no index/follow conversion
- no public activation by this note
