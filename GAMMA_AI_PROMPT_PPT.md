# Gamma AI Prompt for AI Interview System Presentation

## 📊 Presentation Prompt for Gamma AI

Copy and paste this entire prompt into Gamma AI:

---

**Create a professional academic presentation on "AI Interview System: Adaptive Mock Interview Platform with LLMs and Voice Interface"**

The presentation should cover:

### **Slide 1: Title Slide**
- Title: "AI Interview System: Adaptive Mock Interview Platform with LLMs and Voice Interface"
- Authors: Anish Shinde, Rohit Kashid, Sujal Suryawanshi
- Institution: AISSMS Institute of Information Technology, Pune
- Date: 2025

### **Slide 2: Problem Statement**
- Current interview preparation challenges
- Limited access to practice interviews
- Inconsistent feedback quality
- Time-consuming manual screening for recruiters
- Need for automated, personalized interview systems

### **Slide 3: Objectives**
Create slides for each objective:
1. Automate resume analysis using LLM-powered extraction
2. Generate adaptive, personalized interview questions
3. Conduct voice-based interviews with real-time speech-to-text
4. Evaluate responses using AI-driven semantic analysis
5. Provide comprehensive interview reports with actionable insights

### **Slide 4: System Architecture**
Visual diagram showing:
- Input: Resume and Job Description
- LLM Parser (Resume Analysis)
- Question Generator (Adaptive)
- Voice Interface (TTS)
- Speech-to-Text Transcription (Speechmatics)
- Response Analysis
- Evaluation Engine (LLM Scoring)
- Report Generator
- Output: Interview Report with Scores

**Use flow arrows to connect these components**

### **Slide 5: Technology Stack**
Organize in categories:

**Backend:**
- Python 3.x with asyncio

**AI Services:**
- LiteLLM framework (Mistral Large, OpenAI, Anthropic support)

**Speech Processing:**
- Edge-TTS (Text-to-Speech)
- Speechmatics API (Speech-to-Text)
- sounddevice, noisereduce libraries

**Interface:**
- Streamlit (Web UI)
- CLI mode

**Data Processing:**
- PyPDF2 (PDF parsing)
- JSON (Data serialization)

### **Slide 6: Key Features**
Showcase 6 main features with icons/visuals:

1. **Resume Parsing** - Automatic extraction of candidate information using LLMs
2. **Adaptive Questioning** - Personalized questions based on background
3. **Voice Interface** - 4 AI voices (Alex, Aria, Natasha, Sonia)
4. **Real-time Transcription** - <1 second latency with Speechmatics
5. **AI-Powered Scoring** - 0-10 scale with detailed feedback (~90 words each)
6. **Comprehensive Reports** - Complete interview transcripts with actionable insights

### **Slide 7: Workflow Diagram**
Show the interview process:
- Step 1: Upload Resume (PDF)
- Step 2: Provide Job Description
- Step 3: System generates greeting + first question
- Step 4: User answers via voice
- Step 5: Real-time transcription
- Step 6: LLM analyzes and generates next question
- Step 7: Scoring and feedback after each answer
- Step 8: Final report generation
- Step 9: Review results

**Use numbered steps with icons**

### **Slide 8: Adaptive Question Generation**
Explain how it works:

- Input: Candidate's resume + job description + previous answers
- LLM analyzes: Technical skills, experience, background
- Generates: Contextually relevant questions
- Example: Python ML engineer → Questions about TensorFlow, PyTorch, specific ML projects
- Next question adapts based on current answer

**Include a simple example flow**

### **Slide 9: Scoring Framework**
Criteria for evaluation:
- Relevance to the question (10%)
- Completeness of answer (20%)
- Structure and coherence (15%)
- Specificity with examples (20%)
- Impact and results demonstrated (20%)
- Professionalism in communication (15%)

**Show pie chart or bar chart of evaluation criteria**

### **Slide 10: Results & Performance Metrics**
Highlight key achievements:

- ✅ Resume parsing: Successfully extracted from multiple PDF formats
- ✅ Question generation: Contextually relevant, adaptive questions
- ✅ Transcription accuracy: 95%+ for clear audio recordings
- ✅ Latency: <1 second for transcription, 2-3 seconds for question generation
- ✅ User testing: 10+ successful interviews completed
- ✅ Interview duration: 15-20 minutes for 5-question sessions

**Use checkmark icons and metrics**

### **Slide 11: Comparison with Existing Systems**
Create comparison table:

| Feature | Sharma et al. (CV-based) | Mandal et al. (Emotion) | Our System |
|---------|--------------------------|--------------------------|------------|
| Modality | CV+NLP+GenAI | Emotion/Confidence | Voice+NLP |
| Question Gen | Manual | Manual | **Adaptive LLM** |
| Emotion Analysis | Yes (CV) | Yes (CNN) | No |
| Voice Interaction | No | No | **Yes** |
| Resume Integration | Limited | No | **Comprehensive** |
| Open Source | No | No | **Yes** |
| Real-time Adaptation | No | No | **Yes** |

### **Slide 12: Differentiators**
Highlight unique aspects:

