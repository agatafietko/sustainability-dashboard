"""
Add 5 exceptional matches (CCS_Total 90-95) to CCS_Demo_Data.csv
"""

import pandas as pd
import random

print("="*70)
print("ADDING EXCEPTIONAL MATCHES (CCS_Total 90-95)")
print("="*70)

# Load existing data
print("\n1. Loading existing CCS demo data...")
existing_df = pd.read_csv('CCS_Demo_Data.csv')
print(f"✓ Loaded {len(existing_df)} existing matches")

# Load researcher profiles for real data
print("\n2. Loading researcher profiles...")
profiles_df = pd.read_csv('Researcher_Profiles_For_PowerBI.csv')
print(f"✓ Loaded {len(profiles_df)} researcher profiles")

# Filter to researchers with valid data
valid_researchers = profiles_df[
    (profiles_df['primary_sdg'].notna()) &
    (profiles_df['primary_sdg'] != '') &
    (profiles_df['primary_method'].notna()) &
    (profiles_df['career_stage'].notna())
].copy()

print(f"✓ Found {len(valid_researchers)} researchers with valid data")

# Function to generate explanation
def generate_explanation(user_row, match_row, topic_score, method_score, career_score):
    """Generate explanation string"""
    top_keywords = str(match_row.get('top_keywords', '')).split(';')[:2]
    keywords_str = ' and '.join([kw.strip() for kw in top_keywords if kw.strip()])
    
    user_method = user_row.get('primary_method', 'Unknown')
    match_method = match_row.get('primary_method', 'Unknown')
    
    if method_score >= 90:
        method_desc = f"Highly complementary methods ({user_method} + {match_method}) create exceptional research synergy."
    elif method_score >= 85:
        method_desc = f"Complementary methods ({user_method} + {match_method}) create strong research synergy."
    else:
        method_desc = f"Methodological alignment ({user_method} + {match_method}) supports joint research."
    
    user_stage = user_row.get('career_stage', 'Unknown')
    match_stage = match_row.get('career_stage', 'Unknown')
    
    if career_score >= 88:
        if user_stage == 'Pre-Tenure' and match_stage in ['Post-Tenure', 'Senior']:
            career_desc = f"Exceptional mentorship opportunity: {match_stage} researcher can provide expert guidance to {user_stage} researcher."
        else:
            career_desc = f"Optimal mentorship pairing: {user_stage} and {match_stage} researchers create ideal collaboration dynamic."
    elif career_score >= 85:
        career_desc = f"Strong mentorship pairing: {user_stage} and {match_stage} researchers."
    else:
        career_desc = f"Career stage pairing: {user_stage} and {match_stage} researchers."
    
    if keywords_str:
        explanation = f"Expertise in {keywords_str}. {method_desc} {career_desc}"
    else:
        explanation = f"{method_desc} {career_desc}"
    
    return explanation

# Generate 5 exceptional matches
print("\n3. Generating 5 exceptional matches...")

exceptional_matches = []

# Strategy: Create matches with:
# - Exact SDG matches (Topic_Match: 92-95)
# - Highly complementary methods (Method_Match: 90-95)
# - Mentorship opportunities (Career_Fit: 88-92)

# Get researchers with different career stages for mentorship
pre_tenure = valid_researchers[valid_researchers['career_stage'] == 'Pre-Tenure'].copy()
post_tenure = valid_researchers[valid_researchers['career_stage'] == 'Post-Tenure'].copy()
senior = valid_researchers[valid_researchers['career_stage'] == 'Senior'].copy()

# Define complementary method pairs
complementary_pairs = [
    ('Theoretical', 'Empirical'),
    ('Theoretical', 'Fieldwork'),
    ('Empirical', 'Qualitative'),
    ('Fieldwork', 'Computational'),
    ('Theoretical', 'Experimental')
]

