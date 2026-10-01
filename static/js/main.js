/**
 * main.js
 * Frontend controller for AgriXAI Smart Crop Health & Soil Advisory
 * Backend: Django 5+
 * Complete Bilingual (Bengali / English) Engine
 */

let currentLang = 'bn';
let selectedCrop = 'rice';
let selectedSampleFile = 'rice_blast.jpg';
let selectedPresetClass = 'rice_blast';
let allSamples = [];
let lastResultData = null;
let uploadedUserFile = null;

const UI_TRANSLATIONS = {
    bn: {
        brand_title: "AgriXAI • কৃষি-পরামর্শক",
        brand_sub: "স্মার্ট ফসল স্বাস্থ্য ও মৃত্তিকা পুষ্টি পরামর্শক",
        nav_about: "পদ্ধতি ও প্রযুক্তি (Methodology)",
        hero_pill: "🌱 স্মার্ট কৃষি প্রযুক্তি • Smart Agriculture AI Platform",
        hero_heading: "ধান ও পাটের পাতার রোগ সনাক্তকরণ এবং<br>মাটির পুষ্টি-সচেতন সমন্বিত কৃষক পরামর্শ",
        hero_sub: "An Explainable AI System for Rice and Jute Leaf Disease Detection with Soil-Nutrient-Aware Advisory for Bangladeshi Farmers.",
        chip_crops: "২টি প্রধান ফসল: ধান ও পাট",
        chip_gradcam: "Grad-CAM ব্যাখ্যাযোগ্য এআই",
        chip_barc: "BARC মানদণ্ডে সুষম সার",
        chip_soil_score: "০–১০০ মৃত্তিকা স্বাস্থ্য স্কোর",
        hero_organic_title: "সুষম জৈব পুষ্টি ও উর্বর মৃত্তিকা",
        hero_organic_sub: "Sustainable Organic Farming • Healthy Soil Microbiome & Balanced Nutrients",
        step1_num: "১",
        step1_title: "পাতার ছবি ও ফসল নির্বাচন (Leaf Upload)",
        crop_rice_title: "ধান ফসল (Rice)",
        crop_rice_sub: "বোরো / আমন / আউশ ধান",
        crop_jute_title: "পাট ফসল (Jute)",
        crop_jute_sub: "তোষা / দেশী পাট",
        upload_title: "আক্রান্ত পাতার ছবি এখানে আপলোড করুন",
        upload_sub: "ছবি টেনে আনুন (Drag & Drop) অথবা ব্রাউজ করুন (JPG, PNG, JPEG)",
        upload_btn: "📁 ছবি নির্বাচন করুন",
        demo_title: "🧪 অথবা নমুনা ছবি ক্লিক করে পরীক্ষা করুন (Demo Leaves):",
        step2_num: "২",
        step2_title: "মাটির পুষ্টি ও জমির তথ্য (Soil & Land Parameters)",
        param_n_label: "নাইট্রোজেন (N)",
        param_p_label: "ফসফরাস (P)",
        param_k_label: "পটাশিয়াম (K)",
        param_ph_label: "মাটির পিএইচ (pH)",
        bench_n_low: "ঘাটতি: &lt;25",
        bench_n_opt: "আদর্শ: 25-45 ppm",
        bench_p_low: "ঘাটতি: &lt;12",
        bench_p_opt: "আদর্শ: 14-24 ppm",
        bench_k_low: "ঘাটতি: &lt;0.15",
        bench_k_opt: "আদর্শ: 0.18-0.28",
        bench_ph_low: "অম্লীয়: &lt;5.5",
        bench_ph_opt: "অনুকূল: 5.8-6.8",
        label_prev_crop: "🌾 জমিতে পূর্বে চাষকৃত ফসল (Previous Crop):",
        label_land_amount: "জমির পরিমাণ:",
        label_land_unit: "পরিমাপের একক:",
        unit_bigha: "বিঘা (৩৩ শতাংশ / Decimal)",
        unit_decimal: "শতক / ডেসিমাল",
        unit_acre: "একর (১০০ শতাংশ)",
        unit_hectare: "হেক্টর",
        submit_btn: "🔍 রোগ সনাক্তকরণ ও পূর্ণাঙ্গ সার প্রেসক্রিপশন নিন",
        spinner_title: "মডেল প্রক্রিয়াকরণ চলছে...",
        spinner_sub: "MobileNetV2 কনভোলিউশন, Grad-CAM ফিচার ম্যাপ ও বিএআরসি মানদণ্ড বিশ্লেষণ হচ্ছে...",
        step3_num: "৩",
        step3_title: "Grad-CAM ব্যাখ্যাযোগ্য এআই ভিজ্যুয়ালাইজেশন (Explainable AI Studio)",
        gradcam_orig_title: "১. আপলোডকৃত মূল পাতা (Original Leaf)",
        gradcam_orig_desc: "মডেলে ইনপুট হিসেবে প্রেরিত পাতার ছবি",
        gradcam_heat_title: "২. কনভোলিউশনাল হিটম্যাপ (Activation Heatmap)",
        gradcam_heat_desc: "Jet Colormap: লাল ও হলুদ অংশ সর্বাধিক সক্রিয়",
        gradcam_over_title: "৩. সমন্বিত এক্সএআই ওভারলে (Superimposed Overlay)",
        gradcam_over_desc: "আক্রান্ত ক্ষতের উপর ফোকাসকৃত এলাকা স্পষ্টকরণ",
        xai_rationale_title: "এআই মডেল কেন এই সিদ্ধান্তে উপনীত হলো (XAI Decision Rationale):",
        xai_focal_label: "ফোকাসকৃত আক্রান্ত অংশ:",
        xai_focal_leaf: "পাতার উপরিভাগ।",
        prob_header: "📊 শীর্ষ পূর্বাভাস সম্ভাবনা (Predicted Probabilities):",
        step4_num: "৪",
        step4_title: "রোগ ও মাটির পুষ্টি সম্পর্ক (Disease–Soil Linking)",
        risk_factors_title: "চিহ্নিত পুষ্টিগত ঝুঁকির কারণসমূহ (Identified Soil Risk Factors):",
        step5_num: "৫",
        step5_title: "মাটির সামগ্রিক স্বাস্থ্য স্কোর (Soil-Health Score: 0–100)",
        soil_score_max: "/ ১০০",
        step6_num: "৬",
        step6_title: "কৃষকের জমির জন্য সুষম সার ব্যবস্থাপত্র (Fertilizer Prescription)",
        barc_badge: "বিএআরসি অনুমোদিত নির্দেশিকা",
        th_fert: "সারের নাম ও ভূমিকা",
        th_dose: "প্রয়োজনীয় পরিমাণ (Kg)",
        th_timing: "প্রয়োগের সময় ও কিস্তি",
        th_note: "পুষ্টি সমন্বয় মন্তব্য",
        action_plan_title: "🛡️ সমন্বিত রোগ নিরাময় ও প্রতিরোধমূলক পরামর্শ (Comprehensive Action Plan):",
        action_quad_imm: "⚡ জরুরি পদক্ষেপ (Immediate Actions)",
        action_quad_chem: "🧪 অনুমোদিত রাসায়নিক দমন (Chemical Fungicide / Bactericide)",
        action_quad_org: "🌿 পরিবেশবান্ধব জৈব চিকিৎসা (Eco-friendly IPM / Organic)",
        action_quad_prev: "🌾 দীর্ঘমেয়াদী প্রতিরোধ ও জাত নির্বাচন (Preventive Field Care)",
        btn_print: "🖨️ ডায়াগনস্টিক রিপোর্ট ও প্রেসক্রিপশন প্রিন্ট করুন",
        wf_pill: "🌾 স্মার্ট কৃষি ও আধুনিক কর্মপদ্ধতি • Sustainable Smart Agriculture Systems",
        wf_heading: "মাঠ পর্যায়ে কৃষকের আধুনিক ও বিজ্ঞানসম্মত পরিচর্যা পদ্ধতি",
        wf_sub: "সঠিক সময়ে ফসলের রোগ সনাক্তকরণ, মাটির পুষ্টি উপাদানের পরীক্ষা এবং পরিবেশবান্ধব সমন্বিত বালাই ব্যবস্থাপনায় কৃষকের টেকসই ফসল উৎপাদনের ৪টি কার্যকর ধাপ:",
        wf_card1_tag: "ধাপ ০১ • পর্যবেক্ষণ",
        wf_card1_title: "নিয়মিত পাতার স্বাস্থ্য পরীক্ষা",
        wf_card1_desc: "সকালে ক্ষেতে ঘুরে পাতার রঙ পরিবর্তন, ব্লাস্টের তক্ষু আকৃতির দাগ বা সারকোস্পোরার প্রাথমিক ক্ষত পর্যবেক্ষণ ও মোবাইল ক্যামেরায় ধারণ।",
        wf_card1_footer: "✓ এআই ভিত্তিক তাৎক্ষণিক রোগ সনাক্তকরণ",
        wf_card2_tag: "ধাপ ০২ • পুষ্টি নির্ণয়",
        wf_card2_title: "মাটির পুষ্টি ও NPK বিশ্লেষণ",
        wf_card2_desc: "জমির নাইট্রোজেন (N), ফসফরাস (P), পটাশিয়াম (K) এবং অম্লমান (pH) নিয়মিত পরীক্ষা করে মাটির স্বাস্থ্য স্কোর নির্ধারণ করা।",
        wf_card2_footer: "✓ বিএআরসি (BARC) মানদণ্ডে পুষ্টি ঘাটতি নিরূপণ",
        wf_card3_tag: "ধাপ ০৩ • সুষম সার",
        wf_card3_title: "সুষম ও কিস্তিবিত্তিক সার প্রয়োগ",
        wf_card3_desc: "অতিরিক্ত ইউরিয়া পরিহার করে পটাশ, জিপসাম ও জৈব সারের সুষম কিস্তি প্রয়োগ। এতে গাছের রোগ প্রতিরোধ ক্ষমতা বহুগুণ বাড়ে।",
        wf_card3_footer: "✓ বিঘা/শতাংশ প্রতি সঠিক ডোজ ব্যবস্থাপনা",
        wf_card4_tag: "ধাপ ০৪ • সমন্বিত দমন",
        wf_card4_title: "পরিবেশবান্ধব আইপিএম ও ফলন",
        wf_card4_desc: "ট্রাইকোডার্মা, আলো-ফাঁদ ও প্রাকৃতিক শত্রু পোকার সাহায্যে বালাই দমন করে নিরাপদ ফসল ও টেকসই উর্বরতা বজায় রাখা।",
        wf_card4_footer: "✓ রাসায়নিক খরচ ৩০% হ্রাস ও সুস্থ ফলন",
        tractor_title: "কৃষকের স্মার্ট সিদ্ধান্তই পারে নিশ্চিত করতে সুস্থ ফসল ও সমৃদ্ধ বাংলাদেশ",
        tractor_desc: "ডিজিটাল ডায়াগনোসিস ও সুষম সার প্রয়োগে মাটির উর্বরতা রক্ষা পায় এবং উৎপাদন খরচ কমে।",
        tractor_tag1: "🌾 ২৫-৩০% সার সাশ্রয়",
        tractor_tag2: "🛡️ ৩৫% রোগ প্রতিরোধ",
        reg_pill: "🇧🇩 বাংলাদেশের কৃষি অঞ্চলভিত্তিক গবেষণা ও বাস্তব প্রভাব • Regional Agro-Ecological Impact",
        reg_heading: "মাটি ও ফসলের সুরক্ষায় AgriXAI কেন নির্ভরযোগ্য ও অনন্য?",
        reg_sub: "বাংলাদেশের বিভিন্ন কৃষি অঞ্চলের (Agro-Ecological Zones) মাটির তারতম্য, পুষ্টি ভারসাম্যহীনতা এবং ধান ও পাটের অঞ্চলভিত্তিক রোগবালাইয়ের বিস্তার বিশ্লেষণ করে এই সিস্টেমের এআই ইঞ্জিন ও বিএআরসি অ্যালগরিদম সুসংগঠিত করা হয়েছে।",
        metric1_val: "৯৮.৪%",
        metric1_title: "রোগ নির্ণয় নির্ভুলতা",
        metric1_desc: "MobileNetV2 আর্কিটেকচার দ্বারা ৯টি ধান ও পাটের প্রধান রোগ ও সুস্থ পাতা ক্লাসিফিকেশন।",
        metric2_val: "&lt; ২.৫ সে.",
        metric2_title: "তাৎক্ষণিক ডায়াগনোসিস",
        metric2_desc: "পাতার ছবি আপলোডের কয়েক সেকেন্ডের মধ্যে Grad-CAM রঙিন হিটম্যাপ ও বাংলা প্রেসক্রিপশন।",
        metric3_val: "২৫–৩০%",
        metric3_title: "সারের অপচয় ও খরচ সাশ্রয়",
        metric3_desc: "বিএআরসি সুষম সার নির্দেশিকায় জমির পরিমাণ অনুযায়ী কেজি হিসেবে সঠিক সারের ডোজ নির্ধারণ।",
        metric4_val: "৩৫%",
        metric4_title: "রোগবালাই আগাম প্রতিরোধ",
        metric4_desc: "মাটির NPK ও পিএইচ সমন্বয়ে ফসলের প্রাকৃতিক রোগ প্রতিরোধ ক্ষমতা বৃদ্ধি ও দীর্ঘস্থায়ী সুরক্ষা।",
        zones_title: "🗺️ বাংলাদেশের ৪টি প্রধান কৃষি অঞ্চলের মাটি ও রোগ ঝুঁকি বিশ্লেষণ",
        zones_sub: "অঞ্চলভেদে পুষ্টি ঘাটতি ও রোগবালাইয়ের সম্পর্ক জেনে মাঠপর্যায়ে সঠিক ব্যবস্থা গ্রহণ:",
        z1_title: "বরেন্দ্র অঞ্চল (রাজশাহী, নওগাঁ)",
        z1_soil: "<strong style=\"color: #b45309;\">মাটির বৈশিষ্ট্য:</strong> লালচে এঁটেল, দ্রুত আর্দ্রতা হারায়, নাইট্রোজেন ও জৈব পদার্থের চরম ঘাটতি।",
        z1_disease: "<strong style=\"color: #dc2626;\">রোগের ঝুঁকি:</strong> ধানের পাতা পোড়া (Blight) ও ব্লাস্ট।",
        z1_sol: "<strong>AgriXAI সমাধান:</strong> কিস্তিবিত্তিক ইউরিয়া প্রয়োগ ও দস্তা (Zinc) সার সমন্বয়।",
        z2_title: "হাওর ও উত্তর-পূর্বাঞ্চল (সিলেট, সুনামগঞ্জ)",
        z2_soil: "<strong style=\"color: #b45309;\">মাটির বৈশিষ্ট্য:</strong> দীর্ঘস্থায়ী জলাবদ্ধ পলি মাটি, তীব্র পটাশিয়াম (K) ক্ষয় ও অম্লীয় অবস্থা (pH &lt; ৫.৫)।",
        z2_disease: "<strong style=\"color: #dc2626;\">রোগের ঝুঁকি:</strong> ধানের বাদামী দাগ (Brown Spot) ও চারা ধ্বসা।",
        z2_sol: "<strong>AgriXAI সমাধান:</strong> এমওপি (পটাশ) সারের সঠিক মাত্রা এবং ডলোমাইট চুন প্রয়োগ।",
        z3_title: "তিস্তা ও পলল অঞ্চল (রংপুর, ফরিদপুর)",
        z3_soil: "<strong style=\"color: #b45309;\">মাটির বৈশিষ্ট্য:</strong> উর্বর বেলে-দোআঁশ, আর্দ্র অববাহিকা, পাটের জন্য অত্যন্ত অনুকূল তবে ছত্রাকপ্রবণ।",
        z3_disease: "<strong style=\"color: #dc2626;\">রোগের ঝুঁকি:</strong> পাটের কান্ড পচা (Stem Rot) ও গোল্ডেন মোজাইক।",
        z3_sol: "<strong>AgriXAI সমাধান:</strong> সুষম টিএসপি ও জিপসাম প্রয়োগ এবং ট্রাইকোডার্মা জৈব বীজ শোধন।",
        z4_title: "উপকূলীয় অঞ্চল (খুলনা, বরিশাল)",
        z4_soil: "<strong style=\"color: #b45309;\">মাটির বৈশিষ্ট্য:</strong> লবণাক্ততার পরিবর্তনশীল মাত্রা ও ক্ষারীয়/উচ্চ পিএইচ (pH &gt; ৭.৫)।",
        z4_disease: "<strong style=\"color: #dc2626;\">রোগের ঝুঁকি:</strong> ধানের টুংরো ভাইরাস ও শিকড় পচা।",
        z4_sol: "<strong>AgriXAI সমাধান:</strong> সুষম জিপসাম, সবুজ সার (ধৈঞ্চা) চাষ ও লবণ সহনশীল জাত নির্বাচন।",
        cta_pill: "✨ ডিজিটাল বাংলাদেশ • স্মার্ট কৃষির নতুন দিগন্ত",
        cta_heading: "কৃষির ভবিষ্যৎ এখন হাতের মুঠোয় • এক ক্লিকেই ফসল ও মাটির পূর্ণাঙ্গ সমাধান",
        cta_sub: "অনিশ্চয়তা ও অন্ধ অনুমান নয়—কৃত্রিম বুদ্ধিমত্তার চোখ ও বিএআরসি বিজ্ঞানসম্মত সার নির্দেশিকায় আপনার ধান ও পাটের প্রতিটি ক্ষেত রাখুন রোগমুক্ত ও প্রাণবন্ত।",
        cta_btn1: "🌾 স্মার্ট ডায়াগনোসিস শুরু করুন",
        cta_btn2: "📖 গবেষণাপত্র ও গাণিতিক ভিত্তি",
        footer_col1_title: "AgriXAI • কৃষি-পরামর্শক",
        footer_col1_desc: "বাংলাদেশের কৃষক ও কৃষি কর্মকর্তাদের জন্য বিশ্বস্ত, ব্যাখ্যাযোগ্য ও মাটির পুষ্টি-সচেতন বাংলা এআই সিস্টেম। ধান ও পাটের রোগ নির্ণয় ও সুষম সার ব্যবস্থাপনায় নিবেদিত।",
        footer_col2_title: "🔗 প্রয়োজনীয় তথ্য ও লিংক",
        footer_link1: "গবেষণা ও পদ্ধতি বিবরণী",
        footer_link2: "বাংলাদেশ কৃষি গবেষণা কাউন্সিল (BARC)",
        footer_link3: "বাংলাদেশ ধান গবেষণা ইনস্টিটিউট (BRRI)",
        footer_link4: "বাংলাদেশ পাট গবেষণা ইনস্টিটিউট (BJRI)",
        footer_col3_title: "☎️ কৃষক সহায়তা ও হেল্পলাইন",
        footer_helpline1: "<strong>কৃষি কল সেন্টার:</strong> <span style=\"color: var(--green-primary); font-weight: 800; font-size: 0.95rem;\">১৬১২৩</span> (টোল-ফ্রি)",
        footer_helpline2: "<strong>জাতীয় জরুরি সেবা:</strong> <span style=\"font-weight: 700;\">৯৯৯</span> | <strong>সরকারি তথ্য:</strong> <span style=\"font-weight: 700;\">৩৩৩</span>",
        footer_helpline3: "<strong>মাঠ পরামর্শ:</strong> নিকটস্থ উপসহকারী কৃষি কর্মকর্তা (SAAO / DAE) এর সাথে যোগাযোগ করুন।",
        footer_col4_title: "🎓 গবেষণা ও তত্ত্বাবধান",
        footer_researcher: "<strong>গবেষক:</strong> <span style=\"color: #1b4332; font-weight: 700;\">ফাতেমা আক্তার (Fatema Akter)</span>",
        footer_dept: "কম্পিউটার বিজ্ঞান ও প্রকৌশল বিভাগ<br><strong>ড্যাফোডিল ইন্টারন্যাশনাল ইউনিভার্সিটি (DIU)</strong>",
        footer_copy: "© 2026 <strong>AgriXAI</strong> • Daffodil International University • An Explainable AI Crop Advisory System",
        footer_tagline: "AgriXAI - Making farmers' lives easy 🌾"
    },
    en: {
        brand_title: "AgriXAI • Crop Advisor",
        brand_sub: "Smart Crop Health & Soil Nutrient Advisor",
        nav_about: "Methodology & Tech",
        hero_pill: "🌱 Smart Agriculture AI Platform • BARC Fertilizer Engine",
        hero_heading: "Rice & Jute Leaf Disease Detection and<br>Soil-Nutrient-Aware Comprehensive Advisory",
        hero_sub: "An Explainable AI System for Rice and Jute Leaf Disease Detection with Soil-Nutrient-Aware Advisory for Bangladeshi Farmers.",
        chip_crops: "🌾 2 Major Crops: Rice & Jute",
        chip_gradcam: "🔥 Grad-CAM Explainable AI",
        chip_barc: "🧪 BARC Balanced Fertilizer Guide",
        chip_soil_score: "📊 0–100 Soil Health Score",
        hero_organic_title: "Balanced Organic Nutrition & Fertile Soil",
        hero_organic_sub: "Sustainable Organic Farming • Healthy Soil Microbiome & Balanced Nutrients",
        step1_num: "1",
        step1_title: "Leaf Photo & Crop Selection",
        crop_rice_title: "Rice Crop",
        crop_rice_sub: "Boro / Aman / Aus Rice",
        crop_jute_title: "Jute Crop",
        crop_jute_sub: "Tossha / Deshi Jute",
        upload_title: "Upload infected leaf image here",
        upload_sub: "Drag & Drop or browse leaf photo (JPG, PNG, JPEG)",
        upload_btn: "📁 Browse Image",
        demo_title: "🧪 Or click sample images to test (Demo Leaves):",
        step2_num: "2",
        step2_title: "Soil Nutrients & Land Parameters",
        param_n_label: "Nitrogen (N)",
        param_p_label: "Phosphorus (P)",
        param_k_label: "Potassium (K)",
        param_ph_label: "Soil pH",
        bench_n_low: "Deficient: &lt;25",
        bench_n_opt: "Optimum: 25-45 ppm",
        bench_p_low: "Deficient: &lt;12",
        bench_p_opt: "Optimum: 14-24 ppm",
        bench_k_low: "Deficient: &lt;0.15",
        bench_k_opt: "Optimum: 0.18-0.28",
        bench_ph_low: "Acidic: &lt;5.5",
        bench_ph_opt: "Optimum: 5.8-6.8",
        label_prev_crop: "🌾 Previously Cultivated Crop:",
        label_land_amount: "Land Area:",
        label_land_unit: "Measurement Unit:",
        unit_bigha: "Bigha (33 Decimals)",
        unit_decimal: "Decimal (Satak)",
        unit_acre: "Acre (100 Decimals)",
        unit_hectare: "Hectare",
        submit_btn: "🔍 Diagnose Disease & Get Fertilizer Prescription",
        spinner_title: "Processing AI Inference...",
        spinner_sub: "Computing MobileNetV2 features, Grad-CAM heatmap, and BARC recommendations...",
        step3_num: "3",
        step3_title: "Grad-CAM Explainable AI Visualization Studio",
        gradcam_orig_title: "1. Original Leaf Image",
        gradcam_orig_desc: "Input leaf image fed to neural model",
        gradcam_heat_title: "2. Activation Heatmap",
        gradcam_heat_desc: "Jet Colormap: Red & yellow show maximum activation",
        gradcam_over_title: "3. Superimposed Overlay",
        gradcam_over_desc: "Lesion-focused regions highlighted on original leaf",
        xai_rationale_title: "Why AI Model Reached This Decision (XAI Decision Rationale):",
        xai_focal_label: "Focal Lesion Coverage:",
        xai_focal_leaf: "of leaf blade.",
        prob_header: "📊 Top Predicted Probabilities:",
        step4_num: "4",
        step4_title: "Disease–Soil Nutrient Relationship",
        risk_factors_title: "Identified Soil Risk Factors:",
        step5_num: "5",
        step5_title: "Soil-Health Score (0–100)",
        soil_score_max: "/ 100",
        step6_num: "6",
        step6_title: "Balanced Fertilizer Prescription for Farm",
        barc_badge: "BARC Approved Guide",
        th_fert: "Fertilizer & Role",
        th_dose: "Required Dose (Kg)",
        th_timing: "Application Timing & Splits",
        th_note: "Nutrient Adjustment Remarks",
        action_plan_title: "🛡️ Comprehensive Disease Treatment & Prevention Plan:",
        action_quad_imm: "⚡ Immediate Actions",
        action_quad_chem: "🧪 Chemical Treatment (Fungicide / Bactericide)",
        action_quad_org: "🌿 Eco-Friendly Organic / IPM Treatment",
        action_quad_prev: "🌾 Preventive Field Care & Resistant Varieties",
        btn_print: "🖨️ Print Diagnostic Report & Prescription",
        wf_pill: "🌾 Smart Agriculture & Sustainable Farming Systems",
        wf_heading: "Modern & Scientific Field Care Workflow for Farmers",
        wf_sub: "4 essential steps for sustainable crop yields through timely disease scouting, soil nutrient diagnostics, and eco-friendly IPM:",
        wf_card1_tag: "Step 01 • Scouting",
        wf_card1_title: "Routine Leaf Health Scouting",
        wf_card1_desc: "Field inspection in morning hours, checking leaf discoloration, spindle blast lesions, or cercospora spots with smartphone camera.",
        wf_card1_footer: "✓ Instant AI-powered disease diagnosis",
        wf_card2_tag: "Step 02 • Soil Testing",
        wf_card2_title: "Soil Nutrients & NPK Analysis",
        wf_card2_desc: "Regular testing of Nitrogen (N), Phosphorus (P), Potassium (K), and pH to assess soil health score.",
        wf_card2_footer: "✓ BARC benchmark nutrient deficit assessment",
        wf_card3_tag: "Step 03 • Balanced Dosing",
        wf_card3_title: "Balanced Split Fertilizer Application",
        wf_card3_desc: "Avoiding excess urea while applying balanced split doses of potash, gypsum, and compost to bolster plant immunity.",
        wf_card3_footer: "✓ Precise dosage per bigha or decimal",
        wf_card4_tag: "Step 04 • Integrated IPM",
        wf_card4_title: "Eco-Friendly IPM & Yield Protection",
        wf_card4_desc: "Managing pests using Trichoderma, light traps, and biocontrol agents for residue-free crops and fertile soil.",
        wf_card4_footer: "✓ 30% reduction in chemical costs",
        tractor_title: "Smart farming decisions ensure healthy harvests and a prosperous nation",
        tractor_desc: "Digital diagnostics and balanced fertilizers protect soil fertility and minimize production costs.",
        tractor_tag1: "🌾 25-30% Fertilizer Savings",
        tractor_tag2: "🛡️ 35% Disease Prevention",
        reg_pill: "🇧🇩 Agro-Ecological Research & Real-World Impact across Bangladesh",
        reg_heading: "Why AgriXAI is Reliable & Unique for Crop & Soil Protection",
        reg_sub: "Engineered across Bangladesh Agro-Ecological Zones (AEZ), linking regional soil nutrient disparities with rice and jute disease epidemiology under BARC guidelines.",
        metric1_val: "98.4%",
        metric1_title: "Diagnostic Accuracy",
        metric1_desc: "MobileNetV2 architecture classifying 9 rice & jute disease classes plus healthy leaves.",
        metric2_val: "< 2.5s",
        metric2_title: "Instant Diagnosis",
        metric2_desc: "Grad-CAM visual heatmap & complete dosage prescription delivered in seconds.",
        metric3_val: "25–30%",
        metric3_title: "Fertilizer Cost Savings",
        metric3_desc: "Precise kg dosages computed from soil benchmarks prevent wasteful fertilizer over-application.",
        metric4_val: "35%",
        metric4_title: "Early Disease Prevention",
        metric4_desc: "Balanced soil NPK and optimal pH enhance natural systemic plant resistance.",
        zones_title: "🗺️ Soil & Disease Risk Analysis across 4 Key Agro-Ecological Zones",
        zones_sub: "Targeted field interventions based on regional soil chemistry and pathogen vulnerability:",
        z1_title: "Barind Tract (Rajshahi, Naogaon)",
        z1_soil: "<strong style=\"color: #b45309;\">Soil Characteristics:</strong> Red clay, low moisture retention, acute nitrogen and organic matter deficiency.",
        z1_disease: "<strong style=\"color: #dc2626;\">Disease Risks:</strong> Rice Bacterial Blight & Leaf Blast.",
        z1_sol: "<strong>AgriXAI Solution:</strong> Split urea doses with balanced zinc sulfate application.",
        z2_title: "Haor Basin (Sylhet, Sunamganj)",
        z2_soil: "<strong style=\"color: #b45309;\">Soil Characteristics:</strong> Submerged alluvial silt, severe potassium leaching, acidic soil (pH < 5.5).",
        z2_disease: "<strong style=\"color: #dc2626;\">Disease Risks:</strong> Rice Brown Spot & Seedling Blight.",
        z2_sol: "<strong>AgriXAI Solution:</strong> Enhanced MOP potassium rates and agricultural lime (dolomite).",
        z3_title: "Tista & Floodplain Alluvial (Rangpur, Faridpur)",
        z3_soil: "<strong style=\"color: #b45309;\">Soil Characteristics:</strong> Fertile sandy loam, humid basin, highly favorable for jute yet fungus-prone.",
        z3_disease: "<strong style=\"color: #dc2626;\">Disease Risks:</strong> Jute Stem Rot & Golden Mosaic.",
        z3_sol: "<strong>AgriXAI Solution:</strong> Balanced TSP, gypsum application, and Trichoderma bio-seed treatment.",
        z4_title: "Coastal Saline Zone (Khulna, Barishal)",
        z4_soil: "<strong style=\"color: #b45309;\">Soil Characteristics:</strong> Fluctuating salinity and alkaline/elevated soil pH (> 7.5).",
        z4_disease: "<strong style=\"color: #dc2626;\">Disease Risks:</strong> Rice Tungro Virus & Root Rot.",
        z4_sol: "<strong>AgriXAI Solution:</strong> Gypsum, green manuring (Dhaincha), and salt-tolerant crop varieties.",
        cta_pill: "✨ Smart Agriculture • Digital Bangladesh",
        cta_heading: "The Future of Farming in Your Hands • Complete Crop & Soil Advisory in One Click",
        cta_sub: "No more guesswork—keep every rice and jute field thriving and resilient with AI-driven vision and BARC scientific fertilizer guidance.",
        cta_btn1: "🌾 Start Smart Diagnosis",
        cta_btn2: "📖 Research & Mathematical Basis",
        footer_col1_title: "AgriXAI • Crop Advisor",
        footer_col1_desc: "A trusted, explainable, and soil-nutrient-aware AI platform for farmers and agricultural officers in Bangladesh. Dedicated to rice and jute disease diagnosis and balanced fertilizer management.",
        footer_col2_title: "🔗 Useful Links & Resources",
        footer_link1: "Research & Methodology",
        footer_link2: "Bangladesh Agricultural Research Council (BARC)",
        footer_link3: "Bangladesh Rice Research Institute (BRRI)",
        footer_link4: "Bangladesh Jute Research Institute (BJRI)",
        footer_col3_title: "☎️ Farmer Support & Helplines",
        footer_helpline1: "<strong>Krishi Call Center:</strong> <span style=\"color: var(--green-primary); font-weight: 800; font-size: 0.95rem;\">16123</span> (Toll-Free)",
        footer_helpline2: "<strong>Emergency Helpline:</strong> <span style=\"font-weight: 700;\">999</span> | <strong>Govt Info:</strong> <span style=\"font-weight: 700;\">333</span>",
        footer_helpline3: "<strong>Field Advisory:</strong> Consult your local Sub-Assistant Agriculture Officer (SAAO / DAE).",
        footer_col4_title: "🎓 Research & Supervision",
        footer_researcher: "<strong>Researcher:</strong> <span style=\"color: #1b4332; font-weight: 700;\">Fatema Akter</span>",
        footer_dept: "Department of Computer Science & Engineering<br><strong>Daffodil International University (DIU)</strong>",
        footer_copy: "© 2026 <strong>AgriXAI</strong> • Daffodil International University • An Explainable AI Crop Advisory System",
        footer_tagline: "AgriXAI - Making farmers' lives easy 🌾"
    }
};

