# Collaboration Hub MVP & Presentation Guide
## Complete Step-by-Step Implementation Strategy

---

## 🎯 **DECISION: POWER BI vs PYTHON**

### **Recommendation: Use BOTH (Hybrid Approach)**

**Why Hybrid:**
- **Power BI**: Best for **presentation** and **interactive demos** during the case competition
- **Python**: Best for **data processing** and **algorithm implementation** (compatibility scoring)
- **Combined**: Python prepares the data → Power BI visualizes it beautifully

### **Power BI Advantages for Presentation:**
✅ **Visual Appeal**: Professional, polished dashboards that impress judges  
✅ **Interactive**: Click-through demos during presentation  
✅ **Fast Setup**: Can build in 1-2 days  
✅ **No Coding Required**: Visual drag-and-drop interface  
✅ **Export to PowerPoint**: Easy to embed in presentation slides  

### **Python Advantages for Algorithm:**
✅ **Flexible**: Can implement complex matching algorithms  
✅ **Data Processing**: Clean and transform your CSV data  
✅ **Network Graphs**: Create network visualizations (if needed)  
✅ **Reproducible**: Scripts can be shared and run by judges  

### **Final Recommendation:**
**Use Python to prepare the matching data, then import into Power BI for visualization and presentation.**

---

## 📊 **STEP 1: BUILD THE MATCHING ALGORITHM (FIRST TIME ONLY)**

### **What You Have:**
1. **`for distribution case competition filtered_publications.csv`** - Main publication data (ONLY FILE YOU HAVE)

### **What You Need to Create:**
Since you don't have the matching files yet, you need to **build the algorithm first**:

**Run this script:**
```bash
python build_collab_hub_from_scratch.py
```

This script will:
1. ✅ Extract researcher profiles from publications
2. ✅ Infer research methods from keywords/abstracts
3. ✅ Calculate career stages from publication years
4. ✅ Calculate SDG alignments
5. ✅ Calculate topic similarity (SDG + keywords)
6. ✅ Calculate method complementarity (different = higher)
7. ✅ Calculate career stage fit
8. ✅ Generate compatibility scores
9. ✅ Create all output files

**Output Files Created:**
- `faculty_matches.csv` - All compatibility scores
- `best_faculty_match.csv` - Top 50 matches
- `Researcher_Profiles_For_PowerBI.csv` - Researcher profiles
- `network_graph_data.csv` - Network visualization data
- `Collab_Matches_For_PowerBI.csv` - Power BI ready format

**Time Required:** ~5-10 minutes (depending on data size)

**After running the script, proceed to Step 2 below.**

---

## 🚀 **STEP 2: BUILD THE MVP (3-Day Plan)**

### **DAY 1: Build Algorithm & Power BI Setup**

#### **Morning: Build Matching Algorithm (IF FIRST TIME)**

**Task 1.1: Run the Matching Algorithm Script**

If you haven't run it yet:
```bash
python build_collab_hub_from_scratch.py
```

This creates all the matching files you need. Wait for it to complete (~5-10 minutes).

**Task 1.2: Verify Output Files**

Check that these files were created:
- `faculty_matches.csv`
- `Collab_Matches_For_PowerBI.csv`
- `Researcher_Profiles_For_PowerBI.csv`

**Task 1.3: Review Sample Matches**

You need to create a table that Power BI can easily visualize:

```python
# Create a simplified matching table for Power BI
powerbi_matches = matches[[
    'Faculty_A_Name', 'Faculty_A_Dept', 'Faculty_A_Method', 'Faculty_A_Stage',
    'Faculty_B_Name', 'Faculty_B_Dept', 'Faculty_B_Method', 'Faculty_B_Stage',
    'Total_Score', 'Topic_Score', 'Method_Score', 'Stage_Score',
    'SDG', 'Topic_Reason', 'Method_Reason', 'Stage_Reason'
]].copy()

# Add match quality categories
def categorize_match(score):
    if score >= 85:
        return "Excellent Match"
    elif score >= 70:
        return "Good Match"
    elif score >= 55:
        return "Moderate Match"
    else:
        return "Low Match"

powerbi_matches['Match_Quality'] = powerbi_matches['Total_Score'].apply(categorize_match)

# Save for Power BI
powerbi_matches.to_csv('Collab_Matches_For_PowerBI.csv', index=False)
print("✓ Saved Power BI matching table")
```

