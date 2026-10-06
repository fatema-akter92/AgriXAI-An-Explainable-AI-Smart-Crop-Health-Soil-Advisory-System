
## AgriXAI: An Explainable AI Smart Crop Health & Soil Advisory System

An intelligent, explainable web platform built with **Python & Django** for detecting leaf diseases in **Rice (ধান)** and **Jute (পাট)** with visual **Grad-CAM** explanations and soil-nutrient-aware fertilizer prescriptions based on **BARC (Bangladesh Agricultural Research Council)** standards.



-------------

### 🌐 Live Link:
Visit: ****

-----------------


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

-------

<!-- Core Technologies & Platform -->
[![Django Version](https://img.shields.io/badge/Django-6.1%2B-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Region](https://img.shields.io/badge/Region-Bangladesh%20🇧🇩-006a4e?style=for-the-badge)](#)
[![Academic Project](https://img.shields.io/badge/DIU-CSE499%20FYDP-003366?style=for-the-badge)](#)

<!-- AI, Deep Learning & XAI -->
[![Model](https://img.shields.io/badge/Model-MobileNetV2%20Lightweight%20CNN-FF6F00?style=flat&logo=tensorflow&logoColor=white)](#)
[![Explainable AI](https://img.shields.io/badge/XAI-Grad--CAM%20Heatmaps-e11d48?style=flat&logo=target&logoColor=white)](#)
[![Image Processing](https://img.shields.io/badge/Vision-Pillow%20%7C%20Matplotlib-139c5a?style=flat)](#)
[![Data Engine](https://img.shields.io/badge/Math-NumPy%20Vectorized-013243?style=flat&logo=numpy&logoColor=white)](#)

<!-- Agricultural Domain & Standards -->
[![Agriculture Standard](https://img.shields.io/badge/Agricultural%20Standard-BARC%20Fertilizer%20Guide-1b4332?style=flat&logo=leaflet&logoColor=white)](http://barc.gov.bd)
[![Target Crops](https://img.shields.io/badge/Crops-Rice%20%26%20Jute%20(9%20Classes)-52b788?style=flat)](#)
[![Soil Scoring](https://img.shields.io/badge/Soil%20Health-0--100%20Composite%20Index-ca8a04?style=flat)](#)

<!-- Frontend & Deployment -->
[![Frontend](https://img.shields.io/badge/UI-HTML5%20%7C%20CSS3%20%7C%20ES6%2B%20JS-E34F26?style=flat&logo=html5&logoColor=white)](#)
[![Language Support](https://img.shields.io/badge/Language-Bilingual%20(বাংলা%20%2F%20English)-2563eb?style=flat)](#)
[![Production Server](https://img.shields.io/badge/WSGI-Gunicorn%20%7C%20WhiteNoise-499848?style=flat&logo=gunicorn&logoColor=white)](#)
[![Deployment](https://img.shields.io/badge/Deployment-Render%20Cloud-46E3B7?style=flat&logo=render&logoColor=black)](https://render.com)


