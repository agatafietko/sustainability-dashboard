# Collaboration Hub - Business Logic & Decision Rationale

> **A business analyst's guide to understanding the logic, decisions, and data transformations behind the Collaboration Hub**

This document explains **why** decisions were made, **how** data was transformed, and **what** logic drives the matching algorithm from a business perspective.

---

## 📊 **1. Data Transformation: From Publications CSV to Researcher Profiles**

### **1.1 Original Data Source**

**Input**: `for distribution case competition filtered_publications.csv`

**What it contains:**
- One row per publication
- Author information (name, person_uuid, department, email)
- Publication metadata (year, journal, keywords, abstract)
- SDG labels (`top 1`, `top 2`, `top 3`, `is_sustain`)

**Business challenge**: Publications are at the **publication level**, but we need **researcher-level** profiles for matching.

### **1.2 Transformation Logic**

**Decision**: Aggregate publications by `person_uuid` to create researcher profiles.

**Why this approach:**
- Researchers have multiple publications
- Need to understand their **overall** research focus, not just one paper
- Aggregation reveals patterns (most common SDG, dominant method, career trajectory)

**What we aggregate:**
1. **Publication counts** → Total publications, sustainable count
2. **Years** → First/last publication, years active
3. **Keywords** → Most frequent keywords across all publications
4. **SDGs** → Most common SDG across all publications
5. **Abstracts + Keywords** → Combined to infer research method

**Business rationale**: A researcher's profile should reflect their **body of work**, not a single publication.

---

## 🎯 **2. Weight Selection: Why 50% / 35% / 15%?**

### **2.1 The Formula**

```
CCS_Total = (Topic_Score × 50%) + (Method_Score × 35%) + (Career_Score × 15%)
```

### **2.2 Business Rationale for Weights**

#### **Topic Match: 50% (Primary Factor)**

**Why 50%?**
- **Research alignment is foundational**: Without shared research interests, collaboration won't happen regardless of method or career fit
- **Professor's feedback**: Confirmed that topic alignment is the **primary** consideration
- **Business logic**: Two researchers working on completely different topics (e.g., SDG 1 vs SDG 15) won't collaborate, even with perfect method complementarity

**Example**: 
- Researcher A (SDG 9: Industry/Innovation) + Researcher B (SDG 9: Industry/Innovation) = High topic score
- Researcher A (SDG 9) + Researcher B (SDG 1: No Poverty) = Low topic score, collaboration unlikely

**Decision**: Topic gets the highest weight because it's a **necessary condition** for collaboration.

---

#### **Method Match: 35% (Key Innovation)**

**Why 35%?**
- **Professor's emphasis**: Specifically mentioned seeking **complementary** (different) methods
- **Innovation driver**: Different methods bring different perspectives, leading to more innovative research
- **Business value**: This is the **differentiator** - what makes this solution unique

**Why not higher?**
- Topic alignment must come first (50%)
- Method complementarity is valuable but not sufficient without topic alignment

**Why not lower?**
- Method complementarity is the **key innovation** - needs significant weight to matter
- 35% ensures complementary methods are rewarded, not just nice-to-have

**Example**:
- Theoretical + Empirical = 100 (perfect complementarity)
- Theoretical + Theoretical = 25 (low complementarity)
- **Business insight**: The algorithm actively **penalizes** same methods to encourage diversity

**Decision**: 35% balances innovation (complementarity) with necessity (topic alignment).

---

#### **Career Stage: 15% (Strategic Enabler)**

**Why only 15%?**
- **Secondary to research**: Career stage matters for mentorship, but research alignment and method complementarity are more important for collaboration success
- **Not a blocker**: Two researchers at the same stage can still collaborate successfully
- **Strategic value**: Important for mentorship opportunities, but shouldn't dominate the score

**Why include it at all?**
- **Mentorship opportunities**: Pre-Tenure + Senior pairs create valuable mentorship
- **Strategic fit**: Different career stages bring different perspectives and resources
- **Business value**: Helps identify not just good matches, but **strategic** matches

**Example**:
- Pre-Tenure + Senior = 100 (mentorship opportunity)
- Post-Tenure + Post-Tenure = 75 (peer collaboration)
- **Business insight**: Career stage adds strategic value but doesn't determine collaboration quality

**Decision**: 15% acknowledges career stage value without letting it dominate research quality.

---

### **2.3 Weight Validation**

**How we validated these weights:**
1. **Professor feedback**: Confirmed topic is primary, method complementarity is key
2. **Business logic**: Topic must be highest (necessary condition)
3. **Innovation focus**: Method gets significant weight (35%) to drive complementarity
4. **Strategic value**: Career stage included but secondary (15%)

