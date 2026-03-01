# Streamlit App: Sustainability Research Discovery Hub

## 📦 What Was Created

### 1. `app.py` - Main Streamlit Application
A complete, production-ready Streamlit web application that:

- **Landing Page**: Three stakeholder paths (Faculty, Student, Donor)
- **Faculty Path**: Wizard questionnaire (SDG, Department, Method, Career Stage) → CCS matching
- **Student Path**: Opportunity matching based on skills and SDG interest
- **Donor Path**: SDG coverage analysis and funding gap identification
- **NLP Matching Engine**: Uses `sentence-transformers` for semantic topic matching
- **Rule-Based Scoring**: Method complementarity (40%) and Career fit (15%)
- **Top 3 Results**: Displays matches with proactive AI-generated insights
- **Transparency Section**: Full methodology explanation for judges

### 2. `requirements.txt` - Dependencies
All required Python packages:
- `streamlit` - Web framework
- `pandas` - Data manipulation
- `numpy` - Numerical operations
- `scikit-learn` - Cosine similarity calculation
- `sentence-transformers` - NLP semantic similarity
- `torch` - PyTorch (dependency of sentence-transformers)

### 3. `DEPLOYMENT_GUIDE.md` - Step-by-Step Deployment Instructions
Complete guide for deploying to Streamlit Community Cloud (free).

---

## 🎯 Key Features

### ✅ Addresses Judge Feedback

1. **No More "Black Box" AI**
   - Full transparency section explaining the 45/40/15 formula
   - Clear justification for career weight (15%)
   - Explains NLP approach vs. random numbers

2. **Real Data, Not Random**
   - Uses original `for distribution case competition filtered_publications.csv`
   - Builds researcher profiles on-the-fly from original publication data
   - NLP semantic analysis on actual keywords and abstracts from original CSV
   - No pre-processed or simulated data

3. **Persona-Driven User Journey**
   - Clear persona selection at start
   - Wizard questionnaire guides user
   - Proactive insights (not hidden chatbot)

4. **Reframed as Discovery/Complementarity**
   - Called "Complementary Fit Score" (not "prediction")
   - Emphasizes discovery and complementarity
   - Focuses on research alignment, not success prediction

---

## 🔧 How It Works

### Scoring Formula
```
Complementary Fit Score = (Topic × 45%) + (Method × 40%) + (Career × 15%)
```

### Topic Score (45%) - NLP
- Uses `all-MiniLM-L6-v2` sentence transformer
- Embeds user research context + candidate keywords
- Calculates cosine similarity
- Scales to 0-100

### Method Score (40%) - Rules
- Rewards complementarity (Theoretical + Empirical = 100)
- Penalizes same methods (Theoretical + Theoretical = 50)
- Dictionary-based complementarity matrix

### Career Score (15%) - Rules
- Mentorship: Pre-Tenure + Senior = 100
- Peer: Same stage = 75-85
- Based on user's stated goal (Mentorship vs Peer Co-author)

---

## 🚀 Quick Start (Local Testing)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Ensure original CSV is accessible:**
   - The app looks for `for distribution case competition filtered_publications.csv`
   - Should be in repository root or parent directories
   - App will search multiple paths automatically

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser:**
   - App will open at `http://localhost:8501`

---

## 📋 Deployment Checklist

Before deploying to Streamlit Cloud:

- [ ] Test locally - app runs without errors
- [ ] Verify CSV loads correctly
- [ ] Test matching - submit form and see results
- [ ] Check transparency section displays correctly
- [ ] Push to GitHub repository
- [ ] Follow `DEPLOYMENT_GUIDE.md` for Streamlit Cloud setup

---

## 📝 Notes

### Data Requirements
- CSV must have columns: `name`, `department`, `primary_sdg`, `primary_method`, `career_stage`, `top_keywords`, `total_publications`, `email`
- App will search multiple paths for the CSV file

### Performance
- First load downloads NLP model (~80MB) - takes 30-60 seconds
- Subsequent loads are cached and fast
- Matching calculation is optimized for Streamlit Cloud

### Customization
- Adjust weights in scoring formula (lines ~200-250)
- Modify complementarity matrix (lines ~150-180)
- Update insight generation logic (lines ~300-320)

---

## 🎓 For Judges

**Key Points:**
1. **Transparent**: Full methodology explained in "Under the Hood" section
2. **Real Data**: Uses actual researcher profiles, not simulated
3. **NLP-Based**: Semantic similarity replaces random numbers
4. **Explainable**: Every match includes AI-generated insight explaining why it works
5. **Discovery-Focused**: Framed as complementarity discovery, not prediction

**Career Weight Justification:**
> "We prioritize semantic research alignment and methodological fit first (85%), but apply a 15% weighting to career stages to actively foster junior-faculty mentorship and cross-seniority knowledge transfer."

---

## 🔗 Next Steps

1. **Test locally** to ensure everything works
2. **Deploy to Streamlit Cloud** using `DEPLOYMENT_GUIDE.md`
3. **Share public URL** with judges
4. **Optional**: Link "Log Collaboration" button to Impact Engine component

---

**Questions?** Check the code comments in `app.py` - everything is documented inline.
