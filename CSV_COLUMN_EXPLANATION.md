# CSV Column Explanation & Data Generation Logic
## Complete Breakdown of Original Data & Generated Files

---

## 📊 **ORIGINAL CSV: `for distribution case competition filtered_publications.csv`**

### **Column Breakdown (24 columns total):**

| Column Name | Type | What It Represents | Example |
|------------|------|-------------------|---------|
| **`person_uuid`** | ID | Unique identifier for each researcher | `6d42042d-5967-4653-9013-d6eed37ca2c9` |
| **`name`** | Text | Researcher's full name | `"Abdel-Khalik, A. Rashad"` |
| **`email`** | Text | Researcher's email address | `rashad@illinois.edu` |
| **`department`** | Text | Academic department | `Accountancy` |
| **`active`** | Boolean | Whether researcher is currently active | `True` |
| **`article_uuid`** | ID | Unique identifier for each publication | `38792cbd-5cff-4cc8-afdf-f5148896e760` |
| **`title`** | Text | Publication title | `"CEO risk preference and investing in R and D"` |
| **`publication_year`** | Number | Year publication was published | `2014` |
| **`doi`** | URL | Digital Object Identifier (link to paper) | `https://doi.org/10.1111/abac.12029` |
| **`abstract`** | Text | Publication abstract (HTML formatted) | `<p>This study aims at...</p>` |
| **`journal_title`** | Text | Journal name | `Abacus` |
| **`journal_issn`** | Text | Journal ISSN number | `0001-3072` |
| **`active.1`** | Boolean | Duplicate of active column | `True` |
| **`is_sustain`** | Number | Whether publication aligns with SDGs (0 or 1) | `0.0` (not sustainable) or `1.0` (sustainable) |
| **`top 1`** | Number | Primary SDG alignment (1-17) | `3.0` (SDG 3: Good Health) |
| **`top 2`** | Number | Secondary SDG alignment (1-17) | `9.0` (SDG 9: Industry) |
| **`top 3`** | Number | Tertiary SDG alignment (1-17) | `17.0` (SDG 17: Partnerships) |
| **`keywords`** | Text | Research keywords (semicolon-separated) | `Cash Flow;Large Banks;Volatility;Hedging;...` |
| **`keyword_ranks`** | Text | Keyword importance scores (semicolon-separated) | `4.0;3.0;2.5;2.5;...` |
| **`pinecone_complete`** | Number | Vector database completion flag | `1.0` |
| **`source`** | Text | Data source | `Illinois Experts` |
| **`Financial Times`** | Number | FT journal ranking flag (0 or 1) | `0.0` or `1.0` |
| **`UT Dallas`** | Number | UT Dallas journal ranking flag (0 or 1) | `0.0` or `1.0` |
| **`General Business`** | Number | General business journal flag (0 or 1) | `0.0` or `1.0` |

**Key Insight:** This is a **publication-level** dataset. Each row = one publication by one researcher. A researcher with 10 publications appears in 10 rows.

---

## 🔄 **HOW NEW CSVs ARE GENERATED**

### **Process Overview:**

```
Original CSV (2,154 rows)
    ↓
STEP 1: Group by person_uuid (aggregate publications per researcher)
    ↓
Researcher Profiles (100-150 researchers)
    ↓
STEP 2: Calculate pairwise compatibility scores
    ↓
Faculty Matches (4,952 matches)
    ↓
STEP 3: Create derivative files for Power BI
```

---

## 📁 **NEW CSV 1: `Researcher_Profiles_For_PowerBI.csv`**

### **Purpose:** One row per researcher with aggregated profile data

### **Column Generation Logic:**