**Alternative considered**: 60% / 30% / 10%
- **Rejected**: Too much emphasis on topic, not enough on method innovation

**Alternative considered**: 40% / 40% / 20%
- **Rejected**: Method and topic equal weight doesn't reflect that topic is foundational

**Final decision**: 50% / 35% / 15% balances necessity (topic), innovation (method), and strategy (career).

---

## 🔄 **3. Data Simulation: Demo Data vs. Real Data**

### **3.1 Why Demo Data?**

**Business need**: 
- Judges need to see the dashboard working
- Real data might have privacy concerns
- Need diverse examples to show the algorithm works

**Decision**: Create `CCS_Demo_Data.csv` with controlled variation.

### **3.2 What's Simulated vs. Real**

#### **Real (from publications CSV):**
- ✅ Researcher names and departments
- ✅ Career stages (inferred from first publication year)
- ✅ Primary methods (inferred from keywords/abstracts)
- ✅ Top keywords (aggregated from publications)

#### **Simulated (for demo clarity):**
- ⚠️ Some user search inputs (SDG/method) - varied to show diverse scenarios
- ⚠️ Match selection - 2-3 matches per researcher (not all possible pairs)
- ⚠️ Small randomized variation in scores - to show realistic distribution

**Why simulate?**
- **Presentation clarity**: Shows diverse examples (different SDGs, methods, stages)
- **Controlled demonstration**: Can highlight specific scenarios (e.g., perfect complementarity)
- **Privacy**: Doesn't expose all real researcher data

**Business rationale**: Demo data is a **proof of concept** - shows how the algorithm works without exposing all real data.

### **3.3 How Demo Data is Generated**

**Process** (`generate_ccs_demo_data.py`):

1. **Select diverse researchers** (15 researchers, mix of career stages)
   - **Why**: Shows algorithm works across different profiles
   - **Business logic**: Need variety to demonstrate robustness

2. **Generate 2-3 matches per researcher**
   - **Why**: Not all possible pairs (would be too many)
   - **Business logic**: Focus on high-quality examples

3. **Add small randomized variation**
   - **Why**: Shows realistic score distribution
   - **Business logic**: Real scores have variation, demo should reflect that

4. **Use same scoring formula**
   - **Why**: Demo must use same logic as real system
   - **Business logic**: Transparency - demo shows actual algorithm behavior

**Key point**: Demo data uses the **same scoring logic** as real data, just with controlled inputs for presentation clarity.

---

## 🧠 **4. Method Inference Logic: Why Keyword Matching?**

### **4.1 The Challenge**

**Problem**: Publications don't explicitly state "I use Theoretical methods" or "I use Empirical methods"

**Business need**: Need to classify researchers by method to enable complementarity matching.

### **4.2 Decision: Rule-Based Keyword Matching**

**Why not NLP/AI?**
- **Transparency**: Judges can see exactly how methods are inferred
- **Reproducibility**: Same keywords = same method classification
- **Speed**: No model training needed
- **Business logic**: Simple, explainable approach aligns with case competition goals

**Why keyword matching?**
- **Practical**: Keywords and abstracts contain method signals
- **Example**: "regression", "statistical", "data" → Empirical
- **Example**: "model", "optimization", "theoretical" → Theoretical
- **Business rationale**: Researchers describe their methods in their publications

### **4.3 Method Keyword Definitions**

**How we defined methods:**

| Method | Keywords | Business Rationale |
|--------|----------|-------------------|
| **Theoretical** | 'model', 'optimization', 'game theory', 'mathematical' | Theoretical work uses modeling and mathematical frameworks |
| **Empirical** | 'regression', 'statistical', 'data', 'quantitative' | Empirical work analyzes real data statistically |
| **Qualitative** | 'case study', 'interview', 'ethnography' | Qualitative work uses interpretive methods |
| **Fieldwork** | 'field', 'survey', 'experiment', 'observational' | Fieldwork involves data collection in real settings |
| **Experimental** | 'randomized', 'trial', 'laboratory', 'RCT' | Experimental work uses controlled experiments |
| **Computational** | 'simulation', 'machine learning', 'AI', 'neural network' | Computational work uses algorithms and simulations |

**Business logic**: These keywords are **indicators** of method - researchers naturally use these terms when describing their work.

### **4.4 Limitations & Trade-offs**

**Limitation**: May miss nuanced method distinctions
- **Example**: A researcher might use both theoretical modeling AND empirical validation
- **Trade-off**: Defaults to "Mixed Methods" if no clear signal

**Why accept this limitation?**
- **Pragmatic**: Most researchers have a dominant method
- **Business value**: Good enough to enable complementarity matching
- **Future improvement**: Could use richer NLP, but current approach is transparent

**Decision**: Simple, transparent approach > complex, black-box approach for case competition.

