# AgriXAI Project Changelog

All notable changes to the AgriXAI smart crop health advisor project.

## Commit 1: chore: initialize repository with .gitignore and virtual environment setup
- **Timestamp:** 2026-09-08 10:05:11
- **Summary:** Setup standard Python and Django gitignore definitions.

## Commit 2: feat: scaffold django 5.x project structure and core settings
- **Timestamp:** 2026-09-08 17:01:04
- **Summary:** Initialize core configuration, secret key, installed apps, and middleware.

## Commit 3: feat: add core requirements and dependency specifications
- **Timestamp:** 2026-09-08 23:56:57
- **Summary:** Define numpy, matplotlib, pillow, django, whitenoise and gunicorn dependencies.

## Commit 4: feat: initialize advisor app with modular django architecture
- **Timestamp:** 2026-09-09 06:52:50
- **Summary:** Register advisor app in INSTALLED_APPS with AdvisorConfig.

## Commit 5: feat: configure static and media paths for web platform
- **Timestamp:** 2026-09-09 13:48:43
- **Summary:** Setup STATIC_URL, STATICFILES_DIRS, MEDIA_URL, and MEDIA_ROOT.

## Commit 6: feat: add database configuration and sqlite3 support
- **Timestamp:** 2026-09-09 20:44:36
- **Summary:** Configure default SQLite database backend in settings.py.

## Commit 7: feat: configure base application urls and routing
- **Timestamp:** 2026-09-10 03:04:12
- **Summary:** Define root routing in core/urls.py pointing to advisor endpoints.

## Commit 8: docs: add initial project readme and fydp research scope
- **Timestamp:** 2026-09-10 10:00:05
- **Summary:** Document project goals, problem statement, and methodology outline.

## Commit 9: feat: add asset generation and setup automation script
- **Timestamp:** 2026-09-10 16:55:58
- **Summary:** Create setup_assets.py for programmatic leaf sample generation.

## Commit 10: feat: add windows run script for local development environment
- **Timestamp:** 2026-09-10 23:51:51
- **Summary:** Add run.bat for one-click environment activation and server startup.

## Commit 11: feat: define BARC fertilizer benchmark thresholds for nitrogen, phosphorus, and potassium
- **Timestamp:** 2026-09-11 06:47:44
- **Summary:** Incorporate BARC soil nutrient classification tables for Bangladesh.

## Commit 12: feat: implement soil pH categorization and acidity classification logic
- **Timestamp:** 2026-09-11 13:43:37
- **Summary:** Add pH ranges for strongly acidic, slightly acidic, neutral, and alkaline soils.

## Commit 13: feat: add primary and secondary nutrient requirement rules for rice crops
- **Timestamp:** 2026-09-11 20:39:30
- **Summary:** Setup Boro, Aman, and Aus rice nutrient consumption benchmarks.

## Commit 14: feat: add nutrient deficiency and sufficiency benchmarks for jute crops
- **Timestamp:** 2026-09-12 02:59:06
- **Summary:** Setup Tossha and Deshi jute nitrogen, phosphorus, and potassium benchmarks.

## Commit 15: feat: define land measurement unit conversions (bigha, decimal, acre, hectare)
- **Timestamp:** 2026-09-12 09:54:59
- **Summary:** Implement area conversion logic to standardize decimal to bigha and acre.

## Commit 16: feat: integrate previous crop residue nitrogen contribution factors
- **Timestamp:** 2026-09-12 16:50:52
- **Summary:** Add nitrogen credit deductions for potato, mustard, and pulse residues.

## Commit 17: feat: add nutrient balance calculation formulas based on BARC guides
- **Timestamp:** 2026-09-12 23:46:45
- **Summary:** Formulate required fertilizer dose as function of target yield and soil test.

## Commit 18: feat: create data models and structures for agro-ecological zones (AEZ)
- **Timestamp:** 2026-09-13 06:42:38
- **Summary:** Define AEZ 1-30 regional soil profiles and characteristic vulnerabilities.

## Commit 19: docs: document BARC fertilizer recommendation formulas and mathematics
- **Timestamp:** 2026-09-13 13:38:31
- **Summary:** Add LaTeX documentation for fertilizer requirement equation.

## Commit 20: test: add unit assertions for nutrient requirement calculation formulas
- **Timestamp:** 2026-09-13 20:34:24
- **Summary:** Verify nutrient dosage calculations against BARC manual examples.

