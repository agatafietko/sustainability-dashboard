"""
Build CCS Demo Data from Original University CSV
Transforms publication-level data into collaboration matching dataset for Power BI
"""

import pandas as pd
import numpy as np
from collections import Counter
import random
import re

print("="*70)
print("CCS DEMO DATA BUILDER - From Original University CSV")
print("="*70)

# ============================================
# STEP 1: Load Original CSV
# ============================================
print("\n1. Loading original university CSV...")
df = pd.read_csv('for distribution case competition filtered_publications.csv', low_memory=False)
print(f"✓ Loaded {len(df)} publication records")

# Clean data
df['publication_year'] = pd.to_numeric(df['publication_year'], errors='coerce')
df = df[df['publication_year'].between(1900, 2026)].copy()
df['is_sustain'] = pd.to_numeric(df['is_sustain'], errors='coerce').fillna(0).astype(bool)

# Clean SDG columns
for col in ['top 1', 'top 2', 'top 3']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        df.loc[~df[col].between(1, 17), col] = None

print(f"✓ Cleaned data: {len(df)} valid records")

# ============================================
# STEP 2: Aggregate to Researcher Profiles
# ============================================
print("\n2. Aggregating publications to researcher profiles...")

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

# Method inference keywords
method_keywords = {
    'Theoretical': ['theoretical', 'model', 'modeling', 'optimization', 'game theory', 
                   'mathematical', 'algorithm', 'framework', 'conceptual', 'analytical'],
    'Empirical': ['empirical', 'statistical', 'regression', 'analysis', 'data', 
                 'quantitative', 'econometric', 'estimation', 'dataset', 'statistics'],
    'Qualitative': ['qualitative', 'case study', 'interview', 'ethnography', 
                   'narrative', 'discourse', 'phenomenology', 'grounded theory'],
    'Fieldwork': ['field', 'survey', 'experiment', 'observational', 'fieldwork', 
                 'field study', 'field experiment', 'natural experiment'],
    'Experimental': ['experiment', 'randomized', 'trial', 'laboratory', 'lab', 
                    'controlled experiment', 'RCT', 'randomized controlled'],
    'Computational': ['computational', 'simulation', 'machine learning', 'AI', 
                     'artificial intelligence', 'deep learning', 'neural network', 
                     'algorithm', 'computational model']
}

researcher_data = []
for person_uuid in df['person_uuid'].unique():
    person_df = df[df['person_uuid'] == person_uuid].copy()
    
    # Basic info
    name = person_df['name'].iloc[0]
    email = person_df['email'].iloc[0] if pd.notna(person_df['email'].iloc[0]) else ""
    department = person_df['department'].iloc[0] if pd.notna(person_df['department'].iloc[0]) else "Unknown"
    
    # Publication metrics
    total_pubs = len(person_df)
    sustainable_pubs = person_df['is_sustain'].sum()
    first_year = person_df['publication_year'].min()
    last_year = person_df['publication_year'].max()
    years_active = last_year - first_year if pd.notna(first_year) and pd.notna(last_year) else 0
    
    # Career stage
    current_year = 2025
    years_since_first = current_year - first_year if pd.notna(first_year) else 0
    if years_since_first > 15:
        career_stage = "Senior"
    elif years_since_first > 7:
        career_stage = "Post-Tenure"
    else:
        career_stage = "Pre-Tenure"
    
    # Aggregate keywords
    all_keywords = []
    for _, row in person_df.iterrows():
        all_keywords.extend(extract_keywords(row.get('keywords', '')))
    keyword_counts = Counter(all_keywords)
    top_keywords = [kw for kw, _ in keyword_counts.most_common(15)]
    
    # Aggregate SDGs
    all_sdgs = []
    for _, row in person_df.iterrows():
        all_sdgs.extend(get_sdg_list(row))
    sdg_counts = Counter(all_sdgs)
    primary_sdg = sdg_counts.most_common(1)[0][0] if sdg_counts else None
    sdg_list = [sdg for sdg, _ in sdg_counts.most_common(3)]
    
    # Infer research method
    all_text = ' '.join([str(kw).lower() for kw in top_keywords])
    if 'abstract' in person_df.columns:
        abstracts = ' '.join([str(ab).lower() for ab in person_df['abstract'].dropna()])
        all_text += ' ' + abstracts[:5000]
    
    method_scores = {}
    for method, keywords in method_keywords.items():
        score = sum(1 for kw in keywords if kw in all_text)
        method_scores[method] = score
    
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
        'top_keywords': ';'.join(top_keywords[:10])
    })

researchers = pd.DataFrame(researcher_data)
print(f"✓ Extracted {len(researchers)} researcher profiles")

# ============================================
# STEP 3: Select Diverse Top Researchers
# ============================================
print("\n3. Selecting diverse top researchers...")

