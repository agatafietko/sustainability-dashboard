# How to Create Relationships in Power BI Service (Web)

## 🔍 First: Verify You Can See Your Tables

### Step 1: Check What Tables You Have

1. In Power BI Service, go to **Model** view:
   - Click the **Model** icon in the left sidebar (looks like 3 connected circles)
   - Or click **...** (three dots) → **Model view**

2. You should see your tables listed:
   - **Publications** (or your main table name)
   - **SDG_Mappings**
   - **Keywords**
   - **sdg_lookup**

### Step 2: View Table Columns

**To see columns in a table:**
1. Click on a table box (e.g., "Publications")
2. The columns should appear below the table name
3. Look for: `article_uuid` (it should be there!)

**If you don't see columns:**
- Try clicking **Expand** or **+** on the table
- Or double-click the table name
- Or hover over the table

---

## 🔗 Creating Relationships in Power BI Service Web

### Method 1: Drag and Drop (If Available)

1. **Make sure you're in Model view**
2. **Find the two tables** you want to connect:
   - Example: `Publications` and `SDG_Mappings`
3. **Look for the `article_uuid` column** in both tables
4. **Click and drag** from:
   - `Publications[article_uuid]` 
   - **TO**
   - `SDG_Mappings[article_uuid]`
5. A line should appear connecting them

**If drag doesn't work**, try Method 2 below.

---

### Method 2: Right-Click / Manage Relationships (Recommended)

1. **In Model view**, right-click on a table (e.g., "Publications")
2. Select **Manage relationships** or **Edit relationships**
3. A dialog box opens showing relationships

4. **Click "New"** to create a relationship:
   - **Table 1**: Select `Publications`
   - **Column 1**: Select `article_uuid`
   - **Table 2**: Select `SDG_Mappings`
   - **Column 2**: Select `article_uuid`
   - **Cardinality**: Select **Many-to-One** (or Many-to-Many if needed)
   - **Cross-filter direction**: Select **Both**
   - Click **OK**

5. **Repeat for other relationships**

---

### Method 3: Using the Relationship Dialog

1. In Model view, look for a **"Manage relationships"** button (top ribbon)
2. Click it
3. Click **"New"** in the dialog
4. Fill in:
   - **From Table**: Publications
   - **From Column**: article_uuid
   - **To Table**: SDG_Mappings
   - **To Column**: article_uuid
5. Click **OK**

---

## 📋 The 3 Relationships You Need to Create

### Relationship 1: Publications → SDG_Mappings
- **From**: `Publications[article_uuid]`
- **To**: `SDG_Mappings[article_uuid]`
- **Type**: Many-to-One
- **Cross-filter**: Both

### Relationship 2: Publications → Keywords
- **From**: `Publications[article_uuid]`
- **To**: `Keywords[article_uuid]`
- **Type**: Many-to-One
- **Cross-filter**: Both

### Relationship 3: SDG_Mappings → sdg_lookup
- **From**: `SDG_Mappings[SDG ID]`
- **To**: `sdg_lookup[SDG ID]`
- **Type**: Many-to-One
- **Cross-filter**: Both

---

## 🐛 Troubleshooting: "I Don't See article_uuid"

### Issue 1: Column Names Are Different

**Check the actual column names:**
1. Go to **Data** view (left sidebar)
2. Click on each table
3. Look at the column headers
4. Note the exact names (case-sensitive!)

**Common variations:**
- `Article UUID` (with space)
- `article_UUID` (different casing)
- `ArticleUuid` (no underscore)

**Solution**: Use the exact column names you see!

---

### Issue 2: Tables Not Loaded Correctly

**Verify your Excel file loaded:**
1. Go to **Data** view
2. Check if you see all 4 tables:
   - Publications
   - SDG_Mappings
   - Keywords
   - sdg_lookup

**If tables are missing:**
- Go back to dataset creation
- Make sure you selected the Excel file
- Check that all sheets were imported

---

### Issue 3: Power BI Service Limitations

