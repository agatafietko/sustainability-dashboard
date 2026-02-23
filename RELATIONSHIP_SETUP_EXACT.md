# Exact Relationship Setup - Which Table Goes Where

## 🎯 **Clear Instructions for Each Relationship**

Here's exactly which table to put in "From" and "To" fields in Power BI:

---

## **Relationship 1: Publications ↔ SDG_Mappings**

### In Power BI "New Relationship" Dialog:

**From Table**: `SDG_Mappings` ✅  
**From Column**: `article_uuid`  
**To Table**: `Publications` ✅  
**To Column**: `article_uuid`  
**Cardinality**: **Many-to-One**  
**Cross-filter direction**: **Both**

**Why this order:**
- SDG_Mappings has many rows pointing to one Publication
- Publications is the main table (one side)
- SDG_Mappings is the detail table (many side)

**Visual:**
```
SDG_Mappings (Many rows)
    article_uuid = "abc-123"
    article_uuid = "abc-123"  ← Same publication
    article_uuid = "abc-123"  ← Same publication
         ↓
Publications (One row)
    article_uuid = "abc-123"
```

---

## **Relationship 2: Publications ↔ Keywords**

### In Power BI "New Relationship" Dialog:

**From Table**: `Keywords` ✅  
**From Column**: `article_uuid`  
**To Table**: `Publications` ✅  
**To Column**: `article_uuid`  
**Cardinality**: **Many-to-One**  
**Cross-filter direction**: **Both**

**Why this order:**
- Keywords has many rows pointing to one Publication
- Publications is the main table (one side)
- Keywords is the detail table (many side)

**Visual:**
```
Keywords (Many rows)
    article_uuid = "abc-123", keyword = "AI"
    article_uuid = "abc-123", keyword = "Healthcare"
    article_uuid = "abc-123", keyword = "Machine Learning"
         ↓
Publications (One row)
    article_uuid = "abc-123"
```

---

## **Relationship 3: SDG_Mappings ↔ sdg_lookup**

### In Power BI "New Relationship" Dialog:

**From Table**: `SDG_Mappings` ✅  
**From Column**: `SDG ID`  
**To Table**: `sdg_lookup` ✅  
**To Column**: `SDG ID`  
**Cardinality**: **Many-to-One**  
**Cross-filter direction**: **Both**

**Why this order:**
- SDG_Mappings has many rows pointing to one SDG in sdg_lookup
- sdg_lookup is the lookup/reference table (one side)
- SDG_Mappings is the detail table (many side)

**Visual:**
```
SDG_Mappings (Many rows)
    SDG ID = 3  ← Multiple publications
    SDG ID = 3  ← with SDG 3
    SDG ID = 3  ←
         ↓
sdg_lookup (One row)
    SDG ID = 3, SDG Name = "Good Health"
```

---

## 📋 **Quick Copy-Paste Reference**

### Relationship 1:
```
From Table: SDG_Mappings
From Column: article_uuid
To Table: Publications
To Column: article_uuid
Cardinality: Many-to-One
Cross-filter: Both
```

### Relationship 2:
```
From Table: Keywords
From Column: article_uuid
To Table: Publications
To Column: article_uuid
Cardinality: Many-to-One
Cross-filter: Both
```

### Relationship 3:
```
From Table: SDG_Mappings
From Column: SDG ID
To Table: sdg_lookup
To Column: SDG ID
Cardinality: Many-to-One
Cross-filter: Both
```

---

## 🎯 **Key Rule**

**Always put the detail table (many rows) in "From"**  
**Always put the main/lookup table (one row) in "To"**

**Pattern:**
- Detail table → Main table (Many-to-One)
- Detail table → Lookup table (Many-to-One)

---

## ✅ **Step-by-Step Example**

### Creating Relationship 1:

1. Click "Manage relationships" → "New"
2. Fill in:
   - **From Table**: Select `SDG_Mappings` from dropdown
   - **From Column**: Select `article_uuid` from dropdown
   - **To Table**: Select `Publications` from dropdown
   - **To Column**: Select `article_uuid` from dropdown
   - **Cardinality**: Select `Many-to-One`
   - **Cross-filter direction**: Select `Both`
3. Click OK

**Repeat for Relationships 2 and 3 with the tables/columns above.**

---

## 🔍 **How to Verify It's Correct**

After creating relationships:
1. Go to Semantic Model view
2. You should see lines connecting tables
3. The line should have:
   - **1** on the "To" side (Publications, sdg_lookup)
   - **∞** (infinity) on the "From" side (SDG_Mappings, Keywords)

**Visual in Model View:**
```
Publications (1)
    ↑
    │ (Many-to-One)
SDG_Mappings (∞)

Publications (1)
    ↑
    │ (Many-to-One)
Keywords (∞)

sdg_lookup (1)
    ↑
    │ (Many-to-One)
SDG_Mappings (∞)
```

---

## 🐛 **If It's Backwards**

If you accidentally set it backwards:
1. Delete the relationship
2. Create it again with the correct "From" and "To" tables
3. The "From" should always be the table with many rows
4. The "To" should always be the table with one row

---

**Summary: Put the detail table (many rows) in "From", main table (one row) in "To"!** 🎉





