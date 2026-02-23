# Tableau Visuals - Detailed Step-by-Step Instructions
## Complete Guide for Building Collaboration Hub Dashboard in Tableau

---

## 🎯 **WHY TABLEAU? (Advantages)**

✅ **Better for complex visualizations** - More flexible than Power BI  
✅ **Easier data blending** - Handles multiple data sources seamlessly  
✅ **More intuitive drag-and-drop** - Visual interface is very user-friendly  
✅ **Better for presentations** - Export quality is excellent  
✅ **Free Public version available** - Tableau Public is free (with some limitations)  
✅ **Works on Mac** - Native Mac support (unlike Power BI Desktop)

---

## 🎯 **BEFORE YOU START**

### **What You Need:**
1. **Tableau Desktop** (paid) OR **Tableau Public** (free)
   - Download: https://public.tableau.com/app/discover/tableau-public
   - Tableau Public is free but requires publishing to public (fine for case competition)
   - Tableau Desktop has full features but requires license

2. **Your Data File:**
   - `Collab_Hub_Data.xlsx` (the Excel file with multiple sheets)
   - OR individual CSV files if you prefer

### **Verify Your Data:**
- You should have these sheets/tables:
  - **Matches** (or `Collab_Matches_For_PowerBI`)
  - **Researchers** (or `Researcher_Profiles_For_PowerBI`)
  - **Network** (or `network_graph_data`)
  - **Best_Matches** (or `best_faculty_match`)

---

## 📊 **VISUALIZATION 1: TOP MATCHES TABLE**

### **Purpose:** Show best collaboration opportunities ranked by compatibility score

### **Step-by-Step:**

#### **Step 1: Connect to Data**
1. Open **Tableau Desktop** or **Tableau Public**
2. Click **"Connect to Data"** (left side)
3. Select **"Microsoft Excel"** (or **"Text file"** if using CSV)
4. Navigate to your `Collab_Hub_Data.xlsx` file
5. Click **"Open"**

#### **Step 2: Select Your Sheet**
1. In the **Data Source** view (left side), you'll see your Excel sheets
2. **Drag** the **"Matches"** sheet (or `Collab_Matches_For_PowerBI`) to the canvas area
3. You'll see a preview of your data
4. Click **"Sheet 1"** tab at the bottom (or click **"Go to Worksheet"**)

#### **Step 3: Create the Table**
1. You're now in a **Worksheet** view
2. In the **Data** pane (left side), you'll see all your columns
3. **Drag and drop** these fields to the **Rows** shelf:
   - `Faculty_A_Name`
   - `Faculty_B_Name`

4. **Drag and drop** these fields to the **Columns** shelf (or **Text** in Marks card):
   - `Total_Score`
   - `Topic_Score`
   - `Method_Score`
   - `Stage_Score`
   - `Method_Reason` (optional)

**What you'll see:** A table appears with all these columns

**Alternative (Better for Tableau):**
- Drag all fields to **Rows** shelf
- Tableau will automatically create a table
- Right-click on the table → **"Transpose"** if needed

#### **Step 4: Sort by Total Score**
1. Click on the **`Total_Score`** column header
2. You'll see a **sort icon** (up/down arrows)
3. Click the sort icon → Select **"Sort Descending"**
   - OR right-click `Total_Score` → **"Sort"** → **"Descending"**

**Alternative method:**
- Right-click `Total_Score` in the Data pane
- Select **"Sort"** → **"Descending"**
- This sorts at the data level

#### **Step 5: Filter to Top Matches**
1. Drag `Total_Score` to the **Filters** shelf (top of worksheet)
2. A filter dialog appears
3. Select **"Range of values"** or **"At least"**
4. Enter minimum: **70**
5. Click **OK**

**OR use Top N filter:**
1. Drag `Total_Score` to **Filters** shelf
2. In filter dialog, click **"Top"** tab
3. Select **"By field"**
4. Enter: **20** (top 20)
5. Click **OK**

**Result:** Table now shows only top 20 matches (or matches with score ≥70)

#### **Step 6: Format the Table**
1. Click **"Format"** menu → **"Shading"**
2. **Worksheet:**
   - **Background:** White
   - **Border:** Light gray

