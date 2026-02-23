# Power BI Visuals - Detailed Step-by-Step Instructions
## Complete Guide for Building Collaboration Hub Dashboard

---

## 🎯 **BEFORE YOU START**

### **Verify Your Data is Loaded:**
1. In Power BI, look at the **Fields** pane (right side)
2. You should see your dataset/tables:
   - **Matches** (or similar name)
   - **Researchers** (or similar name)
3. Expand each table to see columns
4. Verify you see: `Faculty_A_Name`, `Total_Score`, `Method_Score`, etc.

---

## 📊 **VISUALIZATION 1: TOP MATCHES TABLE**

### **Purpose:** Show best collaboration opportunities ranked by compatibility score

### **Step-by-Step:**

#### **Step 1: Create the Table**
1. In Power BI, make sure you're in **Report** view (left sidebar, chart icon)
2. Click on the **"Table"** icon in the **Visualizations** pane (left side)
   - It looks like a grid/table
   - If you don't see it, scroll through the visualization icons

#### **Step 2: Add Fields to the Table**
1. In the **Fields** pane (right side), find your **Matches** table (or dataset name)
2. **Drag and drop** these fields into the **Values** section (under "Visualizations"):
   - `Faculty_A_Name`
   - `Faculty_B_Name`
   - `Total_Score`
   - `Topic_Score`
   - `Method_Score`
   - `Stage_Score`
   - `Method_Reason` (optional but helpful)

**What you'll see:** A table appears on your canvas with all these columns

#### **Step 3: Sort by Total Score**
1. Click on the **`Total_Score`** column header in the table
2. You'll see a small **sort icon** appear (AZ with arrow)
3. Click the sort icon → Select **"Sort descending"**
   - This shows highest scores first (100, 99, 98...)

**Alternative method:**
- Click **"..."** (three dots) on the table visual
- Select **"Sort by"** → **"Total_Score"** → **"Descending"**

#### **Step 4: Filter to Top Matches**
1. Click **"..."** (three dots) on the table visual
2. Select **"Filters on this visual"**
3. Find **`Total_Score`** in the filter list
4. Set filter:
   - **"Show items when the value"** → **"is greater than or equal to"**
   - Enter: **70**
   - OR use **"Top N"** → Enter: **20**

**Result:** Table now shows only top 20 matches (or matches with score ≥70)

#### **Step 5: Format the Table**
1. Click on the table visual (to select it)
2. Click **"Format visual"** (paint roller icon in Visualizations pane)
3. **General:**
   - **Title:** Turn ON
   - **Title text:** "Top Collaboration Matches"
   - **Font size:** 16pt
   - **Position:** Center

4. **Column headers:**
   - **Text size:** 12pt
   - **Font family:** Segoe UI (or default)

5. **Values:**
   - **Text size:** 11pt

