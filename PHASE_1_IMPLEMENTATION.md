# Phase 1 Implementation Guide - Quick Wins

## 🎯 **Phase 1 Features to Build**

1. **SDG Gap Analysis Tool**
2. **Research Impact Score Dashboard**
3. **Enhanced Collaboration Network**

---

## 📊 **Feature 1: SDG Gap Analysis Tool**

### **Purpose**: Identify which SDGs are under-researched and show opportunities

### **Step 1: Create Gap Analysis Measure**

**Create this measure in Publications table:**

```DAX
SDG Coverage Score = 
VAR TotalSDGs = 17
VAR CoveredSDGs = 
    CALCULATE(
        DISTINCTCOUNT('SDG_Mappings'[SDG ID]),
        Publications[is_sustain] = TRUE()
    )
RETURN
DIVIDE(CoveredSDGs, TotalSDGs, 0) * 100
```

**Create measure for each SDG's coverage:**

```DAX
SDG Coverage by SDG = 
VAR SelectedSDG = SELECTEDVALUE('sdg_lookup'[SDG ID])
VAR SDGCount = 
    CALCULATE(
        COUNTROWS('SDG_Mappings'),
        'SDG_Mappings'[SDG ID] = SelectedSDG
    )
VAR TotalPublications = [Total Publications]
VAR CoveragePercent = DIVIDE(SDGCount, TotalPublications, 0) * 100
RETURN
CoveragePercent
```

**Create gap indicator:**

```DAX
SDG Gap Status = 
VAR Coverage = [SDG Coverage by SDG]
RETURN
SWITCH(
    TRUE(),
    Coverage < 2, "Critical Gap",
    Coverage < 5, "Significant Gap",
    Coverage < 10, "Moderate Gap",
    Coverage >= 10, "Well Covered"
)
```

### **Step 2: Create Gap Analysis Matrix**

1. **Click Matrix visual**
2. **Fields**:
   - **Rows**: `SDG Name` (from sdg_lookup)
   - **Values**: 
     - `Publications by SDG` measure
     - `SDG Coverage by SDG` measure
     - `SDG Gap Status` measure

3. **Format as Heatmap**:
   - **Format pane** → **"Values"** → **"Conditional formatting"**
   - **Background color**: ON
   - **Color scale**:
     - **Minimum**: Red (Critical Gap)
     - **Center**: Yellow (Moderate Gap)
     - **Maximum**: Green (Well Covered)

4. **Add Title**:
   - **Format pane** → **"General"**
   - **Title**: ON
   - **Title text**: "SDG Gap Analysis: Research Coverage Opportunities"
   - **Font size**: 18

### **Step 3: Create Gap Summary Cards**

**Create 4 cards showing gap categories:**

1. **Critical Gap Count**:
```DAX
Critical Gaps = 
CALCULATE(
    DISTINCTCOUNT('sdg_lookup'[SDG ID]),
    FILTER(
        ALL('sdg_lookup'),
        [SDG Coverage by SDG] < 2
    )
)
```

2. **Significant Gap Count**:
```DAX
Significant Gaps = 
CALCULATE(
    DISTINCTCOUNT('sdg_lookup'[SDG ID]),
    FILTER(
        ALL('sdg_lookup'),
        [SDG Coverage by SDG] >= 2 && [SDG Coverage by SDG] < 5
    )
)
```

3. **Well Covered Count**:
```DAX
Well Covered SDGs = 
CALCULATE(
    DISTINCTCOUNT('sdg_lookup'[SDG ID]),
    FILTER(
        ALL('sdg_lookup'),
        [SDG Coverage by SDG] >= 10
    )
)
```

**Note**: These measures use FILTER correctly because FILTER returns a table, and CALCULATE can use that filtered table.

**Create cards for each measure**

### **Step 4: Create Opportunity Recommendations**

**Create a table showing recommendations:**

1. **Click Table visual**
2. **Columns**:
   - `SDG Name`
   - `SDG Coverage by SDG` (as percentage)
   - `SDG Gap Status`
   - `Publications by SDG`

3. **Add calculated column for recommendations:**
```DAX
Recommendation = 
VAR Status = [SDG Gap Status]
VAR SDGName = SELECTEDVALUE('sdg_lookup'[SDG Name])
RETURN
SWITCH(
    Status,
    "Critical Gap", SDGName & " has critical research gap. Consider strategic investment.",
    "Significant Gap", SDGName & " shows opportunity for growth. Potential for expansion.",
    "Moderate Gap", SDGName & " has moderate coverage. Monitor for opportunities.",
    "Well Covered", SDGName & " is well-researched. Consider maintaining focus."
)
```

4. **Format table**:
   - Conditional formatting for Gap Status column
   - Sort by coverage (lowest first - biggest gaps)

