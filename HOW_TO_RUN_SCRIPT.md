# How to Run the Collaboration Hub Script
## Step-by-Step Instructions

---

## 🖥️ **OPTION 1: Using Terminal (Mac)**

### **Step 1: Open Terminal**

1. Press `Cmd + Space` (opens Spotlight)
2. Type "Terminal"
3. Press Enter

OR

1. Open Finder
2. Go to Applications → Utilities
3. Double-click "Terminal"

---

### **Step 2: Navigate to Your Folder**

In Terminal, type this command (then press Enter):

```bash
cd "/Users/meryem/Documents/Case Competition"
```

**What this does:** Changes directory to your project folder

**Verify you're in the right place:**
```bash
ls
```

You should see files like:
- `build_collab_hub_from_scratch.py`
- `for distribution case competition filtered_publications.csv`
- etc.

---

### **Step 3: Check if Python is Installed**

Type this command:
```bash
python3 --version
```

**If you see a version number** (like `Python 3.9.7`): ✅ Python is installed!

**If you see "command not found"**: You need to install Python first (see below)

---

### **Step 4: Install Required Packages (First Time Only)**

If this is your first time running Python scripts, install pandas:

```bash
pip3 install pandas numpy
```

Wait for installation to complete.

---

### **Step 5: Run the Script**

Now run the script:

```bash
python3 build_collab_hub_from_scratch.py
```

**What happens:**
- Script will start running
- You'll see progress messages
- Wait for it to complete (~5-10 minutes)
- You'll see "✓ COLLABORATION HUB MATCHING ALGORITHM COMPLETE!"

---

## 🖥️ **OPTION 2: Using VS Code / Cursor (Easier)**

If you're using VS Code or Cursor (which you are!):

### **Step 1: Open Integrated Terminal**

1. In Cursor/VS Code, press `` Ctrl + ` `` (backtick key, usually above Tab)
   OR
2. Go to **Terminal** → **New Terminal** in the menu

A terminal window will open at the bottom of your editor.

---

### **Step 2: Run the Script**

The terminal should already be in your project folder. Just type:

```bash
python3 build_collab_hub_from_scratch.py
```

Press Enter and wait for it to complete!

---

## 🖥️ **OPTION 3: Using Python IDLE (If You Have It)**

1. Open Python IDLE
2. Go to **File** → **Open**
3. Navigate to your folder and select `build_collab_hub_from_scratch.py`
4. Go to **Run** → **Run Module** (or press F5)

---

## ⚠️ **TROUBLESHOOTING**

### **Problem: "python3: command not found"**

**Solution:** Install Python:
1. Go to https://www.python.org/downloads/
2. Download Python 3.x for Mac
3. Install it
4. Try again

OR use Homebrew:
```bash
brew install python3
```

---

### **Problem: "ModuleNotFoundError: No module named 'pandas'"

**Solution:** Install pandas:
```bash
pip3 install pandas numpy
```

---

### **Problem: "Permission denied"**

**Solution:** Make sure you're in the right directory:
```bash
cd "/Users/meryem/Documents/Case Competition"
ls build_collab_hub_from_scratch.py
```

If the file exists, try:
```bash
python3 build_collab_hub_from_scratch.py
```

---

### **Problem: Script runs but creates no files**

**Solution:** Check for errors in the output. Make sure:
- Your CSV file is named exactly: `for distribution case competition filtered_publications.csv`
- The file is in the same folder as the script
- You have write permissions in the folder

---

## ✅ **VERIFY IT WORKED**

After the script completes, check that these files were created:

```bash
ls -la *.csv
```

You should see:
- `faculty_matches.csv` ✅
- `Collab_Matches_For_PowerBI.csv` ✅
- `Researcher_Profiles_For_PowerBI.csv` ✅
- `network_graph_data.csv` ✅
- `best_faculty_match.csv` ✅

---

## 🎯 **QUICKEST METHOD (Recommended)**

**In Cursor/VS Code:**

1. Press `` Ctrl + ` `` to open terminal
2. Type: `python3 build_collab_hub_from_scratch.py`
3. Press Enter
4. Wait for completion

**That's it!** 🚀

---

## 📝 **WHAT THE OUTPUT LOOKS LIKE**

You'll see something like this:

```
======================================================================
COLLABORATION HUB - Building Matching Algorithm from Publications
======================================================================

1. Loading publications data...
✓ Loaded 2154 publication records
✓ Cleaned data: 2154 valid records

2. Extracting researcher profiles...
✓ Extracted 150 researcher profiles
  - Departments: 12
  - Methods: {'Empirical': 45, 'Theoretical': 30, ...}

3. Calculating compatibility scores...
  Calculating pairwise compatibility...
    Processing researcher 1/100...
    Processing researcher 10/100...
    ...
✓ Calculated 4950 potential matches

4. Creating Power BI-ready outputs...
✓ Saved faculty_matches.csv (4950 matches)
✓ Saved best_faculty_match.csv (top 50 matches)
✓ Saved Researcher_Profiles_For_PowerBI.csv (150 profiles)
✓ Saved network_graph_data.csv (1200 network edges)
✓ Saved Collab_Matches_For_PowerBI.csv

5. Summary Statistics:
  - Total researchers: 150
  - Total matches calculated: 4950
  - Excellent matches (≥85): 234
  - Good matches (70-84): 567
  ...

======================================================================
✓ COLLABORATION HUB MATCHING ALGORITHM COMPLETE!
======================================================================
```

---

**Once you see the completion message, you're ready for Power BI!** ✅