#### **Step 6: Add Conditional Formatting (Color by Score)**
1. Click on the **`Total_Score`** column in the table
2. Click **"..."** (three dots) that appears
3. Select **"Conditional formatting"** → **"Background color"**
4. **Format style:** Select **"Rules"**
5. **Add rules:**
   - **Rule 1:**
     - **If value:** `is greater than or equal to` → **85**
     - **Then color:** Green (#4CAF50 or #00B050)
   - **Rule 2:**
     - **If value:** `is greater than or equal to` → **70** AND `is less than` → **85**
     - **Then color:** Light green (#81C784 or #92D050)
   - **Rule 3:**
     - **If value:** `is greater than or equal to` → **55** AND `is less than` → **70**
     - **Then color:** Yellow (#FFC107 or #FFC000)
   - **Rule 4:**
     - **If value:** `is less than` → **55**
     - **Then color:** Light gray (#E0E0E0 or #D9D9D9)

6. Click **OK**

**Result:** Your table now has color-coded scores - green for excellent, gray for low!

#### **Step 7: Resize and Position**
1. Click and drag the table to position it
2. Drag corners to resize
3. Make it wide enough to see all columns

**✅ DONE!** You now have a color-coded table showing top matches!

---

## 📊 **VISUALIZATION 2: METHOD COMPLEMENTARITY MATRIX**

### **Purpose:** Prove that different methods = higher scores (KEY INNOVATION!)

### **Step-by-Step:**

#### **Step 1: Create the Matrix**
1. Click on a blank area of your canvas (or create new page)
2. Click **"Matrix"** icon in Visualizations pane
   - Looks like a grid with rows and columns

#### **Step 2: Add Fields**
1. In **Fields** pane, find your **Matches** table
2. **Drag and drop:**
   - `Faculty_A_Method` → Drop in **Rows** section
   - `Faculty_B_Method` → Drop in **Columns** section
   - `Total_Score` → Drop in **Values** section

3. **Set aggregation:**
   - Click on `Total_Score` in Values
   - Change from **Sum** to **Average**
   - Click the dropdown arrow next to `Total_Score`
   - Select **"Average"**

**What you'll see:** A matrix with methods as rows/columns and average scores in cells

#### **Step 3: Format the Matrix**
1. Click **"Format visual"** (paint roller icon)
2. **General:**
   - **Title:** Turn ON
   - **Title text:** "Method Complementarity Matrix"
   - **Font size:** 16pt

3. **Row headers:**
   - **Text size:** 11pt
   - **Font style:** Bold

4. **Column headers:**
   - **Text size:** 11pt
   - **Font style:** Bold

5. **Values:**
   - **Text size:** 10pt
   - **Display units:** None (show full numbers)

#### **Step 4: Add Conditional Formatting (Color Scale)**
1. Click on the matrix visual
2. Click **"Format visual"**
3. Scroll to **"Conditional formatting"** section
4. Find **"Background color"** → Turn it ON
5. **Format style:** Select **"Color scale"**
6. **Minimum:**
   - **Color:** Red (#FF0000 or #E81123)
   - **Value:** 0 (or lowest score in your data)
7. **Maximum:**
   - **Color:** Green (#00B050 or #4CAF50)
   - **Value:** 100 (or highest score)
8. **Center:** (optional)
   - **Color:** Yellow (#FFC107)
   - **Value:** 50

**Alternative: Rules-based formatting:**
- **Format style:** Select **"Rules"**
- **Rule 1:** `>= 85` → Green
- **Rule 2:** `>= 70` → Light green
- **Rule 3:** `>= 50` → Yellow
- **Rule 4:** `< 50` → Red

#### **Step 5: Verify the Matrix Shows Complementarity**
**Look for:**
- **Theoretical + Empirical** = Should be GREEN (high score ~85-100) ✅
- **Theoretical + Theoretical** = Should be RED (low score ~25) ❌
- **Empirical + Fieldwork** = Should be GREEN (high score) ✅

**This proves your algorithm rewards complementary methods!**

**✅ DONE!** Your matrix now visually shows method complementarity!

---

## 📊 **VISUALIZATION 3: SCORE BREAKDOWN CHART**

### **Purpose:** Show the three components (Topic 50%, Method 35%, Stage 15%)

### **Step-by-Step:**

#### **Step 1: Create Stacked Bar Chart**
1. Click on blank area of canvas
2. Click **"Stacked bar chart"** icon
   - Looks like horizontal bars stacked on top of each other

#### **Step 2: Add Fields**
1. **Axis (Y-axis):**
   - Drag `Faculty_A_Name` to **Axis** section
   - **OR** create a calculated column for "Match Pair" (see alternative below)

2. **Values (X-axis):**
   - Drag `Topic_Score` to **Values** → Set to **Average**
   - Drag `Method_Score` to **Values** → Set to **Average**
   - Drag `Stage_Score` to **Values** → Set to **Average**

**Alternative: Create Match Pair Column**
- In Power BI Desktop: **Modeling** tab → **New column**
- Formula: `Match Pair = [Faculty_A_Name] & " ↔ " & [Faculty_B_Name]`
- Use this in Axis instead of `Faculty_A_Name`

#### **Step 3: Filter to Top Matches**
1. Click **"..."** on the chart
2. **"Filters on this visual"**
3. Add filter: `Total_Score` → **Top N** → **15**
   - This shows only top 15 matches (otherwise too cluttered)

#### **Step 4: Format the Chart**
1. Click **"Format visual"**
2. **General:**
   - **Title:** Turn ON
   - **Title text:** "Compatibility Score Breakdown"
   - **Font size:** 16pt

3. **Legend:**
   - Turn ON
   - **Position:** Top or Right
   - **Title:** Turn ON
   - **Title text:** "Score Components"

4. **Data colors:**
   - Click on `Topic_Score` → Change color to **Blue** (#13294B - Illinois Blue)
   - Click on `Method_Score` → Change color to **Orange** (#FF6B35 - Illinois Orange)
   - Click on `Stage_Score` → Change color to **Green** (#4CAF50)

5. **Data labels:**
   - Turn ON
   - **Position:** Center
   - **Display units:** None

6. **X-axis:**
   - **Title:** Turn ON
   - **Title text:** "Score (0-100)"
   - **Font size:** 11pt

7. **Y-axis:**
   - **Title:** Turn ON
   - **Title text:** "Researcher Pairs"
   - **Font size:** 11pt

#### **Step 5: Update Legend Labels**
1. In **Fields** pane, right-click `Topic_Score`
2. Select **"Rename"** → Change to **"Topic (50%)"**
3. Repeat for:
   - `Method_Score` → **"Method (35%)"**
   - `Stage_Score` → **"Stage (15%)"**

**✅ DONE!** You now have a stacked bar chart showing score components!

---

## 📊 **VISUALIZATION 4: MATCH QUALITY DISTRIBUTION (PIE CHART)**

### **Purpose:** Show distribution of match quality

### **Step-by-Step:**

#### **Step 1: Create Pie Chart**
1. Click on blank area
2. Click **"Pie chart"** icon (looks like a pie/circle)

#### **Step 2: Add Fields**
1. **Legend:**
   - Drag `Match_Quality` to **Legend** section
   - This creates slices for: Excellent, Good, Moderate, Low

2. **Values:**
   - Drag `Total_Score` to **Values** section
   - Change from **Sum** to **Count**
   - Click dropdown → Select **"Count"**

**What you'll see:** A pie chart with slices for each quality level

#### **Step 3: Format the Pie Chart**
1. Click **"Format visual"**
2. **General:**
   - **Title:** Turn ON
   - **Title text:** "Match Quality Distribution"
   - **Font size:** 16pt

3. **Legend:**
   - Turn ON
   - **Position:** Right or Bottom
   - **Title:** Turn ON
   - **Title text:** "Quality"

4. **Data colors:**
   - Click on "Excellent" → **Green** (#4CAF50)
   - Click on "Good" → **Blue** (#13294B)
   - Click on "Moderate" → **Yellow** (#FFC107)
   - Click on "Low" → **Gray** (#9E9E9E)

5. **Data labels:**
   - Turn ON
   - **Style:** Percentage
   - **Position:** Outside
   - **Show category:** ON
   - **Show value:** ON

**✅ DONE!** Pie chart showing match quality distribution!

---

## 📊 **VISUALIZATION 5: SUMMARY CARDS (KEY METRICS)**

### **Purpose:** Show key metrics at a glance

### **Step-by-Step:**

#### **Card 1: Total Matches**
1. Click **"Card"** icon (looks like a number in a box)
2. Drag `Total_Score` to **Fields**
3. Change from **Sum** to **Count**
   - Click dropdown → **"Count"**
4. **Format:**
   - **Title:** Turn ON
   - **Title text:** "Total Matches"
   - **Data label:** Turn ON
   - **Font size:** 24pt (large number)
   - **Color:** Illinois Blue (#13294B)

#### **Card 2: Average Compatibility Score**
1. Click **"Card"** icon (create new card)
2. Drag `Total_Score` to **Fields**
3. Keep as **Average** (or change to Average if needed)
4. **Format:**
   - **Title:** "Average Compatibility"
   - **Data label:** Turn ON
   - **Font size:** 24pt
   - **Display units:** None
   - **Decimal places:** 1
   - **Color:** Illinois Orange (#FF6B35)

#### **Card 3: Excellent Matches**
1. Click **"Card"** icon
2. Drag `Match_Quality` to **Fields**
3. Change to **Count**
4. **Add filter:**
   - Click **"..."** on card
   - **"Filters on this visual"**
   - Add filter: `Match_Quality` = **"Excellent"**
5. **Format:**
   - **Title:** "Excellent Matches"
   - **Font size:** 24pt
   - **Color:** Green (#4CAF50)

#### **Card 4: Complementary Methods**
1. Click **"Card"** icon
2. Drag `Is_Complementary` to **Fields**
3. Change to **Count**
4. **Add filter:**
   - `Is_Complementary` = **True**
5. **Format:**
   - **Title:** "Complementary Matches"
   - **Font size:** 24pt
   - **Color:** Orange (#FF6B35)

**✅ DONE!** Four cards showing key metrics!

---

## 📊 **VISUALIZATION 6: SDG-BASED MATCHING (BAR CHART)**

### **Purpose:** Show which SDGs have best matches

### **Step-by-Step:**

#### **Step 1: Create Bar Chart**
1. Click **"Bar chart"** icon (horizontal bars)
   - OR **"Column chart"** (vertical bars)

#### **Step 2: Add Fields**
1. **Axis (Y-axis for horizontal, X-axis for vertical):**
   - Drag `SDG` to **Axis** section
   - This shows SDG numbers (1, 2, 3... 17)

2. **Values:**
   - Drag `Total_Score` to **Values** section
   - Change to **Average**

#### **Step 3: Sort the Chart**
1. Click **"..."** on the chart
2. Select **"Sort by"** → **"Total_Score"** → **"Descending"**
   - This shows highest-scoring SDGs first

#### **Step 4: Format the Chart**
1. Click **"Format visual"**
2. **General:**
   - **Title:** "Average Compatibility by SDG"
   - **Font size:** 16pt

3. **Data colors:**
   - **Show all:** ON
   - Use SDG colors if you have them, or use a gradient

4. **Data labels:**
   - Turn ON
   - **Position:** Outside end
   - **Display units:** None
   - **Decimal places:** 1

5. **X-axis (for horizontal bars):**
   - **Title:** "Average Compatibility Score"
   - **Font size:** 11pt

6. **Y-axis:**
   - **Title:** "SDG"
   - **Font size:** 11pt

**✅ DONE!** Bar chart showing SDG compatibility!

---

## 📊 **VISUALIZATION 7: RESEARCHER SEARCH/FILTER (SLICER)**

### **Purpose:** Let users filter by specific researcher

### **Step-by-Step:**

#### **Step 1: Create Slicer**
1. Click **"Slicer"** icon
   - Looks like a filter/funnel icon

#### **Step 2: Add Field**
1. Drag `Faculty_A_Name` to **Field** section
   - This creates a list of all researchers

#### **Step 3: Format the Slicer**
1. Click **"Format visual"**
2. **General:**
   - **Title:** Turn ON
   - **Title text:** "Search by Researcher"
   - **Font size:** 14pt

3. **Selection controls:**
   - **Single select:** ON (user picks one researcher)
   - **Select all:** ON (option to see all)

4. **Style:**
   - **Style:** Dropdown (easier to use)
   - OR **List** (shows all names)

5. **Items:**
   - **Text size:** 11pt
   - **Height:** Adjust to show 5-10 items

#### **Step 4: Enable Search (If Available)**
1. In slicer format options, look for **"Search"**
2. Turn ON if available
   - This lets users type to search for researchers

**How it works:** When user selects a researcher, all other visuals filter to show only their matches!

**✅ DONE!** Interactive filter created!

---

## 📊 **VISUALIZATION 8: MATCH DETAILS CARD (SHOW BREAKDOWN)**

### **Purpose:** Show detailed breakdown when a match is selected

### **Step-by-Step:**

#### **Step 1: Create Multiple Cards**
Create 4 separate card visuals side by side:

#### **Card 1: Total Score**
1. Click **"Card"** icon
2. Drag `Total_Score` to Fields
3. Set to **Average** (or use a measure that shows selected value)
4. **Format:**
   - **Title:** "Compatibility Score"
   - **Font size:** 32pt (very large)
   - **Color:** Illinois Blue

#### **Card 2: Topic Score**
1. Click **"Card"** icon
2. Drag `Topic_Score` to Fields
3. Set to **Average**
4. **Format:**
   - **Title:** "Topic Match (50%)"
   - **Font size:** 20pt
   - **Color:** Blue

#### **Card 3: Method Score**
1. Click **"Card"** icon
2. Drag `Method_Score` to Fields
3. Set to **Average**
4. **Format:**
   - **Title:** "Method Match (35%)"
   - **Font size:** 20pt
   - **Color:** Orange

#### **Card 4: Stage Score**
1. Click **"Card"** icon
2. Drag `Stage_Score` to Fields
3. Set to **Average**
4. **Format:**
   - **Title:** "Stage Match (15%)"
   - **Font size:** 20pt
   - **Color:** Green

**How it works:** When user selects a match in the table, these cards show the breakdown!

**✅ DONE!** Score breakdown cards created!

---

## 🎨 **DASHBOARD FORMATTING & LAYOUT**

### **Step 1: Add Dashboard Title**
1. Click **"Text box"** icon (or use Insert → Text box)
2. Type: **"Collaboration Hub - Compatibility Matching"**
3. **Format:**
   - **Font size:** 24pt
   - **Font style:** Bold
   - **Color:** Illinois Blue (#13294B)
   - **Alignment:** Center

### **Step 2: Arrange Visuals**
1. **Top row:** Title + Summary Cards (4 cards)
2. **Second row:** Top Matches Table (full width)
3. **Third row:** Method Complementarity Matrix + Match Quality Pie Chart
4. **Fourth row:** Score Breakdown Chart (full width)
5. **Fifth row:** SDG Bar Chart + Researcher Slicer

### **Step 3: Apply Consistent Formatting**
1. **Background:**
   - Click on canvas (blank area)
   - **Format** → **Page background**
   - **Color:** White or Light gray (#F5F5F5)

2. **Visual backgrounds:**
   - For each visual, set background to White
   - Add subtle border (1px, light gray)

3. **Spacing:**
   - Add padding between visuals
   - Align visuals neatly (use grid/snap to grid)

---

## ✅ **VALIDATION CHECKLIST**

After building each visualization, verify:

### **Top Matches Table:**
- [ ] Shows researchers' names
- [ ] Sorted by Total_Score (highest first)
- [ ] Color-coded by score (green = high, gray = low)
- [ ] Shows Topic, Method, Stage scores

### **Method Complementarity Matrix:**
- [ ] Theoretical + Empirical = High score (green) ✅
- [ ] Theoretical + Theoretical = Low score (red) ✅
- [ ] Colors make sense (green = good, red = bad)

### **Score Breakdown Chart:**
- [ ] Shows three components (Topic, Method, Stage)
- [ ] Colors: Blue, Orange, Green
- [ ] Legend shows weights (50%, 35%, 15%)

### **Summary Cards:**
- [ ] Total Matches shows correct count
- [ ] Average Score shows reasonable number (30-50)
- [ ] Excellent Matches shows count
- [ ] Complementary Matches shows count

### **Slicer:**
- [ ] Can select a researcher
- [ ] Other visuals filter when researcher selected
- [ ] Search works (if enabled)

---

## 🚨 **COMMON ISSUES & SOLUTIONS**

### **Problem: "Can't see fields in Fields pane"**
**Solution:**
- Make sure you're in **Report** view (not Data or Model view)
- Check that your dataset is loaded (should appear in Fields pane)
- Try refreshing the page

### **Problem: "Visual shows wrong data"**
**Solution:**
- Check aggregation (Sum vs Average vs Count)
- Verify you're using the right field
- Check filters (might be filtering out data)

### **Problem: "Can't sort table"**
**Solution:**
- Click directly on the column header
- Look for sort icon (AZ with arrow)
- Or use "..." menu → "Sort by"

### **Problem: "Conditional formatting not working"**
**Solution:**
- Make sure you're formatting the right field
- Check that values are numeric (not text)
- Verify rule conditions are correct

### **Problem: "Matrix shows wrong values"**
**Solution:**
- Check aggregation is set to **Average** (not Sum)
- Verify rows and columns are correct
- Check if filters are applied

### **Problem: "Slicer doesn't filter other visuals"**
**Solution:**
- Make sure slicer is on the same page as other visuals
- Check that fields are related (if using multiple tables)
- Try selecting a value in the slicer

---

## 🎯 **QUICK REFERENCE: Visual Icons**

| Visual Type | Icon Description | Where to Find |
|------------|------------------|---------------|
| **Table** | Grid/table icon | Visualizations pane, first row |
| **Matrix** | Grid with rows/columns | Visualizations pane |
| **Stacked Bar** | Horizontal bars stacked | Visualizations pane, charts section |
| **Pie Chart** | Circle/pie icon | Visualizations pane, charts section |
| **Card** | Number in box | Visualizations pane |
| **Bar Chart** | Horizontal bars | Visualizations pane, charts section |
| **Slicer** | Funnel/filter icon | Visualizations pane |

---

## 📝 **PRESENTATION TIPS**

### **When Presenting:**

1. **Start with Top Matches Table:**
   - "Here are the top collaboration opportunities"
   - Point out color coding (green = excellent)

2. **Show Method Complementarity Matrix:**
   - "Notice: Theoretical + Empirical = High scores"
   - "But Theoretical + Theoretical = Low scores"
   - "This proves we reward complementary methods!"

3. **Use the Slicer:**
   - Select a researcher
   - Show how other visuals update
   - Demonstrate interactivity

4. **Explain Score Breakdown:**
   - "Each match has three components"
   - "Topic is 50%, Method is 35%, Stage is 15%"
   - "This matches the professor's criteria"

---

## 🎨 **ILLINOIS BRANDING COLORS**

Use these colors throughout:

- **Primary Blue:** #13294B (headers, primary text)
- **Orange:** #FF6B35 (highlights, CTAs, Method scores)
- **Green:** #4CAF50 (success, high scores, Stage scores)
- **Yellow:** #FFC107 (moderate scores, warnings)
- **Gray:** #9E9E9E (low scores, secondary text)

---

**Follow these steps exactly, and you'll have a professional Collaboration Hub dashboard!** 🚀

Start with Visualization 1 (Top Matches Table) - it's the foundation!



