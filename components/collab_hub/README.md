# Collaboration Hub

> **Component of the Illinois Sustainability Impact Engine**

The Collaboration Hub is one of 5 integrated components in the Sustainability Impact Engine. It is a compatibility scoring tool that recommends research collaborators based on topic alignment, method complementarity, and career stage fit. It enhances the platform by adding a compatibility layer, working alongside the Sustainability Dashboard, Research Coverage Analysis, Impact Engine, and AI Prototype.

## 🎯 Quick Overview

**What it does**: Converts publication metadata into researcher profiles, then scores pairwise compatibility to recommend collaboration opportunities.

**Key innovation**: Rewards **complementary methods** (e.g., Theoretical + Empirical) rather than just similarity.

**Output**: Power BI dashboard showing ranked matches with transparent explanations.

**Positioning**: **Supplementary tool** - A "nice-to-have" enhancement that adds compatibility scoring. The Sustainability Dashboard, Research Coverage Analysis, and Impact Engine work independently—the platform functions without the Hub, but it adds value when researchers want to find collaborators.

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

### For Demo Dashboard (What Judges See)

1. **Generate demo data**:
   ```bash
   cd components/collab_hub/scripts
   python generate_ccs_demo_data.py
   ```
   This creates `CCS_Demo_Data.csv` in the parent directory.

2. **Load into Power BI**:
   - Open Power BI Desktop
   - Get Data → Text/CSV
   - Select `CCS_Demo_Data.csv`
   - Build visuals (see `powerbi/README.md`)

### For Full Pipeline (Optional)

1. **Build researcher profiles and matches**:
   ```bash
   cd components/collab_hub/scripts
   python build_collab_hub_from_scratch.py
   ```
   This requires the original publications CSV.

2. **Load into Power BI**:
   - Import `Collab_Matches_For_PowerBI.csv`
   - Import `Researcher_Profiles_For_PowerBI.csv`
   - Create relationships (see `powerbi/README.md`)

---

## 📊 How It Works

### Step 1: Researcher Profile Construction

From the publications CSV, we aggregate:
- **Publication metrics**: Total count, sustainable count, years active
- **Career stage**: Inferred from first publication year
- **Top keywords**: Most frequent keywords across publications
- **Primary SDG**: Most common SDG label
- **Primary method**: Inferred from keywords/abstracts (Theoretical, Empirical, etc.)

### Step 2: Compatibility Scoring

Each researcher pair gets a score:

```
CCS_Total = (Topic × 50%) + (Method × 35%) + (Career × 15%)
```

**Topic Score (50%)**:
- SDG alignment (70% of topic score)
- Keyword overlap (30% of topic score)

**Method Score (35%)**:
- **Rewards complementary methods**: Theoretical + Empirical = 100
- **Penalizes same methods**: Theoretical + Theoretical = 25

**Career Score (15%)**:
- Mentorship pairs (Pre-Tenure + Senior) = 100
- Peer collaboration (same stage) = 60-75

### Step 3: Explainability

Every match includes:
- Total score and sub-scores
- Natural language explanation
- Method complementarity indicator

---

## 📖 Documentation

- **`docs/END_TO_END_PIPELINE.md`** - Complete data journey from original CSV to Power BI
- **`docs/VALUE_PROPOSITION_AND_POSITIONING.md`** - Value proposition and positioning
- **`docs/QUICK_START_FOR_JUDGES.md`** - Quick overview for judges
- **`docs/methodology.md`** - Step-by-step methodology
- **`docs/BUSINESS_LOGIC_AND_DECISIONS.md`** - Business rationale for weights and decisions
- **`docs/DATA_TRANSFORMATION_GUIDE.md`** - Data transformation from CSV to matches
- **`docs/limitations.md`** - Known limitations and future work
- **`docs/judge_qa.md`** - Answers to common judge questions

### Technical Documentation
- **`scripts/README.md`** - Script documentation and usage
- **`scripts/SCRIPT_LOGIC_EXPLANATION.md`** - Detailed code logic and design decisions

---

## ⚠️ Important Notes

### Demo Data vs. Real Data

- **Demo dashboard** uses `CCS_Demo_Data.csv` (synthetic, for presentation)
- **Full pipeline** uses `Collab_Matches_For_PowerBI.csv` (from real publications)

The demo data includes small randomized variation to show diverse examples clearly. It's a **proof of concept**, not a predictive model.

### Data Confidentiality

- Raw publication data is **not** included in this repo
- Only derived outputs and documentation are shared
- See `data/README.md` for data policy

### Transparency

This is a **rule-based system**, not predictive AI. Every score is explainable and transparent.

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