**Task 1.3: Create Researcher Profile Table**

```python
# Load publications to get researcher profiles
publications = pd.read_csv('for distribution case competition filtered_publications.csv')

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

# Calculate career stage (simplified)
current_year = 2024
researcher_profiles['years_active'] = current_year - researcher_profiles['first_publication']
researcher_profiles['career_stage'] = researcher_profiles['years_active'].apply(
    lambda x: 'Senior' if x > 15 else ('Post-Tenure' if x > 7 else 'Pre-Tenure')
)

# Save
researcher_profiles.to_csv('Researcher_Profiles_For_PowerBI.csv', index=False)
print("✓ Saved researcher profiles")
```

#### **Afternoon: Set Up Power BI**

**Task 1.4: Import Data into Power BI**

1. Open **Power BI Desktop**
2. Click **Get Data** → **Text/CSV**
3. Import these files:
   - `Collab_Matches_For_PowerBI.csv` (your matching data)
   - `Researcher_Profiles_For_PowerBI.csv` (researcher info)
   - `Publications_cleaned.csv` (publication details)
   - `sdg_lookup.csv` (SDG names)

4. For each file:
   - Click **Transform Data** to verify
   - Click **Close & Apply**

**Task 1.5: Create Relationships**

1. Go to **Model** view (left sidebar)
2. Create relationships:
   - `Collab_Matches[Faculty_A_Name]` → `Researcher_Profiles[name]` (Many-to-One)
   - `Collab_Matches[Faculty_B_Name]` → `Researcher_Profiles[name]` (Many-to-One)
   - `Collab_Matches[SDG]` → `sdg_lookup[SDG ID]` (Many-to-One)

3. Set **Cross-filter direction** to **Both** for all relationships

---

### **DAY 2: Build Core Visualizations**

#### **Morning: Compatibility Score Dashboard**

**Visual 1: Match Quality Distribution**

1. Click **Pie chart** visual
2. **Legend**: `Match_Quality`
3. **Values**: `Total_Score` (Count)
4. **Format**:
   - Title: "Match Quality Distribution"
   - Colors: Green (Excellent), Blue (Good), Yellow (Moderate), Gray (Low)

**Visual 2: Top Matches Table**

1. Click **Table** visual
2. **Columns**:
   - `Faculty_A_Name`
   - `Faculty_B_Name`
   - `Total_Score`
   - `Topic_Score`
   - `Method_Score`
   - `Stage_Score`
   - `SDG` (from relationship)
3. **Sort**: By `Total_Score` (Descending)
4. **Filter**: Show top 20 matches
5. **Format**:
   - Title: "Top Collaboration Matches"
   - Conditional formatting on `Total_Score`:
     - 85-100: Green background
     - 70-84: Light green
     - 55-69: Yellow
     - <55: Gray

**Visual 3: Score Breakdown Bar Chart**

1. Click **Stacked bar chart**
2. **Axis**: `Faculty_A_Name` (or create a "Match Pair" column)
3. **Values**:
   - `Topic_Score` (Blue)
   - `Method_Score` (Orange)
   - `Stage_Score` (Green)
4. **Format**:
   - Title: "Compatibility Score Breakdown"
   - Legend: Show weights (50%, 35%, 15%)

**Visual 4: Method Complementarity Matrix**

1. Click **Matrix** visual
2. **Rows**: `Faculty_A_Method`
3. **Columns**: `Faculty_B_Method`
4. **Values**: `Total_Score` (Average)
5. **Format**:
   - Title: "Method Complementarity Matrix"
   - Conditional formatting: Color scale (green = high, red = low)
   - **Key Insight**: Show that Theoretical + Empirical = High scores

**Visual 5: SDG-Based Matching**

1. Click **Bar chart**
2. **Axis**: `SDG Name` (from sdg_lookup relationship)
3. **Values**: `Total_Score` (Average)
4. **Format**:
   - Title: "Average Compatibility by SDG"
   - Sort: Descending

#### **Afternoon: Interactive Search Interface**

**Visual 6: Researcher Search & Filter**

1. Click **Slicer** visual
2. **Field**: `Faculty_A_Name` (or create a searchable list)
3. **Format**: Search box enabled

**Visual 7: Match Details Card**

