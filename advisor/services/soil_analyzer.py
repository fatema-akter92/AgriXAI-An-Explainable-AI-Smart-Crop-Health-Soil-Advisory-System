"""
soil_analyzer.py
Calculates Soil-Health Score (0-100), Nutrient Status vs BARC Benchmarks,
and Nutrient Depletion Impact from Previous Crops.
"""

from .data_store import BARC_BENCHMARKS, PREVIOUS_CROPS

def evaluate_single_nutrient(val, benchmark_dict):
    low = benchmark_dict["low"]
    opt_min = benchmark_dict["opt_min"]
    opt_max = benchmark_dict["opt_max"]
    high = benchmark_dict["high"]

    if val < low:
        score = max(10, int((val / low) * 45))
        status_bn = "তীব্র ঘাটতি (Severely Deficient)"
        status_en = "Severely Deficient"
        category = "severe_low"
        color = "#e63946"
    elif val < opt_min:
        frac = (val - low) / max(0.001, (opt_min - low))
        score = int(45 + frac * 35)
        status_bn = "স্বল্প মাত্রায় ঘাটতি (Low)"
        status_en = "Low"
        category = "low"
        color = "#f4a261"
    elif val <= opt_max:
        score = 95 - int(abs(val - ((opt_min + opt_max) / 2)) / ((opt_max - opt_min) / 2) * 10)
        status_bn = "অনুকূল / সুষম মাত্রা (Optimum)"
        status_en = "Optimum"
        category = "optimum"
        color = "#2e7d32"
    elif val <= high:
        score = 80 - int(((val - opt_max) / max(0.001, (high - opt_max))) * 25)
        status_bn = "প্রয়োজনের তুলনায় বেশি (High)"
        status_en = "High"
        category = "high"
        color = "#fb8c00"
    else:
        excess_ratio = min(2.0, (val - high) / max(0.001, high))
        score = max(20, int(55 - excess_ratio * 30))
        status_bn = "মাত্রাতিরিক্ত / বিপজ্জনক (Excessive)"
        status_en = "Excessive"
        category = "excessive"
        color = "#d32f2f"

    return {
        "value": round(val, 2),
        "score": max(0, min(100, score)),
        "status_bn": status_bn,
        "status_en": status_en,
        "category": category,
        "color": color,
        "benchmark": benchmark_dict
    }

