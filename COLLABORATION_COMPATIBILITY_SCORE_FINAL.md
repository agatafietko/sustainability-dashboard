# Collaboration Compatibility Score - Final Algorithm & UX Design
## Illinois Sustainability Impact Engine - Case Competition Deliverable

---

## 📋 **EXECUTIVE SUMMARY**

This document finalizes the **Collaboration Compatibility Score** algorithm and provides comprehensive UX design specifications for the Collaboration Hub. The solution addresses Pillar 2 (Insight Generation) by proactively suggesting interdisciplinary research partners based on quantified compatibility metrics.

**Key Innovation**: A weighted scoring system that quantifies collaboration potential across three critical dimensions validated by stakeholder research.

---

## 🎯 **TASK 1: FINALIZED ALGORITHM & JUSTIFICATION**

### **1.1 Formula Structure**

The Collaboration Compatibility Score is calculated using a weighted linear combination:

$$\text{Compatibility Score} = (W_{\text{Topic}} \times S_{\text{Topic}}) + (W_{\text{Method}} \times S_{\text{Method}}) + (W_{\text{Stage}} \times S_{\text{Stage}})$$

Where:
- **Score Range**: 0-100 (normalized to percentage)
- **$W_{\text{Topic}}$**: Weight for Topic Match (0-1, as percentage)
- **$W_{\text{Method}}$**: Weight for Method Match (0-1, as percentage)
- **$W_{\text{Stage}}$**: Weight for Career Stage Match (0-1, as percentage)
- **$S_{\text{Topic}}$**: Topic Match Sub-Score (0-100)
- **$S_{\text{Method}}$**: Method Match Sub-Score (0-100)
- **$S_{\text{Stage}}$**: Career Stage Match Sub-Score (0-100)

**Constraint**: $W_{\text{Topic}} + W_{\text{Method}} + W_{\text{Stage}} = 1.0$ (100%)

---

### **1.2 Weight Assignment & Justification**

Based on the professor's stakeholder interview feedback, the weights are assigned as follows:

| Component | Weight | Percentage | Justification |
|-----------|--------|------------|---------------|
| **Topic Match** ($W_{\text{Topic}}$) | **0.50** | **50%** | **Primary factor** - Research topic alignment is the foundation of collaboration. Without shared interests, complementary methods and career stages are irrelevant. |
| **Method Match** ($W_{\text{Method}}$) | **0.35** | **35%** | **Critical complementary factor** - The professor emphasized seeking complementary skill sets. This is the key differentiator for interdisciplinary success. |
| **Career Stage Match** ($W_{\text{Stage}}$) | **0.15** | **15%** | **Strategic enabler** - Important for mentorship and strategic fit, but secondary to research alignment and methodological complementarity. |

**Final Formula**:
$$\text{Compatibility Score} = (0.50 \times S_{\text{Topic}}) + (0.35 \times S_{\text{Method}}) + (0.15 \times S_{\text{Stage}})$$

**Rationale for Weight Distribution**:
1. **Topic Match (50%)**: The professor confirmed this is the **primary** consideration. No collaboration can succeed without shared research interests.
2. **Method Match (35%)**: The professor specifically emphasized seeking **complementary** (different) methods. This is the innovation driver for interdisciplinary work.
3. **Career Stage (15%)**: Strategic fit matters for mentorship and career development, but is less critical than research alignment.

---

### **1.3 Sub-Score Logic & Calculation**

#### **1.3.1 Topic Match Sub-Score ($S_{\text{Topic}}$)**

**Purpose**: Quantify alignment of research interests and topics between the user and potential collaborator.

**Data Sources**:
- **FAISS Vector Database**: Semantic similarity search on research content (abstracts, titles, keywords)
- **SDG Relevance Scores**: Two-stage AI analysis providing SDG alignment
- **Publication Keywords**: NLP-extracted keywords from publications
- **Course Curricula**: Research themes from teaching materials

**Calculation Method**:

```
S_Topic = (FAISS_Similarity × 0.40) + (SDG_Alignment × 0.35) + (Keyword_Overlap × 0.25)
```

**Detailed Components**:

