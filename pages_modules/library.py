"""
Library page rendering
"""
import streamlit as st
import pandas as pd

def render():
    """Render the library page"""
    st.markdown("<h1 class='main-header'>Learning Library 📚</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📖 Vocabulary", "✍️ Grammar", "🎯 JLPT Guide"])
    
    with tab1:
        render_vocabulary_tab()
    
    with tab2:
        render_grammar_tab()
    
    with tab3:
        render_jlpt_guide_tab()

def render_vocabulary_tab():
    """Render the vocabulary tab with CSV data"""
    st.markdown("### 🌟 Complete N5 Vocabulary Collection (800+ words)")
    
    try:
        # Load vocabulary from CSV
        csv_path = "data/N5_vocabulary.csv"
        vocab_data = pd.read_csv(csv_path)
        
        # Display stats
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📚 Total Words", len(vocab_data))
        with col2:
            if 'Category' in vocab_data.columns or 'category' in vocab_data.columns:
                cat_col = 'Category' if 'Category' in vocab_data.columns else 'category'
                st.metric("📂 Categories", vocab_data[cat_col].nunique())
            else:
                st.metric("📂 Categories", "N/A")
        with col3:
            st.metric("🎯 Level", "JLPT N5")
        
        st.markdown("---")
        
        # Search and filter
        st.markdown("#### 🔍 Search & Filter")
        col1, col2 = st.columns([3, 1])
        
        with col1:
            search_term = st.text_input("Search vocabulary (Japanese, Romaji, or English)", 
                                       placeholder="e.g., たべる, taberu, eat")
        
        # Category filter
        selected_category = "All"
        if 'Category' in vocab_data.columns or 'category' in vocab_data.columns:
            with col2:
                cat_col = 'Category' if 'Category' in vocab_data.columns else 'category'
                categories = ["All"] + sorted(vocab_data[cat_col].unique().tolist())
                selected_category = st.selectbox("Category", categories)
        
        # Apply filters
        filtered_data = vocab_data.copy()
        
        if search_term:
            mask = filtered_data.astype(str).apply(
                lambda x: x.str.contains(search_term, case=False, na=False)
            ).any(axis=1)
            filtered_data = filtered_data[mask]
        
        if selected_category != "All" and ('Category' in vocab_data.columns or 'category' in vocab_data.columns):
            cat_col = 'Category' if 'Category' in vocab_data.columns else 'category'
            filtered_data = filtered_data[filtered_data[cat_col] == selected_category]
        
        # View mode selection
        view_mode = st.radio("View Mode", ["📋 Card View", "📊 Table View", "📂 Category View"], horizontal=True)
        
        st.markdown("---")
        
        # Render based on view mode
        if view_mode == "📋 Card View":
            render_card_view(filtered_data)
        elif view_mode == "📊 Table View":
            render_table_view(filtered_data)
        else:
            render_category_view(filtered_data, vocab_data)
            
    except FileNotFoundError:
        show_error_message()
    except Exception as e:
        st.error(f"❌ Error loading vocabulary: {str(e)}")
        st.info("Please check your CSV file format and try again.")

def render_card_view(data):
    """Render vocabulary in card view"""
    items_per_page = 20
    total_pages = (len(data) - 1) // items_per_page + 1
    
    if total_pages > 1:
        page_num = st.selectbox(f"Page (showing {len(data)} results)", range(1, total_pages + 1))
    else:
        page_num = 1
    
    start_idx = (page_num - 1) * items_per_page
    end_idx = start_idx + items_per_page
    page_data = data.iloc[start_idx:end_idx]
    
    cols = st.columns(2)
    for idx, row in enumerate(page_data.iterrows()):
        row_data = row[1]
        with cols[idx % 2]:
            japanese = row_data.get('Japanese') or row_data.get('japanese') or row_data.get('Word') or row_data.iloc[0]
            english = row_data.get('English') or row_data.get('english') or row_data.get('Meaning') or row_data.iloc[1] if len(row_data) > 1 else ""
            romaji = row_data.get('Romaji') or row_data.get('romaji') or row_data.get('Reading') or ""
            category = row_data.get('Category') or row_data.get('category') or row_data.get('Type') or ""
            
            st.markdown(f"""
            <div class='quiz-card' style='margin-bottom: 1rem;'>
                <h3 style='color: #FF6B6B; margin: 0;'>{japanese}</h3>
                <p style='color: #666; margin: 0.2rem 0;'><em>{romaji}</em></p>
                <p style='margin: 0.5rem 0;'><strong>{english}</strong></p>
                {f"<span style='background-color: #4ECDC4; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.8rem;'>{category}</span>" if category else ""}
            </div>
            """, unsafe_allow_html=True)

