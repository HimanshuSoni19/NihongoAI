# 🇯🇵 NihongoAI

**NihongoAI** is an intelligent, AI-powered Japanese language learning assistant designed to help students master JLPT N5 vocabulary and grammar. Built with **Streamlit** and powered by **CrewAI** and **Google Gemini**, it offers a personalized and interactive learning experience through multi-agent collaboration.

## 🚀 Features

### 1. 🏠 Home
- **Welcome Dashboard**: Overview of the application and quick start guide.
- **Feature Highlights**: Quick access to quizzes, library, and progress tracking.

### 2. 📝 Intelligent Quiz System
NihongoAI offers two distinct quiz modes:

*   **Mode A: 🚀 AI Agent Quiz (CrewAI + Gemini)**
    *   **Multi-Agent Collaboration**: Five specialized agents (Vocab Expert, Quiz Designer, Grammar Analyzer, Cultural Expert, Performance Analyzer) work together to create unique quizzes.
    *   **Personalized Feedback**: Detailed analysis of your answers, explaining mistakes and providing cultural context.
    *   **Customizable**: Choose your topic, difficulty (N5-N3), and number of questions.

*   **Mode B: ⚡ Quick Quiz (Classic)**
    *   Fast, single-LLM quiz generation for rapid practice.

### 3. 📚 Resource Library
- **N5 Vocabulary Database**: Access to over 800+ N5 level words.
- **Multiple Views**:
    - 📋 **Card View**: Flashcards for memorization.
    - 📊 **Table View**: Searchable and filterable spreadsheet format.
    - 📂 **Category View**: Words organized by topics (e.g., Food, Time, Verbs).
- **Grammar Reference**: Guides on particles, verb forms, and sentence patterns.

### 4. 📊 Progress Tracking
- **Quiz History**: Review past quiz performance.
- **Statistics**: Track your accuracy and total quizzes taken.
- **AI Report Generator**: Generate comprehensive project reports including performance metrics and future study recommendations.

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **AI/LLM Orchestration**: [CrewAI](https://crewai.com/), [LangChain](https://www.langchain.com/)
- **LLM Provider**: Google Gemini (via `google-generativeai`)
- **Data Handling**: Pandas
- **Environment Management**: Python-dotenv

## 📋 Prerequisites

- Python 3.10 or higher
- A Google Gemini API Key

## ⚙️ Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/nihongoai.git
    cd nihongoai
    ```

2.  **Create a virtual environment (optional but recommended)**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables**
    Create a `.env` file in the root directory and add your Google API key:
    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```

## 🏃‍♂️ Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## 📂 Project Structure

```text
nihongoai/
├── app.py                      # Main application entry point
├── .env                        # Environment variables
├── requirements.txt            # Python dependencies
├── agents/                     # CrewAI agent definitions
├── components/                 # UI components (Sidebar, etc.)
├── config/                     # Configuration settings & prompts
├── data/                       # Vocabulary data (CSV)
├── pages_modules/              # Page rendering logic (Home, Quiz, Library, Progress)
└── utils/                      # Utility functions (Session state, Quiz generation)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
