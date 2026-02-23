"""
Build Collaboration Hub Matching Algorithm from Publications Data
This script implements the complete compatibility scoring system:
- Topic Match (50%): SDG alignment + keyword overlap
- Method Match (35%): Complementarity (different methods = higher)
- Career Stage (15%): Strategic fit
"""

import pandas as pd
import numpy as np
from datetime import datetime
import re
from collections import Counter
from itertools import combinations

print("="*70)
print("COLLABORATION HUB - Building Matching Algorithm from Publications")
print("="*70)

# ============================================
# STEP 1: Load and Clean Data
# ============================================
print("\n1. Loading publications data...")

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
# STEP 2: Extract Researcher Profiles
# ============================================
print("\n2. Extracting researcher profiles...")

def extract_keywords(keywords_str):
    """Extract keywords from semicolon-separated string"""
    if pd.isna(keywords_str):
        return []
    keywords = [k.strip() for k in str(keywords_str).split(';') if k.strip()]
    return keywords[:20]  # Top 20 keywords

def get_sdg_list(row):
    """Get list of SDGs for a publication"""
    sdgs = []
    for col in ['top 1', 'top 2', 'top 3']:
        if pd.notna(row.get(col)) and 1 <= row[col] <= 17:
            sdgs.append(int(row[col]))
    return list(set(sdgs))  # Remove duplicates

# Aggregate by researcher
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
    
    # Career stage (simplified)
    # Using 2025 as current year (update if needed)
    current_year = 2025  # datetime.now().year would be dynamic, but using 2025 explicitly
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
    
    # Infer research method from keywords and abstracts
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
    
    # Combine all text
    all_text = ' '.join([str(kw).lower() for kw in top_keywords])
    if 'abstract' in person_df.columns:
        abstracts = ' '.join([str(ab).lower() for ab in person_df['abstract'].dropna()])
        all_text += ' ' + abstracts[:5000]  # First 5000 chars
    
    # Score each method
    method_scores = {}
    for method, keywords in method_keywords.items():
        score = sum(1 for kw in keywords if kw in all_text)
        method_scores[method] = score
    
    # Assign primary method
    if method_scores:
        primary_method = max(method_scores, key=method_scores.get)
        if method_scores[primary_method] == 0:
            primary_method = "Mixed Methods"  # Default if no clear method
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
print(f"  - Departments: {researchers['department'].nunique()}")
print(f"  - Methods: {researchers['primary_method'].value_counts().to_dict()}")

# ============================================
# STEP 3: Calculate Compatibility Scores
# ============================================
print("\n3. Calculating compatibility scores...")

def calculate_topic_score(researcher_a, researcher_b):
    """
    Topic Match Score (0-100, weighted 50%)
    Based on SDG alignment and keyword overlap
    """
    # SDG Alignment (70% of topic score)
    sdg_a = set([int(s) for s in str(researcher_a['sdg_list']).split(',') if s.isdigit()])
    sdg_b = set([int(s) for s in str(researcher_b['sdg_list']).split(',') if s.isdigit()])
    
    if not sdg_a or not sdg_b:
        sdg_score = 0
    else:
        # Exact matches
        exact_matches = len(sdg_a & sdg_b)
        # Related SDGs (same cluster: 1-6 social, 7-12 economic, 13-17 environmental)
        related_score = 0
        for sdg1 in sdg_a:
            for sdg2 in sdg_b:
                if sdg1 != sdg2:
                    # Same cluster
                    cluster1 = (sdg1 - 1) // 6
                    cluster2 = (sdg2 - 1) // 6
                    if cluster1 == cluster2:
                        related_score += 0.3
        
        sdg_score = min(100, exact_matches * 30 + related_score * 10)
    
    # Keyword Overlap (30% of topic score)
    keywords_a = set(str(researcher_a['top_keywords']).split(';'))
    keywords_b = set(str(researcher_b['top_keywords']).split(';'))
    
    if not keywords_a or not keywords_b:
        keyword_score = 0
    else:
        intersection = keywords_a & keywords_b
        union = keywords_a | keywords_b
        if union:
            jaccard = len(intersection) / len(union)
            keyword_score = jaccard * 100
        else:
            keyword_score = 0
    
    # Combined topic score (SDG 70% + Keywords 30%)
    topic_score = (sdg_score * 0.7) + (keyword_score * 0.3)
    return min(100, topic_score)

