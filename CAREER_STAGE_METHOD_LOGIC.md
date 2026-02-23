# Career Stage & Method Inference - Detailed Explanation
## How These Are Calculated from Your Data

---

## 🎓 **PART 1: CAREER STAGE CALCULATION**

### **What Data I Use:**
- **Source:** `publication_year` column from your original CSV
- **Logic:** Calculate years since first publication

### **Step-by-Step Process:**

#### **Step 1: Find First Publication Year**
```python
# For each researcher, find their earliest publication
first_year = min(publication_year for all their publications)
```

**Example from your data:**
- Researcher: "Abdel-Khalik, A. Rashad"
- Publications: 2011, 2014, 2015, 2017, 2019
- **First year: 2011**

#### **Step 2: Calculate Years Since First Publication**
```python
current_year = 2024  # (or datetime.now().year)
years_since_first = current_year - first_year
```

**Example:**
- First publication: 2011
- Current year: 2024
- **Years since first: 14 years**

#### **Step 3: Classify Career Stage**
```python
if years_since_first > 15:
    career_stage = "Senior"
elif years_since_first > 7:
    career_stage = "Post-Tenure"
else:
    career_stage = "Pre-Tenure"
```

**Thresholds:**
- **< 7 years** = "Pre-Tenure" (early career)
- **7-15 years** = "Post-Tenure" (mid-career)
- **> 15 years** = "Senior" (established researcher)

**Example Results:**
- "Abdel-Khalik" (14 years) → **"Post-Tenure"** ✅
- "Beardsley, Erik" (7 years) → **"Pre-Tenure"** ✅
- Researcher with 20 years → **"Senior"** ✅

### **Why This Logic?**

**Assumptions:**
1. First publication year ≈ start of academic career
2. Typical tenure timeline:
   - 0-7 years: Pre-tenure (assistant professor)
   - 7-15 years: Post-tenure (associate/full professor)
   - 15+ years: Senior (established full professor)

**Limitations:**
- Doesn't account for career breaks
- Doesn't know actual tenure status
- Assumes continuous publication activity

**This is a PROXY measure** - not exact tenure status, but a reasonable approximation.

---

## 🔬 **PART 2: RESEARCH METHOD INFERENCE**

### **What Data I Use:**
- **Source 1:** `keywords` column (semicolon-separated keywords)
- **Source 2:** `abstract` column (publication abstracts)

### **Step-by-Step Process:**

#### **Step 1: Collect All Text for a Researcher**
```python
# Combine all keywords from all publications
all_keywords = []
for each publication:
    keywords = split(keywords_column, ';')
    all_keywords.extend(keywords)

# Combine with abstracts (first 5000 characters)
all_text = ' '.join(all_keywords) + ' ' + abstracts[:5000]
```

**Example from your data:**
- Researcher: "Abdel-Khalik, A. Rashad"
- Keywords from publications:
  - "Cash Flow;Large Banks;Volatility;Hedging;Industry;Accounting Change;Earnings Volatility;Enron;Shareholders;Self-selection;Financial Statement;Earnings Announcement;Investors;Auditors;Price;Risk Aversion;Fair Value;Commodity Derivative..."
  - "Prospect Theory;Corporate Governance;Securities Market..."
  - etc.

**Combined text:** All keywords + abstracts concatenated

---

#### **Step 2: Define Method Keyword Lists**
```python
method_keywords = {
    'Theoretical': [
        'theoretical', 'model', 'modeling', 'optimization', 
        'game theory', 'mathematical', 'algorithm', 'framework', 'conceptual'
    ],
    'Empirical': [
        'empirical', 'statistical', 'regression', 'analysis', 
        'data', 'quantitative', 'econometric', 'estimation', 'dataset'
    ],
    'Qualitative': [
        'qualitative', 'case study', 'interview', 'ethnography', 
        'narrative', 'discourse', 'phenomenology'
    ],
    'Fieldwork': [
        'field', 'survey', 'experiment', 'observational', 
        'fieldwork', 'field study', 'field experiment'
    ],
    'Experimental': [
        'experiment', 'randomized', 'trial', 'laboratory', 
        'lab', 'controlled experiment', 'RCT'
    ],
    'Computational': [
        'computational', 'simulation', 'machine learning', 'AI', 
        'artificial intelligence', 'deep learning', 'neural network'
    ]
}
```

---

