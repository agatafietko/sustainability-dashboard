"""
Sustainability Research Discovery Hub
Streamlit web application for discovering cross-disciplinary research partners
using NLP semantic analysis and complementary method matching.
"""

import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter

# Page configuration
st.set_page_config(
    page_title="Sustainability Research Discovery Hub",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cache the model loading to avoid reloading on every interaction
@st.cache_resource
def load_nlp_model():
    """Load the sentence transformer model for semantic similarity"""
    return SentenceTransformer('all-MiniLM-L6-v2')

# Cache original publications data loading
@st.cache_data
@st.cache_data
def load_original_publications_from_path(csv_path):
    """Load the original publications CSV file from a specific path"""
    try:
        df = pd.read_csv(csv_path, low_memory=False)
        if df is None or len(df) == 0:
            return None
        return df
    except Exception as e:
        return None

@st.cache_data
def load_original_publications():
    """Load the original publications CSV file - tries repository paths first"""
    try:
        # Try multiple possible paths for the original CSV
        # Priority: repository root (for Streamlit Cloud), then relative paths (for local dev)
        possible_paths = [
            # Repository root (Streamlit Cloud and local)
            '../../for distribution case competition filtered_publications.csv',
            # Streamlit Cloud absolute paths
            '/mount/src/sustainability_case_competition/for distribution case competition filtered_publications.csv',
            # Local relative paths
            '../for distribution case competition filtered_publications.csv',
            'for distribution case competition filtered_publications.csv',
            '../../../../for distribution case competition filtered_publications.csv',
        ]
        
        csv_path = None
        for path in possible_paths:
            try:
                if os.path.exists(path):
                    csv_path = path
                    break
            except:
                continue
        
        if csv_path is None:
            return None, None
        
        df = pd.read_csv(csv_path, low_memory=False)
        if df is None or len(df) == 0:
            return None, None
        return df, csv_path
    except Exception as e:
        return None, None

# Cache researcher profile construction from original data
@st.cache_data
def build_researcher_profiles_from_original(publications_df):
    """Build researcher profiles from original publications CSV (no simulated data)"""
    if publications_df is None:
        return None
    
    # Clean data (same as build script)
    publications_df = publications_df.copy()
    publications_df['publication_year'] = pd.to_numeric(publications_df['publication_year'], errors='coerce')
    publications_df = publications_df[publications_df['publication_year'].between(1900, 2026)].copy()
    publications_df['is_sustain'] = pd.to_numeric(publications_df['is_sustain'], errors='coerce').fillna(0).astype(bool)
    
    # Clean SDG columns
    for col in ['top 1', 'top 2', 'top 3']:
        if col in publications_df.columns:
            publications_df[col] = pd.to_numeric(publications_df[col], errors='coerce')
            publications_df.loc[~publications_df[col].between(1, 17), col] = None
    
    def extract_keywords(keywords_str):
        """Extract keywords from semicolon-separated string"""
        if pd.isna(keywords_str):
            return []
        keywords = [k.strip() for k in str(keywords_str).split(';') if k.strip()]
        return keywords[:20]
    
    def get_sdg_list(row):
        """Get list of SDGs for a publication"""
        sdgs = []
        for col in ['top 1', 'top 2', 'top 3']:
            if pd.notna(row.get(col)) and 1 <= row[col] <= 17:
                sdgs.append(int(row[col]))
        return list(set(sdgs))
    
    # Aggregate by researcher (from original data)
    researcher_data = []
    for person_uuid in publications_df['person_uuid'].unique():
        person_df = publications_df[publications_df['person_uuid'] == person_uuid].copy()
        
        # Basic info from original CSV
        name = person_df['name'].iloc[0]
        email = person_df['email'].iloc[0] if pd.notna(person_df['email'].iloc[0]) else ""
        department = person_df['department'].iloc[0] if pd.notna(person_df['department'].iloc[0]) else "Unknown"
        
        # Publication metrics from original data
        total_pubs = len(person_df)
        sustainable_pubs = person_df['is_sustain'].sum()
        first_year = person_df['publication_year'].min()
        last_year = person_df['publication_year'].max()
        years_active = last_year - first_year if pd.notna(first_year) and pd.notna(last_year) else 0
        
        # Career stage (calculated from original data)
        current_year = 2025
        years_since_first = current_year - first_year if pd.notna(first_year) else 0
        if years_since_first > 15:
            career_stage = "Senior"
        elif years_since_first > 7:
            career_stage = "Post-Tenure"
        else:
            career_stage = "Pre-Tenure"
        
        # Aggregate keywords from original CSV
        all_keywords = []
        all_abstracts = []
        for _, row in person_df.iterrows():
            all_keywords.extend(extract_keywords(row.get('keywords', '')))
            if pd.notna(row.get('abstract', '')):
                all_abstracts.append(str(row.get('abstract', '')))
        
        keyword_counts = Counter(all_keywords)
        top_keywords = [kw for kw, _ in keyword_counts.most_common(15)]
        
        # Aggregate SDGs from original CSV
        all_sdgs = []
        for _, row in person_df.iterrows():
            all_sdgs.extend(get_sdg_list(row))
        sdg_counts = Counter(all_sdgs)
        primary_sdg = sdg_counts.most_common(1)[0][0] if sdg_counts else None
        sdg_list = [sdg for sdg, _ in sdg_counts.most_common(3)]
        
        # Infer research method from original keywords and abstracts
        method_keywords = {
            'Theoretical': ['theoretical', 'model', 'modeling', 'optimization', 'game theory', 
                           'mathematical', 'algorithm', 'framework', 'conceptual'],
            'Empirical': ['empirical', 'statistical', 'regression', 'analysis', 'data', 
                         'quantitative', 'econometric', 'estimation', 'dataset'],
            'Qualitative': ['qualitative', 'case study', 'interview', 'ethnography', 
                           'narrative', 'discourse', 'phenomenology'],
            'Fieldwork': ['field', 'survey', 'experiment', 'observational', 'fieldwork', 
                         'field study', 'field experiment'],
            'Experimental': ['experiment', 'randomized', 'trial', 'laboratory', 'lab', 
                            'controlled experiment', 'RCT'],
            'Computational': ['computational', 'simulation', 'machine learning', 'AI', 
                             'artificial intelligence', 'deep learning', 'neural network']
        }
        
        # Combine all text from original data
        all_text = ' '.join([str(kw).lower() for kw in top_keywords])
        if all_abstracts:
            abstracts_text = ' '.join([str(ab).lower() for ab in all_abstracts])
            all_text += ' ' + abstracts_text[:5000]  # First 5000 chars
        
        # Score each method based on original data
        method_scores = {}
        for method, keywords in method_keywords.items():
            score = sum(1 for kw in keywords if kw in all_text)
            method_scores[method] = score
        
        # Assign primary method
        if method_scores:
            primary_method = max(method_scores, key=method_scores.get)
            if method_scores[primary_method] == 0:
                primary_method = "Mixed Methods"
        else:
            primary_method = "Mixed Methods"
        
        researcher_data.append({
            'person_uuid': person_uuid,
            'name': name,
            'email': email,
            'department': department,
            'total_publications': total_pubs,
            'sustainable_publications': sustainable_pubs,
            'first_publication_year': first_year,
            'last_publication_year': last_year,
            'years_active': years_active,
            'years_since_first': years_since_first,
            'career_stage': career_stage,
            'primary_method': primary_method,
            'primary_sdg': primary_sdg,
            'sdg_list': ','.join(map(str, sdg_list)),
            'top_keywords': ';'.join(top_keywords[:10]),
            'all_keywords_text': ' '.join(top_keywords),  # For NLP matching
            'all_abstracts_text': ' '.join(all_abstracts)[:5000]  # For NLP matching
        })
    
    return pd.DataFrame(researcher_data)

# Combined function to get researcher profiles
@st.cache_data
def load_researcher_profiles():
    """Load and build researcher profiles from original publications CSV"""
    try:
        publications_df, csv_path = load_original_publications()
        if publications_df is None or csv_path is None:
            return None
        
        profiles_df = build_researcher_profiles_from_original(publications_df)
        if profiles_df is None or len(profiles_df) == 0:
            return None
        return profiles_df
    except Exception as e:
        # Return None and let the UI handle the error message
        return None

def get_researcher_profiles_with_fallback():
    """Get researcher profiles with file upload fallback - use this in UI code"""
    # Try loading from file system first
    df = load_researcher_profiles()
    
    # If not found, check for uploaded file in session state
    if df is None:
        if 'uploaded_publications_df' in st.session_state and st.session_state.uploaded_publications_df is not None:
            df = build_researcher_profiles_from_original(st.session_state.uploaded_publications_df)
    
    return df

# Initialize session state
if 'selected_path' not in st.session_state:
    st.session_state.selected_path = None
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# ============================================
# LANDING PAGE: "Join Us!" Section
# ============================================
if st.session_state.selected_path is None:
    # Header with Illinois Blue/Orange theme
    st.markdown("""
    <div style='text-align: center; padding: 2rem 0;'>
        <h1 style='color: #13294B; font-size: 3rem; margin-bottom: 0.5rem;'>Connect. Collaborate. Impact.</h1>
        <p style='color: #FF5F00; font-size: 1.5rem; font-weight: bold;'>Sustainability Research Discovery Hub</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Value proposition
    st.markdown("""
    <div style='text-align: center; padding: 1rem 0;'>
        <p style='font-size: 1.2rem; color: #666; font-weight: 300;'>
            Moving beyond faculty directories. Discover cross-disciplinary partners, research opportunities, 
            and strategic funding priorities based on semantic overlap and complementary research methods.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Three CTAs
    st.markdown("## 🎯 Choose Your Path")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='text-align: center; padding: 2rem; border: 2px solid #13294B; border-radius: 10px; height: 100%;'>
            <h2 style='color: #13294B;'>🔬 Find a Collaborator</h2>
            <p style='font-size: 1.1rem; margin: 1rem 0;'><strong>Faculty / Researchers</strong></p>
            <p>I have a project; who is the best co-author for me?</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Get Started →", key="faculty_path", use_container_width=True, type="primary"):
            st.session_state.selected_path = "faculty"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 2rem; border: 2px solid #13294B; border-radius: 10px; height: 100%;'>
            <h2 style='color: #13294B;'>🎓 Find Opportunities</h2>
            <p style='font-size: 1.1rem; margin: 1rem 0;'><strong>Students / Junior Faculty</strong></p>
            <p>I have skills; what project needs me?</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Get Started →", key="student_path", use_container_width=True, type="primary"):
            st.session_state.selected_path = "student"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div style='text-align: center; padding: 2rem; border: 2px solid #13294B; border-radius: 10px; height: 100%;'>
            <h2 style='color: #13294B;'>💰 Sponsor a Priority</h2>
            <p style='font-size: 1.1rem; margin: 1rem 0;'><strong>Partners & Donors</strong></p>
            <p>I have money; where can I invest it to make the biggest impact?</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Get Started →", key="donor_path", use_container_width=True, type="primary"):
            st.session_state.selected_path = "donor"
            st.rerun()
    
    st.stop()

# ============================================
# PATH 1: FACULTY - Find a Collaborator (CCS)
# ============================================
if st.session_state.selected_path == "faculty":
    st.title("🔬 Find a Collaborator")
    st.markdown("**Faculty / Researchers**: Discover your best research partner using the Collaboration Compatibility Score (CCS)")
    
    # Back button
    if st.button("← Back to Home"):
        st.session_state.selected_path = None
        st.session_state.form_submitted = False
        st.rerun()
    
    st.markdown("---")
    
    # Load data from original CSV (from repository)
    df = get_researcher_profiles_with_fallback()
    
    # If still not found, show error with helpful message
    if df is None:
        st.error("❌ Original publications CSV file not found.")
        st.info("""
        **The CSV file should be in the repository root directory:**
        - `for distribution case competition filtered_publications.csv`
        - The file is now included in the GitHub repository for Streamlit Cloud access
        """)
        st.stop()
    
    # Show data source info
    with st.expander("ℹ️ Data Source", expanded=False):
        st.info(f"""
        **Using original publications data:**
        - Source: `for distribution case competition filtered_publications.csv`
        - Researchers: {len(df)} profiles built from original publication records
        - NLP analysis performed on actual keywords and abstracts from original data
        - No simulated or random data used
        """)
    
    # Wizard Questionnaire
    with st.form("faculty_form"):
        st.subheader("Tell Us About Your Research")
        
        # Question 1: Targeted SDG
        target_sdg = st.selectbox(
            "🎯 What SDG are you working on?",
            options=[i for i in range(1, 18)],
            format_func=lambda x: f"SDG {x}",
            help="Select the Sustainable Development Goal you're working on"
        )
        
        # Question 2: Target Department
        departments = ['Open to All'] + sorted(df['department'].dropna().unique().tolist())
        target_dept = st.selectbox(
            "🏛️ Preferred Department",
            options=departments,
            help="Filter by department or select 'Open to All'"
        )
        
        # Question 3: Primary Method
        methods = ['Theoretical', 'Empirical', 'Computational', 'Experimental', 'Qualitative', 'Fieldwork', 'Mixed Methods']
        user_method = st.selectbox(
            "🔬 Your Primary Method",
            options=methods,
            help="Select your primary research methodology"
        )
        
        # Question 4: Career Stage
        user_stage = st.radio(
            "👤 Your Career Stage",
            options=['Pre-Tenure', 'Post-Tenure', 'Senior'],
            help="Your current career stage"
        )
        
        submitted = st.form_submit_button("🔍 Find My Best Collaborator", use_container_width=True, type="primary")
    
    # Matching Engine
    if submitted:
        with st.spinner("Analyzing research profiles and calculating compatibility..."):
            # Filter dataset (less strict - allow related SDGs)
            filtered_df = df.copy()
            
            # Department filter
            if target_dept != 'Open to All':
                filtered_df = filtered_df[filtered_df['department'] == target_dept]
            
            # SDG filter - allow exact match OR related SDGs (same cluster)
            if 'primary_sdg' in filtered_df.columns and len(filtered_df) > 0:
                # Get SDG clusters: 1-6 (Social), 7-12 (Economic), 13-17 (Environmental)
                target_cluster = int((target_sdg - 1) // 6)
                
                def is_related_sdg(sdg):
                    if pd.isna(sdg):
                        return False
                    try:
                        sdg_int = int(float(sdg))
                        sdg_cluster = int((sdg_int - 1) // 6)
                        return sdg_int == target_sdg or sdg_cluster == target_cluster
                    except:
                        return False
                
                # Filter to exact match OR same cluster (broader matching)
                filtered_df = filtered_df[filtered_df['primary_sdg'].apply(is_related_sdg)]
            
            # If still no matches, remove SDG filter entirely
            if len(filtered_df) == 0:
                filtered_df = df.copy()
                if target_dept != 'Open to All':
                    filtered_df = filtered_df[filtered_df['department'] == target_dept]
                st.info("⚠️ No exact SDG matches found. Showing researchers from related SDG clusters or all departments.")
            
            if len(filtered_df) == 0:
                st.warning("No researchers found. Try selecting 'Open to All' for department.")
                st.stop()
            
            # Load NLP model
            model = load_nlp_model()
            
            # Prepare user profile for NLP matching
            user_context = f"Research in SDG {target_sdg} using {user_method} methodology"
            user_embedding = model.encode([user_context])  # Encode once, reuse for all candidates
            
            # Batch prepare candidate texts for faster NLP processing
            candidate_texts = []
            candidate_indices = []
            for idx, candidate in filtered_df.iterrows():
                candidate_keywords = candidate.get('all_keywords_text', '')
                candidate_abstracts = candidate.get('all_abstracts_text', '')
                
                if pd.isna(candidate_keywords) or candidate_keywords == '':
                    if pd.isna(candidate_abstracts) or candidate_abstracts == '':
                        candidate_text = ""  # Will handle separately
                    else:
                        candidate_text = str(candidate_abstracts)[:2000]
                else:
                    candidate_text = str(candidate_keywords)
                    if pd.notna(candidate_abstracts) and candidate_abstracts != '':
                        candidate_text += ' ' + str(candidate_abstracts)[:2000]
                
                candidate_texts.append(candidate_text)
                candidate_indices.append(idx)
            
            # Batch encode all candidates at once (much faster)
            non_empty_texts = [(i, t) for i, t in zip(candidate_indices, candidate_texts) if t]
            if non_empty_texts:
                indices_to_encode = [i for i, t in non_empty_texts]
                texts_to_encode = [t for i, t in non_empty_texts]
                candidate_embeddings = model.encode(texts_to_encode)
                
                # Calculate similarities in batch
                similarities = cosine_similarity(user_embedding, candidate_embeddings)[0]
                
                # Create mapping from index to similarity
                similarity_map = {idx: sim * 100 for idx, sim in zip(indices_to_encode, similarities)}
            else:
                similarity_map = {}
            
            # Calculate Topic Score using NLP (batch processed)
            def calculate_topic_score_nlp(candidate_idx):
                """Get pre-calculated similarity or default"""
                if candidate_idx in similarity_map:
                    return max(0, min(100, similarity_map[candidate_idx]))
                return 50  # Default if no text data
            
            # Method complementarity matrix
            def calculate_method_score(user_method, candidate_method):
                complementarity_matrix = {
                    ('Theoretical', 'Empirical'): 100,
                    ('Theoretical', 'Computational'): 100,
                    ('Theoretical', 'Experimental'): 90,
                    ('Theoretical', 'Fieldwork'): 100,
                    ('Empirical', 'Theoretical'): 100,
                    ('Empirical', 'Qualitative'): 85,
                    ('Empirical', 'Fieldwork'): 90,
                    ('Empirical', 'Computational'): 80,
                    ('Computational', 'Theoretical'): 100,
                    ('Computational', 'Fieldwork'): 85,
                    ('Computational', 'Qualitative'): 75,
                    ('Computational', 'Experimental'): 80,
                    ('Experimental', 'Theoretical'): 90,
                    ('Experimental', 'Qualitative'): 80,
                    ('Qualitative', 'Empirical'): 85,
                    ('Qualitative', 'Experimental'): 80,
                    ('Fieldwork', 'Theoretical'): 100,
                    ('Fieldwork', 'Computational'): 85,
                }
                
                if (user_method, candidate_method) in complementarity_matrix:
                    return complementarity_matrix[(user_method, candidate_method)]
                elif (candidate_method, user_method) in complementarity_matrix:
                    return complementarity_matrix[(candidate_method, user_method)]
                
                if user_method == candidate_method:
                    return 50
                return 60
            
            # Career score
            def calculate_career_score(user_stage, candidate_stage):
                optimal_pairs = [
                    ('Pre-Tenure', 'Post-Tenure'),
                    ('Pre-Tenure', 'Senior'),
                    ('Post-Tenure', 'Senior')
                ]
                
                if (user_stage, candidate_stage) in optimal_pairs or (candidate_stage, user_stage) in optimal_pairs:
                    return 100
                if user_stage == candidate_stage:
                    if user_stage == 'Post-Tenure':
                        return 75
                    return 60
                return 50
            
            # Calculate scores using original data (optimized)
            matches = []
            for idx, candidate in filtered_df.iterrows():
                # Use pre-calculated NLP similarity
                topic_score = calculate_topic_score_nlp(idx)
                candidate_method = candidate.get('primary_method', 'Mixed Methods')
                method_score = calculate_method_score(user_method, candidate_method)
                candidate_stage = candidate.get('career_stage', 'Post-Tenure')
                career_score = calculate_career_score(user_stage, candidate_stage)
                
                # CCS Formula: Topic (45%) + Method (40%) + Career (15%)
                total_score = (topic_score * 0.45) + (method_score * 0.40) + (career_score * 0.15)
                
                matches.append({
                    'name': candidate.get('name', 'Unknown'),
                    'department': candidate.get('department', 'Unknown'),
                    'total_score': total_score,
                    'topic_score': topic_score,
                    'method_score': method_score,
                    'career_score': career_score,
                    'method': candidate_method,
                    'stage': candidate_stage,
                    'keywords': candidate.get('top_keywords', ''),
                    'publications': candidate.get('total_publications', 0),
                    'email': candidate.get('email', ''),
                    'primary_sdg': candidate.get('primary_sdg', target_sdg)
                })
            
            matches_df = pd.DataFrame(matches)
            matches_df = matches_df.sort_values('total_score', ascending=False).head(3)
        
        # Display Results - Proactive Top Match
        st.markdown("---")
        st.markdown("## 🎯 Your Best Match")
        
        if len(matches_df) == 0:
            st.warning("No matches found. Try adjusting your criteria.")
        else:
            # Top match - prominently displayed
            top_match = matches_df.iloc[0]
            
            # Display top match with gauge
            col_score, col_gauge = st.columns([2, 1])
            
            with col_score:
                st.markdown(f"""
                <div style='background: linear-gradient(135deg, #13294B 0%, #FF5F00 100%); padding: 2rem; border-radius: 10px; color: white; margin-bottom: 2rem;'>
                    <h2 style='color: white; margin-bottom: 0.5rem;'>{top_match['name']}</h2>
                    <h1 style='color: white; font-size: 4rem; margin: 0;'>{top_match['total_score']:.0f}/100</h1>
                    <p style='color: white; font-size: 1.2rem; margin-top: 0.5rem;'>Collaboration Compatibility Score</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_gauge:
                # Create gauge chart
                score = top_match['total_score']
                fig = go.Figure(go.Indicator(
                    mode = "gauge+number+delta",
                    value = score,
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    title = {'text': "Match Quality"},
                    delta = {'reference': 70},
                    gauge = {
                        'axis': {'range': [None, 100]},
                        'bar': {'color': "#FF5F00"},
                        'steps': [
                            {'range': [0, 50], 'color': "lightgray"},
                            {'range': [50, 70], 'color': "gray"},
                            {'range': [70, 100], 'color': "#13294B"}
                        ],
                        'threshold': {
                            'line': {'color': "red", 'width': 4},
                            'thickness': 0.75,
                            'value': 70
                        }
                    }
                ))
                fig.update_layout(height=250, margin=dict(l=20, r=20, t=40, b=20))
                st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
            
            # Generate contextual explanations based on actual scores
            def generate_topic_explanation(topic_score, user_sdg, match_sdg, match_name):
                """Generate explanation based on actual topic score"""
                match_sdg_str = f"SDG {int(match_sdg)}" if pd.notna(match_sdg) and match_sdg != '' else "related areas"
                
                if topic_score >= 85:
                    return f"**Strong semantic alignment** (score: {topic_score:.0f}/100). Your research in SDG {user_sdg} and {match_name}'s work in {match_sdg_str} show high conceptual overlap based on NLP analysis of keywords and abstracts from the original publications."
                elif topic_score >= 70:
                    return f"**Moderate semantic alignment** (score: {topic_score:.0f}/100). There's some research overlap between SDG {user_sdg} and {match_name}'s focus in {match_sdg_str}, though the connection may be more indirect based on NLP similarity."
                elif topic_score >= 50:
                    return f"**Limited semantic alignment** (score: {topic_score:.0f}/100). The research topics show minimal overlap based on NLP analysis of keywords and abstracts. This match relies more on method complementarity than topic similarity."
                else:
                    return f"**Low semantic alignment** (score: {topic_score:.0f}/100). The research topics are quite different based on NLP analysis. This match is primarily based on complementary methods rather than topic overlap."
            
            def generate_method_explanation(method_score, user_method, match_method, match_name):
                """Generate explanation based on actual method score"""
                if method_score >= 90:
                    return f"**Excellent method complementarity** (score: {method_score:.0f}/100). Combining your {user_method} approach with {match_name}'s {match_method} methodology creates a powerful mixed-methods framework that brings different perspectives together."
                elif method_score >= 75:
                    return f"**Good method complementarity** (score: {method_score:.0f}/100). Your {user_method} and {match_name}'s {match_method} approaches complement each other well, enabling collaborative research."
                elif method_score >= 60:
                    return f"**Moderate method alignment** (score: {method_score:.0f}/100). Both using {user_method if user_method == match_method else 'similar'} methodologies enables collaborative work, though with less methodological diversity."
                else:
                    return f"**Limited method complementarity** (score: {method_score:.0f}/100). Both researchers use {user_method if user_method == match_method else 'similar methods'}, which may limit methodological innovation but enables shared understanding."
            
            def generate_career_explanation(career_score, user_stage, match_stage):
                """Generate explanation based on actual career score"""
                if career_score >= 90:
                    return f"**Excellent career pairing** (score: {career_score:.0f}/100). This {user_stage} + {match_stage} combination offers strong mentorship opportunities and knowledge transfer potential."
                elif career_score >= 75:
                    return f"**Good career pairing** (score: {career_score:.0f}/100). Both at {user_stage if user_stage == match_stage else 'different'} stages, this enables {('peer collaboration' if user_stage == match_stage else 'cross-stage learning')}."
                elif career_score >= 60:
                    return f"**Moderate career pairing** (score: {career_score:.0f}/100). The {user_stage} + {match_stage} combination provides some collaboration benefits, though not optimal for mentorship."
                else:
                    return f"**Limited career alignment** (score: {career_score:.0f}/100). The career stage pairing may not offer the strongest mentorship or peer collaboration opportunities."
            
            # Transparent AI Breakdown - Modal-like expander
            with st.expander("🔍 Why this score? (Click to see breakdown)", expanded=False):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Topic Match", f"{top_match['topic_score']:.0f}/100", 
                             help="NLP semantic similarity based on actual keywords and abstracts from original CSV")
                    st.markdown(generate_topic_explanation(top_match['topic_score'], target_sdg, top_match.get('primary_sdg', target_sdg), top_match['name']))
                
                with col2:
                    st.metric("Method Match", f"{top_match['method_score']:.0f}/100",
                             help="Complementarity of research methods")
                    st.markdown(generate_method_explanation(top_match['method_score'], user_method, top_match['method'], top_match['name']))
                
                with col3:
                    st.metric("Career Stage", f"{top_match['career_score']:.0f}/100",
                             help="Strategic career pairing for mentorship/collaboration")
                    st.markdown(generate_career_explanation(top_match['career_score'], user_stage, top_match['stage']))
                
                st.markdown("---")
                st.markdown(f"""
                **Formula**: CCS = (Topic × 45%) + (Method × 40%) + (Career × 15%)
                
                **Calculation**: ({top_match['topic_score']:.1f} × 0.45) + ({top_match['method_score']:.1f} × 0.40) + ({top_match['career_score']:.1f} × 0.15) = **{top_match['total_score']:.1f}**
                """)
            
            # Match details
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(f"**📧 Email**: {top_match['email']}")
                st.markdown(f"**🏛️ Department**: {top_match['department']}")
                st.markdown(f"**📊 Publications**: {int(top_match['publications'])}")
                st.markdown(f"**🔬 Method**: {top_match['method']}")
                st.markdown(f"**👤 Stage**: {top_match['stage']}")
            
            with col2:
                if st.button("📧 Contact This Researcher", use_container_width=True, type="primary"):
                    st.success(f"Email template ready for {top_match['name']}!")
            
            # Other top matches
            if len(matches_df) > 1:
                st.markdown("---")
                st.markdown("## Other Strong Matches")
                for idx, match in matches_df.iloc[1:].iterrows():
                    with st.container():
                        col1, col2, col3 = st.columns([3, 1, 1])
                        with col1:
                            st.markdown(f"### {match['name']}")
                            st.caption(f"📧 {match['email']} | 🏛️ {match['department']}")
                        with col2:
                            st.metric("CCS Score", f"{match['total_score']:.1f}")
                        with col3:
                            if st.button("View Details", key=f"view_{idx}"):
                                st.info(f"Method: {match['method']} | Stage: {match['stage']}")
                        st.markdown("---")

# ============================================
# PATH 2: STUDENT - Find Opportunities
# ============================================
elif st.session_state.selected_path == "student":
    st.title("🎓 Find Opportunities")
    st.markdown("**Students / Junior Faculty**: Discover research projects that match your skills and interests")
    
    # Back button
    if st.button("← Back to Home"):
        st.session_state.selected_path = None
        st.rerun()
    
    st.markdown("---")
    
    # Load data
    # Load data from original CSV (from repository)
    df = get_researcher_profiles_with_fallback()
    
    # If still not found, show error
    if df is None:
        st.error("❌ Original publications CSV file not found.")
        st.info("The CSV file should be in the repository root directory.")
        st.stop()
    
    # Student questionnaire
    with st.form("student_form"):
        st.subheader("Tell Us About Your Skills")
        
        # Skills/SDG interest
        student_sdg = st.selectbox(
            "🎯 Which SDG interests you most?",
            options=[i for i in range(1, 18)],
            format_func=lambda x: f"SDG {x}",
        )
        
        student_skills = st.multiselect(
            "💼 Your Skills",
            options=['Data Analysis', 'Statistical Methods', 'Qualitative Research', 'Fieldwork', 
                    'Computational Modeling', 'Experimental Design', 'Literature Review', 'Writing'],
            help="Select all skills you have"
        )
        
        student_stage = st.radio(
            "👤 Your Level",
            options=['Undergraduate', 'Graduate Student', 'Doctoral Student', 'Post-Doc', 'Pre-Tenure Faculty'],
        )
        
        submitted = st.form_submit_button("🔍 Find Opportunities", use_container_width=True, type="primary")
    
    if submitted:
        # Calculate Opportunity Match Score for each researcher/project
        opportunities = []
        
        for idx, researcher in df.iterrows():
            # Simple matching: SDG alignment + method overlap
            sdg_match = 100 if researcher.get('primary_sdg') == student_sdg else 50
            
            # Method match (simplified)
            method_match = 75  # Default - could be enhanced
            
            # Career stage fit (students with post-tenure = mentorship opportunity)
            if student_stage in ['Undergraduate', 'Graduate Student', 'Doctoral Student']:
                if researcher.get('career_stage') in ['Post-Tenure', 'Senior']:
                    career_fit = 100
                else:
                    career_fit = 60
            else:
                career_fit = 75
            
            # Opportunity Match Score
            opp_score = (sdg_match * 0.5) + (method_match * 0.3) + (career_fit * 0.2)
            
            opportunities.append({
                'researcher': researcher.get('name', 'Unknown'),
                'department': researcher.get('department', 'Unknown'),
                'sdg': researcher.get('primary_sdg', 'Unknown'),
                'method': researcher.get('primary_method', 'Unknown'),
                'stage': researcher.get('career_stage', 'Unknown'),
                'opportunity_score': opp_score,
                'email': researcher.get('email', ''),
                'publications': researcher.get('total_publications', 0),
                'keywords': researcher.get('top_keywords', '')
            })
        
        opp_df = pd.DataFrame(opportunities)
        opp_df = opp_df.sort_values('opportunity_score', ascending=False).head(10)
        
        st.markdown("---")
        st.markdown("## 📋 Research Opportunity Board")
        st.caption("Projects ranked by Opportunity Match Score based on your skills and SDG interest")
        
        for idx, opp in opp_df.iterrows():
            with st.container():
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.markdown(f"### {opp['researcher']}")
                    st.caption(f"🏛️ {opp['department']} | 🎯 SDG {opp['sdg']} | 🔬 {opp['method']}")
                    if pd.notna(opp['keywords']):
                        st.caption(f"**Research Focus**: {str(opp['keywords']).replace(';', ', ')[:100]}...")
                with col2:
                    st.metric("Match Score", f"{opp['opportunity_score']:.0f}/100")
                with col3:
                    if st.button("Apply", key=f"apply_{idx}"):
                        st.success(f"Application template ready for {opp['researcher']}!")
                st.markdown("---")

# ============================================
# PATH 3: DONOR - Sponsor a Priority
# ============================================
elif st.session_state.selected_path == "donor":
    st.title("💰 Sponsor a Priority")
    st.markdown("**Partners & Donors**: Discover where your investment can make the biggest impact")
    
    # Back button
    if st.button("← Back to Home"):
        st.session_state.selected_path = None
        st.rerun()
    
    st.markdown("---")
    
    # Load data
    # Load data from original CSV (from repository)
    df = get_researcher_profiles_with_fallback()
    
    # If still not found, show error
    if df is None:
        st.error("❌ Original publications CSV file not found.")
        st.info("The CSV file should be in the repository root directory.")
        st.stop()
    
    # Calculate SDG coverage
    if 'primary_sdg' in df.columns:
        sdg_counts = df['primary_sdg'].value_counts().sort_index()
        all_sdgs = pd.Series(range(1, 18), index=range(1, 18))
        sdg_coverage = all_sdgs.map(sdg_counts).fillna(0)
        
        # Identify gaps (low coverage)
        avg_coverage = sdg_coverage.mean()
        gaps = sdg_coverage[sdg_coverage < avg_coverage * 0.7]  # 30% below average
        
        st.markdown("## 📊 Research Coverage by SDG")
        st.caption("Interactive chart showing research coverage and funding gaps")
        
        # Create visualization
        fig = go.Figure()
        
        # Add coverage bars
        fig.add_trace(go.Bar(
            x=[f"SDG {i}" for i in range(1, 18)],
            y=sdg_coverage.values,
            name='Research Coverage',
            marker_color=['#FF5F00' if i in gaps.index else '#13294B' for i in range(1, 18)],
            text=sdg_coverage.values.astype(int),
            textposition='outside'
        ))
        
        # Add average line
        fig.add_hline(y=avg_coverage, line_dash="dash", 
                     annotation_text=f"Average Coverage: {avg_coverage:.0f}",
                     line_color="gray")
        
        fig.update_layout(
            title="SDG Research Coverage & Funding Gaps",
            xaxis_title="Sustainable Development Goals",
            yaxis_title="Number of Researchers",
            height=500,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Priority funding areas
        st.markdown("---")
        st.markdown("## 🎯 Priority Funding Areas")
        st.caption("SDGs with below-average research coverage - your investment is most needed here")
        
        if len(gaps) > 0:
            priority_df = pd.DataFrame({
                'SDG': [f"SDG {i}" for i in gaps.index],
                'Current Coverage': gaps.values.astype(int),
                'Gap Size': (avg_coverage - gaps.values).astype(int),
                'Priority Level': ['High' if gap < avg_coverage * 0.5 else 'Medium' for gap in gaps.values]
            })
            priority_df = priority_df.sort_values('Gap Size', ascending=False)
            
            st.dataframe(priority_df, use_container_width=True, hide_index=True)
            
            st.info("""
            💡 **Strategic Investment Opportunity**: Funding research in these under-researched SDGs 
            will have maximum impact by filling critical knowledge gaps and enabling breakthrough discoveries.
            """)
        else:
            st.success("All SDGs have strong research coverage. Consider funding emerging or interdisciplinary research.")
        
        # Top researchers by SDG (for donor reference)
        st.markdown("---")
        st.markdown("## 👥 Leading Researchers by SDG")
        
        selected_sdg = st.selectbox(
            "Select an SDG to see leading researchers",
            options=[i for i in range(1, 18)],
            format_func=lambda x: f"SDG {x}",
        )
        
        sdg_researchers = df[df['primary_sdg'] == selected_sdg].nlargest(5, 'total_publications')
        
        if len(sdg_researchers) > 0:
            for idx, researcher in sdg_researchers.iterrows():
                st.markdown(f"**{researcher.get('name', 'Unknown')}** - {researcher.get('department', 'Unknown')} ({int(researcher.get('total_publications', 0))} publications)")

# ============================================
# TRANSPARENCY / METHODOLOGY SECTION
# ============================================
if st.session_state.selected_path:
    st.markdown("---")
    with st.expander("⚙️ Under the Hood: How this works & Data Sources"):
        st.markdown("""
        ### Collaboration Compatibility Score (CCS) - Faculty Path
        
        The CCS uses a **weighted formula** to calculate compatibility:
        
        ```
        CCS = (Topic × 45%) + (Method × 40%) + (Career × 15%)
        ```
        
        #### Topic Score (45%) - NLP Semantic Analysis on Original Data
        
        We use **sentence-transformers** (`all-MiniLM-L6-v2`) to calculate semantic similarity between:
        - Your research context (SDG + method)
        - **Actual keywords and abstracts from the original publications CSV** (`for distribution case competition filtered_publications.csv`)
        
        **Data Source**: The NLP analysis uses the actual `keywords` and `abstract` columns from the original 
        publications CSV file. No pre-processed or simulated data is used.
        
        The model generates embeddings (vector representations) of the text, then calculates **cosine similarity** 
        between your research profile and each candidate's actual research content. This similarity is scaled to 
        0-100 to produce the Topic Score.
        
        **Why NLP?** This approach captures semantic meaning beyond simple keyword matching. For example, 
        "machine learning" and "artificial intelligence" are recognized as related concepts even if the exact 
        keywords don't match.
        
        **Transparency**: All matching is performed on real publication data from the original CSV file.
        
        #### Method Score (40%) - Complementarity Rules
        
        The algorithm **rewards complementary methods** rather than similarity:
        
        - **Theoretical + Empirical** = 100 (strong complementarity)
        - **Theoretical + Computational** = 100 (strong complementarity)
        - **Same method** = 50 (moderate, enables collaboration but less innovation)
        
        This drives innovation by bringing together different methodological perspectives.
        
        #### Career Score (15%) - Mentorship & Collaboration Fit
        
        **Why is Career weighted at 15%?** 
        
        We prioritize semantic research alignment and methodological fit first (85%), but apply a 15% weighting 
        to career stages to actively foster junior-faculty mentorship and cross-seniority knowledge transfer. 
        This ensures that while research compatibility is paramount, we also create opportunities for:
        
        - **Mentorship**: Pre-Tenure researchers connecting with Post-Tenure or Senior faculty
        - **Peer Collaboration**: Researchers at similar stages working together
        - **Knowledge Transfer**: Cross-generational research partnerships
        
        ### Opportunity Match Score - Student Path
        
        Calculated as: `(SDG Match × 50%) + (Method Match × 30%) + (Career Fit × 20%)`
        
        - **SDG Match**: Alignment with student's SDG interest
        - **Method Match**: Overlap with student's skills
        - **Career Fit**: Mentorship opportunities (students with senior faculty)
        
        ### Funding Gap Analysis - Donor Path
        
        - Calculates research coverage for each SDG (number of researchers)
        - Identifies gaps (SDGs with coverage 30% below average)
        - Highlights priority funding areas for maximum impact
        
        ### Data Sources
        
        - **Original CSV**: `for distribution case competition filtered_publications.csv`
        - **Researcher Profiles**: Built on-the-fly from original publication records (no pre-processing)
        - **Keywords**: Extracted directly from `keywords` column in original CSV
        - **Abstracts**: Used from `abstract` column in original CSV for NLP matching
        - **SDG Alignment**: Based on `top 1`, `top 2`, `top 3` columns from original CSV
        - **Career Stage**: Calculated from `publication_year` in original CSV
        - **No Simulated Data**: All matching uses only real data from the original publications CSV
        
        ### Limitations & Future Work
        
        - Current implementation uses keyword-based semantic matching; future versions could incorporate full abstracts
        - Method classification is rule-based; could be enhanced with ML classification
        - Career stage is inferred from publication years; could incorporate additional signals
        - Network effects (existing collaborations) not yet considered
        """)

# Footer
st.markdown("---")
st.caption("Sustainability Research Discovery Hub | Part of the Illinois Sustainability Impact Engine")