1. **Voice-First Architecture** - Unlike CV-based systems, we emphasize natural voice interaction
2. **Resume-Integrated Personalization** - Generates highly customized questions
3. **Content-Focused Analysis** - Detailed semantic evaluation via LLMs
4. **Open-Source Implementation** - Transparent and reproducible
5. **Real-time Adaptation** - Questions adapt based on live responses

**Use star icons or highlight boxes**

### **Slide 13: Use Cases**
Applications of the system:

🎯 **Candidate Practice** - 24/7 practice with personalized questions
🎯 **Preliminary Screening** - Initial candidate evaluation for recruiters
🎯 **Interview Training** - Educational institutions training students
🎯 **Self-Assessment** - Identify strengths and weaknesses

**Use application icons for each use case**

### **Slide 14: Limitations & Challenges**
Be honest about current limitations:

1. ❌ Transcription errors due to background noise/accents
2. ❌ LLM consistency varies between runs
3. ❌ No nonverbal analysis (facial expressions, body language)
4. ❌ English-only support currently
5. ❌ API dependency requires stable internet
6. ❌ Scoring subjectivity may differ from human assessment

**Use warning icons appropriately**

### **Slide 15: Future Enhancements**
Roadmap for improvements:

🔮 **Multimodal Analysis** - Add computer vision for facial expression analysis
🔮 **Emotion Recognition** - Confidence and emotional control assessment
🔮 **Language Expansion** - Support for 29+ languages
🔮 **Dynamic Difficulty** - Real-time performance-based adjustment
🔮 **HR Integration** - Connect with applicant tracking systems
🔮 **Code Evaluation** - Automated technical screening capabilities
🔮 **Analytics Dashboard** - Longitudinal performance tracking

**Use future-forward icons/arrows**

### **Slide 16: Conclusion**
Summary points:

✅ Successfully demonstrated:
- Automated resume analysis and information extraction
- Adaptive question generation tailored to profiles
- Real-time voice interaction with accurate transcription
- Comprehensive evaluation with detailed feedback
- Complete interview reporting with actionable insights

🎯 **Modular architecture** enables future enhancements
🎯 **Practical testing** validates utility for interview preparation
🎯 **Open-source approach** benefits research community

### **Slide 17: References**
Key papers cited:
- Sharma et al. (2025) - AI-Powered Mock Interview Platform using CV, NLP, and GenAI
- Mandal et al. (2023) - Emotion and confidence classifier model
- Singh & Kumar (2024) - NLP and Speech Analysis for Personalized Feedback
- Reddy & Thomas (2024) - AI-Based Interview System for Remote Hiring

### **Slide 18: Q&A / Thank You**
- Big "Thank You" or "Questions?" slide
- Contact information if needed
- Project repository link

---

## 🎨 Design Guidelines for Gamma AI:

**Visual Style:**
- Modern, professional academic theme
- Use tech/AI-themed color scheme (blues, purples, whites)
- Clean, minimal design
- Consistent icons throughout
- Professional fonts

**Layout:**
- Mix of text slides and visual slides
- Use diagrams where appropriate (architecture, workflow)
- Include bullet points but not too dense
- Add relevant icons/illustrations
- Use charts/graphs for metrics

**Content Guidelines:**
- Keep text concise (6-8 bullet points per slide max)
- Use visuals to illustrate complex concepts
- Highlight key achievements with bold/call-out boxes
- Show code snippets briefly for technical sections
- Use real examples where applicable

**Presentation Flow:**
- Start with problem (why needed)
- Show solution (system design)
- Explain features (what it does)
- Present results (how well it works)
- Compare with others (differentiators)
- Discuss future (where it's going)

**Total Slides: 18-20 slides**

---

## 📝 Additional Prompt Instructions for Gamma AI:

"Create this presentation with:
- Professional academic design
- Consistent color scheme throughout
- Appropriate icons and visuals
- Clear, readable fonts
- Good balance of text and visuals
- Smooth transitions between slides
- Use charts/diagrams where mentioned
- Professional but engaging presentation style
- Suitable for academic conference or demo"

---

**Instructions for using this prompt:**

1. Copy all content above the divider line
2. Go to Gamma AI (gamma.app)
3. Paste the prompt
4. Gamma will create the presentation automatically
5. Review and customize as needed
6. Export as PowerPoint or present online

---

## 🎯 Alternative: Concise Version for Quick Creation

If you want a shorter prompt, use this:

**"Create a professional 20-slide presentation on 'AI Interview System: Adaptive Mock Interview Platform with LLMs and Voice Interface' for authors Anish Shinde, Rohit Kashid, Sujal Suryawanshi from AISSMS Institute of Information Technology, Pune. Include: Problem statement, objectives, system architecture diagram, technology stack, key features, workflow, adaptive questioning mechanism, scoring framework, results and metrics, comparison table with Sharma et al. and Mandal et al., unique differentiators, use cases, limitations, future enhancements, and conclusion. Use modern academic design with tech/AI theme, professional icons, and clean layout suitable for conference presentation."**