| Column | Source | Logic |
|--------|--------|-------|
| **`person_uuid`** | Original CSV `person_uuid` | ✅ Direct copy (first occurrence per researcher) |
| **`name`** | Original CSV `name` | ✅ Direct copy (first occurrence per researcher) |
| **`email`** | Original CSV `email` | ✅ Direct copy (first occurrence per researcher) |
| **`department`** | Original CSV `department` | ✅ Direct copy (first occurrence per researcher) |
| **`total_publications`** | **CALCULATED** | Count of rows per `person_uuid` |
| **`sustainable_publications`** | Original CSV `is_sustain` | Sum of `is_sustain` values per researcher |
| **`first_publication_year`** | Original CSV `publication_year` | Minimum year per researcher |
| **`last_publication_year`** | Original CSV `publication_year` | Maximum year per researcher |
| **`years_active`** | **CALCULATED** | `last_publication_year - first_publication_year` |
| **`years_since_first`** | **CALCULATED** | `2024 - first_publication_year` (current year - first) |
| **`career_stage`** | **INFERRED** | Based on `years_since_first`:<br>- <7 years = "Pre-Tenure"<br>- 7-15 years = "Post-Tenure"<br>- >15 years = "Senior" |
| **`primary_method`** | **INFERRED** | Scans `keywords` + `abstract` columns:<br>- Counts method-related keywords<br>- Assigns method with highest count<br>- Categories: Theoretical, Empirical, Qualitative, Fieldwork, Experimental, Computational, Mixed Methods |
| **`primary_sdg`** | Original CSV `top 1`, `top 2`, `top 3` | Most common SDG across all publications per researcher |
| **`sdg_list`** | Original CSV `top 1`, `top 2`, `top 3` | Top 3 most common SDGs (comma-separated) |
| **`top_keywords`** | Original CSV `keywords` | Top 10 most frequent keywords across all publications (semicolon-separated) |

### **Example Transformation:**

**Original CSV (multiple rows for one researcher):**
```
person_uuid: 6d42042d-5967-4653-9013-d6eed37ca2c9
Row 1: publication_year=2011, keywords="Cash Flow;Large Banks;..."
Row 2: publication_year=2014, keywords="Volatility;Hedging;..."
Row 3: publication_year=2015, keywords="Risk Aversion;Fair Value;..."
```

**Researcher Profile (one row):**
```
person_uuid: 6d42042d-5967-4653-9013-d6eed37ca2c9
total_publications: 9
first_publication_year: 2011
last_publication_year: 2019
years_since_first: 14
career_stage: Post-Tenure
primary_method: Empirical (inferred from keywords)
top_keywords: "Cash Flow;Large Banks;Volatility;Hedging;..."
```

---

## 📁 **NEW CSV 2: `faculty_matches.csv`**

### **Purpose:** All pairwise compatibility scores between researchers

### **Column Generation Logic:**

| Column | Source | Logic |
|--------|--------|-------|
| **`Faculty_A_ID`** | Researcher Profile `person_uuid` | ✅ Direct copy (Researcher A) |
| **`Faculty_A_Name`** | Researcher Profile `name` | ✅ Direct copy (Researcher A) |
| **`Faculty_A_Dept`** | Researcher Profile `department` | ✅ Direct copy (Researcher A) |
| **`Faculty_A_Method`** | Researcher Profile `primary_method` | ✅ Direct copy (Researcher A) |
| **`Faculty_A_Stage`** | Researcher Profile `career_stage` | ✅ Direct copy (Researcher A) |
| **`Faculty_B_ID`** | Researcher Profile `person_uuid` | ✅ Direct copy (Researcher B) |
| **`Faculty_B_Name`** | Researcher Profile `name` | ✅ Direct copy (Researcher B) |
| **`Faculty_B_Dept`** | Researcher Profile `department` | ✅ Direct copy (Researcher B) |
| **`Faculty_B_Method`** | Researcher Profile `primary_method` | ✅ Direct copy (Researcher B) |
| **`Faculty_B_Stage`** | Researcher Profile `career_stage` | ✅ Direct copy (Researcher B) |
| **`Total_Score`** | **CALCULATED** | `(Topic_Score × 0.50) + (Method_Score × 0.35) + (Stage_Score × 0.15)` |
| **`Topic_Score`** | **CALCULATED** | See Topic Score Logic below |
| **`Method_Score`** | **CALCULATED** | See Method Score Logic below |
| **`Stage_Score`** | **CALCULATED** | See Stage Score Logic below |
| **`SDG`** | Researcher Profile `sdg_list` | Shared SDG between A and B (or primary SDG if no match) |
| **`Topic_Reason`** | **GENERATED** | Text explanation: `"SDG alignment: {A_SDG} & {B_SDG}"` |
| **`Method_Reason`** | **GENERATED** | Text explanation: `"{A_Method} vs {B_Method} (Complementary/Similar)"` |
| **`Stage_Reason`** | **GENERATED** | Text explanation: `"{A_Stage} vs {B_Stage} (Mentorship/Peer collaboration)"` |

---

### **Topic Score Logic (0-100, weighted 50%):**

**Formula:** `Topic_Score = (SDG_Score × 0.70) + (Keyword_Score × 0.30)`

**SDG Score (70% of Topic Score):**
- Extract SDGs from Researcher A's `sdg_list`
- Extract SDGs from Researcher B's `sdg_list`
- **Exact matches:** +30 points per matching SDG
- **Related SDGs** (same cluster): +10 points per related SDG
- **Clusters:** 1-6 (social), 7-12 (economic), 13-17 (environmental)
- **Max:** 100 points

