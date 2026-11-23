"""Builds the Planting Guide seed data.

Edit the tables in this file, then run:  python3 data/build_data.py
Outputs (in data/): plants.json, plants.csv, afflictions.json, pair_rules.json, tools.json

Values are typical ranges for home gardens drawn from common extension-service
guidance. Every plant carries verified=false until someone checks it against a
named source and records that source in `sources`.
"""
import csv
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent

# ---------------------------------------------------------------- plants
# Defaults: any field not given for a plant takes this value.
DEFAULTS = dict(
    scientific_name=None, family=None, category="vegetable",
    life_cycle="annual", zone_min=None, zone_max=None,
    frost_tolerance="tender", sun_need="full", photoperiod_type="neutral",
    ph_min=6.0, ph_max=7.0, soil_texture_pref="loam", drainage_need="well_drained",
    feeder_type="medium", n_fixer=False,
    start_method="transplant_ok", indoor_start_weeks_before_last_frost=None,
    outdoor_weeks_from_last_frost=0,
    germ_soil_temp_min_f=None, germ_soil_temp_opt_f=None,
    days_to_germination_min=None, days_to_germination_max=None,
    sow_depth_in=None, spacing_in=None, row_spacing_in=None, per_sq_ft=None,
    mature_height_in=None, mature_spread_in=None, root_depth_in=None,
    min_container_gal=None,
    water_need="medium", moisture_target="evenly_moist", critical_water_stages=[],
    pruning_type="none", support_type="none", climbing_method=None,
    days_to_maturity_min=None, days_to_maturity_max=None, maturity_from="seed",
    harvest_type="single", harvest_window_days=None,
    years_to_first_harvest=None, succession_interval_days=None, bolt_trigger=[],
    light_lux_min=None, light_lux_max=None, humidity_min_pct=None,
    temp_min_f=None, toxic_to_pets=None,
    afflictions=[], notes="",
    verified=False, sources=[],
)

P = []  # list of plant dicts


def plant(id, name, **kw):
    unknown = set(kw) - set(DEFAULTS)
    if unknown:
        raise KeyError(f"{id}: unknown fields {unknown}")
    rec = {"id": id, "common_name": name, **DEFAULTS, **kw}
    P.append(rec)


SOL, CUC, BRA, FAB = "Solanaceae", "Cucurbitaceae", "Brassicaceae", "Fabaceae"
API, AMA, ALL, LAM = "Apiaceae", "Amaranthaceae", "Amaryllidaceae", "Lamiaceae"

# --- Fruiting vegetables
plant("tomato_indeterminate", "Tomato (indeterminate)", scientific_name="Solanum lycopersicum", family=SOL,
      ph_min=6.2, ph_max=6.8, feeder_type="heavy", start_method="transplant_preferred",
      indoor_start_weeks_before_last_frost=7, outdoor_weeks_from_last_frost=2,
      germ_soil_temp_min_f=50, germ_soil_temp_opt_f=80, days_to_germination_min=5, days_to_germination_max=10,
      sow_depth_in=0.25, spacing_in=24, row_spacing_in=48, per_sq_ft=1,
      mature_height_in=72, mature_spread_in=24, root_depth_in=24, min_container_gal=15,
      water_need="high", critical_water_stages=["flowering", "fruit_set"],
      pruning_type="sucker_removal", support_type="stake_or_trellis", climbing_method="scrambling",
      days_to_maturity_min=70, days_to_maturity_max=85, maturity_from="transplant",
      harvest_type="repeat_continuous", harvest_window_days=60,
      afflictions=["early_blight", "late_blight", "blossom_end_rot", "tomato_hornworm", "aphids", "corn_earworm"],
      notes="Can be planted deep, up to the first true leaves; buried stem grows roots. Keeps fruiting until frost.")
plant("tomato_determinate", "Tomato (determinate)", scientific_name="Solanum lycopersicum", family=SOL,
      ph_min=6.2, ph_max=6.8, feeder_type="heavy", start_method="transplant_preferred",
      indoor_start_weeks_before_last_frost=7, outdoor_weeks_from_last_frost=2,
      germ_soil_temp_min_f=50, germ_soil_temp_opt_f=80, days_to_germination_min=5, days_to_germination_max=10,
      sow_depth_in=0.25, spacing_in=24, row_spacing_in=36, per_sq_ft=1,
      mature_height_in=48, mature_spread_in=24, root_depth_in=24, min_container_gal=7,
      water_need="high", critical_water_stages=["flowering", "fruit_set"],
      support_type="cage", climbing_method="scrambling",
      days_to_maturity_min=60, days_to_maturity_max=80, maturity_from="transplant",
      harvest_type="repeat_continuous", harvest_window_days=21,
      afflictions=["early_blight", "late_blight", "blossom_end_rot", "tomato_hornworm", "aphids"],
      notes="Sets most fruit at once; do not remove suckers. Good for containers and canning.")
plant("pepper_bell", "Pepper (bell)", scientific_name="Capsicum annuum", family=SOL,
      ph_min=6.0, ph_max=6.8, start_method="transplant_preferred",
      indoor_start_weeks_before_last_frost=9, outdoor_weeks_from_last_frost=2,
      germ_soil_temp_min_f=60, germ_soil_temp_opt_f=80, days_to_germination_min=7, days_to_germination_max=14,
      sow_depth_in=0.25, spacing_in=18, row_spacing_in=30, per_sq_ft=1,
      mature_height_in=30, mature_spread_in=18, root_depth_in=18, min_container_gal=5,
      critical_water_stages=["flowering", "fruit_set"], support_type="stake",
      days_to_maturity_min=60, days_to_maturity_max=90, maturity_from="transplant",
      harvest_type="repeat_continuous", harvest_window_days=60,
      afflictions=["aphids", "blossom_end_rot", "spider_mites"],
      notes="Needs warm nights; flowers drop below about 55 F or above 90 F.")
plant("eggplant", "Eggplant", scientific_name="Solanum melongena", family=SOL,
      ph_min=5.5, ph_max=7.0, feeder_type="heavy", start_method="transplant_preferred",
      indoor_start_weeks_before_last_frost=9, outdoor_weeks_from_last_frost=3,
      germ_soil_temp_min_f=60, germ_soil_temp_opt_f=80, days_to_germination_min=7, days_to_germination_max=14,
      sow_depth_in=0.25, spacing_in=24, row_spacing_in=36, per_sq_ft=1,
      mature_height_in=36, mature_spread_in=24, root_depth_in=18, min_container_gal=5,
      support_type="stake", days_to_maturity_min=65, days_to_maturity_max=80, maturity_from="transplant",
      harvest_type="repeat_continuous", harvest_window_days=45,
      afflictions=["flea_beetles", "colorado_potato_beetle", "spider_mites"],
      notes="Most heat-loving of the common nightshades; struggles in short, cool seasons.")
