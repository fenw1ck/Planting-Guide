# Planting Guide

A planner for gardens and houseplants. Place plants in a bed, move the season slider, and the app shows where each plant will do well, along with the reason for every flag.

**Live site:** https://fenw1ck.github.io/Planting-Guide/

## Tabs

| Tab | What it does |
| --- | --- |
| Planner (2D) | A conditions panel on the left sets your zone, frost date, time of year and bed. Place plants and drag them around. The ring shows placement (spacing, neighbors, shade), and a ⚑ flag shows any condition problem, with a fix. Hotbar, pipette, undo and row-painting all have keyboard shortcuts. |
| Garden view (3D) | Shows the same bed in 3D with a distinct silhouette for each plant type, drawn as seedling, growing, mature or past prime. The bed can be rotated. |
| Find plants | You set the filters. Each plant gets a fit score for your conditions, and "Use matches in planner" sends the results to the planner. |
| Pests & diseases | A searchable library of 30 problems, with early, mid and late illustrations, host plants, causes and prevention. |
| Research | Explains how the app thinks, ranks the factors, says whether a regression is possible, reviews the tools (moisture meters, soil thermometers, pH meters), shows the source checks behind every plant value, and lists references. |
| Settings | Rebind every key and set mouse options. Presets follow Stardew Valley, The Sims 4, Cities: Skylines or Factorio, and a comparison table explains the defaults. |

Your growing conditions bar is at the top of every tab: zone, frost date, season length, sun, soil pH, soil type, fertility, watering, beds, containers or indoors, and pets. Settings and the bed you build are saved in your browser.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | The whole site in one file, with the data built in |
| `FACTORS.md` | Final factor and field list, factor ranking, placement rules, growth model |
| `README.md` | This file |
| `setup-board.sh` | Creates the GitHub project board and starter issues |

## Publish the site

1. Upload `index.html`, `README.md` and `FACTORS.md` to the repo, replacing the old copies.
2. Go to **Settings → Pages**. Set **Source** to *Deploy from a branch*, choose `main` and `/ (root)`, then click **Save**.
3. Wait a minute or two, and the site will be live at the link above.

You can delete `planting-guide-phase1.zip` from the repo, because everything in it is now built into `index.html`.

## Builds (v0.6)
The planner holds several named builds (e.g. "Veg garden", "Front flower bed"). Each build has its own conditions, bed size, plants and week. The bar above the planner switches, creates, renames, duplicates and deletes builds. Export saves all builds to a .json file; Import loads them back (useful for moving to another browser or device). Builds live in this browser's storage only: there is no server.

In Find plants, "Place in planner" asks how many. You can add them to the current build, or start a fresh build with that many. Plants go into the first free spots that respect full-size spacing. If they don't all fit, a message says how many did.