# Filter to researchers with valid data
valid_researchers = researchers[
    (researchers['total_publications'] >= 5) &
    (researchers['primary_sdg'].notna()) &
    (researchers['primary_method'].notna())
].copy()

print(f"✓ Found {len(valid_researchers)} researchers with >=5 publications and valid SDG/method")

# Select diverse mix by career stage
pre_tenure = valid_researchers[valid_researchers['career_stage'] == 'Pre-Tenure'].nlargest(6, 'total_publications').copy()
post_tenure = valid_researchers[valid_researchers['career_stage'] == 'Post-Tenure'].nlargest(7, 'total_publications').copy()
senior = valid_researchers[valid_researchers['career_stage'] == 'Senior'].nlargest(3, 'total_publications').copy()

top_researchers = pd.concat([pre_tenure, post_tenure, senior], ignore_index=True).copy()

# Fill to 15 if needed
if len(top_researchers) < 15:
    remaining = valid_researchers[~valid_researchers['name'].isin(top_researchers['name'])].nlargest(15 - len(top_researchers), 'total_publications')
    top_researchers = pd.concat([top_researchers, remaining], ignore_index=True).copy()

print(f"✓ Selected {len(top_researchers)} researchers")
print(f"  - Pre-Tenure: {len(top_researchers[top_researchers['career_stage'] == 'Pre-Tenure'])}")
print(f"  - Post-Tenure: {len(top_researchers[top_researchers['career_stage'] == 'Post-Tenure'])}")
print(f"  - Senior: {len(top_researchers[top_researchers['career_stage'] == 'Senior'])}")

# ============================================
# STEP 4: Scoring Functions
# ============================================