plant("corn_sweet", "Sweet corn", scientific_name="Zea mays", family="Poaceae",
      ph_min=5.8, ph_max=7.0, feeder_type="heavy", start_method="direct_sow_preferred",
      outdoor_weeks_from_last_frost=1,
      germ_soil_temp_min_f=55, germ_soil_temp_opt_f=85, days_to_germination_min=7, days_to_germination_max=10,
      sow_depth_in=1.5, spacing_in=12, row_spacing_in=30, per_sq_ft=1,
      mature_height_in=84, mature_spread_in=18, root_depth_in=48,
      water_need="high", critical_water_stages=["tasseling", "silking"],
      days_to_maturity_min=70, days_to_maturity_max=100,
      harvest_type="single", harvest_window_days=7,
      afflictions=["corn_earworm", "aphids"],
      notes="Wind pollinated: plant in blocks of at least 4 rows, not one long row. Supersweet types need soil near 65 F.")
plant("bean_bush", "Bean (bush)", scientific_name="Phaseolus vulgaris", family=FAB,
      feeder_type="light", n_fixer=True, start_method="direct_sow_only", outdoor_weeks_from_last_frost=1,
      germ_soil_temp_min_f=60, germ_soil_temp_opt_f=80, days_to_germination_min=7, days_to_germination_max=10,
      sow_depth_in=1, spacing_in=4, row_spacing_in=18, per_sq_ft=9,
      mature_height_in=20, mature_spread_in=12, root_depth_in=18, min_container_gal=2,
      critical_water_stages=["flowering", "pod_set"],
      days_to_maturity_min=50, days_to_maturity_max=60,
      harvest_type="repeat_continuous", harvest_window_days=21, succession_interval_days=21,
      afflictions=["mexican_bean_beetle", "aphids", "spider_mites", "slugs"],
      notes="Seeds rot in cold, wet soil. Pick often to keep pods coming.")
plant("bean_pole", "Bean (pole)", scientific_name="Phaseolus vulgaris", family=FAB,
      feeder_type="light", n_fixer=True, start_method="direct_sow_only", outdoor_weeks_from_last_frost=1,
      germ_soil_temp_min_f=60, germ_soil_temp_opt_f=80, days_to_germination_min=7, days_to_germination_max=10,
      sow_depth_in=1, spacing_in=6, row_spacing_in=30, per_sq_ft=8,
      mature_height_in=96, mature_spread_in=12, root_depth_in=18, min_container_gal=3,
      critical_water_stages=["flowering", "pod_set"], support_type="pole_or_trellis", climbing_method="twining",
      days_to_maturity_min=60, days_to_maturity_max=70,
      harvest_type="repeat_continuous", harvest_window_days=45,
      afflictions=["mexican_bean_beetle", "aphids", "spider_mites", "slugs"],
      notes="Twines around poles or corn stalks; thin netting is a poor fit.")
plant("pea", "Pea", scientific_name="Pisum sativum", family=FAB,
      frost_tolerance="hardy", ph_min=6.0, ph_max=7.5, feeder_type="light", n_fixer=True,
      start_method="direct_sow_only", outdoor_weeks_from_last_frost=-5,
      germ_soil_temp_min_f=40, germ_soil_temp_opt_f=75, days_to_germination_min=7, days_to_germination_max=14,
      sow_depth_in=1, spacing_in=2, row_spacing_in=18, per_sq_ft=8,
      mature_height_in=48, mature_spread_in=6, root_depth_in=18, min_container_gal=3,
      critical_water_stages=["flowering", "pod_set"], support_type="trellis_netting", climbing_method="tendrils",
      days_to_maturity_min=55, days_to_maturity_max=70,
      harvest_type="repeat_continuous", harvest_window_days=21, bolt_trigger=["heat"],
      afflictions=["powdery_mildew", "aphids"],
      notes="Stops producing once days are regularly above about 80 F. Tendrils need thin netting or string.")
plant("potato", "Potato", scientific_name="Solanum tuberosum", family=SOL,
      frost_tolerance="half_hardy", ph_min=5.0, ph_max=6.5, soil_texture_pref="sandy_loam", feeder_type="heavy",
      start_method="seed_piece", outdoor_weeks_from_last_frost=-2,
      germ_soil_temp_min_f=45, sow_depth_in=4, spacing_in=12, row_spacing_in=30, per_sq_ft=1,
      mature_height_in=24, mature_spread_in=18, root_depth_in=24, min_container_gal=10,
      critical_water_stages=["flowering", "tuber_set"],
      days_to_maturity_min=70, days_to_maturity_max=120, maturity_from="planting",
      harvest_type="single", harvest_window_days=30,
      afflictions=["early_blight", "late_blight", "colorado_potato_beetle", "flea_beetles"],
      notes="Hill soil over stems as they grow to keep tubers covered. Acid soil (below 6.0) reduces scab.")
# --- Cucurbits
plant("squash_summer", "Summer squash / zucchini", scientific_name="Cucurbita pepo", family=CUC,
      ph_min=6.0, ph_max=7.5, feeder_type="heavy", start_method="direct_sow_preferred", outdoor_weeks_from_last_frost=1,
      indoor_start_weeks_before_last_frost=3,
      germ_soil_temp_min_f=60, germ_soil_temp_opt_f=85, days_to_germination_min=5, days_to_germination_max=10,
      sow_depth_in=1, spacing_in=36, row_spacing_in=48,
      mature_height_in=30, mature_spread_in=48, root_depth_in=24, min_container_gal=10,
      water_need="high", critical_water_stages=["flowering", "fruit_set"],
      days_to_maturity_min=45, days_to_maturity_max=60,
      harvest_type="repeat_continuous", harvest_window_days=60,
      afflictions=["powdery_mildew", "squash_vine_borer", "squash_bugs", "cucumber_beetles"],
      notes="Pick at 6-8 in. Roots dislike disturbance; transplant only in peat or paper pots.")
plant("squash_winter", "Winter squash", scientific_name="Cucurbita maxima / moschata", family=CUC,
      ph_min=6.0, ph_max=7.5, feeder_type="heavy", start_method="direct_sow_preferred", outdoor_weeks_from_last_frost=1,
      indoor_start_weeks_before_last_frost=3,
      germ_soil_temp_min_f=60, germ_soil_temp_opt_f=85, days_to_germination_min=5, days_to_germination_max=10,
      sow_depth_in=1, spacing_in=48, row_spacing_in=72,
      mature_height_in=24, mature_spread_in=96, root_depth_in=36,
      water_need="high", critical_water_stages=["flowering", "fruit_set"], climbing_method="scrambling",
      days_to_maturity_min=85, days_to_maturity_max=110,
      harvest_type="single", harvest_window_days=14,
      afflictions=["powdery_mildew", "squash_vine_borer", "squash_bugs", "cucumber_beetles"],
      notes="The 'mulch' of the Three Sisters. Cure in a warm, dry spot for 10-14 days before storing.")
plant("cucumber", "Cucumber", scientific_name="Cucumis sativus", family=CUC,
      start_method="transplant_ok", indoor_start_weeks_before_last_frost=3, outdoor_weeks_from_last_frost=1,
      germ_soil_temp_min_f=60, germ_soil_temp_opt_f=85, days_to_germination_min=3, days_to_germination_max=10,
      sow_depth_in=1, spacing_in=12, row_spacing_in=36, per_sq_ft=2,
      mature_height_in=72, mature_spread_in=24, root_depth_in=24, min_container_gal=5,
      water_need="high", critical_water_stages=["flowering", "fruit_set"],
      support_type="trellis_vertical", climbing_method="tendrils",
      days_to_maturity_min=50, days_to_maturity_max=70,
      harvest_type="repeat_continuous", harvest_window_days=45,
      afflictions=["cucumber_beetles", "powdery_mildew", "downy_mildew", "spider_mites", "aphids"],
      notes="Spacing assumes a trellis; sprawling vines need about 36 in. Bitter fruit usually means water stress.")
