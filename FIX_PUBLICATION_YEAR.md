# Fix Publication Year Showing as "Sum"

## 🔍 Problem
When you see `publication_year` showing as "Sum" in Power BI, it means Power BI is treating it as a numeric value to aggregate. This is wrong because:
- Years should be used as categories/grouping, not summed
- You want to see individual years, not a sum of years

---

## ✅ **SOLUTION: Change Data Type and Aggregation**

### Method 1: Fix in Data View (Quick Fix)

1. **Go to Data view** (left sidebar, table icon)
2. **Click on the "Publications" table**
3. **Find the `publication_year` column**
4. **Click on the column header** (publication_year)
5. **Look at the top ribbon** - you'll see:
   - **Data type** (might say "Whole Number" or "Decimal Number")
   - **Summarization** (might say "Sum")

6. **Change Summarization**:
   - Click the dropdown next to "Summarization" or "Default summarization"
   - Select **"Don't summarize"** or **"Count"**
   - This prevents Power BI from summing years

7. **Verify Data Type**:
   - Should be **"Whole Number"** (not Decimal)
   - If it's wrong, click **Data type** dropdown → Select **"Whole Number"**

### Method 2: Fix in Transform Data (Power Query)

1. **Open Transform Data**:
   - Click dataset → **"..."** → **"Transform data"**

2. **Select Publications table** (left sidebar)

3. **Select publication_year column**

4. **Change Data Type**:
   - Click **"Data type"** dropdown (top ribbon)
   - Select **"Whole Number"**

5. **Close & Apply**

---

## 🎯 **What You Should See After Fix**

**Before (Wrong):**
```
publication_year (Sum)
- Shows: 4,038,000 (sum of all years - meaningless!)
```

**After (Correct):**
```
publication_year
- 2010
- 2011
- 2012
- etc.
```

OR

```
publication_year (Count)
- Shows: 1899 (number of publications)
```

---

## 📊 **Setting the Right Aggregation**

For `publication_year`, you typically want:

**Option 1: Don't Summarize** (Best for filtering/slicing)
- Shows individual years
- Use for slicers, filters, grouping

**Option 2: Count** (Good for counting publications per year)
- Shows how many publications in each year
- Use for charts showing publication count over time

**Option 3: First** or **Last** (Rarely used for years)
- Shows first/last year in the data

**Never use:**
- ❌ Sum (adds years together - meaningless!)
- ❌ Average (can be useful but not typical for years)
- ❌ Min/Max (can be useful but not typical)

---

## 🔧 **Step-by-Step: Fix in Data View**

1. **Go to Data view** (left sidebar)
2. **Click "Publications" table**
3. **Click on `publication_year` column header**
4. **In the ribbon at top**, look for:
   - **"Summarization"** dropdown
   - Or **"Default summarization"** dropdown
5. **Change from "Sum" to "Don't summarize"**
6. **Verify**:
   - The column should now show individual years
   - When you drag it to a visual, it shows years, not a sum

---

## 📋 **Other Columns to Check**

While you're at it, check these columns:

### ✅ Should be "Don't summarize":
- `publication_year` - Year (not a sum)
- `article_uuid` - ID (not a sum)
- `name` - Name (text)
- `department` - Category (text)
- `title` - Text

### ✅ Can be "Sum" or "Count":
- `is_sustain` - Boolean (can count how many are sustainable)
- `is_recent` - Boolean (can count how many are recent)

### ✅ Should be "Count" or "Sum":
- Publication counts (if you create measures)

---

## 🎨 **How to Use publication_year Correctly**

After fixing, you can use `publication_year` for:

1. **Slicers**:
   - Drag `publication_year` to slicer
   - Shows years 2010-2020
   - Users can select year ranges

2. **X-axis in Charts**:
   - Line chart: `publication_year` on X-axis
   - Shows trend over time

3. **Grouping**:
   - Group publications by year
   - Count publications per year

---

## ✅ **Quick Checklist**

- [ ] Went to Data view
- [ ] Clicked on Publications table
- [ ] Found `publication_year` column
- [ ] Changed summarization from "Sum" to "Don't summarize"
- [ ] Verified data type is "Whole Number"
- [ ] Tested by dragging `publication_year` to a visual
- [ ] Now shows individual years (2010, 2011, etc.) instead of a sum

---

## 🆘 **If You Still See "Sum"**

**Check these:**
1. **Visual level**: Some visuals might override the default
   - In the visual, click the field → Change aggregation
   - Or remove and re-add the field

2. **Measure conflict**: If you created a measure, it might be using Sum
   - Check your measures

3. **Data type issue**: Column might still be treated as numeric
   - Go to Transform Data → Change data type to Whole Number

---

## 💡 **Pro Tip**

After fixing, create a **measure** for counting publications:
```DAX
Publications by Year = COUNTROWS(Publications)
```

Then use this in charts instead of summing `publication_year`.

---

**After fixing, `publication_year` should show individual years (2010, 2011, etc.) instead of a sum!** 🎉

This is a common Power BI issue - numeric columns are automatically set to sum, but years should be treated as categories.





