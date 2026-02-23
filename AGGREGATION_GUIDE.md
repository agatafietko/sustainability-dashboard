# What Should and Shouldn't Be Aggregated in Power BI

## 🎯 **General Rule**

**Don't aggregate** (set to "Don't summarize"):
- Text fields (names, titles, departments)
- IDs and UUIDs (article_uuid, person_uuid)
- Categories (years, departments, countries)
- URLs and DOIs

**Can aggregate** (use Sum, Count, Average, etc.):
- Counts (how many publications)
- Percentages (sustainable %)
- Measures you create (Total Publications, etc.)

---

## ✅ **Should NOT Be Aggregated** (Set to "Don't summarize")

### From Your Publications Table:

| Column | Type | Should Be |
|--------|------|-----------|
| `article_uuid` | ID | Don't summarize ❌ |
| `title` | Text | Don't summarize ❌ |
| `name` | Text | Don't summarize ❌ |
| `department` | Category | Don't summarize ❌ |
| `email` | Text | Don't summarize ❌ |
| `publication_year` | Year | Don't summarize ❌ |
| `doi` | URL | Don't summarize ❌ |
| `abstract_text` | Text | Don't summarize ❌ |
| `journal_title` | Text | Don't summarize ❌ |
| `journal_issn` | Text | Don't summarize ❌ |
| `source` | Text | Don't summarize ❌ |

### Boolean Flags - Use "Count" Instead:
| Column | Type | Should Be |
|--------|------|-----------|
| `is_sustain` | Boolean | Count (how many are sustainable) ✅ |
| `is_recent` | Boolean | Count (how many are recent) ✅ |
| `is_top_journal` | Boolean | Count (how many are top journals) ✅ |

### From Other Tables:
- `Keywords[keyword]` - Don't summarize ❌
- `sdg_lookup[SDG Name]` - Don't summarize ❌
- `SDG_Mappings[SDG ID]` - Don't summarize ❌ (it's an ID)

---

## ✅ **CAN Be Aggregated** (Use Measures Instead)

Instead of aggregating columns, **create measures**:

### Examples:

**Don't do this:**
- ❌ Sum of `publication_year` (meaningless!)
- ❌ Sum of `article_uuid` (meaningless!)

**Do this instead:**
- ✅ Measure: `Total Publications = COUNTROWS(Publications)`
- ✅ Measure: `Sustainable Count = COUNTROWS(FILTER(Publications, Publications[is_sustain] = TRUE()))`

---

## 📋 **Quick Fix Checklist**

Go through each table and check:

### Publications Table:
- [ ] `article_uuid` → Don't summarize
- [ ] `title` → Don't summarize
- [ ] `name` → Don't summarize
- [ ] `department` → Don't summarize
- [ ] `publication_year` → Don't summarize
- [ ] `doi` → Don't summarize
- [ ] `abstract_text` → Don't summarize
- [ ] `journal_title` → Don't summarize
- [ ] `is_sustain` → Count (or Don't summarize)
- [ ] `is_recent` → Count (or Don't summarize)

### Keywords Table:
- [ ] `article_uuid` → Don't summarize
- [ ] `keyword` → Don't summarize

### SDG_Mappings Table:
- [ ] `article_uuid` → Don't summarize
- [ ] `SDG ID` → Don't summarize

### sdg_lookup Table:
- [ ] `SDG ID` → Don't summarize
- [ ] `SDG Name` → Don't summarize
- [ ] `SDG Short` → Don't summarize
- [ ] `Color` → Don't summarize

---

## 🔧 **How to Fix All at Once**

### Step 1: Go to Data View
1. Click **Data** icon (left sidebar)
2. Select each table one by one

### Step 2: For Each Column
1. **Click column header**
2. **Check "Summarization" dropdown**
3. **Set to "Don't summarize"** for:
   - Text fields
   - IDs
   - Years
   - Categories

4. **Set to "Count"** for:
   - Boolean flags (if you want to count them)

### Step 3: Create Measures Instead
Instead of aggregating columns, create measures:
- `Total Publications = COUNTROWS(Publications)`
- `Sustainable Publications = CALCULATE(COUNTROWS(Publications), Publications[is_sustain] = TRUE())`

---

## 💡 **Why This Matters**

### Wrong Way (Aggregating Columns):
```
Visual shows:
- Sum of publication_year = 4,038,000 (meaningless!)
- Sum of article_uuid = 2.5 trillion (meaningless!)
```

### Right Way (Don't Summarize + Measures):
```
Visual shows:
- publication_year as category: 2010, 2011, 2012...
- Total Publications (measure) = 1,899
- Sustainable Publications (measure) = 397
```

---

## 🎯 **Summary**

**Set to "Don't summarize":**
- ✅ All text fields
- ✅ All IDs and UUIDs
- ✅ Years (publication_year)
- ✅ Categories (department, SDG Name)
- ✅ URLs and DOIs

**Can use "Count":**
- ✅ Boolean flags (is_sustain, is_recent) - if you want to count how many

**Create Measures for Aggregations:**
- ✅ Total Publications (count)
- ✅ Sustainable Publications (count)
- ✅ Percentages
- ✅ Averages

---

## ✅ **Your Action Items**

1. **Go to Data view**
2. **Check each column** in each table
3. **Set summarization to "Don't summarize"** for:
   - IDs
   - Text fields
   - Years
   - Categories

4. **Create measures** for any aggregations you need:
   - Total Publications
   - Sustainable Publications
   - Sustainable %

5. **Use measures** in visuals, not aggregated columns

---

**Bottom line: Most columns should be "Don't summarize". Only use measures for aggregations!** 🎉





