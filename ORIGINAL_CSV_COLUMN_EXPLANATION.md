# Original CSV Column Explanation
## Complete Breakdown of `for distribution case competition filtered_publications.csv`

---

## 📊 **FILE OVERVIEW**

**File Name:** `for distribution case competition filtered_publications.csv`  
**Total Rows:** 2,154 (one row per publication)  
**Total Columns:** 24  
**Data Structure:** Publication-level data (each row = one publication by one researcher)

**Key Point:** This is a **publication-level** dataset. If a researcher has 10 publications, they appear in 10 rows with the same `person_uuid` and `name`, but different `article_uuid` and `title`.

---

## 📋 **COLUMN-BY-COLUMN EXPLANATION**

### **Column 1: `person_uuid`**
**Type:** Text (UUID - Universally Unique Identifier)  
**Example:** `6d42042d-5967-4653-9013-d6eed37ca2c9`

**What it represents:**
- Unique identifier for each researcher/faculty member
- Same `person_uuid` appears in multiple rows (one per publication)
- Used to group publications by researcher

**How it's used:**
- Primary key for identifying researchers
- Used to aggregate publications per researcher
- Links all publications to the same person

**Example:**
- Researcher "Abdel-Khalik, A. Rashad" has `person_uuid = 6d42042d-5967-4653-9013-d6eed37ca2c9`
- This UUID appears in 9 rows (one for each of his 9 publications)

---

### **Column 2: `name`**
**Type:** Text (Full name)  
**Example:** `"Abdel-Khalik, A. Rashad"`

**What it represents:**
- Full name of the researcher/faculty member
- Format: Last name, First name (academic format)
- Same name appears in all rows for the same researcher

**How it's used:**
- Display name for researchers
- Used in all output files (Researcher_Profiles, CCS_Demo_Data, etc.)

**Example:**
- `"Abdel-Khalik, A. Rashad"`
- `"Ahsen, Mehmet"`
- `"Brown, Jeffrey"`

---

### **Column 3: `email`**
**Type:** Text (Email address)  
**Example:** `rashad@illinois.edu`

**What it represents:**
- University email address of the researcher
- Same email appears in all rows for the same researcher
- Used for contact information

**How it's used:**
- Contact information for researchers
- Included in Researcher_Profiles output

**Example:**
- `rashad@illinois.edu`
- `ahsen@illinois.edu`
- `brownjr@illinois.edu`

---

### **Column 4: `department`**
**Type:** Text (Department name)  
**Example:** `Accountancy`

**What it represents:**
- Academic department where the researcher works
- Examples: Accountancy, Business Administration, Finance, etc.
- Same department appears in all rows for the same researcher

**How it's used:**
- Department filtering and grouping
- Used in all output files for department-based analysis

**Example:**
- `Accountancy`
- `Business Administration`
- `Finance`
- `Gies Affiliates`

---

### **Column 5: `active`**
**Type:** Boolean (True/False)  
**Example:** `True`

**What it represents:**
- Whether the researcher is currently active at the university
- `True` = Active faculty member
- `False` = Inactive/former faculty member

**How it's used:**
- Filtering to only active researchers
- Not directly used in output files (all appear to be True)

**Note:** This column appears to be duplicated as `active.1` (column 13)

---

### **Column 6: `article_uuid`**
**Type:** Text (UUID)  
**Example:** `38792cbd-5cff-4cc8-afdf-f5148896e760`

**What it represents:**
- Unique identifier for each publication/article
- Each row has a unique `article_uuid` (one per publication)
- Links to the specific publication record

**How it's used:**
- Primary key for publications
- Not used in output files (we aggregate by researcher, not publication)

**Example:**
- Each publication has a unique UUID
- Same researcher, different publications = different `article_uuid`

---

### **Column 7: `title`**
**Type:** Text (Publication title)  
**Example:** `"CEO risk preference and investing in R and D"`

**What it represents:**
- Full title of the publication/article
- Each row has a unique title (one per publication)
- Academic paper/book chapter title

**How it's used:**
- Publication identification
- Not directly used in output files (we aggregate by researcher)

