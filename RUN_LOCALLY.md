# 🚀 How to Run AI Interview System Locally

## 📋 Prerequisites

- **Python 3.11 or higher** (check with `python --version`)
- **Internet connection** for AI processing
- **Microphone** for recording answers
- **Chrome Browser** (recommended for best experience)
- **API Keys**:
  - LLM API Key (e.g., MistralAI, OpenAI, etc.)
  - Speechmatics API Key

---

## 📝 Step-by-Step Instructions

### Step 1: Check Python Version
```bash
python --version
```
**Required:** Python 3.11 or higher. If you don't have it, download from [python.org](https://www.python.org/downloads/)

### Step 2: Navigate to Project Directory
```bash
cd "ai-interview"
```

### Step 3: Create Virtual Environment
**Windows:**
```bash
python -m venv venv
```

**macOS/Linux:**
```bash
python3 -m venv venv
```

### Step 4: Activate Virtual Environment
**Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```bash
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 5: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 6: Configure Environment Variables
Make sure your `.env` file contains the following variables:

```env
# LLM Configuration
LLM_MODEL=mistral/mistral-large-latest
MISTRAL_API_KEY=your_mistral_api_key_here

# OR if using OpenAI
# OPENAI_API_KEY=your_openai_api_key_here

# Speech-to-Text Configuration
SPEECHMATICS_API_KEY=your_speechmatics_api_key_here
```

**Note:** Replace `your_api_key_here` with your actual API keys.

### Step 7: Run the Application
```bash
streamlit run app.py
```

This will start the Streamlit server and automatically open your browser at `http://localhost:8501`

---

## 🎯 How to Use the Application

### 1. **Upload Resume**
- In the sidebar, upload your PDF resume
- The system will extract key information automatically

### 2. **Enter Job Description**
- Paste the job description you're applying for in the text area

### 3. **Configure Settings** (Optional)
- Set the maximum number of questions (default: 5)
- Select the AI interviewer voice (default: Alex - Male)
- Available voices:
  - Alex (Male)
  - Aria (Female)
  - Natasha (Female)
  - Sonia (Female)

### 4. **Submit Information**
- Click the "Submit" button to process your resume

### 5. **Start Interview**
- Click "Start Interview" to begin
- The AI will greet you and ask the first question

### 6. **Answer Questions**
- Listen to each question (audio playback)
- Click the microphone button to record your answer
- Speak clearly when recording
- Click stop when finished

### 7. **Get Results**
- After completing all questions, review your:
  - Overall interview score (out of 10)
  - Detailed feedback for each answer
  - Suggestions for improvement
  - Complete conversation history

---

## 🔧 Troubleshooting

### Issue: "No module named..."
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: API Key Errors
**Solution:** Make sure your `.env` file is in the `ai-interview` directory and contains valid API keys.

### Issue: Microphone Not Working
**Solution:**
- Use Chrome browser (recommended)
- Allow microphone permissions
- Check your system audio settings

### Issue: Port Already in Use
**Solution:** Streamlit will try to use port 8501 by default. If busy:
```bash
streamlit run app.py --server.port 8502
```

### Issue: Virtual Environment Not Activating
**Windows PowerShell:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📦 Alternative: Using Docker

If you prefer Docker:

### Build the Docker image:
```bash
docker build -t ai-interview .
```

### Run the container:
```bash
docker run -p 8501:8501 ai-interview
```

---

## 🔑 Getting API Keys

### 1. Mistral AI (Free Tier Available)
1. Visit [https://mistral.ai/](https://mistral.ai/)
2. Sign up for an account
3. Navigate to API Keys section
4. Generate a new API key
5. Add to `.env` as `MISTRAL_API_KEY`

### 2. Speechmatics
1. Visit [https://www.speechmatics.com/](https://www.speechmatics.com/)
2. Sign up for an account
3. Navigate to API Keys section
4. Generate a new API key
5. Add to `.env` as `SPEECHMATICS_API_KEY`

### 3. Alternative LLM Providers (Optional)
If using OpenAI or other providers:
- Update `LLM_MODEL` in `.env` to match LiteLLM format
- Add the appropriate API key variable
- See [LiteLLM documentation](https://docs.litellm.ai/docs/providers) for more options

---

## 📊 What to Expect

### Interview Flow:
1. **Greeting** - AI introduces itself
2. **Questions** - 5 questions (configurable) based on your resume and job description
3. **Analysis** - Each answer is analyzed in real-time
4. **Results** - Detailed scoring and feedback

### Scoring:
- Each answer scored 0-10
- Overall score calculated from all answers
- Detailed feedback provided
- Suggestions for improvement included

---

## 💡 Tips for Best Results

- **Speak clearly** when recording answers
- **Provide detailed responses** for better evaluation
- **Use Chrome browser** for best compatibility
- **Ensure good internet connection** for AI processing
- **Speak in a quiet environment** for better audio quality
- **Review feedback** to improve future interviews

---

## 📁 Project Structure
```
ai-interview/
├── app.py              # Main Streamlit application
├── main.py             # CLI version (alternative)
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (you created this)
├── utils/             # Utility functions
│   ├── llm_call.py    # LLM integration
│   ├── transcript_audio.py  # Speech-to-text
│   └── ...
├── audio/             # Audio recordings (created during interviews)
└── outputs/           # Interview results (JSON files)
```

---

## 🆘 Need Help?

If you encounter any issues:
1. Check that all API keys are correctly set in `.env`
2. Verify Python version is 3.11+
3. Make sure all dependencies are installed
4. Ensure you're in the activated virtual environment
5. Check the terminal for error messages

---

## ✅ Quick Start Checklist

- [ ] Python 3.11+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file configured with API keys
- [ ] Mistral API key added
- [ ] Speechmatics API key added
- [ ] Ready to run (`streamlit run app.py`)

**You're all set! Happy interviewing! 🎉**
