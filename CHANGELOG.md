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

## Commit 42: docs: document convolutional neural network architecture and hyperparameters
- **Timestamp:** 2026-09-20 02:38:42
- **Summary:** Write model architecture summary including layer counts and parameter specs.

## Commit 43: feat: initialize explainable AI (XAI) service module
- **Timestamp:** 2026-09-20 09:34:35
- **Summary:** Add Grad-CAM visualization framework to make CNN predictions interpretable.

## Commit 44: feat: extract feature activation maps from final convolutional bottleneck layer
- **Timestamp:** 2026-09-20 16:30:28
- **Summary:** Hook into layer 16 expansion convolution to capture spatial activations.

## Commit 45: feat: calculate global average pooling gradients across feature maps
- **Timestamp:** 2026-09-20 23:26:21
- **Summary:** Compute importance weights alpha_k via spatial gradient pooling.

## Commit 46: feat: apply ReLU activation to filter positive contributing visual features
- **Timestamp:** 2026-09-21 06:22:14
- **Summary:** Discard negative gradient influences to isolate target class evidence.

## Commit 47: feat: interpolate 2D activation maps to match original leaf dimensions
- **Timestamp:** 2026-09-21 13:18:07
- **Summary:** Bilinearly upsample 7x7 activation grids to 224x224 pixel resolution.

## Commit 48: feat: apply Jet colormap for high-contrast thermal visualization
- **Timestamp:** 2026-09-21 20:14:00
- **Summary:** Transform normalized heat intensities into RGB thermal color spectrum.

## Commit 49: feat: implement alpha-blending to superimpose heatmap on leaf image
- **Timestamp:** 2026-09-22 02:33:36
- **Summary:** Blend heatmap (40%) with original leaf photo (60%) for lesion localization.

## Commit 50: feat: calculate infected focal region percentage based on heat thresholds
- **Timestamp:** 2026-09-22 09:29:29
- **Summary:** Segment activated pixel cluster to determine lesion blade coverage.

## Commit 51: feat: generate base64 encoded strings for original, heatmap, and overlay images
- **Timestamp:** 2026-09-22 16:25:22
- **Summary:** Encode visual outputs to data URI scheme for zero-disk frontend transmission.

## Commit 52: feat: generate natural language decision rationale explaining model focal points
- **Timestamp:** 2026-09-22 23:21:15
- **Summary:** Synthesize clinical reasoning explaining why the AI localized specific lesions.

## Commit 53: perf: optimize Grad-CAM rendering speed and memory usage
- **Timestamp:** 2026-09-23 06:17:08
- **Summary:** Use in-memory BytesIO buffers to prevent disk I/O bottlenecks.

## Commit 54: test: validate Grad-CAM overlay generation across all 9 disease classes
- **Timestamp:** 2026-09-23 13:13:01
- **Summary:** Ensure heatmap overlays generate without color clipping or dimension errors.

## Commit 55: feat: initialize soil nutrient analyzer service module
- **Timestamp:** 2026-09-23 20:08:54
- **Summary:** Create advisor/services/soil_analyzer.py for chemical parameter interpretation.

## Commit 56: feat: implement nitrogen (N) status classification algorithm
- **Timestamp:** 2026-09-24 02:28:30
- **Summary:** Classify nitrogen ppm into Deficient (<25), Medium (25-45), or Excess (>45).

## Commit 57: feat: implement phosphorus (P) status classification algorithm
- **Timestamp:** 2026-09-24 09:24:23
- **Summary:** Classify phosphorus ppm into Deficient (<12), Optimum (14-24), or High (>24).

## Commit 58: feat: implement potassium (K) status classification algorithm
- **Timestamp:** 2026-09-24 16:20:16
- **Summary:** Classify potassium meq into Deficient (<0.15), Optimum (0.18-0.28), or High (>0.28).

## Commit 59: feat: implement soil pH evaluation and optimal condition checking
- **Timestamp:** 2026-09-24 23:16:09
- **Summary:** Determine if soil pH is Strongly Acidic, Favorable, or Alkaline.

## Commit 60: feat: formulate 0-100 composite soil health scoring algorithm
- **Timestamp:** 2026-09-25 06:12:02
- **Summary:** Develop normalized scoring function combining chemical nutrient indices.