def calculate_method_score(researcher_a, researcher_b):
    """
    Method Match Score (0-100, weighted 35%)
    REWARDS DIFFERENT METHODS (complementarity)
    """
    method_a = researcher_a['primary_method']
    method_b = researcher_b['primary_method']
    
    # Complementarity matrix
    complementary_pairs = {
        ('Theoretical', 'Empirical'): 100,
        ('Theoretical', 'Fieldwork'): 100,
        ('Theoretical', 'Experimental'): 90,
        ('Empirical', 'Theoretical'): 100,
        ('Empirical', 'Qualitative'): 85,
        ('Empirical', 'Fieldwork'): 90,
        ('Qualitative', 'Empirical'): 85,
        ('Qualitative', 'Experimental'): 80,
        ('Fieldwork', 'Theoretical'): 100,
        ('Fieldwork', 'Computational'): 85,
        ('Experimental', 'Theoretical'): 90,
        ('Experimental', 'Qualitative'): 80,
        ('Computational', 'Fieldwork'): 85,
        ('Computational', 'Qualitative'): 75,
    }
    
    # Check for perfect complementarity
    if (method_a, method_b) in complementary_pairs:
        return complementary_pairs[(method_a, method_b)]
    elif (method_b, method_a) in complementary_pairs:
        return complementary_pairs[(method_b, method_a)]
    
    # Same method = low score
    if method_a == method_b:
        if method_a == "Mixed Methods":
            return 50  # Mixed + Mixed = moderate
        else:
            return 25  # Same method = low complementarity
    
    # Different but not explicitly complementary = moderate
    return 50

def calculate_stage_score(researcher_a, researcher_b):
    """
    Career Stage Match Score (0-100, weighted 15%)
    Optimal: Pre-Tenure + Post-Tenure (mentorship)
    """
    stage_a = researcher_a['career_stage']
    stage_b = researcher_b['career_stage']
    
    # Optimal matches (mentorship opportunities)
    optimal_pairs = [
        ('Pre-Tenure', 'Post-Tenure'),
        ('Pre-Tenure', 'Senior'),
        ('Post-Tenure', 'Senior')
    ]
    
    if (stage_a, stage_b) in optimal_pairs or (stage_b, stage_a) in optimal_pairs:
        return 100
    
    # Good matches (peer collaboration)
    if stage_a == stage_b:
        if stage_a == 'Post-Tenure':
            return 75  # Post-tenure peers
        else:
            return 60  # Pre-tenure or Senior peers
    
    # Moderate matches
    return 50

# Calculate all pairwise matches
print("  Calculating pairwise compatibility...")
matches = []
researcher_list = researchers.to_dict('records')

# Limit to reasonable number of comparisons (top researchers by publication count)
top_researchers = researchers.nlargest(100, 'total_publications')
top_researcher_list = top_researchers.to_dict('records')

for i, researcher_a in enumerate(top_researcher_list):
    if i % 10 == 0:
        print(f"    Processing researcher {i+1}/{len(top_researcher_list)}...")
    
    for researcher_b in top_researcher_list[i+1:]:  # Avoid duplicates and self-matches
        # Calculate sub-scores
        topic_score = calculate_topic_score(researcher_a, researcher_b)
        method_score = calculate_method_score(researcher_a, researcher_b)
        stage_score = calculate_stage_score(researcher_a, researcher_b)
        
        # Weighted total score
        total_score = (topic_score * 0.50) + (method_score * 0.35) + (stage_score * 0.15)
        
        # Generate reasons
        topic_reason = f"SDG alignment: {researcher_a['primary_sdg']} & {researcher_b['primary_sdg']}"
        method_reason = f"{researcher_a['primary_method']} vs {researcher_b['primary_method']} ({'Complementary' if method_score >= 75 else 'Similar'})"
        stage_reason = f"{researcher_a['career_stage']} vs {researcher_b['career_stage']} ({'Mentorship opportunity' if stage_score == 100 else 'Peer collaboration'})"
        
        # Get shared SDG
        sdg_a_list = [int(s) for s in str(researcher_a['sdg_list']).split(',') if s.isdigit()]
        sdg_b_list = [int(s) for s in str(researcher_b['sdg_list']).split(',') if s.isdigit()]
        shared_sdg = list(set(sdg_a_list) & set(sdg_b_list))
        primary_sdg = shared_sdg[0] if shared_sdg else (researcher_a['primary_sdg'] or researcher_b['primary_sdg'] or 0)
        
        matches.append({
            'Faculty_A_ID': researcher_a['person_uuid'],
            'Faculty_A_Name': researcher_a['name'],
            'Faculty_A_Dept': researcher_a['department'],
            'Faculty_A_Method': researcher_a['primary_method'],
            'Faculty_A_Stage': researcher_a['career_stage'],
            'Faculty_B_ID': researcher_b['person_uuid'],
            'Faculty_B_Name': researcher_b['name'],
            'Faculty_B_Dept': researcher_b['department'],
            'Faculty_B_Method': researcher_b['primary_method'],
            'Faculty_B_Stage': researcher_b['career_stage'],
            'Total_Score': round(total_score, 1),
            'Topic_Score': round(topic_score, 1),
            'Method_Score': round(method_score, 1),
            'Stage_Score': round(stage_score, 1),
            'SDG': int(primary_sdg) if pd.notna(primary_sdg) else None,
            'Topic_Reason': topic_reason,
            'Method_Reason': method_reason,
            'Stage_Reason': stage_reason
        })

matches_df = pd.DataFrame(matches)
print(f"✓ Calculated {len(matches_df)} potential matches")

# ============================================
# STEP 4: Create Power BI-Ready Outputs
# ============================================
print("\n4. Creating Power BI-ready outputs...")

# Save matches
matches_df.to_csv('faculty_matches.csv', index=False)
print(f"✓ Saved faculty_matches.csv ({len(matches_df)} matches)")