**Power BI Service web has limitations:**
- Some relationship features may not be available
- You might need to use calculated columns instead
- Or work with single dataset at a time

**Workaround**: If relationships don't work:
1. Use **Data** view to manually filter
2. Use calculated columns to combine data
3. Or create measures that reference multiple tables

---

## ✅ Step-by-Step: Creating Each Relationship

### Relationship 1: Publications ↔ SDG_Mappings

1. **Go to Model view**
2. **Right-click** on `Publications` table
3. **Select**: "Manage relationships" or "New relationship"
4. **Fill in**:
   ```
   Table 1: Publications
   Column: article_uuid
   Table 2: SDG_Mappings
   Column: article_uuid
   Cardinality: Many-to-One
   Cross-filter: Both
   ```
5. **Click OK**

### Relationship 2: Publications ↔ Keywords

1. **Right-click** on `Publications` table again
2. **Select**: "New relationship"
3. **Fill in**:
   ```
   Table 1: Publications
   Column: article_uuid
   Table 2: Keywords
   Column: article_uuid
   Cardinality: Many-to-One
   Cross-filter: Both
   ```
4. **Click OK**

### Relationship 3: SDG_Mappings ↔ sdg_lookup

1. **Right-click** on `SDG_Mappings` table
2. **Select**: "New relationship"
3. **Fill in**:
   ```
   Table 1: SDG_Mappings
   Column: SDG ID
   Table 2: sdg_lookup
   Column: SDG ID
   Cardinality: Many-to-One
   Cross-filter: Both
   ```
4. **Click OK**

---

## 🔍 How to Verify Relationships Worked

1. **Go back to Model view**
2. **You should see lines** connecting the tables:
   - Line from Publications to SDG_Mappings
   - Line from Publications to Keywords
   - Line from SDG_Mappings to sdg_lookup

3. **Test in a visual**:
   - Create a simple table
   - Add: `Publications[title]` and `sdg_lookup[SDG Name]`
   - If relationship works, you should see SDG names for publications!

---

## 📸 What Model View Should Look Like

```
┌─────────────────┐
│  Publications   │
│  - article_uuid │──┐
│  - title        │  │
│  - department   │  │
└─────────────────┘  │
                      │
┌─────────────────┐   │
│ SDG_Mappings    │◄──┘
│ - article_uuid  │──┐
│ - SDG ID        │  │
└─────────────────┘  │
                      │
┌─────────────────┐   │
│   sdg_lookup    │◄──┘
│ - SDG ID        │
│ - SDG Name      │
└─────────────────┘

┌─────────────────┐
│    Keywords     │
│ - article_uuid  │◄──┐
│ - keyword       │   │
└─────────────────┘   │
                      │
                      │ (from Publications)
```

---

## 🆘 Still Can't See Columns?

**Try this diagnostic:**

1. **Go to Data view** (not Model view)
2. **Click on "Publications" table**
3. **List all column names you see** - write them down
4. **Check each table** and note column names

**Then tell me:**
- What column names do you see in Publications?
- What column names do you see in SDG_Mappings?
- What column names do you see in Keywords?
- What column names do you see in sdg_lookup?

I can help you create relationships using the actual column names!

---

## 💡 Alternative: Use Auto-Detect

Some Power BI versions have **Auto-detect relationships**:

1. In Model view, look for **"Auto-detect"** or **"Auto-detect relationships"** button
2. Click it
3. Power BI will try to find relationships automatically
4. Review and accept the ones it finds

---

## 🎯 Quick Checklist

- [ ] I'm in Model view
- [ ] I can see all 4 tables (Publications, SDG_Mappings, Keywords, sdg_lookup)
- [ ] I can see columns when I click on tables
- [ ] I found the column I need (`article_uuid` or similar)
- [ ] I created relationship using drag-drop OR right-click method
- [ ] I can see lines connecting tables
- [ ] I tested with a visual and it works

---

**Need help?** Tell me:
1. What tables do you see?
2. What columns do you see in each table?
3. What happens when you try to create a relationship?

I'll help you troubleshoot! 🎉





