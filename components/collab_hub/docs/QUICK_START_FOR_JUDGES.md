# Quick Start Guide for Judges

> **Everything you need to understand the Collaboration Hub in 5 minutes**

---

## 🎯 **What Is This?**

The **Collaboration Hub** is a supplementary compatibility scoring tool that helps researchers find potential collaborators. It's part of the Illinois Sustainability Impact Engine, a 5-component platform for sustainability research.

**Key Point**: It's a "nice-to-have" enhancement, not a core dependency. The Sustainability Dashboard, Research Coverage Analysis, and Impact Engine work independently.

---

## 📊 **End-to-End Process**

### **Step 1: Original Data**
- **Input**: University publications CSV (`for distribution case competition filtered_publications.csv`)
- **Contains**: Real publication metadata (names, departments, keywords, abstracts, SDGs, publication years)

### **Step 2: Streamlit App - Real-Time Analysis**
- **App**: `app.py` (Streamlit web application)
- **Does**: 
  - Loads original CSV directly
  - Builds researcher profiles on-the-fly from original data
  - Performs NLP semantic analysis on actual keywords and abstracts
  - Calculates compatibility scores in real-time
- **Output**: Interactive web interface with three stakeholder paths
- **Data**: 100% real (no simulation, no pre-processing)

### **Step 3: Three Stakeholder Paths**
- **Faculty**: CCS matching with transparent breakdown
- **Students**: Opportunity matching based on skills
- **Donors**: SDG coverage and funding gap analysis

---

## ✅ **Data Source**

### **100% Real** (From Original CSV)
- ✅ All researcher names
- ✅ All departments
- ✅ All publication counts and years
- ✅ All keywords and abstracts (used for NLP)
- ✅ All SDGs from original CSV

### **Calculated** (Based on Real Data)
- 🧮 Career stage (from years since first publication in original CSV)
- 🧮 Primary SDG (most frequent from original CSV)
- 🧮 Primary method (inferred from actual keywords/abstracts in original CSV)
- 🧮 Compatibility scores (algorithm: 45% topic, 40% method, 15% career)
- 🧮 NLP semantic similarity (on actual keywords and abstracts)

### **No Simulation**
- ✅ All data comes from original CSV
- ✅ Profiles built on-the-fly from original publications
- ✅ NLP performed on actual research content
- ✅ All data comes from original publications CSV
- ✅ No pre-processed or simulated data

---

## 🔗 **How It Fits with Other Components**

### **Core Components** (Work Independently)
1. **Sustainability Dashboard** - SDG wheel visualization, coverage overview
2. **Research Coverage Analysis** - Gap identification, department-level analysis
3. **Impact Engine** - Impact scores and outcomes

### **Supplementary Components**
4. **Collaboration Hub** ⭐ - Compatibility scoring (this component)
5. **AI Prototype** - Natural language queries

**Integration**: Collaboration Hub enhances discovery tools by adding compatibility scores. For example:
- Researcher discovers SDG coverage in Dashboard → Uses Hub to find collaborators
- Researcher identifies gap in Coverage Analysis → Uses Hub to find researchers who can fill it

**Key Point**: The platform works without Collaboration Hub, but it adds value when researchers want to find collaborators.

---

## 💡 **Value Proposition**

### **For Researchers**
- Save time finding collaborators
- Discover opportunities across departments
- Understand why matches are recommended (transparent scoring)

### **For University Leadership**
- Accelerate research formation
- Identify collaboration opportunities
- Strategic planning with data-driven insights

### **For the Platform**
- Enhances discovery tools
- Adds compatibility scoring layer
- Complements (doesn't replace) existing networking

---

## 🎤 **Elevator Pitch**

> "The Collaboration Hub is a supplementary tool that adds a compatibility scoring layer to help researchers find potential collaborators. It's not a core dependency—the Sustainability Dashboard and Research Coverage Analysis work independently. But when researchers want to find collaborators, the Hub provides transparent, explainable scores based on topic alignment, method complementarity, and career stage fit. It's a 'nice-to-have' enhancement that saves time and accelerates research formation."

---

## 📚 **Where to Learn More**

1. **`END_TO_END_PIPELINE.md`** - Complete data journey, what each script does
2. **`VALUE_PROPOSITION_AND_POSITIONING.md`** - How to sell the idea, positioning
3. **`methodology.md`** - Step-by-step methodology
4. **`judge_qa.md`** - Answers to common questions

---

## ✅ **Key Takeaways**

1. **Supplementary Tool**: Enhances but doesn't block other components
2. **Real Data**: Uses actual university publication data
3. **Transparent**: Rule-based scoring, not predictive AI
4. **Innovation**: Rewards complementary methods, not just similarity
5. **Actionable**: Provides ranked suggestions with explanations

---

**Questions?** See `judge_qa.md` for detailed answers.
