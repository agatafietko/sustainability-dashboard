"""
Prepare Collaboration Hub Data for Power BI Visualization
This script transforms your existing matching data into Power BI-ready format
"""

import pandas as pd
import numpy as np
from datetime import datetime

print("="*60)
print("Collaboration Hub - Data Preparation for Power BI")
print("="*60)

# ============================================
# STEP 1: Load Existing Matching Data
# ============================================
print("\n1. Loading existing matching data...")

try:
    matches = pd.read_csv('faculty_matches.csv')
    print(f"✓ Loaded {len(matches)} matches from faculty_matches.csv")
except FileNotFoundError:
    print("⚠ faculty_matches.csv not found. Creating from scratch...")
    matches = pd.DataFrame()

try:
    network_data = pd.read_csv('network_graph_data.csv')
    print(f"✓ Loaded {len(network_data)} network connections")
except FileNotFoundError:
    print("⚠ network_graph_data.csv not found. Will create from matches.")
    network_data = pd.DataFrame()

# ============================================
# STEP 2: Create Power BI-Ready Matching Table
# ============================================
print("\n2. Creating Power BI-ready matching table...")

if len(matches) > 0:
    # Select and clean columns
    powerbi_matches = matches[[
        'Faculty_A_ID', 'Faculty_A_Name', 'Faculty_A_Dept', 
        'Faculty_A_Method', 'Faculty_A_Stage',
        'Faculty_B_ID', 'Faculty_B_Name', 'Faculty_B_Dept', 
        'Faculty_B_Method', 'Faculty_B_Stage',
        'Total_Score', 'Topic_Score', 'Method_Score', 'Stage_Score',
        'SDG', 'Topic_Reason', 'Method_Reason', 'Stage_Reason'
    ]].copy()
    
    # Create match quality categories
    def categorize_match(score):
        if pd.isna(score):
            return "Unknown"
        elif score >= 85:
            return "Excellent Match"
        elif score >= 70:
            return "Good Match"
        elif score >= 55:
            return "Moderate Match"
        else:
            return "Low Match"
    
    powerbi_matches['Match_Quality'] = powerbi_matches['Total_Score'].apply(categorize_match)
    
    # Create match pair identifier
    powerbi_matches['Match_Pair'] = (
        powerbi_matches['Faculty_A_Name'] + " ↔ " + powerbi_matches['Faculty_B_Name']
    )
    
    # Add complementarity indicator
    powerbi_matches['Is_Complementary'] = powerbi_matches['Method_Score'] >= 75
    
    # Save
    powerbi_matches.to_csv('Collab_Matches_For_PowerBI.csv', index=False)
    print(f"✓ Saved {len(powerbi_matches)} matches to Collab_Matches_For_PowerBI.csv")
    print(f"  - Excellent matches: {len(powerbi_matches[powerbi_matches['Match_Quality'] == 'Excellent Match'])}")
    print(f"  - Complementary methods: {powerbi_matches['Is_Complementary'].sum()}")
else:
    print("⚠ No matching data found. Please ensure faculty_matches.csv exists.")

# ============================================
# STEP 3: Create Researcher Profile Table
# ============================================
print("\n3. Creating researcher profiles...")

