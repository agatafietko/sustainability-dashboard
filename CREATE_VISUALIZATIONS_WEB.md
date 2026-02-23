# How to Create Visualizations in Power BI Service (Web)

## 🎯 **Step 1: Create a Report (Not Just Dataset)**

In Power BI Service, you need to create a **Report** to build visualizations. The dataset alone isn't enough.

### Option A: Create New Report from Dataset

1. **Click on your dataset** ("Case competition test model")
2. Look for **"Create report"** button (usually top right or near dataset name)
   - Or click **"..."** (three dots) → **"Create report"**
3. Click it
4. This opens a **Report canvas** where you can build visuals

### Option B: Use Create Icon

1. Look at the **left sidebar**
2. Find the **"Create"** icon (plus sign in circle)
3. Click it
4. Select **"Report"** or **"New report"**
5. Choose your dataset when prompted
6. Report canvas opens

---

## 📊 **Step 2: Understanding the Report Canvas**

Once you're in Report view, you'll see:

- **Canvas** (center) - where you place visuals
- **Visualizations pane** (right) - visual types (bar chart, line chart, etc.)
- **Fields pane** (right, under Visualizations) - your tables, columns, measures
- **Format pane** (right, when visual selected) - formatting options

---

## 🎨 **Step 3: Create Your First Visual**

### Example: Create a KPI Card

1. **Click on blank canvas** (or click "Add new page" if needed)
2. In **Visualizations pane**, click **"Card"** icon (looks like a number)
3. A blank card appears on canvas
4. In **Fields pane**, find your **"Total Publications"** measure
5. **Drag it** to the **"Fields"** section of the card (or just click the measure)
6. Card shows your total count!

### Example: Create a Line Chart

1. Click blank area on canvas
2. In **Visualizations pane**, click **"Line chart"** icon
3. In **Fields pane**:
   - Drag **`publication_year`** (from Publications) to **X-axis**
   - Drag **"Publications by Year"** measure to **Y-axis**
4. Chart shows trend over time!

### Example: Create a Bar Chart

1. Click blank area on canvas
2. In **Visualizations pane**, click **"Bar chart"** icon (horizontal bars)
3. In **Fields pane**:
   - Drag **`department`** (from Publications) to **Y-axis**
   - Drag **"Sustainable by Department"** measure to **X-axis**
4. Chart shows departments ranked by sustainable publications!

---

## 📋 **Step-by-Step: Build Your Dashboard**

### Page 1: Overview Dashboard

#### 1. Create KPI Cards (Top Row)

**Card 1: Total Publications**
1. Click **Card** visual
2. Drag **"Total Publications"** measure to card
3. Format: Add title, adjust size

**Card 2: Sustainable Publications**
1. Click **Card** visual (add new)
2. Drag **"Sustainable Publications"** measure to card

**Card 3: Sustainable %**
1. Click **Card** visual (add new)
2. Drag **"Sustainable %"** measure to card
3. Format: Right-click → Format → Show as percentage

**Card 4: Recent Publications**
1. Click **Card** visual (add new)
2. Drag **"Recent Publications"** measure to card

#### 2. Add Slicers (Left Sidebar)

**Slicer 1: Department**
1. Click **Slicer** visual
2. Drag **`department`** (from Publications) to slicer
3. Format: Change to dropdown or list

**Slicer 2: Year**
1. Click **Slicer** visual
2. Drag **`publication_year`** to slicer
3. Format: Change to "Between" (for range selection)

**Slicer 3: SDG**
1. Click **Slicer** visual
2. Drag **`SDG Name`** (from sdg_lookup) to slicer

#### 3. Add Trend Line Chart

1. Click **Line chart** visual
2. X-axis: Drag **`publication_year`**
3. Y-axis: Drag **"Publications by Year"** measure
4. Y-axis (2nd): Drag **"Sustainable Publications"** measure (add to same Y-axis)
5. Format: Add title "Publications Over Time"

#### 4. Add Department Bar Chart