1. **FAISS Similarity Score (0-100, weighted 40%)**:
   - Query: User's research profile (aggregated abstracts, titles, keywords)
   - Search: FAISS vector similarity search against potential collaborator's publications
   - Normalization: Convert cosine similarity (typically -1 to 1) to 0-100 scale
   - Formula: `FAISS_Score = (cosine_similarity + 1) × 50`
   - **Why FAISS**: High-performance semantic search captures conceptual alignment beyond keyword matching

2. **SDG Alignment Score (0-100, weighted 35%)**:
   - Extract: User's primary SDG focus areas (from publications or profile)
   - Match: Potential collaborator's SDG Relevance Scores (from two-stage AI analysis)
   - Calculation: 
     - Exact SDG match: +30 points per matching SDG (max 2 SDGs = 60 points)
     - Related SDG match: +15 points per related SDG (SDGs in same cluster, e.g., SDG 3 & 6 both health-related)
     - Bonus: +10 points if both have high SDG Relevance Scores (>0.7) for same SDG
   - Normalization: Cap at 100, scale proportionally
   - **Why SDG Scores**: Validated sustainability classification provides objective alignment metric

3. **Keyword Overlap Score (0-100, weighted 25%)**:
   - Extract: Top 10 keywords from user's publications (via NLP)
   - Extract: Top 10 keywords from potential collaborator's publications
   - Calculate: Jaccard similarity coefficient
   - Formula: `Keyword_Score = (|Keywords_User ∩ Keywords_Collaborator| / |Keywords_User ∪ Keywords_Collaborator|) × 100`
   - **Why Keywords**: Direct topic matching from publication analysis

**Example Calculation**:
- User focuses on "AI for Healthcare" (SDG 3)
- Collaborator has publications on "Machine Learning in Medical Diagnosis" (SDG 3)
- FAISS similarity: 0.85 → FAISS_Score = 92.5
- SDG Alignment: Both SDG 3, high relevance → SDG_Score = 70
- Keyword Overlap: 6/12 keywords match → Keyword_Score = 50
- **S_Topic = (92.5 × 0.40) + (70 × 0.35) + (50 × 0.25) = 37 + 24.5 + 12.5 = 74**

---

#### **1.3.2 Method Match Sub-Score ($S_{\text{Method}}$)**

**Purpose**: Quantify complementarity of research methods and skill sets. **CRITICAL**: This score rewards DIFFERENT/complementary methods, not identical methods.

**Data Sources**:
- **Faculty Records**: Grants, patents, course curricula
- **Publication Analysis**: Methodological keywords extracted via NLP
- **ORCID Profiles**: Research methods from publication metadata
- **Course Curricula**: Teaching methods indicate research approaches

**Method Classification System**:

The platform classifies researchers into method categories:

| Method Category | Examples | Complementary Pairs |
|----------------|----------|---------------------|
| **Theoretical** | Mathematical modeling, game theory, optimization | ↔ **Empirical**, **Fieldwork** |
| **Empirical/Quantitative** | Statistical analysis, econometrics, data science | ↔ **Qualitative**, **Fieldwork**, **Experimental** |
| **Qualitative** | Case studies, interviews, ethnography | ↔ **Quantitative**, **Experimental** |
| **Fieldwork** | Field experiments, surveys, observational studies | ↔ **Theoretical**, **Computational** |
| **Experimental** | Lab experiments, randomized controlled trials | ↔ **Theoretical**, **Qualitative** |
| **Computational** | Simulation, machine learning, AI | ↔ **Fieldwork**, **Qualitative** |
| **Mixed Methods** | Combination of above | ↔ **Any specialized method** |

**Calculation Method**:

```
S_Method = Complementary_Bonus × 100
```

**Detailed Logic**:

1. **Extract User's Method Profile**:
   - Analyze user's publications for methodological keywords
   - Check grants for method descriptions
   - Review course curricula for teaching methods
   - Classify into primary method category (e.g., "Theoretical")

2. **Extract Collaborator's Method Profile**:
   - Same process for potential collaborator
   - Classify into primary method category (e.g., "Empirical/Quantitative")