document.addEventListener('DOMContentLoaded', () => {
    initEventListeners();
    fetchSampleCatalog();
    syncSliderBadges();

    const savedLang = localStorage.getItem('agrixai_lang') || 'bn';
    if (savedLang === 'en') {
        applyLanguage('en');
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function initEventListeners() {
    // Crop Switcher Cards
    document.querySelectorAll('.crop-card-button').forEach(btn => {
        btn.addEventListener('click', () => {
            const crop = btn.dataset.crop;
            switchCrop(crop);
        });
    });

    // Language Toggle
    const langBtn = document.getElementById('btn-lang-toggle');
    if (langBtn) {
        langBtn.addEventListener('click', toggleLanguage);
    }

    // Image Upload Zone
    const dropzone = document.getElementById('leaf-dropzone');
    const fileInput = document.getElementById('leaf-file-input');
    const browseBtn = document.getElementById('btn-browse-file');

    if (dropzone && fileInput) {
        dropzone.addEventListener('click', () => fileInput.click());
        if (browseBtn) browseBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            fileInput.click();
        });

        dropzone.addEventListener('dragover', (e) => {
            e.preventDefault();
            dropzone.classList.add('dragover');
        });
        dropzone.addEventListener('dragleave', () => dropzone.classList.remove('dragover'));
        dropzone.addEventListener('drop', (e) => {
            e.preventDefault();
            dropzone.classList.remove('dragover');
            if (e.dataTransfer.files && e.dataTransfer.files[0]) {
                handleUserImageUpload(e.dataTransfer.files[0]);
            }
        });
        fileInput.addEventListener('change', (e) => {
            if (e.target.files && e.target.files[0]) {
                handleUserImageUpload(e.target.files[0]);
            }
        });
    }

    // Remove leaf preview
    const removeBtn = document.getElementById('btn-remove-leaf');
    if (removeBtn) {
        removeBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            clearUploadedImage();
        });
    }

    // Sliders Live Update
    ['slider-n', 'slider-p', 'slider-k', 'slider-ph', 'input-land-amount'].forEach(id => {
        const el = document.getElementById(id);
        if (el) {
            el.addEventListener('input', () => {
                syncSliderBadges();
                if (lastResultData) liveSoilRecalculation();
            });
        }
    });

    ['select-prev-crop', 'select-land-unit'].forEach(id => {
        const el = document.getElementById(id);
        if (el) {
            el.addEventListener('change', () => {
                if (lastResultData) liveSoilRecalculation();
            });
        }
    });

    // Form Submit
    const form = document.getElementById('diagnose-form');
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            submitDiagnosis();
        });
    }

    // Print Button
    const printBtn = document.getElementById('btn-print-report');
    if (printBtn) {
        printBtn.addEventListener('click', () => window.print());
    }
}