**Example:**
- `"CEO risk preference and investing in R and D"`
- `"Fair Value Accounting and Stewardship"`
- `"When algorithmic predictions use human-generated data: A bias-aware classification algorithm for breast cancer diagnosis"`

---

### **Column 8: `publication_year`**
**Type:** Number (Year)  
**Example:** `2014`

**What it represents:**
- Year the publication was published
- Range: Typically 2010-2020 (based on data)
- Used to calculate researcher career metrics

**How it's used:**
- **Critical for career stage calculation:**
  - `first_publication_year` = MIN of all years per researcher
  - `last_publication_year` = MAX of all years per researcher
  - `years_since_first` = 2025 - first_publication_year
  - `career_stage` = Calculated from years_since_first

**Example:**
- `2014` - Publication from 2014
- `2011` - Publication from 2011
- Used to determine: Researcher published first in 2011, so `years_since_first = 14` → `career_stage = "Post-Tenure"`

---

### **Column 9: `doi`**
**Type:** URL (Digital Object Identifier)  
**Example:** `https://doi.org/10.1111/abac.12029`

**What it represents:**
- Permanent link to the publication
- DOI (Digital Object Identifier) is a unique identifier for academic publications
- Can be used to access the full publication online

**How it's used:**
- Reference link to publications
- Not used in output files

**Example:**
- `https://doi.org/10.1111/abac.12029`
- `https://doi.org/10.1111/j.1911-3838.2010.00013.x`

---

### **Column 10: `abstract`**
**Type:** Text (HTML formatted)  
**Example:** `"<p>This study aims at: (1) developing an index to measure CEO risk tolerance..."`

**What it represents:**
- Abstract/summary of the publication
- HTML formatted text (contains `<p>` tags)
- Describes the research content and findings

**How it's used:**
- **Used for research method inference:**
  - Combined with `keywords` column
  - Scanned for method-related keywords (e.g., "machine learning", "statistical", "case study")
  - Used to determine `primary_method` (Theoretical, Empirical, Qualitative, etc.)

**Example:**
- Contains full abstract text in HTML format
- Used to infer research methodology

---

### **Column 11: `journal_title`**
**Type:** Text (Journal name)  
**Example:** `Abacus`

**What it represents:**
- Name of the journal where the publication appeared
- Academic journal name
- May be empty for books/chapters

**How it's used:**
- Publication metadata
- Not used in output files

**Example:**
- `Abacus`
- `Accounting Perspectives`
- `Information Systems Research`
- `Cell` (scientific journal)

---

### **Column 12: `journal_issn`**
**Type:** Text (ISSN number)  
**Example:** `0001-3072`

**What it represents:**
- ISSN (International Standard Serial Number) of the journal
- Unique identifier for the journal
- Format: XXXX-XXXX (8 digits with hyphen)

**How it's used:**
- Journal identification
- Not used in output files

**Example:**
- `0001-3072` - ISSN for Abacus journal
- `1911-382X` - ISSN for Accounting Perspectives

---

### **Column 13: `active.1`**
**Type:** Boolean (True/False)  
**Example:** `True`

**What it represents:**
- **Duplicate of `active` column (column 5)**
- Same data as `active`
- Likely a data processing artifact

**How it's used:**
- Not used (duplicate column)
- Can be ignored

---

### **Column 14: `is_sustain`**
**Type:** Number (0.0 or 1.0)  
**Example:** `0.0` or `1.0`

**What it represents:**
- Whether the publication aligns with Sustainable Development Goals (SDGs)
- `1.0` = Publication is sustainability-related
- `0.0` = Publication is not sustainability-related

**How it's used:**
- **Used to calculate `sustainable_publications`:**
  - Sum of all `is_sustain` values per researcher
  - Example: Researcher with 10 publications, 3 have `is_sustain = 1.0` → `sustainable_publications = 3`

**Example:**
- `0.0` - Not sustainability-related
- `1.0` - Sustainability-related (aligns with SDGs)

---

### **Column 15: `top 1`**
**Type:** Number (1-17, or 0.0 if none)  
**Example:** `3.0` or `0.0`

