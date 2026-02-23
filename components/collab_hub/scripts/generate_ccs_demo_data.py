"""
Generate CCS (Collaboration Compatibility Score) Demo Dataset
Creates realistic faculty collaboration matches for Power BI presentation
"""

import pandas as pd
import numpy as np
import random
from collections import Counter

print("="*70)
print("CCS DEMO DATA GENERATOR")
print("="*70)

# ============================================
# STEP 1: Load Researcher Profiles
# ============================================
print("\n1. Loading researcher profiles...")
df = pd.read_csv('Researcher_Profiles_For_PowerBI.csv')
print(f"✓ Loaded {len(df)} researcher profiles")

# ============================================
# STEP 2: Filter and Select Top Researchers
# ============================================
print("\n2. Filtering researchers...")

# Filter criteria
filtered = df[
    (df['total_publications'] >= 5) & 
    (df['primary_sdg'].notna()) & 
    (df['primary_sdg'] != '') &
    (df['primary_sdg'] != 0) &
    (df['career_stage'].notna())
].copy()

print(f"✓ Found {len(filtered)} researchers with >=5 publications and valid SDG")

# Select diverse mix of researchers by career stage
# Get top researchers from each career stage (prioritize variety)
pre_tenure = filtered[filtered['career_stage'] == 'Pre-Tenure'].nlargest(6, 'total_publications').copy()
post_tenure = filtered[filtered['career_stage'] == 'Post-Tenure'].nlargest(6, 'total_publications').copy()
senior = filtered[filtered['career_stage'] == 'Senior'].nlargest(3, 'total_publications').copy()

# Combine to get 15 researchers with variety
top_researchers = pd.concat([pre_tenure, post_tenure, senior], ignore_index=True).copy()

# If we don't have enough from each stage, fill with top overall (but prioritize Pre-Tenure)
if len(top_researchers) < 15:
    remaining_needed = 15 - len(top_researchers)
    # Try to get more Pre-Tenure first
    more_pre_tenure = filtered[
        (filtered['career_stage'] == 'Pre-Tenure') & 
        (~filtered['name'].isin(top_researchers['name']))
    ].nlargest(min(remaining_needed, 3), 'total_publications')
    
    if len(more_pre_tenure) > 0:
        top_researchers = pd.concat([top_researchers, more_pre_tenure], ignore_index=True).copy()
        remaining_needed = 15 - len(top_researchers)
    
    # Fill rest with top overall
    if remaining_needed > 0:
        remaining = filtered[~filtered['name'].isin(top_researchers['name'])].nlargest(remaining_needed, 'total_publications')
        top_researchers = pd.concat([top_researchers, remaining], ignore_index=True).copy()

print(f"✓ Selected {len(top_researchers)} researchers with career stage variety")
print(f"  - Pre-Tenure: {len(top_researchers[top_researchers['career_stage'] == 'Pre-Tenure'])}")
print(f"  - Post-Tenure: {len(top_researchers[top_researchers['career_stage'] == 'Post-Tenure'])}")
print(f"  - Senior: {len(top_researchers[top_researchers['career_stage'] == 'Senior'])}")
print(f"  Publication range: {top_researchers['total_publications'].min()}-{top_researchers['total_publications'].max()}")

# ============================================
# STEP 3: Prepare All Researchers for Matching
# ============================================
print("\n3. Preparing matching pool...")

# All researchers (excluding the top 15) for matching
all_researchers = df[df['name'].isin(top_researchers['name']) == False].copy()
print(f"✓ Prepared {len(all_researchers)} researchers for matching")

# ============================================
# STEP 4: Scoring Functions
# ============================================

