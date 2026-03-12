# Collaboration Hub

> **Component of the Illinois Sustainability Impact Engine**

The Collaboration Hub is one of 5 integrated components in the Sustainability Impact Engine. It is a compatibility scoring tool that recommends research collaborators based on topic alignment, method complementarity, and career stage fit. It enhances the platform by adding a compatibility layer, working alongside the Sustainability Dashboard, Research Coverage Analysis, Impact Engine, and AI Prototype.

## 🎯 Quick Overview

**What it does**: A Streamlit web application that analyzes original publication data using NLP to recommend research collaborators, opportunities, and funding priorities.

**Key innovation**: 
- Uses **NLP semantic analysis** on actual keywords and abstracts from original CSV
- Rewards **complementary methods** (e.g., Theoretical + Empirical) rather than just similarity
- Three stakeholder paths: Faculty (CCS matching), Students (opportunities), Donors (funding gaps)

**Output**: 
- **Streamlit Web App**: Interactive matching with transparent scoring

**Data Source**: Uses original `publications.csv` - builds profiles on-the-fly, no pre-processed data

**Part of**: The Illinois Sustainability Impact Engine (along with Sustainability Dashboard, Research Coverage Analysis, Impact Engine, and AI Prototype)

---

## 📁 Repository Structure

```
components/collab_hub/
├── README.md                    # This file
├── app.py                       # Main Streamlit application
├── requirements.txt             # Python dependencies
└── docs/                        # Documentation
    └── UNDER_THE_HOOD.md       # Complete technical documentation (NLP, CCS formula, judge Q&A)

publications.csv                 # Data file (in repository root)
```

---

## 🚀 Quick Start

### Run Streamlit App (Recommended)

1. **Install dependencies**:
   ```bash
   cd components/collab_hub
   pip install -r requirements.txt
   ```

2. **Run the app**:
   ```bash
   streamlit run app.py
   ```

3. **Access the app**:
   - Opens automatically at `http://localhost:8501`
   - Choose your path: Faculty, Student, or Donor

### Deploy to Streamlit Cloud

1. **Repository**: `https://github.com/meryemrafiq14-hue/sustainability_case_competition.git`
2. **Main file path**: `components/collab_hub/app.py`
3. Ensure `publications.csv` is in the repository root directory

---

## 📊 How It Works

### Data Source
- **Original CSV**: `publications.csv` (in repository root)
- **Profile Construction**: Built on-the-fly from original publication records
- **NLP Analysis**: Uses actual keywords and abstracts from original CSV
- **No Pre-processing**: All analysis performed on original data

### Three Stakeholder Paths

#### 1. Faculty Path - Find a Collaborator
- **CCS Formula**: `(Topic × 45%) + (Method × 40%) + (Career × 15%)`
- **Topic Score (45%)**: NLP semantic similarity on actual keywords/abstracts
- **Method Score (40%)**: Rewards complementarity (Theoretical + Empirical = 100)
- **Career Score (15%)**: Mentorship opportunities (Pre-Tenure + Senior = 100)
- **Output**: Top match with transparent breakdown

#### 2. Student Path - Find Opportunities
- **Opportunity Match Score**: Based on SDG interest, skills, and career fit
- **Output**: Ranked research opportunities

#### 3. Donor Path - Sponsor a Priority
- **SDG Coverage Analysis**: Interactive chart showing research coverage
- **Gap Identification**: Highlights under-researched SDGs
- **Output**: Priority funding areas

---

## 📖 Documentation

### Complete Technical Documentation
- **`docs/UNDER_THE_HOOD.md`** ⭐ - Complete technical documentation including:
  - NLP methodology and CCS scoring formula
  - Weight justification (45/40/15)
  - Data sources and processing
  - Technical implementation details
  - Judge Q&A and frequently asked questions
  - Limitations and future work

### Code
- **`app.py`** - Main Streamlit application (fully commented)

---

## ⚠️ Important Notes

### Data Source

- **Streamlit App**: Uses original `publications.csv`
- **Profile Construction**: Built on-the-fly from original publication records
- **NLP Analysis**: Performed on actual keywords and abstracts from original CSV
- **No Pre-processing**: All analysis uses original data directly
- **No Simulation**: All matching uses real data from the original CSV

### Data Confidentiality

- Original CSV file (`publications.csv`) is included in the repository for Streamlit Cloud deployment

### Transparency

This is a **rule-based system with NLP**, not predictive AI. Every score is explainable and transparent. The NLP component uses semantic similarity on actual research content from the original CSV.

---

## 🎓 For Judges

**Key points to understand**:

1. **Not AI prediction**: This is a transparent heuristic, not a machine learning model
2. **Complementarity focus**: The innovation is rewarding different methods, not similarity
3. **Explainable**: Every match has a clear explanation
4. **Real data only**: The app uses only real data from the original publications CSV
5. **Part of larger platform**: This is one of 5 components in the Sustainability Impact Engine

See `docs/UNDER_THE_HOOD.md` for detailed answers to common questions and complete technical documentation.

---

## 🔗 Related Components

The Collaboration Hub integrates with other platform components:

- **Sustainability Dashboard**: Provides SDG context for matches
- **Research Coverage Analysis**: Identifies collaboration opportunities in under-researched areas
- **Impact Engine**: Measures impact of collaborations
- **AI Prototype**: Natural language interface for finding collaborators

This component is part of the Illinois Sustainability Impact Engine platform.

---

## 📧 Contact

For questions about the Collaboration Hub methodology, see `docs/UNDER_THE_HOOD.md` for complete technical documentation.

---

**Built for the Illinois Sustainability Impact Engine Case Competition**