---

## 📈 **5. Complementarity Matrix: Why Reward Different Methods?**

### **5.1 The Innovation**

**Traditional approach**: Match researchers with **same** methods
- Example: Theoretical + Theoretical = High score

**Our approach**: Match researchers with **complementary** methods
- Example: Theoretical + Empirical = High score (100)
- Example: Theoretical + Theoretical = Low score (25)

### **5.2 Business Rationale**

**Why complementarity?**

1. **Innovation**: Different methods bring different perspectives
   - Theoretical researcher provides frameworks
   - Empirical researcher tests them
   - Together: Stronger research

2. **Real-world success**: Successful collaborations often combine methods
   - Example: Theoretical model + Empirical validation
   - Example: Qualitative insights + Quantitative analysis

3. **Professor's feedback**: Emphasized seeking **complementary** skills

4. **Business value**: Creates more innovative, impactful research

### **5.3 Complementarity Matrix Logic**

**High scores (85-100) for complementary pairs:**
- Theoretical + Empirical = 100
- Theoretical + Fieldwork = 100
- Empirical + Qualitative = 85

**Why these pairs?**
- **Theoretical + Empirical**: Framework development + validation = complete research cycle
- **Theoretical + Fieldwork**: Models + real-world data = grounded theory
- **Empirical + Qualitative**: Numbers + stories = comprehensive understanding

**Low scores (25) for same methods:**
- Theoretical + Theoretical = 25
- Empirical + Empirical = 25

**Why penalize same methods?**
- **Business logic**: Two theoretical researchers might duplicate work
- **Innovation**: Same methods = same perspective = less innovation
- **Value creation**: Complementarity creates more value than similarity

**Decision**: Actively reward diversity to drive innovation.

---

## 🎓 **6. Career Stage Logic: Why 15%?**

### **6.1 Career Stage Inference**

**How it's calculated:**
```python
years_since_first = 2025 - first_publication_year

if years_since_first > 15:
    career_stage = "Senior"
elif years_since_first > 7:
    career_stage = "Post-Tenure"
else:
    career_stage = "Pre-Tenure"
```

**Business rationale**: 
- **Simple proxy**: Years since first publication correlates with career stage
- **Practical**: No need for tenure status data (might not be available)
- **Transparent**: Judges can understand the logic

**Limitation**: May misclassify some researchers
- **Example**: Researcher who started late might be classified as Pre-Tenure but actually Post-Tenure
- **Trade-off**: Simple, transparent > perfect accuracy

### **6.2 Career Stage Scoring**

**Optimal pairs (100 points):**
- Pre-Tenure + Post-Tenure
- Pre-Tenure + Senior
- Post-Tenure + Senior

**Why these score highest?**
- **Mentorship opportunities**: Senior researchers can guide junior researchers
- **Resource complementarity**: Different stages bring different resources (time, funding, networks)
- **Business value**: Creates strategic partnerships beyond just research

**Peer pairs (60-75 points):**
- Same stage (Post-Tenure + Post-Tenure = 75)
- Same stage (Pre-Tenure + Pre-Tenure = 60)

**Why still good scores?**
- **Peer collaboration**: Researchers at same stage can collaborate as equals
- **Business logic**: Peer collaboration is valuable, just not as strategic as mentorship

**Why 15% weight?**
- **Secondary to research**: Career stage matters, but research alignment and method complementarity matter more
- **Strategic value**: Acknowledges mentorship value without dominating score
- **Business balance**: 15% ensures career stage influences matches but doesn't override research quality

---

## 🔍 **7. Topic Score: Why SDG 70% + Keywords 30%?**

### **7.1 Sub-Component Weights**

```
Topic_Score = (SDG_Score × 0.7) + (Keyword_Score × 0.3)
```

### **7.2 Business Rationale**

#### **SDG Alignment: 70% of Topic Score**

**Why 70%?**
- **Structured framework**: SDGs provide a clear, standardized way to categorize research
- **Strategic alignment**: University wants to align with UN SDGs
- **Business value**: SDG alignment is more reliable than keyword matching
- **Case competition focus**: Sustainability Impact Engine is SDG-focused

**How it works:**
- **Exact SDG match**: Same SDG = 30 points each
- **Related SDGs**: Same cluster (1-6 social, 7-12 economic, 13-17 environmental) = bonus
- **Business logic**: Researchers working on related SDGs might collaborate

**Example**:
- Researcher A (SDG 9) + Researcher B (SDG 9) = High SDG score
- Researcher A (SDG 9) + Researcher B (SDG 7) = Moderate SDG score (both economic cluster)

#### **Keyword Overlap: 30% of Topic Score**

