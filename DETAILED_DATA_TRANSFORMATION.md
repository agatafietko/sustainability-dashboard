# Detailed Data Transformation: Original CSV to New CSVs
## Exact Column-by-Column Breakdown with Real Examples

---

## 📊 **ORIGINAL CSV STRUCTURE**

**File:** `for distribution case competition filtered_publications.csv`  
**Total Rows:** 2,154 (one row per publication)  
**Total Columns:** 24

---

## 🔍 **COLUMN-BY-COLUMN ANALYSIS**

### **Column 1: `person_uuid`**
**Original Data Type:** Text (UUID)  
**Example Value:** `6d42042d-5967-4653-9013-d6eed37ca2c9`

**How It's Used:**
- ✅ **USED DIRECTLY** - Primary key for grouping publications by researcher
- **In New CSVs:**
  - `Researcher_Profiles_For_PowerBI.csv`: `person_uuid` column (direct copy)
  - `faculty_matches.csv`: `Faculty_A_ID` and `Faculty_B_ID` (direct copy)

**Transformation:**
```python
# Groups all rows with same person_uuid together
person_df = df[df['person_uuid'] == '6d42042d-5967-4653-9013-d6eed37ca2c9']
# Result: 9 rows (9 publications for this researcher)
```

---

### **Column 2: `name`**
**Original Data Type:** Text  
**Example Value:** `"Abdel-Khalik, A. Rashad"`

**How It's Used:**
- ✅ **USED DIRECTLY** - Copied from first row per researcher
- **In New CSVs:**
  - `Researcher_Profiles_For_PowerBI.csv`: `name` column
  - `faculty_matches.csv`: `Faculty_A_Name` and `Faculty_B_Name`

**Transformation:**
```python
# Takes first occurrence (all rows for same person have same name)
name = person_df['name'].iloc[0]
# Result: "Abdel-Khalik, A. Rashad"
```

---

### **Column 3: `email`**
**Original Data Type:** Text  
**Example Value:** `rashad@illinois.edu`

**How It's Used:**
- ✅ **USED DIRECTLY** - Copied from first row per researcher
- **In New CSVs:**
  - `Researcher_Profiles_For_PowerBI.csv`: `email` column

**Transformation:**
```python
email = person_df['email'].iloc[0] if pd.notna(person_df['email'].iloc[0]) else ""
# Result: "rashad@illinois.edu"
```

---

### **Column 4: `department`**
**Original Data Type:** Text  
**Example Value:** `Accountancy`

**How It's Used:**
- ✅ **USED DIRECTLY** - Copied from first row per researcher
- **In New CSVs:**
  - `Researcher_Profiles_For_PowerBI.csv`: `department` column
  - `faculty_matches.csv`: `Faculty_A_Dept` and `Faculty_B_Dept`

**Transformation:**
```python
department = person_df['department'].iloc[0] if pd.notna(person_df['department'].iloc[0]) else "Unknown"
# Result: "Accountancy"
```

---

### **Column 5: `active`**
**Original Data Type:** Boolean  
**Example Value:** `True`

**How It's Used:**
- ❌ **NOT USED** - Not included in new CSVs

---

### **Column 6: `article_uuid`**
**Original Data Type:** Text (UUID)  
**Example Value:** `38792cbd-5cff-4cc8-afdf-f5148896e760`

**How It's Used:**
- ❌ **NOT USED** - Not included in new CSVs (publication-level identifier, not needed for researcher profiles)

---

### **Column 7: `title`**
**Original Data Type:** Text  
**Example Value:** `"CEO risk preference and investing in R and D"`

**How It's Used:**
- ❌ **NOT USED DIRECTLY** - Not included in new CSVs
- ⚠️ **INDIRECTLY USED** - Could be used for method inference, but script uses `keywords` and `abstract` instead

---

### **Column 8: `publication_year`**
**Original Data Type:** Number  
**Example Values:** `2014`, `2011`, `2015`, `2013`, `2017`, `2016`, `2019`

**How It's Used:**
- ✅ **USED FOR CALCULATIONS** - Critical for career stage inference
- **In New CSVs:**
  - `Researcher_Profiles_For_PowerBI.csv`: 
    - `first_publication_year` (MIN of all years)
    - `last_publication_year` (MAX of all years)
    - `years_active` (MAX - MIN)
    - `years_since_first` (2025 - MIN) → Used to calculate `career_stage`