**What it represents:**
- **Primary SDG (Sustainable Development Goal) alignment**
- SDG number (1-17) that the publication most closely aligns with
- `0.0` = No SDG alignment identified
- SDGs: 1=No Poverty, 2=Zero Hunger, 3=Good Health, ..., 17=Partnerships

**How it's used:**
- **Critical for SDG aggregation:**
  - Collected across all publications per researcher
  - Most frequent SDG = `primary_sdg`
  - Used in compatibility scoring (Topic_Match)

**Example:**
- `3.0` - SDG 3: Good Health and Well-being
- `9.0` - SDG 9: Industry, Innovation and Infrastructure
- `0.0` - No SDG alignment

---

### **Column 16: `top 2`**
**Type:** Number (1-17, or 0.0 if none)  
**Example:** `17.0` or `0.0`

**What it represents:**
- **Secondary SDG alignment**
- Second most relevant SDG for the publication
- `0.0` = No secondary SDG identified

**How it's used:**
- **Used in SDG aggregation:**
  - Collected along with `top 1` and `top 3`
  - Used to determine researcher's SDG focus areas
  - Included in `sdg_list` (top 3 most common SDGs)

**Example:**
- `17.0` - SDG 17: Partnerships for the Goals
- `9.0` - SDG 9: Industry, Innovation and Infrastructure
- `0.0` - No secondary SDG

---

### **Column 17: `top 3`**
**Type:** Number (1-17, or 0.0 if none)  
**Example:** `0.0` (most common - no tertiary SDG)

**What it represents:**
- **Tertiary SDG alignment**
- Third most relevant SDG for the publication
- `0.0` = No tertiary SDG identified (very common)

**How it's used:**
- **Used in SDG aggregation:**
  - Collected along with `top 1` and `top 2`
  - Used to determine researcher's SDG focus areas
  - Included in `sdg_list` (top 3 most common SDGs)

**Example:**
- `0.0` - Most publications don't have a third SDG
- `13.0` - SDG 13: Climate Action (rare)

---

### **Column 18: `keywords`**
**Type:** Text (Semicolon-separated)  
**Example:** `"Cash Flow;Large Banks;Volatility;Hedging;Industry;Accounting Change;..."`

**What it represents:**
- Research keywords associated with the publication
- Semicolon-separated list of keywords
- Describes research topics, methods, and themes
- Can be very long (100+ keywords per publication)

**How it's used:**
- **Critical for multiple purposes:**
  1. **Top keywords aggregation:**
     - Collected from all publications per researcher
     - Counted frequency
     - Top 10 most frequent = `top_keywords`
  
  2. **Research method inference:**
     - Combined with `abstract` column
     - Scanned for method-related keywords
     - Used to determine `primary_method`

  3. **Compatibility scoring:**
     - Keyword overlap between researchers
     - Used in Topic_Match calculation (30% of topic score)

**Example:**
- `"Cash Flow;Large Banks;Volatility;Hedging;Industry;Accounting Change;Earnings Volatility;Enron;Shareholders;Self-selection;..."`
- `"Machine Learning;AI;Deep Learning;Neural Networks;Binary Classification;..."`
- `"Gene Regulatory Network;Mixing Coefficient;Artificial Intelligence;..."`

---

### **Column 19: `keyword_ranks`**
**Type:** Text (Semicolon-separated numbers)  
**Example:** `"4.0;3.0;2.5;2.5;2.3333333;2.0;2.0;..."`

**What it represents:**
- Importance/rank scores for each keyword
- Corresponds to keywords in `keywords` column (same order)
- Higher number = more important keyword
- Format: Decimal numbers separated by semicolons

**How it's used:**
- Keyword importance scoring
- **Not used in output files** (we use frequency instead of rank)

**Example:**
- `"4.0;3.0;2.5;2.5;..."` - First keyword has rank 4.0, second has 3.0, etc.
- Corresponds to keywords: "Cash Flow" (4.0), "Large Banks" (3.0), etc.

---

