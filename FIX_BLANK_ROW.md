# Fix Blank First Row Issue in Power BI Service

## 🔍 Problem
Your Excel file has a blank first row, so:
- Row 1 = blank (Power BI sees as "Column 1", "Column 2", etc.)
- Row 2 = actual headers (like "article_uuid", "title", etc.)
- Row 3+ = data

You need to **remove the blank first row** and **promote row 2 to headers**.

---

## ✅ **SOLUTION: Remove Blank Row in Power Query**

### Step 1: Open Transform Data
1. In Power BI Service, go to your dataset
2. Click **...** (three dots) → **Transform data** or **Edit**
3. This opens Power Query Editor

### Step 2: Remove Blank First Row
For **each table** (Publications, SDG_Mappings, Keywords, sdg_lookup):

1. **Click on the table** (e.g., "Publications")
2. You'll see rows - Row 1 is blank, Row 2 has headers
3. **Right-click on Row 1** (the blank row)
4. Select **"Remove"** or **"Delete Row"**
   - OR: Select Row 1, then **Home** tab → **Remove Rows** → **Remove Top Row**

### Step 3: Promote First Row to Headers
After removing the blank row, the headers row is now in position 1:

1. Click on what is now **Row 1** (which has "article_uuid", "title", etc.)
2. Click **"Use First Row as Headers"** (top ribbon)
   - Or: **Transform** tab → **Use First Row as Headers**
   - Or: Right-click the row → **Use First Row as Headers**

### Step 4: Repeat for All Tables
Do this for:
- ✅ Publications
- ✅ SDG_Mappings  
- ✅ Keywords
- ✅ sdg_lookup

### Step 5: Apply Changes
1. Click **Close & Apply** (top left)
2. Wait for data to refresh
3. Go to **Data** view
4. **Now you should see proper column names!**

---

## 📋 **Step-by-Step Visual Guide**

### For Publications Table:

**Before:**
```
Row 1: [blank] [blank] [blank] ... → Shows as "Column 1", "Column 2"
Row 2: article_uuid | title | name | ... → Shows as data
Row 3: [actual data]
```

**Step 1: Remove Row 1**
- Right-click Row 1 → Remove

**After removing:**
```
Row 1: article_uuid | title | name | ... → Still shows as data
Row 2: [actual data]
```

**Step 2: Promote to Headers**
- Click "Use First Row as Headers"
- Row 1 becomes column headers

**Final:**
```
Headers: article_uuid | title | name | department | ...
Row 1: [actual data]
```

---

## 🔄 **ALTERNATIVE: Use New Fixed Excel File**

I've created a fixed Excel file: **`Power_BI_Combined_Data_Fixed.xlsx`**

This file has:
- ✅ Headers already in row 1 (no blank row)
- ✅ All 4 sheets fixed
- ✅ Ready to import

### Steps:
1. **Delete old dataset** in Power BI Service
2. **Upload new file** to OneDrive:
   - `Power_BI_Combined_Data_Fixed.xlsx`
3. **Create new dataset** from this file
4. Headers should be recognized automatically!

---

## ✅ **What You Should See After Fix**

### In Publications table:
- ✅ `article_uuid` (not "Column 1")
- ✅ `title` (not "Column 2")  
- ✅ `name` (not "Column 3")
- ✅ `department` (not "Column 4")
- ✅ etc.

### In SDG_Mappings table:
- ✅ `article_uuid` (not "Column 1")
- ✅ `SDG ID` (not "Column 2")

### In Keywords table:
- ✅ `article_uuid` (not "Column 1")
- ✅ `keyword` (not "Column 2")

### In sdg_lookup table:
- ✅ `SDG ID` (not "Column 1")
- ✅ `SDG Name` (not "Column 2")
- ✅ etc.

---

## 🎯 **Quick Checklist**

**Option 1: Fix in Power Query**
- [ ] Opened Transform data / Power Query Editor
- [ ] Removed blank first row from Publications table
- [ ] Clicked "Use First Row as Headers" for Publications
- [ ] Repeated for SDG_Mappings, Keywords, sdg_lookup
- [ ] Clicked "Close & Apply"
- [ ] Verified column names in Data view

**Option 2: Use New Excel File** (Easier!)
- [ ] Deleted old dataset in Power BI
- [ ] Uploaded `Power_BI_Combined_Data_Fixed.xlsx` to OneDrive
- [ ] Created new dataset from fixed file
- [ ] Verified column names are correct

---

## 🆘 **Still Having Issues?**

**If you can't find "Remove Row" option:**
1. Select the blank row (Row 1)
2. Go to **Home** tab
3. Look for **"Remove Rows"** dropdown
4. Select **"Remove Top Row"** or **"Remove Blank Rows"**

**If you don't see "Use First Row as Headers":**
1. Select the row with headers (now Row 1 after removing blank)
2. Right-click → Look for header-related options
3. Or check **Transform** tab → **Table** section

---

## 💡 **Pro Tip**

**Using the new fixed Excel file is easier** than fixing in Power Query:
1. Less steps
2. No manual row removal
3. Headers are already correct
4. Just re-import and you're done!

---

**After fixing, you'll be able to create relationships using:**
- `Publications[article_uuid]` → `SDG_Mappings[article_uuid]`
- `Publications[article_uuid]` → `Keywords[article_uuid]`
- `SDG_Mappings[SDG ID]` → `sdg_lookup[SDG ID]`

**Follow these steps and your column names will be correct!** 🎉





