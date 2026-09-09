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