1. Click **Card** visual
2. **Fields**:
   - `Total_Score` (Average)
   - `Topic_Score` (Average)
   - `Method_Score` (Average)
   - `Stage_Score` (Average)
3. **Format**: Large numbers, clear labels

**Visual 8: Match Reasons Text Box**

1. Click **Text box** or **Card** visual
2. Show `Method_Reason` and `Topic_Reason` when a match is selected
3. **Format**: Readable text, highlight "Complementary" methods

---

### **DAY 3: Network Graph & Presentation Prep**

#### **Morning: Network Visualization**

**Option A: Power BI Network Graph (If Available)**

1. Install **Network Navigator** custom visual (from AppSource)
2. **Nodes**: Researchers (from `Researcher_Profiles`)
3. **Links**: Matches (from `Collab_Matches`)
4. **Node Size**: `total_publications`
5. **Link Thickness**: `Total_Score`
6. **Link Color**: `Match_Quality`

**Option B: Python Network Graph (Export to Image)**

```python
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load matches
matches = pd.read_csv('faculty_matches.csv')
network_data = pd.read_csv('network_graph_data.csv')

# Create graph
G = nx.Graph()

# Add nodes
for _, row in matches.iterrows():
    G.add_node(row['Faculty_A_Name'], dept=row['Faculty_A_Dept'])
    G.add_node(row['Faculty_B_Name'], dept=row['Faculty_B_Dept'])

# Add edges with weights
for _, row in network_data.iterrows():
    G.add_edge(row['Source'], row['Target'], weight=row['Score'])

# Draw network
plt.figure(figsize=(20, 15))
pos = nx.spring_layout(G, k=2, iterations=50)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue', alpha=0.7)

# Draw edges (thickness = score)
edges = G.edges()
weights = [G[u][v]['weight'] for u, v in edges]
nx.draw_networkx_edges(G, pos, width=[w/10 for w in weights], alpha=0.5)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=8)

plt.title("Collaboration Network - Method Complementarity", size=16)
plt.axis('off')
plt.tight_layout()
plt.savefig('collaboration_network.png', dpi=300, bbox_inches='tight')
print("✓ Saved network graph")
```

#### **Afternoon: Presentation Dashboard Layout**

**Create Final Dashboard Page:**