# --- Leafy greens and brassicas
plant("lettuce", "Lettuce (leaf)", scientific_name="Lactuca sativa", family="Asteraceae",
      frost_tolerance="half_hardy", sun_need="part", feeder_type="light", moisture_target="evenly_moist",
      indoor_start_weeks_before_last_frost=5, outdoor_weeks_from_last_frost=-3,
      germ_soil_temp_min_f=40, germ_soil_temp_opt_f=70, days_to_germination_min=2, days_to_germination_max=10,
      sow_depth_in=0.125, spacing_in=8, row_spacing_in=12, per_sq_ft=4,
      mature_height_in=10, mature_spread_in=10, root_depth_in=12, min_container_gal=1,
      pruning_type="cut_and_come_again", days_to_maturity_min=30, days_to_maturity_max=60,
      harvest_type="repeat_continuous", harvest_window_days=30, succession_interval_days=14,
      bolt_trigger=["heat", "long_days"], afflictions=["aphids", "slugs"],
      notes="Seed needs light to germinate; barely cover. Seed goes dormant in soil above about 80 F. Tolerates shade in summer.")
plant("spinach", "Spinach", scientific_name="Spinacia oleracea", family=AMA,
      frost_tolerance="hardy", sun_need="part", ph_min=6.5, ph_max=7.5, start_method="direct_sow_preferred",
      outdoor_weeks_from_last_frost=-5, photoperiod_type="long_day_bolting",
      germ_soil_temp_min_f=35, germ_soil_temp_opt_f=70, days_to_germination_min=7, days_to_germination_max=14,
      sow_depth_in=0.5, spacing_in=4, row_spacing_in=12, per_sq_ft=9,
      mature_height_in=8, mature_spread_in=8, root_depth_in=12, min_container_gal=1,
      pruning_type="cut_and_come_again", days_to_maturity_min=40, days_to_maturity_max=50,
      harvest_type="repeat_continuous", harvest_window_days=30, succession_interval_days=14,
      bolt_trigger=["long_days", "heat"], afflictions=["slugs", "aphids", "downy_mildew"],
      notes="Bolts as days lengthen; in far-north summers, sow very early or in late summer for fall.")
plant("kale", "Kale", scientific_name="Brassica oleracea (Acephala)", family=BRA,
      frost_tolerance="hardy", ph_min=6.0, ph_max=7.5, feeder_type="heavy",
      indoor_start_weeks_before_last_frost=5, outdoor_weeks_from_last_frost=-3,
      germ_soil_temp_min_f=40, germ_soil_temp_opt_f=75, days_to_germination_min=5, days_to_germination_max=10,
      sow_depth_in=0.5, spacing_in=18, row_spacing_in=24, per_sq_ft=1,
      mature_height_in=24, mature_spread_in=18, root_depth_in=18, min_container_gal=5,
      pruning_type="cut_and_come_again", days_to_maturity_min=55, days_to_maturity_max=75, maturity_from="transplant",
      harvest_type="repeat_continuous", harvest_window_days=120,
      afflictions=["cabbage_worm", "aphids", "flea_beetles"],
      notes="Frost sweetens the leaves. Harvest lower leaves first and leave the growing tip.")
plant("cabbage", "Cabbage", scientific_name="Brassica oleracea (Capitata)", family=BRA,
      frost_tolerance="hardy", ph_min=6.5, ph_max=7.5, feeder_type="heavy",
      indoor_start_weeks_before_last_frost=6, outdoor_weeks_from_last_frost=-3,
      germ_soil_temp_min_f=40, germ_soil_temp_opt_f=75, days_to_germination_min=5, days_to_germination_max=10,
      sow_depth_in=0.5, spacing_in=18, row_spacing_in=30, per_sq_ft=1,
      mature_height_in=18, mature_spread_in=24, root_depth_in=18, min_container_gal=5,
      critical_water_stages=["head_formation"], days_to_maturity_min=60, days_to_maturity_max=100,
      maturity_from="transplant", harvest_type="single", harvest_window_days=14,
      afflictions=["cabbage_worm", "aphids", "flea_beetles", "slugs"],
      notes="Heads split if heavy rain follows dry spells; water evenly.")
plant("broccoli", "Broccoli", scientific_name="Brassica oleracea (Italica)", family=BRA,
      frost_tolerance="hardy", feeder_type="heavy",
      indoor_start_weeks_before_last_frost=6, outdoor_weeks_from_last_frost=-2,
      germ_soil_temp_min_f=40, germ_soil_temp_opt_f=75, days_to_germination_min=5, days_to_germination_max=10,
      sow_depth_in=0.5, spacing_in=18, row_spacing_in=30, per_sq_ft=1,
      mature_height_in=30, mature_spread_in=18, root_depth_in=18, min_container_gal=5,
      critical_water_stages=["head_formation"], days_to_maturity_min=55, days_to_maturity_max=80,
      maturity_from="transplant", harvest_type="repeat_continuous", harvest_window_days=30,
      bolt_trigger=["heat"], afflictions=["cabbage_worm", "aphids", "flea_beetles"],
      notes="Cut the main head before flowers open; side shoots follow for weeks.")
plant("chard", "Swiss chard", scientific_name="Beta vulgaris (Cicla)", family=AMA,
      frost_tolerance="hardy", sun_need="part", ph_min=6.0, ph_max=7.5,
      indoor_start_weeks_before_last_frost=4, outdoor_weeks_from_last_frost=-2,
      germ_soil_temp_min_f=40, germ_soil_temp_opt_f=75, days_to_germination_min=5, days_to_germination_max=14,
      sow_depth_in=0.5, spacing_in=9, row_spacing_in=18, per_sq_ft=4,
      mature_height_in=18, mature_spread_in=12, root_depth_in=18, min_container_gal=2,
      pruning_type="cut_and_come_again", days_to_maturity_min=50, days_to_maturity_max=60,
      harvest_type="repeat_continuous", harvest_window_days=120,
      afflictions=["slugs", "aphids"],
      notes="Each 'seed' is a cluster; thin to one seedling per spot.")
# --- Roots and alliums
plant("carrot", "Carrot", scientific_name="Daucus carota subsp. sativus", family=API,
      frost_tolerance="hardy", ph_min=6.0, ph_max=6.8, soil_texture_pref="sandy_loam", feeder_type="light",
      start_method="direct_sow_only", outdoor_weeks_from_last_frost=-3,
      germ_soil_temp_min_f=40, germ_soil_temp_opt_f=75, days_to_germination_min=10, days_to_germination_max=21,
      sow_depth_in=0.25, spacing_in=2, row_spacing_in=12, per_sq_ft=16,
      mature_height_in=12, mature_spread_in=4, root_depth_in=12, min_container_gal=2,
      critical_water_stages=["germination"], days_to_maturity_min=60, days_to_maturity_max=80,
      harvest_type="single", harvest_window_days=30, succession_interval_days=21,
      afflictions=["carrot_rust_fly", "aphids"],
      notes="Keep the surface moist until seedlings emerge. Rocky or compacted soil forks roots.")