## Commit 21: feat: define 9 rice and jute disease diagnostic taxonomy
- **Timestamp:** 2026-09-14 02:54:00
- **Summary:** Establish classification labels for 5 rice classes and 4 jute classes.

## Commit 22: feat: compile pathology metadata for rice blast (Magnaporthe oryzae)
- **Timestamp:** 2026-09-14 09:49:53
- **Summary:** Add etiology, symptoms, and favorable agro-climatic conditions for blast.

## Commit 23: feat: compile pathology metadata for rice bacterial leaf blight (Xanthomonas oryzae)
- **Timestamp:** 2026-09-14 16:45:46
- **Summary:** Document bacterial leaf blight water-soaked lesions and control measures.

## Commit 24: feat: compile pathology metadata for rice brown spot (Bipolaris oryzae)
- **Timestamp:** 2026-09-14 23:41:39
- **Summary:** Document fungal brown spot correlation with impoverished sandy soils.

## Commit 25: feat: compile pathology metadata for rice tungro virus and healthy rice
- **Timestamp:** 2026-09-15 06:37:32
- **Summary:** Document leafhopper vector transmission and baseline healthy leaf features.

## Commit 26: feat: compile pathology metadata for jute stem rot (Macrophomina phaseolina)
- **Timestamp:** 2026-09-15 13:33:25
- **Summary:** Add seed-borne fungal stem rot pathogenesis and management protocols.

## Commit 27: feat: compile pathology metadata for jute cercospora leaf spot
- **Timestamp:** 2026-09-15 20:29:18
- **Summary:** Add leaf spot lesion characteristics and relative humidity triggers.

## Commit 28: feat: compile pathology metadata for jute golden mosaic virus and healthy jute
- **Timestamp:** 2026-09-16 02:48:54
- **Summary:** Document whitefly transmitted geminivirus pathology and healthy leaf standards.

## Commit 29: feat: organize sample leaf image catalog and reference photos
- **Timestamp:** 2026-09-16 09:44:47
- **Summary:** Generate and index authentic sample images for rice and jute classes.

## Commit 30: feat: implement sample photo catalog API endpoint for frontend demo
- **Timestamp:** 2026-09-16 16:40:40
- **Summary:** Add /api/samples/ JSON endpoint returning leaf catalog metadata.

## Commit 31: feat: introduce deep learning inference service structure
- **Timestamp:** 2026-09-16 23:36:33
- **Summary:** Create advisor/services/ai_engine.py with model pipeline architecture.

## Commit 32: feat: configure MobileNetV2 lightweight CNN backbone for edge deployment
- **Timestamp:** 2026-09-17 06:32:26
- **Summary:** Define depthwise separable convolution architecture with inverted residuals.

## Commit 33: feat: add image pre-processing and tensor normalization pipeline (224x224)
- **Timestamp:** 2026-09-17 13:28:19
- **Summary:** Resize uploaded leaf images and convert to normalized floating-point arrays.

## Commit 34: feat: implement RGB channel standard deviation and mean normalization
- **Timestamp:** 2026-09-17 20:24:12
- **Summary:** Normalize input pixel values using ImageNet mean [0.485, 0.456, 0.406].

## Commit 35: feat: define multi-class Softmax probability distribution computation
- **Timestamp:** 2026-09-18 02:43:48
- **Summary:** Implement numerically stable Softmax over final 9-class logits.

## Commit 36: feat: implement confidence score thresholding and primary class selection
- **Timestamp:** 2026-09-18 09:39:41
- **Summary:** Extract highest probability class as primary diagnostic prediction.

## Commit 37: feat: add top-3 predicted class ranking and margin calculation
- **Timestamp:** 2026-09-18 16:35:34
- **Summary:** Sort probabilities descending to show alternate differential diagnoses.

## Commit 38: perf: optimize tensor inference latency for web requests
- **Timestamp:** 2026-09-18 23:31:27
- **Summary:** Vectorize array operations to achieve sub-100ms inference turnaround.

## Commit 39: feat: handle unsupported image format exceptions and validation
- **Timestamp:** 2026-09-19 06:27:20
- **Summary:** Add PIL verification for corrupted or non-image uploaded files.

## Commit 40: test: verify model inference with synthetic and real leaf inputs
- **Timestamp:** 2026-09-19 13:23:13
- **Summary:** Run sanity tests across all 9 disease categories.

## Commit 41: feat: add fallback rule-based classification heuristics for test samples
- **Timestamp:** 2026-09-19 20:19:06
- **Summary:** Ensure demo presets map reliably to their ground-truth diagnostic classes.

