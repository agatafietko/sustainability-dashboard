# Data Transformation Guide: From Publications CSV to Collaboration Matches

> **Step-by-step explanation of how the original publications CSV is transformed into researcher profiles and collaboration matches**

---

## 📥 **Input: Original Publications CSV**

### **File**: `for distribution case competition filtered_publications.csv`

### **Structure** (one row per publication):
- `person_uuid` - Unique researcher identifier
- `name` - Researcher name
- `department` - Department affiliation
- `email` - Contact email
- `publication_year` - Year of publication
- `keywords` - Semicolon-separated keywords
- `abstract` or `abstract_text` - Publication abstract
- `top 1`, `top 2`, `top 3` - SDG labels (1-17)
- `is_sustain` - Boolean flag for sustainability focus

### **Example Row**:
```
person_uuid: abc-123
name: "Smith, John"
department: "Business Administration"
publication_year: 2020
keywords: "machine learning; AI; sustainability; data analysis"
abstract: "This paper explores..."
top 1: 9
top 2: 13
is_sustain: TRUE
```

---

## 🔄 **Transformation Step 1: Data Cleaning**

### **What Happens**:
1. **Validate publication years**: Keep only years between 1900-2026
2. **Clean SDG columns**: Ensure `top 1`, `top 2`, `top 3` are between 1-17
3. **Convert boolean**: `is_sustain` converted to True/False

### **Why**:
- **Data quality**: Invalid years indicate data errors
- **SDG validation**: SDGs must be 1-17 (UN SDG framework)
- **Consistency**: Boolean conversion ensures consistent data types

### **Output**: Cleaned publications dataframe

---

## 🔄 **Transformation Step 2: Researcher Profile Construction**

### **What Happens**: Aggregate all publications for each unique `person_uuid`

### **For Each Researcher**:

#### **2.1 Basic Metrics** (Direct aggregation)
```python
total_publications = count of all rows for this person_uuid
sustainable_publications = count where is_sustain = TRUE
first_publication_year = MIN(publication_year)
last_publication_year = MAX(publication_year)
years_active = last_year - first_year
```

#### **2.2 Career Stage** (Inferred)
```python
years_since_first = 2025 - first_publication_year

if years_since_first > 15:
    career_stage = "Senior"
elif years_since_first > 7:
    career_stage = "Post-Tenure"
else:
    career_stage = "Pre-Tenure"
```

**Business logic**: Years since first publication is a proxy for career stage.

#### **2.3 Top Keywords** (Aggregated)
```python
# Collect all keywords from all publications
all_keywords = []
for each publication:
    keywords_list = split(keywords, ';')
    all_keywords.extend(keywords_list)

# Count frequency
keyword_counts = Counter(all_keywords)

# Keep top 15
top_keywords = most_common(15)
```

**Example**:
- Publication 1: "machine learning; AI"
- Publication 2: "AI; deep learning; neural networks"
- Publication 3: "machine learning; data analysis"
- **Result**: top_keywords = ["machine learning", "AI", "deep learning", "neural networks", "data analysis"]

#### **2.4 Primary SDG** (Aggregated)
```python
# Collect all SDG labels
all_sdgs = []
for each publication:
    if top_1 is not null: all_sdgs.append(top_1)
    if top_2 is not null: all_sdgs.append(top_2)
    if top_3 is not null: all_sdgs.append(top_3)

# Count frequency
sdg_counts = Counter(all_sdgs)

# Most common = primary_sdg
primary_sdg = most_common(1)
sdg_list = most_common(3)  # Top 3 SDGs
```

**Example**:
- Publication 1: top_1=9, top_2=13
- Publication 2: top_1=9
- Publication 3: top_1=7, top_2=9
- **Result**: primary_sdg = 9, sdg_list = [9, 13, 7]

#### **2.5 Primary Method** (Inferred from text)
```python
# Combine all text
all_text = join(top_keywords) + first_5000_chars(abstracts)

# Define method keywords
method_keywords = {
    'Theoretical': ['model', 'optimization', 'game theory', ...],
    'Empirical': ['regression', 'statistical', 'data', ...],
    # ... etc
}

# Count matches for each method
for each method:
    score = count how many method_keywords appear in all_text

# Highest score = primary_method
primary_method = method with highest score
```

**Example**:
- Keywords: "regression", "statistical analysis", "data"
- Abstract: "We use econometric methods to analyze..."
- **Result**: primary_method = "Empirical" (highest keyword matches)

### **Output**: `Researcher_Profiles_For_PowerBI.csv`
- One row per researcher
- Contains: name, department, total_publications, career_stage, primary_method, primary_sdg, top_keywords, etc.

---

## 🔄 **Transformation Step 3: Compatibility Score Calculation**

### **What Happens**: For each pair of researchers, calculate compatibility

### **For Each Pair (Researcher A, Researcher B)**:

#### **3.1 Topic Score Calculation**

**SDG Alignment (70% of topic score)**:
```python
sdg_a = set of SDGs from Researcher A's sdg_list
sdg_b = set of SDGs from Researcher B's sdg_list

exact_matches = count of SDGs in both sets
# Each exact match = 30 points

related_score = 0
for each sdg in sdg_a:
    for each sdg in sdg_b:
        if same_cluster(sdg_a, sdg_b):
            related_score += 0.3

sdg_score = min(100, exact_matches × 30 + related_score × 10)
```

