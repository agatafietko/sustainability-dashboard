# How New CSVs Were Generated from Original University Data
## Complete Step-by-Step Transformation Process

---

## 🎯 **THE TRANSFORMATION PROCESS**

```
Original CSV (2,154 rows)
    ↓
[STEP 1: Extract Researcher Profiles]
    ↓
Researcher Profiles (144 researchers)
    ↓
[STEP 2: Calculate Pairwise Compatibility]
    ↓
Faculty Matches (4,952 matches)
    ↓
[STEP 3: Create Power BI Files]
    ↓
5 New CSV Files Ready for Visualization
```

---

## 📊 **STEP 1: UNDERSTANDING THE ORIGINAL DATA**

### **Original File:** `for distribution case competition filtered_publications.csv`

**Structure:** Publication-level data (one row = one publication)

**Key Columns:**
- `person_uuid` - Unique researcher ID
- `name`, `email`, `department` - Researcher info
- `publication_year` - When published
- `keywords` - Research keywords (semicolon-separated)
- `abstract` - Publication abstract
- `top 1`, `top 2`, `top 3` - SDG alignments (1-17)
- `is_sustain` - Whether publication is sustainability-related

**Example:**
```
Row 1: person_uuid=ABC, name="Dr. Smith", publication_year=2010, keywords="Machine Learning;AI"
Row 2: person_uuid=ABC, name="Dr. Smith", publication_year=2012, keywords="Deep Learning;Neural Networks"
Row 3: person_uuid=XYZ, name="Dr. Jones", publication_year=2015, keywords="Statistics;Regression"
```

**Problem:** One researcher appears in multiple rows (one per publication). We need to aggregate this into one row per researcher.

---

## 🔄 **STEP 2: EXTRACTING RESEARCHER PROFILES**

### **Process:** Group all publications by `person_uuid` and aggregate

### **Code Logic (from `build_collab_hub_from_scratch.py`):**

```python
# For each unique researcher (person_uuid):
for person_uuid in df['person_uuid'].unique():
    person_df = df[df['person_uuid'] == person_uuid].copy()
    
    # 1. BASIC INFO (direct copy from first row)
    name = person_df['name'].iloc[0]
    email = person_df['email'].iloc[0]
    department = person_df['department'].iloc[0]
    
    # 2. PUBLICATION METRICS (calculated)
    total_pubs = len(person_df)  # Count rows
    sustainable_pubs = person_df['is_sustain'].sum()  # Sum of 1s
    first_year = person_df['publication_year'].min()  # Earliest year
    last_year = person_df['publication_year'].max()  # Latest year
    years_active = last_year - first_year
    
    # 3. CAREER STAGE (inferred from years)
    current_year = 2025
    years_since_first = current_year - first_year
    if years_since_first > 15:
        career_stage = "Senior"
    elif years_since_first > 7:
        career_stage = "Post-Tenure"
    else:
        career_stage = "Pre-Tenure"
    
    # 4. KEYWORDS (aggregated from all publications)
    all_keywords = []
    for row in person_df:
        keywords = row['keywords'].split(';')  # Split semicolon-separated
        all_keywords.extend(keywords)
    # Count frequency, take top 10
    top_keywords = most_common_keywords(all_keywords, 10)
    
    # 5. SDGs (aggregated from all publications)
    all_sdgs = []
    for row in person_df:
        # Collect top 1, top 2, top 3 SDGs
        if row['top 1']: all_sdgs.append(row['top 1'])
        if row['top 2']: all_sdgs.append(row['top 2'])
        if row['top 3']: all_sdgs.append(row['top 3'])
    # Most common SDG = primary_sdg
    primary_sdg = most_common(all_sdgs)
    
    # 6. RESEARCH METHOD (inferred from keywords + abstracts)
    # Combine all keywords and abstracts
    all_text = combine_keywords_and_abstracts(person_df)
    
    # Define method keywords
    method_keywords = {
        'Theoretical': ['theoretical', 'model', 'optimization', 'game theory'],
        'Empirical': ['empirical', 'statistical', 'regression', 'data'],
        'Qualitative': ['qualitative', 'case study', 'interview'],
        'Fieldwork': ['field', 'survey', 'experiment'],
        'Experimental': ['experiment', 'randomized', 'trial'],
        'Computational': ['computational', 'simulation', 'machine learning', 'AI']
    }
    
    # Count occurrences of each method's keywords
    method_scores = {}
    for method, keywords in method_keywords.items():
        score = count_keyword_matches(all_text, keywords)
        method_scores[method] = score
    
    # Assign method with highest score
    primary_method = max(method_scores, key=method_scores.get)
```

