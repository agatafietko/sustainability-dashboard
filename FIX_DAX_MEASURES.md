# Fix DAX Measure Errors - Troubleshooting Guide

## 🔍 **Error: "Too many arguments were passed to the DISTINCTCOUNT function"**

### **Problem:**
The `DISTINCTCOUNT` function only accepts **one argument** (a column), not a filtered table and a column.

### **Wrong Code:**
```DAX
SDG Coverage Score = 
VAR TotalSDGs = 17
VAR CoveredSDGs =
    DISTINCTCOUNT(
        FILTER(
            'SDG_Mappings',
            RELATED(Publications[is_sustain]) = TRUE()
        ),
        'SDG_Mappings'[SDG ID]  // ❌ ERROR: Too many arguments
    )
RETURN
DIVIDE(CoveredSDGs, TotalSDGs, 0) * 100
```

### **Correct Code (Option 1 - Using CALCULATE):**
```DAX
SDG Coverage Score = 
VAR TotalSDGs = 17
VAR CoveredSDGs =
    CALCULATE(
        DISTINCTCOUNT('SDG_Mappings'[SDG ID]),
        FILTER(
            'SDG_Mappings',
            RELATED(Publications[is_sustain]) = TRUE()
        )
    )
RETURN
DIVIDE(CoveredSDGs, TotalSDGs, 0) * 100
```

### **Correct Code (Option 2 - Simpler):**
```DAX
SDG Coverage Score = 
VAR TotalSDGs = 17
VAR CoveredSDGs =
    CALCULATE(
        DISTINCTCOUNT('SDG_Mappings'[SDG ID]),
        Publications[is_sustain] = TRUE()
    )
RETURN
DIVIDE(CoveredSDGs, TotalSDGs, 0) * 100
```

---

## ✅ **Fixed Phase 1 Measures**

### **Measure 1: SDG Coverage Score (FIXED)**

```DAX
SDG Coverage Score = 
VAR TotalSDGs = 17
VAR CoveredSDGs =
    CALCULATE(
        DISTINCTCOUNT('SDG_Mappings'[SDG ID]),
        Publications[is_sustain] = TRUE()
    )
RETURN
DIVIDE(CoveredSDGs, TotalSDGs, 0) * 100
```

---

### **Measure 2: SDG Coverage by SDG (FIXED)**

```DAX
SDG Coverage by SDG = 
VAR SelectedSDG = SELECTEDVALUE('sdg_lookup'[SDG ID])
VAR SDGCount = 
    IF(
        NOT ISBLANK(SelectedSDG),
        CALCULATE(
            COUNTROWS('SDG_Mappings'),
            'SDG_Mappings'[SDG ID] = SelectedSDG
        ),
        BLANK()
    )
VAR TotalPublications = [Total Publications]
VAR CoveragePercent = 
    IF(
        TotalPublications > 0,
        DIVIDE(SDGCount, TotalPublications, 0) * 100,
        BLANK()
    )
RETURN
CoveragePercent
```

---

### **Measure 3: SDG Gap Status (FIXED)**

```DAX
SDG Gap Status = 
VAR Coverage = [SDG Coverage by SDG]
RETURN
SWITCH(
    TRUE(),
    Coverage < 2, "Critical Gap",
    Coverage < 5, "Significant Gap",
    Coverage < 10, "Moderate Gap",
    Coverage >= 10, "Well Covered",
    "No Data"
)
```

---

### **Measure 4: Critical Gaps Count (FIXED)**

```DAX
Critical Gaps = 
CALCULATE(
    DISTINCTCOUNT('sdg_lookup'[SDG ID]),
    FILTER(
        ALL('sdg_lookup'),
        [SDG Coverage by SDG] < 2
    )
)
```

---

### **Measure 5: Significant Gaps Count (FIXED)**

```DAX
Significant Gaps = 
CALCULATE(
    DISTINCTCOUNT('sdg_lookup'[SDG ID]),
    FILTER(
        ALL('sdg_lookup'),
        [SDG Coverage by SDG] >= 2 && [SDG Coverage by SDG] < 5
    )
)
```

---

### **Measure 6: Well Covered SDGs (FIXED)**

```DAX
Well Covered SDGs = 
CALCULATE(
    DISTINCTCOUNT('sdg_lookup'[SDG ID]),
    FILTER(
        ALL('sdg_lookup'),
        [SDG Coverage by SDG] >= 10
    )
)
```

---

## 🔧 **Common DAX Errors & Fixes**

### **Error 1: DISTINCTCOUNT with multiple arguments**

