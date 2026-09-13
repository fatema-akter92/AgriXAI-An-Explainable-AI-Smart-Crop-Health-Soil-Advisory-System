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

