# 🚀 Quick Start Guide

## ✅ What's Been Created

Your data model is **ready to import into Power BI**! Here's what you have:

### 📁 Data Files (Ready to Import)
1. **`sdg_lookup.csv`** - SDG reference table with names and colors
2. **`Publications_cleaned.csv`** - 1,899 cleaned publications
3. **`Keywords_cleaned.csv`** - 139,481 keyword mappings
4. **`SDG_Mappings_cleaned.csv`** - 714 SDG-to-publication links

### 📄 Documentation Files
1. **`POWER_BI_BUILD_GUIDE.md`** - Complete step-by-step instructions
2. **`DAX_Measures.txt`** - All Power BI measures (copy & paste ready)
3. **`prepare_data_for_powerbi.py`** - Data cleaning script (already run)

---

## 🎯 Your Next Steps (30 minutes)

### 1. Open Power BI Desktop
   - Download if needed: https://powerbi.microsoft.com/desktop/

### 2. Import Data (5 minutes)
   - **Get Data** → **Text/CSV**
   - Import all 4 CSV files from your folder
   - Click **Close & Apply** for each

### 3. Create Relationships (2 minutes)
   - Switch to **Model** view
   - Drag connections:
     - `Publications[article_uuid]` → `SDG_Mappings[article_uuid]`
     - `Publications[article_uuid]` → `Keywords[article_uuid]`
     - `SDG_Mappings[SDG ID]` → `sdg_lookup[SDG ID]`

### 4. Add DAX Measures (5 minutes)
   - Open `DAX_Measures.txt`
   - Copy measures into Power BI (New Measure button)
   - Start with: Total Publications, Sustainable Publications, Sustainable %, Impact Story

### 5. Build First Page (15 minutes)
   - Create **Overview** page
   - Add 4 KPI cards (use the measures)
   - Add slicers (Department, Year, SDG)
   - Add line chart (Year × Publications)
   - Add bar chart (Department × Sustainable Publications)

### 6. Test It! (3 minutes)
   - Try the slicers
   - Verify numbers match expectations
   - Check that visuals update

---

## 📊 Key Metrics You Have

- **1,899 total publications** (2010-2020)
- **397 sustainable publications** (20.9%)
- **15 SDGs covered**
- **Top SDG**: SDG 3 (Good Health) - 120 publications
- **Top Department**: Business Administration - 244 sustainable publications

---

## 🎨 Dashboard Recommendations

### Must-Have Visuals:
1. ✅ KPI cards (Total, Sustainable, %)
2. ✅ Trend line (Publications over time)
3. ✅ Department bar chart
4. ✅ SDG coverage chart
5. ✅ Impact Story card (dynamic)

### Nice-to-Have:
- Matrix heatmap (Department × SDG)
- Network graph (if custom visual available)
- Word cloud (keywords)

---

## 📖 Full Instructions

See **`POWER_BI_BUILD_GUIDE.md`** for complete step-by-step instructions with screenshots guidance.

---

## 💡 Pro Tips

1. **Start Simple**: Build Overview page first, then add complexity
2. **Test Frequently**: Check slicers work as you build
3. **Use Impact Story**: This is your competitive advantage - make it prominent!
4. **Record Demo**: Film a 2-minute walkthrough showing interactivity

---

## 🆘 Need Help?

- Check `POWER_BI_BUILD_GUIDE.md` for troubleshooting
- Verify relationships in Model view
- Ensure measures use correct table names
- Test with simple filters first

---

**You're ready to build! 🎉**

Open Power BI and follow the steps above. The hard part (data cleaning) is done!