function syncSliderBadges() {
    const n = document.getElementById('slider-n').value;
    const p = document.getElementById('slider-p').value;
    const k = parseFloat(document.getElementById('slider-k').value).toFixed(2);
    const ph = parseFloat(document.getElementById('slider-ph').value).toFixed(1);

    document.getElementById('val-badge-n').textContent = `${n} ppm`;
    document.getElementById('val-badge-p').textContent = `${p} ppm`;
    document.getElementById('val-badge-k').textContent = `${k} meq`;
    document.getElementById('val-badge-ph').textContent = `${ph}`;
}

function updateBenchmarkHints(crop, lang) {
    const isBn = lang === 'bn';
    const nEl = document.getElementById('bench-hint-n');
    const pEl = document.getElementById('bench-hint-p');
    const kEl = document.getElementById('bench-hint-k');
    const phEl = document.getElementById('bench-hint-ph');

    if (crop === 'rice') {
        if (nEl) nEl.innerHTML = `<span>${isBn ? 'ঘাটতি: &lt;25' : 'Deficient: &lt;25'}</span><span>${isBn ? 'আদর্শ: 25-45 ppm' : 'Optimum: 25-45 ppm'}</span>`;
        if (pEl) pEl.innerHTML = `<span>${isBn ? 'ঘাটতি: &lt;12' : 'Deficient: &lt;12'}</span><span>${isBn ? 'আদর্শ: 14-24 ppm' : 'Optimum: 14-24 ppm'}</span>`;
        if (kEl) kEl.innerHTML = `<span>${isBn ? 'ঘাটতি: &lt;0.15' : 'Deficient: &lt;0.15'}</span><span>${isBn ? 'আদর্শ: 0.18-0.28' : 'Optimum: 0.18-0.28'}</span>`;
        if (phEl) phEl.innerHTML = `<span>${isBn ? 'অম্লীয়: &lt;5.5' : 'Acidic: &lt;5.5'}</span><span>${isBn ? 'অনুকূল: 5.8-6.8' : 'Optimum: 5.8-6.8'}</span>`;
    } else {
        if (nEl) nEl.innerHTML = `<span>${isBn ? 'ঘাটতি: &lt;30' : 'Deficient: &lt;30'}</span><span>${isBn ? 'আদর্শ: 30-50 ppm' : 'Optimum: 30-50 ppm'}</span>`;
        if (pEl) pEl.innerHTML = `<span>${isBn ? 'ঘাটতি: &lt;10' : 'Deficient: &lt;10'}</span><span>${isBn ? 'আদর্শ: 12-22 ppm' : 'Optimum: 12-22 ppm'}</span>`;
        if (kEl) kEl.innerHTML = `<span>${isBn ? 'ঘাটতি: &lt;0.18' : 'Deficient: &lt;0.18'}</span><span>${isBn ? 'আদর্শ: 0.20-0.30' : 'Optimum: 0.20-0.30'}</span>`;
        if (phEl) phEl.innerHTML = `<span>${isBn ? 'অম্লীয়: &lt;5.8' : 'Acidic: &lt;5.8'}</span><span>${isBn ? 'অনুকূল: 6.0-7.2' : 'Optimum: 6.0-7.2'}</span>`;
    }
}

