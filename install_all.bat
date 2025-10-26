@echo off
echo ================================================
echo   Installing All AI Interview Dependencies
echo ================================================
echo.

cd /d "%~dp0"

REM Activate virtual environment
if not exist venv (
    echo Creating virtual environment...
    py -m venv venv
)

call venv\Scripts\activate.bat

echo.
echo Installing all required packages from requirements.txt...
echo This may take several minutes...
echo.

pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ================================================
echo   Installation Complete!
echo ================================================
echo.
echo You can now run the application with:
echo   streamlit run app.py
echo.
pause