# Create best matches (top 50)
best_matches = matches_df.nlargest(50, 'Total_Score')
best_matches.to_csv('best_faculty_match.csv', index=False)
print(f"✓ Saved best_faculty_match.csv (top 50 matches)")

# Create researcher profiles
researchers.to_csv('Researcher_Profiles_For_PowerBI.csv', index=False)
print(f"✓ Saved Researcher_Profiles_For_PowerBI.csv ({len(researchers)} profiles)")

# Create network graph data
network_data = []
for _, match in matches_df.iterrows():
    if match['Total_Score'] >= 70:  # Only high-quality matches
        network_data.append({
            'Source': match['Faculty_A_Name'],
            'Target': match['Faculty_B_Name'],
            'Score': match['Total_Score'],
            'Source_ID': match['Faculty_A_ID'],
            'Target_ID': match['Faculty_B_ID']
        })

network_df = pd.DataFrame(network_data)
network_df.to_csv('network_graph_data.csv', index=False)
print(f"✓ Saved network_graph_data.csv ({len(network_df)} network edges)")

# Create match quality summary
matches_df['Match_Quality'] = matches_df['Total_Score'].apply(
    lambda x: 'Excellent' if x >= 85 else ('Good' if x >= 70 else ('Moderate' if x >= 55 else 'Low'))
)
matches_df['Is_Complementary'] = matches_df['Method_Score'] >= 75

# Save enhanced matches for Power BI
powerbi_matches = matches_df[[
    'Faculty_A_ID', 'Faculty_A_Name', 'Faculty_A_Dept', 'Faculty_A_Method', 'Faculty_A_Stage',
    'Faculty_B_ID', 'Faculty_B_Name', 'Faculty_B_Dept', 'Faculty_B_Method', 'Faculty_B_Stage',
    'Total_Score', 'Topic_Score', 'Method_Score', 'Stage_Score',
    'SDG', 'Topic_Reason', 'Method_Reason', 'Stage_Reason',
    'Match_Quality', 'Is_Complementary'
]].copy()

powerbi_matches['Match_Pair'] = (
    powerbi_matches['Faculty_A_Name'] + " ↔ " + powerbi_matches['Faculty_B_Name']
)

powerbi_matches.to_csv('Collab_Matches_For_PowerBI.csv', index=False)
print(f"✓ Saved Collab_Matches_For_PowerBI.csv")

# ============================================
# STEP 5: Summary Statistics
# ============================================
print("\n5. Summary Statistics:")
print(f"  - Total researchers: {len(researchers)}")
print(f"  - Total matches calculated: {len(matches_df)}")
print(f"  - Excellent matches (≥85): {len(matches_df[matches_df['Total_Score'] >= 85])}")
print(f"  - Good matches (70-84): {len(matches_df[(matches_df['Total_Score'] >= 70) & (matches_df['Total_Score'] < 85)])}")
print(f"  - Complementary method matches: {matches_df['Is_Complementary'].sum()}")
print(f"  - Average compatibility score: {matches_df['Total_Score'].mean():.1f}")
print(f"  - Average topic score: {matches_df['Topic_Score'].mean():.1f}")
print(f"  - Average method score: {matches_df['Method_Score'].mean():.1f}")
print(f"  - Average stage score: {matches_df['Stage_Score'].mean():.1f}")

# Method complementarity validation
print("\n6. Method Complementarity Validation:")
theoretical_empirical = matches_df[
    ((matches_df['Faculty_A_Method'] == 'Theoretical') & (matches_df['Faculty_B_Method'] == 'Empirical')) |
    ((matches_df['Faculty_A_Method'] == 'Empirical') & (matches_df['Faculty_B_Method'] == 'Theoretical'))
]
if len(theoretical_empirical) > 0:
    print(f"  ✓ Theoretical + Empirical matches: {len(theoretical_empirical)}")
    print(f"    Average score: {theoretical_empirical['Method_Score'].mean():.1f} (should be ~100)")

same_method = matches_df[matches_df['Faculty_A_Method'] == matches_df['Faculty_B_Method']]
if len(same_method) > 0:
    print(f"  ✓ Same method matches: {len(same_method)}")
    print(f"    Average score: {same_method['Method_Score'].mean():.1f} (should be ~25)")

print("\n" + "="*70)
print("✓ COLLABORATION HUB MATCHING ALGORITHM COMPLETE!")
print("="*70)
print("\nFiles created:")
print("  1. faculty_matches.csv - All compatibility scores")
print("  2. best_faculty_match.csv - Top 50 matches")
print("  3. Researcher_Profiles_For_PowerBI.csv - Researcher profiles")
print("  4. network_graph_data.csv - Network visualization data")
print("  5. Collab_Matches_For_PowerBI.csv - Power BI ready format")
print("\nNext steps:")
print("  1. Review the matches in faculty_matches.csv")
print("  2. Import Collab_Matches_For_PowerBI.csv into Power BI")
print("  3. Build visualizations (see COLLAB_HUB_MVP_GUIDE.md)")
print("="*70)