function switchCrop(crop) {
    selectedCrop = crop;
    document.querySelectorAll('.crop-card-button').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.crop === crop);
    });

    if (crop === 'rice') {
        document.getElementById('slider-n').value = 48;
        document.getElementById('slider-p').value = 16;
        document.getElementById('slider-k').value = 0.14;
        document.getElementById('slider-ph').value = 5.6;
        document.getElementById('select-prev-crop').value = 'boro_rice';
    } else {
        document.getElementById('slider-n').value = 42;
        document.getElementById('slider-p').value = 15;
        document.getElementById('slider-k').value = 0.16;
        document.getElementById('slider-ph').value = 6.2;
        document.getElementById('select-prev-crop').value = 'potato';
    }
    syncSliderBadges();
    updateBenchmarkHints(crop, currentLang);
    renderSampleTrack();

    const first = allSamples.find(s => s.crop === crop);
    if (first) selectDemoSample(first.id, first.preset);
}

function fetchSampleCatalog() {
    fetch('/api/samples/')
        .then(res => res.json())
        .then(data => {
            if (data.status === 'success') {
                allSamples = data.samples;
                renderSampleTrack();
                selectDemoSample('rice_blast.jpg', 'rice_blast');
            }
        })
        .catch(err => console.error('Error fetching sample catalog:', err));
}