3. **Calculate Complementarity Score**:
   - **Perfect Complementarity (Score = 100)**: User and collaborator have complementary method categories (see table above)
     - Example: User = Theoretical, Collaborator = Empirical → Score = 100
   - **High Complementarity (Score = 75)**: One has specialized method, other has Mixed Methods
     - Example: User = Experimental, Collaborator = Mixed Methods → Score = 75
   - **Moderate Complementarity (Score = 50)**: Both have Mixed Methods, but different emphasis
     - Example: User = Mixed (theoretical emphasis), Collaborator = Mixed (empirical emphasis) → Score = 50
   - **Low Complementarity (Score = 25)**: Same method category, but different sub-approaches
     - Example: User = Quantitative (econometrics), Collaborator = Quantitative (data science) → Score = 25
   - **No Complementarity (Score = 0)**: Identical method profiles
     - Example: User = Theoretical, Collaborator = Theoretical → Score = 0

4. **Bonus Adjustments**:
   - **Skill Diversity Bonus (+10 points)**: If collaborator has skills user lacks (e.g., user has no programming, collaborator has strong computational skills)
   - **Grant Method Alignment (+5 points)**: If collaborator's grant methods complement user's needs

**Example Calculation**:
- User Profile: "Theoretical" (mathematical modeling, optimization)
- Collaborator Profile: "Empirical/Quantitative" (statistical analysis, field data)
- Base Score: Perfect complementarity → 100
- Skill Diversity: Collaborator has programming skills user lacks → +10
- **S_Method = 100** (capped at 100)

**Why This Approach**:
- The professor explicitly stated seeking **complementary** skill sets
- Interdisciplinary collaboration thrives on method diversity
- Rewarding different methods encourages cross-pollination of approaches

---

#### **1.3.3 Career Stage Match Sub-Score ($S_{\text{Stage}}$)**

**Purpose**: Quantify strategic fit based on career stage alignment for mentorship and collaboration dynamics.

**Data Sources**:
- **Faculty Records**: Tenure status, years since PhD, rank
- **Publication History**: Career trajectory (early vs. established)
- **Grants**: Career stage indicators (early career grants vs. senior investigator)

**Career Stage Classification**:

| Stage | Criteria | Typical Characteristics |
|-------|----------|-------------------------|
| **Pre-Tenure** | Assistant Professor, <7 years post-PhD | Building research portfolio, seeking mentorship |
| **Post-Tenure** | Associate/Full Professor, 7+ years post-PhD | Established researcher, potential mentor |
| **Senior** | Full Professor, 15+ years post-PhD | Research leader, extensive network |
| **Early Career** | Postdoc, Lecturer, <3 years post-PhD | Developing expertise, seeking opportunities |

**Calculation Method**:

```
S_Stage = Strategic_Fit_Score
```

**Detailed Logic**:

1. **Extract User's Career Stage**:
   - Determine from faculty records (rank, tenure status, years post-PhD)
   - Classify into stage category

2. **Extract Collaborator's Career Stage**:
   - Same process for potential collaborator

3. **Calculate Strategic Fit Score**:

   **Optimal Matches (Score = 100)**:
   - Pre-Tenure ↔ Post-Tenure (mentorship opportunity)
   - Early Career ↔ Pre-Tenure (peer collaboration with growth potential)
   - Post-Tenure ↔ Senior (strategic partnership)

   **Good Matches (Score = 75)**:
   - Pre-Tenure ↔ Pre-Tenure (peer collaboration, but limited mentorship)
   - Post-Tenure ↔ Post-Tenure (equal partnership)

   **Moderate Matches (Score = 50)**:
   - Early Career ↔ Post-Tenure (large experience gap, but possible)
   - Senior ↔ Pre-Tenure (significant gap, but mentorship value)

   **Low Matches (Score = 25)**:
   - Early Career ↔ Senior (very large gap, challenging dynamics)

   **No Match (Score = 0)**:
   - Same exact stage with identical experience (no strategic advantage)

4. **Contextual Adjustments**:
   - **Mentorship Bonus (+10 points)**: If user is pre-tenure and collaborator is post-tenure
   - **Network Bonus (+5 points)**: If collaborator has extensive collaboration network
   - **Research Stage Alignment (+5 points)**: If both are at similar research maturity levels

