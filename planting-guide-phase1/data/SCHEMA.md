# Planting Guide data schema (v0.1)

This is the phase-one field list. The source of truth is `build_data.py`: edit the tables there, then run `python3 data/build_data.py` to regenerate the JSON and CSV files.

| File | Records | What it holds |
| --- | --- | --- |
| `plants.json` / `plants.csv` | 42 | One record per plant: traits, timing, spacing, care, afflictions |
| `afflictions.json` | 25 | Pests, diseases and disorders, with 3 symptom stages and photo slots |
| `pair_rules.json` | 48 | Companion, antagonist, guild and shared-disease rules between two plants |
| `tools.json` | 16 | Gardener tools, what they measure, and the fields they fill |

Units: inches, °F, days and gallons throughout. Negative week values mean *before* the last spring frost.

## Plant fields

### Identity
| Field | Type | Values / notes |
| --- | --- | --- |
| `id` | string | snake_case, unique |
| `common_name`, `scientific_name`, `family` | string | Family drives crop rotation and shared-disease checks |
| `category` | enum | vegetable, herb, fruit, flower, houseplant |

### Site
| Field | Type | Values / notes |
| --- | --- | --- |
| `life_cycle` | enum | annual, biennial, perennial, perennial_grown_as_annual |
| `zone_min`, `zone_max` | int | USDA zones; perennials only. For houseplants, where they live outdoors year-round |
| `frost_tolerance` | enum | tender (killed by frost), half_hardy (light frost), hardy (hard frost) |
| `sun_need` | enum | full (6+ h), full_or_part, part (3–6 h), shade (<3 h), indirect (houseplants) |
| `photoperiod_type` | enum | neutral, long_day_bolting, long_short_or_intermediate_day (onions) |
| `light_lux_min`, `light_lux_max` | int | Houseplants; approximate |
| `humidity_min_pct`, `temp_min_f` | int | Houseplants |

### Soil
| Field | Type | Values / notes |
| --- | --- | --- |
| `ph_min`, `ph_max` | float | Preferred range |
| `soil_texture_pref` | enum | loam, sandy_loam, sandy, sandy_acidic, potting_mix |
| `drainage_need` | enum | moist, well_drained, dry |
| `feeder_type` | enum | light, medium, heavy |
| `n_fixer` | bool | Legumes |

### Planting
| Field | Type | Values / notes |
| --- | --- | --- |
| `start_method` | enum | direct_sow_only, direct_sow_preferred, transplant_ok, transplant_preferred, seed_piece, clove, crown, bare_root_cane, potted_shrub, transplant_or_division, transplant_or_cutting, cutting_or_division |
| `indoor_start_weeks_before_last_frost` | int | Null if not started indoors |
| `outdoor_weeks_from_last_frost` | int | When to sow or plant out; negative = before frost. Null = not tied to spring frost (garlic, houseplants) |
| `germ_soil_temp_min_f`, `germ_soil_temp_opt_f` | int | Germination soil temperature |
| `days_to_germination_min/max` | int | |
| `sow_depth_in` | float | 0 = surface sow (needs light) |
| `spacing_in`, `row_spacing_in` | int | Between plants; between rows |
| `per_sq_ft` | int | Square-foot gardening count |
| `mature_height_in`, `mature_spread_in`, `root_depth_in` | int | Used for shade and footprint |
| `min_container_gal` | float | Null = not suited to containers |
| `clear_radius_in` | float | **Derived:** spacing_in ÷ 2. The ring under the symbol |
| `footprint_radius_in` | float | **Derived:** mature_spread_in ÷ 2 |