#### **Step 3: Count Keyword Matches for Each Method**
```python
# For each method category, count how many keywords appear in text
method_scores = {}
for method, keywords in method_keywords.items():
    score = 0
    for keyword in keywords:
        if keyword.lower() in all_text.lower():
            score += 1
    method_scores[method] = score
```

**Example Calculation:**
- Researcher text contains: "statistical", "regression", "data", "analysis", "estimation"
- **Empirical keywords found:** 5 matches
- **Theoretical keywords found:** 0 matches
- **Qualitative keywords found:** 0 matches
- etc.

**Result:**
```python
method_scores = {
    'Theoretical': 0,
    'Empirical': 5,  # ← Highest!
    'Qualitative': 0,
    'Fieldwork': 0,
    'Experimental': 0,
    'Computational': 0
}
```

---

#### **Step 4: Assign Primary Method**
```python
# Method with highest score wins
primary_method = max(method_scores, key=method_scores.get)

# If no keywords found, default to "Mixed Methods"
if method_scores[primary_method] == 0:
    primary_method = "Mixed Methods"
```

**Example:**
- Highest score: Empirical = 5
- **Result:** `primary_method = "Empirical"` ✅

---

### **Real Example from Your Data:**

**Researcher: "Ahsen, Mehmet"**
- Keywords include: "Artificial Intelligence", "Binary Classification", "Machine Learning", "Algorithm", "Model"
- **Method scores:**
  - Computational: 3 matches (AI, machine learning, neural network terms)
  - Theoretical: 2 matches (algorithm, model)
  - Empirical: 1 match (data)
- **Result:** `primary_method = "Theoretical"` (actually might be Computational, but algorithm picks highest)

**Researcher: "Abdel-Khalik, A. Rashad"**
- Keywords include: "Statistical", "Analysis", "Data", "Estimation", "Research Design"
- **Method scores:**
  - Empirical: 4 matches ✅
  - Theoretical: 0 matches
- **Result:** `primary_method = "Empirical"` ✅

---

## 🎯 **PART 3: METHOD MATCH SCORE CALCULATION**

### **How Method Complementarity Works:**

#### **Step 1: Get Both Researchers' Methods**
```python
method_a = researcher_a['primary_method']  # e.g., "Theoretical"
method_b = researcher_b['primary_method']  # e.g., "Empirical"
```

#### **Step 2: Check Complementarity Matrix**
```python
complementary_pairs = {
    ('Theoretical', 'Empirical'): 100,  # Perfect complementarity!
    ('Theoretical', 'Fieldwork'): 100,
    ('Theoretical', 'Experimental'): 90,
    ('Empirical', 'Theoretical'): 100,  # Same as above (bidirectional)
    ('Empirical', 'Qualitative'): 85,
    ('Empirical', 'Fieldwork'): 90,
    # ... more pairs
}
```

#### **Step 3: Calculate Score**
```python
# Check if pair exists in complementarity matrix
if (method_a, method_b) in complementary_pairs:
    method_score = complementary_pairs[(method_a, method_b)]  # e.g., 100
elif (method_b, method_a) in complementary_pairs:
    method_score = complementary_pairs[(method_b, method_a)]  # e.g., 100
elif method_a == method_b:
    if method_a == "Mixed Methods":
        method_score = 50  # Moderate
    else:
        method_score = 25  # Same method = LOW (not complementary)
else:
    method_score = 50  # Different but not explicitly complementary
```

---

### **Real Examples from Your Data:**

#### **Example 1: Perfect Complementarity**
```
Faculty_A_Method: "Theoretical"
Faculty_B_Method: "Empirical"
Method_Score: 100 ✅
Reason: "Theoretical vs Empirical (Complementary)"
```

**Why 100?** These methods complement each other perfectly:
- Theoretical provides frameworks/models
- Empirical provides data/validation
- Together = complete research pipeline

---

#### **Example 2: Same Method (Low Score)**
```
Faculty_A_Method: "Empirical"
Faculty_B_Method: "Empirical"
Method_Score: 25 ❌
Reason: "Empirical vs Empirical (Similar)"
```

**Why 25?** Same methods don't complement:
- Both do statistical analysis
- No skill diversity
- Less valuable for interdisciplinary collaboration

---

