@echo off
echo ================================================
echo   Starting AI Interview System
echo ================================================
echo.

REM Activate virtual environment
if not exist venv (
    echo ERROR: Virtual environment not found!
    echo Please run setup_and_run.bat first
    pause
    exit /b 1
)

call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

echo Starting application...
echo Opening browser at http://localhost:8501
echo Press Ctrl+C to stop the server
echo.

streamlit run app.py

pause