plant("beet", "Beet", scientific_name="Beta vulgaris", family=AMA,
      frost_tolerance="hardy", ph_min=6.0, ph_max=7.5, start_method="direct_sow_preferred",
      outdoor_weeks_from_last_frost=-2,
      germ_soil_temp_min_f=40, germ_soil_temp_opt_f=75, days_to_germination_min=5, days_to_germination_max=14,
      sow_depth_in=0.5, spacing_in=3, row_spacing_in=12, per_sq_ft=9,
      mature_height_in=12, mature_spread_in=6, root_depth_in=18, min_container_gal=2,
      days_to_maturity_min=50, days_to_maturity_max=70,
      harvest_type="single", harvest_window_days=30, succession_interval_days=21,
      afflictions=["slugs", "aphids"],
      notes="Greens are edible. Seed clusters produce several seedlings; thin early.")
plant("radish", "Radish", scientific_name="Raphanus sativus", family=BRA,
      frost_tolerance="hardy", feeder_type="light", start_method="direct_sow_only",
      outdoor_weeks_from_last_frost=-4,
      germ_soil_temp_min_f=40, germ_soil_temp_opt_f=70, days_to_germination_min=3, days_to_germination_max=7,
      sow_depth_in=0.5, spacing_in=2, row_spacing_in=6, per_sq_ft=16,
      mature_height_in=6, mature_spread_in=3, root_depth_in=6, min_container_gal=1,
      days_to_maturity_min=22, days_to_maturity_max=30,
      harvest_type="single", harvest_window_days=7, succession_interval_days=10,
      bolt_trigger=["heat", "long_days"], afflictions=["flea_beetles"],
      notes="Fastest crop in the garden; useful as a row marker sown with slow carrots.")
plant("onion", "Onion (bulb)", scientific_name="Allium cepa", family=ALL,
      frost_tolerance="hardy", photoperiod_type="long_short_or_intermediate_day",
      start_method="transplant_preferred", indoor_start_weeks_before_last_frost=11,
      outdoor_weeks_from_last_frost=-4,
      germ_soil_temp_min_f=50, germ_soil_temp_opt_f=75, days_to_germination_min=7, days_to_germination_max=14,
      sow_depth_in=0.5, spacing_in=4, row_spacing_in=12, per_sq_ft=9,
      mature_height_in=18, mature_spread_in=4, root_depth_in=12, min_container_gal=2,
      critical_water_stages=["bulbing"], days_to_maturity_min=90, days_to_maturity_max=120,
      maturity_from="transplant", harvest_type="single", harvest_window_days=21,
      afflictions=["thrips"],
      notes="Bulbing is set by day length: grow long-day types in the north (above about 37 N), short-day in the south. Stop watering when tops fall over.")
plant("garlic", "Garlic", scientific_name="Allium sativum", family=ALL,
      life_cycle="perennial_grown_as_annual", frost_tolerance="hardy",
      start_method="clove", outdoor_weeks_from_last_frost=None,
      sow_depth_in=2, spacing_in=6, row_spacing_in=12, per_sq_ft=4,
      mature_height_in=24, mature_spread_in=6, root_depth_in=12, min_container_gal=3,
      critical_water_stages=["bulbing"], days_to_maturity_min=240, days_to_maturity_max=270,
      maturity_from="fall_planting", harvest_type="single", harvest_window_days=14,
      afflictions=["thrips"],
      notes="Plant cloves in fall, about 4-6 weeks before the ground freezes; mulch over winter. Harvest when lower third of leaves brown.")
# --- Perennial vegetables
plant("asparagus", "Asparagus", scientific_name="Asparagus officinalis", family="Asparagaceae",
      life_cycle="perennial", zone_min=3, zone_max=8, frost_tolerance="hardy",
      ph_min=6.5, ph_max=7.5, feeder_type="heavy", start_method="crown",
      outdoor_weeks_from_last_frost=-2, sow_depth_in=6, spacing_in=18, row_spacing_in=48,
      mature_height_in=60, mature_spread_in=24, root_depth_in=48,
      pruning_type="dormant_cutback", harvest_type="repeat_seasonal", harvest_window_days=42,
      years_to_first_harvest=3, afflictions=["asparagus_beetle"],
      notes="Light harvest in year 2, full harvest from year 3; a bed can produce for 15-20 years. Leave summer ferns to feed the crowns.")
plant("rhubarb", "Rhubarb", scientific_name="Rheum rhabarbarum", family="Polygonaceae",
      life_cycle="perennial", zone_min=3, zone_max=8, frost_tolerance="hardy", sun_need="full_or_part",
      ph_min=6.0, ph_max=6.8, feeder_type="heavy", start_method="crown",
      outdoor_weeks_from_last_frost=-2, sow_depth_in=2, spacing_in=36, row_spacing_in=48,
      mature_height_in=36, mature_spread_in=48, root_depth_in=24,
      pruning_type="deadhead", harvest_type="repeat_seasonal", harvest_window_days=56,
      years_to_first_harvest=2, afflictions=["slugs"], toxic_to_pets=True,
      notes="Needs winter cold; thrives in Alaska. Leaves are toxic; eat stalks only. Remove flower stalks.")
# --- Herbs
plant("basil", "Basil", scientific_name="Ocimum basilicum", family=LAM, category="herb",
      start_method="transplant_preferred", indoor_start_weeks_before_last_frost=6, outdoor_weeks_from_last_frost=2,
      germ_soil_temp_min_f=65, germ_soil_temp_opt_f=75, days_to_germination_min=5, days_to_germination_max=10,
      sow_depth_in=0.125, spacing_in=10, row_spacing_in=18, per_sq_ft=2,
      mature_height_in=18, mature_spread_in=12, root_depth_in=12, min_container_gal=1,
      pruning_type="pinch_tips", days_to_maturity_min=50, days_to_maturity_max=75,
      harvest_type="repeat_continuous", harvest_window_days=90, bolt_trigger=["heat"],
      afflictions=["aphids", "downy_mildew", "slugs"],
      notes="Blackens below about 50 F. Pinch flower buds to keep leaves coming.")
plant("cilantro", "Cilantro", scientific_name="Coriandrum sativum", family=API, category="herb",
      frost_tolerance="half_hardy", sun_need="full_or_part", ph_min=6.2, ph_max=6.8,
      start_method="direct_sow_preferred", outdoor_weeks_from_last_frost=-1,
      germ_soil_temp_min_f=55, germ_soil_temp_opt_f=65, days_to_germination_min=7, days_to_germination_max=14,
      sow_depth_in=0.25, spacing_in=6, row_spacing_in=12, per_sq_ft=9,
      mature_height_in=18, mature_spread_in=6, root_depth_in=12, min_container_gal=1,
      pruning_type="cut_and_come_again", days_to_maturity_min=45, days_to_maturity_max=70,
      harvest_type="repeat_continuous", harvest_window_days=21, succession_interval_days=21,
      bolt_trigger=["heat", "long_days"], afflictions=["aphids"],
      notes="Bolts fast in heat; seeds are coriander.")
