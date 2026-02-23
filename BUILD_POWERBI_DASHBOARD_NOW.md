# Build Your Collaboration Hub Dashboard - Step by Step
## Power BI Visualization Guide

---

## 🎯 **VISUALIZATION 1: Top Matches Table (MOST IMPORTANT)**

### **Purpose:** Show best collaboration opportunities ranked by compatibility score

### **Steps:**

1. **Click "Table" visual** (in Visualizations pane, left side)

2. **Add Fields to Values:**
   - Drag `Faculty_A_Name` to Values
   - Drag `Faculty_B_Name` to Values
   - Drag `Total_Score` to Values
   - Drag `Topic_Score` to Values
   - Drag `Method_Score` to Values
   - Drag `Stage_Score` to Values
   - Drag `Method_Reason` to Values (optional, but helpful)

3. **Sort by Score:**
   - Click on the `Total_Score` column header in the table
   - Click the **sort icon** (AZ with arrow) → Select **"Sort descending"**
   - This shows highest scores first!

4. **Filter to Top Matches:**
   - Click **"..."** (three dots) on the table visual
   - Select **"Filter"** → **"Total_Score"**
   - Set filter: **"is greater than or equal to"** → **70**
   - OR set to show **Top N** → **20** items

5. **Format the Table:**
   - Click **Format** (paint roller icon)
   - **Title:** "Top Collaboration Matches"
   - **Font size:** 12-14pt
   - **Column headers:** Bold

