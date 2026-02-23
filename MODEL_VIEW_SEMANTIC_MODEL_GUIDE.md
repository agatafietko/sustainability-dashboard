# Model View / Semantic Model in Power BI Service Web

## 🎯 Yes, They're the Same Thing!

**Semantic Model** = **Model View** = Where you create relationships between tables

Power BI Service (web) uses different terminology than Desktop, but they're the same concept.

---

## 🔍 How to Access Model View in Power BI Service

### Method 1: From Dataset (Recommended)

1. **Go to Power BI Service**: https://app.powerbi.com
2. **Click on "My Workspace"** (left sidebar)
3. **Find your dataset** (click on it)
4. You'll see options:
   - **"Semantic Model"** tab (this is Model view!)
   - Or: **"..."** (three dots) → **"Manage"** → **"Semantic Model"**

### Method 2: From Report

1. **Open your report** (if you've created one)
2. **Click on the dataset name** (top left)
3. Select **"Manage"** or **"Semantic Model"**

### Method 3: Direct Access

1. In Power BI Service, find your dataset
2. Click **"..."** (three dots) next to dataset
3. Select **"Manage"** or **"Semantic Model"**
4. Click **"Semantic Model"** tab

---

## 📊 What You'll See in Semantic Model View

Once you're in Semantic Model view, you'll see:
- **Table boxes** showing your tables (Publications, Keywords, SDG_Mappings, sdg_lookup)
- **Columns** listed under each table
- **Lines** connecting tables (if relationships exist)
- **Toolbar** at the top with relationship options

---

## 🔗 Creating Relationships in Semantic Model View

### Step 1: Access Semantic Model
Follow Method 1 above to get to Semantic Model view.

### Step 2: View Your Tables
You should see boxes representing your tables:
- Publications
- SDG_Mappings
- Keywords
- sdg_lookup

### Step 3: Create Relationship

**Option A: Drag and Drop (If Available)**
1. Find the column you want to connect (e.g., `article_uuid` in Publications)
2. **Click and drag** from that column
3. **Drop it** on the matching column in another table (e.g., `article_uuid` in SDG_Mappings)
4. A relationship line should appear

**Option B: Manage Relationships Button (Recommended)**
1. Look for **"Manage relationships"** button (top toolbar)
2. Click it
3. Click **"New"** button
4. Fill in:
   - **From Table**: Publications
   - **From Column**: article_uuid
   - **To Table**: SDG_Mappings
   - **To Column**: article_uuid
   - **Cardinality**: Many-to-One (or One-to-Many)
   - **Cross-filter direction**: Both
5. Click **OK**

**Option C: Right-Click Method**
1. **Right-click** on a table
2. Select **"Manage relationships"** or **"New relationship"**
3. Fill in the relationship details
4. Click **OK**

---

## 📋 The 3 Relationships You Need

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

## 🎨 Visual Guide: What Semantic Model View Looks Like

```
┌─────────────────────────────────────────┐
│  Semantic Model / Model View            │
│  [Manage relationships] [New] [Delete]   │
├─────────────────────────────────────────┤
│                                         │
│  ┌─────────────────┐                   │
│  │  Publications   │                   │
│  │  - article_uuid │──┐                │
│  │  - title        │  │                │
│  │  - name         │  │                │
│  └─────────────────┘  │                │
│                        │                │
│  ┌─────────────────┐   │                │
│  │ SDG_Mappings    │◄──┘ (relationship)│
│  │ - article_uuid  │──┐                │
│  │ - SDG ID        │  │                │
│  └─────────────────┘  │                │
│                        │                │
│  ┌─────────────────┐   │                │
│  │   sdg_lookup    │◄──┘                │
│  │ - SDG ID        │                    │
│  │ - SDG Name      │                    │
│  └─────────────────┘                    │
│                                         │
│  ┌─────────────────┐                    │
│  │    Keywords     │◄───────────────────┐
│  │ - article_uuid │                    │
│  │ - keyword      │                    │
│  └─────────────────┘                    │
│                                         │
└─────────────────────────────────────────┘
```

---

## 🐛 Troubleshooting

### Issue: Can't Find "Semantic Model" Tab

**Solution:**
- Look for **"Manage"** button instead
- Or click **"..."** → **"Manage"**
- Then look for **"Semantic Model"** section

### Issue: Can't See Tables

**Solution:**
1. Make sure your dataset is loaded
2. Check if you're in the right view
3. Try refreshing the page
4. Go back to dataset and try again

### Issue: Can't Create Relationships

**Possible reasons:**
1. **Power BI Service web limitations**: Some relationship features may be limited
2. **Column types don't match**: Ensure both columns are the same data type
3. **Tables not loaded**: Make sure all tables are imported

**Solutions:**
- Use **"Manage relationships"** button instead of drag-drop
- Verify column names match exactly
- Check that columns are in the correct data format

---

## ✅ Step-by-Step: Creating First Relationship

### Example: Publications → SDG_Mappings

1. **Access Semantic Model**:
   - Go to dataset → Click **"Semantic Model"** tab
   - Or: Click **"Manage"** → **"Semantic Model"**

2. **Find Tables**:
   - You should see "Publications" and "SDG_Mappings" boxes

3. **Create Relationship**:
   - Click **"Manage relationships"** button
   - Click **"New"**
   - Fill in:
     ```
     From Table: Publications
     From Column: article_uuid
     To Table: SDG_Mappings
     To Column: article_uuid
     Cardinality: Many-to-One
     Cross-filter direction: Both
     ```
   - Click **OK**

4. **Verify**:
   - You should see a line connecting the two tables
   - The relationship appears in the relationships list

5. **Repeat** for other relationships

---

## 🔄 Alternative: Create Relationships in Power Query

If Semantic Model view doesn't work, you can also create relationships in **Power Query Editor**:

1. **Transform Data** → Opens Power Query Editor
2. **Manage Relationships** button (top ribbon)
3. Create relationships same way

---

## 💡 Key Differences: Desktop vs Service

| Feature | Power BI Desktop | Power BI Service (Web) |
|---------|------------------|------------------------|
| **Name** | "Model" view | "Semantic Model" |
| **Access** | Model icon in sidebar | Manage → Semantic Model |
| **Relationships** | Full support | Limited support |
| **Drag-drop** | Yes | Sometimes |

---

## 📋 Quick Checklist

- [ ] I found my dataset in Power BI Service
- [ ] I clicked "Semantic Model" or "Manage" → "Semantic Model"
- [ ] I can see all my tables (Publications, Keywords, SDG_Mappings, sdg_lookup)
- [ ] I can see column names in each table
- [ ] I found "Manage relationships" button
- [ ] I created Relationship 1: Publications → SDG_Mappings
- [ ] I created Relationship 2: Publications → Keywords
- [ ] I created Relationship 3: SDG_Mappings → sdg_lookup
- [ ] I can see relationship lines connecting tables

---

## 🎯 Summary

**Semantic Model = Model View** - They're the same thing!

**To access:**
1. Dataset → **"Semantic Model"** tab
2. Or: **"Manage"** → **"Semantic Model"**

**To create relationships:**
1. Click **"Manage relationships"**
2. Click **"New"**
3. Fill in table and column names
4. Set cardinality and cross-filter
5. Click **OK**

**After creating relationships, you can:**
- Use columns from related tables in visuals
- Create measures that reference multiple tables
- Build dashboards with cross-table filtering

---

**Follow these steps and you'll be able to create relationships in Power BI Service!** 🎉

If you can't find Semantic Model view, tell me what you see when you click on your dataset, and I'll help you navigate!