**Keyword Overlap (30% of topic score)**:
```python
keywords_a = set of keywords from Researcher A
keywords_b = set of keywords from Researcher B

intersection = keywords_a & keywords_b  # Common keywords
union = keywords_a | keywords_b          # All unique keywords
jaccard = len(intersection) / len(union)

keyword_score = jaccard × 100
```

**Combined Topic Score**:
```python
topic_score = (sdg_score × 0.7) + (keyword_score × 0.3)
```

#### **3.2 Method Score Calculation**

```python
method_a = Researcher A's primary_method
method_b = Researcher B's primary_method

# Check complementarity matrix
if (method_a, method_b) in complementary_pairs:
    method_score = 100  # Perfect complementarity
elif method_a == method_b:
    method_score = 25   # Same method = low
else:
    method_score = 50   # Different but not complementary
```

#### **3.3 Career Score Calculation**

```python
stage_a = Researcher A's career_stage
stage_b = Researcher B's career_stage

if (stage_a, stage_b) in mentorship_pairs:
    career_score = 100  # Mentorship opportunity
elif stage_a == stage_b:
    career_score = 60-75  # Peer collaboration
else:
    career_score = 50    # Other
```

#### **3.4 Total Compatibility Score**

```python
ccs_total = (topic_score × 0.50) + (method_score × 0.35) + (career_score × 0.15)
```

### **Output**: `Collab_Matches_For_PowerBI.csv`
- One row per researcher pair
- Contains: Researcher A info, Researcher B info, all scores, explanations

---

## 🔄 **Transformation Step 4: Demo Data Generation**

### **What Happens**: Create demo dataset for Power BI presentation

### **Process** (`generate_ccs_demo_data.py`):

1. **Load researcher profiles** from `Researcher_Profiles_For_PowerBI.csv`

2. **Select 15 diverse researchers**:
   - Mix of career stages (Pre-Tenure, Post-Tenure, Senior)
   - Researchers with valid data (SDG, method, stage)

3. **For each selected researcher**:
   - **Determine user inputs** (with variation):
     - 70% use actual `primary_sdg`
     - 30% randomly vary SDG (to show diverse scenarios)
     - 60% use actual `primary_method`
     - 40% randomly vary method
     - Always use actual `career_stage`
   
   - **Find 2-3 matches**:
     - Filter to researchers with valid data
     - Select 2-3 potential matches
   
   - **Calculate scores** using same formula as main pipeline
   
   - **Generate explanation** with natural language

4. **Add small randomized variation** to scores:
   - Topic scores: ±2-3 points
   - Method scores: ±2-3 points
   - Career scores: ±2-3 points
   - **Why**: Shows realistic score distribution

### **Output**: `CCS_Demo_Data.csv`
- Demo matches for Power BI dashboard
- Uses same scoring formula as real data
- Includes controlled variation for presentation clarity

---

## 📊 **Data Flow Summary**

```
Original Publications CSV
    ↓ [Clean & Validate]
    ↓ [Aggregate by Researcher]
Researcher_Profiles_For_PowerBI.csv
    ↓ [Calculate Pairwise Compatibility]
Collab_Matches_For_PowerBI.csv
    ↓ [Generate Demo Data - Optional]
CCS_Demo_Data.csv
```

---

## 🔍 **Key Transformations Explained**

### **1. Publication-Level → Researcher-Level**

**Before**: One row per publication
**After**: One row per researcher

**Why**: Need researcher profiles for matching, not individual publications

### **2. Multiple Publications → Single Profile**

**Before**: Researcher has 10 publications with different SDGs
**After**: Researcher has `primary_sdg = 9` (most common)

**Why**: Need to identify dominant research focus

### **3. Keywords → Method Classification**

**Before**: Keywords: "regression", "statistical", "data"
**After**: `primary_method = "Empirical"`

**Why**: Need method classification to enable complementarity matching

### **4. Years → Career Stage**

**Before**: `first_publication_year = 2010`
**After**: `career_stage = "Post-Tenure"`

**Why**: Need career stage to identify mentorship opportunities

### **5. Researcher Profiles → Compatibility Scores**

**Before**: Two separate researcher profiles
**After**: One compatibility score with sub-scores

**Why**: Need quantified compatibility to rank and recommend matches

---

## ✅ **Validation**

### **What We Verify**:

1. **Profile accuracy**: Researcher profiles reflect their actual publications
2. **Score ranges**: All scores are 0-100
3. **Weight sum**: 50% + 35% + 15% = 100%
4. **Complementarity**: Theoretical + Empirical scores higher than Theoretical + Theoretical
5. **Mentorship**: Pre-Tenure + Senior scores higher than Pre-Tenure + Pre-Tenure

### **How We Verify**:

- Check method complementarity matrix works correctly
- Verify score distributions are reasonable
- Ensure explanations are generated for all matches
- Validate demo data uses same formula as real data

---

**This guide shows exactly how the original CSV becomes actionable collaboration recommendations.**