6. **Add Conditional Formatting (Color by Score):**
   - Click on `Total_Score` column
   - Click **"..."** → **"Conditional formatting"** → **"Background color"**
   - Set rules:
     - **85-100:** Green (#4CAF50)
     - **70-84:** Light green (#81C784)
     - **55-69:** Yellow (#FFC107)
     - **<55:** Light gray (#E0E0E0)

**Result:** You'll see a table showing the best matches with color-coded scores!

---

## 🎯 **VISUALIZATION 2: Method Complementarity Matrix**

### **Purpose:** Prove that different methods = higher scores (KEY INNOVATION!)

### **Steps:**

1. **Click "Matrix" visual**

2. **Add Fields:**
   - Drag `Faculty_A_Method` to **Rows**
   - Drag `Faculty_B_Method` to **Columns**
   - Drag `Total_Score` to **Values** (set to **Average**)

3. **Format:**
   - Click **Format** (paint roller)
   - **Title:** "Method Complementarity Matrix"
   - **Conditional formatting:**
     - Click on the matrix
     - **"..."** → **"Conditional formatting"** → **"Background color"**
     - **Color scale:** Green (high) to Red (low)
     - **OR** set specific rules:
       - **≥85:** Green
       - **70-84:** Light green
       - **50-69:** Yellow
       - **<50:** Red

4. **What to Look For:**
   - **Theoretical + Empirical** = Should be HIGH (green) ✅
   - **Theoretical + Theoretical** = Should be LOW (red) ❌
   - This proves complementarity works!

**Result:** A matrix showing which method pairs score highest!

---

## 🎯 **VISUALIZATION 3: Score Breakdown Chart**

### **Purpose:** Show the three components (Topic 50%, Method 35%, Stage 15%)

### **Steps:**

1. **Click "Stacked bar chart"** (or "Clustered bar chart")

2. **Add Fields:**
   - **Axis:** Drag `Faculty_A_Name` (or create a calculated column for "Match Pair")
   - **Values:**
     - Drag `Topic_Score` (set to **Average**)
     - Drag `Method_Score` (set to **Average**)
     - Drag `Stage_Score` (set to **Average**)

3. **Filter:**
   - Show only top 10-15 matches (filter by `Total_Score`)

4. **Format:**
   - **Title:** "Compatibility Score Breakdown"
   - **Colors:**
     - `Topic_Score`: Blue (#13294B - Illinois Blue)
     - `Method_Score`: Orange (#FF6B35 - Illinois Orange)
     - `Stage_Score`: Green (#4CAF50)
   - **Legend:** Show with labels
   - **Data labels:** ON (show values on bars)

5. **Add Legend Labels:**
   - In legend, rename:
     - "Topic_Score" → "Topic (50%)"
     - "Method_Score" → "Method (35%)"
     - "Stage_Score" → "Stage (15%)"

**Result:** A stacked bar chart showing how each score contributes!

---

## 🎯 **VISUALIZATION 4: Match Quality Distribution**

### **Purpose:** Show distribution of match quality

### **Steps:**

1. **Click "Pie chart"** (or "Donut chart")

2. **Add Fields:**
   - **Legend:** Drag `Match_Quality` (from your data)
   - **Values:** Drag `Total_Score` (set to **Count**)

3. **Format:**
   - **Title:** "Match Quality Distribution"
   - **Colors:**
     - "Excellent": Green (#4CAF50)
     - "Good": Blue (#13294B)
     - "Moderate": Yellow (#FFC107)
     - "Low": Gray (#9E9E9E)
   - **Data labels:** Show percentage

**Result:** A pie chart showing how many matches are Excellent vs Good vs Moderate!

---

## 🎯 **VISUALIZATION 5: Score Summary Cards**

### **Purpose:** Key metrics at a glance

### **Steps:**

1. **Click "Card" visual** (repeat for each metric)

2. **Card 1: Total Matches**
   - Drag `Total_Score` to Fields
   - Set to **Count**
   - **Title:** "Total Matches"

3. **Card 2: Average Score**
   - Drag `Total_Score` to Fields
   - Set to **Average**
   - **Title:** "Average Compatibility"
   - **Format:** 1 decimal place

4. **Card 3: Excellent Matches**
   - Drag `Match_Quality` to Fields
   - Add filter: `Match_Quality = "Excellent"`
   - Set to **Count**
   - **Title:** "Excellent Matches"

5. **Card 4: Complementary Methods**
   - Drag `Is_Complementary` to Fields
   - Add filter: `Is_Complementary = True`
   - Set to **Count**
   - **Title:** "Complementary Matches"

**Result:** Four cards showing key metrics!

---

## 🎯 **VISUALIZATION 6: SDG-Based Matching**

### **Purpose:** Show which SDGs have best matches

### **Steps:**

1. **Click "Bar chart"** (horizontal or vertical)

2. **Add Fields:**
   - **Axis:** Drag `SDG` (from Matches table)
   - **Values:** Drag `Total_Score` (set to **Average**)

3. **Format:**
   - **Title:** "Average Compatibility by SDG"
   - **Sort:** By `Total_Score` (descending)
   - **Colors:** Use SDG colors if you have them, or gradient

**Result:** Bar chart showing which SDGs have highest compatibility scores!

---

## 🎯 **VISUALIZATION 7: Researcher Search/Filter**

### **Purpose:** Let users filter by specific researcher

### **Steps:**

1. **Click "Slicer" visual**

2. **Add Field:**
   - Drag `Faculty_A_Name` to Field

3. **Format:**
   - **Style:** Dropdown or List
   - **Title:** "Search by Researcher"
   - Enable **Search** option

4. **How It Works:**
   - When user selects a researcher, all other visuals filter to show their matches!

**Result:** Interactive filter for exploring matches!

---

## 📊 **DASHBOARD LAYOUT**

### **Recommended Arrangement:**

```
┌─────────────────────────────────────────────────────────┐
│  COLLABORATION HUB - Compatibility Matching            │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  [Search: Researcher...]                                 │
│                                                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐ │
│  │ Total    │  │ Avg      │  │ Excellent│  │Complement│ │
│  │ Matches  │  │ Score    │  │ Matches  │  │ Methods  │ │
│  │  4,950   │  │  39.9    │  │    0     │  │  2,697   │ │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘ │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Top Collaboration Matches (Table)               │  │
│  │  [Shows top 20 matches with scores]              │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
│  ┌──────────────────┐  ┌──────────────────────────────┐ │
│  │ Match Quality    │  │ Method Complementarity       │ │
│  │ Distribution     │  │ Matrix                       │ │
│  │ (Pie Chart)      │  │ [Theoretical + Empirical]   │ │
│  └──────────────────┘  └──────────────────────────────┘ │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Score Breakdown (Stacked Bar)                   │  │
│  │  [Topic 50% | Method 35% | Stage 15%]            │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Average Compatibility by SDG (Bar Chart)        │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

## 🎨 **FORMATTING TIPS**

### **Colors (Illinois Branding):**
- **Primary Blue:** #13294B (headers, text)
- **Orange:** #FF6B35 (highlights, CTAs)
- **Green:** #4CAF50 (success, high scores)
- **Yellow:** #FFC107 (moderate scores)
- **Gray:** #9E9E9E (low scores)

### **Fonts:**
- **Headers:** Bold, 18-24pt
- **Titles:** 14-16pt
- **Data:** 12pt

### **Spacing:**
- Add padding between visuals
- Use consistent spacing
- Align visuals neatly

---

## ✅ **QUICK CHECKLIST**

### **Must-Have Visualizations:**
- [ ] Top Matches Table (sorted by score)
- [ ] Method Complementarity Matrix
- [ ] Score Breakdown Chart
- [ ] Summary Cards (4 key metrics)

### **Should-Have:**
- [ ] Match Quality Distribution (pie chart)
- [ ] SDG-Based Matching (bar chart)
- [ ] Researcher Search/Filter (slicer)

### **Formatting:**
- [ ] Illinois colors applied
- [ ] Titles added to all visuals
- [ ] Conditional formatting on scores
- [ ] Dashboard title added

---

## 🎯 **KEY VALIDATION**

After building, verify:

1. **Method Complementarity Works:**
   - Theoretical + Empirical = High scores (green) ✅
   - Theoretical + Theoretical = Low scores (red) ✅

2. **Scores Display Correctly:**
   - Total_Score shows 0-100 range
   - Topic_Score, Method_Score, Stage_Score visible

3. **Filtering Works:**
   - Selecting a researcher filters other visuals
   - Scores update correctly

---

## 🚀 **NEXT: Presentation Prep**

Once your dashboard is built:

1. **Practice your demo:**
   - Click through different researchers
   - Show method complementarity matrix
   - Explain the three criteria

2. **Create slides:**
   - Problem statement
   - Solution overview
   - Algorithm explanation
   - Live demo (Power BI)
   - Impact & next steps

3. **Key talking points:**
   - "Method complementarity rewards different methods"
   - "Proactive matching, not just search"
   - "Transparent scoring with explainable breakdowns"

---

**Start with Visualization 1 (Top Matches Table) - it's the most important!** 🎯