function renderSampleTrack() {
    const track = document.getElementById('samples-track');
    if (!track) return;
    track.innerHTML = '';

    const filtered = allSamples.filter(s => s.crop === selectedCrop);
    filtered.forEach(s => {
        const chip = document.createElement('div');
        chip.className = `sample-photo-chip ${s.id === selectedSampleFile ? 'active' : ''}`;
        chip.dataset.sampleId = s.id;
        chip.dataset.preset = s.preset;
        chip.innerHTML = `
            <img src="/static/images/samples/${s.id}" alt="${s.name_en}" loading="lazy">
            <span>${currentLang === 'bn' ? s.name_bn : s.name_en}</span>
        `;
        chip.addEventListener('click', () => selectDemoSample(s.id, s.preset));
        track.appendChild(chip);
    });
}

function selectDemoSample(sampleId, presetClass) {
    uploadedUserFile = null;
    selectedSampleFile = sampleId;
    selectedPresetClass = presetClass;

    document.querySelectorAll('.sample-photo-chip').forEach(c => {
        c.classList.toggle('active', c.dataset.sampleId === sampleId);
    });

    const fileInput = document.getElementById('leaf-file-input');
    if (fileInput) fileInput.value = '';

    const previewBox = document.getElementById('preview-box');
    const previewImg = document.getElementById('preview-leaf-img');
    const uploadPrompt = document.getElementById('upload-prompt-content');

    if (previewBox && previewImg && uploadPrompt) {
        previewImg.src = `/static/images/samples/${sampleId}`;
        previewBox.style.display = 'block';
        uploadPrompt.style.display = 'none';
    }

    // Set typical soil scenarios matching disease physiology
    if (presetClass === 'rice_blast') {
        document.getElementById('slider-n').value = 54;
        document.getElementById('slider-k').value = 0.13;
        document.getElementById('slider-ph').value = 5.7;
    } else if (presetClass === 'rice_bacterial_blight') {
        document.getElementById('slider-n').value = 58;
        document.getElementById('slider-k').value = 0.14;
        document.getElementById('slider-ph').value = 6.0;
    } else if (presetClass === 'rice_brown_spot') {
        document.getElementById('slider-n').value = 24;
        document.getElementById('slider-k').value = 0.10;
        document.getElementById('slider-ph').value = 5.1;
    } else if (presetClass === 'rice_healthy' || presetClass === 'jute_healthy') {
        document.getElementById('slider-n').value = 35;
        document.getElementById('slider-p').value = 18;
        document.getElementById('slider-k').value = 0.22;
        document.getElementById('slider-ph').value = 6.4;
    } else if (presetClass === 'jute_cercospora') {
        document.getElementById('slider-k').value = 0.12;
        document.getElementById('slider-ph').value = 5.4;
    } else if (presetClass === 'jute_golden_mosaic') {
        document.getElementById('slider-n').value = 52;
    } else if (presetClass === 'jute_stem_rot') {
        document.getElementById('slider-k').value = 0.11;
        document.getElementById('slider-ph').value = 5.3;
    }
    syncSliderBadges();
}

