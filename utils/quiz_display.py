"""
Enhanced Quiz Display Component for NihongoAI
Better formatting and interactive UI
"""
import streamlit as st
import re

def parse_quiz_questions(quiz_text):
    """
    Parse quiz text into structured format
    Returns: list of {question_num, question_text, options: [A, B, C, D]}
    """
    questions = []
    lines = quiz_text.strip().split('\n')
    
    current_q = None
    current_options = []
    
    for line in lines:
        line = line.strip()
        if not line:
            if current_q and current_options:
                questions.append({
                    'num': current_q['num'],
                    'text': current_q['text'],
                    'options': current_options[:4]  # Ensure max 4 options
                })
                current_q = None
                current_options = []
            continue
        
        # Check if line starts with number (question)
        if re.match(r'^\d+\.', line):
            if current_q and current_options:
                questions.append({
                    'num': current_q['num'],
                    'text': current_q['text'],
                    'options': current_options[:4]
                })
            
            parts = line.split('.', 1)
            current_q = {
                'num': parts[0].strip(),
                'text': parts[1].strip() if len(parts) > 1 else ''
            }
            current_options = []
        
        # Check if line is an option (starts with ○)
        elif line.startswith('○'):
            option_text = line[1:].strip()  # Remove ○ and trim
            if option_text:
                current_options.append(option_text)
    
    # Don't forget last question
    if current_q and current_options:
        questions.append({
            'num': current_q['num'],
            'text': current_q['text'],
            'options': current_options[:4]
        })
    
    return questions


def display_quiz_beautiful(quiz_text):
    """
    Display quiz in beautiful, interactive format
    Returns: dict of user answers {question_num: selected_option_index}
    """
    questions = parse_quiz_questions(quiz_text)
    
    if not questions:
        st.error("Could not parse quiz questions. Please regenerate.")
        return {}
    
    st.markdown("### 📝 Answer the Questions")
    st.info(f"💡 Total Questions: {len(questions)} | Select one option for each question")
    
    user_answers = {}
    
    for idx, q in enumerate(questions):
        st.markdown("---")
        
        # Question card with better styling
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 1rem; border-radius: 10px; margin: 1rem 0;'>
            <h3 style='color: white; margin: 0;'>
                Question {q['num']}
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Question text - larger font for Japanese
        st.markdown(f"""
        <div style='background-color: #f8f9fa; padding: 1.5rem; 
                    border-radius: 10px; margin: 1rem 0; border-left: 4px solid #4ECDC4;'>
            <p style='font-size: 1.4rem; font-weight: 500; margin: 0; color: #2c3e50;'>
                {q['text']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Options as radio buttons with better styling
        if len(q['options']) >= 2:
            # Create option labels with letters
            option_labels = [f"{chr(65+i)}) {opt}" for i, opt in enumerate(q['options'])]
            
            selected = st.radio(
                f"Select your answer for Question {q['num']}:",
                options=range(len(q['options'])),
                format_func=lambda x: option_labels[x],
                key=f"q_{q['num']}",
                label_visibility="collapsed"
            )
            
            user_answers[q['num']] = chr(65 + selected)  # Convert to A, B, C, D
        else:
            st.warning(f"⚠️ Question {q['num']} has insufficient options")
    
    return user_answers


def display_quiz_simple_cards(quiz_text):
    """
    Alternative: Simple card-based display (less code)
    """
    questions = parse_quiz_questions(quiz_text)
    user_answers = {}
    
    for idx, q in enumerate(questions):
        with st.container():
            st.markdown(f"### Question {q['num']}")
            st.markdown(f"**{q['text']}**")
            
            if len(q['options']) >= 2:
                cols = st.columns(min(len(q['options']), 2))
                
                for i, option in enumerate(q['options']):
                    with cols[i % 2]:
                        if st.button(
                            f"{chr(65+i)}) {option}",
                            key=f"btn_q{q['num']}_opt{i}",
                            use_container_width=True
                        ):
                            user_answers[q['num']] = chr(65 + i)
                            st.session_state[f"answer_q{q['num']}"] = chr(65 + i)
            
            # Show selected answer
            if f"answer_q{q['num']}" in st.session_state:
                answer_key = f"answer_q{q['num']}"
                st.success(f"✅ Selected: {st.session_state[answer_key]}")
            
            st.markdown("---")
    
    return user_answers


def display_feedback_beautiful(feedback_text):
    """
    Display feedback in structured, beautiful format
    """
    lines = feedback_text.split('\n')
    
    # Extract score
    score_line = lines[0] if lines else "Score: 0 / 0 (0%)"
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); 
                padding: 2rem; border-radius: 15px; text-align: center; margin: 2rem 0;'>
        <h1 style='color: white; margin: 0; font-size: 2.5rem;'>{score_line}</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Parse and display each question feedback
    current_q = None
    current_feedback = []
    
    for line in lines[1:]:
        line = line.strip()
        
        if line.startswith('Q') and ':' in line:
            # Save previous question feedback
            if current_q:
                display_question_feedback(current_q, current_feedback)
            
            # Start new question
            parts = line.split(':', 1)
            q_num = parts[0].strip()
            status = parts[1].strip() if len(parts) > 1 else ''
            current_q = {'num': q_num, 'status': status}
            current_feedback = []
        
        elif line and current_q:
            current_feedback.append(line)
    
    # Don't forget last question
    if current_q:
        display_question_feedback(current_q, current_feedback)


def display_question_feedback(q_info, feedback_lines):
    """Helper to display individual question feedback"""
    status = q_info['status'].lower()
    
    if 'correct' in status and 'incorrect' not in status:
        icon = "✅"
        color = "#d4edda"
        border_color = "#28a745"
    else:
        icon = "❌"
        color = "#f8d7da"
        border_color = "#dc3545"
    
    st.markdown(f"""
    <div style='background-color: {color}; padding: 1rem; 
                border-radius: 10px; border-left: 4px solid {border_color}; margin: 1rem 0;'>
        <h4 style='margin: 0 0 0.5rem 0;'>{icon} {q_info['num']}: {q_info['status']}</h4>
    """, unsafe_allow_html=True)
    
    for line in feedback_lines:
        if line.startswith('-'):
            st.markdown(f"<p style='margin: 0.3rem 0; padding-left: 1rem;'>{line}</p>", 
                       unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)