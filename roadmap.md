# Planting Guide — roadmap (from user notes, 2026-11-23)

Status key: ✅ done · 🔜 next · 📋 planned · ❓ waiting on a decision

## Decisions (user, 2026-11-23)
1. The app asks for **state or ZIP**. Native and invasive status are keyed by state, not by hardiness zone.
2. "Plan my garden" **suggests counts and suggests additional plants**, on top of what the user picked.
3. **No server for now.** Builds are saved in the browser with export/import. Revisit if this becomes a problem.
4. **Fence animals:** deer, moose, rabbits, groundhogs, voles, gophers, **dogs and kids**. A fenced area that keeps dogs and kids out removes the pet/child toxicity concern for plants inside it. In the fence details, the user ticks a checklist of which animals they think the fence keeps out; the app suggests ticks from the height and buried depth.
5. **Bed shapes:** rectangle, L-shape, circle and sets of raised beds.
6. **Build order:** (1) quick fixes → (2) named builds + Place-in-planner pop-up → (3) Calendar tab → (4) structures, shade, fences → (5) interactive 3D → (6) data expansion, Techniques tab, native/invasive filters.

## 1. Quick fixes — 🔜 in progress
- **Wording:** "Tight with X" (a spacing warning) becomes "Too close to X". Companion notes become "Grows well near X".
- **Season length:** red if days to maturity are more than the days in the season; amber if the margin is under 2 weeks.
- **Grow light** setting when Indoors is chosen (none / hours per day). The light check uses it.

## 2. Builds — 🔜 in progress
- Named builds ("Veg garden", "Front flower bed"), each with its own bed size, conditions and plant list. Saved in the browser, with export/import as a file.
- **Find → "Place in planner"** opens a pop-up: "Add n × [plant] to [current build]" or "Start a fresh build" (both ask for n).

## 3. Calendar tab
- A weekly itinerary built from the current build: sow/transplant, harden off, trellis, prune, water (preferred and minimum), harvest (once or repeating), frost-check reminders. One combined entry per week, e.g. "Transplant cabbage, broccoli, kale into main garden. Lettuce and radish seedlings into trays. Water seedlings daily, main garden every 3 days. Check frost forecast before planting."
- Each task has a done checkbox and "delay by n days", which shifts the tasks that depend on it.
- Export to a phone calendar (.ics).

## 4. Planner 2D: site and layout
- **Available-plant count** at the bottom right of the conditions panel (darker tan). It recalculates as conditions change. Plants that fail a hard condition drop out of the palette (light tan) instead of just turning red.
- **Select plants → "Plan my garden!"**: auto-places the selection with suggested counts and suggested extra plants.
- **Bed dimensions** in the conditions panel *and* under the canvas, both controlling the same setting. Bed shapes: rectangle, L, circle, raised-bed sets.
- **Move/remove help:** visible hints (drag to move; right-click or Delete to remove) and a "?" overlay.
- **Maximize my space:** the densest valid packing (respects spacing, neighbor distances and height order).
- **Target output:** the user enters desired lbs (total or per week); the app sizes the count. If that's over capacity, the number turns red and the error gives two caps: (1) the max if this were the only plant, (2) the max given the space other plants already hold.
- **Site objects:** walkways use planting space but don't change the outer circle. Fences have a height, a buried depth and an animal checklist (see decision 4). A house or wall casts shade.
- **Orientation:** a "which way is south" control. Plants are ordered tall to short, north to south.
- **Shade from structures:** sun hours per spot. Full-sun plants go red below their minimum, and shade plants are preferred there.
- **Irrigation layer:** drip lines, soaker hoses and sprinklers. Feeds the watering schedule.
- **Location input:** state/ZIP.

## 5. Garden 3D
- Make 3D a full editor: the same palette, place/move/remove, reset scenario and the same conditions panel. State is shared with 2D.

## 6. Data, Find and Techniques
- **Find:** Indoor/Outdoor toggle. Indoor uses an indoor climate (a heated home is treated as about zone 11) plus a coolest-room-temperature setting.
- **Native** filter: prefer (sort first) or require. **Invasive** filter: warn/sort last, or exclude. Both by state.
- **Zone coverage (50 plants):** the 31 annuals fit every zone. Perennials per zone: Z1–3: 0, Z4: 5, Z5–6: 12, Z7: 13, Z8: 11, Z9: 7, Z10: 2, Z11–13: 1. Priority: perennials for zones 1–4 and 9–13, plus short-season annual varieties.
- Native status by state (USDA PLANTS) and invasive status by state (state lists, EDDMapS).
- Yield per plant (extension tables) for the output target.
- Gardener-error issues: overwatering and underwatering.
- **Techniques tab:** grafting, hugelkultur, trenching asparagus, trellis types, season extension, tillage vs no-till, irrigation methods. Extension sources first.

## Done
- ✅ Removed the "Can we run a regression?" section (2026-11-23, v0.5.1).