**Transformation Example:**
```python
# Original data for researcher "Abdel-Khalik, A. Rashad":
# Row 1: publication_year = 2014
# Row 2: publication_year = 2011
# Row 3: publication_year = 2015
# Row 4: publication_year = 2013
# Row 5: publication_year = 2017
# Row 6: publication_year = 2016
# Row 7: publication_year = 2019
# Row 8: publication_year = 2019
# Row 9: publication_year = 2019

first_year = min([2014, 2011, 2015, 2013, 2017, 2016, 2019, 2019, 2019])
# Result: first_publication_year = 2011

last_year = max([2014, 2011, 2015, 2013, 2017, 2016, 2019, 2019, 2019])
# Result: last_publication_year = 2019

years_active = 2019 - 2011
# Result: years_active = 8

years_since_first = 2025 - 2011
# Result: years_since_first = 14

# Career stage calculation:
if years_since_first > 15:
    career_stage = "Senior"
elif years_since_first > 7:
    career_stage = "Post-Tenure"  # ✅ 14 > 7, so "Post-Tenure"
else:
    career_stage = "Pre-Tenure"
# Result: career_stage = "Post-Tenure"
```

---

### **Column 9: `doi`**
**Original Data Type:** URL  
**Example Value:** `https://doi.org/10.1111/abac.12029`

**How It's Used:**
- ❌ **NOT USED** - Not included in new CSVs

---

### **Column 10: `abstract`**
**Original Data Type:** Text (HTML formatted)  
**Example Value:** `"<p>This study aims at: (1) developing an index to measure CEO risk tolerance..."`

**How It's Used:**
- ✅ **USED FOR METHOD INFERENCE** - Combined with keywords to determine research method
- **In New CSVs:**
  - Not directly included, but used to calculate `primary_method` in `Researcher_Profiles_For_PowerBI.csv`

**Transformation:**
```python
# Collect all abstracts for researcher
abstracts = []
for row in person_df:
    if pd.notna(row['abstract']):
        abstracts.append(str(row['abstract']).lower())

# Combine with keywords (see keywords section)
all_text = ' '.join(keywords) + ' ' + ' '.join(abstracts)[:5000]
# First 5000 characters of combined text

# Then scan for method keywords (see method inference section)
```

**Real Example:**
```python
# For "Abdel-Khalik, A. Rashad", abstracts contain words like:
# "accounting", "fair value", "derivatives", "hedging", "financial instruments"
# These don't match method keywords strongly, so method = "Mixed Methods"
```

---

### **Column 11: `journal_title`**
**Original Data Type:** Text  
**Example Value:** `Abacus`

**How It's Used:**
- ❌ **NOT USED** - Not included in new CSVs

---

### **Column 12: `journal_issn`**
**Original Data Type:** Text  
**Example Value:** `0001-3072`

**How It's Used:**
- ❌ **NOT USED** - Not included in new CSVs

---

### **Column 13: `active.1`**
**Original Data Type:** Boolean (duplicate of `active`)  
**Example Value:** `True`

**How It's Used:**
- ❌ **NOT USED** - Duplicate column, not included in new CSVs

---

### **Column 14: `is_sustain`**
**Original Data Type:** Number (0.0 or 1.0)  
**Example Values:** `0.0` (not sustainable), `1.0` (sustainable)

**How It's Used:**
- ✅ **USED FOR AGGREGATION** - Summed across all publications per researcher
- **In New CSVs:**
  - `Researcher_Profiles_For_PowerBI.csv`: `sustainable_publications` (SUM of all `is_sustain` values)

**Transformation Example:**
```python
# Original data for researcher "Abdel-Khalik, A. Rashad":
# Row 1: is_sustain = 0.0
# Row 2: is_sustain = 0.0
# Row 3: is_sustain = 0.0
# Row 4: is_sustain = 0.0
# Row 5: is_sustain = 0.0
# Row 6: is_sustain = 0.0
# Row 7: is_sustain = 0.0
# Row 8: is_sustain = 0.0
# Row 9: is_sustain = 0.0

sustainable_pubs = sum([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
# Result: sustainable_publications = 0

# For researcher "Ahsen, Mehmet":
# Row 1: is_sustain = 1.0
# Row 2: is_sustain = 1.0
# Row 3: is_sustain = 1.0
# Row 4: is_sustain = 1.0
# Row 5: is_sustain = 1.0
# Row 6: is_sustain = 1.0

sustainable_pubs = sum([1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
# Result: sustainable_publications = 6
```

---

