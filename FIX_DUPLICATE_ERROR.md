# Fix: Duplicate Value Error in Relationship

## 🔍 **Problem**

Error message:
```
Column 'article_uuid' in Table 'SDG_Mappings' contains a duplicate value 
and this is not allowed for columns on the one side of a many-to-one relationship
```

**What this means:**
- Power BI thinks `SDG_Mappings` is the "One" side
- But `SDG_Mappings[article_uuid]` has duplicates (one publication can have multiple SDGs)
- Power BI is confused about which side is which

---

## ✅ **Solution: Reverse the Relationship**

The relationship is set up backwards. Here's how to fix it:

### **Relationship 1: SDG_Mappings → Publications**

**Current (Wrong):**
- From Table: SDG_Mappings ❌
- To Table: Publications

**Correct Setup:**
- **From Table**: `Publications` ✅
- **From Column**: `article_uuid`
- **To Table**: `SDG_Mappings` ✅
- **To Column**: `article_uuid`
- **Cardinality**: **Many-to-One** (but reversed!)
- **Cross-filter direction**: Both

**OR** keep the original direction but change cardinality:

**Alternative (Keep Original Direction):**
- **From Table**: `SDG_Mappings`
- **From Column**: `article_uuid`
- **To Table**: `Publications`
- **To Column**: `article_uuid`
- **Cardinality**: **One-to-Many** ✅ (instead of Many-to-One)
- **Cross-filter direction**: Both

---

## 🎯 **Correct Setup for All Relationships**

### **Relationship 1: Publications ↔ SDG_Mappings**

**Option A (Recommended):**
- From Table: `Publications`
- From Column: `article_uuid`
- To Table: `SDG_Mappings`
- To Column: `article_uuid`
- **Cardinality**: **One-to-Many** ✅
- Cross-filter direction: Both

**Option B (Alternative):**
- From Table: `SDG_Mappings`
- From Column: `article_uuid`
- To Table: `Publications`
- To Column: `article_uuid`
- **Cardinality**: **Many-to-One** ✅
- Cross-filter direction: Both

**Why this works:**
- Publications[article_uuid] is unique (one row per publication)
- SDG_Mappings[article_uuid] has duplicates (many SDGs per publication)
- So Publications is the "One" side, SDG_Mappings is the "Many" side

---

### **Relationship 2: Publications ↔ Keywords**

**Same pattern:**
- From Table: `Publications`
- From Column: `article_uuid`
- To Table: `Keywords`
- To Column: `article_uuid`
- **Cardinality**: **One-to-Many** ✅
- Cross-filter direction: Both

**OR:**
- From Table: `Keywords`
- From Column: `article_uuid`
- To Table: `Publications`
- To Column: `article_uuid`
- **Cardinality**: **Many-to-One** ✅
- Cross-filter direction: Both

---

### **Relationship 3: SDG_Mappings ↔ sdg_lookup**

**This one should work:**
- From Table: `SDG_Mappings`
- From Column: `SDG ID`
- To Table: `sdg_lookup`
- To Column: `SDG ID`
- **Cardinality**: **Many-to-One** ✅
- Cross-filter direction: Both

**Why this works:**
- SDG_Mappings[SDG ID] has duplicates (many publications per SDG)
- sdg_lookup[SDG ID] is unique (one row per SDG)

---

## 🔧 **Step-by-Step Fix**

### Step 1: Delete the Broken Relationship
1. Go to **Semantic Model** view
2. Find the broken relationship
3. **Right-click** → **Delete** (or click **Delete** button)

### Step 2: Create Relationship Correctly

**For Relationship 1:**

**Option 1: Reverse Direction**
1. Click **"Manage relationships"** → **"New"**
2. Fill in:
   - **From Table**: `Publications`
   - **From Column**: `article_uuid`
   - **To Table**: `SDG_Mappings`
   - **To Column**: `article_uuid`
   - **Cardinality**: **One-to-Many** ✅
   - Cross-filter direction: Both
3. Click OK

**Option 2: Keep Direction, Change Cardinality**
1. Click **"Manage relationships"** → **"New"**
2. Fill in:
   - **From Table**: `SDG_Mappings`
   - **From Column**: `article_uuid`
   - **To Table**: `Publications`
   - **To Column**: `article_uuid`
   - **Cardinality**: **Many-to-One** ✅ (make sure Publications is the "To" side)
   - Cross-filter direction: Both
3. Click OK

### Step 3: Verify
- Should not see error
- Relationship line should show:
  - **1** on Publications side
  - **∞** on SDG_Mappings side

---

## 💡 **Key Rule**

**For Many-to-One:**
- The "To" table must have **unique values** in the relationship column
- The "From" table can have **duplicates**

**For One-to-Many:**
- The "From" table must have **unique values** in the relationship column
- The "To" table can have **duplicates**

**In your case:**
- `Publications[article_uuid]` = Unique ✅ (one row per publication)
- `SDG_Mappings[article_uuid]` = Has duplicates ✅ (many SDGs per publication)
- So: Publications = One, SDG_Mappings = Many

---

## ✅ **Quick Fix Checklist**

- [ ] Deleted the broken relationship
- [ ] Created new relationship with correct direction
- [ ] Set cardinality correctly (One-to-Many or Many-to-One)
- [ ] Verified no error message
- [ ] Tested relationship works in a visual

---

## 🐛 **If Still Getting Error**

**Check if Publications[article_uuid] has duplicates:**
1. Go to **Data view**
2. Click **Publications** table
3. Look for duplicate `article_uuid` values
4. If there are duplicates, that's a data issue - need to deduplicate

**Most likely:**
- The relationship direction/cardinality is wrong
- Try reversing it or changing cardinality

---

**Try Option 1 (reverse direction) first - that usually fixes it!** 🎉





