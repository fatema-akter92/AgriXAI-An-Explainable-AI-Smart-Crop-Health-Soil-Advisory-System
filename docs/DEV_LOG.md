# AgriXAI Engineering & Research Development Log

Daily log of commits, technical milestones, and scientific verifications.

### [2026-09-08 10:05:11] #001 - chore: initialize repository with .gitignore and virtual environment setup
Setup standard Python and Django gitignore definitions.

### [2026-09-08 17:01:04] #002 - feat: scaffold django 5.x project structure and core settings
Initialize core configuration, secret key, installed apps, and middleware.

### [2026-09-08 23:56:57] #003 - feat: add core requirements and dependency specifications
Define numpy, matplotlib, pillow, django, whitenoise and gunicorn dependencies.

### [2026-09-09 06:52:50] #004 - feat: initialize advisor app with modular django architecture
Register advisor app in INSTALLED_APPS with AdvisorConfig.

### [2026-09-09 13:48:43] #005 - feat: configure static and media paths for web platform
Setup STATIC_URL, STATICFILES_DIRS, MEDIA_URL, and MEDIA_ROOT.

### [2026-09-09 20:44:36] #006 - feat: add database configuration and sqlite3 support
Configure default SQLite database backend in settings.py.

### [2026-09-10 03:04:12] #007 - feat: configure base application urls and routing
Define root routing in core/urls.py pointing to advisor endpoints.

### [2026-09-10 10:00:05] #008 - docs: add initial project readme and fydp research scope
Document project goals, problem statement, and methodology outline.

### [2026-09-10 16:55:58] #009 - feat: add asset generation and setup automation script
Create setup_assets.py for programmatic leaf sample generation.

### [2026-09-10 23:51:51] #010 - feat: add windows run script for local development environment
Add run.bat for one-click environment activation and server startup.

### [2026-09-11 06:47:44] #011 - feat: define BARC fertilizer benchmark thresholds for nitrogen, phosphorus, and potassium
Incorporate BARC soil nutrient classification tables for Bangladesh.

### [2026-09-11 13:43:37] #012 - feat: implement soil pH categorization and acidity classification logic
Add pH ranges for strongly acidic, slightly acidic, neutral, and alkaline soils.

### [2026-09-11 20:39:30] #013 - feat: add primary and secondary nutrient requirement rules for rice crops
Setup Boro, Aman, and Aus rice nutrient consumption benchmarks.

### [2026-09-12 02:59:06] #014 - feat: add nutrient deficiency and sufficiency benchmarks for jute crops
Setup Tossha and Deshi jute nitrogen, phosphorus, and potassium benchmarks.

### [2026-09-12 09:54:59] #015 - feat: define land measurement unit conversions (bigha, decimal, acre, hectare)
Implement area conversion logic to standardize decimal to bigha and acre.

### [2026-09-12 16:50:52] #016 - feat: integrate previous crop residue nitrogen contribution factors
Add nitrogen credit deductions for potato, mustard, and pulse residues.

