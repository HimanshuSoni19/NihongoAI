"""
Progress page rendering
"""
import streamlit as st
from config.prompts import PROMPTS

def render():
    """Render the progress page"""
    st.markdown("<h1 class='main-header'>Your Progress 📊</h1>", unsafe_allow_html=True)
    
    if not st.session_state.quiz_history:
        st.info("🌱 No quiz history yet. Start practicing to track your progress!")
    else:
        st.markdown(f"### Quiz History ({len(st.session_state.quiz_history)} total)")
        
        # Display last 10 quizzes
        for idx, quiz in enumerate(reversed(st.session_state.quiz_history[-10:]), 1):
            quiz_number = len(st.session_state.quiz_history) - idx + 1
            with st.expander(f"#{quiz_number} - {PROMPTS[quiz['type']]['icon']} {quiz['type']} - {quiz['timestamp']}"):
                st.markdown(quiz['content'])
        
        # Clear history button
        if st.button("🗑️ Clear History"):
            st.session_state.quiz_history = []
            st.session_state.current_quiz = None
            st.rerun()