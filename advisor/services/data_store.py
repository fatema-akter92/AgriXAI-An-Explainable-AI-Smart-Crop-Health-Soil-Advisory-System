"""
data_store.py
Knowledge base for Rice and Jute Leaf Diseases, BARC Soil Standards,
and Crop Nutrient-Removal Rates.
Based on Bangladesh Agricultural Research Council (BARC) Fertilizer Recommendation Guide
and SRDI Upazila-level Soil & Agricultural Reports.
"""

DISEASE_DATABASE = {
    # ------------------ RICE (ধান) ------------------
    "rice_blast": {
        "crop": "rice",
        "crop_bn": "ধান",
        "crop_en": "Rice",
        "disease_id": "rice_blast",
        "name_bn": "ধানের ব্লাস্ট রোগ (Leaf Blast)",
        "name_en": "Rice Leaf Blast",
        "scientific_name": "Magnaporthe oryzae (Pyricularia oryzae)",
        "type": "Fungal (ছত্রাকজনিত)",
        "severity": "উচ্চ (High)",
        "symptoms_bn": "পাতায় ছোট ছোট স্পিন্ডল বা চোখের আকৃতির দাগ দেখা যায়, যার কেন্দ্র ধূসর এবং প্রান্ত বাদামী বা লালচে বাদামী হয়। রোগ তীব্র হলে পাতা পুড়ে শুকিয়ে যায়।",
        "symptoms_en": "Spindle-shaped or eye-shaped lesions with grayish centers and brown/reddish-brown borders appear on leaves. Under high severity, leaves wither and dry up.",
        "soil_link_bn": "মাটিতে অতিরিক্ত নাইট্রোজেন (ইউরিয়া) সার প্রয়োগ করলে উদ্ভিদের কোষ প্রাচীর নরম হয়ে যায়, যা ব্লাস্ট ছত্রাকের আক্রমণ বহুলাংশে বাড়িয়ে দেয়। পটাশিয়ামের ঘাটতি থাকলে গাছের রোগ প্রতিরোধ ক্ষমতা ভেঙে পড়ে।",
        "soil_link_en": "Excessive nitrogen (urea) application makes leaf tissues tender and succulent, drastically increasing vulnerability to blast fungal hyphae. Potassium deficiency further impairs plant resistance.",
        "recommendation_bn": {
            "immediate_action": "১. জমিতে ইউরিয়া সারের উপরিপ্রয়োগ অবিলম্বে সম্পূর্ণ বন্ধ রাখুন।\n২. জমিতে পর্যাপ্ত পানি ধরে রাখুন (মাটি শুকিয়ে ফেটে যেতে দেবেন না)।",
            "chemical_treatment": "ট্রাইসাইক্লাজোল (যেমন: ট্রুপার ৭৫ ডব্লিউপি / বাণ ৭৫ ডব্লিউপি) প্রতি লিটার পানিতে ০.৭৫ গ্রাম অথবা ট্রাইসাইক্লাজোল + ডাইফেনোকোনাজোল স্প্রে করুন। আক্রমণ বেশি হলে ৫-৭ দিন পর পুনরায় স্প্রে করুন।",
            "organic_treatment": "এক কেজি কাঁচা গোবর ও এক লিটার গোমূত্র ১০ লিটার পানিতে মিশিয়ে ছেঁকে স্প্রে করলে ছত্রাক প্রতিরোধে কার্যকর হয়। এছাড়া ট্রাইকোডার্মা মিশ্রণ ব্যবহার করুন।",
            "preventive_care": "সুষম মাত্রায় পটাশ সার ব্যবহার করুন। প্রতিরোধী জাত (যেমন: ব্রি ধান ৮১, ব্রি ধান ৮৯) চাষ করুন।"
        },
        "recommendation_en": {
            "immediate_action": "1. Immediately halt all urea (nitrogen) top-dressing on the field.\n2. Maintain adequate standing water depth to keep soil moist.",
            "chemical_treatment": "Spray Tricyclazole (e.g., Trooper 75 WP / Baan 75 WP) @ 0.75 g/L water or Tricyclazole + Difenoconazole. Repeat after 5-7 days if severe.",
            "organic_treatment": "Spray filtered solution of fresh cow dung and urine (1kg dung + 1L urine in 10L water). Apply Trichoderma-enriched compost.",
            "preventive_care": "Apply balanced potassium (MOP) fertilizer. Cultivate blast-resistant modern varieties (BRRI dhan 81, BRRI dhan 89)."
        },
        "fertilizer_adjustment": {
            "urea": "অতিরিক্ত নাইট্রোজেনের কারণে ইউরিয়া ৩০%-৫০% কমাতে হবে",
            "mop": "গাছের প্রতিরোধ ক্ষমতা বাড়াতে পটাশ (এমওপি) ২০% বৃদ্ধি করুন",
            "gypsum": "সালফারের স্বাভাবিক মাত্রা বজায় রাখুন",
            "zinc": "জিংক সালফেট ১-২ কেজি/বিঘা প্রয়োগ করুন"
        }
    },
    "rice_bacterial_blight": {
        "crop": "rice",
        "crop_bn": "ধান",
        "crop_en": "Rice",
        "disease_id": "rice_bacterial_blight",
        "name_bn": "ধানের ব্যাকটেরিয়াল লিফ ব্লাইট (পাতা পোড়া রোগ)",
        "name_en": "Bacterial Leaf Blight (BLB)",
        "scientific_name": "Xanthomonas oryzae pv. oryzae",
        "type": "Bacterial (ব্যাকটেরিয়াজনিত)",
        "severity": "উচ্চ (High)",
        "symptoms_bn": "পাতার ডগা বা কিনারা থেকে ঢেউ খেলানো হলুদ বা ধূসর রেখা নিচের দিকে নামতে থাকে। আক্রান্ত অংশ দ্রুত শুকিয়ে খড়ের রঙ ধারণ করে।",
        "symptoms_en": "Water-soaked to yellowish-green wavy stripes start along leaf margins, spreading downward. Severely affected leaves turn straw-colored and dry out.",
        "soil_link_bn": "অতিরিক্ত ইউরিয়া প্রয়োগ ও অনুপযুক্ত পটাশ অনুপাত ব্যাকটেরিয়ার বিস্তারকে অত্যন্ত দ্রুত করে। বিশেষ করে ঝড়ো হাওয়া বা বৃষ্টির পর জমিতে অতিরিক্ত নাইট্রোজেন থাকলে জীবাণু সহজেই প্রবেশ করে।",
        "soil_link_en": "Excessive nitrogen coupled with low potassium creates lush, fragile leaf hydathodes that bacterial pathogens easily penetrate, especially after rainfall or wind damage.",
        "recommendation_bn": {
            "immediate_action": "১. জমিতে ইউরিয়ার উপরিপ্রয়োগ সম্পূর্ণ বন্ধ করুন।\n২. জমি থেকে অতিরিক্ত পানি নিষ্কাশন করে ২-৩ দিন শুকিয়ে আবার সেচ দিন।",
            "chemical_treatment": "কপার হাইড্রোক্সাইড (যেমন: কুপ্রোফিক্স) প্রতি লিটার পানিতে ২ গ্রাম অথবা বিসমারথিয়াজল (ব্যাকট্রোবান) ১ গ্রাম/লিটার হারে স্প্রে করুন। প্রতি বিঘায় ৬০ গ্রাম পটাশ ও ৬০ গ্রাম থিওভিট মিশিয়ে স্প্রে করলেও সুফল পাওয়া যায়।",
            "organic_treatment": "নিমপাতার রস ও গোমূত্রের নির্যাস পাতায় স্প্রে করলে ব্যাকটেরিয়ার বিস্তার হ্রাস পায়।",
            "preventive_care": "পরবর্তী মৌসুমে সুষম সার ব্যবস্থাপনা গ্রহণ করুন এবং বিঘা প্রতি ৫ কেজি অতিরিক্ত এমওপি সার ব্যবহার করুন।"
        },
        "recommendation_en": {
            "immediate_action": "1. Completely stop urea top-dressing.\n2. Drain standing water from the field, allow the surface to aerate for 2-3 days, then re-irrigate.",
            "chemical_treatment": "Spray Copper Hydroxide (e.g., Cuprofix / Kocide) @ 2 g/L water or Bismerthiazol (Bactroban) @ 1 g/L. Spraying 60g MOP + 60g Thiovit per bigha also suppresses bacterial spread.",
            "organic_treatment": "Spray aqueous neem leaf juice mixed with cow urine extract to curb bacterial proliferation.",
            "preventive_care": "Adopt balanced fertilizer practices in the next crop cycle and incorporate an additional 5 kg/bigha MOP."
        },
        "fertilizer_adjustment": {
            "urea": "ইউরিয়া টপ-ড্রেসিং স্থগিত রাখুন",
            "mop": "পটাশ সার বিঘা প্রতি ৪-৫ কেজি ছিটিয়ে দিন",
            "gypsum": "স্বাভাবিক প্রয়োগ",
            "zinc": "প্রয়োজন অনুযায়ী"
        }
    },
    "rice_brown_spot": {
        "crop": "rice",
        "crop_bn": "ধান",
        "crop_en": "Rice",
        "disease_id": "rice_brown_spot",
        "name_bn": "ধানের বাদামী দাগ রোগ (Brown Spot)",
        "name_en": "Rice Brown Spot",
        "scientific_name": "Bipolaris oryzae (Cochliobolus miyabeanus)",
        "type": "Fungal (ছত্রাকজনিত / পুষ্টিহীনতাজনিত)",
        "severity": "মাঝারি (Moderate)",
        "symptoms_bn": "পাতায় অসংখ্য ছোট ছোট বৃত্তাকার বা ডিম্বাকৃতির গাঢ় বাদামী রঙের তিলের মতো দাগ পড়ে। দাগের চারপাশে হলুদ বলয় (Halo) দেখা যায়।",
        "symptoms_en": "Numerous round to oval dark brown spots resembling sesame seeds with yellowish halos on the leaves. Common in nutrient-depleted, stressed soils.",
        "soil_link_bn": "এই রোগটিকে 'দরিদ্র মাটির রোগ' বলা হয়। মাটিতে পটাশিয়াম (K), সিলিকন এবং জৈব পদার্থের তীব্র ঘাটতি থাকলে এবং মাটি অম্লীয় হলে (pH < ৫.৫) এই রোগের প্রকোপ নাটকীয়ভাবে বাড়ে।",
        "soil_link_en": "Often termed a 'poor soil disease'. Strongly correlated with acute potassium deficiency, low micronutrient (Mn/Si) availability, and high soil acidity.",
        "recommendation_bn": {
            "immediate_action": "১. জমিতে সুষম পুষ্টি নিশ্চিত করতে ইউরিয়ার সাথে সমপরিমাণ পটাশ স্প্রে করুন।\n২. জমিতে পর্যাপ্ত সেচ দিন, শুকনো মাটিতে এই রোগ বাড়ে।",
            "chemical_treatment": "ম্যানকোজেব (যেমন: ডাইথেন এম-৪৫) প্রতি লিটার পানিতে ২ গ্রাম অথবা কার্বেনডাজিম (নোইন ৫০ ডব্লিউপি) ১ গ্রাম/লিটার মিশিয়ে ৭ দিন পর পর দুইবার স্প্রে করুন।",
            "organic_treatment": "জৈব সার বা ভার্মিকম্পোস্ট প্রয়োগ করুন। কাঠকয়লার ছাই (পটাশিয়ামের প্রাকৃতিক উৎস) জমিতে ছিটিয়ে দিলে প্রতিরোধ বাড়ে।",
            "preventive_care": "মাটির স্বাস্থ্য ফেরাতে বিঘা প্রতি ১ টন গোবর সার বা ভার্মিকম্পোস্ট এবং সুপারিশকৃত মাত্রায় পটাশ প্রয়োগ করুন।"
        },
        "recommendation_en": {
            "immediate_action": "1. Foliar spray equal proportions of urea and potash to restore foliar nutrient balance.\n2. Provide adequate irrigation; moisture stress aggravates brown spot.",
            "chemical_treatment": "Spray Mancozeb (e.g., Dithane M-45) @ 2 g/L water or Carbendazim (Knowin 50 WP) @ 1 g/L twice at 7-day intervals.",
            "organic_treatment": "Apply organic manure or vermicompost. Broadcast wood ash (natural potassium source) over the field.",
            "preventive_care": "Incorporate 1 ton/bigha farmyard manure/vermicompost and apply the recommended dose of potash to restore soil health."
        },
        "fertilizer_adjustment": {
            "urea": "স্বাভাবিক মাত্রায় সুষম প্রয়োগ",
            "mop": "পটাশ (এমওপি) ৩০% বৃদ্ধি করতে হবে",
            "gypsum": "বিঘা প্রতি ৮-১০ কেজি প্রয়োগ",
            "zinc": "চিলেটেড জিংক ১ গ্রাম/লিটার স্প্রে"
        }
    },
    "rice_tungro": {
        "crop": "rice",
        "crop_bn": "ধান",
        "crop_en": "Rice",
        "disease_id": "rice_tungro",
        "name_bn": "ধানের টুংরো রোগ (Rice Tungro)",
        "name_en": "Rice Tungro Disease",
        "scientific_name": "Rice tungro bacilliform virus (RTBV) + Spherical virus (RTSV)",
        "type": "Viral (ভাইরাসজনিত - সবুজ পাতা ফড়িং বাহক)",
        "severity": "মারাত্মক (Severe)",
        "symptoms_bn": "পাতা আগা থেকে শুরু করে কমলা-হলুদ বা বাদামী বর্ণ ধারণ করে। গাছ খাটো হয়ে যায় এবং কুশি সংখ্যা কমে শক্ত হয়ে দাঁড়িয়ে থাকে।",
        "symptoms_en": "Leaves display bright orange-yellow discoloration starting from tips. Severe stunting of plants and drastically reduced tillering.",
        "soil_link_bn": "মাটিতে নাইট্রোজেনের ভারসাম্যহীনতা গাছকে দ্রুত দুর্বল করে এবং সবুজ পাতা ফড়িং (Nephotettix virescens) পোকার আক্রমণকে ত্বরান্বিত করে, যা এই ভাইরাসের প্রধান বাহক।",
        "soil_link_en": "Nutrient-stressed plants succumb rapidly to viral symptom expression. Vector insects thrive in tender, imbalanced vegetative canopies.",
        "recommendation_bn": {
            "immediate_action": "১. জমিতে আলোক ফাঁদ পেতে সবুজ পাতা ফড়িং নিধন করুন।\n২. মারাত্মক আক্রান্ত গাছ তুলে মাটিতে পুঁতে ফেলুন।",
            "chemical_treatment": "সবুজ পাতা ফড়িং দমনে ইমিডাক্লোপ্রিড (যেমন: টিডো ২০ এসএল) প্রতি লিটার পানিতে ০.৫ মিলি অথবা মিপসিন ৭৫ ডব্লিউপি ২ গ্রাম/লিটার হারে বিকেলের দিকে স্প্রে করুন।",
            "organic_treatment": "নিমবীজের তেলের স্প্রে (প্রতি লিটারে ৫ মিলি) সাদা মাছি ও ফড়িং দমনে অত্যন্ত কার্যকর।",
            "preventive_care": "নিয়মিত জমি পরিদর্শন এবং প্রতিরোধী জাত চাষ করুন। জমিতে সঠিক মাত্রায় পটাশ ও দস্তা সার প্রয়োগ করুন।"
        },
        "recommendation_en": {
            "immediate_action": "1. Set up light traps to eliminate green leafhopper (GLH) vectors.\n2. Rogue out severely infected plants and bury them deep in soil.",
            "chemical_treatment": "To control GLH vectors, spray Imidacloprid (e.g., Tido 20 SL) @ 0.5 mL/L or Mipcin 75 WP @ 2 g/L in the late afternoon.",
            "organic_treatment": "Neem seed oil spray (5 mL/L with mild detergent) is highly effective against leafhoppers.",
            "preventive_care": "Routinely inspect fields and cultivate virus-tolerant varieties. Maintain recommended potassium and zinc levels to boost immunity."
        },
        "fertilizer_adjustment": {
            "urea": "ইউরিয়া প্রয়োগ সাময়িক নিয়ন্ত্রণ করুন",
            "mop": "পটাশ স্বাভাবিক মাত্রায় প্রয়োগ",
            "gypsum": "স্বাভাবিক প্রয়োগ",
            "zinc": "গাছের রোগ প্রতিরোধে জিংক প্রয়োগ প্রয়োজন"
        }
    },
    "rice_healthy": {
        "crop": "rice",
        "crop_bn": "ধান",
        "crop_en": "Rice",
        "disease_id": "rice_healthy",
        "name_bn": "সুস্থ ধান পাতা (Healthy Rice Leaf)",
        "name_en": "Healthy Rice Leaf",
        "scientific_name": "Oryza sativa (Disease Free)",
        "type": "Healthy (সুস্থ)",
        "severity": "কোনো রোগ নেই (None)",
        "symptoms_bn": "গাছের পাতা উজ্জ্বল গাঢ় সবুজ, কোনো দাগ বা ক্ষত নেই। শিরা ও কান্ডের গঠন সুষম ও দৃঢ়।",
        "symptoms_en": "Vibrant emerald green leaves with intact cellular veins, zero necrotic spots, and robust vegetative turgor.",
        "soil_link_bn": "মাটিতে এন-পি-কে ও অম্লতার মান সন্তোষজনক অবস্থায় রয়েছে। পুষ্টির সুষম শোষণের কারণে পাতার প্রাকৃতিক রোগ প্রতিরোধ ক্ষমতা সক্রিয় রয়েছে।",
        "soil_link_en": "Soil NPK and pH values are within balanced BARC standard parameters, sustaining natural systemic resistance.",
        "recommendation_bn": {
            "immediate_action": "কোনো কীটনাশক বা ছত্রাকনাশক প্রয়োগের প্রয়োজন নেই।",
            "chemical_treatment": "প্রয়োজন নেই। অপচয় রোধ করুন।",
            "organic_treatment": "পরবর্তী ধাপের জন্য হালকা কম্পোস্ট মালচিং করতে পারেন।",
            "preventive_care": "সুষম সার ব্যবস্থাপনা ধরে রাখুন এবং নিয়মিত পর্যবেক্ষণ করুন।"
        },
        "recommendation_en": {
            "immediate_action": "No chemical pesticide or fungicide application needed.",
            "chemical_treatment": "Not required. Prevent unnecessary chemical runoff.",
            "organic_treatment": "Light organic mulch or compost can be applied for sustained vigor.",
            "preventive_care": "Maintain balanced BARC fertilizer management and scout fields periodically."
        },
        "fertilizer_adjustment": {
            "urea": "বিএআরসি অনুমোদিত রুটিন মাত্রা বজায় রাখুন",
            "mop": "রুটিন মাত্রা বজায় রাখুন",
            "gypsum": "রুটিন মাত্রা বজায় রাখুন",
            "zinc": "রুটিন মাত্রা বজায় রাখুন"
        }
    },

    # ------------------ JUTE (পাট) ------------------
    "jute_cercospora": {
        "crop": "jute",
        "crop_bn": "পাট",
        "crop_en": "Jute",
        "disease_id": "jute_cercospora",
        "name_bn": "পাটের সারকোস্পোরা পাতার দাগ (Cercospora Leaf Spot)",
        "name_en": "Jute Cercospora Leaf Spot",
        "scientific_name": "Cercospora corchori",
        "type": "Fungal (ছত্রাকজনিত)",
        "severity": "মাঝারি (Moderate)",
        "symptoms_bn": "পাটের পাতায় ছোট ছোট গোলাকার বা কোণাকৃতির ছাই রঙের দাগ দেখা যায়, যার চারপাশ লালচে বাদামী বৃত্ত দ্বারা ঘেরা থাকে। পাতা হলুদ হয়ে অকালে ঝরে পড়ে।",
        "symptoms_en": "Small circular to angular grayish spots bordered by reddish-brown halos. Severely affected leaves turn yellow and drop prematurely, degrading fiber yield.",
        "soil_link_bn": "মাটিতে পটাশের ঘাটতি ও অম্লীয় ভাব (pH < ৬.০) থাকলে পাটের কান্ড ও পাতার বহিঃত্বক দুর্বল হয়, ফলে সারকোস্পোরা ছত্রাক অতি দ্রুত সংক্রমণ ঘটায়।",
        "soil_link_en": "Potassium deficiency coupled with sub-optimal soil pH renders jute epidermis thin, significantly lowering natural resistance to Cercospora spore colonization.",
        "recommendation_bn": {
            "immediate_action": "১. ঝরে পড়া ও শুকিয়ে যাওয়া পাতা সংগ্রহ করে পুড়িয়ে ফেলুন যাতে ছত্রাকের স্পোর ছড়াতে না পারে।\n২. জমিতে পানি নিষ্কাশনের সুষ্ঠু ব্যবস্থা করুন।",
            "chemical_treatment": "কার্বেনডাজিম (যেমন: অটোস্টিন ৫০ ডব্লিউপি) প্রতি লিটার পানিতে ১ গ্রাম অথবা ডাইফেনোকোনাজোল (স্কোর ২৫০ ইসি) ০.৫ মিলি/লিটার হারে স্প্রে করুন।",
            "organic_treatment": "নিম খৈল গুঁড়া জমিতে প্রয়োগ করুন এবং নিম পাতার নির্যাস পাতায় ছিটিয়ে দিন।",
            "preventive_care": "পরবর্তী মৌসুমে জমি তৈরির সময় প্রতি শতকে ৩০০-৪০০ গ্রাম পটাশ (এমওপি) নিশ্চিত করুন।"
        },
        "recommendation_en": {
            "immediate_action": "1. Collect and burn fallen withered leaves to prevent fungal spore dispersal.\n2. Maintain good field drainage to avoid standing humidity.",
            "chemical_treatment": "Spray Carbendazim (e.g., Autostin 50 WP) @ 1 g/L water or Difenoconazole (Score 250 EC) @ 0.5 mL/L.",
            "organic_treatment": "Apply neem cake powder to the soil and spray aqueous neem leaf extract onto the foliage.",
            "preventive_care": "Apply 300-400g MOP per decimal during land preparation for the next crop season."
        },
        "fertilizer_adjustment": {
            "urea": "ইউরিয়া অতিরিক্ত দেবেন না (১০% কমান)",
            "mop": "পটাশ (এমওপি) ২৫% বৃদ্ধি করুন",
            "gypsum": "সালফার ঘাটতি থাকলে জিপসাম ৩ কেজি/বিঘা দিন",
            "zinc": "স্বাভাবিক মাত্রা"
        }
    },
    "jute_golden_mosaic": {
        "crop": "jute",
        "crop_bn": "পাট",
        "crop_en": "Jute",
        "disease_id": "jute_golden_mosaic",
        "name_bn": "পাটের হলুদ মোজাইক রোগ (Golden Mosaic Disease)",
        "name_en": "Jute Golden Mosaic Disease",
        "scientific_name": "Jute Yellow Mosaic Virus (JYMV - Begomovirus)",
        "type": "Viral (সাদা মাছি বাহিত ভাইরাস)",
        "severity": "উচ্চ (High)",
        "symptoms_bn": "পাতায় উজ্জ্বল সোনালী-হলুদ ও সবুজ রঙের ছোপ ছোপ মোজাইক নকশা দেখা যায়। পাতা কুঁচকে যায়, গাছের বৃদ্ধি থমকে যায় এবং আঁশের গুণমান মারাত্মক হ্রাস পায়।",
        "symptoms_en": "Striking golden-yellow and dark green mosaic patches across leaf blades. Leaf curling, stunted plant stature, and severe fiber tensile strength loss.",
        "soil_link_bn": "মাটিতে নাইট্রোজেনের ভারসাম্যহীনতা এবং জৈব পদার্থের শূন্যতা সাদা মাছি (Bemisia tabaci) পোকার আক্রমণকে অনুকূল করে তোলে। উদ্ভিদে মাইক্রোনিউট্রিয়েন্ট ঘাটতি ভাইরাস প্রতিহত করার ক্ষমতা কমায়।",
        "soil_link_en": "Imbalanced nitrogen promotes tender leafy tissue preferred by whitefly vectors. Micronutrient depletion impairs cellular antiviral defense mechanisms.",
        "recommendation_bn": {
            "immediate_action": "১. প্রাথমিক অবস্থায় আক্রান্ত চারাগুলো তুলে আগুনে পুড়িয়ে বা মাটির নিচে পুঁতে ফেলুন।\n২. ভাইরাস বাহক সাদা মাছি দমনে জরুরি ব্যবস্থা নিন।",
            "chemical_treatment": "সাদা মাছি দমনে অ্যাসিটামিপ্রিড (যেমন: গেইন ২০ এসপি) ০.২ গ্রাম/লিটার অথবা ইমিডাক্লোপ্রিড (অ্যাডমায়ার) ০.৫ মিলি/লিটার পানিতে মিশিয়ে বিকেলে স্প্রে করুন।",
            "organic_treatment": "হলুদ আঠালো ফাঁদ (Yellow Sticky Trap) জমিতে স্থাপন করুন। নিম তেলের দ্রবণ প্রতি ৫ দিন অন্তর স্প্রে করুন।",
            "preventive_care": "বীজ বপনের পূর্বে ভিটাভেক্স বা ব্যাভিস্টিন দিয়ে বীজ শোধন করুন। অনুমোদিত মোজাইক সহনশীল জাত নির্বাচন করুন।"
        },
        "recommendation_en": {
            "immediate_action": "1. Rogue out infected seedlings early and destroy by burning or deep burial.\n2. Take immediate measures to control whitefly virus vectors.",
            "chemical_treatment": "Spray Acetamiprid (Gain 20 SP) @ 0.2 g/L or Imidacloprid (Admire) @ 0.5 mL/L in the late afternoon against whiteflies.",
            "organic_treatment": "Set up yellow sticky traps across the field. Spray neem oil solution at 5-day intervals.",
            "preventive_care": "Treat seeds with Vitavax or Bavistin before sowing. Choose certified mosaic-tolerant jute varieties."
        },
        "fertilizer_adjustment": {
            "urea": "ইউরিয়া স্বাভাবিক বা সামান্য কম প্রয়োগ করুন",
            "mop": "গাছের রোগসহনশীলতা বাড়াতে পটাশ নিশ্চিত করুন",
            "gypsum": "জিপসাম প্রয়োগ করুন",
            "zinc": "দস্তা স্প্রে করুন"
        }
    },
    "jute_stem_rot": {
        "crop": "jute",
        "crop_bn": "পাট",
        "crop_en": "Jute",
        "disease_id": "jute_stem_rot",
        "name_bn": "পাটের কান্ড পচা ও গোড়া পচা রোগ (Stem Rot / Anthracnose)",
        "name_en": "Jute Stem Rot / Anthracnose",
        "scientific_name": "Macrophomina phaseolina / Colletotrichum corchorum",
        "type": "Fungal (ছত্রাকজনিত)",
        "severity": "মারাত্মক (Severe)",
        "symptoms_bn": "পাতায় বাদামী রঙের ক্ষত সৃষ্টি হয় এবং কান্ডে কালো বা গাঢ় বাদামী ক্ষতের সৃষ্টি হয় যা ফেটে যায়। কান্ড পচে গাছ শুকিয়ে ঢলে পড়ে এবং আঁশ নষ্ট হয়ে যায়।",
        "symptoms_en": "Brownish necrotic lesions on leaves extending into dark elongated cankers on stems. Stems rot, plant wilts, and fibers blacken and disintegrate.",
        "soil_link_bn": "মাটিতে পানির নিষ্কাশন ব্যবস্থা খারাপ হলে, পটাশিয়ামের অভাব থাকলে এবং অতিরিক্ত অম্লীয় মাটিতে (pH < ৫.৫) এই ছত্রাক শিকড় ও কান্ডের গোড়ায় দ্রুত আক্রমণ বিস্তার করে।",
        "soil_link_en": "Waterlogged soils combined with low potassium and acidic conditions (pH < 5.5) strongly favor soil-borne Macrophomina fungal sclerotia germination.",
        "recommendation_bn": {
            "immediate_action": "১. জমি থেকে অতিরিক্ত বৃষ্টির পানি নিষ্কাশনের নালা কেটে দিন।\n২. রোগাক্রান্ত গাছ তুলে মাঠের বাইরে নষ্ট করুন।",
            "chemical_treatment": "কার্বেনডাজিম (নোইন ৫০ ডব্লিউপি) ২ গ্রাম/লিটার অথবা কপার অক্সিক্লোরাইড (কুপ্রাভিট) ৪ গ্রাম/লিটার পানিতে মিশিয়ে কান্ড ও গোড়ায় ভালোভাবে ভিজিয়ে স্প্রে করুন।",
            "organic_treatment": "জমিতে ট্রাইকোডার্মা মিশ্রিত জৈব সার প্রয়োগ করুন। কাঁচা ছাই গোড়ায় ছিটিয়ে দিলে আর্দ্রতা ও ছত্রাক কমে।",
            "preventive_care": "ফসলের পর্যায়ক্রম (Crop Rotation) মেনে চলুন। ডাল বা তেলবীজ ফসলের পর পাট চাষ করলে মাটিতে ছত্রাকের চাপ কমে।"
        },
        "recommendation_en": {
            "immediate_action": "1. Promptly dig drainage trenches to evacuate excess standing rainwater.\n2. Rogue out and destroy diseased plants outside the field perimeter.",
            "chemical_treatment": "Spray Carbendazim (Knowin 50 WP) @ 2 g/L or Copper Oxychloride (Cupravit) @ 4 g/L, drenching stem bases thoroughly.",
            "organic_treatment": "Apply Trichoderma-enriched organic compost. Sprinkle raw wood ash around stem bases to reduce moisture and fungal growth.",
            "preventive_care": "Practice crop rotation with legumes or oilseeds to break the fungal inoculum cycle in soil."
        },
        "fertilizer_adjustment": {
            "urea": "ইউরিয়া সীমিত করুন",
            "mop": "পটাশ সার বিঘা প্রতি ৫-৬ কেজি প্রয়োগ করুন",
            "gypsum": "জিপসাম অবশ্যই প্রয়োগ করুন (সালফার ছত্রাক নিরোধক)",
            "zinc": "জিংক সালফেট প্রয়োগ করুন"
        }
    },
    "jute_healthy": {
        "crop": "jute",
        "crop_bn": "পাট",
        "crop_en": "Jute",
        "disease_id": "jute_healthy",
        "name_bn": "সুস্থ পাট পাতা (Healthy Jute Leaf)",
        "name_en": "Healthy Jute Leaf",
        "scientific_name": "Corchorus olitorius / capsularis (Disease Free)",
        "type": "Healthy (সুস্থ)",
        "severity": "কোনো রোগ নেই (None)",
        "symptoms_bn": "পাতার ত্বক চকচকে, অক্ষত ও সতেজ সবুজ। কান্ড সোজা ও দৃঢ়। কোনো ধরণের হলুদ ছোপ বা ছত্রাকজনিত দাগ নেই।",
        "symptoms_en": "Intact, lustrous emerald-green foliage with no chlorosis, lesion spots, or fungal blight. Vigorous stem elongation.",
        "soil_link_bn": "মাটির পিএইচ (pH ৬.২ - ৭.০) এবং এনপিকে অনুপাত পাটের জন্য অত্যন্ত অনুকূল ও পুষ্টিকর অবস্থায় রয়েছে।",
        "soil_link_en": "Soil chemical properties, drainage, and NPK metrics are in harmonious balance aligning with BARC optimums.",
        "recommendation_bn": {
            "immediate_action": "কোনো রাসায়নিক প্রয়োগের প্রয়োজন নেই।",
            "chemical_treatment": "প্রয়োজন নেই।",
            "organic_treatment": "স্বাভাবিক জৈব পরিচর্যা জারি রাখুন।",
            "preventive_care": "সময়মতো আগাছা পরিষ্কার রাখুন এবং পানির নিষ্কাশন নিশ্চিত রাখুন।"
        },
        "recommendation_en": {
            "immediate_action": "No chemical application needed.",
            "chemical_treatment": "Not required.",
            "organic_treatment": "Continue routine organic crop care.",
            "preventive_care": "Keep the field weed-free and maintain good drainage channels."
        },
        "fertilizer_adjustment": {
            "urea": "সুপারিশকৃত কিস্তি অনুযায়ী প্রয়োগ",
            "mop": "রুটিন মাত্রা বজায় রাখুন",
            "gypsum": "রুটিন মাত্রা বজায় রাখুন",
            "zinc": "রুটিন মাত্রা বজায় রাখুন"
        }
    }
}

