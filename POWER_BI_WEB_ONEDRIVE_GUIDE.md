# Power BI Service (Web) with OneDrive - Step-by-Step Guide

## 🎯 Perfect for Mac Users!

This guide will walk you through creating your dashboard using Power BI Service (web) with OneDrive.

---

## 📋 **PRE-REQUISITES**

✅ Microsoft account (free - use Outlook.com or existing Microsoft account)  
✅ Your 4 cleaned CSV files ready:
   - `sdg_lookup.csv`
   - `Publications_cleaned.csv`
   - `Keywords_cleaned.csv`
   - `SDG_Mappings_cleaned.csv`

---

## **STEP 1: Upload CSV Files to OneDrive** (10 minutes)

### 1.1 Access OneDrive
1. Open browser (Safari, Chrome, or Firefox)
2. Go to: **https://onedrive.live.com**
3. Sign in with your Microsoft account
   - Don't have one? Create free at https://signup.live.com

### 1.2 Create Folder
1. Click **+ New** → **Folder**
2. Name it: **"Power BI Dashboard Data"**
3. Click **Create**

### 1.3 Upload CSV Files
1. Open the folder you just created
2. Click **Upload** → **Files**
3. Navigate to: `/Users/meryem/Documents/Case Competition/`
4. Select all 4 CSV files:
   - `sdg_lookup.csv`
   - `Publications_cleaned.csv`
   - `Keywords_cleaned.csv`
   - `SDG_Mappings_cleaned.csv`
5. Click **Open**
6. Wait for uploads to complete (should see 4 files)

**✅ Step 1 Complete!** You should see 4 CSV files in your OneDrive folder.

---

## **STEP 2: Access Power BI Service** (2 minutes)

1. Go to: **https://app.powerbi.com**
2. Sign in with **same Microsoft account** you used for OneDrive
3. If first time, you may need to:
   - Accept terms
   - Choose workspace (select **My Workspace** - free tier)

**✅ Step 2 Complete!** You're now in Power BI Service.

---

## **STEP 3: Create Main Dataset** (10 minutes)

### 3.1 Create Dataset from Publications
1. In Power BI, click **+ New** (top left)
2. Select **Dataset**
3. Choose **OneDrive for Business** or **Files** (may show as "OneDrive - Personal")
4. Navigate to your **"Power BI Dashboard Data"** folder
5. Select **`Publications_cleaned.csv`**
6. Click **Create**

### 3.2 Load Data
1. You'll see a preview of your data
2. Click **Load** (or **Transform data** if you want to edit)
3. Wait for data to load (may take 1-2 minutes)

### 3.3 Create Report
1. After dataset loads, you'll see options
2. Click **Create Report** (or click the dataset name)
3. This opens the report canvas

**✅ Step 3 Complete!** You now have your main dataset loaded.

---

## **STEP 4: Add Additional Data Sources** (15 minutes)

⚠️ **Important**: Power BI Service has limitations with multiple CSV relationships. We'll use a workaround.

### Option A: Create Separate Datasets (Simpler, but limited relationships)

For each remaining CSV:
1. Click **+ New** → **Dataset**
2. Select **OneDrive**
3. Upload and create:
   - `sdg_lookup.csv`
   - `Keywords_cleaned.csv`
   - `SDG_Mappings_cleaned.csv`

**Note**: These will be separate datasets. Relationships between datasets are limited in web version.

### Option B: Combine Data in Excel First (Recommended Workaround)

**Better approach**: Create a combined Excel file:

1. **Download Excel Online** (or use Excel if you have it):
   - Go to https://www.office.com
   - Click **Excel**
   - Create new workbook

2. **Import Data**:
   - In Excel, go to **Data** → **Get Data** → **From File** → **From Text/CSV**
   - Connect to OneDrive and import each CSV
   - Or copy-paste data from CSV files

3. **Create Relationships**:
   - Create separate sheets for each table:
     - Sheet 1: Publications
     - Sheet 2: SDG_Mappings
     - Sheet 3: sdg_lookup
     - Sheet 4: Keywords

4. **Save to OneDrive**:
   - Save as: `Power_BI_Combined_Data.xlsx`
   - Upload to same OneDrive folder

5. **Import to Power BI**:
   - In Power BI Service, **+ New** → **Dataset**
   - Choose **OneDrive**
   - Select `Power_BI_Combined_Data.xlsx`
   - Power BI will recognize multiple sheets
   - You can create relationships between sheets!

**✅ Step 4 Complete!** You now have your data in Power BI.

---