def calculate_topic_match(user_sdg, match_sdg):
    """Calculate Topic Match Score (70-95)"""
    if pd.isna(user_sdg) or pd.isna(match_sdg):
        return random.randint(70, 80)
    
    user_sdg = float(user_sdg)
    match_sdg = float(match_sdg)
    
    # Exact match = highest score
    if user_sdg == match_sdg:
        return random.randint(90, 95)
    
    # Related SDGs (same cluster)
    # Cluster 1: SDGs 1-6 (Social)
    # Cluster 2: SDGs 7-12 (Economic)
    # Cluster 3: SDGs 13-17 (Environmental)
    user_cluster = int((user_sdg - 1) // 6)
    match_cluster = int((match_sdg - 1) // 6)
    
    if user_cluster == match_cluster:
        return random.randint(85, 90)
    
    # Different clusters
    return random.randint(70, 80)

def calculate_method_match(user_method, match_method):
    """Calculate Method Match Score (70-95)"""
    if pd.isna(user_method) or pd.isna(match_method):
        return random.randint(70, 80)
    
    # Define quantitative vs qualitative methods
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
    """Calculate Career Fit Score (70-92)"""
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
    """Generate explanation string"""
    # Get top keywords (first 2)
    top_keywords = str(match_row.get('top_keywords', '')).split(';')[:2]
    keywords_str = ' and '.join([kw.strip() for kw in top_keywords if kw.strip()])
    
    # Method description
    if method_score >= 85:
        method_desc = f"Complementary methods ({user_row.get('primary_method', 'Unknown')} + {match_row.get('primary_method', 'Unknown')}) create strong research synergy."
    elif method_score >= 75:
        method_desc = f"Similar methodological approaches ({user_row.get('primary_method', 'Unknown')} + {match_row.get('primary_method', 'Unknown')}) enable collaborative research."
    else:
        method_desc = f"Methodological alignment ({user_row.get('primary_method', 'Unknown')} + {match_row.get('primary_method', 'Unknown')}) supports joint research."
    
    # Career pairing description
    user_stage = user_row.get('career_stage', 'Unknown')
    match_stage = match_row.get('career_stage', 'Unknown')
    
    if career_score >= 85:
        if user_stage == 'Pre-Tenure' and match_stage in ['Post-Tenure', 'Senior']:
            career_desc = f"Excellent mentorship opportunity: {match_stage} researcher can guide {user_stage} researcher."
        else:
            career_desc = f"Strong mentorship pairing: {user_stage} and {match_stage} researchers."
    elif user_stage == match_stage:
        career_desc = f"Peer collaboration: Both researchers at {user_stage} stage can collaborate as equals."
    else:
        career_desc = f"Career stage pairing: {user_stage} and {match_stage} researchers."
    
    # Combine
    if keywords_str:
        explanation = f"Expertise in {keywords_str}. {method_desc} {career_desc}"
    else:
        explanation = f"{method_desc} {career_desc}"
    
    return explanation

# ============================================
# STEP 5: Generate Matches
# ============================================
print("\n4. Generating collaboration matches...")

demo_data = []
possible_sdgs = [7, 8, 9, 12, 13]  # For varying User_SDG
possible_methods = ['Theoretical', 'Empirical', 'Qualitative', 'Fieldwork', 'Computational', 'Experimental', 'Mixed Methods']

for idx, user_row in top_researchers.iterrows():
    user_name = user_row['name']
    
    # Determine User_SDG (use primary_sdg OR randomly vary)
    if random.random() < 0.7:  # 70% use actual primary_sdg
        user_sdg = user_row['primary_sdg']
    else:  # 30% vary
        user_sdg = random.choice(possible_sdgs)
    
    # Determine User_Method (use primary_method OR randomly vary)
    if random.random() < 0.6:  # 60% use actual primary_method
        user_method = user_row['primary_method']
    else:  # 40% vary
        user_method = random.choice(possible_methods)
    
    # User_Stage always uses actual career_stage
    user_stage = user_row['career_stage']
    
    # Find potential matches (different researchers)
    # Filter to researchers with valid data
    potential_matches = all_researchers[
        (all_researchers['name'] != user_name) &
        (all_researchers['primary_sdg'].notna()) &
        (all_researchers['primary_method'].notna())
    ].copy()
    
    if len(potential_matches) == 0:
        # If no matches in all_researchers, use other top researchers
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
        
        # Calculate CCS Total
        ccs_total = round((topic_score * 0.45) + (method_score * 0.40) + (career_score * 0.15))
        
        # Generate explanation
        explanation = generate_explanation(user_row, match_row, topic_score, method_score, career_score)
        
        # Create row
        demo_row = {
            'User_Name': user_name,
            'User_Dept': user_row['department'],
            'User_SDG': int(user_sdg) if pd.notna(user_sdg) else None,
            'User_Method': user_method,
            'User_Stage': user_stage,
            'Match_Name': match_row['name'],
            'Match_Dept': match_row['department'],
            'Match_SDG': int(match_row['primary_sdg']) if pd.notna(match_row['primary_sdg']) else None,
            'Match_Method': match_row['primary_method'],
            'Match_Stage': match_row['career_stage'],
            'Topic_Match': topic_score,
            'Method_Match': method_score,
            'Career_Fit': career_score,
            'CCS_Total': ccs_total,
            'Explanation': explanation
        }
        
        demo_data.append(demo_row)

# ============================================
# STEP 6: Create DataFrame and Sort
# ============================================
print("\n5. Creating final dataset...")

demo_df = pd.DataFrame(demo_data)
print(f"✓ Generated {len(demo_df)} collaboration matches")

# Sort by CCS_Total descending
demo_df = demo_df.sort_values('CCS_Total', ascending=False).reset_index(drop=True)

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
print(f"  - Unique users: {demo_df['User_Name'].nunique()}")
print(f"  - Unique matches: {demo_df['Match_Name'].nunique()}")
print(f"  - Average CCS_Total: {demo_df['CCS_Total'].mean():.1f}")
print(f"  - CCS_Total range: {demo_df['CCS_Total'].min()}-{demo_df['CCS_Total'].max()}")
print(f"  - Average Topic_Match: {demo_df['Topic_Match'].mean():.1f}")
print(f"  - Average Method_Match: {demo_df['Method_Match'].mean():.1f}")
print(f"  - Average Career_Fit: {demo_df['Career_Fit'].mean():.1f}")

print("\n" + "="*70)
print("✓ CCS DEMO DATA GENERATION COMPLETE!")
print("="*70)
print("\nFirst 10 rows:")
print(demo_df.head(10).to_string())
print("\n")