1. Click **Bar chart** (horizontal) visual
2. Y-axis: Drag **`department`**
3. X-axis: Drag **"Sustainable by Department"** measure
4. Sort: Descending
5. Format: Add title "Top Departments by Sustainable Research"

#### 5. Add SDG Coverage Chart

1. Click **Bar chart** (vertical) visual
2. X-axis: Drag **`SDG Name`** (from sdg_lookup)
3. Y-axis: Drag **"Total Publications"** measure (or create "Publications by SDG" measure)
4. Sort: Descending
5. Format: Add title "Research Coverage by SDG"

---

## 🎯 **Quick Reference: Visual Types**

| Visual Type | Use For | Fields |
|-------------|---------|--------|
| **Card** | Single number | 1 measure |
| **Line Chart** | Trends over time | X-axis: year, Y-axis: measure |
| **Bar Chart** | Comparisons | X/Y-axis: category + measure |
| **Table** | Detailed data | Multiple columns |
| **Slicer** | Filtering | 1 column (category) |
| **Matrix** | Heatmap | Rows + Columns + Values |

---

## 📝 **Step-by-Step Checklist**

### Setup:
- [ ] Created report from dataset
- [ ] Report canvas is visible
- [ ] Visualizations pane is visible
- [ ] Fields pane shows my tables and measures

### Build Dashboard:
- [ ] Created 4 KPI cards (Total, Sustainable, %, Recent)
- [ ] Created 3 slicers (Department, Year, SDG)
- [ ] Created line chart (Publications over time)
- [ ] Created bar chart (Departments by sustainable)
- [ ] Created bar chart (SDG coverage)
- [ ] Tested slicers work (they filter all visuals)

---

## 🔧 **Troubleshooting**

### Issue: Can't Find "Create Report" Button

**Solutions:**
1. Click on your dataset name
2. Look for **"Create report"** in the top ribbon or near dataset name
3. Try **"..."** menu → **"Create report"**
4. Or use **"Create"** icon in left sidebar → **"Report"**

### Issue: Fields Pane Doesn't Show Measures

**Solutions:**
1. Make sure you're in **Report view** (not Model view)
2. Check that measures are in the Publications table
3. Expand "Publications" table in Fields pane
4. Look for measures with calculator icon (📊)

### Issue: Visual Shows Error

**Common Errors:**
- **"Can't display the visual"**: Check if measures/columns are correct
- **"No data"**: Check if filters are too restrictive
- **"Relationship needed"**: Verify relationships are set up

**Fix:**
- Remove and re-add fields
- Check slicer filters aren't excluding all data
- Verify relationships in Model view

---

## 💡 **Pro Tips**

1. **Arrange Layout**: Drag visuals to arrange them nicely
2. **Use Format Pane**: Right-click visual → Format to customize
3. **Test Slicers**: Click different slicer values to verify filtering works
4. **Add Titles**: Format each visual → Title → Add descriptive title
5. **Save Often**: Power BI Service auto-saves, but be aware

---

## 🎨 **Visual Layout Example**

```
┌─────────────────────────────────────────┐
│  [Card] [Card] [Card] [Card]           │
│  Total   Sust.  %      Recent          │
├─────────────────────────────────────────┤
│  [Slicer] │  [Line Chart]              │
│  Dept     │  Publications Over Time    │
│           │                             │
│  [Slicer] │  [Bar Chart]               │
│  Year     │  Departments by Sustainable│
│           │                             │
│  [Slicer] │  [Bar Chart]               │
│  SDG      │  SDG Coverage              │
└─────────────────────────────────────────┘
```

---

## ✅ **Next Steps**

After creating visuals:
1. **Format visuals** (add titles, colors, fonts)
2. **Test slicers** (click different values, verify filtering)
3. **Add more pages** (SDG Explorer, Impact Stories)
4. **Save/Publish** report

---

**Start by clicking "Create report" on your dataset, then you can build all your visuals!** 🎉

If you can't find "Create report", tell me what you see when you click on your dataset and I'll help you locate it!