**Why 30%?**
- **Complementary to SDG**: Keywords provide granularity beyond SDG labels
- **Business value**: Two researchers might have same SDG but different keywords (e.g., "AI" vs "robotics")
- **Refinement**: Keywords help distinguish within SDG categories

**How it works:**
- **Jaccard similarity**: `intersection / union` of keyword sets
- **Business logic**: More shared keywords = more aligned research interests

**Example**:
- Researcher A (keywords: "machine learning", "AI", "neural networks")
- Researcher B (keywords: "machine learning", "deep learning", "AI")
- High keyword overlap = high keyword score

**Why 70/30 split?**
- **SDG is primary**: More structured, reliable indicator
- **Keywords refine**: Add granularity but are less reliable
- **Business balance**: SDG provides structure, keywords provide detail

---

## 📊 **8. Data Flow: How Original CSV Becomes Matches**

### **8.1 Complete Transformation Pipeline**

```
Original Publications CSV
    ↓
[Step 1] Clean & Validate
    - Remove invalid years
    - Validate SDG labels (1-17)
    - Filter to valid publications
    ↓
[Step 2] Aggregate by Researcher
    - Group by person_uuid
    - Count publications
    - Extract keywords
    - Identify primary SDG
    - Infer career stage
    - Infer research method
    ↓
Researcher_Profiles_For_PowerBI.csv
    ↓
[Step 3] Calculate Pairwise Compatibility
    - For each researcher pair:
      - Calculate topic score (SDG + keywords)
      - Calculate method score (complementarity)
      - Calculate career score (mentorship)
      - Combine with weights (50/35/15)
    ↓
Collab_Matches_For_PowerBI.csv
    ↓
[Step 4] Generate Demo Data (Optional)
    - Select diverse researchers
    - Generate 2-3 matches each
    - Add controlled variation
    - Use same scoring formula
    ↓
CCS_Demo_Data.csv (for Power BI dashboard)
```

### **8.2 Business Decisions at Each Step**

**Step 1 - Cleaning:**
- **Decision**: Remove publications outside 1900-2026
- **Rationale**: Data quality - invalid years indicate data errors
- **Business impact**: Ensures only valid publications are analyzed

**Step 2 - Aggregation:**
- **Decision**: Aggregate by researcher (not by publication)
- **Rationale**: Need researcher-level profiles for matching
- **Business impact**: Creates actionable profiles from publication data

**Step 3 - Pairwise Matching:**
- **Decision**: Calculate all pairs (or top 100 researchers)
- **Rationale**: Need compatibility scores for all potential matches
- **Business impact**: Enables ranking and recommendation

**Step 4 - Demo Data:**
- **Decision**: Create synthetic demo data with variation
- **Rationale**: Presentation clarity without exposing all real data
- **Business impact**: Demonstrates algorithm while protecting privacy

---

## 🎯 **9. Key Business Insights**

### **9.1 Why This Approach Works**

1. **Transparent**: Every score is explainable
   - Judges can see exactly why a match was recommended
   - No black box - builds trust

2. **Business-aligned**: Weights reflect business priorities
   - Topic alignment (50%) = foundational
   - Method complementarity (35%) = innovation driver
   - Career stage (15%) = strategic enabler

3. **Innovative**: Rewards complementarity, not similarity
   - Different from traditional "find similar researchers" approach
   - Drives interdisciplinary innovation

4. **Practical**: Uses available data
   - No need for additional data sources
   - Works with publication metadata

### **9.2 Trade-offs Made**

| Decision | Trade-off | Business Rationale |
|----------|-----------|-------------------|
| Rule-based (not AI) | Less "sophisticated" | Transparency > complexity for case competition |
| Keyword matching for methods | May miss nuance | Simple & explainable > perfect accuracy |
| 15% career weight | Lower than some might expect | Research quality > mentorship opportunity |
| Demo data with variation | Not "real" data | Presentation clarity > data authenticity |

**Key insight**: Every decision balances **transparency**, **practicality**, and **business value**.

---

## 📝 **10. Summary: Business Logic Chain**

**Problem**: How to recommend research collaborators?

**Solution logic**:
1. **Topic alignment is necessary** (50%) → Without shared interests, collaboration won't happen
2. **Method complementarity drives innovation** (35%) → Different methods = more innovative research
3. **Career stage enables strategy** (15%) → Mentorship adds value but doesn't determine quality

**Data transformation**:
- Publications → Researcher profiles → Compatibility scores → Recommendations

**Key innovation**:
- Reward **complementarity** (Theoretical + Empirical) over **similarity** (Theoretical + Theoretical)

**Business value**:
- Transparent, explainable recommendations
- Drives interdisciplinary innovation
- Supports strategic mentorship opportunities

---

**This document explains the business reasoning behind every major decision in the Collaboration Hub.**