**Keyword Score (30% of Topic Score):**
- Extract keywords from Researcher A's `top_keywords`
- Extract keywords from Researcher B's `top_keywords`
- **Jaccard Similarity:** `(Intersection / Union) × 100`
- **Example:** 7 shared keywords out of 13 total = 54% similarity

**Data Source:**
- SDGs: Original CSV `top 1`, `top 2`, `top 3` columns
- Keywords: Original CSV `keywords` column

---

### **Method Score Logic (0-100, weighted 35%):**

**Key Principle:** REWARDS DIFFERENT METHODS (complementarity)

**Complementarity Matrix:**
```
Theoretical + Empirical = 100 points ✅ (Perfect complementarity)
Theoretical + Fieldwork = 100 points ✅
Theoretical + Experimental = 90 points ✅
Empirical + Qualitative = 85 points ✅
Empirical + Fieldwork = 90 points ✅
... (see script for full matrix)

Theoretical + Theoretical = 25 points ❌ (Same method = low)
Empirical + Empirical = 25 points ❌
```

**Logic:**
1. Get Researcher A's `primary_method`
2. Get Researcher B's `primary_method`
3. Check complementarity matrix
4. If complementary pair exists → High score (75-100)
5. If same method → Low score (25)
6. If different but not complementary → Moderate score (50)

**Data Source:**
- Methods: **INFERRED** from Original CSV `keywords` + `abstract` columns

---

### **Stage Score Logic (0-100, weighted 15%):**

**Optimal Matches (100 points):**
- Pre-Tenure + Post-Tenure = Mentorship opportunity ✅
- Pre-Tenure + Senior = Mentorship opportunity ✅
- Post-Tenure + Senior = Strategic partnership ✅

**Good Matches (60-75 points):**
- Same stage = Peer collaboration
- Post-Tenure + Post-Tenure = 75 points
- Pre-Tenure + Pre-Tenure = 60 points

**Moderate Matches (50 points):**
- Other combinations

**Data Source:**
- Career Stage: **CALCULATED** from Original CSV `publication_year` column

---

## 📁 **NEW CSV 3: `Collab_Matches_For_PowerBI.csv`**

### **Purpose:** Enhanced version of faculty_matches for Power BI visualization

### **Additional Columns (beyond faculty_matches.csv):**

| Column | Source | Logic |
|--------|--------|-------|
| **`Match_Quality`** | **CALCULATED** | Based on `Total_Score`:<br>- ≥85 = "Excellent"<br>- 70-84 = "Good"<br>- 55-69 = "Moderate"<br>- <55 = "Low" |
| **`Is_Complementary`** | **CALCULATED** | Boolean: `Method_Score >= 75` |
| **`Match_Pair`** | **GENERATED** | Text: `"{Faculty_A_Name} ↔ {Faculty_B_Name}"` |

**All other columns:** Same as `faculty_matches.csv`

---

## 📁 **NEW CSV 4: `best_faculty_match.csv`**

### **Purpose:** Top 50 matches by Total_Score

### **Generation Logic:**
```python
best_matches = faculty_matches.nlargest(50, 'Total_Score')
```

**Simply:** Takes top 50 rows from `faculty_matches.csv` sorted by `Total_Score` (descending)

**Columns:** Same as `faculty_matches.csv`

---

## 📁 **NEW CSV 5: `network_graph_data.csv`**

### **Purpose:** Network visualization data (edges between researchers)

### **Column Generation Logic:**

| Column | Source | Logic |
|--------|--------|-------|
| **`Source`** | `faculty_matches.csv` `Faculty_A_Name` | ✅ Direct copy |
| **`Target`** | `faculty_matches.csv` `Faculty_B_Name` | ✅ Direct copy |
| **`Score`** | `faculty_matches.csv` `Total_Score` | ✅ Direct copy |
| **`Source_ID`** | `faculty_matches.csv` `Faculty_A_ID` | ✅ Direct copy |
| **`Target_ID`** | `faculty_matches.csv` `Faculty_B_ID` | ✅ Direct copy |

**Filter Applied:**
- Only includes matches where `Total_Score >= 70` (high-quality matches only)

**Why:** Network graphs get cluttered with too many edges. Filtering to high-quality matches makes visualization clearer.

---

## 🔍 **DETAILED METHOD INFERENCE LOGIC**

### **How Research Methods Are Inferred:**

