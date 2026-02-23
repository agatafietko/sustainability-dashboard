# Clear Chart Creation Guide - Step by Step

## 📊 **Chart 3: Trend Line Chart**

### Step 1: Create Line Chart
1. Click **blank area** on canvas
2. In **Visualizations pane**, click **"Line chart"** icon (line going up)
3. Blank line chart appears

### Step 2: Add Fields
1. In **Fields pane** (right side):
   - **X-axis**: Drag `publication_year` (from Publications table)
   - **Y-axis**: Drag `Publications by Year` measure
   - **Y-axis (2nd line)**: Click **"+"** next to Y-axis, drag `Sustainable Publications` measure

### Step 3: Add Title
1. **Select the line chart**
2. **Format pane** (right side) → **"General"** section
3. Find **"Title"** toggle - turn it **ON**
4. **Title text** field appears - type: **"Publications Over Time"**
5. **Font size**: 18
6. **Font color**: Dark blue (#13294B)
7. **Position**: Above chart

### Step 4: Format Chart
1. **Format pane** → **"Visual"** → **"Effects"**:
   - **Background**: White
   - **Visual border**: ON
   - **Border color**: Light gray
   - **Border width**: 1px
   - **Rounded corners**: 4px

2. **Format pane** → **"Data colors"**:
   - **Line 1 color**: Illinois Blue (#13294B)
   - **Line 2 color**: Illinois Orange (#FF6B35)
   - **Line width**: 3px

3. **Format pane** → **"Y-axis"**:
   - **Title**: ON
   - **Title text**: "Number of Publications"
   - **Font size**: 12

4. **Format pane** → **"X-axis"**:
   - **Title**: ON
   - **Title text**: "Year"
   - **Font size**: 12

---

## 📊 **Chart 4: Department Bar Chart**

### Step 1: Create Bar Chart
1. Click **blank area** on canvas
2. In **Visualizations pane**, click **"Bar chart"** icon (horizontal bars)
3. Blank bar chart appears

### Step 2: Add Fields
1. In **Fields pane**:
   - **Y-axis**: Drag `department` (from Publications)
   - **X-axis**: Drag `Sustainable by Department` measure

### Step 3: Sort Descending
1. **Select bar chart**
2. Look for **"Sort"** icon (usually in top right of visual or Format pane)
3. Click **"Sort descending"** (highest to lowest)
4. Or: **Format pane** → **"General"** → **"Sort"** → Select "Descending"

### Step 4: Add Title
1. **Format pane** → **"General"** section
2. **Title**: ON
3. **Title text**: **"Top Departments by Sustainable Research"**
4. **Font size**: 18
5. **Font color**: Dark blue (#13294B)

### Step 5: Format Chart
1. **Format pane** → **"Visual"** → **"Effects"**:
   - **Background**: White
   - **Visual border**: ON, Light gray, 1px
   - **Rounded corners**: 4px

2. **Format pane** → **"Data colors"**:
   - **Color**: Illinois Orange (#FF6B35) or Blue (#13294B)
   - **Gradient**: OFF

3. **Format pane** → **"Data labels"**:
   - **Data labels**: ON
   - **Position**: End (outside bars)
   - **Font size**: 11

---

## 📊 **Chart 5: SDG Coverage Chart**

### Step 1: Create Bar Chart (Vertical)
1. Click **blank area** on canvas
2. In **Visualizations pane**, click **"Bar chart"** icon
3. **Change to vertical**: Look for orientation toggle, or it's vertical by default

### Step 2: Add Fields
1. In **Fields pane**:
   - **X-axis**: Drag `SDG Name` (from sdg_lookup table)
   - **Y-axis**: Drag `Total Publications` measure
   
   **OR** create "Publications by SDG" measure first:
   ```DAX
   Publications by SDG = 
   VAR SelectedSDG = SELECTEDVALUE('sdg_lookup'[SDG ID])
   RETURN
   IF(
       NOT ISBLANK(SelectedSDG),
       CALCULATE(
           [Total Publications],
           FILTER(
               'SDG_Mappings',
               'SDG_Mappings'[SDG ID] = SelectedSDG
           )
       ),
       BLANK()
   )
   ```
   Then use this measure instead

### Step 3: Sort Descending
1. **Select bar chart**
2. Click **"Sort descending"** icon
3. Bars now show highest SDG first

### Step 4: Add Title
1. **Format pane** → **"General"** section
2. **Title**: ON
3. **Title text**: **"Research Coverage by SDG"**
4. **Font size**: 18
5. **Font color**: Dark blue (#13294B)

### Step 5: Format Chart
1. **Format pane** → **"Visual"** → **"Effects"**:
   - **Background**: White
   - **Visual border**: ON, Light gray, 1px
   - **Rounded corners**: 4px

2. **Format pane** → **"Data colors"**:
   - **Color**: Illinois Blue (#13294B) or use conditional formatting by SDG
   - **Gradient**: OFF

3. **Format pane** → **"X-axis"**:
   - **Font size**: 11 (SDG names might be long)
   - **Angle**: 45 degrees (if names overlap)

4. **Format pane** → **"Data labels"**:
   - **Data labels**: ON
   - **Position**: Top (above bars)
   - **Font size**: 10

---

## 🎯 **Quick Reference: Adding Titles to Any Visual**

### Universal Steps:
1. **Select the visual**
2. **Format pane** (right side) → **"General"** section
3. **Title**: Toggle **ON**
4. **Title text**: Type your title
5. **Font size**: 18 (for main titles)
6. **Font color**: Dark blue (#13294B)
7. **Position**: Above visual (default)

---

## ✅ **Complete Checklist for All 3 Charts**

### Trend Line Chart:
- [ ] Line chart created
- [ ] X-axis: publication_year
- [ ] Y-axis: Publications by Year measure
- [ ] Y-axis (2nd): Sustainable Publications measure
- [ ] Title added: "Publications Over Time"
- [ ] Title formatted (18pt, dark blue)
- [ ] Chart formatted (colors, borders, rounded corners)
- [ ] Axis titles added

### Department Bar Chart:
- [ ] Bar chart created (horizontal)
- [ ] Y-axis: department
- [ ] X-axis: Sustainable by Department measure
- [ ] Sorted descending
- [ ] Title added: "Top Departments by Sustainable Research"
- [ ] Title formatted (18pt, dark blue)
- [ ] Chart formatted (colors, borders)
- [ ] Data labels added

### SDG Coverage Chart:
- [ ] Bar chart created (vertical)
- [ ] X-axis: SDG Name
- [ ] Y-axis: Total Publications (or Publications by SDG measure)
- [ ] Sorted descending
- [ ] Title added: "Research Coverage by SDG"
- [ ] Title formatted (18pt, dark blue)
- [ ] Chart formatted (colors, borders)
- [ ] Data labels added
- [ ] X-axis labels angled (if needed)

---

## 💡 **Pro Tips**

1. **Consistent Titles**: All charts should have 18pt, dark blue titles
2. **Sorting**: Always sort bar charts descending (highest first)
3. **Data Labels**: Add labels to bars for easy reading
4. **Colors**: Use Illinois Blue (#13294B) and Orange (#FF6B35)
5. **Spacing**: Leave room between charts for clean layout

---

**Follow these exact steps and all your charts will be properly formatted with titles!** 🎉