---

## 📈 **Feature 2: Research Impact Score**

### **Purpose**: Quantify research impact with a 0-100 score

### **Step 1: Create Impact Score Components**

**Component 1: Journal Tier Score (0-40 points)**
```DAX
Journal Tier Score = 
VAR FTScore = IF(MAX(Publications[Financial Times_flag]) = TRUE(), 20, 0)
VAR UTDScore = IF(MAX(Publications[UT Dallas_flag]) = TRUE(), 20, 0)
RETURN
FTScore + UTDScore
```

**Component 2: SDG Alignment Score (0-30 points)**
```DAX
SDG Alignment Score = 
VAR SDGCount = 
    CALCULATE(
        DISTINCTCOUNT('SDG_Mappings'[SDG ID]),
        RELATED(Publications[is_sustain]) = TRUE()
    )
RETURN
MIN(SDGCount * 10, 30)  // Max 30 points for 3+ SDGs
```

**Component 3: Recency Score (0-20 points)**
```DAX
Recency Score = 
VAR CurrentYear = YEAR(TODAY())
VAR PubYear = MAX(Publications[publication_year])
VAR YearsAgo = CurrentYear - PubYear
RETURN
SWITCH(
    TRUE(),
    YearsAgo <= 2, 20,
    YearsAgo <= 5, 15,
    YearsAgo <= 10, 10,
    5
)
```

**Component 4: Sustainability Score (0-10 points)**
```DAX
Sustainability Score = 
IF(MAX(Publications[is_sustain]) = TRUE(), 10, 0)
```

### **Step 2: Create Total Impact Score**

```DAX
Research Impact Score = 
[Journal Tier Score] + 
[SDG Alignment Score] + 
[Recency Score] + 
[Sustainability Score]
```

### **Step 3: Create Impact Score Visualizations**

**Visualization 1: Impact Score Distribution**

1. **Click Histogram or Bar Chart**
2. **X-axis**: `Research Impact Score` (binned into ranges: 0-20, 21-40, 41-60, 61-80, 81-100)
3. **Y-axis**: Count of publications
4. **Title**: "Research Impact Score Distribution"

**Visualization 2: Top Researchers by Impact**

1. **Click Table or Bar Chart**
2. **Rows**: `name` (from Publications)
3. **Values**: Average of `Research Impact Score`
4. **Sort**: Descending
5. **Title**: "Top Researchers by Impact Score"

**Visualization 3: Impact Score by Department**

1. **Click Bar Chart**
2. **Y-axis**: `department`
3. **X-axis**: Average of `Research Impact Score`
4. **Title**: "Average Impact Score by Department"

**Visualization 4: Impact Score Card**

1. **Click Card**
2. **Value**: Average of `Research Impact Score`
3. **Title**: "Average Research Impact Score"
4. **Format**: Show as number with 1 decimal

### **Step 4: Create Impact Score Breakdown**

**Create a stacked bar chart showing score components:**

1. **Click Stacked Bar Chart**
2. **Y-axis**: `title` (top 10 publications)
3. **Values**:
   - `Journal Tier Score`
   - `SDG Alignment Score`
   - `Recency Score`
   - `Sustainability Score`
4. **Title**: "Impact Score Breakdown - Top Publications"
5. **Legend**: Shows each component

---

## 🤝 **Feature 3: Enhanced Collaboration Network**

### **Purpose**: Advanced network visualization showing research connections

### **Step 1: Install Network Visual**

1. In **Visualizations pane**, click **"..."** (Get more visuals)
2. Search for **"Network Navigator"** or **"Chord Chart"**
3. Click **"Add"** to install

### **Step 2: Create Department-SDG Network**

**Option A: Using Network Navigator**

1. **Click Network Navigator visual**
2. **Source**: Drag `department` (from Publications)
3. **Target**: Drag `SDG Name` (from sdg_lookup)
4. **Weight**: Drag `Total Publications` measure
5. Network shows connections between departments and SDGs

**Format Network:**
- **Format pane** → **"General"**:
  - **Title**: ON
  - **Title text**: "Research Collaboration Network: Departments & SDGs"
  - **Font size**: 18

