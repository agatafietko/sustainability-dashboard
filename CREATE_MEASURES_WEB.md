# How to Create Measures in Power BI Service (Web)

## 🎯 **Step-by-Step Guide**

### Step 1: Access Your Dataset

1. Go to **Power BI Service**: https://app.powerbi.com
2. Sign in
3. Click **"My Workspace"** (left sidebar)
4. Find your dataset (e.g., "Case competition test model")
5. **Click on the dataset name**

---

### Step 2: Open Data View

1. Look for **"Data"** icon/tab (usually in left sidebar or top tabs)
2. Click it to open Data view
3. You'll see your tables listed

---

### Step 3: Select Table for Measure

1. In the **Data** pane (usually on the right), find **"Publications"** table
2. **Click on "Publications"** to select it
   - This is where your measure will be stored
   - You can store measures in any table, but Publications is good for most

---

### Step 4: Create New Measure

**Option A: Using Ribbon (Recommended)**
1. Look at the **top ribbon** (Home tab)
2. Find **"New measure"** button
3. Click it
4. A formula bar appears at the top

**Option B: Right-Click Method**
1. **Right-click** on "Publications" table in the Data pane
2. Select **"New measure"** from the menu
3. Formula bar appears

**Option C: Using Shortcut**
1. Select Publications table
2. Press **Alt + M** (Windows) or check if there's a shortcut
3. Formula bar appears

---

### Step 5: Enter Measure Formula

1. In the **formula bar** at the top, you'll see:
   ```
   Measure = 
   ```
2. **Delete the default text** and paste your measure code

**Example - First Measure:**
```
Total Publications = COUNTROWS(Publications)
```

3. Click **✓ (checkmark)** or press **Enter** to save

---

### Step 6: Verify Measure Created

1. The measure should appear in the **Data pane** under "Publications" table
2. You'll see it listed with a **calculator icon** (📊)
3. It should show: `Total Publications` with the formula

---

### Step 7: Create More Measures

Repeat Steps 4-6 for each measure:

**Measure 2: Sustainable Publications**
```
Sustainable Publications = 
CALCULATE(
    COUNTROWS(Publications),
    Publications[is_sustain] = TRUE()
)
```

**Measure 3: Sustainable %**
```
Sustainable % = 
DIVIDE(
    [Sustainable Publications],
    [Total Publications],
    0
)
```

**Measure 4: Publications by Year**
```
Publications by Year = 
CALCULATE(
    [Total Publications],
    ALLEXCEPT(Publications, Publications[publication_year])
)
```

**Measure 5: Sustainable by Department**
```
Sustainable by Department = 
CALCULATE(
    [Sustainable Publications],
    ALLEXCEPT(Publications, Publications[department])
)
```

---

## 📋 **Visual Guide: Where to Find Everything**

### Finding "New Measure" Button:

**In Power BI Service Web:**
1. **Top ribbon** → **"Home"** tab
2. Look for **"New measure"** button
   - Usually in the **Calculations** section
   - Or under **"Data"** section
   - May be labeled as **"Measure"** or **"New measure"**

**If you can't find it:**
- Look for **"..."** (three dots) menu
- May be under **"More options"** or **"Data tools"**
- Or try **"Transform data"** → might have measure options there

---

## 🔧 **Alternative: Using Transform Data / Power Query**

If "New measure" isn't visible in the main view:

1. Click **"Transform data"** or **"Edit"** (opens Power Query)
2. Look for **"New measure"** in Power Query editor
3. Create measure there
4. Click **"Close & Apply"**

---

## 📝 **Copy-Paste Ready Measures**

Copy these from `DAX_Measures.txt`:

### Essential Measures (Start Here):

**1. Total Publications**
```DAX
Total Publications = COUNTROWS(Publications)
```

**2. Sustainable Publications**
```DAX
Sustainable Publications = 
CALCULATE(
    COUNTROWS(Publications),
    Publications[is_sustain] = TRUE()
)
```

**3. Sustainable %**
```DAX
Sustainable % = 
DIVIDE(
    [Sustainable Publications],
    [Total Publications],
    0
)
```

**4. Publications by Year**
```DAX
Publications by Year = 
CALCULATE(
    [Total Publications],
    ALLEXCEPT(Publications, Publications[publication_year])
)
```

**5. Sustainable by Department**
```DAX
Sustainable by Department = 
CALCULATE(
    [Sustainable Publications],
    ALLEXCEPT(Publications, Publications[department])
)
```

---

## ✅ **Step-by-Step Checklist**

- [ ] Opened Power BI Service
- [ ] Clicked on my dataset
- [ ] Found "Data" view/tab
- [ ] Selected "Publications" table
- [ ] Found "New measure" button
- [ ] Created "Total Publications" measure
- [ ] Verified it appears in Data pane
- [ ] Created "Sustainable Publications" measure
- [ ] Created "Sustainable %" measure
- [ ] Created "Publications by Year" measure
- [ ] Created "Sustainable by Department" measure

---

## 🎨 **Using Measures in Visuals**

After creating measures:

1. **Create a visual** (card, chart, etc.)
2. **Drag the measure** to **"Values"** field
   - NOT to "Columns" or "Rows"
   - Measures go in "Values" section
3. Visual will show the aggregated value

**Example:**
- Create **Card** visual
- Drag **"Total Publications"** measure to **Values**
- Card shows: 1,899 (or your total count)

---

## 🐛 **Troubleshooting**

### Issue: Can't Find "New Measure" Button

**Solutions:**
1. Make sure you're in **Data view** (not Report view)
2. Try **"Transform data"** → might have measure options
3. Check if you're in the right workspace (My Workspace)
4. Look for **"..."** menu → might be hidden there

### Issue: Formula Bar Doesn't Appear

**Solutions:**
1. Make sure a table is selected
2. Try clicking directly on the table name in Data pane
3. Try right-clicking table → "New measure"

### Issue: Measure Shows Error

**Common Errors:**
- **Table not found**: Check table name matches exactly (case-sensitive)
- **Column not found**: Check column name matches exactly
- **Syntax error**: Check for typos, missing commas, brackets

**Fix:**
- Edit measure (click on it in Data pane)
- Check formula matches examples exactly
- Verify table and column names are correct

---

## 💡 **Pro Tips**

1. **Start Simple**: Create "Total Publications" first to test
2. **Test Each**: Add measure to a card visual to verify it works
3. **Use Existing Measures**: Later measures can reference earlier ones (like `[Sustainable Publications]`)
4. **Format Measures**: Right-click measure → Format → Set as percentage for %

---

## 🎯 **Quick Reference**

**Location of "New Measure":**
- Top ribbon → Home tab → "New measure"
- Or: Right-click table → "New measure"
- Or: Transform data → Power Query editor

**Where Measures Are Stored:**
- Under the table you selected (usually Publications)
- Shows with calculator icon (📊)
- Listed in Data pane

**How to Use:**
- Drag measure to "Values" in visual
- NOT to "Columns" or "Rows"

---

**Follow these steps and you'll have all your measures created!** 🎉

If you can't find "New measure", tell me what you see in the ribbon/tabs and I'll help you locate it!





