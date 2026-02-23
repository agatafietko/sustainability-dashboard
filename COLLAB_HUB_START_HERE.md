# Collaboration Hub - START HERE
## Quick Start Guide (You Only Have Publications CSV)

---

## 🎯 **YOUR SITUATION**

You have:
- ✅ `for distribution case competition filtered_publications.csv` - Publications data

You need:
- ❌ Matching algorithm (doesn't exist yet)
- ❌ Compatibility scores (need to calculate)
- ❌ Power BI visualizations (need to build)

---

## 🚀 **STEP-BY-STEP (30 Minutes Total)**

### **STEP 1: Build the Matching Algorithm (10 minutes)**

**Run this command:**
```bash
python build_collab_hub_from_scratch.py
```

**What it does:**
- Reads your publications CSV
- Extracts researcher profiles
- Infers research methods from keywords/abstracts
- Calculates career stages
- Calculates compatibility scores (Topic 50% + Method 35% + Stage 15%)
- Creates all output files

**Wait for completion** - You'll see:
```
✓ COLLABORATION HUB MATCHING ALGORITHM COMPLETE!
```

**Files created:**
- `faculty_matches.csv` ✅
- `Collab_Matches_For_PowerBI.csv` ✅
- `Researcher_Profiles_For_PowerBI.csv` ✅
- `network_graph_data.csv` ✅

---

### **STEP 2: Import into Power BI (5 minutes)**

1. Open **Power BI Desktop**
2. Click **Get Data** → **Text/CSV**
3. Import these files:
   - `Collab_Matches_For_PowerBI.csv`
   - `Researcher_Profiles_For_PowerBI.csv`
   - `sdg_lookup.csv` (if you have it, or create manually)

4. For each file:
   - Click **Transform Data** to verify
   - Click **Close & Apply**

---

### **STEP 3: Create Relationships (2 minutes)**

1. Go to **Model** view (left sidebar, 3 circles icon)
2. Create relationships:
   - `Collab_Matches[Faculty_A_Name]` → `Researcher_Profiles[name]` (Many-to-One)
   - `Collab_Matches[Faculty_B_Name]` → `Researcher_Profiles[name]` (Many-to-One)
   - If you have `sdg_lookup`: `Collab_Matches[SDG]` → `sdg_lookup[SDG ID]` (Many-to-One)

3. Set **Cross-filter direction** to **Both** for all

---

### **STEP 4: Build Your First Visualization (10 minutes)**

**Create Top Matches Table:**

1. Click **Table** visual
2. **Columns**:
   - `Faculty_A_Name`
   - `Faculty_B_Name`
   - `Total_Score`
   - `Topic_Score`
   - `Method_Score`
   - `Stage_Score`
   - `Method_Reason`
3. **Sort**: By `Total_Score` (Descending)
4. **Filter**: Show top 20
5. **Format**:
   - Title: "Top Collaboration Matches"
   - Conditional formatting on `Total_Score`:
     - 85-100: Green
     - 70-84: Light green
     - 55-69: Yellow
     - <55: Gray

**Done!** You now have a working demo.

---

### **STEP 5: Add Method Complementarity Matrix (3 minutes)**

1. Click **Matrix** visual
2. **Rows**: `Faculty_A_Method`
3. **Columns**: `Faculty_B_Method`
4. **Values**: `Total_Score` (Average)
5. **Format**:
   - Title: "Method Complementarity Matrix"
   - Conditional formatting: Color scale
   - **Key**: Look for Theoretical + Empirical = High scores!

---

## ✅ **VALIDATION CHECK**

After Step 1, verify the algorithm works:

1. Open `faculty_matches.csv` in Excel
2. Look for matches where:
   - `Faculty_A_Method` = "Theoretical"
   - `Faculty_B_Method` = "Empirical"
   - `Method_Score` should be ~100 (high complementarity)

3. Look for matches where:
   - `Faculty_A_Method` = "Theoretical"
   - `Faculty_B_Method` = "Theoretical"
   - `Method_Score` should be ~25 (low complementarity)

**If these are correct, your algorithm is working!** ✅

---

## 🎯 **WHAT THE ALGORITHM DOES**

### **Compatibility Score Formula:**
```
Total Score = (Topic × 0.50) + (Method × 0.35) + (Stage × 0.15)
```

### **Topic Match (50% weight):**
- SDG alignment (70% of topic score)
- Keyword overlap (30% of topic score)

### **Method Match (35% weight):**
- **Rewards DIFFERENT methods** (complementarity)
- Theoretical + Empirical = 100 points
- Theoretical + Theoretical = 25 points
- This is the KEY innovation!

### **Career Stage (15% weight):**
- Pre-Tenure + Post-Tenure = 100 (mentorship)
- Same stage = 60-75 (peer collaboration)

---

## 📊 **NEXT STEPS**

Once you have the basic visualizations:

1. **Read**: `COLLAB_HUB_MVP_GUIDE.md` for full dashboard
2. **Add**: Score breakdown charts
3. **Add**: Network graph visualization
4. **Polish**: Format with Illinois colors
5. **Present**: Practice your demo

---

## 🚨 **TROUBLESHOOTING**

### **Problem**: Script fails to run
- **Solution**: Make sure you have pandas installed: `pip install pandas numpy`

### **Problem**: No matches generated
- **Solution**: Check that your CSV has valid data (names, years, keywords)

### **Problem**: Method scores all the same
- **Solution**: The script infers methods from keywords. If keywords are missing, it defaults to "Mixed Methods"

### **Problem**: Power BI won't load CSV
- **Solution**: Check file encoding (should be UTF-8). Try opening in Excel and re-saving.

---

## 💡 **KEY INSIGHT**

**The algorithm rewards complementary methods, not identical methods!**

This is what makes your solution innovative:
- ❌ Traditional: "Find researchers with same methods"
- ✅ Your solution: "Find researchers with COMPLEMENTARY methods"

**Show this in your presentation!**

---

## 📁 **FILE STRUCTURE AFTER STEP 1**

```
Case Competition/
├── for distribution case competition filtered_publications.csv  (Your input)
│
├── build_collab_hub_from_scratch.py                            (Script you run)
│
├── faculty_matches.csv                                          (All matches)
├── best_faculty_match.csv                                        (Top 50)
├── Collab_Matches_For_PowerBI.csv                               (Power BI ready)
├── Researcher_Profiles_For_PowerBI.csv                          (Profiles)
└── network_graph_data.csv                                       (Network)
```

---

**Start with Step 1 and you'll have a working Collaboration Hub in 30 minutes!** 🚀