# Generate 5 matches
for i in range(5):
    # Select user (Post-Tenure or Senior for mentorship)
    if len(post_tenure) > 0 and random.random() < 0.6:
        user_row = post_tenure.sample(1).iloc[0]
    elif len(senior) > 0:
        user_row = senior.sample(1).iloc[0]
    else:
        user_row = valid_researchers.sample(1).iloc[0]
    
    user_sdg = float(user_row['primary_sdg'])
    
    # Find match with same SDG (for high Topic_Match)
    same_sdg_matches = valid_researchers[
        (valid_researchers['name'] != user_row['name']) &
        (valid_researchers['primary_sdg'].notna()) &
        (pd.to_numeric(valid_researchers['primary_sdg'], errors='coerce') == user_sdg)
    ].copy()
    
    # If no exact SDG match, find related SDG (same cluster)
    if len(same_sdg_matches) == 0:
        user_cluster = int((user_sdg - 1) // 6)
        same_sdg_matches = valid_researchers[
            (valid_researchers['name'] != user_row['name']) &
            (valid_researchers['primary_sdg'].notna())
        ].copy()
        same_sdg_matches['sdg_cluster'] = (pd.to_numeric(same_sdg_matches['primary_sdg'], errors='coerce') - 1) // 6
        same_sdg_matches = same_sdg_matches[same_sdg_matches['sdg_cluster'] == user_cluster].copy()
    
    # Filter for complementary methods
    user_method = user_row['primary_method']
    potential_matches = []
    
    for _, match_candidate in same_sdg_matches.iterrows():
        match_method = match_candidate['primary_method']
        # Check if methods are complementary
        if (user_method, match_method) in complementary_pairs or (match_method, user_method) in complementary_pairs:
            potential_matches.append(match_candidate)
        elif user_method != match_method and user_method not in ['Mixed Methods'] and match_method not in ['Mixed Methods']:
            # Different methods (still good)
            potential_matches.append(match_candidate)
    
    if len(potential_matches) == 0:
        potential_matches = list(same_sdg_matches.iterrows())
    
    if len(potential_matches) == 0:
        # Fallback: any valid researcher
        potential_matches = list(valid_researchers[valid_researchers['name'] != user_row['name']].iterrows())
    
    # Select match (prefer Pre-Tenure for mentorship)
    match_row = None
    for candidate in potential_matches:
        if isinstance(candidate, tuple):
            candidate = candidate[1]
        if candidate['career_stage'] == 'Pre-Tenure' and user_row['career_stage'] in ['Post-Tenure', 'Senior']:
            match_row = candidate
            break
    
    if match_row is None:
        match_row = potential_matches[0]
        if isinstance(match_row, tuple):
            match_row = match_row[1]
    
    # Calculate high scores for exceptional match
    # Topic_Match: 92-95 (exact SDG match)
    if pd.to_numeric(user_row['primary_sdg'], errors='coerce') == pd.to_numeric(match_row['primary_sdg'], errors='coerce'):
        topic_score = random.randint(92, 95)
    else:
        topic_score = random.randint(88, 92)
    
    # Method_Match: 90-95 (highly complementary)
    user_method = user_row['primary_method']
    match_method = match_row['primary_method']
    if (user_method, match_method) in complementary_pairs or (match_method, user_method) in complementary_pairs:
        method_score = random.randint(90, 95)
    elif user_method != match_method:
        method_score = random.randint(88, 92)
    else:
        method_score = random.randint(85, 90)
    
    # Career_Fit: 88-92 (mentorship)
    user_stage = user_row['career_stage']
    match_stage = match_row['career_stage']
    if (user_stage == 'Post-Tenure' and match_stage == 'Pre-Tenure') or \
       (user_stage == 'Senior' and match_stage == 'Pre-Tenure') or \
       (user_stage == 'Senior' and match_stage == 'Post-Tenure'):
        career_score = random.randint(88, 92)
    elif user_stage == match_stage and user_stage == 'Post-Tenure':
        career_score = random.randint(85, 88)
    else:
        career_score = random.randint(82, 88)
    
    # Calculate CCS_Total
    ccs_total = round((topic_score * 0.45) + (method_score * 0.40) + (career_score * 0.15))
    
    # Ensure CCS_Total is between 90-95
    if ccs_total < 90:
        # Adjust scores to reach 90+
        topic_score = max(topic_score, 92)
        method_score = max(method_score, 90)
        career_score = max(career_score, 88)
        ccs_total = round((topic_score * 0.45) + (method_score * 0.40) + (career_score * 0.15))
    
    if ccs_total > 95:
        # Slightly reduce to stay within 90-95
        topic_score = min(topic_score, 94)
        method_score = min(method_score, 94)
        ccs_total = round((topic_score * 0.45) + (method_score * 0.40) + (career_score * 0.15))
    
    # Generate explanation
    explanation = generate_explanation(user_row, match_row, topic_score, method_score, career_score)
    
    # Create row
    exceptional_row = {
        'User_Name': user_row['name'],
        'User_Dept': user_row['department'],
        'User_SDG': int(user_sdg),
        'User_Method': user_method,
        'User_Stage': user_stage,
        'Match_Name': match_row['name'],
        'Match_Dept': match_row['department'],
        'Match_SDG': int(match_row['primary_sdg']) if pd.notna(match_row['primary_sdg']) else None,
        'Match_Method': match_method,
        'Match_Stage': match_stage,
        'Topic_Match': topic_score,
        'Method_Match': method_score,
        'Career_Fit': career_score,
        'CCS_Total': ccs_total,
        'Explanation': explanation
    }
    
    exceptional_matches.append(exceptional_row)
    print(f"  Match {i+1}: {user_row['name']} ↔ {match_row['name']} (CCS: {ccs_total})")

# Combine with existing data
print("\n4. Combining with existing data...")
exceptional_df = pd.DataFrame(exceptional_matches)
combined_df = pd.concat([existing_df, exceptional_df], ignore_index=True)

# Sort by CCS_Total descending
combined_df = combined_df.sort_values('CCS_Total', ascending=False).reset_index(drop=True)

# Save
print("\n5. Saving updated CSV...")
combined_df.to_csv('CCS_Demo_Data.csv', index=False)
print(f"✓ Saved CCS_Demo_Data.csv with {len(combined_df)} total matches")

# Summary
print("\n6. Summary:")
print(f"  - Total matches: {len(combined_df)}")
print(f"  - Exceptional matches (90-95): {len(combined_df[combined_df['CCS_Total'] >= 90])}")
print(f"  - CCS_Total range: {combined_df['CCS_Total'].min()}-{combined_df['CCS_Total'].max()}")

print("\n" + "="*70)
print("✓ EXCEPTIONAL MATCHES ADDED!")
print("="*70)
print("\nTop 10 matches (by CCS_Total):")
print(combined_df.head(10)[['User_Name', 'Match_Name', 'CCS_Total', 'Topic_Match', 'Method_Match', 'Career_Fit']].to_string())
print("\n")



