# Planting Guide — project index

- Factor analysis & data model doc: https://claude.ai/artifact/J8Yw52xnyQfoQbzSspaSs4
- GitHub repo: https://github.com/fenw1ck/Planting-Guide
- Live site (GitHub Pages, confirmed working by user 2026-11-23): https://fenw1ck.github.io/Planting-Guide/ — Claude's sandbox cannot reach github.io; verify uploads by cloning the repo.

## Decisions so far
- Seven factor families: site, soil, planting, care, lifecycle/harvest, neighbors, pests & diseases.
- Ring = placement only (spacing now/later, bad neighbors, shade from taller plants to the south). ⚑ Flag = conditions (zone, frost timing, season length, sun, soil, pH, water, fertility, pot size, pets, past prime), each with a fix text. Conditions are set in a left-hand panel in the planner. (User request 2026-11-23: a ring stuck red for a soil reason gives no clue how to fix it.)
- Source-disagreement rule (user): take the risk-averse value — later planting week (frost), but move earlier (down to the earliest sourced week) if the crop won't mature before fall frost; wider spacing; longer days to maturity / years to harvest; higher min germination temp; warmer zone_min, cooler zone_max; narrower pH; toxic if any list says toxic. With 3+ sources, majority wins; no majority → risk-averse.
- Companion rules carry an evidence level and never change a color.
- Factor ranking weights: climate 25, light 20, water 12, drainage 10, nutrients 8, pH 8, room 7, pests 4, technique 3, care 3. Hypotheses until outcome data allows a regression.
- Controls: all rebindable in a Settings tab; presets for Stardew Valley, The Sims 4, Cities: Skylines, Factorio; defaults = left-click place, right-click inspect, 1–0 hotbar + Tab, Q pipette, Del remove, Ctrl+Z/Y, Shift-drag to plant a row, Alt off-grid, G grid, [ ] weeks, Space play, , . rotate 3D, V switch view.
- Delivery format: single self-contained index.html + .md files. No zips (user preference).
- Units: inches, °F, days, gallons. Week offsets relative to last spring frost.

## Status
- 2026-11-23: v0.3 uploaded (user). v0.4 sent (index.html, FACTORS.md, README.md; pending upload): risk-averse/majority rules applied, ASPCA pet toxicity, zones for perennial veg/herbs, kale/garlic/sunflower/fig checks; 30/50 plants fully checked, 134 values changed; planner split into conditions panel + placement ring + condition flag; hotbar, undo/redo, pipette, row painting; Settings tab with controls analysis.
- Still unchecked: kale germ temp; pH for chard, cilantro, dill, pothos, peace lily; zones for strawberry, blueberry, apple, pear, peach; chill for strawberry/raspberry; fig & zinnia spacing; most Meyer lemon values.
- Next: licensed pest photos; expand plants across all hardiness zones; varieties; outcome log for regression; remaining 13 tool reviews.