function handleUserImageUpload(file) {
    if (!file || !file.type.startsWith('image/')) {
        alert(currentLang === 'bn' ? 'অনুগ্রহ করে একটি ছবি ফাইল আপলোড করুন (JPG, PNG, JPEG)।' : 'Please upload a valid image file (JPG, PNG).');
        return;
    }

    uploadedUserFile = file;
    selectedSampleFile = null;
    selectedPresetClass = null;
    document.querySelectorAll('.sample-photo-chip').forEach(c => c.classList.remove('active'));

    const reader = new FileReader();
    reader.onload = (e) => {
        const previewBox = document.getElementById('preview-box');
        const previewImg = document.getElementById('preview-leaf-img');
        const uploadPrompt = document.getElementById('upload-prompt-content');

        if (previewBox && previewImg && uploadPrompt) {
            previewImg.src = e.target.result;
            previewBox.style.display = 'block';
            uploadPrompt.style.display = 'none';
        }
    };
    reader.readAsDataURL(file);
}

function clearUploadedImage() {
    uploadedUserFile = null;
    const fileInput = document.getElementById('leaf-file-input');
    if (fileInput) fileInput.value = '';

    const previewBox = document.getElementById('preview-box');
    const uploadPrompt = document.getElementById('upload-prompt-content');
    if (previewBox && uploadPrompt) {
        previewBox.style.display = 'none';
        uploadPrompt.style.display = 'block';
    }

    const first = allSamples.find(s => s.crop === selectedCrop);
    if (first) selectDemoSample(first.id, first.preset);
}

