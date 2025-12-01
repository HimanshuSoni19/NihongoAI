# 🇯🇵 NihongoAI – Japanese Learning App
### Powered by **Google Gemini 2.5 Flash** and **Streamlit**

**NihongoAI** is an intelligent, interactive Japanese language learning application designed to help students master JLPT N5 and N4 levels. It leverages the power of **Google's Gemini 2.5 Flash** model to generate personalized quizzes, provide detailed feedback, and track your progress.

---

## 🚀 Features

### 🤖 AI-Powered Quiz Generation
- **Dynamic Content**: Generates unique quizzes every time based on your chosen topic (General, Kanji, Vocabulary, Grammar, Reading).
- **Customizable Difficulty**: Tailor the challenge level to your needs (N5 or N4).
- **Smart Randomization**: Ensures answer options are randomized for a fair testing experience.

### 📝 Interactive Learning
- **Instant Feedback**: Get immediate analysis of your answers.
- **Detailed Explanations**: Understand *why* an answer is correct or incorrect with AI-generated reasoning.
- **Beautiful UI**: Enjoy a clean, modern interface built with Streamlit.

### � Progress Tracking
- **Quiz History**: Keep track of all your generated quizzes.
- **Performance Reports**: Generate comprehensive PDF-ready reports of your learning journey using AI.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **AI Models**:
    - **Google Gemini 2.5 Flash** (via `google-generativeai`) - *Primary*
    - **Elyza Llama 7B** (Local Model) - *Alternative*
- **Backend Logic**: Python
- **Data Management**: Pandas

---

## 📂 Project Structure

```text
NihongoAI/
│
├── agents/
│   └── gemini_backend.py    # Core Gemini integration & quiz logic
│
├── utils/
│   ├── quiz_display.py      # UI components for rendering quizzes
│   └── session_state.py     # Streamlit session state management
│
├── pages_modules/           # Application pages
│   ├── home.py
│   ├── library.py
│   └── progress.py
│
├── config/
│   └── settings.py          # App configuration & CSS
│
├── data/                    # Vocabulary databases
│
├── .env                     # API keys (not committed)
├── .gitignore
├── requirements.txt
├── app_with_gemini.py       # Main application (Gemini Version)
└── app.py                   # Alternative application (Elyza Version)
```

---

## ⚙️ Setup & Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/HimanshuSoni19/NihongoAI.git
    cd NihongoAI
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment**
    Create a `.env` file in the root directory and add your Google Gemini API key:
    ```env
    GEMINI_API_KEY=your_api_key_here
    ```

4.  **Run the App**

    **Option A: Gemini Version (Recommended)**
    ```bash
    streamlit run app_with_gemini.py
    ```

    **Option B: Elyza Version (Local)**
    ```bash
    streamlit run app.py
    ```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
