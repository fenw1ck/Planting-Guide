#!/usr/bin/env bash
# Creates the Planting Guide project board, labels and starter issues on GitHub.
# Requires the GitHub CLI (gh), logged in with: gh auth login --scopes project,repo
# Run from anywhere:  bash setup-board.sh
set -euo pipefail

REPO="fenw1ck/Planting-Guide"
OWNER="fenw1ck"
TITLE="Planting Guide Roadmap"

# Labels (one per workstream)
declare -A LABELS=(
  [research]="1d76db"   [data]="5319e7"   [tools]="fbca04"
  [planner]="0e8a16"    [art]="d93f0b"    [pests]="b60205"   [site]="c5def5"
)
for name in "${!LABELS[@]}"; do
  gh label create "$name" --repo "$REPO" --color "${LABELS[$name]}" --force >/dev/null
done

# Project board
PROJECT_NUM=$(gh project create --owner "$OWNER" --title "$TITLE" --format json --jq .number)
echo "Created project #$PROJECT_NUM"

# Issues: "label|title|body"
ISSUES=(
"research|Finalize factor and field list|Review the factor analysis doc and lock the plant, plot and placement fields."
"research|Confirm sowing offsets for Three Sisters and other guilds|Record relative_sow_offset_days and triggers (e.g. corn at 6 in) for each guild."
"research|Add evidence level to companion and antagonist rules|Tag each pair rule as tested, traditional or anecdotal."
"data|Design database schema|Tables: plant, variety, plot, cell, placement, pair_rule, affliction, tool, reading."
"data|Load seed data for 30-50 common plants|Vegetables, herbs and houseplants with spacing, height, pH, harvest type and timing."
"data|Import zone and frost-date lookup|Look up hardiness zone and frost dates by ZIP or location."
"tools|Write review: soil moisture meters|Compare accuracy, calibration and durability for 3-5 models."
"tools|Write review: soil thermometers|Compare 3-5 models; tie readings to germination temperatures."
"tools|Write review: pH meters and test strips|Call out the inaccuracy of cheap two-prong meters."
"tools|Write reviews: hygrometers, light meters, EC meters|One page per tool type, 3-5 models each."
"planner|2D placement checker with red/amber/green ring|Space, time, site and neighbor checks on every drag (prototype on the site)."
"planner|Season slider with growth curves|Grow plants over time, free harvested spots, show conflicts appearing mid-season."
"planner|Shade model by latitude and date|Cast shadows from plant height and sun angle."
"planner|Plant detail card|Care reminders, afflictions to watch this month, and suggested tools."
"art|Plant silhouette set|Distinct isometric shapes per plant family and growth stage, farming-sim style."
"art|Isometric 3D view with 90-degree rotation|Rotate and tilt the plot; keep a top-down mode for precise spacing."
"pests|Affliction library with stage photos|Early, mid and late photos with alt text and image licences recorded."
"pests|Prevention and treatment notes|Organic and chemical controls, favoring conditions and spread risk."
"site|GitHub Pages landing page|Publish index.html from the main branch root."
)

for row in "${ISSUES[@]}"; do
  IFS="|" read -r label title body <<<"$row"
  url=$(gh issue create --repo "$REPO" --title "$title" --body "$body" --label "$label")
  gh project item-add "$PROJECT_NUM" --owner "$OWNER" --url "$url" >/dev/null
  echo "Added: $title"
done

echo "Done. Open the board: https://github.com/users/$OWNER/projects/$PROJECT_NUM"