### **Column 20: `pinecone_complete`**
**Type:** Number (0.0 or 1.0)  
**Example:** `1.0`

**What it represents:**
- Processing flag for Pinecone (vector database)
- `1.0` = Data has been processed/loaded into Pinecone
- `0.0` = Not yet processed
- Internal processing indicator

**How it's used:**
- Internal data processing flag
- **Not used in output files**

**Example:**
- `1.0` - Most/all publications appear to be processed

---

### **Column 21: `source`**
**Type:** Text (Data source name)  
**Example:** `Illinois Experts`

**What it represents:**
- Source system where the publication data came from
- Likely the university's research database system
- Same value appears in all rows

**How it's used:**
- Data source tracking
- **Not used in output files**

**Example:**
- `Illinois Experts` - University research database

---

### **Column 22: `Financial Times`**
**Type:** Number (0.0 or 1.0)  
**Example:** `0.0` or `1.0`

**What it represents:**
- Whether the journal is ranked in Financial Times Top 50 journals
- `1.0` = Journal is in FT Top 50
- `0.0` = Journal is not in FT Top 50
- Prestigious business journal ranking

**How it's used:**
- Journal quality/prestige indicator
- **Not used in output files**

**Example:**
- `1.0` - Journal is in Financial Times Top 50
- `0.0` - Journal is not in FT Top 50

---

### **Column 23: `UT Dallas`**
**Type:** Number (0.0 or 1.0)  
**Example:** `0.0` or `1.0`

**What it represents:**
- Whether the journal is ranked in UT Dallas Top 100 journals
- `1.0` = Journal is in UT Dallas Top 100
- `0.0` = Journal is not in UT Dallas Top 100
- Prestigious business journal ranking

**How it's used:**
- Journal quality/prestige indicator
- **Not used in output files**

**Example:**
- `1.0` - Journal is in UT Dallas Top 100
- `0.0` - Journal is not in UT Dallas Top 100

---

### **Column 24: `General Business`**
**Type:** Number (0.0 or 1.0)  
**Example:** `0.0` or `1.0`

**What it represents:**
- Whether the journal is classified as a "General Business" journal
- `1.0` = General Business journal
- `0.0` = Not a General Business journal
- Journal category classification

**How it's used:**
- Journal category indicator
- **Not used in output files**

**Example:**
- `1.0` - General Business journal
- `0.0` - Specialized journal (e.g., Accounting, Finance, etc.)

---

## 📊 **SUMMARY: COLUMNS USED vs NOT USED**

### ✅ **COLUMNS USED IN OUTPUT FILES (9 out of 24):**

| Column | How Used | Output Files |
|--------|----------|--------------|
| `person_uuid` | Grouping key | Researcher_Profiles, Matches |
| `name` | Researcher name | All output files |
| `email` | Contact info | Researcher_Profiles |
| `department` | Department info | All output files |
| `publication_year` | Career stage calculation | Researcher_Profiles |
| `is_sustain` | Sustainable publications count | Researcher_Profiles |
| `top 1`, `top 2`, `top 3` | SDG aggregation | Researcher_Profiles, Matches |
| `keywords` | Method inference + keyword aggregation | Researcher_Profiles, Matches |
| `abstract` | Method inference | Researcher_Profiles (indirect) |

### ❌ **COLUMNS NOT USED (15 out of 24):**

- `active`, `article_uuid`, `title`, `doi`, `journal_title`, `journal_issn`, `active.1`, `keyword_ranks`, `pinecone_complete`, `source`, `Financial Times`, `UT Dallas`, `General Business`

---

## 🎯 **KEY INSIGHTS**

1. **Publication-Level Data:** Each row = one publication, so researchers appear multiple times
2. **SDG Data:** `top 1`, `top 2`, `top 3` columns identify which SDGs each publication aligns with
3. **Keywords are Critical:** Used for method inference, keyword aggregation, and compatibility scoring
4. **Career Metrics:** `publication_year` is essential for calculating career stage
5. **Sparse SDG Data:** Many publications have `top 1/2/3 = 0.0` (no SDG alignment)

---

This explains every column in your original university CSV file! 🎯