plant("parsley", "Parsley", scientific_name="Petroselinum crispum", family=API, category="herb",
      life_cycle="biennial", frost_tolerance="hardy", sun_need="full_or_part",
      indoor_start_weeks_before_last_frost=9, outdoor_weeks_from_last_frost=-2,
      germ_soil_temp_min_f=50, germ_soil_temp_opt_f=75, days_to_germination_min=14, days_to_germination_max=28,
      sow_depth_in=0.25, spacing_in=8, row_spacing_in=12, per_sq_ft=4,
      mature_height_in=12, mature_spread_in=12, root_depth_in=12, min_container_gal=1,
      pruning_type="cut_and_come_again", days_to_maturity_min=70, days_to_maturity_max=90,
      harvest_type="repeat_continuous", harvest_window_days=120,
      afflictions=["aphids"],
      notes="Slow to sprout; soak seed overnight. Host plant for swallowtail caterpillars. Flowers and dies in year 2.")
plant("dill", "Dill", scientific_name="Anethum graveolens", family=API, category="herb",
      frost_tolerance="half_hardy", ph_min=5.5, ph_max=6.5, start_method="direct_sow_preferred",
      outdoor_weeks_from_last_frost=0,
      germ_soil_temp_min_f=60, germ_soil_temp_opt_f=70, days_to_germination_min=7, days_to_germination_max=21,
      sow_depth_in=0.25, spacing_in=12, row_spacing_in=18, per_sq_ft=1,
      mature_height_in=36, mature_spread_in=12, root_depth_in=18, min_container_gal=2,
      pruning_type="cut_and_come_again", support_type="stake",
      days_to_maturity_min=40, days_to_maturity_max=60,
      harvest_type="repeat_continuous", harvest_window_days=30, succession_interval_days=21,
      bolt_trigger=["heat"], afflictions=["aphids"],
      notes="Flowers attract beneficial wasps and hoverflies. Self-seeds freely.")
plant("chives", "Chives", scientific_name="Allium schoenoprasum", family=ALL, category="herb",
      life_cycle="perennial", zone_min=3, zone_max=9, frost_tolerance="hardy", sun_need="full_or_part",
      start_method="transplant_or_division", indoor_start_weeks_before_last_frost=7, outdoor_weeks_from_last_frost=-3,
      germ_soil_temp_min_f=60, germ_soil_temp_opt_f=70, days_to_germination_min=7, days_to_germination_max=14,
      sow_depth_in=0.25, spacing_in=6, row_spacing_in=12, per_sq_ft=9,
      mature_height_in=12, mature_spread_in=8, root_depth_in=8, min_container_gal=1,
      pruning_type="cut_and_come_again", days_to_maturity_min=75, days_to_maturity_max=90,
      harvest_type="repeat_seasonal", harvest_window_days=150, years_to_first_harvest=1,
      afflictions=["thrips"],
      notes="Divide clumps every 3-4 years. Flowers are edible.")
plant("mint", "Mint", scientific_name="Mentha spp.", family=LAM, category="herb",
      life_cycle="perennial", zone_min=3, zone_max=8, frost_tolerance="hardy", sun_need="full_or_part",
      drainage_need="moist", start_method="cutting_or_division",
      spacing_in=18, per_sq_ft=1, mature_height_in=18, mature_spread_in=24, root_depth_in=12, min_container_gal=2,
      water_need="high", pruning_type="pinch_tips", harvest_type="repeat_seasonal", harvest_window_days=120,
      years_to_first_harvest=1, afflictions=["spider_mites", "aphids"],
      notes="Spreads by runners and takes over beds; grow in a container or a sunken pot.")
plant("thyme", "Thyme", scientific_name="Thymus vulgaris", family=LAM, category="herb",
      life_cycle="perennial", zone_min=5, zone_max=9, frost_tolerance="hardy",
      ph_min=6.0, ph_max=8.0, soil_texture_pref="sandy", drainage_need="dry", feeder_type="light",
      start_method="transplant_or_cutting", indoor_start_weeks_before_last_frost=8, outdoor_weeks_from_last_frost=0,
      germ_soil_temp_min_f=60, germ_soil_temp_opt_f=70, days_to_germination_min=14, days_to_germination_max=28,
      sow_depth_in=0, spacing_in=12, per_sq_ft=4,
      mature_height_in=10, mature_spread_in=12, root_depth_in=8, min_container_gal=1,
      water_need="low", moisture_target="dry_out_between", pruning_type="shear_after_flowering",
      harvest_type="repeat_seasonal", harvest_window_days=150, years_to_first_harvest=1,
      afflictions=["root_rot", "spider_mites"],
      notes="Wet winter soil kills it faster than cold. Surface sow; seed needs light.")
# --- Fruit
plant("strawberry", "Strawberry", scientific_name="Fragaria x ananassa", family="Rosaceae", category="fruit",
      life_cycle="perennial", zone_min=3, zone_max=9, frost_tolerance="hardy", ph_min=5.5, ph_max=6.8,
      start_method="crown", outdoor_weeks_from_last_frost=-2, sow_depth_in=0,
      spacing_in=18, row_spacing_in=36, per_sq_ft=1,
      mature_height_in=8, mature_spread_in=18, root_depth_in=12, min_container_gal=1,
      critical_water_stages=["flowering", "fruiting"], pruning_type="runner_removal",
      harvest_type="repeat_seasonal", harvest_window_days=21, years_to_first_harvest=1,
      afflictions=["slugs", "gray_mold", "spider_mites", "aphids"],
      notes="Set the crown exactly at soil level. June-bearers fruit once; everbearers fruit in waves. Replant every 3-4 years.")
plant("raspberry", "Raspberry", scientific_name="Rubus idaeus", family="Rosaceae", category="fruit",
      life_cycle="perennial", zone_min=3, zone_max=8, frost_tolerance="hardy", ph_min=5.5, ph_max=6.5,
      start_method="bare_root_cane", outdoor_weeks_from_last_frost=-2,
      spacing_in=24, row_spacing_in=72,
      mature_height_in=60, mature_spread_in=24, root_depth_in=18,
      critical_water_stages=["fruiting"], pruning_type="renewal", support_type="trellis_wire",
      harvest_type="repeat_seasonal", harvest_window_days=30, years_to_first_harvest=2,
      afflictions=["japanese_beetle", "spider_mites", "gray_mold"],
      notes="Spreads by suckers; keep rows 12-18 in wide. Avoid sites where tomatoes or potatoes grew (verticillium wilt).")
plant("blueberry", "Blueberry (highbush)", scientific_name="Vaccinium corymbosum", family="Ericaceae", category="fruit",
      life_cycle="perennial", zone_min=4, zone_max=7, frost_tolerance="hardy",
      ph_min=4.5, ph_max=5.5, soil_texture_pref="sandy_acidic", feeder_type="light",
      start_method="potted_shrub", outdoor_weeks_from_last_frost=-2,
      spacing_in=60, row_spacing_in=96, mature_height_in=72, mature_spread_in=60, root_depth_in=18,
      min_container_gal=20, critical_water_stages=["fruiting"], pruning_type="renewal",
      harvest_type="repeat_seasonal", harvest_window_days=30, years_to_first_harvest=3,
      afflictions=["japanese_beetle"],
      notes="Fails in neutral soil: test pH before planting. Plant two varieties for better pollination. Half-high types suit zone 3.")