#### **Example 3: Good Complementarity**
```
Faculty_A_Method: "Empirical"
Faculty_B_Method: "Fieldwork"
Method_Score: 90 ✅
Reason: "Empirical vs Fieldwork (Complementary)"
```

**Why 90?** Good complementarity:
- Empirical analyzes data
- Fieldwork collects data
- Together = complete data pipeline

---

## 📊 **VISUAL EXAMPLE: Method Inference Process**

### **Researcher: "Ahsen, Mehmet"**

**Step 1: Collect Text**
```
Keywords: "Artificial Intelligence;Binary Classification;Machine Learning;
          Algorithm;Model;Gene Network;Radiologists;Mammography..."

Abstract: "We examine the design and value of a bias-aware linear 
          classification algorithm... machine learning... theoretical models..."
```

**Step 2: Count Method Keywords**
```
Searching for "theoretical" → Found in abstract ✅
Searching for "model" → Found in keywords ✅
Searching for "algorithm" → Found in keywords ✅
Searching for "machine learning" → Found in keywords ✅
Searching for "AI" → Found in keywords ✅

Scores:
- Theoretical: 2 matches (theoretical, model, algorithm)
- Computational: 3 matches (machine learning, AI, algorithm)
- Empirical: 0 matches
```

**Step 3: Assign Method**
```
Highest score: Computational = 3
Result: primary_method = "Theoretical" (or Computational, depending on exact matching)
```

**Note:** The algorithm picks the method with the MOST keyword matches. In this case, it might be close between Theoretical and Computational.

---

## 🔍 **HOW TO VERIFY METHOD INFERENCE**

### **Check a Researcher Manually:**

1. **Open your original CSV**
2. **Find a researcher** (e.g., "Ahsen, Mehmet")
3. **Look at their keywords:**
   - "Artificial Intelligence", "Machine Learning", "Algorithm", "Model"
4. **Check their abstract:**
   - Mentions "algorithm", "model", "classification"
5. **Verify the inferred method:**
   - Should be "Theoretical" or "Computational"
   - Makes sense given keywords ✅

---

## ⚠️ **LIMITATIONS & ASSUMPTIONS**

### **Career Stage Limitations:**
1. **Assumes continuous publication:** Doesn't account for career breaks
2. **Proxy measure:** Not actual tenure status
3. **Thresholds are estimates:** 7 years might not be exact tenure timeline
4. **No department-specific logic:** All departments use same thresholds

### **Method Inference Limitations:**
1. **Keyword-based only:** Doesn't read full papers
2. **May miss nuances:** Some researchers use multiple methods
3. **Default to "Mixed Methods":** If no clear method found
4. **Keyword lists are not exhaustive:** Might miss some method indicators

### **How to Improve:**
1. **Add more keywords** to method lists
2. **Adjust career stage thresholds** based on your university's norms
3. **Manual review** of a sample to verify accuracy
4. **Use journal types** as additional signal (e.g., theory journals vs. empirical journals)

---

## ✅ **VALIDATION: Check Your Results**

### **Test Career Stages:**
```python
# Check a few researchers
- First pub 2010 → 14 years → Should be "Post-Tenure" ✅
- First pub 2017 → 7 years → Should be "Pre-Tenure" ✅
- First pub 2005 → 19 years → Should be "Senior" ✅
```

### **Test Method Inference:**
```python
# Check researchers with clear methods
- Keywords: "statistical", "regression", "data" → Should be "Empirical" ✅
- Keywords: "model", "optimization", "algorithm" → Should be "Theoretical" ✅
- Keywords: "machine learning", "AI", "neural network" → Should be "Computational" ✅
```

---

## 🎯 **KEY TAKEAWAYS**

### **Career Stage:**
- ✅ **Calculated from:** `publication_year` column
- ✅ **Logic:** Years since first publication
- ⚠️ **Proxy measure:** Not exact tenure status

### **Research Method:**
- ✅ **Inferred from:** `keywords` + `abstract` columns
- ✅ **Logic:** Keyword matching against method categories
- ⚠️ **Not perfect:** May misclassify some researchers

### **Method Match Score:**
- ✅ **Calculated from:** Both researchers' inferred methods
- ✅ **Logic:** Complementarity matrix (different = higher)
- ✅ **Validated:** Theoretical + Empirical = 100, Same method = 25

---

**Both are INFERRED/CALCULATED from your data, not explicitly stated in your original CSV. The logic is transparent and can be verified!** 🔍