def analyze_soil(crop_key, n_val, p_val, k_val, ph_val, prev_crop_key="aman_rice"):
    crop = crop_key if crop_key in BARC_BENCHMARKS else "rice"
    bench = BARC_BENCHMARKS[crop]
    prev_info = PREVIOUS_CROPS.get(prev_crop_key, PREVIOUS_CROPS["aman_rice"])

    n_res = evaluate_single_nutrient(float(n_val), {
        "low": bench["nitrogen"]["low"],
        "opt_min": bench["nitrogen"]["optimum_min"],
        "opt_max": bench["nitrogen"]["optimum_max"],
        "high": bench["nitrogen"]["high"],
        "unit": bench["nitrogen"]["unit"]
    })

    p_res = evaluate_single_nutrient(float(p_val), {
        "low": bench["phosphorus"]["low"],
        "opt_min": bench["phosphorus"]["optimum_min"],
        "opt_max": bench["phosphorus"]["optimum_max"],
        "high": bench["phosphorus"]["high"],
        "unit": bench["phosphorus"]["unit"]
    })

    k_res = evaluate_single_nutrient(float(k_val), {
        "low": bench["potassium"]["low"],
        "opt_min": bench["potassium"]["optimum_min"],
        "opt_max": bench["potassium"]["optimum_max"],
        "high": bench["potassium"]["high"],
        "unit": bench["potassium"]["unit"]
    })

    ph_res = evaluate_single_nutrient(float(ph_val), {
        "low": bench["ph"]["low"],
        "opt_min": bench["ph"]["optimum_min"],
        "opt_max": bench["ph"]["optimum_max"],
        "high": bench["ph"]["high"],
        "unit": bench["ph"]["unit"]
    })

    base_score = (
        n_res["score"] * 0.30 +
        p_res["score"] * 0.20 +
        k_res["score"] * 0.30 +
        ph_res["score"] * 0.20
    )

    depletion_impact = 0.0
    if prev_crop_key == "legume_pulses":
        depletion_impact = +6.0
    elif prev_crop_key == "maize":
        depletion_impact = -10.0
    elif prev_crop_key == "potato":
        depletion_impact = -8.0
    elif prev_crop_key == "boro_rice":
        depletion_impact = -5.0
    elif prev_crop_key == "fallow":
        depletion_impact = +4.0

    final_score = round(max(5.0, min(99.0, base_score + depletion_impact)), 1)

    if final_score >= 82:
        grade_bn = "চমৎকার উর্বর মাটি (Excellent Soil Health)"
        grade_en = "Excellent Soil Health"
        grade_color = "#2e7d32"
        health_summary_bn = "মাটির পুষ্টি উপাদান ও অম্লতার মান অত্যন্ত সুষম। রোগবালাই আক্রমণের স্বাভাবিক ঝুঁকি সর্বনিম্ন।"
        health_summary_en = "Soil nutrients and pH are well-balanced. Natural resistance against disease infection is optimal."
    elif final_score >= 68:
        grade_bn = "ভালো ও উৎপাদনশীল মাটি (Good Soil Health)"
        grade_en = "Good Soil Health"
        grade_color = "#43a047"
        health_summary_bn = "মাটির পুষ্টিমান সন্তোষজনক। কিছু পুষ্টি উপাদানে সামান্য সমন্বয় করলে সর্বোচ্চ ফলন নিশ্চিত হবে।"
        health_summary_en = "Soil nutrient status is satisfactory. Minor split adjustments will maximize crop yields."
    elif final_score >= 50:
        grade_bn = "মাঝারি উর্বরতা - ঘাটতি বিদ্যমান (Moderate Soil Health)"
        grade_en = "Moderate Soil Health"
        grade_color = "#f9a825"
        health_summary_bn = "মাটিতে লক্ষণীয় পুষ্টি ভারসাম্যহীনতা রয়েছে। রোগপ্রতিরোধ ক্ষমতা বৃদ্ধি করতে দ্রুত সার পুনঃসমন্বয় প্রয়োজন।"
        health_summary_en = "Noticeable nutrient imbalance detected. Prompt fertilizer realignment is recommended to boost plant vigor."
    elif final_score >= 35:
        grade_bn = "দুর্বল ও ক্ষয়িষ্ণু মাটি (Poor Soil Health)"
        grade_en = "Poor Soil Health"
        grade_color = "#fb8c00"
        health_summary_bn = "মাটিতে প্রধান পুষ্টি উপাদানের তীব্র ঘাটতি রয়েছে। গাছ শারীরবৃত্তীয় চাপের মধ্যে রয়েছে।"
        health_summary_en = "Acute deficiency in primary macronutrients. Plants are under significant physiological stress."
    else:
        grade_bn = "অত্যন্ত সংকটপূর্ণ মাটি (Severely Depleted)"
        grade_en = "Critically Depleted"
        grade_color = "#d32f2f"
        health_summary_bn = "মাটির স্বাস্থ্য বিপর্যয়কর অবস্থায় আছে। দ্রুত জৈব পদার্থ প্রয়োগ ও জরুরি সার ব্যবস্থাপনা ব্যতিরেকে ফসল ফলানো ঝুঁকিপূর্ণ।"
        health_summary_en = "Critical soil depletion. Organic matter incorporation and emergency soil restoration are urgently required."

    return {
        "final_score": final_score,
        "grade_bn": grade_bn,
        "grade_en": grade_en,
        "grade_color": grade_color,
        "health_summary_bn": health_summary_bn,
        "health_summary_en": health_summary_en,
        "nutrients": {
            "nitrogen": n_res,
            "phosphorus": p_res,
            "potassium": k_res,
            "ph": ph_res
        },
        "previous_crop": prev_info,
        "depletion_impact": depletion_impact
    }
