@echo off
echo ================================================
echo   AI Interview System - Setup and Run Script
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.11 or higher from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Step 1: Checking Python version...
python --version
echo.

echo Step 2: Creating virtual environment...
if not exist venv (
    python -m venv venv
    echo Virtual environment created successfully!
) else (
    echo Virtual environment already exists.
)
echo.

echo Step 3: Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo.

echo Step 4: Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    echo Please check your internet connection and try again.
    pause
    exit /b 1
)
echo.

echo Step 5: Checking .env file...
if not exist .env (
    echo WARNING: .env file not found!
    echo.
    echo Please create a .env file with the following variables:
    echo   MISTRAL_API_KEY=your_api_key_here
    echo   SPEECHMATICS_API_KEY=your_api_key_here
    echo   LLM_MODEL=mistral/mistral-large-latest
    echo.
    echo Press any key to create a template .env file...
    pause >nul
    (
        echo # LLM Configuration
        echo LLM_MODEL=mistral/mistral-large-latest
        echo MISTRAL_API_KEY=your_mistral_api_key_here
        echo.
        echo # Speech-to-Text Configuration
        echo SPEECHMATICS_API_KEY=your_speechmatics_api_key_here
    ) > .env
    echo .env file created! Please edit it with your API keys.
    echo.
) else (
    echo .env file found!
)
echo.

echo ================================================
echo   Setup Complete! Starting the application...
echo ================================================
echo.
echo Opening browser at http://localhost:8501
echo Press Ctrl+C to stop the server
echo.

streamlit run app.py

pause