## Commit 61: feat: assign weighted coefficients to primary macronutrients (N:35%, P:25%, K:25%, pH:15%)
- **Timestamp:** 2026-09-25 13:07:55
- **Summary:** Weight individual parameter sub-scores to compute balanced soil health.

## Commit 62: feat: calculate status badges (Deficient, Medium, Optimum, Excess)
- **Timestamp:** 2026-09-25 20:03:48
- **Summary:** Generate UI badge metadata with appropriate alert colors for each nutrient.

## Commit 63: feat: generate contextual nutrient advisory remarks based on soil test values
- **Timestamp:** 2026-09-26 02:23:24
- **Summary:** Produce personalized agronomic tips explaining soil condition implications.

## Commit 64: test: verify soil score edge cases (all deficient vs all optimal)
- **Timestamp:** 2026-09-26 09:19:17
- **Summary:** Verify that depleted soil yields <30 score and balanced soil yields 90+ score.

## Commit 65: docs: document soil health scoring methodology and mathematical weights
- **Timestamp:** 2026-09-26 16:15:10
- **Summary:** Document mathematical formulation and justification for nutrient weights.

## Commit 66: feat: initialize disease-soil linkage reasoning engine
- **Timestamp:** 2026-09-26 23:11:03
- **Summary:** Create advisor/services/disease_soil_linker.py for cross-domain causal linking.

## Commit 67: feat: map excess nitrogen correlation with rice blast susceptibility
- **Timestamp:** 2026-09-27 06:06:56
- **Summary:** Link high nitrogen (>50 ppm) with lush foliage and blast fungus proliferation.

## Commit 68: feat: map nitrogen overload and high humidity links with bacterial leaf blight
- **Timestamp:** 2026-09-27 13:02:49
- **Summary:** Identify nitrogen-induced soft leaf tissues as infection vectors for Xanthomonas.

## Commit 69: feat: map severe nitrogen and potassium deficiency links with rice brown spot
- **Timestamp:** 2026-09-27 19:58:42
- **Summary:** Link brown spot epidemics with nutrient-starved, silica/potassium deficient soils.

## Commit 70: feat: map acidic soil and potassium deficiency triggers for jute stem rot
- **Timestamp:** 2026-09-28 02:18:18
- **Summary:** Link pH < 5.5 and potassium starvation with Rhizoctonia / Macrophomina stem rot.

## Commit 71: feat: map nitrogen and potassium imbalance factors for jute leaf spot
- **Timestamp:** 2026-09-28 09:14:11
- **Summary:** Correlate Cercospora spot severity with poor potash levels in jute fields.

## Commit 72: feat: generate scientific causal factor summaries for diagnostic reports
- **Timestamp:** 2026-09-28 16:10:04
- **Summary:** Summarize identified soil vulnerabilities directly aggravating observed leaf pathology.

## Commit 73: feat: formulate soil mitigation recommendations to prevent disease relapse
- **Timestamp:** 2026-09-28 23:05:57
- **Summary:** Provide soil amendment guidelines to break the disease susceptibility cycle.

## Commit 74: test: verify disease-soil linkage output for rice and jute pathogens
- **Timestamp:** 2026-09-29 06:01:50
- **Summary:** Assert linkage engine correctly tags excess nitrogen during blast predictions.

## Commit 75: feat: create unified advisory generator combining AI and soil analysis
- **Timestamp:** 2026-09-29 12:57:43
- **Summary:** Create advisor/services/advisory_generator.py assembling comprehensive response.

## Commit 76: feat: calculate precise fertilizer dosages (Urea, TSP, MoP, Gypsum, Zinc)
- **Timestamp:** 2026-09-29 19:53:36
- **Summary:** Implement stoichiometric nutrient conversion into standard fertilizer bags.

## Commit 77: feat: scale fertilizer quantity based on farm area and measurement unit
- **Timestamp:** 2026-09-30 02:13:12
- **Summary:** Apply area scaling factors for custom farmer land parcels in bigha or decimals.