## **STEP 5: Create Relationships** (10 minutes)

### If Using Excel File (Recommended):
1. In Power BI, go to **Model** view (left sidebar)
2. You should see your tables/sheets
3. Drag connections:
   - `Publications[article_uuid]` → `SDG_Mappings[article_uuid]`
   - `Publications[article_uuid]` → `Keywords[article_uuid]`
   - `SDG_Mappings[SDG ID]` → `sdg_lookup[SDG ID]`

### If Using Separate Datasets:
⚠️ Relationships between datasets are limited. You may need to:
- Use calculated columns
- Or work with single dataset at a time

**✅ Step 5 Complete!** Relationships are set up.

---

## **STEP 6: Create Measures** (15 minutes)

### 6.1 Access Data View
1. Click **Data** icon (left sidebar)
2. Select the **Publications** table (or your main table)

### 6.2 Create Measures
1. Click **New Measure** (top ribbon)
2. Copy measures from `DAX_Measures.txt` one by one:

**Start with these essential measures:**

```DAX
Total Publications = COUNTROWS(Publications)
```

```DAX
Sustainable Publications = 
CALCULATE(
    [Total Publications],
    Publications[is_sustain] = TRUE()
)
```

```DAX
Sustainable % = 
DIVIDE(
    [Sustainable Publications],
    [Total Publications],
    0
)
```

```DAX
Recent Publications = 
CALCULATE(
    [Total Publications],
    Publications[is_recent] = TRUE()
)
```

**Note**: Some complex measures may not work in web version. Start simple and add complexity.

**✅ Step 6 Complete!** You have basic measures.

---

## **STEP 7: Build Dashboard - Overview Page** (20 minutes)

### 7.1 Create Visuals

1. **KPI Cards** (Top row):
   - Click **Card** visual (Visualizations pane)
   - Drag `Total Publications` measure
   - Format: Large font, add title
   - Repeat for:
     - `Sustainable Publications`
     - `Sustainable %`
     - `Recent Publications`

2. **Slicers** (Left sidebar):
   - Click **Slicer** visual
   - Add fields:
     - `Publications[department]` (Dropdown)
     - `Publications[publication_year]` (Between)
   - Format: Make them look nice

3. **Trend Line Chart**:
   - Click **Line chart** visual
   - X-axis: `Publications[publication_year]`
   - Y-axis: `Total Publications`
   - Add second measure: `Sustainable Publications`
   - Format: Add title "Publications Over Time"

4. **Department Bar Chart**:
   - Click **Bar chart** (horizontal)
   - Y-axis: `Publications[department]`
   - X-axis: `Total Publications`
   - Sort: Descending
   - Format: Add title "Publications by Department"

5. **SDG Coverage Chart**:
   - Click **Bar chart** (vertical)
   - X-axis: `sdg_lookup[SDG Name]` (if relationship works)
   - Y-axis: `Total Publications`
   - Format: Add title "Research Coverage by SDG"

**✅ Step 7 Complete!** You have your Overview page!

---

## **STEP 8: Create Impact Story Card** (10 minutes)

### 8.1 Create Impact Story Measure

Since web version has limitations, create a simpler version:

```DAX
Impact Story = 
VAR Title = SELECTEDVALUE(Publications[title])
VAR Author = SELECTEDVALUE(Publications[name])
VAR Department = SELECTEDVALUE(Publications[department])
VAR Year = SELECTEDVALUE(Publications[publication_year])
VAR Journal = SELECTEDVALUE(Publications[journal_title])
VAR Abstract = SELECTEDVALUE(Publications[abstract_text])
RETURN
IF(
    HASONEVALUE(Publications[article_uuid]),
    "📊 IMPACT STORY" & UNICHAR(10) & UNICHAR(10) &
    "Title: " & Title & UNICHAR(10) & UNICHAR(10) &
    "Author: " & Author & UNICHAR(10) &
    "Department: " & Department & UNICHAR(10) &
    "Year: " & Year & UNICHAR(10) & UNICHAR(10) &
    IF(NOT ISBLANK(Journal), "Journal: " & Journal & UNICHAR(10) & UNICHAR(10), "") &
    "Why it matters:" & UNICHAR(10) &
    IF(LEN(Abstract) > 500, LEFT(Abstract, 500) & "...", Abstract),
    "👆 Select a publication to view its Impact Story."
)
```

### 8.2 Add Impact Story Card

1. Create **Table** visual with publications
2. Add columns: `title`, `name`, `department`, `year`
3. Create **Card** visual next to it
4. Add `Impact Story` measure
5. Format: Large font, multi-line
6. When you click on table row, story updates!