- **Format pane** → **"Visual"**:
  - **Node colors**: 
    - Departments: Illinois Blue (#13294B)
    - SDGs: Illinois Orange (#FF6B35)
  - **Edge colors**: Light gray
  - **Node size**: Based on publication count

**Option B: Using Chord Chart (Alternative)**

1. **Click Chord Chart visual**
2. **Source**: `department`
3. **Target**: `SDG Name`
4. **Value**: `Total Publications`
5. Shows circular network of connections

### **Step 3: Create Collaboration Strength Matrix**

**Create a matrix showing collaboration strength:**

1. **Click Matrix visual**
2. **Rows**: `department` (from Publications)
3. **Columns**: `SDG Name` (from sdg_lookup)
4. **Values**: `Total Publications` measure
5. **Format as heatmap** (conditional formatting)
6. **Title**: "Department-SDG Collaboration Strength"

### **Step 4: Create Collaboration Metrics**

**Create measures for network analysis:**

**Measure 1: Department Connectivity**
```DAX
Department Connectivity = 
VAR Dept = SELECTEDVALUE(Publications[department])
VAR SDGCount = 
    CALCULATE(
        DISTINCTCOUNT('SDG_Mappings'[SDG ID]),
        FILTER(
            ALL(Publications),
            Publications[department] = Dept
        )
    )
RETURN
SDGCount
```

**Measure 2: SDG Reach**
```DAX
SDG Reach = 
VAR SelectedSDG = SELECTEDVALUE('sdg_lookup'[SDG ID])
VAR DeptCount = 
    CALCULATE(
        DISTINCTCOUNT(Publications[department]),
        FILTER(
            'SDG_Mappings',
            'SDG_Mappings'[SDG ID] = SelectedSDG
        )
    )
RETURN
DeptCount
```

**Create cards showing:**
- Average Department Connectivity
- Most Connected Department
- SDG with Highest Reach

### **Step 5: Create Interactive Network Filters**

**Add slicers that filter the network:**

1. **Slicer 1**: `department` - Filter by department
2. **Slicer 2**: `SDG Name` - Filter by SDG
3. **Slicer 3**: `publication_year` - Filter by year range

**Network updates when filters change**

---

## 📋 **Complete Phase 1 Dashboard Structure**

### **New Page: "Strategic Analysis"**

**Layout:**

```
Row 1: [Gap Summary Cards]
       Critical Gaps | Significant Gaps | Well Covered

Row 2: [SDG Gap Analysis Matrix - Full Width]
       Heatmap showing coverage

Row 3: [Gap Recommendations Table]
       List of opportunities

Row 4: [Impact Score Cards]
       Average Impact | Top Score | Distribution

Row 5: [Impact Score Breakdown Chart]
       Top publications by impact

Row 6: [Collaboration Network - Full Width]
       Interactive network graph

Row 7: [Collaboration Metrics Cards]
       Connectivity | Reach | Strength
```

---

## ✅ **Phase 1 Implementation Checklist**

### **SDG Gap Analysis:**
- [ ] Created SDG Coverage Score measure
- [ ] Created SDG Coverage by SDG measure
- [ ] Created SDG Gap Status measure
- [ ] Created gap summary cards (Critical, Significant, Well Covered)
- [ ] Created gap analysis matrix with heatmap
- [ ] Created recommendations table
- [ ] Formatted all visuals with titles

### **Research Impact Score:**
- [ ] Created Journal Tier Score measure
- [ ] Created SDG Alignment Score measure
- [ ] Created Recency Score measure
- [ ] Created Sustainability Score measure
- [ ] Created Research Impact Score measure
- [ ] Created impact score distribution chart
- [ ] Created top researchers table
- [ ] Created impact score by department chart
- [ ] Created impact score breakdown chart

### **Enhanced Collaboration Network:**
- [ ] Installed Network Navigator or Chord Chart
- [ ] Created department-SDG network graph
- [ ] Formatted network (colors, sizes)
- [ ] Created collaboration strength matrix
- [ ] Created Department Connectivity measure
- [ ] Created SDG Reach measure
- [ ] Created collaboration metrics cards
- [ ] Added interactive filters (department, SDG, year)

### **Overall:**
- [ ] Created new page "Strategic Analysis"
- [ ] Arranged all visuals in logical layout
- [ ] Applied consistent formatting (titles, colors)
- [ ] Tested all slicers and cross-filtering
- [ ] Verified all measures calculate correctly

---

## 🎯 **Quick Start Steps**

1. **Create new page**: Click "+" → Rename to "Strategic Analysis"
2. **Start with Gap Analysis**: Build the matrix and cards first
3. **Add Impact Score**: Create all component measures, then total score
4. **Build Network**: Install visual, create network graph
5. **Format everything**: Add titles, colors, consistent styling
6. **Test**: Verify slicers work, measures calculate correctly

---

## 💡 **Pro Tips**

1. **Start Simple**: Build basic version first, enhance later
2. **Test Measures**: Verify each measure works before building visuals
3. **Use Conditional Formatting**: Makes heatmaps and matrices more visual
4. **Interactive Elements**: Add slicers to make network dynamic
5. **Documentation**: Add tooltips explaining what each metric means

---

**Follow these steps to build all Phase 1 features! Start with Gap Analysis, then Impact Score, then Network.** 🎉

Need help with any specific step? Let me know which feature you're working on!

