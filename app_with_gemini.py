"""
NihongoAI - Main Application
Perfected version with Gemini 2.5 Flash
"""
import streamlit as st
from dotenv import load_dotenv
from datetime import datetime

# Load environment
load_dotenv()

# Import configurations
from config.settings import PAGE_CONFIG, CUSTOM_CSS
from utils.session_state import initialize_session_state
from components.sidebar import render_sidebar

# Import pages
from pages_modules import home, library, progress

# Import backend
from agents.gemini_backend import NihongoCrew

# Page configuration
st.set_page_config(**PAGE_CONFIG)
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Initialize session state
initialize_session_state()

# Initialize backend (cached for performance)
@st.cache_resource
def get_gemini_backend():
    """Initialize and cache the Gemini backend"""
    try:
        return NihongoCrew()
    except Exception as e:
        st.error(f"Failed to initialize AI system: {e}")
        return None

# Get cached backend
gemini_backend = get_gemini_backend()

if 'agent_quizzes' not in st.session_state:
    st.session_state.agent_quizzes = []

# Render sidebar
page = render_sidebar()

# ================================================================
# HOME PAGE
# ================================================================
if page == "🏠 Home":
    home.render()

# ================================================================
# QUIZ PAGE
# ================================================================
elif page == "📝 Quiz":
    st.markdown("<h1 class='main-header'>AI-Powered Quiz 🤖</h1>", unsafe_allow_html=True)
    
    # Import display functions
    from utils.quiz_display import display_quiz_beautiful, display_feedback_beautiful
    
    if gemini_backend is None:
        st.error("❌ AI system not available. Check GEMINI_API_KEY in .env")
        st.stop()
    
    # Quiz configuration
    st.markdown("### 🎯 Configure Your Quiz")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        topic = st.selectbox(
            "Topic",
            ["general", "kanji", "vocabulary", "grammar", "reading"],
            help="Choose what aspect of Japanese to practice"
        )
    
    with col2:
        difficulty = st.selectbox(
            "Difficulty",
            ["N5", "N4"],
            help="JLPT level (N5 = beginner)"
        )
    
    with col3:
        num_questions = st.slider(
            "Questions",
            min_value=3,
            max_value=8,
            value=5,
            help="Number of questions in the quiz"
        )
    
    st.markdown("---")
    
    # Generate quiz button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Generate AI Quiz", type="primary", use_container_width=True):
            with st.spinner("🤖 AI is creating your quiz... (5-10 seconds)"):
                try:
                    # Generate quiz
                    result = gemini_backend.generate_quiz(
                        topic=topic,
                        difficulty=difficulty,
                        num_questions=num_questions
                    )
                    
                    # Store quiz
                    quiz_data = {
                        'content': str(result),
                        'topic': topic,
                        'difficulty': difficulty,
                        'num_questions': num_questions,
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M"),
                        'mode': 'Gemini 2.5'
                    }
                    st.session_state.agent_quizzes.append(quiz_data)
                    st.session_state.current_quiz = quiz_data
                    
                    # Clear previous answers
                    for key in list(st.session_state.keys()):
                        if key.startswith('q_'):
                            del st.session_state[key]
                    
                    st.success("✅ Quiz generated successfully!")
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
                    st.info("💡 Check internet connection or try again")
    
    # Display quiz
    if st.session_state.get('current_quiz'):
        st.markdown("---")
        
        quiz = st.session_state.current_quiz
        
        # Quiz info card
        st.markdown(f"""
        <div class='quiz-card'>
            <h3>🤖 {quiz['topic'].title()} Quiz ({quiz['difficulty']} Level)</h3>
            <p><small>📅 {quiz['timestamp']}</small></p>
            <p><small>🎯 {quiz['num_questions']} Questions | Powered by Gemini 2.5 Flash</small></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Display quiz with beautiful UI
        user_answers = display_quiz_beautiful(quiz['content'])
        
        # Submit button
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📊 Submit & Get Feedback", type="primary", use_container_width=True):
                if not user_answers or len(user_answers) < quiz['num_questions']:
                    st.warning(f"⚠️ Please answer all {quiz['num_questions']} questions!")
                else:
                    with st.spinner("🤖 Analyzing answers... (5-10 seconds)"):
                        try:
                            feedback = gemini_backend.analyze_answers(
                                quiz_content=quiz['content'],
                                user_answers=user_answers
                            )
                            
                            st.success("✅ Analysis Complete!")
                            st.markdown("---")
                            
                            # Display feedback
                            display_feedback_beautiful(feedback)
                            
                            # Store feedback
                            quiz['feedback'] = str(feedback)
                            quiz['user_answers'] = user_answers
                            
                        except Exception as e:
                            st.error(f"❌ Error: {str(e)}")
        
        # Action buttons
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📋 View Raw Quiz", use_container_width=True):
                with st.expander("📄 Raw Quiz Text", expanded=True):
                    st.code(quiz['content'], language=None)
        
        with col2:
            if st.button("🔄 Generate New", use_container_width=True):
                st.session_state.current_quiz = None
                for key in list(st.session_state.keys()):
                    if key.startswith('q_'):
                        del st.session_state[key]
                st.rerun()
        
        with col3:
            if st.button("🗑️ Clear", use_container_width=True):
                st.session_state.current_quiz = None
                for key in list(st.session_state.keys()):
                    if key.startswith('q_'):
                        del st.session_state[key]
                st.rerun()

# ================================================================
# LIBRARY PAGE
# ================================================================
elif page == "📚 Library":
    library.render()

# ================================================================
# PROGRESS PAGE
# ================================================================
elif page == "📊 Progress":
    progress.render()
    
    # AI Report Generation
    if len(st.session_state.agent_quizzes) > 0:
        st.markdown("---")
        st.markdown("### 🤖 AI-Generated Project Report")
        st.info(f"📊 You have completed {len(st.session_state.agent_quizzes)} AI quizzes")
        
        if st.button("📄 Generate Comprehensive Report", type="primary"):
            if gemini_backend is None:
                st.error("❌ AI system not available")
            else:
                with st.spinner("🤖 Generating report... (15-30 seconds)"):
                    try:
                        stats = {
                            'total_quizzes': len(st.session_state.quiz_history) + len(st.session_state.agent_quizzes),
                            'ai_quizzes': len(st.session_state.agent_quizzes),
                            'classic_quizzes': len(st.session_state.quiz_history)
                        }
                        
                        report = gemini_backend.generate_project_report(
                            quiz_history=st.session_state.quiz_history + st.session_state.agent_quizzes,
                            user_stats=stats
                        )
                        
                        st.success("✅ Report Generated!")
                        st.markdown("### 📋 NihongoAI Project Report")
                        st.markdown("---")
                        st.markdown(report)
                        
                        # Download button
                        st.download_button(
                            label="⬇️ Download Report (Markdown)",
                            data=report,
                            file_name=f"NihongoAI_Report_{datetime.now().strftime('%Y%m%d_%H%M')}.md",
                            mime="text/markdown"
                        )
                        
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p>NihongoAI - Powered by Google Gemini 2.5 Flash 🤖</p>
        <p style='font-size: 0.9rem;'>AI-Driven Japanese Language Learning Platform</p>
    </div>
""", unsafe_allow_html=True)