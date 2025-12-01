"""
NihongoAI - Main Application with CrewAI Integration
"""
import streamlit as st
from dotenv import load_dotenv
from datetime import datetime
import sys
import os

# Load environment
load_dotenv()

# Import configurations
from config.settings import PAGE_CONFIG, CUSTOM_CSS
from utils.session_state import initialize_session_state
from components.sidebar import render_sidebar

# Import pages
from pages_modules import home, library, progress

# Import CrewAI system
from agents.nihongo_crew import NihongoCrew

# Page configuration
st.set_page_config(**PAGE_CONFIG)
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Initialize session state
initialize_session_state()

# Initialize CrewAI (only once)
@st.cache_resource
def get_crew():
    """Initialize and cache the CrewAI system"""
    try:
        return NihongoCrew()
    except Exception as e:
        st.error(f"Failed to initialize AI agents: {e}")
        return None

# Get cached crew
crew = get_crew()

if 'agent_quizzes' not in st.session_state:
    st.session_state.agent_quizzes = []

# Render sidebar
page = render_sidebar()

# Route to pages
if page == "🏠 Home":
    home.render()
    
elif page == "📝 Quiz":
    st.markdown("<h1 class='main-header'>AI-Powered Quiz 🤖</h1>", unsafe_allow_html=True)
    
    if crew is None:
        st.error("❌ AI agents not available. Please check your GEMINI_API_KEY in .env file")
        st.stop()
    
    # Quiz configuration
    st.markdown("### 🎯 Configure Your AI Quiz")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        topic = st.selectbox(
            "Topic",
            ["General", "Kanji", "Vocabulary", "Particles", "Grammar", "Verbs", "Adjectives"]
        )
    
    with col2:
        difficulty = st.selectbox("Difficulty", ["N5", "N4"])
    
    with col3:
        num_questions = st.slider("Questions", 3, 8, 5)
    
    st.markdown("---")
    
    # Generate button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Generate AI Quiz", type="primary", use_container_width=True):
            with st.spinner("🤖 AI Agents are collaborating to create your quiz... (10-20 seconds)"):
                try:
                    # Generate quiz using CrewAI
                    result = crew.generate_quiz(
                        topic=topic.lower(),
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
                        'mode': 'AI Agent'
                    }
                    st.session_state.agent_quizzes.append(quiz_data)
                    st.session_state.current_quiz = quiz_data
                    
                    st.success("✅ AI Agents successfully created your quiz!")
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Error generating quiz: {str(e)}")
                    st.info("💡 Try refreshing the page or checking your internet connection")
    
    # Display current quiz
    if st.session_state.get('current_quiz'):
        st.markdown("---")
        st.markdown("### 📝 Your AI-Generated Quiz")
        
        quiz = st.session_state.current_quiz
        
        st.markdown(f"""
        <div class='quiz-card'>
            <h4>🤖 {quiz['topic']} Quiz ({quiz['difficulty']} Level)</h4>
            <p><small>📅 Generated: {quiz['timestamp']}</small></p>
            <p><small>🎯 {quiz['num_questions']} Questions | Created by Multi-Agent AI</small></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Display quiz content
        st.markdown("---")
        st.markdown(quiz['content'])
        
        # Answer submission
        st.markdown("---")
        st.markdown("### ✍️ Submit Your Answers")
        
        st.info("💡 Type your answer (A, B, C, or D) for each question")
        
        # Dynamic answer inputs based on number of questions
        num_q = quiz.get('num_questions', 5)
        
        answers = {}
        cols = st.columns(min(num_q, 3))  # Max 3 columns
        
        for i in range(num_q):
            col_idx = i % 3
            with cols[col_idx]:
                answer = st.text_input(
                    f"Question {i+1}",
                    key=f"q{i+1}",
                    placeholder="A, B, C, or D",
                    max_chars=1
                ).upper()
                if answer:
                    answers[i+1] = answer
        
        st.markdown("---")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📊 Get AI Feedback", type="primary", use_container_width=True):
                if len(answers) < num_q:
                    st.warning(f"⚠️ Please answer all {num_q} questions!")
                else:
                    with st.spinner("🤖 AI is analyzing your answers... (10-15 seconds)"):
                        try:
                            feedback = crew.analyze_answers(
                                quiz_content=quiz['content'],
                                user_answers=answers
                            )
                            
                            st.success("✅ Analysis Complete!")
                            st.markdown("### 📊 AI Feedback & Analysis")
                            st.markdown("---")
                            st.markdown(str(feedback))
                            
                            # Store feedback
                            quiz['feedback'] = str(feedback)
                            quiz['user_answers'] = answers
                            
                        except Exception as e:
                            st.error(f"❌ Error analyzing answers: {str(e)}")
        
        # Action buttons
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📋 Copy Quiz", use_container_width=True):
                st.code(quiz['content'], language=None)
                st.info("💡 Select text above and copy (Ctrl+C)")
        
        with col2:
            if st.button("🔄 Generate New", use_container_width=True):
                st.session_state.current_quiz = None
                st.rerun()
        
        with col3:
            if st.button("🗑️ Clear", use_container_width=True):
                st.session_state.current_quiz = None
                st.rerun()

elif page == "📚 Library":
    library.render()

elif page == "📊 Progress":
    progress.render()
    
    # Add AI Report Generation
    if len(st.session_state.agent_quizzes) > 0:
        st.markdown("---")
        st.markdown("### 🤖 AI-Generated Project Report")
        st.info(f"📊 You have completed {len(st.session_state.agent_quizzes)} AI-powered quizzes")
        
        if st.button("📄 Generate Comprehensive Report", type="primary"):
            with st.spinner("🤖 AI is generating your project report... (15-30 seconds)"):
                try:
                    stats = {
                        'total_quizzes': len(st.session_state.quiz_history) + len(st.session_state.agent_quizzes),
                        'ai_quizzes': len(st.session_state.agent_quizzes),
                        'classic_quizzes': len(st.session_state.quiz_history)
                    }
                    
                    report = crew.generate_project_report(
                        quiz_history=st.session_state.quiz_history + st.session_state.agent_quizzes,
                        user_stats=stats
                    )
                    
                    st.success("✅ Report Generated Successfully!")
                    st.markdown("### 📋 NihongoAI Project Report")
                    st.markdown("---")
                    st.markdown(str(report))
                    
                    # Download button
                    st.download_button(
                        label="⬇️ Download Report (Markdown)",
                        data=str(report),
                        file_name=f"NihongoAI_Report_{datetime.now().strftime('%Y%m%d_%H%M')}.md",
                        mime="text/markdown"
                    )
                    
                except Exception as e:
                    st.error(f"❌ Error generating report: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p>NihongoAI - Powered by CrewAI + Google Gemini 🤖</p>
        <p style='font-size: 0.9rem;'>Multi-Agent Learning System | 5 Specialized AI Agents</p>
    </div>
""", unsafe_allow_html=True)