### **Column 15: `top 1`**
**Original Data Type:** Number (1-17, or 0.0 if none)  
**Example Values:** `0.0` (no SDG), `3.0` (SDG 3: Good Health), `9.0` (SDG 9: Industry)

**How It's Used:**
- ✅ **USED FOR SDG AGGREGATION** - Collected across all publications per researcher
- **In New CSVs:**
  - `Researcher_Profiles_For_PowerBI.csv`: 
    - `primary_sdg` (most common SDG from `top 1`, `top 2`, `top 3`)
    - `sdg_list` (top 3 most common SDGs)
  - Used in compatibility scoring: `Topic_Score` calculation

**Transformation Example:**
```python
# Original data for researcher "Ahsen, Mehmet":
# Row 1: top 1 = 3.0, top 2 = 0.0, top 3 = 0.0
# Row 2: top 1 = 3.0, top 2 = 17.0, top 3 = 0.0
# Row 3: top 1 = 3.0, top 2 = 9.0, top 3 = 0.0
# Row 4: top 1 = 3.0, top 2 = 0.0, top 3 = 0.0
# Row 5: top 1 = 3.0, top 2 = 0.0, top 3 = 0.0
# Row 6: top 1 = 3.0, top 2 = 0.0, top 3 = 0.0

# Collect all SDGs (only valid ones: 1-17)
all_sdgs = []
for row in person_df:
    if 1 <= row['top 1'] <= 17:
        all_sdgs.append(int(row['top 1']))  # [3, 3, 3, 3, 3, 3]
    if 1 <= row['top 2'] <= 17:
        all_sdgs.append(int(row['top 2']))  # [17, 9]
    if 1 <= row['top 3'] <= 17:
        all_sdgs.append(int(row['top 3']))  # []

# Result: all_sdgs = [3, 3, 3, 3, 3, 3, 17, 9]

# Count frequency
sdg_counts = Counter(all_sdgs)
# Result: {3: 6, 17: 1, 9: 1}

# Most common = primary SDG
primary_sdg = 3  # Appears 6 times

# Top 3 most common = SDG list
sdg_list = [3, 17, 9]  # Sorted by frequency
# Result in CSV: sdg_list = "3,17,9"
```

---

### **Column 16: `top 2`**
**Original Data Type:** Number (1-17, or 0.0 if none)  
**Example Values:** `0.0`, `17.0` (SDG 17: Partnerships), `9.0` (SDG 9: Industry)

**How It's Used:**
- ✅ **USED FOR SDG AGGREGATION** - Same as `top 1` (see above)

---

### **Column 17: `top 3`**
**Original Data Type:** Number (1-17, or 0.0 if none)  
**Example Values:** `0.0` (most common - no tertiary SDG)

**How It's Used:**
- ✅ **USED FOR SDG AGGREGATION** - Same as `top 1` (see above)

---

### **Column 18: `keywords`**
**Original Data Type:** Text (semicolon-separated)  
**Example Value:** `"Cash Flow;Large Banks;Volatility;Hedging;Industry;Accounting Change;..."`

**How It's Used:**
- ✅ **USED EXTENSIVELY** - Critical for:
  1. **Top Keywords Aggregation** - Most frequent keywords across all publications
  2. **Method Inference** - Scanned for method-related keywords
  3. **Compatibility Scoring** - Keyword overlap between researchers (Topic Score)

**In New CSVs:**
- `Researcher_Profiles_For_PowerBI.csv`: `top_keywords` (top 10, semicolon-separated)
- Used to calculate `primary_method`
- Used in `Topic_Score` calculation (keyword overlap)

**Transformation Example:**
```python
# Original data for researcher "Abdel-Khalik, A. Rashad":
# Row 1: keywords = "Cash Flow;Large Banks;Volatility;Hedging;Industry;..."
# Row 2: keywords = "Cash Flow;Large Banks;Volatility;Hedging;Industry;..."
# Row 3: keywords = "Cash Flow;Large Banks;Volatility;Hedging;Industry;..."
# ... (same keywords repeated across all 9 publications)

# Extract keywords from each row
all_keywords = []
for row in person_df:
    keywords_str = row['keywords']
    if pd.notna(keywords_str):
        # Split by semicolon
        keywords = [k.strip() for k in str(keywords_str).split(';') if k.strip()]
        all_keywords.extend(keywords)

# Result: all_keywords = ["Cash Flow", "Large Banks", "Volatility", "Hedging", 
#                         "Industry", "Accounting Change", "Cash Flow", "Large Banks", 
#                         "Volatility", ...] (repeated across all publications)

# Count frequency
keyword_counts = Counter(all_keywords)
# Result: {"Cash Flow": 9, "Large Banks": 9, "Volatility": 9, "Hedging": 9, 
#          "Industry": 9, "Accounting Change": 9, ...}

# Top 10 most common
top_keywords = [kw for kw, _ in keyword_counts.most_common(10)]
# Result: ["Cash Flow", "Large Banks", "Volatility", "Hedging", "Industry", 
#          "Accounting Change", "Earnings Volatility", "Enron", "Shareholders", 
#          "Self-selection"]

# Join with semicolon
top_keywords_str = ';'.join(top_keywords)
# Result in CSV: "Cash Flow;Large Banks;Volatility;Hedging;Industry;Accounting Change;Earnings Volatility;Enron;Shareholders;Self-selection"
```

