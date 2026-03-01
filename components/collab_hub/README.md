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
- **Power BI Dashboard**: Alternative visualization (optional)

**Data Source**: Uses original `for distribution case competition filtered_publications.csv` - builds profiles on-the-fly, no pre-processed data

**Part of**: The Illinois Sustainability Impact Engine (along with Sustainability Dashboard, Research Coverage Analysis, Impact Engine, and AI Prototype)

---

## 📁 Repository Structure

```
components/collab_hub/
├── README.md                    # This file
├── scripts/                     # Python scripts
│   ├── README.md               # Script documentation
│   ├── build_collab_hub_from_scratch.py
│   └── generate_ccs_demo_data.py
├── docs/                        # Methodology & submission docs
│   ├── methodology.md          # Complete methodology
│   ├── limitations.md          # Known limitations
│   ├── judge_qa.md            # Answers to judge questions
│   ├── cover_letter_template.md
│   └── slides_outline.md
├── powerbi/                     # Power BI setup
│   └── README.md
├── data/                        # Data policy
│   └── README.md
└── outputs/                     # Output descriptions
    └── README.md
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
3. See `DEPLOYMENT_GUIDE.md` for detailed instructions

### Power BI Dashboard (Optional)

For Power BI visualization, see `powerbi/README.md`

---

## 📊 How It Works

### Data Source
- **Original CSV**: `for distribution case competition filtered_publications.csv`
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

### Essential Reading
- **`STREAMLIT_DEPLOYMENT.md`** ⭐ - Quick deployment guide with GitHub repo link
- **`DEPLOYMENT_GUIDE.md`** - Detailed Streamlit Cloud deployment instructions
- **`docs/END_TO_END_PIPELINE.md`** - Complete data journey from original CSV to Streamlit app
- **`docs/QUICK_START_FOR_JUDGES.md`** - Quick overview for judges

### Detailed Documentation
- **`docs/methodology.md`** - Step-by-step methodology
- **`docs/BUSINESS_LOGIC_AND_DECISIONS.md`** - Business rationale for weights and decisions
- **`docs/judge_qa.md`** - Answers to common judge questions
- **`docs/limitations.md`** - Known limitations and future work

### Technical Documentation
- **`scripts/README.md`** - Script documentation (for batch processing, optional)
- **`app.py`** - Main Streamlit application (commented code)

---

## ⚠️ Important Notes

### Data Source

- **Streamlit App**: Uses original `for distribution case competition filtered_publications.csv`
- **Profile Construction**: Built on-the-fly from original publication records
- **NLP Analysis**: Performed on actual keywords and abstracts from original CSV
- **No Pre-processing**: All analysis uses original data directly
- **No Simulation**: All matching uses real data from original CSV

### Data Confidentiality

- Original CSV file is **not** included in this public repo
- App expects CSV to be in repository root or accessible path
- See `DATA_POLICY.md` in root directory for data policy

### Transparency

This is a **rule-based system with NLP**, not predictive AI. Every score is explainable and transparent. The NLP component uses semantic similarity on actual research content from the original CSV.

---

## 🎓 For Judges

**Key points to understand**:

1. **Not AI prediction**: This is a transparent heuristic, not a machine learning model
2. **Complementarity focus**: The innovation is rewarding different methods, not similarity
3. **Explainable**: Every match has a clear explanation
4. **Demo layer**: The dashboard uses demo data for clarity; the methodology works on real data
5. **Part of larger platform**: This is one of 5 components in the Sustainability Impact Engine

See `docs/judge_qa.md` for detailed answers to common questions.

---

## 🔗 Related Components

The Collaboration Hub integrates with other platform components:

- **Sustainability Dashboard**: Provides SDG context for matches
- **Research Coverage Analysis**: Identifies collaboration opportunities in under-researched areas
- **Impact Engine**: Measures impact of collaborations
- **AI Prototype**: Natural language interface for finding collaborators

See the main repository `README.md` for the complete platform overview.

---

## 📧 Contact

For questions about the Collaboration Hub methodology, see the documentation in `docs/` or refer to the main case competition repository README.

---

**Built for the Illinois Sustainability Impact Engine Case Competition**