# --- Companion flowers
plant("marigold_french", "Marigold (French)", scientific_name="Tagetes patula", family="Asteraceae", category="flower",
      start_method="transplant_ok", indoor_start_weeks_before_last_frost=6, outdoor_weeks_from_last_frost=1,
      germ_soil_temp_min_f=65, germ_soil_temp_opt_f=75, days_to_germination_min=4, days_to_germination_max=14,
      sow_depth_in=0.25, spacing_in=10, per_sq_ft=2,
      mature_height_in=12, mature_spread_in=10, root_depth_in=12, min_container_gal=1,
      water_need="low", moisture_target="dry_top_inch", pruning_type="deadhead",
      days_to_maturity_min=45, days_to_maturity_max=60, harvest_type="repeat_continuous",
      afflictions=["spider_mites", "slugs"],
      notes="Grown densely as a cover crop, roots suppress root-knot nematodes; a few scattered plants do much less.")
plant("nasturtium", "Nasturtium", scientific_name="Tropaeolum majus", family="Tropaeolaceae", category="flower",
      ph_min=6.1, ph_max=7.8, feeder_type="light", start_method="direct_sow_preferred", outdoor_weeks_from_last_frost=1,
      germ_soil_temp_min_f=55, germ_soil_temp_opt_f=65, days_to_germination_min=7, days_to_germination_max=12,
      sow_depth_in=0.5, spacing_in=10, per_sq_ft=1,
      mature_height_in=12, mature_spread_in=18, root_depth_in=12, min_container_gal=1,
      water_need="low", moisture_target="dry_top_inch",
      days_to_maturity_min=35, days_to_maturity_max=52, harvest_type="repeat_continuous",
      afflictions=["aphids"],
      notes="Flowers best in lean soil; rich soil gives leaves, few blooms. Flowers and leaves are edible. Often used as an aphid trap crop.")
# --- Houseplants (indoor values; zone = where it can live outdoors year-round)
HP = dict(category="houseplant", life_cycle="perennial", zone_min=10, zone_max=12, sun_need="indirect",
          start_method="cutting_or_division", outdoor_weeks_from_last_frost=None, feeder_type="light",
          soil_texture_pref="potting_mix")
plant("pothos", "Pothos", scientific_name="Epipremnum aureum", family="Araceae", **HP,
      light_lux_min=500, light_lux_max=10000, humidity_min_pct=40, temp_min_f=55, toxic_to_pets=True,
      moisture_target="dry_top_2in", mature_height_in=120, mature_spread_in=24, min_container_gal=1,
      pruning_type="pinch_tips", support_type="moss_pole_optional", climbing_method="aerial_roots",
      afflictions=["mealybugs", "root_rot", "fungus_gnats", "spider_mites"],
      notes="Tolerates low light but variegation fades. Trails or climbs.")
plant("snake_plant", "Snake plant", scientific_name="Dracaena trifasciata", family="Asparagaceae", **{**HP, "zone_min": 9, "zone_max": 11},
      light_lux_min=500, light_lux_max=20000, humidity_min_pct=30, temp_min_f=50, toxic_to_pets=True,
      water_need="low", moisture_target="dry_out_between", drainage_need="dry",
      mature_height_in=36, mature_spread_in=12, min_container_gal=1,
      afflictions=["root_rot", "mealybugs"],
      notes="Overwatering is the usual cause of death; water every 2-6 weeks depending on light.")
plant("monstera", "Monstera", scientific_name="Monstera deliciosa", family="Araceae", **HP,
      light_lux_min=5000, light_lux_max=20000, humidity_min_pct=50, temp_min_f=60, toxic_to_pets=True,
      moisture_target="dry_top_2in", mature_height_in=96, mature_spread_in=48, min_container_gal=5,
      support_type="moss_pole", climbing_method="aerial_roots",
      afflictions=["spider_mites", "mealybugs", "thrips", "root_rot"],
      notes="Leaf splits (fenestrations) need bright indirect light and a mature plant.")
plant("peace_lily", "Peace lily", scientific_name="Spathiphyllum spp.", family="Araceae", **{**HP, "zone_min": 11},
      light_lux_min=1000, light_lux_max=10000, humidity_min_pct=50, temp_min_f=60, toxic_to_pets=True,
      water_need="high", moisture_target="evenly_moist", mature_height_in=24, mature_spread_in=24, min_container_gal=2,
      pruning_type="deadhead", afflictions=["fungus_gnats", "mealybugs", "root_rot"],
      notes="Droops visibly when thirsty and recovers within hours of watering.")
plant("spider_plant", "Spider plant", scientific_name="Chlorophytum comosum", family="Asparagaceae", **{**HP, "zone_min": 9, "zone_max": 11},
      light_lux_min=2000, light_lux_max=15000, humidity_min_pct=40, temp_min_f=50, toxic_to_pets=False,
      moisture_target="dry_top_inch", mature_height_in=12, mature_spread_in=24, min_container_gal=1,
      afflictions=["spider_mites", "root_rot"],
      notes="Brown tips often come from fluoride or salts in tap water. Plantlets root easily.")

