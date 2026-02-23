# Fix Keywords Table - Missing Column Names

## 🔍 Problem
Other tables have column names (like `article_uuid`, `title`, etc.), but the **Keywords** table still shows "Column 1", "Column 2" instead of `article_uuid`, `keyword`.

---

## ✅ **SOLUTION: Fix Keywords Table in Power BI**

### Step 1: Open Transform Data
1. In Power BI Service, go to your dataset
2. Click **...** (three dots) → **Transform data** or **Edit**
3. This opens Power Query Editor

### Step 2: Fix Keywords Table
1. **Click on the "Keywords" table** (left sidebar)
2. Look at the columns - you should see:
   - "Column 1" (should be `article_uuid`)
   - "Column 2" (should be `keyword`)

3. **Check Row 1:**
   - If Row 1 is blank → Remove it (right-click → Remove)
   - If Row 1 has "article_uuid", "keyword" → Promote to headers

4. **Promote First Row to Headers:**
   - Click on the row that has "article_uuid" and "keyword"
   - Click **"Use First Row as Headers"** (top ribbon)
     - Or: **Transform** tab → **Use First Row as Headers**
     - Or: Right-click the row → **Use First Row as Headers**

### Step 3: Verify
After promoting headers, you should see:
- ✅ `article_uuid` (not "Column 1")
- ✅ `keyword` (not "Column 2")

### Step 4: Apply
1. Click **Close & Apply** (top left)
2. Wait for refresh
3. Go to **Data** view
4. Click on Keywords table
5. Verify you see `article_uuid` and `keyword` as column names

---

## 🔄 **ALTERNATIVE: Re-Import Keywords Sheet**

If the above doesn't work, you can recreate just the Keywords sheet:

### Option 1: Fix in Power Query (Recommended)

1. In Power Query Editor, click on **Keywords** table
2. If you see "Column 1" and "Column 2":
   - **Check if Row 1 has the headers**: Look for "article_uuid" and "keyword"
   - If Row 1 is blank, remove it first
   - Then click "Use First Row as Headers"

3. If that doesn't work:
   - **Remove Column Headers** (if they exist as data)
   - **Promote First Row** again

### Option 2: Delete and Re-Add Keywords Table

1. In Power Query Editor, **right-click Keywords table** → **Delete**
2. Click **New Source** → **Excel workbook**
3. Navigate to your OneDrive file
4. Select the **Keywords** sheet
5. **Make sure "First row as headers" is CHECKED**
6. Click **Load**
7. Click **Close & Apply**

---

## 📋 **What Keywords Table Should Look Like**

**After fixing:**
- Column 1: `article_uuid` ✅
- Column 2: `keyword` ✅

**Data preview:**
```
article_uuid                          | keyword
38792cbd-5cff-4cc8-afdf-f5148896e760 | Cash Flow
38792cbd-5cff-4cc8-afdf-f5148896e760 | Large Banks
...
```

---

## 🎯 **Quick Fix Steps**

1. **Open Transform data** in Power BI
2. **Click Keywords table**
3. **If Row 1 is blank** → Remove it
4. **Click "Use First Row as Headers"**
5. **Close & Apply**
6. **Verify** in Data view

---

## 🆘 **Still Not Working?**

**If you still see "Column 1", "Column 2":**

1. **Check the actual data:**
   - In Power Query, look at Row 1 and Row 2
   - What values do you see?

2. **Try manual column rename:**
   - In Power Query, right-click "Column 1"
   - Select **Rename**
   - Type: `article_uuid`
   - Repeat for "Column 2" → rename to `keyword`

3. **Or delete and re-import:**
   - Delete Keywords table
   - Re-import from Excel file
   - Make sure headers are checked

---

**Follow these steps and your Keywords table should have proper column names!** 🎉





