"""
NihongoAI - Main Application Entry Point
"""
import streamlit as st
from dotenv import load_dotenv
from config.settings import PAGE_CONFIG, CUSTOM_CSS
from utils.session_state import initialize_session_state
from components.sidebar import render_sidebar
from pages_modules import home, quiz, library, progress

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(**PAGE_CONFIG)

# Apply custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Initialize session state
initialize_session_state()

# Render sidebar and get selected page
page = render_sidebar()

# Route to appropriate page
if page == "🏠 Home":
    home.render()
elif page == "📝 Quiz":
    quiz.render()
elif page == "📚 Library":
    library.render()
elif page == "📊 Progress":
    progress.render()

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p>NihongoAI - Powered by AI 🤖 | がんばって! (Ganbare - Do your best!)</p>
    </div>
""", unsafe_allow_html=True)