def render_table_view(data):
    """Render vocabulary in table view"""
    st.dataframe(data, use_container_width=True, height=600)
    
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Download Filtered Data",
        data=csv,
        file_name="filtered_vocabulary.csv",
        mime="text/csv"
    )

def render_category_view(filtered_data, vocab_data):
    """Render vocabulary organized by category"""
    if 'Category' in vocab_data.columns or 'category' in vocab_data.columns:
        cat_col = 'Category' if 'Category' in vocab_data.columns else 'category'
        categories = sorted(filtered_data[cat_col].unique())
        
        for category in categories:
            cat_data = filtered_data[filtered_data[cat_col] == category]
            with st.expander(f"📌 {category} ({len(cat_data)} words)", expanded=False):
                cols = st.columns(3)
                for idx, row in enumerate(cat_data.iterrows()):
                    row_data = row[1]
                    japanese = row_data.get('Japanese') or row_data.get('japanese') or row_data.get('Word') or row_data.iloc[0]
                    english = row_data.get('English') or row_data.get('english') or row_data.get('Meaning') or row_data.iloc[1] if len(row_data) > 1 else ""
                    romaji = row_data.get('Romaji') or row_data.get('romaji') or row_data.get('Reading') or ""
                    
                    with cols[idx % 3]:
                        st.markdown(f"**{japanese}** {f'({romaji})' if romaji else ''}")
                        st.caption(english)
    else:
        st.warning("No category column found in the CSV. Please use Card or Table view.")

def show_error_message():
    """Show error message when CSV file is not found"""
    st.error("❌ CSV file not found at `data/N5_vocabulary.csv`")
    st.info("""
    **Please ensure your CSV file is located at:**
    ```
    data/N5_vocabulary.csv
    ```
    
    **Expected CSV format:**
    - Column 1: Japanese word (e.g., たべる)
    - Column 2: English meaning (e.g., to eat)
    - Column 3 (optional): Romaji (e.g., taberu)
    - Column 4 (optional): Category (e.g., Verbs, Food, etc.)
    """)
    
    # Fallback content
    st.markdown("### 📚 Sample N5 Vocabulary")
    vocab_categories = {
        "Numbers": ["いち (ichi) - 1", "に (ni) - 2", "さん (san) - 3"],
        "Family": ["ちち (chichi) - father", "はは (haha) - mother"],
        "Time": ["あさ (asa) - morning", "ひる (hiru) - noon"],
        "Places": ["がっこう (gakkou) - school", "いえ (ie) - home"]
    }
    
    for category, words in vocab_categories.items():
        with st.expander(f"📌 {category}"):
            for word in words:
                st.markdown(f"- {word}")

def render_grammar_tab():
    """Render the grammar tab"""
    st.markdown("### Basic Grammar Points")
    
    st.markdown("""
    #### Particles
    - **は** (wa): Topic marker - "わたしは学生です" (I am a student)
    - **が** (ga): Subject marker - "犬がいます" (There is a dog)
    - **を** (wo): Object marker - "本を読みます" (Read a book)
    - **に** (ni): Direction/time - "学校に行きます" (Go to school)
    - **で** (de): Location of action - "図書館で勉強します" (Study at library)
    """)

def render_jlpt_guide_tab():
    """Render the JLPT guide tab"""
    st.markdown("### JLPT N5 Study Guide")
    
    st.info("""
    **What is JLPT N5?**
    
    The Japanese Language Proficiency Test (JLPT) N5 is the beginner level. 
    
    **Requirements:**
    - 800 vocabulary words
    - 100 kanji characters
    - Basic grammar structures
    
    **Topics Covered:**
    - Self-introduction
    - Daily activities
    - Shopping and dining
    - Time and schedules
    """)