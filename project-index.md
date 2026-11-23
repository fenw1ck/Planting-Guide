# Planting Guide — project index

- Factor analysis & data model doc: https://claude.ai/artifact/J8Yw52xnyQfoQbzSspaSs4
- GitHub repo: https://github.com/fenw1ck/Planting-Guide
- GitHub Pages URL (once Pages is enabled): https://fenw1ck.github.io/Planting-Guide/

## Decisions so far
- Seven factor families: site, soil, planting, care, lifecycle/harvest, neighbors, pests & diseases.
- Placement ring has three states plus grey: red (conflict), amber (works, not ideal), green (good), grey (not in ground that week). Ring = half the spacing (room needed when grown); filled disc = this week's size; badge ✓ ! ✕ for color-blind reading.
- Conflicts are checked in time as well as space; plants grow along a logistic growth curve over a season slider (weeks from last frost).
- Companion rules carry an evidence level (tested / traditional / anecdotal) and never change ring color.
- Factor ranking (production-ecology tiers): climate 25, light 20, water 12, drainage 10, nutrients 8, pH 8, room 7, pests 4, technique 3, care 3; companions notes only. Weights are hypotheses until outcome data allows a regression (boundary-line or mixed model).
- Delivery format: single self-contained index.html + .md files. No zips (user preference).
- Units: inches, °F, days, gallons. Week offsets are relative to last spring frost (negative = before).

## Status
- 2026-11-22: index.html, README.md, setup-board.sh uploaded. Phase 1 uploaded only as planting-guide-phase1.zip (not extracted).
- 2026-11-23: v0.2 built and sent as index.html + FACTORS.md + README.md (pending upload). Tabs: Planner 2D (season slider, per-check explanations), Garden 3D isometric (19 silhouettes, 4 growth-stage icons incl. rot marker), Find plants (user filters + fit score), Pests & diseases (30, drawn stage illustrations), Research (thought process, ranking, regression answer, reviews of moisture meters / soil thermometers / pH meters, references). Data: 50 plants (added apple, pear, peach, fig, Meyer lemon, sunflower, zinnia, lavender), 30 afflictions, 54 pair rules, 16 tools.
- Next: licensed photos per pest stage; verify values against extension sources; expand plants across all hardiness zones; varieties; outcome log for future regression; remaining 13 tool reviews.
