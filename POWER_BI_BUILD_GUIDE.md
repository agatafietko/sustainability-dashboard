# Power BI Dashboard Build Guide
## University of Illinois Research Impact Dashboard

---

## 📋 PRE-REQUISITES

✅ **Power BI Desktop** installed (free download from Microsoft)  
✅ **Data files ready** (created by the Python script):
   - `Publications_cleaned.csv`
   - `Keywords_cleaned.csv`
   - `SDG_Mappings_cleaned.csv`
   - `sdg_lookup.csv`

---

## 🚀 STEP-BY-STEP BUILD PROCESS

### **STEP 1: Import Data into Power BI**

1. Open **Power BI Desktop**
2. Click **Get Data** → **Text/CSV**
3. Navigate to your folder and import **ALL 4 CSV files**:
   - `sdg_lookup.csv`
   - `Publications_cleaned.csv`
   - `Keywords_cleaned.csv`
   - `SDG_Mappings_cleaned.csv`

4. For each file:
   - Click **Transform Data** (or **Edit** in Power Query Editor)
   - Verify the data looks correct
   - Click **Close & Apply**

---

### **STEP 2: Create Relationships**

1. Click the **Model** view icon (left sidebar, looks like 3 connected circles)

2. Create relationships by dragging between tables:

   **Primary Relationship:**
   - `Publications[article_uuid]` → `SDG_Mappings[article_uuid]` (Many-to-One)
   - `Publications[article_uuid]` → `Keywords[article_uuid]` (Many-to-One)
   - `SDG_Mappings[SDG ID]` → `sdg_lookup[SDG ID]` (Many-to-One)

3. **Verify relationships:**
   - Right-click each relationship → **Properties**
   - Ensure **Cardinality** is correct
   - Ensure **Cross-filter direction** is set to **Both** (for bidirectional filtering)

---

### **STEP 3: Add DAX Measures**

1. Go to **Data** view (left sidebar, table icon)
2. Select the **Publications** table
3. Click **New Measure** (Home ribbon)
4. Copy measures from `DAX_Measures.txt` one by one:

   **Start with these core measures:**
   - `Total Publications`
   - `Sustainable Publications`
   - `Sustainable %`
   - `Recent Publications`
   - `Recent Sustainable`
   - `Impact Story`

5. Repeat for other measures as needed

---

### **STEP 4: Build Dashboard Pages**

#### **PAGE 1: Overview Dashboard**

1. Create new page: **Right-click** in Pages panel → **New Page**
2. Rename: **Double-click** page name → "Overview"

3. **Add KPI Cards (Top Row):**
   - Insert → **Card** visual
   - Drag measure: `Total Publications`
   - Format: Large font, add title
   - Repeat for:
     - `Sustainable Publications`
     - `Sustainable %`
     - `Recent Sustainable`

4. **Add Slicers (Left Sidebar):**
   - Insert → **Slicer** visual
   - Add slicers for:
     - `Publications[department]` (Dropdown)
     - `Publications[publication_year]` (Between)
     - `sdg_lookup[SDG Name]` (Dropdown)
     - `Keywords[keyword]` (Search)

5. **Add Trend Line Chart:**
   - Insert → **Line chart**
   - X-axis: `Publications[publication_year]`
   - Y-axis: `Total Publications` and `Sustainable Publications`
   - Format: Add title "Publications Over Time"

6. **Add Department Bar Chart:**
   - Insert → **Bar chart** (horizontal)
   - Y-axis: `Publications[department]`
   - X-axis: `Sustainable by Department`
   - Sort: Descending
   - Format: Add title "Top Departments by Sustainable Research"

7. **Add SDG Coverage:**
   - Insert → **Bar chart** (vertical)
   - X-axis: `sdg_lookup[SDG Name]`
   - Y-axis: `Publications by SDG`
   - Sort: Descending
   - Format: Add title "Research Coverage by SDG"

---

#### **PAGE 2: SDG Explorer**

1. Create new page: **"SDG Explorer"**

2. **Add Matrix Heatmap:**
   - Insert → **Matrix** visual
   - Rows: `Publications[department]`
   - Columns: `sdg_lookup[SDG Name]`
   - Values: `Total Publications`
   - Format → Conditional formatting → Color scale
     - Minimum: Light color
     - Maximum: Dark color
   - Format → Title: "SDG Coverage by Department"

3. **Add Network Graph (Optional - requires custom visual):**
   - Click **...** (More visuals) → **Get more visuals**
   - Search for "Network Navigator" or "Chord Chart"
   - Install if needed
   - Use: Department ↔ SDG relationships

4. **Add SDG Slicer:**
   - Insert → **Slicer**
   - Field: `sdg_lookup[SDG Name]` (Multi-select)

5. **Add Publications Table:**
   - Insert → **Table** visual
   - Columns: `title`, `name`, `department`, `publication_year`, `SDG Name`
   - Add filter: Only show when SDG is selected

---

#### **PAGE 3: Impact Stories**

1. Create new page: **"Impact Stories"**

2. **Add Publications Table:**
   - Insert → **Table** visual
   - Columns:
     - `title`
     - `name`
     - `department`
     - `publication_year`
     - `is_sustain` (as icon)
   - Format: Make rows clickable/selectable

3. **Add Impact Story Card:**
   - Insert → **Card** or **Text box** visual
   - Drag measure: `Impact Story`
   - Format: 
     - Large font (12-14pt)
     - Multi-line enabled
     - Background: Light color
   - Position: Right side of page

