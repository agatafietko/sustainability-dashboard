# How to Format Card to Show Percentage

## 🔍 **Problem**

Your card shows: **0.21** instead of **21%**

This is because Power BI is showing the decimal value. You need to format it as a percentage.

---

## ✅ **Solution: Format as Percentage**

### Step 1: Select the Sustainable % Card

1. **Click on the card** showing "0.21 Sustaina'"
2. It should be highlighted/selected

### Step 2: Open Format Pane

1. Look at the **right side** for **"Format visual"** pane
2. If not visible, click the **paint roller icon** or **"Format"** button

### Step 3: Format as Percentage

**Option A: Using Format Pane (Recommended)**

1. In **Format pane**, scroll down to find **"Values"** or **"Data labels"** section
2. Look for **"Display format"** or **"Format"** dropdown
3. Click the dropdown
4. Select **"Percentage"** or **"%"`
5. You might see options like:
   - **0.00%** (shows 2 decimals: 20.90%)
   - **0%** (shows no decimals: 21%)
   - **0.0%** (shows 1 decimal: 20.9%)
6. Choose the format you want (usually **0.00%** or **0%**)
7. Card should now show **21%** instead of **0.21**

**Option B: Using Field Format**

1. In **Data pane** (right side), find **"Sustainable %"** measure
2. **Right-click** on "Sustainable %"
3. Select **"Format"** or **"Format this field"**
4. Choose **"Percentage"**
5. Set decimal places (0, 1, or 2)
6. Click OK

---

## 📊 **Visual Guide**

**Before Formatting:**
```
┌─────────────────┐
│ Sustainable %   │
│                 │
│     0.21        │  ← Wrong! (decimal)
└─────────────────┘
```

**After Formatting:**
```
┌─────────────────┐
│ Sustainable %   │
│                 │
│     21%         │  ← Correct! (percentage)
└─────────────────┘
```

OR with decimals:
```
┌─────────────────┐
│ Sustainable %   │
│                 │
│    20.90%       │  ← Shows 2 decimals
└─────────────────┘
```

---

## 🎯 **Step-by-Step Checklist**

- [ ] Selected the Sustainable % card
- [ ] Opened Format pane
- [ ] Found "Values" or "Data labels" section
- [ ] Changed "Display format" to "Percentage"
- [ ] Selected decimal places (0, 1, or 2)
- [ ] Card now shows 21% or 20.90% (not 0.21)

---

## 💡 **Pro Tips**

1. **Choose Decimal Places**: 
   - **0%** = Clean look (21%)
   - **0.00%** = More precise (20.90%)
   - **0.0%** = Middle ground (20.9%)

2. **Consistent Formatting**: Format all percentage cards the same way

3. **Check Your Measure**: Make sure your "Sustainable %" measure uses DIVIDE:
   ```DAX
   Sustainable % = 
   DIVIDE(
       [Sustainable Publications],
       [Total Publications],
       0
   )
   ```
   This returns a decimal (0.21), which you format as percentage (21%)

---

## 🔧 **Alternative: Format in the Measure**

You can also format it directly in the DAX measure:

```DAX
Sustainable % = 
FORMAT(
    DIVIDE(
        [Sustainable Publications],
        [Total Publications],
        0
    ),
    "0.00%"
)
```

But formatting in the visual is usually easier!

---

## ✅ **Quick Reference**

**Format Options:**
- **0%** = 21%
- **0.0%** = 20.9%
- **0.00%** = 20.90%

**Where to Find:**
- Format pane → Values section → Display format → Percentage

---

**After formatting, your card should show 21% or 20.90% instead of 0.21!** 🎉

If you can't find the format option, tell me what you see in the Format pane and I'll help you locate it!