try:
    publications = pd.read_csv('for distribution case competition filtered_publications.csv', low_memory=False)
    print(f"✓ Loaded {len(publications)} publications")
    
    # Create researcher summary
    researcher_profiles = publications.groupby(['person_uuid', 'name', 'department', 'email']).agg({
        'article_uuid': 'count',  # Publication count
        'is_sustain': 'sum',  # Sustainable publications
        'publication_year': ['min', 'max'],  # Career span
        'top 1': lambda x: x.mode()[0] if len(x.mode()) > 0 else None,  # Primary SDG
    }).reset_index()
    
    researcher_profiles.columns = [
        'person_uuid', 'name', 'department', 'email',
        'total_publications', 'sustainable_count', 'first_publication', 'last_publication', 'primary_sdg'
    ]
    
    # Calculate career metrics
    current_year = datetime.now().year
    researcher_profiles['years_active'] = (
        researcher_profiles['last_publication'] - researcher_profiles['first_publication']
    )
    researcher_profiles['years_since_first'] = (
        current_year - researcher_profiles['first_publication']
    )
    
    # Infer career stage (simplified logic)
    def infer_career_stage(years):
        if pd.isna(years):
            return "Unknown"
        elif years > 15:
            return "Senior"
        elif years > 7:
            return "Post-Tenure"
        else:
            return "Pre-Tenure"
    
    researcher_profiles['career_stage'] = researcher_profiles['years_since_first'].apply(infer_career_stage)
    
    # Calculate sustainability rate
    researcher_profiles['sustainability_rate'] = (
        researcher_profiles['sustainable_count'] / researcher_profiles['total_publications'] * 100
    ).round(1)
    
    # Save
    researcher_profiles.to_csv('Researcher_Profiles_For_PowerBI.csv', index=False)
    print(f"✓ Saved {len(researcher_profiles)} researcher profiles")
    print(f"  - Departments: {researcher_profiles['department'].nunique()}")
    print(f"  - Total publications: {researcher_profiles['total_publications'].sum()}")
    
except FileNotFoundError:
    print("⚠ Publications CSV not found. Skipping researcher profiles.")
    researcher_profiles = pd.DataFrame()

# ============================================
# STEP 4: Create Method Complementarity Summary
# ============================================
print("\n4. Creating method complementarity summary...")

if len(matches) > 0:
    # Create method pair combinations
    method_pairs = []
    
    for _, row in matches.iterrows():
        method_pairs.append({
            'Method_A': row['Faculty_A_Method'],
            'Method_B': row['Faculty_B_Method'],
            'Total_Score': row['Total_Score'],
            'Method_Score': row['Method_Score'],
            'Is_Complementary': row['Method_Score'] >= 75
        })
    
    method_summary = pd.DataFrame(method_pairs)
    
    # Aggregate by method pair
    method_complementarity = method_summary.groupby(['Method_A', 'Method_B']).agg({
        'Total_Score': ['mean', 'count'],
        'Method_Score': 'mean',
        'Is_Complementary': 'sum'
    }).reset_index()
    
    method_complementarity.columns = [
        'Method_A', 'Method_B', 'Avg_Total_Score', 'Match_Count', 
        'Avg_Method_Score', 'Complementary_Count'
    ]
    
    # Calculate complementarity rate
    method_complementarity['Complementarity_Rate'] = (
        method_complementarity['Complementary_Count'] / method_complementarity['Match_Count'] * 100
    ).round(1)
    
    # Save
    method_complementarity.to_csv('Method_Complementarity_For_PowerBI.csv', index=False)
    print(f"✓ Saved method complementarity matrix")
    print(f"  - Method pairs: {len(method_complementarity)}")
    print(f"  - Highest complementarity: {method_complementarity['Avg_Method_Score'].max():.1f}")

# ============================================
# STEP 5: Create SDG Matching Summary
# ============================================
print("\n5. Creating SDG matching summary...")

if len(matches) > 0:
    sdg_summary = matches.groupby('SDG').agg({
        'Total_Score': ['mean', 'count'],
        'Topic_Score': 'mean',
        'Method_Score': 'mean',
        'Stage_Score': 'mean'
    }).reset_index()
    
    sdg_summary.columns = [
        'SDG', 'Avg_Total_Score', 'Match_Count',
        'Avg_Topic_Score', 'Avg_Method_Score', 'Avg_Stage_Score'
    ]
    
    # Load SDG names if available
    try:
        sdg_lookup = pd.read_csv('sdg_lookup.csv')
        sdg_summary = sdg_summary.merge(
            sdg_lookup[['SDG ID', 'SDG Name']],
            left_on='SDG',
            right_on='SDG ID',
            how='left'
        )
        sdg_summary = sdg_summary.drop('SDG ID', axis=1)
    except FileNotFoundError:
        print("  ⚠ sdg_lookup.csv not found. SDG names not added.")
    
    # Save
    sdg_summary.to_csv('SDG_Matching_Summary_For_PowerBI.csv', index=False)
    print(f"✓ Saved SDG matching summary")
    print(f"  - SDGs with matches: {sdg_summary['SDG'].nunique()}")