**Step 1: Collect Text**
```python
# Combine all keywords and abstracts for a researcher
all_text = keywords + abstracts (first 5000 chars)
```

**Step 2: Keyword Matching**
```python
method_keywords = {
    'Theoretical': ['theoretical', 'model', 'modeling', 'optimization', 
                   'game theory', 'mathematical', 'algorithm', 'framework'],
    'Empirical': ['empirical', 'statistical', 'regression', 'analysis', 
                 'data', 'quantitative', 'econometric', 'estimation'],
    'Qualitative': ['qualitative', 'case study', 'interview', 'ethnography'],
    'Fieldwork': ['field', 'survey', 'experiment', 'observational', 'fieldwork'],
    'Experimental': ['experiment', 'randomized', 'trial', 'laboratory', 'RCT'],
    'Computational': ['computational', 'simulation', 'machine learning', 'AI', 
                    'artificial intelligence', 'deep learning']
}
```

**Step 3: Count Matches**
```python
# For each method category, count how many keywords appear in text
for method, keywords in method_keywords.items():
    score = count(keywords found in all_text)
```

**Step 4: Assign Method**
```python
# Method with highest score wins
primary_method = method with max(score)
# If no keywords found, default to "Mixed Methods"
```

**Example:**
- Researcher has keywords: "statistical analysis", "regression", "data", "econometric"
- Matches found: Empirical=4, Theoretical=0, Qualitative=0
- **Result:** `primary_method = "Empirical"`

---

## 📊 **DATA FLOW DIAGRAM**

```
Original CSV (2,154 rows)
├── person_uuid, name, email, department
├── publication_year
├── keywords
├── abstract
├── top 1, top 2, top 3 (SDGs)
└── is_sustain
         ↓
    [GROUP BY person_uuid]
         ↓
Researcher Profiles (100-150 rows)
├── person_uuid, name, email, department ✅ (direct)
├── total_publications ✅ (count)
├── first_publication_year ✅ (min)
├── last_publication_year ✅ (max)
├── career_stage ⚠️ (calculated from years)
├── primary_method ⚠️ (inferred from keywords)
├── primary_sdg ✅ (most common from top 1/2/3)
├── sdg_list ✅ (top 3 from top 1/2/3)
└── top_keywords ✅ (most frequent from keywords)
         ↓
    [PAIRWISE COMPARISON]
         ↓
Faculty Matches (4,952 rows)
├── Faculty_A_* ✅ (from Researcher Profile A)
├── Faculty_B_* ✅ (from Researcher Profile B)
├── Topic_Score ⚠️ (calculated: SDG + keywords)
├── Method_Score ⚠️ (calculated: complementarity)
├── Stage_Score ⚠️ (calculated: career fit)
└── Total_Score ⚠️ (calculated: weighted sum)
         ↓
    [DERIVATIVE FILES]
         ↓
├── best_faculty_match.csv (top 50)
├── Collab_Matches_For_PowerBI.csv (+ Match_Quality, Is_Complementary)
└── network_graph_data.csv (filtered to Score >= 70)
```

---

## ✅ **AUTHENTICITY SUMMARY**

### **100% Authentic (Direct from Original CSV):**
- ✅ All researcher names, emails, departments
- ✅ All publication counts and years
- ✅ All SDG alignments (from `top 1`, `top 2`, `top 3`)
- ✅ All keywords (from `keywords` column)
- ✅ All publication metadata

### **Calculated/Inferred (Not Explicit in Original CSV):**
- ⚠️ Research methods (inferred from keywords/abstracts)
- ⚠️ Career stages (calculated from publication years)
- ⚠️ Compatibility scores (calculated using algorithm)

### **Generated (Created by Algorithm):**
- ⚠️ Topic_Score, Method_Score, Stage_Score
- ⚠️ Total_Score
- ⚠️ Match_Quality, Is_Complementary
- ⚠️ Reason text fields

---

## 🎯 **KEY INSIGHTS**

1. **One-to-Many Relationship:** Original CSV has multiple rows per researcher (one per publication). New CSVs aggregate to one row per researcher.

2. **Method Inference:** Methods are NOT in your original data. They're inferred by scanning keywords and abstracts for method-related terms.

3. **Career Stage Calculation:** Stages are calculated from publication years, not from explicit tenure data.

4. **Score Calculation:** All compatibility scores are calculated using transparent algorithms based on your real data.

5. **Data Integrity:** All source data (names, departments, SDGs, keywords) comes directly from your original CSV - nothing is made up.

---

**This explains exactly how each column is generated and where the data comes from!** 📊



