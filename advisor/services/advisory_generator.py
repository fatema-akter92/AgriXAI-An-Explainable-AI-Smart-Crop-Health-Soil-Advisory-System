"""
advisory_generator.py
Generates personalized agricultural advisory in Bengali and English,
with dynamic fertilizer dosage calculations based on BARC guides.
"""

from .data_store import DISEASE_DATABASE, BARC_BENCHMARKS

def calculate_fertilizer_prescription(crop_key, nutrients, land_unit="bigha", land_amount=1.0):
    crop = crop_key if crop_key in BARC_BENCHMARKS else "rice"
    base_std = BARC_BENCHMARKS[crop]["standard_fertilizer_per_bigha"]

    unit_multipliers = {
        "bigha": 1.0,
        "decimal": 1.0 / 33.0,
        "acre": 100.0 / 33.0,
        "hectare": 247.0 / 33.0
    }
    multiplier = unit_multipliers.get(land_unit, 1.0) * float(land_amount)

    n_cat = nutrients["nitrogen"]["category"]
    p_cat = nutrients["phosphorus"]["category"]
    k_cat = nutrients["potassium"]["category"]

    # Urea
    urea_base = base_std["urea"]
    if n_cat == "excessive":
        urea_adj = urea_base * 0.40
        urea_note = "মাটিতে অতিরিক্ত নাইট্রোজেন থাকায় ইউরিয়া ৬০% কমাতে হবে"
    elif n_cat == "high":
        urea_adj = urea_base * 0.70
        urea_note = "মাটিতে নাইট্রোজেন বেশি থাকায় ইউরিয়া ৩০% হ্রাস করা হয়েছে"
    elif n_cat in ["severe_low"]:
        urea_adj = urea_base * 1.30
        urea_note = "নাইট্রোজেন ঘাটতি পূরণে ইউরিয়া ৩০% বৃদ্ধি করা হয়েছে"
    elif n_cat in ["low"]:
        urea_adj = urea_base * 1.15
        urea_note = "নাইট্রোজেন ঘাটতি মেটাতে ইউরিয়া ১৫% বাড়ানো হয়েছে"
    else:
        urea_adj = urea_base
        urea_note = "সুষম রুটিন মাত্রা বজায় রাখা হয়েছে"

    # TSP
    tsp_base = base_std["tsp"]
    if p_cat in ["severe_low"]:
        tsp_adj = tsp_base * 1.35
        tsp_note = "ফসফরাস তীব্র ঘাটতি পূরণে টিএসপি ৩৫% বৃদ্ধি"
    elif p_cat in ["low"]:
        tsp_adj = tsp_base * 1.15
        tsp_note = "ফসফরাস স্বল্প ঘাটতি পূরণে টিএসপি ১৫% বৃদ্ধি"
    elif p_cat in ["high", "excessive"]:
        tsp_adj = tsp_base * 0.65
        tsp_note = "মাটিতে ফসফরাস জমা থাকায় টিএসপি ৩৫% সাশ্রয় করুন"
    else:
        tsp_adj = tsp_base
        tsp_note = "স্ট্যান্ডার্ড মাত্রা"

    # MoP
    mop_base = base_std["mop"]
    if k_cat in ["severe_low"]:
        mop_adj = mop_base * 1.40
        mop_note = "পটাশিয়ামের তীব্র ঘাটতি মেটাতে ও রোগ প্রতিরোধে পটাশ ৪০% বাড়ান"
    elif k_cat in ["low"]:
        mop_adj = mop_base * 1.20
        mop_note = "পটাশ ঘাটতি কাটাতে এমওপি ২০% বাড়ান"
    elif k_cat in ["high", "excessive"]:
        mop_adj = mop_base * 0.75
        mop_note = "পটাশিয়াম সন্তোষজনক থাকায় ২৫% কমানো হয়েছে"
    else:
        mop_adj = mop_base
        mop_note = "স্ট্যান্ডার্ড মাত্রা"

    gypsum_base = base_std["gypsum"]
    zinc_base = base_std["zinc_sulphate"]

    total_urea = round(urea_adj * multiplier, 2)
    total_tsp = round(tsp_adj * multiplier, 2)
    total_mop = round(mop_adj * multiplier, 2)
    total_gypsum = round(gypsum_base * multiplier, 2)
    total_zinc = round(zinc_base * multiplier, 2)

    return {
        "land_unit": land_unit,
        "land_amount": land_amount,
        "prescription": [
            {
                "fertilizer_bn": "ইউরিয়া (Urea - N)",
                "fertilizer_en": "Urea (Nitrogen 46%)",
                "dose_kg": total_urea,
                "role_bn": "গাছের বৃদ্ধি ও সবুজ পাতার জন্য",
                "role_en": "Vegetative vigor & chlorophyll formation",
                "timing_bn": "৩ কিস্তিতে উপরিপ্রয়োগ (চারা লাগানোর ১৫, ৩০ এবং ৪৫ দিন পর)",
                "timing_en": "3 split top-dressings (15, 30, and 45 days after transplanting)",
                "note_bn": urea_note,
                "note_en": "Adjusted per leaf condition & BARC benchmark"
            },
            {
                "fertilizer_bn": "টিএসপি / ডিএপি (TSP/DAP - P)",
                "fertilizer_en": "TSP / DAP (Phosphorus)",
                "dose_kg": total_tsp,
                "role_bn": "শিকড়ের বিস্তার ও দ্রুত কুশি ছাড়ার জন্য",
                "role_en": "Root elongation & early active tillering",
                "timing_bn": "জমি তৈরির শেষ চাষে সম্পূর্ণ প্রয়োগ",
                "timing_en": "Full basal application during final plowing",
                "note_bn": tsp_note,
                "note_en": "Basal phosphorus dose based on soil reserves"
            },
            {
                "fertilizer_bn": "এমওপি / পটাশ (MoP - K)",
                "fertilizer_en": "MoP (Muriate of Potash)",
                "dose_kg": total_mop,
                "role_bn": "রোগ প্রতিরোধ ক্ষমতা ও দানার পুষ্টতার জন্য",
                "role_en": "Disease resistance & robust grain filling",
                "timing_bn": "অর্ধেক জমি তৈরিতে এবং বাকি অর্ধেক শেষ কিস্তি ইউরিয়ার সাথে",
                "timing_en": "Half basal at plowing, remainder with final urea split",
                "note_bn": mop_note,
                "note_en": "Crucial for strengthening leaf cuticle and disease immunity"
            },
            {
                "fertilizer_bn": "জিপসাম (Gypsum - S)",
                "fertilizer_en": "Gypsum (Sulphur 18%)",
                "dose_kg": total_gypsum,
                "role_bn": "গাছ হলুদ হওয়া রোধ ও প্রোটিন গঠনে",
                "role_en": "Prevents sulfur chlorosis & synthesizes plant proteins",
                "timing_bn": "জমি তৈরির শেষ চাষে প্রয়োগ",
                "timing_en": "Basal application during final land preparation",
                "note_bn": "স্বাভাবিক সালফার মাত্রা",
                "note_en": "Standard routine sulfur rate"
            },
            {
                "fertilizer_bn": "জিংক সালফেট (Zinc Sulphate - Zn)",
                "fertilizer_en": "Zinc Sulphate (36% Zn)",
                "dose_kg": total_zinc,
                "role_bn": "ধানের খায়রা রোগ দমন ও পাটের ক্লোরোফিল তৈরিতে",
                "role_en": "Controls zinc chlorosis & activates growth hormones",
                "timing_bn": "জমি তৈরিতে (টিএসপি প্রয়োগের ৩ দিন পর বা আলাদা প্রয়োগ)",
                "timing_en": "Basal (apply 3 days apart from TSP to prevent fixation)",
                "note_bn": "মাইক্রোনিউট্রিয়েন্ট ব্যালেন্স",
                "note_en": "Micronutrient balancing"
            }
        ]
    }

def generate_full_advisory(disease_id, soil_analysis, disease_soil_link, crop_key, land_unit="bigha", land_amount=1.0):
    disease = DISEASE_DATABASE.get(disease_id, DISEASE_DATABASE["rice_healthy"])
    fert_rx = calculate_fertilizer_prescription(crop_key, soil_analysis["nutrients"], land_unit, land_amount)

    return {
        "disease_info": disease,
        "soil_health": {
            "score": soil_analysis["final_score"],
            "grade_bn": soil_analysis["grade_bn"],
            "grade_en": soil_analysis["grade_en"],
            "grade_color": soil_analysis["grade_color"],
            "summary_bn": soil_analysis["health_summary_bn"],
            "summary_en": soil_analysis["health_summary_en"]
        },
        "soil_link": disease_soil_link,
        "fertilizer_prescription": fert_rx,
        "treatment": disease.get("recommendation_bn", {}),
        "treatment_bn": disease.get("recommendation_bn", {}),
        "treatment_en": disease.get("recommendation_en", {})
    }