# ============================================
# STEP 6: Create Network Graph Data (Enhanced)
# ============================================
print("\n6. Creating enhanced network graph data...")

if len(matches) > 0:
    # Create network edges from matches
    network_edges = []
    
    for _, row in matches.iterrows():
        network_edges.append({
            'Source': row['Faculty_A_Name'],
            'Target': row['Faculty_B_Name'],
            'Score': row['Total_Score'],
            'Topic_Score': row['Topic_Score'],
            'Method_Score': row['Method_Score'],
            'Stage_Score': row['Stage_Score'],
            'Source_ID': row['Faculty_A_ID'],
            'Target_ID': row['Faculty_B_ID'],
            'Source_Dept': row['Faculty_A_Dept'],
            'Target_Dept': row['Faculty_B_Dept'],
            'Source_Method': row['Faculty_A_Method'],
            'Target_Method': row['Faculty_B_Method'],
            'SDG': row['SDG']
        })
    
    network_df = pd.DataFrame(network_edges)
    
    # Add edge categories
    network_df['Edge_Category'] = network_df['Score'].apply(categorize_match)
    
    # Save
    network_df.to_csv('Network_Graph_For_PowerBI.csv', index=False)
    print(f"✓ Saved network graph data")
    print(f"  - Edges: {len(network_df)}")
    print(f"  - Unique researchers: {len(set(network_df['Source'].tolist() + network_df['Target'].tolist()))}")

# ============================================
# STEP 7: Create Summary Statistics
# ============================================
print("\n7. Creating summary statistics...")

if len(matches) > 0:
    summary_stats = {
        'Total_Matches': len(matches),
        'Excellent_Matches': len(matches[matches['Total_Score'] >= 85]),
        'Good_Matches': len(matches[(matches['Total_Score'] >= 70) & (matches['Total_Score'] < 85)]),
        'Avg_Total_Score': matches['Total_Score'].mean(),
        'Avg_Topic_Score': matches['Topic_Score'].mean(),
        'Avg_Method_Score': matches['Method_Score'].mean(),
        'Avg_Stage_Score': matches['Stage_Score'].mean(),
        'Complementary_Matches': len(matches[matches['Method_Score'] >= 75]),
        'Unique_Researchers': len(set(matches['Faculty_A_Name'].tolist() + matches['Faculty_B_Name'].tolist())),
        'SDGs_Covered': matches['SDG'].nunique()
    }
    
    summary_df = pd.DataFrame([summary_stats])
    summary_df.to_csv('Summary_Stats_For_PowerBI.csv', index=False)
    print("✓ Saved summary statistics")
    print(f"  - Total matches: {summary_stats['Total_Matches']}")
    print(f"  - Excellent matches: {summary_stats['Excellent_Matches']}")
    print(f"  - Average score: {summary_stats['Avg_Total_Score']:.1f}")
    print(f"  - Complementary matches: {summary_stats['Complementary_Matches']}")

# ============================================
# COMPLETE
# ============================================
print("\n" + "="*60)
print("✓ DATA PREPARATION COMPLETE!")
print("="*60)
print("\nFiles created for Power BI:")
print("  1. Collab_Matches_For_PowerBI.csv - Main matching data")
print("  2. Researcher_Profiles_For_PowerBI.csv - Researcher info")
print("  3. Method_Complementarity_For_PowerBI.csv - Method matrix")
print("  4. SDG_Matching_Summary_For_PowerBI.csv - SDG analysis")
print("  5. Network_Graph_For_PowerBI.csv - Network visualization")
print("  6. Summary_Stats_For_PowerBI.csv - Key metrics")
print("\nNext steps:")
print("  1. Open Power BI Desktop")
print("  2. Import all CSV files")
print("  3. Create relationships between tables")
print("  4. Build visualizations (see COLLAB_HUB_MVP_GUIDE.md)")
print("="*60)



