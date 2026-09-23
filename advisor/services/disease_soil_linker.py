"""
disease_soil_linker.py
Rule-based Disease–Soil Linking Module.
Connects detected leaf pathology with soil NPK status under BARC guidelines.
"""

from .data_store import DISEASE_DATABASE

def link_disease_to_soil(disease_id, soil_analysis, crop_key):
    disease_info = DISEASE_DATABASE.get(disease_id, None)
    if not disease_info:
        return {}

    nutrients = soil_analysis["nutrients"]
    n_cat = nutrients["nitrogen"]["category"]
    k_cat = nutrients["potassium"]["category"]
    n_val = nutrients["nitrogen"]["value"]
    k_val = nutrients["potassium"]["value"]
    ph_val = nutrients["ph"]["value"]

    link_status = "neutral"
    causal_factors = []
    aggravating_factors = []
    soil_risk_score = 50

    if disease_id in ["rice_healthy", "jute_healthy"]:
        if n_cat == "optimum" and k_cat == "optimum":
            causal_summary_bn = "মাটির পুষ্টি উপাদানগুলো বিএআরসি (BARC) মানদণ্ড অনুযায়ী সন্তোষজনক ও সুষম রয়েছে। ফসলের স্বাভাবিক রোগ প্রতিরোধ ক্ষমতা অক্ষুণ্ণ রয়েছে।"
            causal_summary_en = "Soil NPK and pH are within optimal BARC standards. Plant immune resistance is robust."
            soil_risk_score = 15
            link_status = "healthy_balanced"
        else:
            imbalances = []
            if n_cat in ["high", "excessive"]:
                imbalances.append("উচ্চ নাইট্রোজেন")
            elif n_cat in ["low", "severe_low"]:
                imbalances.append("নাইট্রোজেন ঘাটতি")
            if k_cat in ["low", "severe_low"]:
                imbalances.append("পটাশের ঘাটতি")
            imbalance_str = ", ".join(imbalances) if imbalances else "সামান্য পুষ্টি তারতম্য"
            causal_summary_bn = f"বর্তমানে পাতা সুস্থ থাকলেও মাটিতে {imbalance_str} বিদ্যমান। দ্রুত সার সমন্বয় না করলে রোগ সংক্রমণের ঝুঁকি রয়েছে।"
            causal_summary_en = f"Leaf is healthy currently, but soil displays {imbalance_str}."
            soil_risk_score = 45
            link_status = "healthy_warning"

        return {
            "disease_name_bn": disease_info["name_bn"],
            "disease_name_en": disease_info["name_en"],
            "link_status": link_status,
            "soil_risk_score": soil_risk_score,
            "causal_summary_bn": causal_summary_bn,
            "causal_summary_en": causal_summary_en,
            "causal_factors": causal_factors,
            "aggravating_factors": aggravating_factors
        }

    if disease_id == "rice_blast":
        if n_cat in ["high", "excessive"]:
            causal_factors.append({
                "factor_bn": f"অতিরিক্ত নাইট্রোজেন ({n_val} ppm): ইউরিয়ার প্রাচুর্য পাতার কোষপ্রাচীর নরম ও রসাল করেছে, যা ব্লাস্ট ছত্রাকের স্পোর প্রবেশে সহায়তা করেছে।",
                "factor_en": f"Excessive Nitrogen ({n_val} ppm): Abundance of urea renders leaf cells tender and succulent, facilitating blast spore entry.",
                "severity": "high"
            })
            soil_risk_score += 25
        if k_cat in ["low", "severe_low"]:
            aggravating_factors.append({
                "factor_bn": f"পটাশিয়ামের ঘাটতি ({k_val} meq/100g): পটাশের অভাবে ধানের পাতায় সুরক্ষাকারী সিলিকা কিউটিকল স্তর দুর্বল হয়েছে।",
                "factor_en": f"Potassium Deficiency ({k_val} meq/100g): Potash scarcity weakens the protective silica-cuticle shield of rice leaves.",
                "severity": "medium"
            })
            soil_risk_score += 15
        causal_summary_bn = "মাটি বিশ্লেষণ নিশ্চিত করছে যে অতিরিক্ত ইউরিয়া প্রয়োগ ও পটাশের ঘাটতিই ব্লাস্ট ছত্রাকের দ্রুত ছড়িয়ে পড়ার অনুকূল ক্ষেত্র তৈরি করেছে।"
        causal_summary_en = "Soil linkage confirms high nitrogen along with low potassium created favorable conditions for blast fungal infection."

    elif disease_id == "rice_bacterial_blight":
        if n_cat in ["high", "excessive"]:
            causal_factors.append({
                "factor_bn": f"মাত্রাতিরিক্ত নাইট্রোজেন ({n_val} ppm): অতিরিক্ত ইউরিয়া প্রয়োগে পাতার হাইডাথোড রন্ধ্রগুলো প্রশস্ত হয়, যা ব্যাকটেরিয়াল ব্লাইটের প্রধান প্রবেশদ্বার।",
                "factor_en": f"Excessive Nitrogen ({n_val} ppm): Over-application of urea enlarges leaf hydathodes, creating primary entry points for Xanthomonas bacteria.",
                "severity": "high"
            })
            soil_risk_score += 30
        if k_cat in ["low", "severe_low"]:
            aggravating_factors.append({
                "factor_bn": "পটাশ ঘাটতি ব্যাকটেরিয়ার অভ্যন্তরীণ পরিবহন দ্রুততর করেছে।",
                "factor_en": "Potassium deficiency accelerated systemic bacterial vascular proliferation.",
                "severity": "medium"
            })
            soil_risk_score += 10
        causal_summary_bn = "অতিরিক্ত নাইট্রোজেন এবং অপর্যাপ্ত পটাশিয়ামের যৌথ প্রভাবে পাতার রন্ধ্র দিয়ে ব্যাকটেরিয়া সহজে সংক্রমিত হয়েছে।"
        causal_summary_en = "Excessive nitrogen and potassium deficit accelerated hydathodal bacterial invasion."

    elif disease_id == "rice_brown_spot":
        if k_cat in ["low", "severe_low"]:
            causal_factors.append({
                "factor_bn": f"পটাশিয়ামের তীব্র ঘাটতি ({k_val} meq/100g): ব্রাউন স্পট একটি পুষ্টিহীনতাজনিত ছত্রাক রোগ; মাটিতে পটাশ কম থাকলে গাছ দুর্বল হয়ে আক্রান্ত হয়।",
                "factor_en": f"Severe Potassium Deficiency ({k_val} meq/100g): Brown spot is a nutrient-depletion disease; acute potash deficit severely weakens host defenses.",
                "severity": "high"
            })
            soil_risk_score += 35
        if ph_val < 5.5:
            causal_factors.append({
                "factor_bn": f"অতিরিক্ত অম্লীয় মাটি (pH {ph_val}): অম্লতার কারণে মাটিতে পুষ্টি সহজলভ্যতা ব্যাহত হচ্ছে।",
                "factor_en": f"High Soil Acidity (pH {ph_val}): Soil acidity impairs essential nutrient uptake and enzymatic resilience.",
                "severity": "medium"
            })
            soil_risk_score += 15
        causal_summary_bn = "মাটিতে পটাশিয়ামের তীব্র সংকট এবং দুর্বল পুষ্টি পরিবেশই এই ব্রাউন স্পট রোগের প্রধান অনুঘটক।"
        causal_summary_en = "Severe potassium deficit and soil acidity are the primary drivers behind brown spot incidence."

    elif disease_id == "rice_tungro":
        if n_cat in ["high", "excessive"]:
            aggravating_factors.append({
                "factor_bn": "অতিরিক্ত নাইট্রোজেনের কারণে ধানের কচি পাতা সবুজ পাতা ফড়িং পোকাকে বেশি আকৃষ্ট করেছে।",
                "factor_en": "Excessive nitrogen generated soft succulent canopy foliage that attracted green leafhopper (GLH) virus vectors.",
                "severity": "medium"
            })
            soil_risk_score += 20
        causal_summary_bn = "গাছের পুষ্টি ভারসাম্যহীনতা সবুজ পাতা ফড়িং পোকার আক্রমণকে অনুকূল করেছে, যা এই ভাইরাস ছড়ানোর বাহক।"
        causal_summary_en = "Nutrient stress and tender foliage boosted leafhopper vector attraction."

    elif disease_id == "jute_cercospora":
        if k_cat in ["low", "severe_low"]:
            causal_factors.append({
                "factor_bn": f"পটাশের ঘাটতি ({k_val} meq/100g): পাটের পাতায় সারকোস্পোরা ছত্রাকের দাগ সৃষ্টি ও পাতা ঝরে পড়ার জন্য পটাশের ঘাটতি প্রধান দায়ী।",
                "factor_en": f"Potassium Deficiency ({k_val} meq/100g): Depleted potassium is the primary driver of Cercospora leaf spotting and premature defoliation.",
                "severity": "high"
            })
            soil_risk_score += 25
        if ph_val < 6.0:
            aggravating_factors.append({
                "factor_bn": f"মাটির নিম্ন পিএইচ (pH {ph_val}): পাটের জন্য অম্লীয় মাটি ছত্রাকের জন্য অনুকূল পরিবেশ তৈরি করে।",
                "factor_en": f"Sub-optimal Soil pH (pH {ph_val}): Acidic soil environments stimulate fungal sporulation in jute fields.",
                "severity": "medium"
            })
            soil_risk_score += 15
        causal_summary_bn = "মাটির নিম্ন পিএইচ এবং পটাশিয়ামের স্বল্পতা পাটের পাতাকে সারকোস্পোরা ছত্রাকের প্রতি ঝুঁকিপূর্ণ করেছে।"
        causal_summary_en = "Sub-optimal soil pH and potassium scarcity lowered epidermal resilience."

    elif disease_id == "jute_golden_mosaic":
        if n_cat in ["high", "excessive"]:
            causal_factors.append({
                "factor_bn": "অতিরিক্ত ইউরিয়া প্রয়োগের ফলে কচি ডগা বৃদ্ধি পেয়ে সাদা মাছি (Whitefly) পোকাকে আকৃষ্ট করেছে।",
                "factor_en": "Excessive urea application fostered delicate new shoots that heavily attracted whitefly (Bemisia tabaci) virus vectors.",
                "severity": "high"
            })
            soil_risk_score += 25
        causal_summary_bn = "মাটিতে অতিরিক্ত নাইট্রোজেন সাদা মাছি বাহকের বিস্তার ঘটিয়েছে, যা পাটের হলুদ মোজাইক ভাইরাস সংক্রমণের মূল কারণ।"
        causal_summary_en = "Elevated nitrogen promoted tender succulent shoots that accelerated whitefly viral transmission."

    elif disease_id == "jute_stem_rot":
        if k_cat in ["low", "severe_low"]:
            causal_factors.append({
                "factor_bn": f"পটাশিয়ামের চরম অভাব ({k_val} meq/100g): কান্ডের দৃঢ়তা রক্ষাকারী উপাদান কমে যাওয়ায় কান্ড পচা ছত্রাক দ্রুত মূল ও কান্ড বিনষ্ট করেছে।",
                "factor_en": f"Severe Potassium Scarcity ({k_val} meq/100g): Loss of stem tensile lignification enabled Macrophomina fungal mycelia to destroy collar roots and stems.",
                "severity": "high"
            })
            soil_risk_score += 30
        if ph_val < 5.8:
            aggravating_factors.append({
                "factor_bn": "অম্লীয় মাটি ম্যাক্রোফোমিনা ছত্রাকের বিস্তার বৃদ্ধি করেছে।",
                "factor_en": "Acidic soil accelerated Macrophomina fungal sclerotia proliferation.",
                "severity": "medium"
            })
            soil_risk_score += 15
        causal_summary_bn = "মাটির অম্লীয় পরিবেশ এবং পটাশের অপ্রতুলতা কান্ড পচা ছত্রাকের সংবেদনশীলতা বাড়িয়ে দিয়েছে।"
        causal_summary_en = "Soil acidity combined with potassium starvation aggravated stem rot vulnerability."
    else:
        causal_summary_bn = "মাটির পুষ্টি উপাদান ও রোগের লক্ষণ পরস্পর সম্পর্কযুক্ত।"
        causal_summary_en = "Soil nutrients exhibit direct correlation with detected pathology."

    soil_risk_score = min(98, max(30, soil_risk_score))

    return {
        "disease_name_bn": disease_info["name_bn"],
        "disease_name_en": disease_info["name_en"],
        "link_status": "correlated",
        "soil_risk_score": soil_risk_score,
        "causal_summary_bn": causal_summary_bn,
        "causal_summary_en": causal_summary_en,
        "causal_factors": causal_factors,
        "aggravating_factors": aggravating_factors
    }