### **Result:** One row per researcher with aggregated data

**Example Transformation:**

**Before (3 rows for Dr. Smith):**
```
Row 1: person_uuid=ABC, year=2010, keywords="ML;AI", top 1=9
Row 2: person_uuid=ABC, year=2012, keywords="DL;NN", top 1=9
Row 3: person_uuid=ABC, year=2015, keywords="AI;Robotics", top 1=9
```

**After (1 row for Dr. Smith):**
```
person_uuid=ABC
name="Dr. Smith"
total_publications=3
first_publication_year=2010
last_publication_year=2015
years_active=5
years_since_first=15
career_stage="Senior"
primary_method="Computational" (inferred from "ML", "AI", "DL", "NN")
primary_sdg=9
top_keywords="Machine Learning;AI;Deep Learning;Neural Networks;Robotics"
```

---

## 🔄 **STEP 3: CALCULATING COMPATIBILITY SCORES**

### **Process:** Compare every pair of researchers (A vs B)

### **Code Logic:**

```python
# For each pair of researchers:
for researcher_a in researchers:
    for researcher_b in researchers (after researcher_a):
        
        # 1. TOPIC SCORE (50% weight)
        topic_score = calculate_topic_score(researcher_a, researcher_b)
        # - SDG Alignment (70% of topic score)
        #   - Exact SDG matches = high score
        #   - Related SDGs (same cluster) = medium score
        # - Keyword Overlap (30% of topic score)
        #   - Jaccard similarity of top keywords
        
        # 2. METHOD SCORE (35% weight)
        method_score = calculate_method_score(researcher_a, researcher_b)
        # - REWARDS DIFFERENT METHODS (complementarity)
        # - Theoretical + Empirical = 100 points
        # - Theoretical + Theoretical = 25 points (low!)
        # - Different but not complementary = 50 points
        
        # 3. STAGE SCORE (15% weight)
        stage_score = calculate_stage_score(researcher_a, researcher_b)
        # - Pre-Tenure + Post-Tenure = 100 (mentorship)
        # - Same stage = 60-75 (peer collaboration)
        # - Other combinations = 50
        
        # 4. TOTAL SCORE (weighted sum)
        total_score = (topic_score * 0.50) + 
                     (method_score * 0.35) + 
                     (stage_score * 0.15)
```

### **Detailed Scoring Functions:**

#### **1. Topic Score Calculation:**

```python
def calculate_topic_score(researcher_a, researcher_b):
    # SDG Alignment (70% of topic score)
    sdg_a = [9, 12, 17]  # Researcher A's SDGs
    sdg_b = [9, 13, 17]  # Researcher B's SDGs
    
    exact_matches = intersection(sdg_a, sdg_b)  # [9, 17] = 2 matches
    exact_score = exact_matches * 30  # 2 * 30 = 60 points
    
    # Related SDGs (same cluster)
    # Cluster 1: SDGs 1-6 (Social)
    # Cluster 2: SDGs 7-12 (Economic)
    # Cluster 3: SDGs 13-17 (Environmental)
    related_score = count_related_sdgs(sdg_a, sdg_b) * 10
    
    sdg_score = min(100, exact_score + related_score)
    
    # Keyword Overlap (30% of topic score)
    keywords_a = ["ML", "AI", "Data"]
    keywords_b = ["ML", "Statistics", "Analysis"]
    
    intersection = ["ML"]  # 1 common keyword
    union = ["ML", "AI", "Data", "Statistics", "Analysis"]  # 5 total unique
    
    jaccard = len(intersection) / len(union)  # 1/5 = 0.2
    keyword_score = jaccard * 100  # 20 points
    
    # Combined topic score
    topic_score = (sdg_score * 0.7) + (keyword_score * 0.3)
    # Example: (80 * 0.7) + (20 * 0.3) = 56 + 6 = 62 points
    
    return topic_score
```

