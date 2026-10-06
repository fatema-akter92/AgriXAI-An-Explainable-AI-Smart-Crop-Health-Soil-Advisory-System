# AgriXAI: An Explainable AI Smart Crop Health & Soil Advisory System

An intelligent, explainable web platform built with **Python & Django** for detecting leaf diseases in **Rice (ধান)** and **Jute (পাট)** with visual **Grad-CAM** explanations and soil-nutrient-aware fertilizer prescriptions based on **BARC (Bangladesh Agricultural Research Council)** standards.

-------------

-------------

##  Key Features

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






### 🌐 Open in Browser:
Visit: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**
