"""
Session state management utilities
"""
import streamlit as st

def initialize_session_state():
    """Initialize all session state variables"""
    if 'quiz_history' not in st.session_state:
        st.session_state.quiz_history = []
    
    if 'current_quiz' not in st.session_state:
        st.session_state.current_quiz = None
    
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = {}
    
    if 'selected_quiz_type' not in st.session_state:
        st.session_state.selected_quiz_type = None
    
    if 'is_generating' not in st.session_state:
        st.session_state.is_generating = False