### Care
| Field | Type | Values / notes |
| --- | --- | --- |
| `water_need` | enum | low, medium, high |
| `moisture_target` | enum | evenly_moist, dry_top_inch, dry_top_2in, dry_out_between |
| `critical_water_stages` | list | germination, flowering, fruit_set, pod_set, tuber_set, tasseling, silking, head_formation, bulbing, fruiting |
| `pruning_type` | enum | none, sucker_removal, pinch_tips, cut_and_come_again, deadhead, renewal, dormant_cutback, runner_removal, shear_after_flowering |
| `support_type` | enum | none, stake, cage, stake_or_trellis, trellis_vertical, trellis_netting, trellis_wire, pole_or_trellis, moss_pole, moss_pole_optional |
| `climbing_method` | enum | tendrils, twining, scrambling, aerial_roots, null |

### Lifecycle and harvest
| Field | Type | Values / notes |
| --- | --- | --- |
| `days_to_maturity_min/max` | int | |
| `maturity_from` | enum | seed, transplant, planting, fall_planting |
| `harvest_type` | enum | single, repeat_continuous, repeat_seasonal |
| `harvest_window_days` | int | How long harvest lasts |
| `years_to_first_harvest` | int | Perennials |
| `succession_interval_days` | int | Re-sow interval for quick crops |
| `bolt_trigger` | list | heat, long_days |

### Relationships (derived from `pair_rules.json`)
| Field | Type | Values / notes |
| --- | --- | --- |
| `companions` | list of ids | relation = companion or guild |
| `antagonists` | list of ids | relation = antagonist or shared_disease |
| `afflictions` | list of ids | Links to `afflictions.json` |

### Housekeeping
| Field | Type | Values / notes |
| --- | --- | --- |
| `toxic_to_pets` | bool | Null = not recorded |
| `notes` | string | One or two practical tips |
| `verified` | bool | False until checked against a named source |
| `sources` | list | URLs or citations used to verify |

## Pair rules

| Field | Values |
| --- | --- |
| `plant_a`, `plant_b` | Plant ids (order does not matter) |
| `relation` | companion, antagonist, shared_disease, guild |
| `reason` | support, living_mulch, nitrogen, pest_confusion, trap_crop, beneficial_insects, nematode_suppression, shade_provider, space_use, row_marker, growth_inhibition, late_blight, corn_earworm, verticillium_wilt, ... |
| `evidence` | tested (research-backed), traditional (long-standing practice), anecdotal (gardener lore) |
| `min_distance_in` | For antagonists and shared diseases: keep at least this far apart. Null for companions |

## Afflictions

| Field | Values |
| --- | --- |
| `type` | insect, mite, mollusk, fungus, oomycete, disorder |
| `hosts` | **Derived** from plants that list it |
| `stages` | 3 items (early, mid, late), each with `symptoms`, `photo`, `photo_credit`, `photo_license` |
| `favoring_conditions`, `prevention` | Short text |

## Tools

| Field | Values |
| --- | --- |
| `measures`, `units` | What the reading is |
| `fills_fields` | Plot or reading fields the measurement fills |
| `cost_tier` | free_low, low, low_medium, medium, medium_high, low_high (rough; low under 25 USD, medium 25–100, high over 100) |
| `review_url` | Link to the comparison review, once written |

## Placement check (how the planner uses these fields)

1. **Site fit:** the plot's zone, frost dates and season length against `zone_min/max`, `frost_tolerance` and `days_to_maturity_max`. Cell sun hours against `sun_need`, and soil pH against `ph_min/max`.
2. **Time overlap:** only placements whose date spans overlap are compared.
3. **Space:** a conflict exists when the distance between two centers is less than `clear_radius_in(A) + footprint_radius_in(B)`, or the reverse.
4. **Neighbor rules:** antagonists or shared diseases closer than `min_distance_in` turn the ring red. Shade from a taller neighbor to the south turns a full-sun plant amber.

## Known gaps for phase two
- Every value is a typical range and needs checking against named sources. Set `verified` to true and fill in `sources` as each one is checked.
- No affliction photos yet. Photo licenses must be recorded before any image is used.
- Growth curve fields (days to 25%, 50% and 100% of height) are not yet included; the planner uses straight-line growth for now.
- Varieties (e.g. specific tomato cultivars) are not yet split out from plants.
