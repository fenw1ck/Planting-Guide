# Planting Guide

A planner for gardens and houseplants. Each plant carries the factors that decide whether it thrives: zone, sun, soil, spacing, depth, water, pruning, support, harvest timing, companions, and pests. You place plant symbols on a 3D plot, and a ring under each one turns green, amber or red to show whether the spot works.

**Live site:** https://fenw1ck.github.io/Planting-Guide/

## What's here

| File | Purpose |
| --- | --- |
| `index.html` | GitHub Pages landing page with an interactive placement-check prototype |
| `setup-board.sh` | Creates the project board, labels and starter issues with the GitHub CLI |

## Publish the site

1. Push `index.html` to the `main` branch.
2. In the repo, go to **Settings → Pages**, set **Source** to *Deploy from a branch*, choose `main` and `/ (root)`, and click **Save**.
3. After a minute or two, the site is live at the link above.

## Create the project board

```bash
gh auth login --scopes project,repo
bash setup-board.sh
```

The script creates 7 workstream labels and 19 issues, then adds them all to a project called *Planting Guide Roadmap*.
