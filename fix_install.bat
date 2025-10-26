@echo off
echo Fixing installation...
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install sounddevice pypdf2 PyPDF2 pypdf speechmatics-python python-dotenv streamlit litellm edge-tts noisereduce numpy scipy pillow pygame
echo.
echo Now installing all requirements...
pip install -r requirements.txt
echo.
echo Done! Try running: streamlit run app.py
pause

