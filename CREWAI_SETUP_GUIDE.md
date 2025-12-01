# 🚀 CrewAI + Gemini Integration Guide

## ✅ STEP-BY-STEP SETUP

### **STEP 1: Get Gemini API Key (5 min)**

1. Visit: https://aistudio.google.com/app/apikey
2. Click "Create API Key" (Free tier: 60 requests/minute)
3. Copy your API key

### **STEP 2: Update .env File**

Add to your `.env` file:
```env
# Existing
HF_TOKEN=your_huggingface_token

# NEW - Add this
GEMINI_API_KEY=your_gemini_api_key_here
```

### **STEP 3: Install Dependencies**

```bash
# Activate environment
cd D:\NihongoAI
elyza-env\Scripts\activate

# Install CrewAI and Gemini
pip install crewai crewai-tools langchain-google-genai google-generativeai
```

### **STEP 4: Create Folder Structure**

```bash
# Create agents folder
mkdir agents
cd agents
type nul > __init__.py
type nul > nihongo_crew.py
cd ..
```

### **STEP 5: Copy Agent Files**

1. Create `agents/nihongo_crew.py` - Copy code from artifact #12
2. Update `app.py` - Use code from artifact #13

### **STEP 6: Rename pages folder**

```bash
# Rename to avoid Streamlit auto-navigation
ren pages views
```

Update imports in affected files to use `views` instead of `pages`.

### **STEP 7: Test Installation**

```bash
streamlit run app_crewai.py
```

---

## 🤖 **What Each Agent Does**

### **1. Vocabulary Expert** 📚
- Selects appropriate N5 vocabulary
- Provides reading, meaning, and usage
- Gives memory tips and mnemonics

### **2. Quiz Designer** ✍️
- Creates pedagogically sound questions
- Designs realistic distractors
- Ensures appropriate difficulty

### **3. Grammar Analyzer** 📖
- Explains grammar patterns
- Breaks down sentence structure
- Clarifies particle usage

### **4. Cultural Expert** 🎌
- Provides cultural context
- Explains formal vs. casual usage
- Shares social norms and etiquette

### **5. Performance Analyzer** 📊
- Analyzes quiz results
- Identifies learning patterns
- Generates study recommendations
- Creates comprehensive reports

---

## 📋 **Features Available**

### **AI-Powered Quiz Generation**
```python
# Generate quiz with multiple agents
crew.generate_quiz(
    topic='particles',
    difficulty='N5',
    num_questions=5
)
```

### **Intelligent Answer Analysis**
```python
# Get detailed feedback on answers
crew.analyze_answers(
    quiz_content=quiz,
    user_answers={'1': 'A', '2': 'B', '3': 'C'}
)
```

### **Personalized Study Plans**
```python
# Generate custom study plan
crew.generate_study_plan(
    user_level='beginner',
    weak_areas=['particles', 'verb conjugation']
)
```

### **Project Report Generation**
```python
# Generate comprehensive report
crew.generate_project_report(
    quiz_history=all_quizzes,
    user_stats=statistics
)
```

---

## 🔧 **Troubleshooting**

### **Error: "GEMINI_API_KEY not found"**
```bash
# Check .env file exists
dir .env

# Verify key is set
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('GEMINI_API_KEY'))"
```

### **Error: "No module named 'crewai'"**
```bash
# Reinstall
pip uninstall crewai -y
pip install crewai crewai-tools
```

### **Error: "Import langchain_google_genai failed"**
```bash
pip install langchain-google-genai
```

### **Gemini API Rate Limit**
- Free tier: 60 requests/minute
- Wait 60 seconds if you hit limit
- Consider adding delays between requests

---

## 📊 **Testing Checklist**

- [ ] Gemini API key works
- [ ] CrewAI imports successfully
- [ ] App launches without errors
- [ ] AI Quiz button generates quiz
- [ ] Answer analysis provides feedback
- [ ] Report generation works
- [ ] All agents respond correctly

---

## 🎯 **Next Steps for Project Report**

1. **Generate Multiple Quizzes**
   - Test all topics (Kanji, Vocab, Particles, Grammar)
   - Try different difficulty levels
   - Take screenshots of results

2. **Take Screenshots** (6-8 needed)
   - Home page
   - AI Quiz generation in progress
   - Generated quiz with questions
   - Answer submission interface
   - AI feedback analysis
   - Progress dashboard
   - Report generation

3. **Generate Final Report**
   - Click "Generate Project Report" in Progress tab
   - Download the markdown file
   - Convert to PDF/Word for submission

4. **Document Metrics**
   - Agent response times
   - Quiz generation accuracy
   - User satisfaction
   - System performance

---

## 📈 **Project Report Structure**

Your AI will generate a report with:

1. **Executive Summary**
   - Project overview
   - Technologies used
   - Key achievements

2. **System Architecture**
   - Multi-agent design
   - Workflow diagrams
   - Agent interactions

3. **Technical Implementation**
   - CrewAI integration
   - Gemini API usage
   - Streamlit interface

4. **Performance Metrics**
   - Response times
   - Accuracy rates
   - Usage statistics

5. **Results & Impact**
   - Learning outcomes
   - System effectiveness
   - User feedback

6. **Future Enhancements**
   - Planned features
   - Scalability plans

---

## 🎓 **Benefits Over Old System**

| Feature | Old (Elyza) | New (CrewAI + Gemini) |
|---------|-------------|----------------------|
| Response Quality | Good | Excellent |
| Context Understanding | Limited | Advanced |
| Multi-agent Collaboration | ❌ | ✅ |
| Cultural Context | ❌ | ✅ |
| Performance Analysis | ❌ | ✅ |
| Report Generation | Manual | Automated |
| Cost | Free | Free (with limits) |

---

## 🆘 **Need Help?**

If you encounter issues:
1. Check error message carefully
2. Verify API key is correct
3. Ensure all dependencies installed
4. Check internet connection
5. Review logs in terminal

**Ready to test!** Run `streamlit run app_crewai.py` and select "🚀 AI Agent Quiz"