BARC_BENCHMARKS = {
    "rice": {
        "name": "Rice (ধান - বোরো/আমন)",
        "nitrogen": {"low": 20.0, "optimum_min": 25.0, "optimum_max": 45.0, "high": 55.0, "unit": "ppm"},
        "phosphorus": {"low": 10.0, "optimum_min": 14.0, "optimum_max": 24.0, "high": 30.0, "unit": "ppm"},
        "potassium": {"low": 0.12, "optimum_min": 0.18, "optimum_max": 0.28, "high": 0.38, "unit": "meq/100g"},
        "ph": {"low": 5.2, "optimum_min": 5.8, "optimum_max": 6.8, "high": 7.5, "unit": "pH Scale"},
        "standard_fertilizer_per_bigha": {
            "urea": 35.0,
            "tsp": 14.0,
            "mop": 20.0,
            "gypsum": 12.0,
            "zinc_sulphate": 1.5
        }
    },
    "jute": {
        "name": "Jute (পাট - তোষা/দেশী)",
        "nitrogen": {"low": 22.0, "optimum_min": 30.0, "optimum_max": 50.0, "high": 60.0, "unit": "ppm"},
        "phosphorus": {"low": 8.0, "optimum_min": 12.0, "optimum_max": 22.0, "high": 28.0, "unit": "ppm"},
        "potassium": {"low": 0.14, "optimum_min": 0.20, "optimum_max": 0.30, "high": 0.40, "unit": "meq/100g"},
        "ph": {"low": 5.5, "optimum_min": 6.0, "optimum_max": 7.2, "high": 7.8, "unit": "pH Scale"},
        "standard_fertilizer_per_bigha": {
            "urea": 28.0,
            "tsp": 8.0,
            "mop": 16.0,
            "gypsum": 10.0,
            "zinc_sulphate": 1.0
        }
    }
}

