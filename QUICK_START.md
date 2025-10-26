# ⚡ Quick Start Guide

## 🎯 Running AI Interview System in 5 Minutes

### ✅ Prerequisites Checklist
- [ ] Python 3.11+ installed
- [ ] Internet connection active
- [ ] Chrome browser installed
- [ ] Microphone connected
- [ ] API Keys ready (Mistral + Speechmatics)

---

## 🚀 Three Ways to Run

### Method 1: 🎉 Easy Way (Windows) - Just Double Click!

1. **First Time Setup:**
   - Double-click `setup_and_run.bat`
   - Wait for automatic setup
   - Edit `.env` file with your API keys
   - Done! Application starts automatically

2. **Every Time After:**
   - Double-click `run_app.bat`
   - Application starts immediately

---

### Method 2: 📝 Manual Setup (All Platforms)

#### Windows (PowerShell/Command Prompt):
```bash
cd ai-interview
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Add your API keys to .env file
# Then run:
streamlit run app.py
```

#### macOS/Linux:
```bash
cd ai-interview
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Add your API keys to .env file
# Then run:
streamlit run app.py
```

---

### Method 3: 🐳 Docker (Advanced Users)
```bash
docker build -t ai-interview .
docker run -p 8501:8501 ai-interview
```

---

## 📝 Setting Up Your .env File

1. Navigate to the `ai-interview` folder
2. Create or edit `.env` file
3. Add your API keys:

```env
LLM_MODEL=mistral/mistral-large-latest
MISTRAL_API_KEY=your_actual_key_here
SPEECHMATICS_API_KEY=your_actual_key_here
```

---

## 🔑 Getting API Keys

### Mistral AI (Free tier available!)
1. Go to https://mistral.ai/
2. Sign up → Dashboard → API Keys
3. Generate new key → Copy to `.env`

### Speechmatics
1. Go to https://www.speechmatics.com/
2. Sign up → API Keys
3. Generate new key → Copy to `.env`

---

## 🎬 Using the Application

### 1️⃣ **Submit Information** (Sidebar)
- Upload PDF resume
- Paste job description
- Set question count (optional)
- Choose AI voice (optional)
- Click "Submit"

### 2️⃣ **Start Interview**
- Click "Start Interview" button
- AI greets you with audio

### 3️⃣ **Answer Questions**
- Listen to question (auto-play)
- Click microphone button
- Speak your answer
- Click stop when done
- AI processes your answer

### 4️⃣ **Get Results**
- View your score (out of 10)
- Read detailed feedback
- See improvements needed
- Download interview data

---

## ⚡ Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Python not found | Install Python 3.11+ from python.org |
| API key error | Check `.env` file has correct keys |
| Port already in use | Use `streamlit run app.py --server.port 8502` |
| Microphone not working | Use Chrome browser, allow permissions |
| Module not found | Run `pip install -r requirements.txt` |

---

## 📊 Application Structure

```
Browser opens automatically at:
http://localhost:8501

Application has two versions:
1. app.py - Web interface (Streamlit) ⭐ USE THIS
2. main.py - CLI version (terminal only)
```

---

## 💡 Pro Tips

✨ **Best Experience:**
- Use Chrome browser
- Ensure stable internet
- Test microphone before starting
- Speak clearly and at moderate pace
- Provide detailed answers for better scoring

✨ **Before Interview:**
- Review your resume
- Understand the job description
- Prepare like a real interview
- Find a quiet place

---

## 🎉 You're Ready!

Just run:
```bash
streamlit run app.py
```

Or double-click `run_app.bat` (Windows)

---

**Need more details?** → See [RUN_LOCALLY.md](RUN_LOCALLY.md)

**Need help?** → Check the main [README.md](README.md)