**Method Inference from Keywords:**
```python
# Combine keywords and abstracts
all_text = ' '.join([kw.lower() for kw in top_keywords])
# Result: "cash flow large banks volatility hedging industry accounting change..."

# Define method keywords
method_keywords = {
    'Theoretical': ['theoretical', 'model', 'optimization', 'game theory'],
    'Empirical': ['empirical', 'statistical', 'regression', 'data'],
    'Computational': ['computational', 'simulation', 'machine learning', 'AI'],
    # ... more methods
}

# Count matches for each method
method_scores = {}
for method, keywords in method_keywords.items():
    score = sum(1 for kw in keywords if kw in all_text)
    method_scores[method] = score

# For "Abdel-Khalik, A. Rashad":
# - "model" appears in keywords? No
# - "statistical" appears? No
# - "machine learning" appears? No
# Result: method_scores = {'Theoretical': 0, 'Empirical': 0, 'Computational': 0, ...}

# Since all scores are 0, assign "Mixed Methods"
primary_method = "Mixed Methods"
```

**For "Ahsen, Mehmet" (different example):**
```python
# Keywords include: "Machine Learning", "Artificial Intelligence", "Binary Classification", 
#                   "Gene Network", "Radiologists", "Mammography", "Compressed Sensing", 
#                   "Learning Theory", "RNA Sequencing", "Python Package"

all_text = "machine learning artificial intelligence binary classification..."

# Method keyword matching:
# - "machine learning" in all_text? ✅ Yes
# - "artificial intelligence" in all_text? ✅ Yes
# - "simulation" in all_text? Maybe
# Result: method_scores = {'Computational': 3, 'Theoretical': 1, 'Empirical': 0, ...}

# Highest score = Computational
primary_method = "Computational"
```

---

### **Column 19: `keyword_ranks`**
**Original Data Type:** Text (semicolon-separated numbers)  
**Example Value:** `"4.0;3.0;2.5;2.5;2.3333333;2.0;..."`

**How It's Used:**
- ❌ **NOT USED** - Not included in new CSVs (importance scores, but we use frequency instead)

---

### **Column 20: `pinecone_complete`**
**Original Data Type:** Number  
**Example Value:** `1.0`

**How It's Used:**
- ❌ **NOT USED** - Not included in new CSVs (internal processing flag)

---

### **Column 21: `source`**
**Original Data Type:** Text  
**Example Value:** `Illinois Experts`

**How It's Used:**
- ❌ **NOT USED** - Not included in new CSVs

---

### **Column 22: `Financial Times`**
**Original Data Type:** Number (0.0 or 1.0)  
**Example Value:** `0.0` or `1.0`

**How It's Used:**
- ❌ **NOT USED** - Not included in new CSVs (journal ranking flag)

---

### **Column 23: `UT Dallas`**
**Original Data Type:** Number (0.0 or 1.0)  
**Example Value:** `0.0` or `1.0`

**How It's Used:**
- ❌ **NOT USED** - Not included in new CSVs (journal ranking flag)

---

### **Column 24: `General Business`**
**Original Data Type:** Number (0.0 or 1.0)  
**Example Value:** `0.0` or `1.0`

**How It's Used:**
- ❌ **NOT USED** - Not included in new CSVs (journal ranking flag)

---

## 📊 **SUMMARY: COLUMNS USED vs NOT USED**

### ✅ **COLUMNS USED (9 out of 24):**