# ---------------------------------------------------------------- afflictions
# id: (name, type, early, mid, late, favoring_conditions, prevention)
AFF = {
 "aphids": ("Aphids", "insect", "A few soft green or black insects under new leaves", "Curled, sticky leaves; ants visiting", "Stunted tips; black sooty mold", "Lush new growth from excess nitrogen; few predators", "Blast off with water; encourage lady beetles; insecticidal soap"),
 "early_blight": ("Early blight", "fungus", "Small brown spots on lower leaves", "Target-like rings with yellow halos", "Lower leaves dead; stem lesions; sunscalded fruit", "Warm, humid weather; splashing soil", "Mulch, water at the base, remove lower leaves, rotate crops 3 years"),
 "late_blight": ("Late blight", "oomycete", "Pale green, water-soaked patches", "Dark lesions with white fuzz underneath", "Whole plant collapses within days; brown greasy fruit", "Cool, wet weather with high humidity", "Resistant varieties; remove infected plants at once; do not compost them"),
 "powdery_mildew": ("Powdery mildew", "fungus", "White dusty spots on upper leaves", "Whole leaves coated", "Leaves yellow and die; yield drops", "Dry leaves with humid nights; crowding; shade", "Space for airflow; resistant varieties; remove worst leaves"),
 "downy_mildew": ("Downy mildew", "oomycete", "Pale yellow patches between leaf veins", "Gray or purple fuzz on leaf undersides", "Leaves brown and collapse", "Cool, wet, humid weather; wet leaves overnight", "Water in the morning at the base; resistant varieties; airflow"),
 "cabbage_worm": ("Imported cabbage worm and loopers", "insect", "White butterflies; tiny yellow eggs under leaves", "Ragged holes; green droppings", "Leaves skeletonized; heads tunneled", "Brassicas grown uncovered in summer", "Floating row cover from planting; hand-pick; Bt"),
 "squash_vine_borer": ("Squash vine borer", "insect", "Orange-and-black moth; eggs at stem base", "Sawdust-like frass at stem base; midday wilting", "Vine collapses", "Early summer moth flight", "Row cover until flowering; wrap stem bases; plant resistant C. moschata"),
 "squash_bugs": ("Squash bugs", "insect", "Bronze egg clusters on leaf undersides", "Gray nymphs in groups; yellow speckled leaves", "Leaves wilt and blacken", "Debris and mulch for shelter", "Crush egg clusters; board traps; clean up debris"),
 "cucumber_beetles": ("Cucumber beetles", "insect", "Yellow beetles with black stripes or spots on seedlings", "Holes in leaves and flowers; scarred fruit", "Bacterial wilt: vines wilt and do not recover", "Young cucurbit seedlings in spring", "Row cover until flowering; yellow sticky traps; remove wilted vines"),
 "blossom_end_rot": ("Blossom end rot", "disorder", "Small water-soaked spot at fruit bottom", "Spot turns brown and leathery", "Large sunken black patch; mold may follow", "Uneven watering limits calcium uptake", "Water deeply and evenly; mulch; test soil before adding calcium"),
 "fungus_gnats": ("Fungus gnats", "insect", "Tiny dark flies over wet potting mix", "Larvae in top inch of mix", "Seedling roots damaged; damping off", "Constantly wet potting mix", "Let the top inch dry; yellow sticky traps; bottom-water"),
 "spider_mites": ("Spider mites", "mite", "Fine pale speckling on leaves", "Fine webbing at leaf joints", "Bronzed, dry leaves drop", "Hot, dry air; dusty leaves", "Raise humidity; rinse leaves; insecticidal soap or predatory mites"),
 "slugs": ("Slugs and snails", "mollusk", "Slime trails", "Irregular holes with smooth edges", "Seedlings eaten to the ground", "Damp, shady beds; mulch; mild nights", "Hand-pick at night; beer or board traps; iron phosphate bait"),
 "tomato_hornworm": ("Tomato hornworm", "insect", "Dark droppings on leaves below", "Stripped leaves and stems at the top", "Plant defoliated; fruit chewed", "Mid to late summer", "Hand-pick; leave ones carrying white wasp cocoons"),
 "flea_beetles": ("Flea beetles", "insect", "Tiny shiny beetles that jump when disturbed", "Many shot holes in leaves", "Seedlings stunted or killed", "Warm, dry spring weather; young seedlings", "Row cover at planting; transplant larger seedlings"),
 "colorado_potato_beetle": ("Colorado potato beetle", "insect", "Yellow-orange egg clusters under leaves", "Red humpbacked larvae feeding", "Plants defoliated", "Fields with potatoes or eggplant last year", "Rotate; hand-pick adults and eggs; straw mulch"),
 "corn_earworm": ("Corn earworm (tomato fruitworm)", "insect", "Eggs on fresh silks", "Damaged silks; frass at ear tips", "Kernels at ear tip eaten; holes in tomatoes", "Mid to late summer", "Drop mineral oil on silks after they wilt; tight-husked varieties"),
 "carrot_rust_fly": ("Carrot rust fly", "insect", "Small flies near carrot tops", "Rust-colored tunnels in roots", "Roots rot; tops yellow", "Sowings that come up in late spring", "Row cover; delay sowing until after first flight"),
 "mexican_bean_beetle": ("Mexican bean beetle", "insect", "Yellow egg clusters under leaves", "Spiny yellow larvae; lacy leaves", "Leaves skeletonized", "Midsummer", "Hand-pick; row cover; succession sowing"),
 "asparagus_beetle": ("Asparagus beetle", "insect", "Dark eggs standing on spears", "Chewed, scarred spears", "Ferns stripped", "Spring through summer", "Hand-pick; harvest promptly; clean up ferns in fall"),
 "japanese_beetle": ("Japanese beetle", "insect", "Shiny green-and-copper beetles", "Lacy leaves eaten between veins", "Plants defoliated", "Midsummer; eastern and central US", "Hand-pick into soapy water in the morning; do not use lure traps near plants"),
 "gray_mold": ("Gray mold (Botrytis)", "fungus", "Soft brown spots on flowers or fruit", "Gray fuzzy growth", "Fruit rots on the plant", "Cool, wet weather; crowding", "Airflow; mulch so fruit sits off the soil; remove infected fruit"),
 "thrips": ("Thrips", "insect", "Silvery streaks on leaves", "Black specks of droppings", "Distorted leaves and flowers", "Hot, dry weather; indoors year-round", "Blue sticky traps; rinse leaves; insecticidal soap"),
 "mealybugs": ("Mealybugs", "insect", "White cottony spots in leaf joints", "Sticky honeydew; slowed growth", "Yellowing; leaf drop", "Indoor plants; new plants brought home", "Isolate new plants; wipe with rubbing alcohol on a swab"),
 "root_rot": ("Root rot", "fungus", "Soil stays wet for days; lower leaves yellow", "Wilting even when soil is wet", "Roots brown and mushy; stems collapse", "Overwatering; pots without drainage; heavy soil", "Pots with drainage holes; water only when the top inch is dry"),
}

# ---------------------------------------------------------------- pair rules
# (a, b, relation, reason, evidence, min_distance_in)
# relation: companion | antagonist | shared_disease | guild
RULES = [
 ("corn_sweet", "bean_pole", "guild", "support", "traditional", None),
 ("corn_sweet", "squash_winter", "guild", "living_mulch", "traditional", None),
 ("bean_pole", "squash_winter", "guild", "nitrogen", "traditional", None),
 ("tomato_indeterminate", "basil", "companion", "space_use_and_pollinators", "anecdotal", None),
 ("tomato_determinate", "basil", "companion", "space_use_and_pollinators", "anecdotal", None),
 ("tomato_indeterminate", "potato", "shared_disease", "late_blight", "tested", 120),
 ("tomato_determinate", "potato", "shared_disease", "late_blight", "tested", 120),
 ("tomato_indeterminate", "corn_sweet", "shared_disease", "corn_earworm", "tested", 48),
 ("tomato_indeterminate", "marigold_french", "companion", "nematode_suppression", "tested", None),
 ("tomato_determinate", "marigold_french", "companion", "nematode_suppression", "tested", None),
 ("potato", "marigold_french", "companion", "nematode_suppression", "tested", None),
 ("raspberry", "tomato_indeterminate", "shared_disease", "verticillium_wilt", "tested", 120),
 ("raspberry", "potato", "shared_disease", "verticillium_wilt", "tested", 120),
 ("bean_bush", "onion", "antagonist", "growth_inhibition", "traditional", 24),
 ("bean_bush", "garlic", "antagonist", "growth_inhibition", "traditional", 24),
 ("bean_bush", "chives", "antagonist", "growth_inhibition", "traditional", 24),
 ("bean_pole", "onion", "antagonist", "growth_inhibition", "traditional", 24),
 ("bean_pole", "garlic", "antagonist", "growth_inhibition", "traditional", 24),
 ("pea", "onion", "antagonist", "growth_inhibition", "traditional", 24),
 ("pea", "garlic", "antagonist", "growth_inhibition", "traditional", 24),
 ("pea", "carrot", "companion", "space_use", "traditional", None),
 ("pea", "radish", "companion", "space_use", "traditional", None),
 ("pea", "spinach", "companion", "shade_provider", "traditional", None),
 ("carrot", "onion", "companion", "pest_confusion", "traditional", None),
 ("carrot", "radish", "companion", "row_marker", "traditional", None),
 ("carrot", "lettuce", "companion", "space_use", "traditional", None),
 ("carrot", "dill", "antagonist", "cross_pollination_and_shared_pests", "anecdotal", 24),
 ("lettuce", "radish", "companion", "space_use", "traditional", None),
 ("lettuce", "corn_sweet", "companion", "shade_provider", "traditional", None),
 ("cucumber", "dill", "companion", "beneficial_insects", "traditional", None),
 ("cucumber", "nasturtium", "companion", "trap_crop", "anecdotal", None),
 ("cucumber", "radish", "companion", "pest_deter", "anecdotal", None),
 ("squash_summer", "nasturtium", "companion", "trap_crop", "anecdotal", None),
 ("cabbage", "dill", "companion", "beneficial_insects", "traditional", None),
 ("kale", "dill", "companion", "beneficial_insects", "traditional", None),
 ("broccoli", "dill", "companion", "beneficial_insects", "traditional", None),
 ("cabbage", "onion", "companion", "pest_confusion", "anecdotal", None),
 ("kale", "nasturtium", "companion", "trap_crop", "anecdotal", None),
 ("pepper_bell", "basil", "companion", "space_use_and_pollinators", "anecdotal", None),
 ("pepper_bell", "onion", "companion", "pest_confusion", "anecdotal", None),
 ("asparagus", "parsley", "companion", "space_use", "traditional", None),
 ("asparagus", "tomato_indeterminate", "companion", "pest_deter", "anecdotal", None),
 ("strawberry", "spinach", "companion", "space_use", "traditional", None),
 ("beet", "onion", "companion", "space_use", "traditional", None),
 ("beet", "bean_pole", "antagonist", "growth_inhibition", "anecdotal", 24),
 ("chives", "carrot", "companion", "pest_confusion", "anecdotal", None),
 ("potato", "bean_bush", "companion", "space_use", "traditional", None),
 ("mint", "cabbage", "companion", "pest_deter", "anecdotal", None),
]