**Example Calculation**:
- User: Pre-Tenure Assistant Professor (3 years post-PhD)
- Collaborator: Post-Tenure Associate Professor (10 years post-PhD)
- Base Score: Optimal match (Pre-Tenure ↔ Post-Tenure) → 100
- Mentorship Bonus: User is pre-tenure, collaborator is post-tenure → +10
- **S_Stage = 100** (capped at 100)

**Why This Approach**:
- The professor mentioned strategic fit (e.g., pre-tenure with post-tenure for mentorship)
- Career stage alignment affects collaboration dynamics and outcomes
- Balances mentorship opportunities with peer collaboration

---

### **1.4 Complete Algorithm Example**

**Scenario**: User searches for collaborators for an "AI for Healthcare" project.

**User Profile**:
- Research Topic: AI, Healthcare, Machine Learning (SDG 3)
- Method: Theoretical (mathematical modeling)
- Career Stage: Pre-Tenure Assistant Professor

**Potential Collaborator A**:
- Research Topic: Machine Learning in Medical Diagnosis (SDG 3)
- Method: Empirical/Quantitative (statistical analysis, field data)
- Career Stage: Post-Tenure Associate Professor

**Calculation**:

1. **S_Topic**:
   - FAISS similarity: 0.88 → 94
   - SDG Alignment: Both SDG 3, high relevance → 70
   - Keyword Overlap: 7/13 keywords → 54
   - **S_Topic = (94 × 0.40) + (70 × 0.35) + (54 × 0.25) = 37.6 + 24.5 + 13.5 = 75.6**

2. **S_Method**:
   - User: Theoretical
   - Collaborator: Empirical/Quantitative
   - Perfect complementarity → 100
   - Skill diversity bonus → +10
   - **S_Method = 100** (capped)

3. **S_Stage**:
   - User: Pre-Tenure
   - Collaborator: Post-Tenure
   - Optimal match → 100
   - Mentorship bonus → +10
   - **S_Stage = 100** (capped)

**Final Compatibility Score**:
$$\text{Score} = (0.50 \times 75.6) + (0.35 \times 100) + (0.15 \times 100)$$
$$\text{Score} = 37.8 + 35 + 15 = 87.8$$

**Result**: **87.8/100** - Excellent match for interdisciplinary collaboration.

---

### **1.5 Algorithm Implementation Notes**

**Performance Optimization**:
- FAISS similarity search is pre-computed and cached for common queries
- Method classification uses keyword matching with NLP preprocessing
- Career stage is extracted once per faculty member and stored

**Edge Cases**:
- Missing data: If method or career stage is unknown, use average score (50) for that component
- New faculty: Use publication history and grants to infer method and stage
- External collaborators: Use ORCID profile data if available

**Scalability**:
- Algorithm runs in O(n) time where n = number of potential collaborators
- FAISS search is optimized for large-scale similarity queries
- Results are ranked and top 20 matches are returned

---

## 🎨 **TASK 2: UX DELIVERABLES & PRESENTATION PLANS**

### **2.1 Search Results Wireframe Plan**

**Purpose**: Present the Compatibility Score as the primary ranking mechanism in search results, making it immediately visible and actionable.

#### **2.1.1 Layout Structure**