PREVIOUS_CROPS = {
    "potato": {
        "name_bn": "আলু (Potato)",
        "name_en": "Potato",
        "soil_impact_bn": "আলু জমি থেকে প্রচুর পরিমাণ পটাশিয়াম ও মাঝারি নাইট্রোজেন শোষণ করে। আলুর পর ধান বা পাট চাষ করলে পটাশের তীব্র টান পড়তে পারে।"
    },
    "boro_rice": {
        "name_bn": "বোরো ধান (Boro Rice)",
        "name_en": "Boro Rice",
        "soil_impact_bn": "উচ্চ ফলনশীল বোরো ধান মাটি থেকে প্রচুর নাইট্রোজেন এবং পটাশিয়াম নিষ্কাশন করে।"
    },
    "aman_rice": {
        "name_bn": "রোপা আমন ধান (T. Aman Rice)",
        "name_en": "T. Aman Rice",
        "soil_impact_bn": "আমন ধানের পুষ্টি শোষণ সহনশীল মাত্রায় থাকে। মাটি মাঝারি উর্বর থাকে।"
    },
    "mustard": {
        "name_bn": "সরিষা (Mustard)",
        "name_en": "Mustard",
        "soil_impact_bn": "সরিষা মাটি থেকে সালফার ও ফসফরাস অধিক গ্রহণ করে।"
    },
    "maize": {
        "name_bn": "ভুট্টা (Maize/Corn)",
        "name_en": "Maize",
        "soil_impact_bn": "ভুট্টা অতিমাত্রায় পুষ্টিগ্রাসী ফসল। এটি মাটি থেকে সর্বাধিক নাইট্রোজেন ও পটাশিয়াম শেষ করে।"
    },
    "legume_pulses": {
        "name_bn": "ডাল জাতীয় ফসল (Legumes)",
        "name_en": "Legumes / Pulses",
        "soil_impact_bn": "ডাল জাতীয় ফসল মাটিতে নাইট্রোজেন সংবন্ধন করে উর্বরতা বাড়ায়।"
    },
    "fallow": {
        "name_bn": "পতিত জমি (Fallow Land)",
        "name_en": "Fallow Land",
        "soil_impact_bn": "জমি পতিত থাকায় মাটির প্রাকৃতিক বিশ্রাম হয়েছে।"
    }
}