# ---------------------------------------------------------------- tools
TOOLS = [
 ("soil_moisture_meter", "Soil moisture meter", "Water in the root zone", "1-10 scale or % VWC", ["moisture_reading"], "Houseplants, containers", "low"),
 ("hygrometer", "Hygrometer", "Air humidity and temperature", "% RH, F", ["room_humidity"], "Tropical houseplants, seed starting", "low"),
 ("soil_thermometer", "Soil thermometer", "Soil temperature at seed depth", "F", ["soil_temp"], "Direct sowing; Three Sisters timing", "low"),
 ("min_max_thermometer", "Min/max thermometer", "Coldest and hottest temperatures since reset", "F", ["microclimate_low", "microclimate_high"], "Frost pockets, greenhouses", "low"),
 ("ph_meter", "Soil pH meter or strips", "Acidity or alkalinity", "pH", ["soil_ph"], "Blueberries, brassicas, new beds", "low_medium"),
 ("npk_test_kit", "Soil test kit (NPK)", "Nitrogen, phosphorus, potassium", "low/medium/high", ["soil_n", "soil_p", "soil_k"], "Heavy feeders, poor yields", "low"),
 ("lab_soil_test", "Lab soil test", "pH, nutrients, organic matter, lead", "ppm, %", ["soil_ph", "soil_n", "soil_p", "soil_k", "soil_om", "soil_lead"], "New gardens, urban soil", "medium"),
 ("ec_meter", "EC / TDS meter", "Salts and fertilizer strength", "dS/m or ppm", ["soil_ec"], "Containers, hydroponics", "medium"),
 ("light_meter", "Light meter (lux or PAR)", "Light intensity", "lux, umol/m2/s", ["light_reading"], "Houseplants, grow lights, shady beds", "low_high"),
 ("sun_calculator", "Sun path / sun calculator app", "Hours of direct sun by date", "hours", ["sun_hours"], "Bed layout and shade", "free_low"),
 ("rain_gauge", "Rain gauge", "Rainfall", "in", ["rainfall_week"], "Deciding whether to water", "low"),
 ("penetrometer", "Penetrometer", "Soil compaction", "psi", ["compaction"], "Clay soils, new yards", "medium"),
 ("refractometer", "Refractometer", "Sugar in fruit or sap", "Brix", ["brix"], "Harvest timing", "medium"),
 ("hand_lens", "Hand lens (10x-30x)", "Close-up view of pests and spores", "none", ["affliction_observation"], "Early pest ID", "low"),
 ("sticky_traps", "Yellow and blue sticky traps", "Flying pest counts", "count per week", ["pest_count"], "Gnats, whiteflies, thrips", "low"),
 ("smart_sensor", "Smart sensor / weather station", "Continuous moisture, temperature, light, humidity", "logged series", ["moisture_reading", "soil_temp", "light_reading", "room_humidity"], "Automatic reminders", "medium_high"),
]


def main():
    ids = {p["id"] for p in P}
    assert len(ids) == len(P), "duplicate plant ids"
    for p in P:
        for a in p["afflictions"]:
            assert a in AFF, f"{p['id']}: unknown affliction {a}"
    rules = []
    for a, b, rel, reason, ev, dist in RULES:
        assert a in ids and b in ids, f"rule {a}-{b}: unknown plant"
        rules.append(dict(plant_a=a, plant_b=b, relation=rel, reason=reason,
                          evidence=ev, min_distance_in=dist))
    # Derived per-plant lists, so the app can read one record
    for p in P:
        p["companions"] = sorted({r["plant_b"] if r["plant_a"] == p["id"] else r["plant_a"]
                                  for r in rules if p["id"] in (r["plant_a"], r["plant_b"])
                                  and r["relation"] in ("companion", "guild")})
        p["antagonists"] = sorted({r["plant_b"] if r["plant_a"] == p["id"] else r["plant_a"]
                                   for r in rules if p["id"] in (r["plant_a"], r["plant_b"])
                                   and r["relation"] in ("antagonist", "shared_disease")})
        # Placement-ring radii (inches) used by the planner
        p["clear_radius_in"] = p["spacing_in"] / 2 if p["spacing_in"] else None
        p["footprint_radius_in"] = p["mature_spread_in"] / 2 if p["mature_spread_in"] else None

    afflictions = []
    for aid, (name, typ, e, m, l, fav, prev) in AFF.items():
        afflictions.append(dict(
            id=aid, name=name, type=typ,
            hosts=sorted(p["id"] for p in P if aid in p["afflictions"]),
            stages=[dict(stage="early", symptoms=e, photo=None, photo_credit=None, photo_license=None),
                    dict(stage="mid", symptoms=m, photo=None, photo_credit=None, photo_license=None),
                    dict(stage="late", symptoms=l, photo=None, photo_credit=None, photo_license=None)],
            favoring_conditions=fav, prevention=prev, verified=False, sources=[]))

    tools = [dict(id=i, name=n, measures=m, units=u, fills_fields=f, best_for=b,
                  cost_tier=c, review_url=None) for i, n, m, u, f, b, c in TOOLS]

    def dump(name, obj):
        (OUT / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")

    dump("plants.json", P)
    dump("afflictions.json", afflictions)
    dump("pair_rules.json", rules)
    dump("tools.json", tools)

    cols = list(P[0].keys())
    with open(OUT / "plants.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for p in P:
            w.writerow({k: ("; ".join(map(str, v)) if isinstance(v, list) else v) for k, v in p.items()})

    print(f"{len(P)} plants, {len(afflictions)} afflictions, {len(rules)} pair rules, {len(tools)} tools")


if __name__ == "__main__":
    main()