```
┌─────────────────────────────────────────────────────────────────┐
│  COLLABORATION HUB - Find Research Partners                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  [Search Bar: "Search by name, topic, or keyword..."]           │
│                                                                   │
│  Filters: [SDG ▼] [Department ▼] [Method ▼] [Career Stage ▼]   │
│                                                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Rank #1                                    Compatibility │   │
│  │  ┌─────────────────────────────────────┐   Score: 87.8  │   │
│  │  │                                       │   ┌──────────┐ │   │
│  │  │  [Profile Photo]                     │   │  87.8    │ │   │
│  │  │                                       │   │  /100   │ │   │
│  │  │                                       │   └──────────┘ │   │
│  │  └─────────────────────────────────────┘   [Why?] [Contact]│   │
│  │                                                             │   │
│  │  Dr. Jane Smith                                            │   │
│  │  Associate Professor | Business Administration            │   │
│  │                                                             │   │
│  │  Research Focus: Machine Learning in Medical Diagnosis     │   │
│  │  SDG Alignment: [SDG 3: Good Health]                       │   │
│  │                                                             │   │
│  │  Method: Empirical/Quantitative | Career: Post-Tenure      │   │
│  │                                                             │   │
│  │  Recent Publications: 3 in last 2 years                     │   │
│  │  Grants: $500K active funding                              │   │
│  │                                                             │   │
│  │  ┌─────────────────────────────────────────────────────┐ │   │
│  │  │  Score Breakdown (Quick View):                       │ │   │
│  │  │  Topic Match: ████████████░░░░ 75.6 (50%)          │ │   │
│  │  │  Method Match: ████████████████ 100 (35%)           │ │   │
│  │  │  Career Stage: ████████████████ 100 (15%)           │ │   │
│  │  └─────────────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Rank #2                                    Compatibility │   │
│  │  ┌─────────────────────────────────────┐   Score: 82.3  │   │
│  │  │                                       │   ┌──────────┐ │   │
│  │  │  [Profile Photo]                     │   │  82.3    │ │   │
│  │  │                                       │   │  /100   │ │   │
│  │  │                                       │   └──────────┘ │   │
│  │  └─────────────────────────────────────┘   [Why?] [Contact]│   │
│  │  ... (similar structure)                                    │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
│  [Load More Results]                                            │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

#### **2.1.2 Key Visual Elements**

**1. Compatibility Score Display (Primary Element)**:
- **Location**: Top-right of each result card
- **Visual Design**:
  - Large, bold number (e.g., "87.8") in Illinois Blue (#13294B)
  - "/100" suffix in smaller, gray text
  - Circular or rounded rectangle background (light blue/white)
  - Border: 2px solid, color-coded by score range:
    - 80-100: Green border (Excellent match)
    - 60-79: Blue border (Good match)
    - 40-59: Yellow border (Moderate match)
    - 0-39: Gray border (Low match)
- **Size**: Prominent but not overwhelming (approximately 80px × 80px)
- **Positioning**: Fixed position relative to card, always visible

**2. Quick Score Breakdown (Inline Preview)**:
- **Location**: Bottom of each result card (collapsible section)
- **Design**: Horizontal progress bars for each sub-score
- **Color Coding**:
  - Topic Match: Blue (#13294B)
  - Method Match: Orange (#FF6B35)
  - Career Stage: Green (#4CAF50)
- **Information Display**:
  - Sub-score value (e.g., "75.6")
  - Weight percentage in parentheses (e.g., "50%")
  - Visual progress bar (filled portion represents score)

**3. Ranking Indicator**:
- **Location**: Top-left of each card
- **Design**: "Rank #1", "Rank #2", etc. in bold
- **Purpose**: Reinforce that results are sorted by Compatibility Score

**4. Action Buttons**:
- **"Why?" Button**: Opens transparent AI breakdown modal (see Section 2.2)
- **"Contact" Button**: Primary CTA, initiates collaboration request
- **Design**: Prominent, Illinois Orange (#FF6B35) for Contact, secondary style for Why?

**5. Result Card Layout**:
- **Profile Section**: Photo, name, title, department
- **Research Focus**: Brief description of research interests
- **SDG Badges**: Visual SDG icons/badges
- **Method & Career Indicators**: Icons + text (e.g., "Empirical/Quantitative | Post-Tenure")
- **Quick Stats**: Recent publications count, active grants

#### **2.1.3 Responsive Design Considerations**

- **Desktop**: 3-column grid layout, full score breakdown visible
- **Tablet**: 2-column grid, score breakdown collapsible
- **Mobile**: Single column, score prominently displayed, breakdown in modal

#### **2.1.4 Interaction Design**

- **Hover State**: Card elevates slightly, score border brightens
- **Click on Card**: Expands to show full profile details
- **Click on "Why?"**: Opens transparent AI breakdown modal
- **Sorting**: Default sort by Compatibility Score (descending), with option to sort by other criteria

---

### **2.2 "Transparent AI" Breakdown Plan (Modal Pop-up)**

**Purpose**: Provide detailed, explainable breakdown of the Compatibility Score to build trust and transparency. This is the "Why this score?" evidence.

#### **2.2.1 Modal Structure**

```
┌─────────────────────────────────────────────────────────────────┐
│  Compatibility Score Breakdown                    [X Close]     │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Overall Compatibility Score                            │   │
│  │                                                           │   │
│  │            ┌──────────────┐                              │   │
│  │            │              │                              │   │
│  │            │     87.8     │                              │   │
│  │            │    /100      │                              │   │
│  │            │              │                              │   │
│  │            └──────────────┘                              │   │
│  │                                                           │   │
│  │  Excellent Match for Interdisciplinary Collaboration     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Topic Match Score: 75.6 (Weight: 50%)                   │   │
│  │  ─────────────────────────────────────────────────────── │   │
│  │                                                           │   │
│  │  ████████████░░░░░░░░  75.6/100                         │   │
│  │                                                           │   │
│  │  Breakdown:                                              │   │
│  │  • FAISS Semantic Similarity: 94/100 (40% of Topic)      │   │
│  │    └─ Your research: "AI for Healthcare"                │   │
│  │    └─ Their research: "Machine Learning in Medical..." │   │
│  │    └─ Similarity: 0.88 (high conceptual alignment)     │   │
│  │                                                           │   │
│  │  • SDG Alignment: 70/100 (35% of Topic)                  │   │
│  │    └─ Your SDG Focus: SDG 3 (Good Health)               │   │
│  │    └─ Their SDG Focus: SDG 3 (Good Health)             │   │
│  │    └─ Relevance Scores: Both >0.7 (high alignment)      │   │
│  │                                                           │   │
│  │  • Keyword Overlap: 54/100 (25% of Topic)               │   │
│  │    └─ Shared Keywords: 7 out of 13 total                │   │
│  │    └─ Matching: AI, Healthcare, Machine Learning, ...   │   │
│  │                                                           │   │
│  │  Evidence:                                               │   │
│  │  📄 3 publications on similar topics                     │   │
│  │  🎯 Both focus on SDG 3 (Good Health)                    │   │
│  │  🔗 High semantic similarity in research content         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Method Match Score: 100 (Weight: 35%)                  │   │
│  │  ─────────────────────────────────────────────────────── │   │
│  │                                                           │   │
│  │  ████████████████████  100/100                           │   │
│  │                                                           │   │
│  │  Breakdown:                                              │   │
│  │  • Your Method Profile: Theoretical                      │   │
│  │    └─ Mathematical modeling, optimization                │   │
│  │    └─ Based on: 5 publications, 2 grants                 │   │
│  │                                                           │   │
│  │  • Their Method Profile: Empirical/Quantitative          │   │
│  │    └─ Statistical analysis, field data collection         │   │
│  │    └─ Based on: 8 publications, 3 grants                │   │
│  │                                                           │   │
│  │  • Complementarity Assessment:                           │   │
│  │    ✅ Perfect Method Complementarity                     │   │
│  │    ✅ Theoretical + Empirical = Strong Interdisciplinary │   │
│  │    ✅ Skill Diversity: They have programming skills     │   │
│  │                                                           │   │
│  │  Why This Matters:                                       │   │
│  │  Your theoretical models can be validated with their     │   │
│  │  empirical data, creating a complete research pipeline.   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Career Stage Match Score: 100 (Weight: 15%)            │   │
│  │  ─────────────────────────────────────────────────────── │   │
│  │                                                           │   │
│  │  ████████████████████  100/100                           │   │
│  │                                                           │   │
│  │  Breakdown:                                              │   │
│  │  • Your Career Stage: Pre-Tenure Assistant Professor    │   │
│  │    └─ 3 years post-PhD                                   │   │
│  │                                                           │   │
│  │  • Their Career Stage: Post-Tenure Associate Professor  │   │
│  │    └─ 10 years post-PhD                                  │   │
│  │                                                           │   │
│  │  • Strategic Fit: Optimal Match                           │   │
│  │    ✅ Mentorship Opportunity                              │   │
│  │    ✅ Established Network Access                          │   │
│  │    ✅ Career Development Support                           │   │
│  │                                                           │   │
│  │  Why This Matters:                                       │   │
│  │  This collaboration provides mentorship while you build   │   │
│  │  your research portfolio, and they gain fresh            │   │
│  │  perspectives from your theoretical expertise.            │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Recommended Next Steps                                  │   │
│  │  ─────────────────────────────────────────────────────── │   │
│  │  • Review their recent publications                       │   │
│  │  • Explore their active grants                            │   │
│  │  • [Contact Researcher] button                           │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
│  [Close] [Contact Researcher]                                   │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