def calculate_topic_match(user_sdg, match_sdg):
    """Topic Match Score (0-100) - 45% weight"""
    if pd.isna(user_sdg) or pd.isna(match_sdg):
        return random.randint(70, 80)
    
    user_sdg = float(user_sdg)
    match_sdg = float(match_sdg)
    
    # Exact match = highest score
    if user_sdg == match_sdg:
        return random.randint(90, 95)
    
    # Related SDGs (same cluster)
    user_cluster = int((user_sdg - 1) // 6)
    match_cluster = int((match_sdg - 1) // 6)
    
    if user_cluster == match_cluster:
        return random.randint(85, 90)
    
    # Different clusters
    return random.randint(70, 80)

def calculate_method_match(user_method, match_method):
    """Method Match Score (0-100) - 40% weight"""
    if pd.isna(user_method) or pd.isna(match_method):
        return random.randint(70, 80)
    
    # Define complementary pairs
    quantitative = ['Theoretical', 'Empirical', 'Computational', 'Experimental']
    qualitative = ['Qualitative', 'Fieldwork']
    
    user_quant = user_method in quantitative
    match_quant = match_method in quantitative
    user_qual = user_method in qualitative
    match_qual = match_method in qualitative
    
    # Different types (quantitative + qualitative) = high complementarity
    if (user_quant and match_qual) or (user_qual and match_quant):
        return random.randint(85, 95)
    
    # Same method = medium
    if user_method == match_method:
        if user_method == "Mixed Methods":
            return random.randint(75, 80)
        return random.randint(70, 80)
    
    # Different but same type = moderate
    return random.randint(75, 85)

def calculate_career_fit(user_stage, match_stage):
    """Career Fit Score (0-100) - 15% weight"""
    if pd.isna(user_stage) or pd.isna(match_stage):
        return random.randint(70, 80)
    
    # Optimal mentorship pairs
    mentorship_pairs = [
        ('Pre-Tenure', 'Post-Tenure'),
        ('Pre-Tenure', 'Senior'),
        ('Post-Tenure', 'Senior')
    ]
    
    if (user_stage, match_stage) in mentorship_pairs or (match_stage, user_stage) in mentorship_pairs:
        return random.randint(85, 92)
    
    # Same stage = peer collaboration
    if user_stage == match_stage:
        if user_stage == 'Post-Tenure':
            return random.randint(75, 82)
        else:
            return random.randint(70, 78)
    
    # Other combinations
    return random.randint(70, 80)

def generate_explanation(user_row, match_row, topic_score, method_score, career_score):
    """Generate explanation text (150-200 characters)"""
    # Get top keywords (first 2)
    top_keywords = str(match_row.get('top_keywords', '')).split(';')[:2]
    keywords_str = ' and '.join([kw.strip() for kw in top_keywords if kw.strip()])
    
    user_method = user_row.get('primary_method', 'Unknown')
    match_method = match_row.get('primary_method', 'Unknown')
    
    # Method description
    if method_score >= 85:
        method_desc = f"Complementary methods ({user_method} + {match_method}) create strong synergy."
    elif method_score >= 75:
        method_desc = f"Similar methods ({user_method} + {match_method}) enable collaboration."
    else:
        method_desc = f"Method alignment ({user_method} + {match_method}) supports research."
    
    # Career pairing
    user_stage = user_row.get('career_stage', 'Unknown')
    match_stage = match_row.get('career_stage', 'Unknown')
    
    if career_score >= 85:
        if user_stage == 'Pre-Tenure' and match_stage in ['Post-Tenure', 'Senior']:
            career_desc = f"Excellent mentorship: {match_stage} guides {user_stage}."
        else:
            career_desc = f"Strong mentorship pairing: {user_stage} + {match_stage}."
    elif user_stage == match_stage:
        career_desc = f"Peer collaboration: Both at {user_stage} stage."
    else:
        career_desc = f"Career pairing: {user_stage} + {match_stage}."
    
    # Combine
    if keywords_str:
        explanation = f"Expertise in {keywords_str}. {method_desc} {career_desc}"
    else:
        explanation = f"{method_desc} {career_desc}"
    
    # Trim to 200 characters if needed
    if len(explanation) > 200:
        explanation = explanation[:197] + "..."
    
    return explanation

# ============================================
# STEP 5: Generate Collaboration Matches
# ============================================
print("\n4. Generating collaboration matches...")

demo_data = []
possible_sdgs = [7, 8, 9, 12, 13]  # For varying User_SDG
possible_methods = ['Theoretical', 'Empirical', 'Qualitative', 'Fieldwork', 'Computational', 'Experimental', 'Mixed Methods']

# All researchers for matching (excluding top researchers)
all_researchers = valid_researchers[~valid_researchers['name'].isin(top_researchers['name'])].copy()

for idx, user_row in top_researchers.iterrows():
    user_name = user_row['name']
    
    # Determine User_SDG (70% use actual, 30% vary)
    if random.random() < 0.7:
        user_sdg = user_row['primary_sdg']
    else:
        user_sdg = random.choice(possible_sdgs)
    
    # Determine User_Method (60% use actual, 40% vary)
    if random.random() < 0.6:
        user_method = user_row['primary_method']
    else:
        user_method = random.choice(possible_methods)
    
    # User_Stage always uses actual
    user_stage = user_row['career_stage']
    
    # Find potential matches
    potential_matches = all_researchers[
        (all_researchers['name'] != user_name) &
        (all_researchers['primary_sdg'].notna()) &
        (all_researchers['primary_method'].notna())
    ].copy()
    
    if len(potential_matches) == 0:
        # Use other top researchers if needed
        potential_matches = top_researchers[
            (top_researchers['name'] != user_name) &
            (top_researchers['primary_sdg'].notna()) &
            (top_researchers['primary_method'].notna())
        ].copy()
    
    # Select 2-3 matches
    num_matches = random.randint(2, 3)
    selected_matches = potential_matches.sample(min(num_matches, len(potential_matches))).copy()
    
    print(f"  {user_name}: Generating {len(selected_matches)} matches...")
    
    for match_idx, match_row in selected_matches.iterrows():
        # Calculate scores
        topic_score = calculate_topic_match(user_sdg, match_row.get('primary_sdg'))
        method_score = calculate_method_match(user_method, match_row.get('primary_method'))
        career_score = calculate_career_fit(user_stage, match_row.get('career_stage'))
        
        # Calculate CCS Total (weighted sum)
        ccs_total = round((topic_score * 0.45) + (method_score * 0.40) + (career_score * 0.15))
        
        # Ensure scores are integers
        topic_score = int(topic_score)
        method_score = int(method_score)
        career_score = int(career_score)
        ccs_total = int(ccs_total)
        
        # Generate explanation
        explanation = generate_explanation(user_row, match_row, topic_score, method_score, career_score)
        
        # Create row
        demo_row = {
            'UserName': user_name,
            'UserDept': user_row['department'],
            'UserSDG': int(user_sdg) if pd.notna(user_sdg) else None,
            'UserMethod': user_method,
            'UserStage': user_stage,
            'MatchName': match_row['name'],
            'MatchDept': match_row['department'],
            'MatchSDG': int(match_row['primary_sdg']) if pd.notna(match_row['primary_sdg']) else None,
            'MatchMethod': match_row['primary_method'],
            'MatchStage': match_row['career_stage'],
            'Topic_Match': topic_score,
            'Method_Match': method_score,
            'Career_Fit': career_score,
            'CCS_Total': ccs_total,
            'Explanation': explanation
        }
        
        demo_data.append(demo_row)

# ============================================
# STEP 6: Create DataFrame and Adjust to 40 Rows
# ============================================
print("\n5. Creating final dataset...")

demo_df = pd.DataFrame(demo_data)

# Adjust to exactly 40 rows
if len(demo_df) > 40:
    # Keep top 40 by CCS_Total
    demo_df = demo_df.nlargest(40, 'CCS_Total').copy()
elif len(demo_df) < 40:
    # Add more matches if needed by generating additional matches
    print(f"  Warning: Only {len(demo_df)} matches generated. Adding more...")
    needed = 40 - len(demo_df)
    
    # Generate additional matches from top researchers
    for idx, user_row in top_researchers.iterrows():
        if needed <= 0:
            break
        
        user_name = user_row['name']
        user_sdg = user_row['primary_sdg']
        user_method = user_row['primary_method']
        user_stage = user_row['career_stage']
        
        # Find matches not already in demo_data
        existing_matches = set([(row['UserName'], row['MatchName']) for row in demo_data])
        potential_matches = all_researchers[
            (all_researchers['name'] != user_name) &
            (all_researchers['primary_sdg'].notna()) &
            (all_researchers['primary_method'].notna()) &
            (~all_researchers['name'].isin([row['MatchName'] for row in demo_data if row['UserName'] == user_name]))
        ].copy()
        
        if len(potential_matches) > 0:
            match_row = potential_matches.sample(1).iloc[0]
            
            # Calculate scores
            topic_score = int(calculate_topic_match(user_sdg, match_row.get('primary_sdg')))
            method_score = int(calculate_method_match(user_method, match_row.get('primary_method')))
            career_score = int(calculate_career_fit(user_stage, match_row.get('career_stage')))
            ccs_total = int(round((topic_score * 0.45) + (method_score * 0.40) + (career_score * 0.15)))
            
            explanation = generate_explanation(user_row, match_row, topic_score, method_score, career_score)
            
            demo_row = {
                'UserName': user_name,
                'UserDept': user_row['department'],
                'UserSDG': int(user_sdg) if pd.notna(user_sdg) else None,
                'UserMethod': user_method,
                'UserStage': user_stage,
                'MatchName': match_row['name'],
                'MatchDept': match_row['department'],
                'MatchSDG': int(match_row['primary_sdg']) if pd.notna(match_row['primary_sdg']) else None,
                'MatchMethod': match_row['primary_method'],
                'MatchStage': match_row['career_stage'],
                'Topic_Match': topic_score,
                'Method_Match': method_score,
                'Career_Fit': career_score,
                'CCS_Total': ccs_total,
                'Explanation': explanation
            }
            
            demo_data.append(demo_row)
            needed -= 1
    
    # Recreate DataFrame
    demo_df = pd.DataFrame(demo_data)

# Sort by CCS_Total descending
demo_df = demo_df.sort_values('CCS_Total', ascending=False).reset_index(drop=True)

# Ensure all scores are integers (no decimals)
for col in ['Topic_Match', 'Method_Match', 'Career_Fit', 'CCS_Total']:
    demo_df[col] = demo_df[col].astype(int)

# Ensure SDG columns are integers (convert NaN to 0, then back to None for display)
for col in ['UserSDG', 'MatchSDG']:
    # Convert to int, but keep None values
    demo_df[col] = demo_df[col].apply(lambda x: int(x) if pd.notna(x) else None)

print(f"✓ Generated {len(demo_df)} collaboration matches")

# ============================================
# STEP 7: Export to CSV
# ============================================
print("\n6. Exporting to CSV...")

demo_df.to_csv('CCS_Demo_Data.csv', index=False)
print(f"✓ Saved CCS_Demo_Data.csv")

# ============================================
# STEP 8: Summary Statistics
# ============================================
print("\n7. Summary Statistics:")
print(f"  - Total matches: {len(demo_df)}")
print(f"  - Unique users: {demo_df['UserName'].nunique()}")
print(f"  - Unique matches: {demo_df['MatchName'].nunique()}")
print(f"  - CCS_Total range: {demo_df['CCS_Total'].min()}-{demo_df['CCS_Total'].max()}")
print(f"  - Average CCS_Total: {demo_df['CCS_Total'].mean():.1f}")
print(f"  - Career stages:")
print(f"    - Pre-Tenure users: {len(demo_df[demo_df['UserStage'] == 'Pre-Tenure'])}")
print(f"    - Post-Tenure users: {len(demo_df[demo_df['UserStage'] == 'Post-Tenure'])}")
print(f"    - Senior users: {len(demo_df[demo_df['UserStage'] == 'Senior'])}")
print(f"  - SDGs represented: {demo_df['UserSDG'].nunique()}")
print(f"  - Methods represented: {demo_df['UserMethod'].nunique()}")

print("\n" + "="*70)
print("✓ CCS DEMO DATA GENERATION COMPLETE!")
print("="*70)
print("\nFirst 5 rows:")
print(demo_df.head(5)[['UserName', 'MatchName', 'CCS_Total', 'Topic_Match', 'Method_Match', 'Career_Fit']].to_string())
print("\n")

