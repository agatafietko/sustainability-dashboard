# Essential Measures (Aggregations) for Your Dashboard

## 🎯 **Core Measures You Need**

These are the key aggregations you'll use in your visuals. Copy these into Power BI as measures.

---

## 📊 **1. Basic Counts**

### Total Publications
```DAX
Total Publications = COUNTROWS(Publications)
```
**Use for**: KPI card showing total number of publications

### Sustainable Publications
```DAX
Sustainable Publications = 
CALCULATE(
    COUNTROWS(Publications),
    Publications[is_sustain] = TRUE()
)
```
**Use for**: KPI card showing how many are sustainable

### Sustainable Percentage
```DAX
Sustainable % = 
DIVIDE(
    [Sustainable Publications],
    [Total Publications],
    0
)
```
**Use for**: KPI card showing percentage (20.9%)

---

## 📈 **2. Time-Based Measures**

### Recent Publications (Last 5 Years)
```DAX
Recent Publications = 
CALCULATE(
    [Total Publications],
    Publications[is_recent] = TRUE()
)
```
**Use for**: Showing recent activity

### Recent Sustainable
```DAX
Recent Sustainable = 
CALCULATE(
    [Sustainable Publications],
    Publications[is_recent] = TRUE()
)
```
**Use for**: Sustainable publications in last 5 years

---

## 🏢 **3. Department Measures**

### Publications by Department
```DAX
Publications by Department = 
CALCULATE(
    [Total Publications],
    ALLEXCEPT(Publications, Publications[department])
)
```
**Use for**: Bar chart showing publications per department

### Sustainable by Department
```DAX
Sustainable by Department = 
CALCULATE(
    [Sustainable Publications],
    ALLEXCEPT(Publications, Publications[department])
)
```
**Use for**: Bar chart showing sustainable publications per department

---

## 🌍 **4. SDG Measures**

### Publications by SDG
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
**Use for**: Chart showing publications per SDG

### Sustainable by SDG
```DAX
Sustainable by SDG = 
VAR SelectedSDG = SELECTEDVALUE('sdg_lookup'[SDG ID])
RETURN
IF(
    NOT ISBLANK(SelectedSDG),
    CALCULATE(
        [Sustainable Publications],
        FILTER(
            'SDG_Mappings',
            'SDG_Mappings'[SDG ID] = SelectedSDG
        )
    ),
    BLANK()
)
```
**Use for**: Chart showing sustainable publications per SDG

---

## 📅 **5. Year Trends**

### Publications by Year
```DAX
Publications by Year = 
CALCULATE(
    [Total Publications],
    ALLEXCEPT(Publications, Publications[publication_year])
)
```
**Use for**: Line chart showing trend over time

### Sustainable by Year
```DAX
Sustainable by Year = 
CALCULATE(
    [Sustainable Publications],
    ALLEXCEPT(Publications, Publications[publication_year])
)
```
**Use for**: Line chart overlay showing sustainable trend

---

## 🏆 **6. Top Journal Measures**

### Top Journal Publications
```DAX
Top Journal Publications = 
CALCULATE(
    [Total Publications],
    Publications[is_top_journal] = TRUE()
)
```
**Use for**: KPI showing publications in top journals

---

## 📝 **7. Impact Story Measure**

### Impact Story (Dynamic Text)
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
    IF(
        IsSustainable,
        "SDG Focus: " & SDGList & UNICHAR(10) & UNICHAR(10),
        ""
    ) &
    IF(
        NOT ISBLANK(Journal),
        "Journal: " & Journal & UNICHAR(10) & UNICHAR(10),
        ""
    ) &
    IF(
        NOT ISBLANK(DOI),
        "DOI: " & DOI & UNICHAR(10) & UNICHAR(10),
        ""
    ) &
    "Why it matters:" & UNICHAR(10) &
    IF(
        LEN(Abstract) > 500,
        LEFT(Abstract, 500) & "...",
        Abstract
    ),
    "👆 Select a single publication to view its Impact Story."
)
```
**Use for**: Dynamic text card that shows story when you select a publication

---

## 🎯 **Priority Measures (Start Here)**

### Must-Have (For Basic Dashboard):
1. ✅ **Total Publications** - KPI card
2. ✅ **Sustainable Publications** - KPI card
3. ✅ **Sustainable %** - KPI card
4. ✅ **Publications by Year** - Line chart
5. ✅ **Sustainable by Department** - Bar chart

### Nice-to-Have (For Advanced Dashboard):
6. ✅ **Publications by SDG** - SDG coverage chart
7. ✅ **Recent Publications** - KPI card
8. ✅ **Impact Story** - Dynamic text card

---

## 📋 **How to Add Measures**

### Step 1: Create Measure
1. Go to **Data** view
2. Select **Publications** table
3. Click **New Measure** (top ribbon)
4. Paste measure code
5. Click ✓ to save

### Step 2: Use in Visuals
1. Create visual (card, chart, etc.)
2. Drag measure to **Values** field
3. Visual will show the aggregated value

---

## 🎨 **Where to Use Each Measure**

### KPI Cards (Top Row):
- Total Publications
- Sustainable Publications
- Sustainable %
- Recent Publications (optional)

### Line Chart (Trends):
- X-axis: `publication_year` (Don't summarize)
- Y-axis: Publications by Year
- Y-axis (2nd): Sustainable by Year

### Bar Chart (Department Performance):
- Y-axis: `department` (Don't summarize)
- X-axis: Sustainable by Department
- Sort: Descending

### Bar Chart (SDG Coverage):
- X-axis: `SDG Name` (Don't summarize)
- Y-axis: Publications by SDG
- Sort: Descending

### Impact Story Card:
- Drag "Impact Story" measure to card
- Shows dynamic text when publication is selected

---

## ✅ **Quick Checklist**

- [ ] Created "Total Publications" measure
- [ ] Created "Sustainable Publications" measure
- [ ] Created "Sustainable %" measure
- [ ] Created "Publications by Year" measure
- [ ] Created "Sustainable by Department" measure
- [ ] Created "Publications by SDG" measure (optional)
- [ ] Created "Impact Story" measure (optional)
- [ ] Tested measures in visuals

---

## 💡 **Pro Tips**

1. **Start Simple**: Create the first 5 measures first
2. **Test Each**: Add measure to a card and verify it works
3. **Use in Visuals**: Measures go in "Values", not "Columns"
4. **Format**: Right-click measure → Format → Set as percentage for %

---

**These are all the aggregations you need! Start with the first 5 measures, then add more as needed.** 🎉





