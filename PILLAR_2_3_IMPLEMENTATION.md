# Pillar 2 & 3 Implementation Guide - Power BI Dashboard

## 🎯 **Overview**

This guide covers implementing:
- **Pillar 2**: Strategic Tools for University Leadership
- **Pillar 3**: Advanced Visualizations
- **Extra**: Stakeholder interview integration

---

## 📊 **PILLAR 2: Strategic Planning View**

### **Feature 1: Research Portfolio Analysis (SDG Mapping)**

#### Create SDG Coverage Matrix/Heatmap:

**Step 1: Create Matrix Visual**
1. Click blank area on canvas
2. In **Visualizations pane**, click **"Matrix"** icon (looks like a grid)
3. A blank matrix appears

**Step 2: Add Fields**
1. In **Fields pane**:
   - **Rows**: Drag `department` (from Publications)
   - **Columns**: Drag `SDG Name` (from sdg_lookup)
   - **Values**: Drag `Total Publications` measure (or create "Publications by SDG" measure)

**Step 3: Format as Heatmap**
1. **Select matrix**
2. **Format pane** → **"Values"** section
3. **Conditional formatting** → **"Background color"**
4. **Enable**: ON
5. **Color scale**: 
   - **Minimum**: Light color (light blue or light orange)
   - **Maximum**: Dark color (dark blue #13294B)
6. Matrix now shows color intensity based on publication count

**Step 4: Add Title**
1. **Format pane** → **"General"** section
2. **Title**: ON
3. **Title text**: "Research Portfolio Analysis: SDG Coverage by Department"
4. **Font size**: 18
5. **Font color**: Dark blue (#13294B)

**Step 5: Format Matrix**
1. **Format pane** → **"Visual"** → **"Effects"**:
   - Background: White
   - Border: ON, Color: Light gray, Width: 1px
   - Rounded corners: 4px
2. **Format pane** → **"Grid"**:
   - Grid lines: ON
   - Color: Light gray
   - Width: 1px

---

### **Feature 2: Emerging Trend Analysis (Predictive Analytics)**

#### Create Trend Analysis with Forecast:

**Step 1: Create Line Chart**
1. Click **Line chart** visual
2. **X-axis**: Drag `publication_year`
3. **Y-axis**: Drag `Total Publications` measure

**Step 2: Add Analytics (Forecast)**
1. **Select line chart**
2. **Format pane** → **"Analytics"** section (or look for "Analytics" tab)
3. **Forecast**: ON
4. **Forecast length**: 3-5 years
5. **Confidence interval**: 95%
6. Chart now shows forecasted trend line

**Step 3: Add Multiple Lines (SDG Trends)**
1. **Y-axis**: Add multiple measures:
   - `Total Publications`
   - `Sustainable Publications`
   - Or create measures for specific SDGs
2. **Legend**: Shows different lines
3. **Format**: Different colors for each line

**Step 4: Add Title**
1. **Format pane** → **"General"**:
   - Title: ON
   - Title text: "Emerging Research Trends & Forecast"
   - Font size: 18

**Step 5: Add Data Labels**
1. **Format pane** → **"Data labels"**:
   - Data labels: ON
   - Position: Above (for key points)
   - Font size: 11

---

### **Feature 3: Collaboration Hub (Search & Filter)**

#### Create Advanced Filtering System:

**Step 1: Create Slicers**
1. **Slicer 1: SDG Alignment**
   - Click **Slicer** visual
   - Drag `SDG Name` (from sdg_lookup)
   - Format: Dropdown or list
   - Title: "Filter by SDG"

2. **Slicer 2: Research Methods/Keywords**
   - Click **Slicer** visual
   - Drag `keyword` (from Keywords table)
   - Format: Search box (if available) or list
   - Title: "Filter by Research Area"

3. **Slicer 3: Department**
   - Click **Slicer** visual
   - Drag `department`
   - Format: Dropdown
   - Title: "Filter by Department"

**Step 2: Create Searchable Table**
1. Click **Table** visual
2. **Columns**: 
   - `title` (Publications)
   - `name` (Publications)
   - `department` (Publications)
   - `SDG Name` (from sdg_lookup - via relationship)
   - `keyword` (from Keywords - via relationship)
   - `publication_year`
3. **Format**: 
   - Enable search/filter in table
   - Sortable columns
   - Conditional formatting for SDG alignment

**Step 3: Add Title**
1. **Format pane** → **"General"**:
   - Title: ON
   - Title text: "Collaboration Hub: Find Research Partners"
   - Font size: 18

**Step 4: Cross-Filter Setup**
- All slicers should filter the table
- Table should show researchers matching selected criteria
- Use relationships to show SDG and keyword info

---

### **Feature 4: Automated Impact Narratives**

#### Create Dynamic Impact Story Card:

**Step 1: Create Impact Story Measure** (if not already created)
```DAX
Impact Story = 
VAR Title = SELECTEDVALUE(Publications[title])
VAR Author = SELECTEDVALUE(Publications[name])
VAR Department = SELECTEDVALUE(Publications[department])
VAR Year = SELECTEDVALUE(Publications[publication_year])
VAR Journal = SELECTEDVALUE(Publications[journal_title])
VAR DOI = SELECTEDVALUE(Publications[doi])
VAR Abstract = SELECTEDVALUE(Publications[abstract_text])
VAR IsSustainable = SELECTEDVALUE(Publications[is_sustain])

VAR SDGList = 
    IF(
        IsSustainable,
        CONCATENATEX(
            DISTINCT(
                RELATEDTABLE('sdg_lookup')
            ),
            'sdg_lookup'[SDG Name],
            ", "
        ),
        "N/A"
    )

RETURN
IF(
    HASONEVALUE(Publications[article_uuid]),
    "📊 IMPACT STORY" & UNICHAR(10) & UNICHAR(10) &
    "Title: " & Title & UNICHAR(10) & UNICHAR(10) &
    "Author: " & Author & UNICHAR(10) &
    "Department: " & Department & UNICHAR(10) &
    "Year: " & Year & UNICHAR(10) & UNICHAR(10) &
    IF(IsSustainable, "SDG Focus: " & SDGList & UNICHAR(10) & UNICHAR(10), "") &
    IF(NOT ISBLANK(Journal), "Journal: " & Journal & UNICHAR(10) & UNICHAR(10), "") &
    IF(NOT ISBLANK(DOI), "DOI: " & DOI & UNICHAR(10) & UNICHAR(10), "") &
    "Why it matters:" & UNICHAR(10) &
    IF(LEN(Abstract) > 500, LEFT(Abstract, 500) & "...", Abstract),
    "👆 Select a publication to view its Impact Story."
)
```

**Step 2: Create Impact Stories Page**
1. **Add new page**: Click "+" → Rename to "Impact Stories"
2. **Add Table**: Publications list
   - Columns: `title`, `name`, `department`, `publication_year`
3. **Add Card/Text Box**: 
   - Drag `Impact Story` measure to card
   - Format: Large text box, multi-line
   - Position: Right side of table

**Step 3: Format Impact Story Card**
1. **Format pane** → **"General"**:
   - Title: ON
   - Title text: "Automated Impact Narrative"
   - Font size: 18
2. **Format pane** → **"Values"**:
   - Font size: 12-14
   - Font color: Dark gray
   - Text wrap: ON
3. **Format pane** → **"Effects"**:
   - Background: Light blue or light gray
   - Border: ON, Color: Blue
   - Padding: 15px

**Step 4: Make It Interactive**
- When user clicks row in table, Impact Story updates automatically
- Add slicers to filter which stories appear

---

## 🎨 **PILLAR 3: Advanced Visualizations**

### **Feature 1: Network Graphs (Collaboration Visualization)**

#### Option A: Using Power BI Custom Visual (Recommended)

**Step 1: Install Network Visual**
1. In **Visualizations pane**, click **"..."** (Get more visuals)
2. Search for **"Network Navigator"** or **"Chord Chart"**
3. Click **"Add"** to install

**Step 2: Create Network Graph**
1. Click **Network Navigator** visual
2. **Source**: Drag `department` (or `name` for researcher-level)
3. **Target**: Drag `SDG Name` (or another `department` for collaboration)
4. **Weight**: Drag `Total Publications` measure
5. Graph shows connections between departments and SDGs

**Step 3: Format Network Graph**
1. **Format pane** → **"General"**:
   - Title: ON
   - Title text: "Research Collaboration Network"
   - Font size: 18
2. **Format pane** → **"Visual"**:
   - Node colors: Use Illinois Blue/Orange
   - Edge colors: Light gray
   - Node size: Based on publication count

#### Option B: Alternative - Use Chord Chart
1. Install **"Chord Chart"** custom visual
2. **Source**: `department`
3. **Target**: `SDG Name`
4. **Value**: `Total Publications`
5. Shows circular network of connections

---

### **Feature 2: Geographic Heatmaps**

#### Create Geographic Visualization:

**Step 1: Check Your Data**
- You need geographic data (country, region, etc.)
- If not in your data, you can:
  - Add a calculated column based on keywords
  - Or use journal locations
  - Or create a mapping table

**Step 2: Create Map Visual**
1. Click **Map** visual (or **Filled Map**)
2. **Location**: Drag geographic field (if available)
3. **Size**: Drag `Total Publications` measure
4. **Color**: Drag `Sustainable Publications` measure
5. Map shows geographic distribution

**Step 3: Format Map**
1. **Format pane** → **"General"**:
   - Title: ON
   - Title text: "Global Research Impact"
   - Font size: 18
2. **Format pane** → **"Data colors"**:
   - Color scale: Light to dark (blue or orange)
   - Show legend: ON

**Note**: If you don't have geographic data, you can:
- Create a "Region" calculated column based on keywords
- Or use a different visualization (e.g., matrix by region)

---

### **Feature 3: Interactive Trendlines (Streamgraphs)**

#### Create Streamgraph Visualization:

**Step 1: Install Streamgraph Custom Visual**
1. In **Visualizations pane**, click **"..."** (Get more visuals)
2. Search for **"Streamgraph"** or **"Area Chart"**
3. Click **"Add"** to install

**Step 2: Create Streamgraph**
1. Click **Streamgraph** visual
2. **X-axis**: Drag `publication_year`
3. **Legend**: Drag `SDG Name` (from sdg_lookup)
4. **Values**: Drag `Total Publications` measure
5. Chart shows stacked area chart with SDG trends over time

**Step 3: Format Streamgraph**
1. **Format pane** → **"General"**:
   - Title: ON
   - Title text: "SDG Research Trends Over Time"
   - Font size: 18
2. **Format pane** → **"Data colors"**:
   - Use different colors for each SDG
   - Use Illinois color palette (blues and oranges)
3. **Format pane** → **"Visual"**:
   - Smooth curves: ON
   - Show data labels: ON (for key years)

#### Alternative: Use Standard Area Chart
1. Click **Area chart** visual
2. **X-axis**: `publication_year`
3. **Y-axis**: `Total Publications`
4. **Legend**: `SDG Name`
5. Shows stacked area chart (similar to streamgraph)

---

## 📋 **Complete Dashboard Structure**

### **Page 1: Executive Overview**
- 4 KPI cards
- Line chart (trends)
- Bar chart (departments)

### **Page 2: Strategic Planning View** (NEW)
- SDG Coverage Matrix/Heatmap
- Emerging Trend Analysis (with forecast)
- Collaboration Hub (searchable table with slicers)
- Impact Stories section

### **Page 3: Advanced Visualizations** (NEW)
- Network Graph (collaboration)
- Geographic Heatmap (if data available)
- Streamgraph (SDG trends over time)

### **Page 4: Impact Stories** (NEW)
- Publications table
- Dynamic Impact Story card
- Slicers for filtering

---

## ✅ **Implementation Checklist**

### Pillar 2 Features:
- [ ] SDG Coverage Matrix/Heatmap created
- [ ] Emerging Trend Analysis with forecast
- [ ] Collaboration Hub with advanced slicers
- [ ] Searchable publications table
- [ ] Automated Impact Narratives card
- [ ] Impact Stories page created

### Pillar 3 Features:
- [ ] Network Graph installed and configured
- [ ] Geographic Heatmap created (if data available)
- [ ] Streamgraph/Area chart for SDG trends
- [ ] All advanced visuals formatted professionally

### Design:
- [ ] All visuals have titles (18pt, dark blue)
- [ ] Consistent color scheme (Illinois Blue/Orange)
- [ ] Professional formatting applied
- [ ] Interactive elements work (slicers, cross-filtering)

---

## 💡 **Pro Tips**

1. **Custom Visuals**: Some advanced visuals require custom visuals from AppSource
2. **Data Requirements**: Geographic heatmap needs location data
3. **Performance**: Network graphs can be slow with large datasets - filter data
4. **Testing**: Test all slicers and cross-filtering to ensure they work
5. **Documentation**: Add tooltips/descriptions explaining each feature

---

## 🎯 **Next Steps**

1. **Create new pages** for Strategic Planning and Advanced Visualizations
2. **Install custom visuals** (Network Navigator, Streamgraph)
3. **Build each feature** following the steps above
4. **Format consistently** using Illinois colors
5. **Test interactivity** (slicers, cross-filtering, impact stories)

---

**Follow these steps to implement all Pillar 2 and 3 features!** 🎉

For specific questions about any feature, let me know which one and I'll provide more detailed instructions!