```
┌─────────────────────────────────────────────────────────┐
│  COLLABORATION HUB - Compatibility Matching            │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  [Search: Faculty Name...]  [SDG Filter ▼] [Dept ▼]    │
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │ Total Matches│  │ Avg Score    │  │ Top Quality  │ │
│  │    1,234     │  │    72.5      │  │    85%       │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Top Collaboration Matches (Table)                │  │
│  │  [Shows top 20 matches with scores]              │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
│  ┌──────────────────┐  ┌──────────────────────────────┐ │
│  │ Match Quality    │  │ Score Breakdown             │ │
│  │ Distribution     │  │ (Stacked Bar)                 │ │
│  │ (Pie Chart)     │  │                              │ │
│  └──────────────────┘  └──────────────────────────────┘ │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Method Complementarity Matrix                  │  │
│  │  [Shows Theoretical + Empirical = High]         │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Network Graph (or Image)                        │  │
│  │  [Shows collaboration opportunities]            │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

## 📝 **STEP 3: PRESENTATION STRATEGY**

### **Presentation Structure (15-20 minutes)**

#### **Slide 1: Problem Statement**
- "Researchers struggle to find interdisciplinary collaborators"
- "Current methods: word-of-mouth, department directories"
- "Need: Data-driven matching based on research alignment"

#### **Slide 2: Solution Overview**
- **Collaboration Hub**: AI-powered compatibility matching
- **Three Critical Criteria** (from Prof. Fei):
  1. **Research Topic** (50% weight) - Shared interests
  2. **Method Complementarity** (35% weight) - **DIFFERENT methods**
  3. **Career Stage** (15% weight) - Strategic fit

#### **Slide 3: Algorithm Logic**
- Show the formula: `Score = (0.50 × Topic) + (0.35 × Method) + (0.15 × Stage)`
- **Key Innovation**: Method complementarity rewards DIFFERENT methods
- Example: Theoretical + Empirical = 100, Theoretical + Theoretical = 0

#### **Slide 4: Live Demo - Power BI Dashboard**
- **Show**: Top matches table
- **Click**: On a high-scoring match (e.g., 87.8)
- **Explain**: Why it's a good match:
  - Topic: Both focus on SDG 3 (Health)
  - Method: Theoretical + Empirical (complementary!)
  - Stage: Pre-Tenure + Post-Tenure (mentorship)

#### **Slide 5: Method Complementarity Matrix**
- **Show**: Matrix visualization
- **Highlight**: Theoretical + Empirical = High scores
- **Explain**: "We reward complementary methods, not identical ones"

#### **Slide 6: Network Visualization**
- **Show**: Network graph
- **Explain**: Thick edges = high compatibility
- **Point out**: Interdisciplinary opportunities

#### **Slide 7: Impact & Next Steps**
- **Quantify**: "X potential collaborations identified"
- **Value**: "Enables proactive matching, not just search"
- **Future**: Integration with university systems

### **Key Talking Points**

1. **"Proactive, Not Reactive"**
   - "We don't just provide search - we proactively suggest opportunities"

2. **"Method Complementarity"**
   - "The professor emphasized seeking complementary (different) methods. Our algorithm rewards this."

3. **"Transparent & Explainable"**
   - "Users understand why matches are good through detailed breakdowns"

4. **"Data-Driven"**
   - "Based on actual publication data, SDG alignments, and research methods"

---

## 🎨 **STEP 4: POWER BI MEASURES (If Needed)**

If you need to create additional measures in Power BI:

### **Measure 1: Total Matches**
```DAX
Total Matches = COUNTROWS('Collab_Matches')
```

### **Measure 2: Average Compatibility Score**
```DAX
Avg Compatibility Score = AVERAGE('Collab_Matches'[Total_Score])
```

### **Measure 3: Excellent Matches Count**
```DAX
Excellent Matches = 
CALCULATE(
    COUNTROWS('Collab_Matches'),
    'Collab_Matches'[Total_Score] >= 85
)
```

### **Measure 4: Method Complementarity Rate**
```DAX
Method Complementarity Rate = 
DIVIDE(
    CALCULATE(
        COUNTROWS('Collab_Matches'),
        'Collab_Matches'[Method_Score] >= 75
    ),
    [Total Matches],
    0
) * 100
```

---

## ✅ **FINAL CHECKLIST**

### **Before Presentation:**

- [ ] All data imported into Power BI
- [ ] Relationships created and verified
- [ ] Top matches table shows correct data
- [ ] Method complementarity matrix displays correctly
- [ ] Network graph created (or image ready)
- [ ] Dashboard is visually appealing (Illinois colors)
- [ ] Can click through and filter during demo
- [ ] Presentation slides prepared
- [ ] Example match selected for live demo
- [ ] Talking points memorized

### **Key Validation:**

- [ ] Method Match rewards DIFFERENT methods (Theoretical + Empirical = High)
- [ ] Topic Match is primary (50% weight visible)
- [ ] Career Stage enables strategic fit (15% weight)
- [ ] Scores are explainable (can show breakdown)

---

## 💡 **QUICK START (If Time is Limited)**

### **2-Hour MVP:**

1. **30 min**: Load `faculty_matches.csv` into Power BI
2. **30 min**: Create top matches table
3. **30 min**: Create method complementarity matrix
4. **30 min**: Create score breakdown chart
5. **Done!** You have a working demo

### **1-Day Polish:**

- Add network graph
- Add filters and search
- Format with Illinois colors
- Create presentation slides
- Practice demo

---

## 🎯 **WHY THIS APPROACH WORKS**

1. **Leverages Existing Work**: You already have the matching algorithm in `faculty_matches.csv`
2. **Fast to Build**: Power BI visualizations are quick to create
3. **Impressive Demo**: Interactive dashboard wows judges
4. **Aligned with Requirements**: Directly addresses Prof. Fei's three criteria
5. **Professional**: Looks polished and production-ready

---

## 📚 **RESOURCES**

- **Power BI Desktop**: Free download from Microsoft
- **Custom Visuals**: Network Navigator (if needed)
- **Python Scripts**: Use for data prep and network graphs
- **Your Data**: `faculty_matches.csv` is your goldmine!

---

**Follow this guide to build a compelling Collaboration Hub MVP in 3 days!** 🚀

