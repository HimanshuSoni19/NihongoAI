"""
Home page rendering
"""
import streamlit as st

def render():
    """Render the home page"""
    st.markdown("<h1 class='main-header'>Welcome to NihongoAI! 🌸</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align: center; padding: 2rem 0;'>
            <h3>Your Intelligent Japanese Learning Companion</h3>
            <p style='font-size: 1.1rem; color: #666;'>
                Master Japanese through AI-powered quizzes and interactive learning
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Feature cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class='stats-box'>
                <h2>📝</h2>
                <h3>Smart Quizzes</h3>
                <p>AI-generated questions tailored to JLPT N5 level</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='stats-box'>
                <h2>📚</h2>
                <h3>Rich Library</h3>
                <p>Comprehensive vocabulary and grammar resources</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class='stats-box'>
                <h2>📊</h2>
                <h3>Track Progress</h3>
                <p>Monitor your learning journey and improvements</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick start guide
    st.markdown("### 🚀 Quick Start Guide")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
            **Step 1:** Choose Quiz  
            **Step 2:** Generate Questions  
            **Step 3:** Practice & Learn  
            **Step 4:** Review Answers  
        """)
    
    with col2:
        st.info("""
            **Pro Tips:**
            - Start with Vocabulary and Particles for beginners
            - Practice Kanji Reading to improve recognition
            - Review incorrect answers to identify weak areas
            - Take quizzes regularly for best results
        """)