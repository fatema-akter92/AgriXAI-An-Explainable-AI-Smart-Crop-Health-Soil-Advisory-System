@echo off
title AgriXAI - Smart Crop Health & Soil Advisory (Django)
echo ==============================================================================
echo   AgriXAI: Smart Crop Health & Soil Advisory System
echo   Backend: Python Django Web Platform
echo ==============================================================================
echo.
echo [1/4] Checking Python environment...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH! Please install Python 3.10+
    pause
    exit /b
)

echo [2/4] Verifying / Installing Dependencies...
pip install -r requirements.txt

echo.
echo [3/4] Initializing Database & Media Assets...
python setup_assets.py
python manage.py makemigrations
python manage.py migrate

echo.
echo ==============================================================================
echo   Server is starting!
echo   Open your browser at: http://127.0.0.1:8000
echo ==============================================================================
echo.
python manage.py runserver 127.0.0.1:8000
pause