#### **2. Method Score Calculation:**

```python
def calculate_method_score(researcher_a, researcher_b):
    method_a = "Theoretical"
    method_b = "Empirical"
    
    # Complementarity matrix (defined in code)
    complementary_pairs = {
        ('Theoretical', 'Empirical'): 100,  # Perfect complement!
        ('Theoretical', 'Fieldwork'): 100,
        ('Empirical', 'Qualitative'): 85,
        # ... more pairs
    }
    
    # Check if pair is complementary
    if (method_a, method_b) in complementary_pairs:
        return 100  # High score!
    
    # Same method = low score
    if method_a == method_b:
        return 25  # Low complementarity
    
    # Different but not complementary
    return 50  # Moderate
```

#### **3. Stage Score Calculation:**

```python
def calculate_stage_score(researcher_a, researcher_b):
    stage_a = "Pre-Tenure"
    stage_b = "Post-Tenure"
    
    # Optimal mentorship pairs
    optimal_pairs = [
        ('Pre-Tenure', 'Post-Tenure'),  # ✅ Mentorship!
        ('Pre-Tenure', 'Senior'),
        ('Post-Tenure', 'Senior')
    ]
    
    if (stage_a, stage_b) in optimal_pairs:
        return 100  # Perfect mentorship opportunity
    
    # Same stage = peer collaboration
    if stage_a == stage_b:
        if stage_a == 'Post-Tenure':
            return 75  # Good peer collaboration
        else:
            return 60
    
    return 50  # Moderate
```

### **Result:** One row per researcher pair with compatibility scores

**Example Match:**
```
Faculty_A_Name: "Dr. Smith"
Faculty_A_Method: "Theoretical"
Faculty_A_Stage: "Senior"
Faculty_B_Name: "Dr. Jones"
Faculty_B_Method: "Empirical"
Faculty_B_Stage: "Post-Tenure"
Topic_Score: 62.0
Method_Score: 100.0  (Theoretical + Empirical = perfect!)
Stage_Score: 100.0   (Senior + Post-Tenure = mentorship!)
Total_Score: 81.0    (62*0.5 + 100*0.35 + 100*0.15)
```

---

## 📁 **STEP 4: CREATING OUTPUT FILES**

### **File 1: `faculty_matches.csv`**
**Purpose:** All pairwise compatibility scores

**Generation:**
```python
matches_df.to_csv('faculty_matches.csv', index=False)
```

**Contains:** All 4,952 matches with full details

---

### **File 2: `best_faculty_match.csv`**
**Purpose:** Top 50 matches only

**Generation:**
```python
best_matches = matches_df.nlargest(50, 'Total_Score')
best_matches.to_csv('best_faculty_match.csv', index=False)
```

**Contains:** Top 50 matches sorted by `Total_Score` (descending)

---

### **File 3: `Researcher_Profiles_For_PowerBI.csv`**
**Purpose:** One row per researcher with all profile data

**Generation:**
```python
researchers.to_csv('Researcher_Profiles_For_PowerBI.csv', index=False)
```

**Contains:** 144 researcher profiles with:
- Basic info (name, email, department)
- Publication metrics
- Career stage (inferred)
- Primary method (inferred)
- SDG alignments
- Top keywords

---

### **File 4: `network_graph_data.csv`**
**Purpose:** Data for network visualization (high-quality matches only)

**Generation:**
```python
network_data = []
for match in matches_df:
    if match['Total_Score'] >= 70:  # Only high-quality matches
        network_data.append({
            'Source': match['Faculty_A_Name'],
            'Target': match['Faculty_B_Name'],
            'Score': match['Total_Score']
        })
network_df.to_csv('network_graph_data.csv', index=False)
```

