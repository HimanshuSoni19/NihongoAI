"""
Configuration settings for NihongoAI
"""

# Page configuration
PAGE_CONFIG = {
    "page_title": "NihongoAI - Japanese Learning Platform",
    "page_icon": "🇯🇵",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Custom CSS styles
CUSTOM_CSS = """
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #FF6B6B;
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(90deg, #FF6B6B 0%, #4ECDC4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .quiz-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #4ECDC4;
        margin: 1rem 0;
    }
    .stButton>button {
        width: 100%;
        background-color: #4ECDC4;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #45b8b0;
        transform: translateY(-2px);
    }
    .sidebar-info {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
    .stats-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .selected-quiz-type {
        background-color: #4ECDC4 !important;
        border: 3px solid #FF6B6B !important;
    }
    </style>
"""

# Model configuration
MODEL_CONFIG = {
    "provider": "featherless-ai",
    "model": "elyza/Llama-3-ELYZA-JP-8B",
    "temperature": 0.7,
    "max_tokens": 2000
}