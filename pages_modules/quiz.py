"""
Quiz page rendering
"""
import streamlit as st
from datetime import datetime
from config.prompts import PROMPTS
from utils.quiz_generator import generate_quiz

def render():
    """Render the quiz page"""
    st.markdown("<h1 class='main-header'>Quiz Practice 📝</h1>", unsafe_allow_html=True)
    
    # Quiz type selection
    st.markdown("### Select Your Quiz Type")
    
    cols = st.columns(len(PROMPTS))
    
    for idx, (key, value) in enumerate(PROMPTS.items()):
        with cols[idx]:
            button_type = "primary" if st.session_state.selected_quiz_type == key else "secondary"
            if st.button(
                f"{value['icon']}\n\n**{key}**\n\n{value['description']}", 
                key=f"btn_{key}",
                use_container_width=True,
                type=button_type
            ):
                st.session_state.selected_quiz_type = key
                st.rerun()
    
    st.markdown("---")
    
    # Show selected quiz type
    if st.session_state.selected_quiz_type:
        st.success(f"✅ Selected: **{st.session_state.selected_quiz_type}** {PROMPTS[st.session_state.selected_quiz_type]['icon']}")
    else:
        st.info("👆 Please select a quiz type above to get started!")
    
    # Generate quiz button
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        generate_button = st.button(
            "🎲 Generate Quiz" if not st.session_state.is_generating else "⏳ Generating...",
            type="primary",
            use_container_width=True,
            disabled=st.session_state.is_generating or not st.session_state.selected_quiz_type
        )
        
        if generate_button:
            if not st.session_state.selected_quiz_type:
                st.warning("⚠️ Please select a quiz type first!")
            else:
                st.session_state.is_generating = True
                st.rerun()
    
    # Handle quiz generation
    if st.session_state.is_generating:
        with st.spinner("🤔 AI is creating your personalized quiz... This may take 10-20 seconds."):
            try:
                quiz_text = generate_quiz(PROMPTS[st.session_state.selected_quiz_type]["prompt"])
                st.session_state.current_quiz = {
                    "type": st.session_state.selected_quiz_type,
                    "content": quiz_text,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                st.session_state.quiz_history.append(st.session_state.current_quiz)
                st.session_state.is_generating = False
                st.success("✅ Quiz generated successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"❌ Error generating quiz: {str(e)}")
                st.session_state.is_generating = False
                st.rerun()
    
    # Display current quiz
    if st.session_state.current_quiz and not st.session_state.is_generating:
        st.markdown("---")
        st.markdown("### 📖 Your Quiz")
        
        quiz_container = st.container()
        with quiz_container:
            st.markdown(f"""
                <div class='quiz-card'>
                    <h4>{PROMPTS[st.session_state.current_quiz['type']]['icon']} 
                        {st.session_state.current_quiz['type']} Quiz</h4>
                    <p><small>📅 Generated at: {st.session_state.current_quiz['timestamp']}</small></p>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown(st.session_state.current_quiz['content'])
        
        # Action buttons
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📋 Copy to Clipboard", use_container_width=True):
                st.code(st.session_state.current_quiz['content'], language=None)
                st.info("💡 Select the text above and copy it!")
        with col2:
            if st.button("🔄 Generate New Quiz", use_container_width=True):
                st.session_state.is_generating = True
                st.rerun()
        with col3:
            if st.button("🗑️ Clear Quiz", use_container_width=True):
                st.session_state.current_quiz = None
                st.rerun()