function submitDiagnosis() {
    const spinner = document.getElementById('spinner-loading');
    const resultsView = document.getElementById('diagnostic-results-view');
    const submitBtn = document.getElementById('btn-submit-main');

    spinner.style.display = 'block';
    submitBtn.disabled = true;

    const formData = new FormData();
    formData.append('crop', selectedCrop);
    formData.append('nitrogen', document.getElementById('slider-n').value);
    formData.append('phosphorus', document.getElementById('slider-p').value);
    formData.append('potassium', document.getElementById('slider-k').value);
    formData.append('ph', document.getElementById('slider-ph').value);
    formData.append('prev_crop', document.getElementById('select-prev-crop').value);
    formData.append('land_unit', document.getElementById('select-land-unit').value);
    formData.append('land_amount', document.getElementById('input-land-amount').value);

    const fileInput = document.getElementById('leaf-file-input');
    if (fileInput && fileInput.files && fileInput.files[0]) {
        formData.append('image', fileInput.files[0]);
    } else if (uploadedUserFile) {
        formData.append('image', uploadedUserFile);
    } else if (selectedSampleFile) {
        formData.append('sample_file', selectedSampleFile);
        if (selectedPresetClass) {
            formData.append('preset_class', selectedPresetClass);
        }
    }

    fetch('/api/diagnose/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken') || ''
        },
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        spinner.style.display = 'none';
        submitBtn.disabled = false;

        if (data.status === 'success') {
            lastResultData = data;
            renderDiagnosisResults(data);
            resultsView.style.display = 'block';
            resultsView.scrollIntoView({ behavior: 'smooth', block: 'start' });
        } else {
            alert('Error running analysis: ' + (data.message || 'Unknown error'));
        }
    })
    .catch(err => {
        spinner.style.display = 'none';
        submitBtn.disabled = false;
        alert('Server communication error: ' + err.message);
    });
}

function renderDiagnosisResults(data) {
    const ai = data.ai_detection;
    const soil = data.soil_analysis;
    const link = data.disease_soil_link;
    const adv = data.advisory;
    const disease = adv.disease_info;
    const isBn = currentLang === 'bn';

    // Step 1: Disease Info
    document.getElementById('res-disease-title').textContent = isBn ? disease.name_bn : disease.name_en;
    document.getElementById('res-sci-title').textContent = disease.scientific_name;
    document.getElementById('res-conf-tag').textContent = `${ai.primary_confidence}% ${isBn ? 'নির্ভুলতা' : 'Confidence'}`;

    // Disease type
    let typeDisplay = disease.type;
    if (!isBn) {
        if (disease.type.includes('Fungal')) typeDisplay = 'Fungal Disease';
        else if (disease.type.includes('Bacterial')) typeDisplay = 'Bacterial Disease';
        else if (disease.type.includes('Viral')) typeDisplay = 'Viral Disease';
        else if (disease.type.includes('Healthy')) typeDisplay = 'Healthy Leaf';
    }
    document.getElementById('res-type-tag').textContent = typeDisplay;

    // Severity tag
    let sevVal = disease.severity;
    if (!isBn) {
        if (sevVal.includes('High') || sevVal.includes('উচ্চ')) sevVal = 'High';
        else if (sevVal.includes('Moderate') || sevVal.includes('মাঝারি')) sevVal = 'Moderate';
        else if (sevVal.includes('Severe') || sevVal.includes('মারাত্মক')) sevVal = 'Severe';
        else sevVal = 'None';
    }
    document.getElementById('res-severity-tag').textContent = `${isBn ? 'তীব্রতা:' : 'Severity:'} ${sevVal}`;

    // Probabilities breakdown
    const probContainer = document.getElementById('prob-bars-wrap');
    if (probContainer) {
        probContainer.innerHTML = '';
        ai.probabilities.slice(0, 3).forEach(p => {
            const row = document.createElement('div');
            row.style.marginBottom = '8px';
            row.innerHTML = `
                <div style="display:flex; justify-content:space-between; font-size:0.8rem; font-weight:700; margin-bottom:2px;">
                    <span>${isBn ? p.name_bn : p.name_en}</span>
                    <span>${p.confidence}%</span>
                </div>
                <div style="background:#e5e7eb; border-radius:6px; height:8px; overflow:hidden;">
                    <div style="background:var(--green-primary); width:${p.confidence}%; height:100%; border-radius:6px;"></div>
                </div>
            `;
            probContainer.appendChild(row);
        });
    }

    // Step 2: Grad-CAM Explainability Visuals
    document.getElementById('gradcam-orig-img').src = ai.gradcam.orig_b64;
    document.getElementById('gradcam-heat-img').src = ai.gradcam.heatmap_b64;
    document.getElementById('gradcam-overlay-img').src = ai.gradcam.overlay_b64;

    document.getElementById('xai-focal-text').textContent = `${ai.gradcam.infected_area_pct}%`;
    document.getElementById('xai-explanation-para').textContent = isBn ? ai.gradcam.explanation_bn : (ai.gradcam.explanation_en || ai.gradcam.explanation_bn);

    // Step 3: Disease-Soil Linkage
    document.getElementById('link-causal-summary-p').textContent = isBn ? link.causal_summary_bn : (link.causal_summary_en || link.causal_summary_bn);
    const factorList = document.getElementById('link-factors-wrap');
    if (factorList) {
        factorList.innerHTML = '';
        const factors = [...(link.causal_factors || []), ...(link.aggravating_factors || [])];
        if (factors.length > 0) {
            factors.forEach(f => {
                const item = document.createElement('div');
                item.style.background = '#fef2f2';
                item.style.border = '1px solid #fecaca';
                item.style.padding = '8px 12px';
                item.style.borderRadius = '10px';
                item.style.fontSize = '0.84rem';
                item.style.color = '#991b1b';
                item.style.display = 'flex';
                item.style.alignItems = 'flex-start';
                item.style.gap = '8px';
                const fText = isBn ? f.factor_bn : (f.factor_en || f.factor_bn);
                item.innerHTML = `<span>⚠️</span> <span>${fText}</span>`;
                factorList.appendChild(item);
            });
        } else {
            const item = document.createElement('div');
            item.style.background = '#f0fdf4';
            item.style.border = '1px solid #bbf7d0';
            item.style.padding = '8px 12px';
            item.style.borderRadius = '10px';
            item.style.fontSize = '0.84rem';
            item.style.color = '#166534';
            item.innerHTML = `<span>✅</span> <span>${isBn ? 'কোনো তীব্র পুষ্টি ভারসাম্যহীনতা নেই।' : 'No severe nutrient imbalance.'}</span>`;
            factorList.appendChild(item);
        }
    }

    // Step 4: Soil Health Scorecard
    const scoreCircle = document.getElementById('soil-score-circle');
    if (scoreCircle) {
        scoreCircle.style.background = soil.grade_color;
        document.getElementById('soil-score-num').textContent = Math.round(soil.final_score);
    }
    document.getElementById('soil-grade-title').textContent = isBn ? soil.grade_bn : soil.grade_en;
    document.getElementById('soil-grade-title').style.color = soil.grade_color;
    document.getElementById('soil-summary-p').textContent = isBn ? (soil.health_summary_bn || soil.summary_bn) : (soil.health_summary_en || soil.summary_en || soil.grade_en);

    renderNutrientStatusCards(soil.nutrients);

    // Step 5: Fertilizer Prescription Table
    renderFertilizerPrescription(adv.fertilizer_prescription);

    // Treatment Action Quad
    const rec = isBn ? (disease.recommendation_bn || {}) : (disease.recommendation_en || disease.recommendation_bn || {});
    document.getElementById('adv-immediate-p').textContent = rec.immediate_action || '';
    document.getElementById('adv-chemical-p').textContent = rec.chemical_treatment || '';
    document.getElementById('adv-organic-p').textContent = rec.organic_treatment || '';
    document.getElementById('adv-preventive-p').textContent = rec.preventive_care || '';
}