4. **Add Filters:**
   - Department slicer
   - Year slicer
   - SDG slicer
   - Keyword search

5. **Instructions Text:**
   - Insert → **Text box**
   - Add: "👆 Click on a publication in the table to view its Impact Story"

---

#### **PAGE 4: Department Detail (Drillthrough)**

1. Create new page: **"Department Detail"**

2. **Set up Drillthrough:**
   - Right-click page → **Page Tools** → Enable **Drillthrough**
   - Add drillthrough field: `Publications[department]`

3. **Add Visuals:**
   - **Card**: `Total Publications` (filtered by department)
   - **Card**: `Sustainable by Department`
   - **Line Chart**: Publications over time (filtered)
   - **Table**: All publications from department
   - **Bar Chart**: SDG distribution for department

---

### **STEP 5: Formatting & Styling**

1. **Apply Theme:**
   - View → **Themes** → Choose a theme (or create custom)
   - Use Illinois colors (Orange/Blue) if desired

2. **Format Visuals:**
   - Select each visual → **Format** pane
   - Add titles, adjust colors, fonts
   - Ensure consistent styling across pages

3. **Page Layout:**
   - Arrange visuals logically
   - Use alignment guides
   - Group related visuals

4. **Add Navigation:**
   - Insert → **Buttons** → **Navigation**
   - Link buttons to different pages
   - Or use **Bookmarks** for preset views

---

### **STEP 6: Advanced Features (Optional)**

#### **Word Cloud:**
1. Get custom visual: **Word Cloud**
2. Add: `Keywords[keyword]` as data
3. Size by: Count of publications

#### **Trend Analysis:**
1. Add **Analytics** pane to line chart
2. Enable: Forecast, Trend line

#### **Bookmarks:**
1. Create bookmarks for preset views:
   - "SDG 3 Focus" (filter to SDG 3)
   - "Last 5 Years" (filter to recent)
   - "Top Departments"

---

### **STEP 7: Test & Validate**

1. **Test Slicers:**
   - Select different departments
   - Filter by year ranges
   - Select SDGs
   - Verify all visuals update correctly

2. **Test Impact Story:**
   - Click different publications
   - Verify story updates
   - Check formatting

3. **Check Performance:**
   - View → **Performance Analyzer**
   - Identify slow visuals
   - Optimize if needed

---

### **STEP 8: Publish & Share**

1. **Save PBIX file:**
   - File → **Save As**
   - Name: "Illinois_Research_Impact_Dashboard.pbix"

2. **Publish to Power BI Service (optional):**
   - Home → **Publish**
   - Sign in to Power BI account
   - Select workspace

3. **Export to PDF (for submission):**
   - File → **Export** → **Export to PDF**
   - Select pages to export

---

## 📊 DASHBOARD STRUCTURE SUMMARY

```
📄 Overview Dashboard
   ├── KPI Cards (4)
   ├── Slicers (Department, Year, SDG, Keyword)
   ├── Trend Line Chart
   ├── Department Bar Chart
   └── SDG Coverage Chart

📄 SDG Explorer
   ├── Matrix Heatmap (Dept × SDG)
   ├── Network Graph (optional)
   ├── SDG Slicer
   └── Publications Table

📄 Impact Stories
   ├── Publications Table
   ├── Impact Story Card (dynamic)
   └── Filters

📄 Department Detail (Drillthrough)
   ├── Department KPIs
   ├── Trend Chart
   ├── Publications Table
   └── SDG Distribution
```

---

## 🎯 KEY TIPS FOR CASE COMPETITION

1. **Tell a Story:**
   - Start with Overview → Show trends → Drill into Impact Stories
   - Use bookmarks to create a narrative flow

2. **Highlight Impact:**
   - Feature the Impact Story card prominently
   - Showcase SDG 3 (Good Health) - your strongest area

3. **Demonstrate Interactivity:**
   - Record a short video showing slicers and filters
   - Show how Impact Story updates dynamically

4. **Show Process:**
   - Include a slide/page on data preparation
   - Document cleaning steps

5. **Quantify Value:**
   - 397 sustainable publications (20.9%)
   - 15 SDGs covered
   - Top department: Business Administration (244 sustainable pubs)

---

## 🐛 TROUBLESHOOTING

**Issue: Impact Story shows "Select a publication"**
- ✅ Ensure you clicked on a row in the table
- ✅ Check that `HASONEVALUE(Publications[article_uuid])` is working

**Issue: Relationships not working**
- ✅ Verify cardinality in Model view
- ✅ Check cross-filter direction is "Both"

**Issue: Measures return blank**
- ✅ Check for filters affecting the calculation
- ✅ Verify data types match

**Issue: Slow performance**
- ✅ Reduce data size (filter early years if needed)
- ✅ Use aggregation in visuals instead of detail rows

---

## ✅ FINAL CHECKLIST

- [ ] All 4 data files imported
- [ ] Relationships created correctly
- [ ] Core DAX measures added
- [ ] All 4 pages created with visuals
- [ ] Slicers working across all pages
- [ ] Impact Story updates when selecting publications
- [ ] Formatting consistent and professional
- [ ] Dashboard saved as .pbix file
- [ ] Tested with different filter combinations
- [ ] Ready for submission!

---

## 📞 NEXT STEPS

1. Follow steps 1-8 above
2. Customize visuals and colors
3. Add your own insights and annotations
4. Create presentation slides highlighting key findings
5. Record a 2-3 minute demo video

**Good luck with your case competition! 🎉**