#### **2.2.2 Key Design Elements**

**1. Overall Score Display**:
- Large, centered score (87.8/100)
- Color-coded background (green for 80+, blue for 60-79, etc.)
- Brief interpretation text ("Excellent Match for Interdisciplinary Collaboration")

**2. Detailed Breakdown Sections**:
- Each sub-score (Topic, Method, Stage) in its own expandable section
- Progress bar visualization
- Weight percentage clearly displayed
- Component-level breakdown (e.g., FAISS, SDG, Keywords for Topic)
- Evidence citations (publication counts, grant info, etc.)

**3. Explainability Features**:
- **"Why This Matters"** section for each sub-score
- **Evidence** section with specific data points
- **Data Sources** indicated (e.g., "Based on: 5 publications, 2 grants")
- **Transparency**: Show how each component contributes to the final score

**4. Visual Hierarchy**:
- Most important information (overall score) at top
- Sub-scores in order of weight (Topic → Method → Stage)
- Action items at bottom

**5. Interactive Elements**:
- Expandable sections (can collapse/expand each sub-score)
- Links to evidence (click to view publications, grants)
- Direct action buttons (Contact Researcher)

#### **2.2.3 Content Guidelines**

**For Each Sub-Score Section, Include**:
1. **Score Value & Weight**: Clear display of score and its contribution
2. **Component Breakdown**: How the sub-score was calculated
3. **Evidence**: Specific data points supporting the score
4. **Interpretation**: What the score means in practical terms
5. **Why It Matters**: Explanation of why this dimension is important