**✅ Step 8 Complete!** Impact Story is working!

---

## **STEP 9: Add More Pages** (Optional, 15 minutes)

### 9.1 Create New Page
1. Click **+** (bottom left, next to page tabs)
2. Rename: "SDG Explorer"

### 9.2 Add Visuals
- Matrix heatmap (Department × SDG)
- SDG slicer
- Publications table

### 9.3 Create Impact Stories Page
- Table of publications
- Impact Story card
- Filters

**✅ Step 9 Complete!** You have multiple pages!

---

## **STEP 10: Format & Style** (10 minutes)

1. **Apply Theme**:
   - View → **Themes** → Choose a theme
   - Or customize colors

2. **Format Visuals**:
   - Select each visual
   - Format pane → Add titles, adjust colors
   - Make it look professional

3. **Arrange Layout**:
   - Align visuals
   - Use consistent spacing
   - Group related visuals

**✅ Step 10 Complete!** Dashboard is styled!

---

## **STEP 11: Test & Validate** (5 minutes)

1. **Test Slicers**:
   - Select different departments
   - Filter by year ranges
   - Verify visuals update

2. **Test Impact Story**:
   - Click different publications in table
   - Verify story updates

3. **Check Numbers**:
   - Verify totals match expectations
   - Check percentages make sense

**✅ Step 11 Complete!** Dashboard is tested!

---

## **STEP 12: Share & Export** (5 minutes)

### 12.1 Share Dashboard
1. Click **Share** (top right)
2. Enter email or get link
3. Set permissions

### 12.2 Export to PDF (For Submission)
1. Click **File** → **Export** → **PDF**
2. Select pages to export
3. Save PDF

### 12.3 Get Shareable Link
1. Click **Share**
2. Get link
3. Share with judges/team

**✅ Step 12 Complete!** Dashboard is shared!

---

## 🐛 **TROUBLESHOOTING**

### Issue: Can't see relationships
- ✅ Relationships only work if using Excel file with multiple sheets
- ✅ Separate datasets have limited relationship support
- **Solution**: Use Excel file approach (Step 4, Option B)

### Issue: Measures not working
- ✅ Some complex DAX may not work in web version
- ✅ Start with simple measures, add complexity gradually
- **Solution**: Simplify measures, use basic DAX functions

### Issue: Can't import multiple CSVs
- ✅ Web version has limitations
- **Solution**: Use Excel file with multiple sheets (Step 4, Option B)

### Issue: Slow performance
- ✅ Web version can be slower than Desktop
- ✅ Reduce data size if needed
- ✅ Use aggregations instead of detail rows

---

## 📊 **WORKAROUNDS FOR WEB LIMITATIONS**

### Limited Relationships?
- **Solution**: Use Excel file with multiple sheets (Step 4, Option B)
- Relationships work between sheets in same Excel file

### Complex DAX Not Working?
- **Solution**: Simplify measures
- Use basic functions: COUNT, SUM, CALCULATE
- Avoid complex nested functions

### Can't Import All CSVs?
- **Solution**: Combine in Excel first, then import Excel file

---

## ✅ **FINAL CHECKLIST**

- [ ] CSV files uploaded to OneDrive
- [ ] Power BI Service account created
- [ ] Main dataset created (Publications)
- [ ] Additional data added (Excel file or separate datasets)
- [ ] Relationships created (if using Excel)
- [ ] Core measures added
- [ ] Overview page built
- [ ] Impact Story card working
- [ ] Slicers tested
- [ ] Dashboard formatted
- [ ] Exported to PDF or shared

---

## 🎯 **QUICK REFERENCE**

**OneDrive**: https://onedrive.live.com  
**Power BI Service**: https://app.powerbi.com  
**Excel Online**: https://www.office.com → Excel

**Key Steps:**
1. Upload CSVs → OneDrive
2. Create Excel file with multiple sheets (recommended)
3. Import Excel → Power BI Service
4. Create relationships
5. Build dashboard
6. Share/Export

---

## 💡 **PRO TIPS**

1. **Use Excel File**: Combining data in Excel first solves most relationship issues
2. **Start Simple**: Build basic visuals first, add complexity later
3. **Test Frequently**: Check slicers work as you build
4. **Save Often**: Power BI Service auto-saves, but be careful
5. **Use Filters**: Web version filters work well - use them!

---

**You're ready to build! 🎉**

Follow the steps above, and you'll have a working Power BI dashboard in Power BI Service!

**Need help with a specific step?** Let me know!





