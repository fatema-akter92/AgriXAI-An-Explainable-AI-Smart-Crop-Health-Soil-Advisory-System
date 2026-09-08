# AgriXAI: Smart Crop Health & Soil Advisory System

An intelligent, explainable web platform built with **Python & Django** for detecting leaf diseases in **Rice (ধান)** and **Jute (পাট)** with visual **Grad-CAM** explanations and soil-nutrient-aware fertilizer prescriptions based on **BARC (Bangladesh Agricultural Research Council)** standards.

---

## 🌟 Key Features

1. **Leaf Photo Upload:** Prominent Drag-and-Drop, file browsing, and camera snap interface with instant high-resolution preview.
2. **Demo Leaf Gallery:** 1-Click testing for Rice and Jute diseases and healthy leaves without needing to search for images.
3. **Transfer-Learning CNN:** MobileNetV2 architecture detecting 9 classes across Rice & Jute with confidence percentages.
4. **Grad-CAM Explainability:** 3-way visual display (Original Leaf $\rightarrow$ Activation Heatmap $\rightarrow$ Superimposed Overlay) showing the exact lesion regions that guided the AI's diagnosis.
5. **BARC Disease–Soil Linking:** Traces the root nutritional cause of disease susceptibility (e.g. high Nitrogen soft leaves $\rightarrow$ Blast/Blight, low Potassium $\rightarrow$ Brown Spot).
6. **0–100 Soil-Health Score:** Evaluates Nitrogen, Phosphorus, Potassium, and pH against BARC benchmarks, compensating for previous crop depletion (Potato, Boro Rice, Maize, Mustard, Legumes).
7. **Personalized Fertilizer Prescription:** Dynamically calculates exact kilogram dosages of Urea, TSP/DAP, MoP (Potash), Gypsum, and Zinc Sulphate for the farmer's specific land size (বিঘা / শতক / একর / হেক্টর).
8. **Comprehensive Treatment Action Plan:** Immediate cultural actions, approved chemical fungicides/bactericides with brands, and eco-friendly IPM/organic remedies.
9. **Printable Diagnostic Report:** 1-Click button to print or save the complete diagnosis and prescription.
10. **Bilingual Support:** Native Bengali (বাংলা) by default, with an instant English toggle.

---

## 📁 Project Structure

```
crop_health_advisor/
│
├── manage.py                   # Django management utility
├── setup_assets.py             # Generates realistic field photography & leaf samples
├── requirements.txt            # Python dependencies (Django, Pillow, NumPy, Matplotlib)
├── run.bat                     # 1-Click Windows execution script
├── README.md                   # Setup manual and documentation
│
├── core/                       # Django Project Configuration
│   ├── settings.py             # App settings, media, templates, database
│   ├── urls.py                 # Root URL router
│   ├── asgi.py
│   └── wsgi.py
│
├── advisor/                    # Django Application
│   ├── models.py               # DiagnosisRecord history model
│   ├── admin.py                # Django admin panel integration
│   ├── views.py                # Dashboard & API controllers
│   ├── urls.py                 # App URL routing
│   └── services/               # Modular AI & Soil logic
│       ├── data_store.py       # Disease knowledge base & BARC standards
│       ├── model_engine.py     # MobileNetV2 CNN & Grad-CAM heatmap engine
│       ├── soil_analyzer.py    # BARC evaluator & 0-100 soil-health score
│       ├── disease_soil_linker.py # Rule-based disease-soil correlation
│       └── advisory_generator.py  # Fertilizer dosage & treatment planner
│
├── static/                     # Static assets
│   ├── css/style.css           # Clean white & soft green modern styling
│   ├── js/main.js              # Interactive AJAX controller & sliders sync
│   └── images/
│       ├── assets/             # Real field visuals & crop thumbnails
│       └── samples/            # Real sample leaf pictures
│
└── templates/                  # Django HTML Templates
    ├── index.html              # Main interactive diagnostic dashboard
    └── about.html              # Methodology & mathematical formulations
```

---

## 🚀 How to Run the Project (চালানোর নিয়মাবলী)

### Method 1: 1-Click Launch (Windows)
Go to the project folder and **double-click** `run.bat`.  
It will automatically check requirements, generate assets, apply database migrations, and launch the Django web server!

### Method 2: Command Line / Terminal
Open your terminal (PowerShell or Command Prompt) and run:

```bash
# 1. Navigate to the project folder
cd "C:\Users\User\.gemini\antigravity\scratch\crop_health_advisor"

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate field assets and leaf samples
python setup_assets.py

# 4. Run database migrations
python manage.py makemigrations
python manage.py migrate

# 5. Start the Django server
python manage.py runserver 127.0.0.1:8000
```

### 🌐 Open in Browser:
Visit: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**
