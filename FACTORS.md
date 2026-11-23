# Planting Guide: factors and fields (v0.2)

This is the final factor and field list for phase 2. The data itself lives inside `index.html`, in the `<script id="pgdata">` block. It covers 50 plants, 30 pests and diseases, 54 pair rules and 16 tools.

Units are inches, °F, days and gallons. Week numbers count from the average last spring frost, and negative weeks are before it.

## 1. Factor ranking (impact on outcome)

The ranking uses the production-ecology hierarchy from crop science, which sorts factors into three tiers:

- **Defining** factors set the ceiling on what a plant can do.
- **Limiting** factors hold it below that ceiling.
- **Reducing** factors take yield away.

Inside each tier, the order reflects how often home gardens get that factor wrong and how much it costs when they do.

Any single factor at an extreme becomes the most important one, because growth is capped by whichever resource is scarcest (Liebig's law of the minimum). The weights are the app's starting hypothesis, and the Find plants tab uses them for the fit score.

| Rank | Tier | Factor | Fields used | Weight |
|---|---|---|---|---|
| 1 | Defining | Temperature and frost fit | zone_min/max, frost_tolerance, days_to_maturity, outdoor week, season length | 25 |
| 2 | Defining | Light | sun_need, sun_hours_min, light_lux | 20 |
| 3 | Limiting | Water | water_need, moisture_target, critical_water_stages | 12 |
| 4 | Limiting | Drainage and soil air | drainage_need, soil_texture_pref | 10 |
| 5 | Limiting | Nutrients | feeder_type, n_fixer | 8 |
| 6 | Limiting | Soil pH | ph_min, ph_max | 8 |
| 7 | Limiting | Spacing and room | spacing_in, mature_spread_in, min_container_gal | 7 |
| 8 | Reducing | Pests and diseases | afflictions | 4 |
| 9 | Reducing | Planting technique | germ temps, sow_depth_in, start_method, difficulty | 3 |
| 10 | Reducing | Care and safety | pruning_type, support_type, toxic_to_pets | 3 |
| 11 | Reducing | Companion planting | pair rules (companion / guild) | notes only |

### Can we run a regression?

Not yet. A regression needs outcomes, meaning how each plant actually did, and so far the app has only conditions.

Here is what it would take:

1. **Log outcomes per placed plant.** This could be harvest weight, survival to harvest, or a 1–5 health score.
2. **Log measured inputs.** These come from the tools: moisture, soil temperature, pH and sun hours.
3. **Collect enough records.** Plan on a few hundred plantings per crop.
4. **Choose a model that suits limiting factors.** Use boundary-line analysis or a mixed model with crop as a grouping factor. A plain linear regression won't work well here, because the factors don't add up: the scarcest one caps the result, and sun, temperature and water rise and fall together.

Once enough logs exist, fitted weights replace the ones in the table above.

## 2. Placement checks (why a ring is red, amber or green)

Each check runs at the slider's week. The ring takes the color of the worst result, and grey means the plant is not in the ground that week.

| Check | Red | Amber |
|---|---|---|
| Frost | Tender plant out before last frost | Half-hardy plant out more than 4 weeks early |
| Season length | — | Can't mature before first fall frost |
| Zone (perennials) | Winters colder than zone_min | Winters warmer than zone_max |
| Light | Full-sun plant in shade or indoors | Full-sun plant in part sun; shade plant in full sun |
| Crowding | Closer than 70% of combined spacing at this week's sizes | Tight now, or will crowd later while both are growing |
| Bad neighbors | Antagonist or shared-disease plant inside min_distance_in while both are planted | They will overlap in time later |
| Neighbor shade | — | Plant at least 6 in taller is to the south and its midday shadow (0.8 × height) reaches this one |
| Soil / water | pH off by more than 1; dry-soil plant in clay | pH slightly off; drainage, water or fertility mismatch |
| Past prime | — | Harvest window over |

Companion pairs show as a green note and never change the ring color.

**Symbols:**

- **Ring:** half the recommended spacing, so the room the plant needs when full grown.
- **Filled disc:** the plant's canopy this week.
- **Dotted outline** (shown when a plant is selected): its full-grown size.
- **Dashed lines:** point to the neighbor causing an amber or red check.
- **Corner badge:** ✓, ! or ✕, so the status can be read without relying on color.

## 3. Growth model

Annuals grow on an S-shaped (logistic) curve:

- They start at `start_size_frac`, which is 0.15 for transplants, 0.12 for seed pieces and cloves, and 0.03 for direct sowing.
- They reach half size at `days_to_half_size`, which is 55% of `days_to_maturity_max`.
- They reach full size at `days_to_maturity_max`.

Each plant moves through these stages:

| Stage | When |
|---|---|
| Seedling | Under 30% of full size |
| Growing | From 30% of full size until days_to_maturity_min |
| Mature | From days_to_maturity_min until the harvest window ends |
| Past prime | For 3 weeks after the harvest window, then removed |

Tender plants die at the first fall frost, half-hardy plants 2 weeks later and hardy plants 6 weeks later. Perennials are treated as established plants that go dormant over winter. A "newly planted" option draws them at 40% size.

## 4. Plant fields

### Identity
| Field | Type | Notes |
|---|---|---|
| id | string | snake_case, unique |
| common_name, scientific_name, family | string | Family drives rotation and shared-disease checks |
| category | enum | vegetable, herb, fruit, flower, houseplant |

### Site
| Field | Type | Notes |
|---|---|---|
| life_cycle | enum | annual, biennial, perennial, perennial_grown_as_annual |
| zone_min, zone_max | int | USDA zones (perennials and houseplants) |
| frost_tolerance | enum | tender, half_hardy, hardy |
| sun_need | enum | full, full_or_part, part, shade, indirect |
| sun_hours_min | int | **New.** Derived: full 6, full_or_part 4, part 3, others 0 |
| photoperiod_type | enum | neutral, long_day_bolting, long_short_or_intermediate_day |
| chill_hours | int | **New.** Winter chill needed to fruit (fruit trees) |
| pollinizer_needed | bool | **New.** Needs a second variety nearby |
| light_lux_min/max, humidity_min_pct, temp_min_f | int | Houseplants |

### Soil
| Field | Type | Notes |
|---|---|---|
| ph_min, ph_max | float | Preferred range |
| soil_texture_pref | enum | loam, sandy_loam, sandy, sandy_acidic, potting_mix |
| drainage_need | enum | moist, well_drained, dry |
| feeder_type | enum | light, medium, heavy |
| n_fixer | bool | Legumes |

### Planting
| Field | Type | Notes |
|---|---|---|
| start_method | enum | direct_sow_only, direct_sow_preferred, transplant_ok, transplant_preferred, seed_piece, clove, crown, bare_root_cane, bare_root_tree, potted_shrub, transplant_or_division, transplant_or_cutting, cutting_or_division |
| indoor_start_weeks_before_last_frost | int | |
| outdoor_weeks_from_last_frost | int | Default planting week in the planner |
| germ_soil_temp_min_f, germ_soil_temp_opt_f | int | Filled by a soil thermometer reading |
| days_to_germination_min/max | int | |
| sow_depth_in | float | 0 = surface sow |
| spacing_in, row_spacing_in, per_sq_ft | int | Houseplants: spacing = spread |
| mature_height_in, mature_spread_in, root_depth_in | int | |
| min_container_gal | float | Null = not suited to containers |
| clear_radius_in | float | Derived: spacing ÷ 2 (the ring) |
| footprint_radius_in | float | Derived: spread ÷ 2 (dotted outline) |

### Growth and display (new in v0.2)
| Field | Type | Notes |
|---|---|---|
| start_size_frac | float | Size when planted, as a fraction of full size |
| days_to_half_size | int | Logistic midpoint |
| silhouette | enum | vine_staked, bush, mound_sprawl, rosette, upright_leafy, feathery, root_top, grass_spike, tall_stalk, cane, shrub, spike_flower, tree, potted_tree, flower_stem, house_trailing, house_sword, house_bigleaf, house_clump |
| foliage_color, accent_color | hex | Leaf color; fruit or flower color |
| difficulty | enum | easy, moderate, hard |

### Care
| Field | Type | Notes |
|---|---|---|
| water_need | enum | low, medium, high |
| moisture_target | enum | evenly_moist, dry_top_inch, dry_top_2in, dry_out_between. Filled by a moisture meter reading |
| critical_water_stages | list | germination, flowering, fruit_set, pod_set, tuber_set, tasseling, silking, head_formation, bulbing, fruiting |
| pruning_type | enum | none, sucker_removal, pinch_tips, cut_and_come_again, deadhead, renewal, dormant_cutback, dormant_structural, runner_removal, shear_after_flowering |
| support_type | enum | none, stake, cage, stake_or_trellis, trellis_vertical, trellis_netting, trellis_wire, pole_or_trellis, moss_pole, moss_pole_optional |
| climbing_method | enum | tendrils, twining, scrambling, aerial_roots, null |

### Lifecycle and harvest
| Field | Type | Notes |
|---|---|---|
| days_to_maturity_min/max | int | |
| maturity_from | enum | seed, transplant, planting, fall_planting |
| harvest_type | enum | single, repeat_continuous, repeat_seasonal |
| harvest_window_days | int | After this the plant is "past prime" |
| years_to_first_harvest | int | Perennials |
| succession_interval_days | int | |
| bolt_trigger | list | heat, long_days |

### Relationships and housekeeping
| Field | Type | Notes |
|---|---|---|
| companions, antagonists | list | Derived from pair rules |
| afflictions | list | Links to the pest library |
| toxic_to_pets | bool | Null = not recorded |
| notes | string | |
| verified, sources | bool, list | False until checked against a named source |

## 5. Pair rules
| Field | Values |
|---|---|
| plant_a, plant_b | Plant ids |
| relation | companion, antagonist, shared_disease, guild |
| reason | support, living_mulch, nitrogen, pest_confusion, trap_crop, beneficial_insects, nematode_suppression, shade_provider, space_use, growth_inhibition, late_blight, corn_earworm, verticillium_wilt, fire_blight, … |
| evidence | tested, traditional, anecdotal |
| min_distance_in | Antagonists and shared diseases |

## 6. Pests and diseases
| Field | Values |
|---|---|
| type | insect, mite, mollusk, fungus, water_mold, bacterium, disorder |
| hosts | Derived from plants |
| stages | early, mid, late, each with `symptoms`, `photo`, `photo_credit`, `photo_license` |
| favoring_conditions, prevention | Text |
| pattern, pattern_color | **New.** Drives the stage illustrations until licensed photos are added |
| photo_search_url | **New.** Wikimedia Commons search for openly licensed photos |

## 7. Tools
These are the 16 tools in `tools` (moisture meter, hygrometer, soil thermometer, min/max thermometer, pH meter, NPK kit, lab test, EC meter, light meter, sun calculator, rain gauge, penetrometer, refractometer, hand lens, sticky traps, smart sensor). Each record lists `measures`, `units`, `fills_fields`, `best_for`, `cost_tier` and `review_url`. Reviews are written for the moisture meter, soil thermometer and pH meter, and the rest are queued.

## 8. Still to do
- Check every value against a named extension source, then set `verified` and fill in `sources`.
- Replace the illustrations with photos, recording each photo's credit and license.
- Expand plant coverage to every hardiness zone, including zone 1–3 perennials and zone 10–13 tropical fruit and vegetables.
- Split varieties out from plants (for example, specific tomato cultivars).
- Add an outcome log so the fit weights can eventually come from a regression.
