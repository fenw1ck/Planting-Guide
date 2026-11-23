# Planting Guide — project index

- Factor analysis & data model doc: https://claude.ai/artifact/J8Yw52xnyQfoQbzSspaSs4
- GitHub repo: https://github.com/fenw1ck/Planting-Guide
- GitHub Pages URL (once Pages is enabled): https://fenw1ck.github.io/Planting-Guide/

## Decisions so far
- Seven factor families: site, soil, planting, care, lifecycle/harvest, neighbors, pests & diseases.
- Placement ring has three states: red (conflict), amber (works, not ideal), green (good).
- Conflicts are checked in time as well as space; plants grow along a growth curve over a season slider.
- Companion rules carry an evidence level (tested / traditional / anecdotal).
- 16 gardener tools mapped to fields; each will link to a multi-model review page.
- Units: inches, °F, days, gallons. Week offsets are relative to last spring frost (negative = before).

## Status
- 2026-11-22: index.html, README.md, setup-board.sh uploaded to repo. Pages not yet reachable (likely not enabled).
- 2026-11-22: Phase one built (delivered as zip, pending upload): data/SCHEMA.md (field list v0.1), data/build_data.py generator, 42 plants, 25 afflictions, 48 pair rules, 16 tools (JSON + CSV), plants.html browser.
- Next (phase two): verify each value against named extension sources (verified/sources fields), affliction photos with licenses, growth-curve fields, varieties.
