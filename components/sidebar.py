"""
Sidebar component
"""
import streamlit as st

def render_sidebar():
    """
    Render the sidebar navigation and information
    
    Returns:
        str: Selected page name
    """
    with st.sidebar:
        st.markdown("<h2 style='text-align: center;'>🇯🇵 NihongoAI</h2>", unsafe_allow_html=True)
        
        page = st.radio(
            "Navigation",
            ["🏠 Home", "📝 Quiz", "📚 Library", "📊 Progress"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Learning tip
        st.markdown("""
            <div class='sidebar-info'>
                <strong>💡 Learning Tip</strong><br>
                Practice daily for 15-20 minutes to see steady improvement!
            </div>
        """, unsafe_allow_html=True)
        
        # Display quiz count if available
        if st.session_state.quiz_history:
            st.metric("Quizzes Taken", len(st.session_state.quiz_history))
    
    return page