**Language Style**:
- Clear, non-technical language
- Avoid jargon, explain technical terms
- Use bullet points for scannability
- Include specific examples and numbers

---

### **2.3 Network Graph Integration Plan**

**Purpose**: Visualize Compatibility Scores on the Network Graph to make interdisciplinary opportunities instantly visible through visual encoding.

#### **2.3.1 Network Graph Structure**

**Node Types**:
- **User Node**: Central node (larger, highlighted)
- **Potential Collaborator Nodes**: Other researchers
- **SDG Nodes**: Optional, for SDG-based clustering

**Edge Types**:
- **Compatibility Edges**: Connections between user and potential collaborators
- **Collaboration Edges**: Existing collaborations (if data available)

#### **2.3.2 Visual Encoding of Compatibility Score**

**1. Edge Thickness (Primary Encoding)**:
- **Thicker edges** = Higher Compatibility Score
- **Thinner edges** = Lower Compatibility Score
- **Scale**: 
  - 80-100: 5px edge width (thickest, most visible)
  - 60-79: 3px edge width (medium)
  - 40-59: 2px edge width (thin)
  - 0-39: 1px edge width (very thin, barely visible)

**2. Edge Color/Brightness (Secondary Encoding)**:
- **Brighter, more saturated colors** = Higher Compatibility Score
- **Darker, less saturated colors** = Lower Compatibility Score
- **Color Scale**:
  - 80-100: Bright Illinois Orange (#FF6B35) or Green (#4CAF50)
  - 60-79: Medium Illinois Blue (#13294B)
  - 40-59: Light gray (#CCCCCC)
  - 0-39: Very light gray (#E0E0E0)

**3. Edge Opacity (Tertiary Encoding)**:
- **Higher opacity** = Higher Compatibility Score
- **Lower opacity** = Lower Compatibility Score
- **Opacity Scale**:
  - 80-100: 100% opacity (fully opaque)
  - 60-79: 70% opacity
  - 40-59: 40% opacity
  - 0-39: 20% opacity

**4. Node Size (Optional)**:
- Larger nodes for collaborators with higher Compatibility Scores
- Helps identify top matches at a glance

#### **2.3.3 Network Graph Layout**

```
                    [SDG 3 Node]
                         │
                         │ (thick, bright edge)
                         │
                    [Collaborator A]
                    (Score: 87.8)
                         │
                         │ (thick, bright edge)
                         │
              [User Node] ──────── [Collaborator B]
              (Central)            (Score: 82.3)
                         │
                         │ (medium edge)
                         │
                    [Collaborator C]
                    (Score: 65.1)
                         │
                         │ (thin, dim edge)
                         │
                    [Collaborator D]
                    (Score: 45.2)
```

**Layout Algorithm**:
- **Force-directed layout**: Nodes positioned based on Compatibility Score
- **Clustering**: Group collaborators by SDG or department
- **User-centric**: User node at center, collaborators positioned around

#### **2.3.4 Interactive Features**

**1. Hover Interactions**:
- **Hover on Edge**: Display Compatibility Score in tooltip
- **Hover on Node**: Highlight connected edges, show collaborator info

**2. Click Interactions**:
- **Click on Edge**: Open Compatibility Score breakdown modal
- **Click on Node**: Navigate to collaborator profile page

**3. Filtering**:
- **Slider Filter**: Filter edges by minimum Compatibility Score (e.g., show only scores >70)
- **Dynamic Updates**: Graph updates in real-time as filters change

**4. Legend**:
- **Edge Thickness Legend**: Show examples of different edge widths
- **Color Legend**: Show color scale for Compatibility Scores
- **Score Range Labels**: "Excellent (80-100)", "Good (60-79)", etc.

#### **2.3.5 Visual Design Specifications**

**Node Design**:
- **User Node**: 
  - Size: 40px diameter
  - Color: Illinois Blue (#13294B)
  - Border: 3px, white
  - Icon: User profile photo or initials
- **Collaborator Nodes**:
  - Size: 30px diameter (scaled by Compatibility Score)
  - Color: Illinois Orange (#FF6B35) or department color
  - Border: 2px, white
  - Icon: Profile photo or department icon

**Edge Design**:
- **Style**: Curved lines (bezier curves) for better visual flow
- **Arrowheads**: Optional, pointing from user to collaborator
- **Labels**: Optional score labels on edges (for top matches only)

**Background**:
- Light gray or white background
- Grid lines optional (subtle)
- SDG cluster areas (optional, shaded regions)

#### **2.3.6 Implementation Notes**

**Performance Considerations**:
- Limit displayed nodes to top 50 matches for performance
- Use edge bundling for dense networks
- Implement level-of-detail (LOD) rendering: show full detail on zoom, simplified on overview

**Accessibility**:
- Color-blind friendly: Use both color and thickness encoding
- Keyboard navigation support
- Screen reader support: Alt text for nodes and edges

**Integration with Search Results**:
- Clicking a node in the network graph highlights corresponding result in search list
- Filtering search results updates the network graph
- Synchronized selection between graph and list views

---

## 📊 **PRESENTATION SUMMARY**

### **Key Points for Judges**

1. **Algorithm Rigor**:
   - Weighted formula based on stakeholder-validated criteria
   - Three sub-scores with clear, explainable logic
   - Method score specifically rewards complementarity (different methods)

2. **Transparency**:
   - "Transparent AI" breakdown provides full explainability
   - Evidence-based scoring with data citations
   - Clear visualization of score components

3. **User Experience**:
   - Score is primary ranking mechanism (visible, actionable)
   - Network graph makes opportunities instantly visible
   - Seamless integration across all Collaboration Hub views

4. **Innovation**:
   - Proactive suggestion (not just search)
   - Quantified compatibility (not subjective)
   - Interdisciplinary focus (method complementarity)

---

## ✅ **IMPLEMENTATION CHECKLIST**

### **Algorithm Implementation**:
- [ ] Implement FAISS similarity search integration
- [ ] Build method classification system
- [ ] Extract career stage from faculty records
- [ ] Calculate all three sub-scores
- [ ] Combine with weighted formula
- [ ] Test with sample user profiles

### **UX Implementation**:
- [ ] Build search results page with score display
- [ ] Create transparent AI breakdown modal
- [ ] Integrate network graph with score visualization
- [ ] Implement filtering and sorting by score
- [ ] Add responsive design for mobile/tablet
- [ ] Test user interactions and flows

### **Presentation Preparation**:
- [ ] Create wireframe mockups for all three views
- [ ] Prepare example scenarios with score breakdowns
- [ ] Document algorithm justification
- [ ] Create visual design specifications
- [ ] Prepare demo data and test cases

---

**This document provides the complete specification for finalizing and presenting the Collaboration Compatibility Score solution.** 🎯