| Column | How Used | New CSV Column(s) |
|--------|----------|-------------------|
| `person_uuid` | Direct copy (grouping key) | `person_uuid`, `Faculty_A_ID`, `Faculty_B_ID` |
| `name` | Direct copy | `name`, `Faculty_A_Name`, `Faculty_B_Name` |
| `email` | Direct copy | `email` |
| `department` | Direct copy | `department`, `Faculty_A_Dept`, `Faculty_B_Dept` |
| `publication_year` | MIN/MAX/Calculation | `first_publication_year`, `last_publication_year`, `years_active`, `years_since_first`, `career_stage` |
| `is_sustain` | SUM aggregation | `sustainable_publications` |
| `top 1` | Frequency aggregation | `primary_sdg`, `sdg_list` |
| `top 2` | Frequency aggregation | `primary_sdg`, `sdg_list` |
| `top 3` | Frequency aggregation | `primary_sdg`, `sdg_list` |
| `keywords` | Frequency aggregation + Method inference | `top_keywords`, `primary_method` |
| `abstract` | Method inference (indirect) | `primary_method` |

### ❌ **COLUMNS NOT USED (13 out of 24):**

- `active`, `article_uuid`, `title`, `doi`, `journal_title`, `journal_issn`, `active.1`, `keyword_ranks`, `pinecone_complete`, `source`, `Financial Times`, `UT Dallas`, `General Business`

---

## 🔄 **COMPLETE TRANSFORMATION EXAMPLE**

### **Original Data (9 rows for one researcher):**

```
person_uuid: 6d42042d-5967-4653-9013-d6eed37ca2c9
name: "Abdel-Khalik, A. Rashad"
email: rashad@illinois.edu
department: Accountancy

Row 1: publication_year=2014, is_sustain=0.0, top 1=0.0, keywords="Cash Flow;Large Banks;..."
Row 2: publication_year=2011, is_sustain=0.0, top 1=0.0, keywords="Cash Flow;Large Banks;..."
Row 3: publication_year=2014, is_sustain=0.0, top 1=0.0, keywords="Cash Flow;Large Banks;..."
Row 4: publication_year=2015, is_sustain=0.0, top 1=0.0, keywords="Cash Flow;Large Banks;..."
Row 5: publication_year=2013, is_sustain=0.0, top 1=0.0, keywords="Cash Flow;Large Banks;..."
Row 6: publication_year=2017, is_sustain=0.0, top 1=0.0, keywords="Cash Flow;Large Banks;..."
Row 7: publication_year=2016, is_sustain=0.0, top 1=0.0, keywords="Cash Flow;Large Banks;..."
Row 8: publication_year=2019, is_sustain=0.0, top 1=0.0, keywords="Cash Flow;Large Banks;..."
Row 9: publication_year=2019, is_sustain=0.0, top 1=0.0, keywords="Cash Flow;Large Banks;..."
```

### **Transformed Data (1 row in Researcher_Profiles_For_PowerBI.csv):**

```
person_uuid: 6d42042d-5967-4653-9013-d6eed37ca2c9
name: "Abdel-Khalik, A. Rashad"
email: rashad@illinois.edu
department: Accountancy
total_publications: 9                    # COUNT of rows
sustainable_publications: 0               # SUM of is_sustain (0+0+0+0+0+0+0+0+0)
first_publication_year: 2011              # MIN of publication_year
last_publication_year: 2019               # MAX of publication_year
years_active: 8                           # 2019 - 2011
years_since_first: 14                     # 2025 - 2011
career_stage: "Post-Tenure"               # INFERRED (14 > 7 and 14 <= 15)
primary_method: "Mixed Methods"            # INFERRED (no strong method keywords found)
primary_sdg: None                         # No SDGs in top 1/2/3 (all 0.0)
sdg_list: ""                              # No SDGs
top_keywords: "Cash Flow;Large Banks;Volatility;Hedging;Industry;Accounting Change;Earnings Volatility;Enron;Shareholders;Self-selection"
                                          # Top 10 most frequent keywords
```

---

## 🎯 **KEY INSIGHTS**

1. **Only 9 out of 24 columns are used** - The script focuses on researcher-level data, not publication-level details
2. **Most transformations are aggregations** - COUNT, SUM, MIN, MAX, frequency counting
3. **Two key inferences:**
   - **Career Stage** - Calculated from `publication_year` (years since first)
   - **Research Method** - Inferred from `keywords` + `abstract` (keyword matching)
4. **SDG data is sparse** - Many researchers have `top 1/2/3 = 0.0` (no SDG alignment)
5. **Keywords are critical** - Used for both method inference and compatibility scoring

---

This shows exactly which data from your original CSV was used to create the new files! 🎯



