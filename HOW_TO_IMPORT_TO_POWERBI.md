# How to Import CSV Files into Power BI
## Step-by-Step Guide for Power BI Service (Web)

---

## 🌐 **METHOD 1: Power BI Service (Web) - Direct Upload**

### **Step 1: Go to Power BI Service**

1. Open your browser
2. Go to **https://app.powerbi.com**
3. Sign in with your Microsoft account (or create a free account)

---

### **Step 2: Upload Your CSV Files**

#### **Option A: Upload Individual Files**

1. Click **"+ New"** (top right)
2. Select **"File upload"**
3. Click **"Browse"** or drag and drop your CSV file
4. Upload these files one by one:
   - `Collab_Matches_For_PowerBI.csv`
   - `Researcher_Profiles_For_PowerBI.csv`
   - `network_graph_data.csv` (optional)

5. Wait for each file to upload (you'll see a progress bar)

**Note:** Power BI will create a dataset automatically for each file.

---

#### **Option B: Upload as Excel (RECOMMENDED - Easier Relationships)**

**This is easier because Power BI automatically links sheets in the same Excel file!**

1. **Open Excel**
2. **Create a new workbook**
3. **Import your CSV files as separate sheets:**
   - Sheet 1: Name it "Matches" → Import `Collab_Matches_For_PowerBI.csv`
   - Sheet 2: Name it "Researchers" → Import `Researcher_Profiles_For_PowerBI.csv`
   - Sheet 3: Name it "Network" → Import `network_graph_data.csv` (optional)

4. **Save as:** `Collab_Hub_Data.xlsx`

5. **Upload to Power BI:**
   - In Power BI Service, click **"+ New"** → **"File upload"**
   - Upload `Collab_Hub_Data.xlsx`
   - Power BI will automatically create a dataset with all sheets linked

**Why this is better:** Relationships between sheets are easier to set up!

---

### **Step 3: Create a Report**

1. After upload, find your dataset in **"My workspace"**
2. Click on the dataset name (or click **"Create report"**)
3. You'll see a blank canvas - ready to build visualizations!

---

## 💻 **METHOD 2: Power BI Desktop (If You Can Use It)**

### **Step 1: Open Power BI Desktop**

1. Download from: https://powerbi.microsoft.com/desktop/
2. Install and open Power BI Desktop

---

### **Step 2: Import CSV Files**

1. Click **"Get Data"** (Home ribbon)
2. Select **"Text/CSV"**
3. Navigate to your folder
4. Select `Collab_Matches_For_PowerBI.csv`
5. Click **"Load"** (or **"Transform Data"** to preview first)

6. **Repeat for other files:**
   - `Researcher_Profiles_For_PowerBI.csv`
   - `network_graph_data.csv` (optional)

---

### **Step 3: Create Relationships**

1. Click **"Model"** view (left sidebar, 3 circles icon)
2. **Create relationships:**
   - Drag `Faculty_A_Name` from Matches table
   - Drop on `name` in Researchers table
   - Set to **Many-to-One**
   - Enable **Cross-filter direction: Both**

3. **Repeat for:**
   - `Faculty_B_Name` → `name` in Researchers table

---

### **Step 4: Build Visualizations**

1. Click **"Report"** view (left sidebar)
2. Start building your visualizations (see COLLAB_HUB_MVP_GUIDE.md)

---

## 📊 **QUICK START: Excel Method (Easiest for Web)**

### **Step-by-Step:**

1. **Open Excel**
2. **Create 3 sheets:**
   ```
   Sheet 1: "Matches" → Import Collab_Matches_For_PowerBI.csv
   Sheet 2: "Researchers" → Import Researcher_Profiles_For_PowerBI.csv
   Sheet 3: "Network" → Import network_graph_data.csv (optional)
   ```
3. **Save as:** `Collab_Hub_Data.xlsx`
4. **Upload to Power BI Service:**
   - Go to https://app.powerbi.com
   - Click **"+ New"** → **"File upload"**
   - Upload `Collab_Hub_Data.xlsx`
5. **Create report:**
   - Click on the dataset
   - Click **"Create report"**
   - Start building visualizations!

---

## 🎯 **WHAT TO IMPORT (Priority Order)**

### **Must-Have:**
1. ✅ **`Collab_Matches_For_PowerBI.csv`** - Main matching data
2. ✅ **`Researcher_Profiles_For_PowerBI.csv`** - Researcher info

### **Optional:**
3. ⭐ **`network_graph_data.csv`** - For network visualization
4. ⭐ **`best_faculty_match.csv`** - Top matches only

---

## ✅ **VERIFICATION: Check Your Import**

After importing, verify:

1. **Dataset appears in "My workspace"**
2. **Can see all columns** when you click on the dataset
3. **Data looks correct** (names, scores, etc.)
4. **Ready to create report**

---

## 🚨 **TROUBLESHOOTING**

### **Problem: "File upload failed"**
- **Solution:** Check file size (should be < 100MB)
- **Solution:** Try uploading one file at a time
- **Solution:** Check file encoding (should be UTF-8)

### **Problem: "Can't see relationships"**
- **Solution:** Use Excel method - relationships are easier
- **Solution:** In Power BI Desktop, go to Model view to create relationships manually

### **Problem: "Columns missing"**
- **Solution:** Make sure you uploaded the correct CSV file
- **Solution:** Check that CSV has headers in first row

### **Problem: "Data looks wrong"**
- **Solution:** Click **"Refresh"** on the dataset
- **Solution:** Re-upload the file

---

## 📝 **QUICK REFERENCE**

### **Power BI Service (Web):**
1. Go to https://app.powerbi.com
2. Click **"+ New"** → **"File upload"**
3. Upload CSV files (or Excel with multiple sheets)
4. Click dataset → **"Create report"**

### **Power BI Desktop:**
1. Open Power BI Desktop
2. **Get Data** → **Text/CSV**
3. Select CSV files
4. Create relationships in Model view
5. Build visualizations in Report view

---

## 🎯 **RECOMMENDED: Excel Method**

**Why Excel method is best:**
- ✅ One file to manage
- ✅ Automatic sheet relationships
- ✅ Easier to update
- ✅ Works great in Power BI Service

**Steps:**
1. Open Excel
2. Import CSVs as separate sheets
3. Save as `.xlsx`
4. Upload to Power BI
5. Done!

---

**Start with the Excel method - it's the easiest!** 🚀