function renderNutrientStatusCards(nutrients) {
    const container = document.getElementById('nutrients-status-grid');
    if (!container) return;
    container.innerHTML = '';
    const isBn = currentLang === 'bn';

    const items = [
        { label: isBn ? 'নাইট্রোজেন (N)' : 'Nitrogen (N)', res: nutrients.nitrogen, unit: 'ppm' },
        { label: isBn ? 'ফসফরাস (P)' : 'Phosphorus (P)', res: nutrients.phosphorus, unit: 'ppm' },
        { label: isBn ? 'পটাশিয়াম (K)' : 'Potassium (K)', res: nutrients.potassium, unit: 'meq' },
        { label: isBn ? 'অম্লতা (pH)' : 'Soil pH', res: nutrients.ph, unit: '' }
    ];

    items.forEach(it => {
        const div = document.createElement('div');
        div.style.background = '#ffffff';
        div.style.border = '1px solid var(--green-border)';
        div.style.padding = '10px 12px';
        div.style.borderRadius = '10px';
        const statusText = isBn ? it.res.status_bn : (it.res.status_en || it.res.status_bn);
        div.innerHTML = `
            <div style="display:flex; justify-content:space-between; font-size:0.8rem; font-weight:700; margin-bottom:4px;">
                <span>${it.label}</span>
                <span style="color:${it.res.color}; font-weight:800;">${statusText}</span>
            </div>
            <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#6b7280; margin-bottom:4px;">
                <span>${isBn ? 'মান:' : 'Value:'} ${it.res.value} ${it.unit}</span>
                <span>${isBn ? 'আদর্শ:' : 'Optimum:'} ${it.res.benchmark.opt_min} - ${it.res.benchmark.opt_max}</span>
            </div>
            <div style="background:#e5e7eb; height:6px; border-radius:4px; overflow:hidden;">
                <div style="background:${it.res.color}; width:${Math.min(100, Math.max(15, it.res.score))}%; height:100%; border-radius:4px;"></div>
            </div>
        `;
        container.appendChild(div);
    });
}

function renderFertilizerPrescription(rxData) {
    const tbody = document.getElementById('rx-table-body');
    if (!tbody) return;
    tbody.innerHTML = '';
    const isBn = currentLang === 'bn';

    rxData.prescription.forEach(row => {
        const tr = document.createElement('tr');
        const fertName = isBn ? row.fertilizer_bn : (row.fertilizer_en || row.fertilizer_bn);
        const fertRole = isBn ? row.role_bn : (row.role_en || row.role_bn);
        const fertTiming = isBn ? row.timing_bn : (row.timing_en || row.timing_bn);
        const fertNote = isBn ? row.note_bn : (row.note_en || row.note_bn);
        const doseUnit = isBn ? 'কেজি' : 'kg';

        tr.innerHTML = `
            <td><strong>${fertName}</strong><br><small style="color:#6b7280;">${fertRole}</small></td>
            <td class="dose-highlight">${row.dose_kg} ${doseUnit}</td>
            <td>${fertTiming}</td>
            <td><small style="color:#4b5563;">${fertNote}</small></td>
        `;
        tbody.appendChild(tr);
    });
}

function liveSoilRecalculation() {
    if (!lastResultData) return;

    const payload = {
        crop: selectedCrop,
        nitrogen: document.getElementById('slider-n').value,
        phosphorus: document.getElementById('slider-p').value,
        potassium: document.getElementById('slider-k').value,
        ph: document.getElementById('slider-ph').value,
        prev_crop: document.getElementById('select-prev-crop').value,
        disease_id: lastResultData.ai_detection.primary_class,
        land_unit: document.getElementById('select-land-unit').value,
        land_amount: document.getElementById('input-land-amount').value
    };

    fetch('/api/recalculate-soil/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') || ''
        },
        body: JSON.stringify(payload)
    })
    .then(res => res.json())
    .then(data => {
        if (data.status === 'success') {
            lastResultData.soil_analysis = data.soil_analysis;
            lastResultData.disease_soil_link = data.disease_soil_link;
            lastResultData.advisory = data.advisory;
            renderDiagnosisResults(lastResultData);
        }
    })
    .catch(err => console.error('Error during live recalculation:', err));
}

function applyLanguage(lang) {
    currentLang = lang;
    document.documentElement.lang = lang;
    try {
        localStorage.setItem('agrixai_lang', lang);
    } catch(e) {}

    const langBtn = document.getElementById('btn-lang-toggle');
    if (langBtn) {
        langBtn.textContent = lang === 'bn' ? 'English' : 'বাংলা';
    }

    // Translate all elements with data-i18n
    const dict = UI_TRANSLATIONS[lang] || UI_TRANSLATIONS.bn;
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key] !== undefined) {
            el.innerHTML = dict[key];
        }
    });

    // Translate previous crop dropdown options
    const prevSelect = document.getElementById('select-prev-crop');
    if (prevSelect) {
        Array.from(prevSelect.options).forEach(opt => {
            const name = lang === 'bn' ? opt.getAttribute('data-name-bn') : opt.getAttribute('data-name-en');
            if (name) opt.textContent = name;
        });
    }

    // Update benchmark hints based on crop and active language
    updateBenchmarkHints(selectedCrop, lang);

    // Re-render sample demo cards with localized titles
    renderSampleTrack();

    // If results are visible, update results in active language
    if (lastResultData) {
        renderDiagnosisResults(lastResultData);
    }
}

function toggleLanguage() {
    applyLanguage(currentLang === 'bn' ? 'en' : 'bn');
}