**Contains:** Only matches with `Total_Score >= 70` (high-quality connections)

---

### **File 5: `Collab_Matches_For_PowerBI.csv`**
**Purpose:** Enhanced matches with quality flags for Power BI

**Generation:**
```python
# Add quality flags
matches_df['Match_Quality'] = matches_df['Total_Score'].apply(
    lambda x: 'Excellent' if x >= 85 else 
              ('Good' if x >= 70 else 
               ('Moderate' if x >= 55 else 'Low'))
)

matches_df['Is_Complementary'] = matches_df['Method_Score'] >= 75

# Add match pair column
matches_df['Match_Pair'] = (
    matches_df['Faculty_A_Name'] + " ↔ " + matches_df['Faculty_B_Name']
)

matches_df.to_csv('Collab_Matches_For_PowerBI.csv', index=False)
```

**Contains:** All matches with:
- `Match_Quality` (Excellent/Good/Moderate/Low)
- `Is_Complementary` (True/False)
- `Match_Pair` (formatted string like "Dr. Smith ↔ Dr. Jones")

---

## 🔍 **KEY INFERENCES EXPLAINED**

### **1. Career Stage Inference**

**Source Data:**
- `publication_year` (from original CSV)

**Logic:**
```python
current_year = 2025
first_publication_year = min(all_publication_years)  # e.g., 2010
years_since_first = 2025 - 2010 = 15 years

if years_since_first > 15:
    career_stage = "Senior"        # 15+ years = Senior
elif years_since_first > 7:
    career_stage = "Post-Tenure"   # 7-15 years = Post-Tenure
else:
    career_stage = "Pre-Tenure"    # <7 years = Pre-Tenure
```

**Why this works:**
- Academic career progression typically follows this timeline
- Pre-tenure: 0-7 years (assistant professor)
- Post-tenure: 7-15 years (associate professor)
- Senior: 15+ years (full professor)

---

### **2. Research Method Inference**

**Source Data:**
- `keywords` column (semicolon-separated)
- `abstract` column (text)

**Logic:**
```python
# Combine all keywords and abstracts for researcher
all_text = "machine learning AI deep learning neural network..."

# Define method keywords
method_keywords = {
    'Computational': ['machine learning', 'AI', 'deep learning', 'neural network'],
    'Theoretical': ['theoretical', 'model', 'optimization', 'game theory'],
    'Empirical': ['empirical', 'statistical', 'regression', 'data'],
    # ... more methods
}

# Count keyword matches
computational_score = count_occurrences(all_text, method_keywords['Computational'])
# Result: 4 matches (machine learning, AI, deep learning, neural network)

theoretical_score = count_occurrences(all_text, method_keywords['Theoretical'])
# Result: 0 matches

# Assign method with highest score
primary_method = "Computational"  # Highest score (4)
```

**Why this works:**
- Researchers' keywords and abstracts contain method indicators
- "Machine learning", "AI" → Computational
- "Regression", "statistical" → Empirical
- "Model", "optimization" → Theoretical

---

### **3. SDG Aggregation**

**Source Data:**
- `top 1`, `top 2`, `top 3` columns (SDG numbers 1-17)

**Logic:**
```python
# Collect all SDGs from all publications
all_sdgs = []
for publication in researcher_publications:
    if publication['top 1']: all_sdgs.append(publication['top 1'])
    if publication['top 2']: all_sdgs.append(publication['top 2'])
    if publication['top 3']: all_sdgs.append(publication['top 3'])

# Example: [9, 12, 9, 17, 9, 12, 9]
# Count frequency
sdg_counts = {9: 4, 12: 2, 17: 1}

# Most common = primary SDG
primary_sdg = 9  # Appears 4 times

# Top 3 = SDG list
sdg_list = [9, 12, 17]  # Sorted by frequency
```

**Why this works:**
- Researchers often work on multiple SDGs
- Most common SDG = their primary focus area
- Top 3 SDGs = their research scope

