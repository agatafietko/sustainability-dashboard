"""
Data Preparation Script for Power BI Dashboard
This script cleans and transforms the publications CSV into Power BI-ready tables
"""

import pandas as pd
import re
from html import unescape
import numpy as np
from datetime import datetime

print("Loading main CSV file...")
# Load the main CSV
df = pd.read_csv('!!! for distribution case competition filtered_publications.csv', low_memory=False)

print(f"Original data: {len(df)} rows, {len(df.columns)} columns")

# ============================================
# 1. CLEAN PUBLICATIONS TABLE
# ============================================
print("\n1. Cleaning Publications table...")

# Remove duplicates based on article_uuid
df = df.drop_duplicates(subset=['article_uuid'], keep='first')
print(f"After removing duplicates: {len(df)} rows")

# Clean department names
df['department'] = df['department'].str.strip().str.title()

# Clean publication year - ensure it's numeric and reasonable
df['publication_year'] = pd.to_numeric(df['publication_year'], errors='coerce')
df = df[df['publication_year'].between(1900, 2026)]  # Filter reasonable years
print(f"After filtering valid years: {len(df)} rows")

# Clean is_sustain - convert to boolean
df['is_sustain'] = df['is_sustain'].astype(float).fillna(0).astype(bool)

# Clean journal flags - convert to boolean
for col in ['Financial Times', 'UT Dallas', 'General Business']:
    if col in df.columns:
        df[f'{col}_flag'] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(bool)

# Clean top 1, 2, 3 SDG columns - ensure they're valid SDG IDs (1-17)
for col in ['top 1', 'top 2', 'top 3']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        df.loc[~df[col].between(1, 17), col] = None

# Strip HTML from abstracts
def clean_html(text):
    if pd.isna(text):
        return ""
    text = str(text)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Decode HTML entities
    text = unescape(text)
    # Clean up whitespace
    text = ' '.join(text.split())
    return text

df['abstract_text'] = df['abstract'].apply(clean_html)

# Add is_recent flag (last 5 years)
current_year = datetime.now().year
df['is_recent'] = df['publication_year'] >= (current_year - 5)

# Add top journal flag
df['is_top_journal'] = df['Financial Times_flag'] | df['UT Dallas_flag']

# Select and rename columns for Publications table
publications_cols = [
    'article_uuid', 'title', 'name', 'department', 'email', 
    'publication_year', 'doi', 'abstract_text', 'journal_title', 'journal_issn',
    'is_sustain', 'is_recent', 'is_top_journal', 'source'
]

# Keep only columns that exist
publications_cols = [col for col in publications_cols if col in df.columns]
publications_df = df[publications_cols].copy()

# Save Publications table
publications_df.to_csv('Publications_cleaned.csv', index=False)
print(f"✓ Saved Publications table: {len(publications_df)} rows")

# ============================================
# 2. CREATE KEYWORDS TABLE
# ============================================
print("\n2. Creating Keywords table...")

keywords_data = []
for idx, row in df.iterrows():
    article_id = row['article_uuid']
    keywords_str = str(row.get('keywords', ''))
    
    if pd.notna(keywords_str) and keywords_str.strip():
        # Split by semicolon
        keywords_list = [k.strip() for k in keywords_str.split(';') if k.strip()]
        
        for keyword in keywords_list:
            keywords_data.append({
                'article_uuid': article_id,
                'keyword': keyword
            })

keywords_df = pd.DataFrame(keywords_data)
keywords_df = keywords_df.drop_duplicates(subset=['article_uuid', 'keyword'])
keywords_df.to_csv('Keywords_cleaned.csv', index=False)
print(f"✓ Saved Keywords table: {len(keywords_df)} rows, {keywords_df['keyword'].nunique()} unique keywords")

# ============================================
# 3. CREATE SDG MAPPINGS TABLE
# ============================================
print("\n3. Creating SDG Mappings table...")

sdg_data = []
for idx, row in df.iterrows():
    article_id = row['article_uuid']
    
    # Only include if is_sustain is True
    if row.get('is_sustain', False):
        for sdg_col in ['top 1', 'top 2', 'top 3']:
            sdg_id = row.get(sdg_col)
            if pd.notna(sdg_id) and 1 <= sdg_id <= 17:
                sdg_data.append({
                    'article_uuid': article_id,
                    'SDG ID': int(sdg_id)
                })

sdg_mappings_df = pd.DataFrame(sdg_data)
sdg_mappings_df = sdg_mappings_df.drop_duplicates(subset=['article_uuid', 'SDG ID'])
sdg_mappings_df.to_csv('SDG_Mappings_cleaned.csv', index=False)
print(f"✓ Saved SDG Mappings table: {len(sdg_mappings_df)} rows")

# ============================================
# 4. CREATE SUMMARY STATISTICS
# ============================================
print("\n4. Generating summary statistics...")

summary = {
    'Total Publications': len(publications_df),
    'Sustainable Publications': publications_df['is_sustain'].sum(),
    'Sustainable %': f"{(publications_df['is_sustain'].sum() / len(publications_df) * 100):.1f}%",
    'Unique Departments': publications_df['department'].nunique(),
    'Year Range': f"{int(publications_df['publication_year'].min())} - {int(publications_df['publication_year'].max())}",
    'Recent Publications (5 years)': publications_df['is_recent'].sum(),
    'Top Journal Publications': publications_df['is_top_journal'].sum() if 'is_top_journal' in publications_df.columns else 0,
    'Unique SDGs Covered': sdg_mappings_df['SDG ID'].nunique() if len(sdg_mappings_df) > 0 else 0,
    'Total Keywords': len(keywords_df),
    'Unique Keywords': keywords_df['keyword'].nunique()
}

print("\n" + "="*50)
print("DATA SUMMARY")
print("="*50)
for key, value in summary.items():
    print(f"{key:30}: {value}")

print("\n" + "="*50)
print("TOP 10 DEPARTMENTS BY SUSTAINABLE PUBLICATIONS")
print("="*50)
dept_stats = publications_df[publications_df['is_sustain']].groupby('department').size().sort_values(ascending=False).head(10)
for dept, count in dept_stats.items():
    print(f"{dept:40}: {count}")

print("\n" + "="*50)
print("SDG DISTRIBUTION")
print("="*50)
sdg_dist = sdg_mappings_df['SDG ID'].value_counts().sort_index()
for sdg_id, count in sdg_dist.items():
    print(f"SDG {int(sdg_id):2d}: {count:4d} publications")

print("\n" + "="*50)
print("✓ All data files created successfully!")
print("="*50)
print("\nFiles created:")
print("  1. Publications_cleaned.csv")
print("  2. Keywords_cleaned.csv")
print("  3. SDG_Mappings_cleaned.csv")
print("  4. sdg_lookup.csv (already exists)")
print("\nReady to import into Power BI!")





