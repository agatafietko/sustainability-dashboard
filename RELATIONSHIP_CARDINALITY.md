# Relationship Cardinality Guide

## 🎯 **Understanding Cardinality**

**One-to-Many (1:Many)**:
- One record in Table A can relate to many records in Table B
- Example: One publication can have many keywords

**Many-to-One (Many:1)**:
- Many records in Table A relate to one record in Table B
- Example: Many publications can relate to one SDG

**Note**: One-to-Many and Many-to-One are the same relationship, just viewed from different directions!

---

## 📋 **Your 3 Relationships**

### **Relationship 1: Publications → SDG_Mappings**

**Cardinality: One-to-Many (or Many-to-One)**

**From**: Publications (One)  
**To**: SDG_Mappings (Many)

**Why:**
- ✅ One publication can have multiple SDG mappings (top 1, top 2, top 3)
- ✅ One SDG_Mappings row belongs to only one publication
- ✅ Example: Publication A can have SDG 3, SDG 8, SDG 16

**In Power BI:**
- Set as: **Many-to-One** (from SDG_Mappings perspective)
- Or: **One-to-Many** (from Publications perspective)
- **Recommended**: **Many-to-One** (SDG_Mappings → Publications)

---

### **Relationship 2: Publications → Keywords**

**Cardinality: One-to-Many (or Many-to-One)**

**From**: Publications (One)  
**To**: Keywords (Many)

**Why:**
- ✅ One publication can have many keywords
- ✅ One keyword row belongs to only one publication
- ✅ Example: Publication A has keywords: "AI", "Healthcare", "Machine Learning"

**In Power BI:**
- Set as: **Many-to-One** (from Keywords perspective)
- Or: **One-to-Many** (from Publications perspective)
- **Recommended**: **Many-to-One** (Keywords → Publications)

---

### **Relationship 3: SDG_Mappings → sdg_lookup**

**Cardinality: Many-to-One**

**From**: SDG_Mappings (Many)  
**To**: sdg_lookup (One)

**Why:**
- ✅ Many SDG_Mappings rows can reference the same SDG
- ✅ One SDG in sdg_lookup can be referenced by many publications
- ✅ Example: Many publications can have SDG 3 (Good Health)

**In Power BI:**
- Set as: **Many-to-One** (SDG_Mappings → sdg_lookup)
- sdg_lookup is the "one" side (lookup table)
- SDG_Mappings is the "many" side

---

## 📊 **Visual Summary**

```
Publications (One)
    │
    ├─→ SDG_Mappings (Many) ──┐
    │                          │
    └─→ Keywords (Many)         │
                                │
                                ↓
                        sdg_lookup (One)
```

**Flow:**
- Publications → SDG_Mappings (1:Many)
- Publications → Keywords (1:Many)
- SDG_Mappings → sdg_lookup (Many:1)

---

## 🔧 **How to Set in Power BI**

### Relationship 1: Publications ↔ SDG_Mappings

**In Power BI:**
- From Table: **SDG_Mappings**
- From Column: `article_uuid`
- To Table: **Publications**
- To Column: `article_uuid`
- **Cardinality**: **Many-to-One** ✅
- **Cross-filter direction**: **Both** ✅

**Why this way:**
- Many SDG_Mappings can relate to one Publication
- Power BI reads it as "Many SDG_Mappings to One Publication"

---

### Relationship 2: Publications ↔ Keywords

**In Power BI:**
- From Table: **Keywords**
- From Column: `article_uuid`
- To Table: **Publications**
- To Column: `article_uuid`
- **Cardinality**: **Many-to-One** ✅
- **Cross-filter direction**: **Both** ✅

**Why this way:**
- Many Keywords can relate to one Publication
- Power BI reads it as "Many Keywords to One Publication"

---

### Relationship 3: SDG_Mappings ↔ sdg_lookup

**In Power BI:**
- From Table: **SDG_Mappings**
- From Column: `SDG ID`
- To Table: **sdg_lookup**
- To Column: `SDG ID`
- **Cardinality**: **Many-to-One** ✅
- **Cross-filter direction**: **Both** ✅

**Why this way:**
- Many SDG_Mappings can relate to one SDG in sdg_lookup
- sdg_lookup is the lookup/reference table (one side)

---

## ✅ **Quick Reference Table**

| Relationship | From Table | To Table | Cardinality | Why |
|-------------|-----------|----------|-------------|-----|
| **1** | SDG_Mappings | Publications | **Many-to-One** | Many SDG mappings → One publication |
| **2** | Keywords | Publications | **Many-to-One** | Many keywords → One publication |
| **3** | SDG_Mappings | sdg_lookup | **Many-to-One** | Many mappings → One SDG |

---

## 🎯 **Key Points**

1. **All relationships are Many-to-One** (from the detail table to the main table)
2. **Cross-filter direction: Both** - allows filtering in both directions
3. **Publications is the main table** - it's the "one" side in relationships 1 and 2
4. **sdg_lookup is a lookup table** - it's the "one" side in relationship 3

---

## 📋 **Step-by-Step Setup**

### For Each Relationship:

1. **Click "Manage relationships"**
2. **Click "New"**
3. **Fill in:**
   - From Table: (the "many" side)
   - From Column: (the foreign key)
   - To Table: (the "one" side)
   - To Column: (the primary key)
   - **Cardinality**: **Many-to-One** ✅
   - **Cross-filter direction**: **Both** ✅
4. **Click OK**

---

## 🐛 **Common Mistakes**

❌ **Wrong**: Setting as One-to-One
- Only use if there's exactly one record on both sides

❌ **Wrong**: Setting as Many-to-Many
- Only use if you need bidirectional many relationships

✅ **Correct**: Many-to-One for all your relationships
- This matches your data structure

---

## ✅ **Final Checklist**

- [ ] Relationship 1: SDG_Mappings → Publications (Many-to-One)
- [ ] Relationship 2: Keywords → Publications (Many-to-One)
- [ ] Relationship 3: SDG_Mappings → sdg_lookup (Many-to-One)
- [ ] All relationships have "Cross-filter direction: Both"
- [ ] Tested relationships by creating a visual that uses columns from multiple tables

---

**Summary: All 3 relationships are Many-to-One! Set them all that way in Power BI.** 🎉