---

## 📊 **DATA FLOW DIAGRAM**

```
┌─────────────────────────────────────────────────────────┐
│  Original CSV: for distribution case competition        │
│  filtered_publications.csv                              │
│  (2,154 rows, publication-level)                        │
└─────────────────────────────────────────────────────────┘
                        ↓
        ┌───────────────────────────────┐
        │  Group by person_uuid         │
        │  Aggregate publications       │
        └───────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  Researcher Profiles (144 researchers)                  │
│  - Basic info (name, email, dept)                       │
│  - Publication metrics (count, years)                   │
│  - Career stage (INFERRED from years)                   │
│  - Primary method (INFERRED from keywords/abstracts)    │
│  - SDGs (AGGREGATED from top 1/2/3)                     │
│  - Top keywords (AGGREGATED from all publications)      │
└─────────────────────────────────────────────────────────┘
                        ↓
        ┌───────────────────────────────┐
        │  Calculate pairwise           │
        │  compatibility scores         │
        │  (A vs B for all pairs)       │
        └───────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  Faculty Matches (4,952 matches)                        │
│  - Topic Score (50%): SDG + Keywords                   │
│  - Method Score (35%): Complementarity                  │
│  - Stage Score (15%): Mentorship fit                    │
│  - Total Score (weighted sum)                           │
└─────────────────────────────────────────────────────────┘
                        ↓
        ┌───────────────────────────────┐
        │  Create derivative files      │
        │  for Power BI                 │
        └───────────────────────────────┘
                        ↓
    ┌──────────┬──────────┬──────────┬──────────┬──────────┐
    │ faculty_ │  best_   │Researcher│ network_ │ Collab_  │
    │ matches  │ faculty_ │ Profiles │ graph_   │ Matches  │
    │ .csv     │ match.csv│ .csv     │ data.csv │ .csv     │
    └──────────┴──────────┴──────────┴──────────┴──────────┘
```

---

## ✅ **VALIDATION: HOW WE KNOW IT WORKS**

### **1. Method Complementarity Check:**

```python
# Theoretical + Empirical should = high score
theoretical_empirical = matches_df[
    (matches_df['Faculty_A_Method'] == 'Theoretical') & 
    (matches_df['Faculty_B_Method'] == 'Empirical')
]
# Average Method_Score should be ~100 ✅

# Same method should = low score
same_method = matches_df[
    matches_df['Faculty_A_Method'] == matches_df['Faculty_B_Method']
]
# Average Method_Score should be ~25 ✅
```

### **2. Career Stage Check:**

```python
# Pre-Tenure + Post-Tenure should = high stage score
mentorship_pairs = matches_df[
    ((matches_df['Faculty_A_Stage'] == 'Pre-Tenure') & 
     (matches_df['Faculty_B_Stage'] == 'Post-Tenure'))
]
# Average Stage_Score should be ~100 ✅
```

---

## 🎯 **SUMMARY**

### **What Was Created:**
1. **Researcher Profiles** - Aggregated from publication-level data
2. **Compatibility Scores** - Calculated using weighted algorithm
3. **5 Output Files** - Ready for Power BI/Tableau visualization

### **What Was Inferred (Not in Original Data):**
1. **Career Stage** - From publication years
2. **Research Method** - From keywords and abstracts
3. **SDG Focus** - From aggregated SDG columns

### **What Was Calculated:**
1. **Topic Score** - SDG alignment + keyword overlap
2. **Method Score** - Complementarity (different = better)
3. **Stage Score** - Mentorship fit
4. **Total Score** - Weighted combination (50% + 35% + 15%)

### **Key Innovation:**
**Method Complementarity** - The algorithm REWARDS different methods (Theoretical + Empirical = high score), which is the core innovation of the Collaboration Hub!

---

**All of this is generated by running:**
```bash
python3 build_collab_hub_from_scratch.py
```

**The script reads:** `for distribution case competition filtered_publications.csv`  
**The script creates:** 5 new CSV files ready for visualization!