**Wrong:**
```DAX
DISTINCTCOUNT(FILTER(Table, Condition), Column)
```

**Right:**
```DAX
CALCULATE(DISTINCTCOUNT(Column), FILTER(Table, Condition))
```

---

### **Error 2: RELATED() in wrong context**

**Wrong:**
```DAX
FILTER('SDG_Mappings', RELATED(Publications[is_sustain]) = TRUE())
```

**Right:**
```DAX
FILTER(
    'SDG_Mappings',
    RELATED(Publications[is_sustain]) = TRUE()
)
```

**Or better:**
```DAX
CALCULATE(
    DISTINCTCOUNT('SDG_Mappings'[SDG ID]),
    Publications[is_sustain] = TRUE()
)
```

---

### **Error 3: Using FILTER when CALCULATE is better**

**When to use CALCULATE:**
- Filtering based on related tables
- Simple conditions
- Better performance

**When to use FILTER:**
- Complex conditions
- Need to iterate over table
- Multiple conditions with AND/OR

---

## 📋 **Step-by-Step: Fix Your Current Measure**

### **Step 1: Delete the broken measure**
1. In **Data pane**, find "SDG Coverage Score"
2. **Right-click** → **Delete** (or select and press Delete)

### **Step 2: Create new measure with fixed code**
1. **Right-click Publications table** → **New measure**
2. **Paste this corrected code:**

```DAX
SDG Coverage Score = 
VAR TotalSDGs = 17
VAR CoveredSDGs =
    CALCULATE(
        DISTINCTCOUNT('SDG_Mappings'[SDG ID]),
        Publications[is_sustain] = TRUE()
    )
RETURN
DIVIDE(CoveredSDGs, TotalSDGs, 0) * 100
```

3. **Click ✓ (checkmark)** to save

### **Step 3: Verify it works**
1. **Create a card visual**
2. **Drag "SDG Coverage Score"** to the card
3. **Should show a percentage** (e.g., 88.2% if 15 out of 17 SDGs are covered)

---

## 🎯 **Key DAX Rules to Remember**

1. **DISTINCTCOUNT** takes only **one argument**: a column
   - ✅ `DISTINCTCOUNT(Table[Column])`
   - ❌ `DISTINCTCOUNT(FilteredTable, Column)`

2. **Use CALCULATE** to add filters:
   - ✅ `CALCULATE(DISTINCTCOUNT(Column), FilterCondition)`
   - ✅ `CALCULATE(Measure, FilterCondition)`

3. **FILTER** returns a table, not a value:
   - Use FILTER inside CALCULATE
   - Or use FILTER to create a filtered table variable

4. **RELATED** works in row context:
   - Use in calculated columns
   - Or inside FILTER when iterating

---

## ✅ **Quick Reference: Correct Syntax Patterns**

### **Pattern 1: Count distinct with filter**
```DAX
CALCULATE(
    DISTINCTCOUNT(Table[Column]),
    FilterCondition
)
```

### **Pattern 2: Count distinct with multiple filters**
```DAX
CALCULATE(
    DISTINCTCOUNT(Table[Column]),
    Table[Column1] = Value1,
    Table[Column2] = Value2
)
```

### **Pattern 3: Count distinct with FILTER function**
```DAX
CALCULATE(
    DISTINCTCOUNT(Table[Column]),
    FILTER(
        Table,
        Table[Column1] = Value1 && Table[Column2] = Value2
    )
)
```

---

## 🐛 **If Still Getting Errors**

### **Check These:**
1. **Table names**: Exact match (case-sensitive)
   - `'SDG_Mappings'` not `'SDG_Mapping'`
   - `Publications` not `Publication`

2. **Column names**: Exact match
   - `'SDG_Mappings'[SDG ID]` (with space)
   - `Publications[is_sustain]` (with underscore)

3. **Relationships**: Make sure relationships are set up
   - Publications ↔ SDG_Mappings
   - SDG_Mappings ↔ sdg_lookup

4. **Data types**: Make sure columns are correct type
   - `is_sustain` should be True/False
   - `SDG ID` should be whole number

---

## 💡 **Pro Tips**

1. **Test incrementally**: Build measure step by step
2. **Use variables**: Makes debugging easier
3. **Check relationships**: Errors often come from relationship issues
4. **Simplify first**: Get basic version working, then add complexity

---

**Replace your broken measure with the fixed version above!** 🎉

The key fix: Use `CALCULATE(DISTINCTCOUNT(Column), FilterCondition)` instead of `DISTINCTCOUNT(FILTER(...), Column)`