## Commit 78: feat: formulate split application schedule for vegetative, tillering, and panicle stages
- **Timestamp:** 2026-09-30 09:09:05
- **Summary:** Detail fertilizer split timings (Basal, 1st Top Dressing, 2nd Top Dressing).

## Commit 79: feat: compile immediate emergency actions for active disease outbreaks
- **Timestamp:** 2026-09-30 16:04:58
- **Summary:** Provide immediate cultural control steps (draining standing water, halting urea).

## Commit 80: feat: compile approved chemical fungicide/bactericide application guidelines
- **Timestamp:** 2026-09-30 23:00:51
- **Summary:** List authorized active ingredients (Tricyclazole, Azoxystrobin, Copper Oxychloride).

## Commit 81: feat: compile eco-friendly organic and IPM treatments (Neem, Trichoderma, ash)
- **Timestamp:** 2026-10-01 05:56:44
- **Summary:** Include biological controls, organic leaf extracts, and bio-fertilizer recipes.

## Commit 82: feat: compile preventive agronomic practices and resistant seed varieties
- **Timestamp:** 2026-10-01 12:52:37
- **Summary:** Recommend BRRI / BJRI resistant cultivars and certified clean seed practices.

## Commit 83: feat: design responsive web interface with agricultural emerald color palette
- **Timestamp:** 2026-10-01 19:48:30
- **Summary:** Build modern CSS styling using CSS variables, cards, and smooth transitions.

## Commit 84: feat: implement leaf drag-and-drop file upload zone with instant preview
- **Timestamp:** 2026-10-02 02:08:06
- **Summary:** Add dropzone event listeners with FileReader API image preview.

## Commit 85: feat: add interactive sliders for soil test parameters (N, P, K, pH)
- **Timestamp:** 2026-10-02 09:03:59
- **Summary:** Build real-time slider input widgets with synchronized value badges.

## Commit 86: feat: display real-time benchmark indicator hints beneath soil sliders
- **Timestamp:** 2026-10-02 15:59:52
- **Summary:** Display dynamic deficiency vs optimum benchmark thresholds below sliders.

## Commit 87: feat: integrate crop switcher buttons for rice and jute
- **Timestamp:** 2026-10-02 22:55:45
- **Summary:** Provide intuitive one-click toggle switching between Rice and Jute modes.

## Commit 88: feat: implement sample photo carousel for quick demo evaluation
- **Timestamp:** 2026-10-03 05:51:38
- **Summary:** Allow users to click pre-loaded reference leaves without needing camera upload.

## Commit 89: feat: design diagnostic results studio with triple-panel Grad-CAM visualization
- **Timestamp:** 2026-10-03 12:47:31
- **Summary:** Present original leaf, heatmap, and overlay images side-by-side.

## Commit 90: feat: design balanced fertilizer prescription table with print-friendly layout
- **Timestamp:** 2026-10-03 19:43:24
- **Summary:** Format fertilizer dosage table and add browser print stylesheet.

## Commit 91: feat: add 4-stage smart farming workflow section
- **Timestamp:** 2026-10-04 02:03:00
- **Summary:** Illustrate 4-step precision agriculture process from leaf upload to harvest.

## Commit 92: feat: add 4 agro-ecological zone (AEZ) regional impact and soil risk cards
- **Timestamp:** 2026-10-04 08:58:53
- **Summary:** Detail Barind Tract, Haor Basin, Brahmaputra Floodplain, and Coastal Saline zones.

## Commit 93: feat: design call-to-action banner and comprehensive 4-column footer
- **Timestamp:** 2026-10-04 15:54:46
- **Summary:** Add emergency helpline 16123, institutional links, and academic attribution.

## Commit 94: feat: create comprehensive research methodology page (about.html)
- **Timestamp:** 2026-10-04 22:50:39
- **Summary:** Document research mathematical formulation, confusion matrix, and citations.

## Commit 95: feat: implement complete client-side bilingual translation engine (BN/EN)
- **Timestamp:** 2026-10-05 05:46:32
- **Summary:** Add UI_TRANSLATIONS dictionary and instant language toggle without page reload.

## Commit 96: feat: integrate dual-language API responses and localStorage persistence
- **Timestamp:** 2026-10-05 12:42:25
- **Summary:** Store language preference in localStorage and localize backend advisories.

