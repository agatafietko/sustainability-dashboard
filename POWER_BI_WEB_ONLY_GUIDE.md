# Power BI Web-Only Guide
## Building Collaboration Hub Dashboard Without Desktop

---

## 🎯 **STEP 1: Upload CSV Files to Power BI Service**

### **Method A: Direct Upload (Easiest)**

1. Go to **https://app.powerbi.com**
2. Sign in with your Microsoft account (or create free account)
3. Click **"My workspace"** (or create a new workspace)
4. Click **"+ New"** → **"File upload"**
5. Upload all 3 CSV files:
   - `Collab_Matches_For_PowerBI.csv`
   - `Researcher_Profiles_For_PowerBI.csv`
   - `sdg_lookup.csv` (if you have it)

6. Wait for files to upload (you'll see them in "Files" section)

---

### **Method B: Upload to OneDrive First (More Reliable)**

1. **Upload to OneDrive:**
   - Go to **https://onedrive.live.com**
   - Upload your 3 CSV files to a folder
   - Right-click each file → **"Details"** → Copy the file path

2. **Connect from Power BI:**
   - In Power BI Service, click **"+ New"** → **"Dataset"**
   - Select **"OneDrive"** or **"Files"**
   - Navigate to your files and select them
   - Click **"Connect"**

---

## 🎯 **STEP 2: Create a Dataset**

1. In Power BI Service, click **"+ New"** → **"Dataset"**
2. Select **"Upload a file"** or **"OneDrive"**
3. Choose your CSV files:
   - Start with `Collab_Matches_For_PowerBI.csv`
   - Power BI will create a dataset automatically

4. **For additional files:**
   - You may need to create separate datasets for each file
   - OR combine them in Excel first (see Step 3 alternative)

---

## 🎯 **STEP 3: Combine Files in Excel First (RECOMMENDED)**

Since Power BI Web has limited relationship capabilities, **combine your data in Excel first:**

### **Option A: Create One Combined Excel File**

1. **Open Excel**
2. **Create 3 sheets:**
   - Sheet 1: Name it "Matches" → Import `Collab_Matches_For_PowerBI.csv`
   - Sheet 2: Name it "Researchers" → Import `Researcher_Profiles_For_PowerBI.csv`
   - Sheet 3: Name it "SDG_Lookup" → Import `sdg_lookup.csv` (if you have it)

3. **Save as Excel file:** `Collab_Hub_Data.xlsx`

4. **Upload to Power BI:**
   - In Power BI Service, click **"+ New"** → **"File upload"**
   - Upload `Collab_Hub_Data.xlsx`
   - Power BI will automatically create a dataset with all sheets

---

## 🎯 **STEP 4: Create a Report**

1. In Power BI Service, find your dataset
2. Click **"Create report"** (or click the dataset name)
3. You'll see a blank canvas

---

## 🎯 **STEP 5: Build Visualizations (Web Interface)**

### **Visualization 1: Top Matches Table**

1. Click **"Table"** icon in Visualizations pane
2. In **Fields** pane, expand your dataset
3. Drag these fields to **Values**:
   - `Faculty_A_Name`
   - `Faculty_B_Name`
   - `Total_Score`
   - `Topic_Score`
   - `Method_Score`
   - `Stage_Score`

4. **Sort:**
   - Click on `Total_Score` column header
   - Click **"Sort descending"**

5. **Filter:**
   - Click **"..."** (three dots) on the visual
   - Select **"Filter"**
   - Set `Total_Score` to show top 20

6. **Format:**
   - Click **Format** (paint roller icon)
   - Add title: "Top Collaboration Matches"
   - Enable **Conditional formatting** for `Total_Score`:
     - 85-100: Green
     - 70-84: Light green
     - 55-69: Yellow
     - <55: Gray

---

### **Visualization 2: Method Complementarity Matrix**

1. Click **"Matrix"** icon
2. Drag `Faculty_A_Method` to **Rows**
3. Drag `Faculty_B_Method` to **Columns**
4. Drag `Total_Score` to **Values** (set to Average)

5. **Format:**
   - Title: "Method Complementarity Matrix"
   - Enable **Conditional formatting**:
     - Color scale: Green (high) to Red (low)
   - **Key insight:** Look for Theoretical + Empirical = High scores!

---

### **Visualization 3: Score Breakdown Chart**

1. Click **"Stacked bar chart"** icon
2. Drag `Faculty_A_Name` to **Axis** (or create a calculated column for "Match Pair")
3. Drag to **Values**:
   - `Topic_Score` (set to Average)
   - `Method_Score` (set to Average)
   - `Stage_Score` (set to Average)

4. **Format:**
   - Title: "Compatibility Score Breakdown"
   - Colors: Blue (Topic), Orange (Method), Green (Stage)
   - Add legend

---

### **Visualization 4: Match Quality Distribution**

1. Click **"Pie chart"** icon
2. Create a calculated column first:
   - In **Fields** pane, right-click your dataset
   - Select **"New column"**
   - Name: `Match_Quality`
   - Formula:
   ```
   Match_Quality = 
   IF([Total_Score] >= 85, "Excellent",
   IF([Total_Score] >= 70, "Good",
   IF([Total_Score] >= 55, "Moderate", "Low")))
   ```

3. Drag `Match_Quality` to **Legend**
4. Drag `Total_Score` to **Values** (Count)

5. **Format:**
   - Title: "Match Quality Distribution"
   - Colors: Green (Excellent), Blue (Good), Yellow (Moderate), Gray (Low)

---

## 🎯 **STEP 6: Create Relationships (If Using Multiple Datasets)**

If you uploaded separate CSV files:

1. Click **"Model"** view (left sidebar, 3 circles icon)
2. You should see your datasets
3. **Create relationships:**
   - Drag `Faculty_A_Name` from Matches dataset
   - Drop on `name` in Researchers dataset
   - Set to **Many-to-One**
   - Enable **Cross-filter direction: Both**

4. Repeat for `Faculty_B_Name`

**Note:** Power BI Web has limited relationship editing. If this doesn't work, use the Excel method (Step 3) instead.

---

## 🎯 **STEP 7: Format Your Dashboard**

1. **Add title:**
   - Click **"Text box"** icon
   - Type: "Collaboration Hub - Compatibility Matching"
   - Format: Large, bold, Illinois Blue (#13294B)

2. **Arrange visuals:**
   - Drag visuals to arrange them
   - Resize as needed

3. **Add filters:**
   - Click **"Slicer"** icon
   - Drag `Faculty_A_Name` to slicer
   - Users can filter by researcher

---

## ⚠️ **LIMITATIONS OF POWER BI WEB**

**What you CAN'T do easily:**
- Complex data transformations
- Advanced DAX measures (limited)
- Some relationship configurations
- Custom visuals (limited selection)

**What you CAN do:**
- Basic visualizations (tables, charts, matrices)
- Simple filters and slicers
- Conditional formatting
- Basic calculations

---

## 💡 **ALTERNATIVE: Use Excel + Power BI Web**

**Easier approach:**

1. **Combine data in Excel:**
   - Open Excel
   - Import all 3 CSV files as separate sheets
   - Use VLOOKUP or Power Query to combine if needed
   - Save as `.xlsx`

2. **Upload Excel to Power BI:**
   - Upload the Excel file
   - Power BI automatically creates relationships between sheets
   - Build visualizations from the combined data

---

## ✅ **QUICK CHECKLIST**

- [ ] CSV files uploaded to Power BI Service
- [ ] Dataset created
- [ ] Report created
- [ ] Top matches table built
- [ ] Method complementarity matrix created
- [ ] Score breakdown chart added
- [ ] Dashboard formatted
- [ ] Filters added

---

## 🚨 **TROUBLESHOOTING**

### **Problem: Can't create relationships**
**Solution:** Use Excel method - combine files first, then upload

### **Problem: Visualizations look wrong**
**Solution:** Check that you're using the right aggregation (Average, Count, Sum)

### **Problem: Can't see all fields**
**Solution:** Make sure you uploaded the correct CSV file with all columns

### **Problem: Data not updating**
**Solution:** Click **"Refresh"** on your dataset, or re-upload files

---

## 🎯 **RECOMMENDED WORKFLOW**

1. **Combine in Excel first** (easiest)
2. **Upload Excel file** to Power BI
3. **Create report** from the dataset
4. **Build visualizations**
5. **Format and share**

---

**Even without Desktop, you can build a great dashboard in Power BI Web!** 🚀

Start with Step 3 (combine in Excel) - it's the easiest approach.



