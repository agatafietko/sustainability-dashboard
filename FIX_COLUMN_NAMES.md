# Fix "Column 1, Column 2" Issue in Power BI Service

## 🔍 Problem
Power BI imported your data but didn't recognize the first row as headers, so you see "Column 1", "Column 2", etc. instead of actual column names like `article_uuid`, `title`, etc.

---

## ✅ **SOLUTION: Transform Data to Set Headers**

### Step 1: Open Your Dataset
1. In Power BI Service, go to **My Workspace**
2. Find your dataset (click on it)
3. Click **...** (three dots) next to the dataset
4. Select **Settings** or **Edit** or **Transform data**

### Step 2: Transform Data (Power Query Editor)
1. You should see a **"Transform data"** or **"Edit"** button
2. Click it - this opens Power Query Editor
3. You'll see your tables with "Column 1", "Column 2", etc.

### Step 3: Promote First Row to Headers
For **each table** (Publications, SDG_Mappings, Keywords, sdg_lookup):

1. **Click on the table** (e.g., "Publications")
2. Look for **"Use First Row as Headers"** button (top ribbon)
   - Or: **Transform** tab → **Use First Row as Headers**
   - Or: Right-click first row → **Use First Row as Headers**
3. Click it!
4. The column names should change from "Column 1" to `article_uuid`, etc.

### Step 4: Repeat for All Tables
Do this for:
- ✅ Publications
- ✅ SDG_Mappings  
- ✅ Keywords
- ✅ sdg_lookup

### Step 5: Apply & Close
1. Click **Close & Apply** (top left)
2. Wait for data to refresh
3. Go back to Model view
4. **Now you should see proper column names!**

---

## 🔄 **ALTERNATIVE: Re-Import with Headers**

If Transform doesn't work, re-import the dataset:

### Step 1: Delete Old Dataset
1. In Power BI Service, go to **My Workspace**
2. Find your dataset
3. Click **...** → **Delete**

### Step 2: Re-Import Excel File
1. Click **+ New** → **Dataset**
2. Choose **OneDrive**
3. Select `Power_BI_Combined_Data_Fixed.xlsx` (or your Excel file)
4. **IMPORTANT**: When it asks about headers, make sure **"First row as headers"** is **CHECKED**
5. Click **Create**

### Step 3: Verify
1. After import, go to **Data** view
2. Click on **Publications** table
3. You should now see: `article_uuid`, `title`, `name`, etc. (not "Column 1", "Column 2")

---

## 📋 **Quick Checklist**

- [ ] I opened Transform data / Power Query Editor
- [ ] I clicked "Use First Row as Headers" for Publications table
- [ ] I clicked "Use First Row as Headers" for SDG_Mappings table
- [ ] I clicked "Use First Row as Headers" for Keywords table
- [ ] I clicked "Use First Row as Headers" for sdg_lookup table
- [ ] I clicked "Close & Apply"
- [ ] I went to Data view and verified column names are correct
- [ ] I can now see `article_uuid` instead of "Column 1"

---

## 🎯 **What You Should See After Fix**

### In Publications table:
- `article_uuid` (not "Column 1")
- `title` (not "Column 2")
- `name` (not "Column 3")
- `department` (not "Column 4")
- etc.

### In SDG_Mappings table:
- `article_uuid` (not "Column 1")
- `SDG ID` (not "Column 2")

### In Keywords table:
- `article_uuid` (not "Column 1")
- `keyword` (not "Column 2")

### In sdg_lookup table:
- `SDG ID` (not "Column 1")
- `SDG Name` (not "Column 2")
- etc.

---

## 🆘 **Still Seeing "Column 1, Column 2"?**

**Try this:**

1. **In Power Query Editor**, look at the first row of data
2. If the first row contains actual column names (like "article_uuid"), then:
   - Select that row
   - Right-click → **Use First Row as Headers**

3. **If first row is blank or has data**, then:
   - The Excel file might not have headers in row 1
   - Use the new file: `Power_BI_Combined_Data_Fixed.xlsx` (I just created it)
   - Re-import it

---

## ✅ **After Fixing Headers**

Once you see proper column names:
1. Go to **Model** view
2. You should now see `article_uuid` in Publications table
3. You can create relationships:
   - `Publications[article_uuid]` → `SDG_Mappings[article_uuid]`
   - `Publications[article_uuid]` → `Keywords[article_uuid]`
   - `SDG_Mappings[SDG ID]` → `sdg_lookup[SDG ID]`

---

**Follow these steps and your column names should appear correctly!** 🎉

If you still have issues, tell me what you see after clicking "Use First Row as Headers"!