3. **Headers:**
   - **Font:** Segoe UI, 12pt, Bold
   - **Background:** Illinois Blue (#13294B)
   - **Text color:** White

4. **Cells:**
   - **Font:** Segoe UI, 11pt
   - **Alignment:** Center (for numbers)

5. **Add Title:**
   - Click **"Worksheet"** menu → **"Show Title"**
   - Double-click title → Type: **"Top Collaboration Matches"**
   - Format title: 16pt, Bold, Illinois Blue

#### **Step 7: Add Conditional Formatting (Color by Score)**
1. Drag `Total_Score` to the **Color** shelf (in Marks card)
2. Click the **Color** shelf → **"Edit Colors"**
3. **Color Palette:** Select **"Red-Blue Diverging"** or **"Traffic Light"**
4. **Stepped Color:** Turn ON
5. **Steps:** 4
6. **Range:**
   - **Start:** 0 (Red)
   - **End:** 100 (Green)
   - **Center:** 50 (Yellow)

**OR use custom colors:**
1. Click **"Edit Colors"**
2. Select **"Custom"**
3. Click each color → Set:
   - **High (85-100):** Green (#4CAF50)
   - **Medium-High (70-85):** Light Green (#81C784)
   - **Medium (55-70):** Yellow (#FFC107)
   - **Low (<55):** Gray (#E0E0E0)

**Result:** Your table now has color-coded scores!

#### **Step 8: Resize and Position**
1. Click and drag the table to position it
2. Drag corners to resize
3. Make it wide enough to see all columns

**✅ DONE!** You now have a color-coded table showing top matches!

---

## 📊 **VISUALIZATION 2: METHOD COMPLEMENTARITY MATRIX**

### **Purpose:** Prove that different methods = higher scores (KEY INNOVATION!)

### **Step-by-Step:**

#### **Step 1: Create New Worksheet**
1. Click **"New Worksheet"** icon (bottom left, + icon)
2. Name it: **"Method Complementarity"**

#### **Step 2: Create the Matrix**
1. **Drag** `Faculty_A_Method` to **Rows** shelf
2. **Drag** `Faculty_B_Method` to **Columns** shelf
3. **Drag** `Total_Score` to **Text** (in Marks card)
   - This shows the score in each cell

4. **Change aggregation:**
   - Right-click `Total_Score` in Marks card
   - Select **"Measure (Sum)"** → **"Average"**
   - OR click the dropdown arrow on `Total_Score` → **"Average"**

**What you'll see:** A matrix with methods as rows/columns and average scores in cells

#### **Step 3: Format the Matrix**
1. **Format headers:**
   - Right-click row header → **"Format"**
   - **Font:** 11pt, Bold
   - **Alignment:** Left

2. **Format cells:**
   - Click **"Format"** menu → **"Shading"**
   - **Cell background:** White
   - **Border:** Light gray, 1px

3. **Format numbers:**
   - Right-click `Total_Score` in Marks card
   - **"Format"** → **"Numbers"**
   - **Number:** Custom
   - **Decimal places:** 1

4. **Add Title:**
   - **"Worksheet"** → **"Show Title"**
   - Title: **"Method Complementarity Matrix"**
   - Format: 16pt, Bold, Illinois Blue

#### **Step 4: Add Conditional Formatting (Color Scale)**
1. **Drag** `Total_Score` to the **Color** shelf (in Marks card)
2. Click the **Color** shelf → **"Edit Colors"**
3. **Color Palette:** Select **"Red-Green Diverging"**
4. **Stepped Color:** Turn ON
5. **Steps:** 5
6. **Range:**
   - **Start:** 0 (Red)
   - **End:** 100 (Green)
   - **Center:** 50 (Yellow)

**Custom colors:**
1. Click **"Edit Colors"** → **"Custom"**
2. Set colors:
   - **≥85:** Green (#4CAF50)
   - **70-85:** Light Green (#81C784)
   - **50-70:** Yellow (#FFC107)
   - **<50:** Red (#E81123)

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

#### **Step 1: Create New Worksheet**
1. Click **"New Worksheet"** icon
2. Name it: **"Score Breakdown"**

#### **Step 2: Create Stacked Bar Chart**
1. **Create Match Pair:**
   - Right-click in Data pane → **"Create Calculated Field"**
   - Name: **"Match Pair"**
   - Formula: `[Faculty_A_Name] + " ↔ " + [Faculty_B_Name]`
   - Click **OK**

2. **Drag** `Match Pair` to **Rows** shelf

3. **Drag** `Topic_Score` to **Columns** shelf
   - Right-click → **"Measure (Sum)"** → **"Average"**

4. **Drag** `Method_Score` to **Columns** shelf (next to Topic_Score)
   - Right-click → **"Average"**

5. **Drag** `Stage_Score` to **Columns** shelf (next to Method_Score)
   - Right-click → **"Average"**

**What you'll see:** Three separate bars for each match

**To stack them:**
1. Click **"Show Me"** (top right) → Select **"Stacked Bar Chart"**
2. OR manually: Drag all three scores to same axis

**Better approach - Stacked:**
1. **Drag** `Match Pair` to **Rows** shelf
2. **Drag** `Topic_Score` to **Columns** shelf → Set to **Average**
3. **Drag** `Method_Score` to **Columns** shelf → Set to **Average**
4. **Drag** `Stage_Score` to **Columns** shelf → Set to **Average**
5. Click on **"Show Me"** → Select **"Stacked Bar Chart"**

#### **Step 3: Filter to Top Matches**
1. **Drag** `Total_Score` to **Filters** shelf
2. Select **"Top"** tab
3. **By field:** Top **15**
4. Click **OK**

#### **Step 4: Format the Chart**
1. **Add Title:**
   - **"Worksheet"** → **"Show Title"**
   - Title: **"Compatibility Score Breakdown"**
   - Format: 16pt, Bold

2. **Format colors:**
   - Click on **Color** shelf (in Marks card)
   - **Edit Colors:**
     - `Topic_Score`: Illinois Blue (#13294B)
     - `Method_Score`: Illinois Orange (#FF6B35)
     - `Stage_Score`: Green (#4CAF50)

3. **Add Legend:**
   - **"Worksheet"** → **"Show Legend"**
   - Legend title: **"Score Components"**
   - Position: Top or Right

4. **Format axes:**
   - Right-click X-axis → **"Format Axis"**
   - **Title:** "Score (0-100)"
   - **Font:** 11pt

   - Right-click Y-axis → **"Format Axis"**
   - **Title:** "Researcher Pairs"
   - **Font:** 11pt

5. **Add data labels:**
   - **"Analysis"** menu → **"Stack Marks"** → **"On"**
   - Right-click chart → **"Show Mark Labels"**

#### **Step 5: Update Field Labels**
1. Right-click `Topic_Score` in Data pane
2. **"Rename"** → **"Topic (50%)"**
3. Repeat for:
   - `Method_Score` → **"Method (35%)"**
   - `Stage_Score` → **"Stage (15%)"**

**✅ DONE!** You now have a stacked bar chart showing score components!

---

## 📊 **VISUALIZATION 4: MATCH QUALITY DISTRIBUTION (PIE CHART)**

### **Purpose:** Show distribution of match quality

### **Step-by-Step:**

#### **Step 1: Create New Worksheet**
1. Click **"New Worksheet"** icon
2. Name it: **"Match Quality Distribution"**

#### **Step 2: Create Pie Chart**
1. **Drag** `Match_Quality` to **Color** shelf (in Marks card)
2. **Drag** `Total_Score` to **Angle** shelf (in Marks card)
   - Right-click → **"Measure (Sum)"** → **"Count"**

3. **Click "Show Me"** → Select **"Pie Chart"**

**What you'll see:** A pie chart with slices for each quality level

#### **Step 3: Format the Pie Chart**
1. **Add Title:**
   - **"Worksheet"** → **"Show Title"**
   - Title: **"Match Quality Distribution"**
   - Format: 16pt, Bold

2. **Format colors:**
   - Click **Color** shelf → **"Edit Colors"**
   - Set colors:
     - **Excellent:** Green (#4CAF50)
     - **Good:** Illinois Blue (#13294B)
     - **Moderate:** Yellow (#FFC107)
     - **Low:** Gray (#9E9E9E)

3. **Add labels:**
   - **Drag** `Match_Quality` to **Label** shelf (in Marks card)
   - **Drag** `Total_Score` to **Label** shelf → Set to **Count**
   - Right-click label → **"Format"**
   - **Show:** Category, Value, Percentage
   - **Position:** Outside

4. **Add Legend:**
   - **"Worksheet"** → **"Show Legend"**
   - Legend title: **"Quality"**
   - Position: Right or Bottom

**✅ DONE!** Pie chart showing match quality distribution!

---

## 📊 **VISUALIZATION 5: SUMMARY CARDS (KEY METRICS)**

### **Purpose:** Show key metrics at a glance

### **Step-by-Step:**

#### **Card 1: Total Matches**
1. Create new worksheet: **"Summary Cards"**
2. **Drag** `Total_Score` to **Text** shelf (in Marks card)
3. Right-click → **"Measure (Sum)"** → **"Count"**
4. **Format:**
   - Click **"Format"** menu → **"Shading"**
   - **Background:** Illinois Blue (#13294B)
   - **Border:** None
   - **Text:** White, 48pt, Bold
   - **Alignment:** Center

5. **Add Title:**
   - **"Worksheet"** → **"Show Title"**
   - Title: **"Total Matches"**
   - Format: 14pt, Bold, White

#### **Card 2: Average Compatibility Score**
1. Create new worksheet: **"Average Score Card"**
2. **Drag** `Total_Score` to **Text** shelf
3. Right-click → **"Average"**
4. **Format:**
   - **Background:** Illinois Orange (#FF6B35)
   - **Text:** White, 48pt, Bold
   - **Numbers:** 1 decimal place

5. **Add Title:** **"Average Compatibility"**

#### **Card 3: Excellent Matches**
1. Create new worksheet: **"Excellent Matches Card"**
2. **Drag** `Match_Quality` to **Filters** shelf
3. Select only **"Excellent"**
4. **Drag** `Total_Score` to **Text** shelf → Set to **Count**
5. **Format:**
   - **Background:** Green (#4CAF50)
   - **Text:** White, 48pt, Bold

6. **Add Title:** **"Excellent Matches"**

#### **Card 4: Complementary Methods**
1. Create new worksheet: **"Complementary Card"**
2. **Drag** `Is_Complementary` to **Filters** shelf
3. Select only **"True"**
4. **Drag** `Total_Score` to **Text** shelf → Set to **Count**
5. **Format:**
   - **Background:** Orange (#FF6B35)
   - **Text:** White, 48pt, Bold

6. **Add Title:** **"Complementary Matches"**

**✅ DONE!** Four cards showing key metrics!

---

## 📊 **VISUALIZATION 6: SDG-BASED MATCHING (BAR CHART)**

### **Purpose:** Show which SDGs have best matches

### **Step-by-Step:**

#### **Step 1: Create New Worksheet**
1. Click **"New Worksheet"** icon
2. Name it: **"SDG Compatibility"**

#### **Step 2: Create Bar Chart**
1. **Drag** `SDG` to **Rows** shelf
   - (If SDG is in a different table, you may need to join tables - see Relationships section)

2. **Drag** `Total_Score` to **Columns** shelf
   - Right-click → **"Average"**

#### **Step 3: Sort the Chart**
1. Click on the **`Total_Score`** axis
2. Click **"Sort"** icon (top toolbar)
3. Select **"Descending"**
   - OR right-click `Total_Score` → **"Sort"** → **"Descending"**

#### **Step 4: Format the Chart**
1. **Add Title:**
   - **"Worksheet"** → **"Show Title"**
   - Title: **"Average Compatibility by SDG"**
   - Format: 16pt, Bold

2. **Format colors:**
   - **Drag** `Total_Score` to **Color** shelf
   - **Edit Colors:** Use gradient (Blue to Green)

3. **Add data labels:**
   - **Drag** `Total_Score` to **Label** shelf
   - Right-click label → **"Format"**
   - **Decimal places:** 1

4. **Format axes:**
   - X-axis title: **"Average Compatibility Score"**
   - Y-axis title: **"SDG"**
   - Font: 11pt

**✅ DONE!** Bar chart showing SDG compatibility!

---

## 📊 **VISUALIZATION 7: RESEARCHER SEARCH/FILTER (FILTER)**

### **Purpose:** Let users filter by specific researcher

### **Step-by-Step:**

#### **Step 1: Create Dashboard**
1. Click **"New Dashboard"** icon (bottom left)
2. Name it: **"Collaboration Hub Dashboard"**

#### **Step 2: Add Filter**
1. **Drag** your worksheet (e.g., "Top Matches") to the dashboard
2. In the **Objects** pane (left side), find **"Filter"**
3. **Drag** `Faculty_A_Name` from Data pane to dashboard
   - This creates a filter control

#### **Step 3: Format the Filter**
1. Click on the filter control
2. **Format Filter:**
   - **Style:** Dropdown (easier to use)
   - **Show:** All values
   - **Search:** Enable (if available)

3. **Add Title:**
   - Right-click filter → **"Edit Title"**
   - Title: **"Search by Researcher"**
   - Format: 14pt, Bold

#### **Step 4: Apply Filter to All Sheets**
1. Click on the filter control
2. Click **"..."** (three dots) → **"Apply to Worksheets"**
3. Select **"All using this data source"**
4. Click **OK**

**How it works:** When user selects a researcher, all visuals filter to show only their matches!

**✅ DONE!** Interactive filter created!

---

## 📊 **VISUALIZATION 8: MATCH DETAILS CARDS (SHOW BREAKDOWN)**

### **Purpose:** Show detailed breakdown when a match is selected

### **Step-by-Step:**

#### **Step 1: Create Multiple Card Worksheets**
Create 4 separate worksheets:

#### **Card 1: Total Score**
1. Create worksheet: **"Total Score Card"**
2. **Drag** `Total_Score` to **Text** shelf
3. Right-click → **"Average"**
4. **Format:**
   - **Background:** Illinois Blue (#13294B)
   - **Text:** White, 64pt, Bold
   - **Numbers:** 1 decimal place

5. **Add Title:** **"Compatibility Score"**

#### **Card 2: Topic Score**
1. Create worksheet: **"Topic Score Card"**
2. **Drag** `Topic_Score` to **Text** shelf → **Average**
3. **Format:**
   - **Background:** Blue (#13294B)
   - **Text:** White, 32pt, Bold

4. **Add Title:** **"Topic Match (50%)"**

#### **Card 3: Method Score**
1. Create worksheet: **"Method Score Card"**
2. **Drag** `Method_Score` to **Text** shelf → **Average**
3. **Format:**
   - **Background:** Orange (#FF6B35)
   - **Text:** White, 32pt, Bold

4. **Add Title:** **"Method Match (35%)"**

#### **Card 4: Stage Score**
1. Create worksheet: **"Stage Score Card"**
2. **Drag** `Stage_Score` to **Text** shelf → **Average**
3. **Format:**
   - **Background:** Green (#4CAF50)
   - **Text:** White, 32pt, Bold

4. **Add Title:** **"Stage Match (15%)"**

**How it works:** When user selects a match in the table, these cards show the breakdown!

**✅ DONE!** Score breakdown cards created!

---

## 🎨 **DASHBOARD LAYOUT & FORMATTING**

### **Step 1: Create Dashboard**
1. Click **"New Dashboard"** icon
2. Name it: **"Collaboration Hub - Compatibility Matching"**

### **Step 2: Add Title**
1. In **Objects** pane, find **"Text"**
2. **Drag** text box to top of dashboard
3. Double-click → Type: **"Collaboration Hub - Compatibility Matching"**
4. **Format:**
   - **Font:** 24pt, Bold
   - **Color:** Illinois Blue (#13294B)
   - **Alignment:** Center

### **Step 3: Arrange Visuals**
1. **Drag** worksheets from left pane to dashboard:
   - **Top row:** Summary Cards (4 cards side by side)
   - **Second row:** Top Matches Table (full width)
   - **Third row:** Method Complementarity Matrix + Match Quality Pie Chart
   - **Fourth row:** Score Breakdown Chart (full width)
   - **Fifth row:** SDG Bar Chart + Researcher Filter

2. **Resize visuals:**
   - Click and drag corners to resize
   - Use **"Tiled"** layout (default) for clean alignment

### **Step 4: Apply Consistent Formatting**
1. **Dashboard background:**
   - **"Format"** menu → **"Dashboard"**
   - **Background:** White or Light gray (#F5F5F5)

2. **Visual backgrounds:**
   - Click each visual → **"Format"** → **"Shading"**
   - **Background:** White
   - **Border:** Light gray, 1px

3. **Spacing:**
   - **"Format"** → **"Layout"**
   - **Padding:** 10px between visuals

---

## 🔗 **CREATING RELATIONSHIPS (IF NEEDED)**

If you're using multiple data sources:

### **Step 1: Add Second Data Source**
1. **"Data"** menu → **"New Data Source"**
2. Select your second sheet (e.g., `Researcher_Profiles_For_PowerBI`)
3. Click **"Add to Sheet"**

### **Step 2: Create Relationship**
1. **"Data"** menu → **"Edit Relationships"**
2. Click **"Add"**
3. **Primary Data Source:** Select first table
4. **Secondary Data Source:** Select second table
5. **Join Fields:**
   - Match on common field (e.g., `Faculty_A_Name` = `Name`)
6. **Join Type:** Left Join (or Inner Join)
7. Click **OK**

### **Step 3: Blend Data**
1. When using fields from both sources, Tableau will automatically blend
2. Look for **"Link"** icon in Data pane (indicates blended data)
3. If needed, **"Data"** menu → **"Edit Relationships"** to adjust

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

### **Filter:**
- [ ] Can select a researcher
- [ ] Other visuals filter when researcher selected
- [ ] Search works (if enabled)

---

## 🚨 **COMMON ISSUES & SOLUTIONS**

### **Problem: "Can't see data in Data pane"**
**Solution:**
- Make sure you've connected to your Excel file
- Check that you've dragged the sheet to the canvas in Data Source view
- Try refreshing: **"Data"** → **"Refresh"**

### **Problem: "Visual shows wrong data"**
**Solution:**
- Check aggregation (Sum vs Average vs Count)
- Right-click field → Check measure type
- Verify you're using the right field

### **Problem: "Can't sort table"**
**Solution:**
- Click on the column header
- Look for sort icon (up/down arrows)
- OR right-click field → **"Sort"**

### **Problem: "Conditional formatting not working"**
**Solution:**
- Make sure field is on **Color** shelf
- Check that values are numeric (not text)
- Try **"Edit Colors"** → **"Stepped Color"**

### **Problem: "Filter doesn't affect other visuals"**
**Solution:**
- Make sure filter is on **Dashboard** (not individual worksheet)
- Check **"Apply to Worksheets"** setting
- Verify all worksheets use same data source

### **Problem: "Can't create relationships"**
**Solution:**
- Use **Data Blending** instead (Tableau's automatic feature)
- Make sure common field exists in both tables
- Check field names match exactly

---

## 🎯 **TABLEAU vs POWER BI: KEY DIFFERENCES**

| Feature | Tableau | Power BI |
|---------|---------|----------|
| **Data Import** | Excel, CSV, databases | Excel, CSV, databases |
| **Relationships** | Automatic blending | Manual relationships |
| **Visual Creation** | Drag-and-drop (very intuitive) | Click icons + drag fields |
| **Conditional Formatting** | Color shelf (very flexible) | Rules-based (more limited) |
| **Filtering** | Filters shelf (works everywhere) | Visual-level filters |
| **Calculations** | Calculated fields (formula-based) | DAX measures (more complex) |
| **Export Quality** | Excellent (high-res) | Good |
| **Mac Support** | Native ✅ | Desktop: No, Web: Yes |
| **Free Version** | Tableau Public (with limitations) | Power BI Service (limited) |

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

3. **Use the Filter:**
   - Select a researcher
   - Show how other visuals update
   - Demonstrate interactivity

4. **Explain Score Breakdown:**
   - "Each match has three components"
   - "Topic is 50%, Method is 35%, Stage is 15%"
   - "This matches the professor's criteria"

### **Exporting for Presentation:**
1. **Export as Image:**
   - **"Worksheet"** → **"Export"** → **"Image"**
   - High resolution PNG

2. **Export Dashboard:**
   - **"Dashboard"** → **"Export Image"**
   - Full dashboard as image

3. **Export as PDF:**
   - **"File"** → **"Print to PDF"**
   - Good for submission

4. **Publish to Tableau Public:**
   - **"Server"** → **"Tableau Public"** → **"Save to Tableau Public"**
   - Get shareable link (public, but fine for case competition)

---

## 🎨 **ILLINOIS BRANDING COLORS**

Use these colors throughout:

- **Primary Blue:** #13294B (headers, primary text)
- **Orange:** #FF6B35 (highlights, CTAs, Method scores)
- **Green:** #4CAF50 (success, high scores, Stage scores)
- **Yellow:** #FFC107 (moderate scores, warnings)
- **Gray:** #9E9E9E (low scores, secondary text)

**To set custom colors in Tableau:**
1. Click **Color** shelf → **"Edit Colors"**
2. Select **"Custom"**
3. Click color → Enter hex code (e.g., #13294B)

---

## 🚀 **QUICK START CHECKLIST**

- [ ] Tableau Desktop/Public installed
- [ ] `Collab_Hub_Data.xlsx` file ready
- [ ] Data connected in Tableau
- [ ] Top Matches Table created
- [ ] Method Complementarity Matrix created
- [ ] Score Breakdown Chart created
- [ ] Match Quality Pie Chart created
- [ ] Summary Cards created
- [ ] SDG Bar Chart created
- [ ] Researcher Filter added
- [ ] Dashboard layout finalized
- [ ] Colors formatted (Illinois branding)
- [ ] All visuals validated

---

**Follow these steps exactly, and you'll have a professional Collaboration Hub dashboard in Tableau!** 🚀

**Tableau is often easier and more flexible than Power BI - you'll love it!**

Start with Visualization 1 (Top Matches Table) - it's the foundation!



