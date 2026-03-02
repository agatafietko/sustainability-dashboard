# The Illinois Sustainability Impact Engine

> **A decision-support platform for discovering sustainability research expertise and facilitating interdisciplinary collaboration across university departments.**

---

## 🎯 Quick Overview

The **Illinois Sustainability Impact Engine** is a comprehensive platform that transforms fragmented sustainability research into actionable insights. It enables researchers, faculty, and leadership to discover expertise, identify collaboration opportunities, and make data-driven decisions aligned with the UN Sustainable Development Goals (SDGs).

### ✨ What Makes This Different

- **🔍 Discovery**: Instantly identify sustainability research expertise across all 17 UN SDGs
- **🤝 Smart Matching**: Collaboration recommendations based on complementary methods, not just similarity
- **📊 Strategic Insights**: Visualize research coverage, gaps, and trends to inform funding decisions
- **🎯 Actionable**: Move from passive reporting to proactive collaboration facilitation

---

## 📋 Table of Contents

- [Problem Statement](#-problem-statement)
- [Solution Architecture](#-solution-architecture)
- [Platform Components](#-platform-components)
- [Collaboration Hub](#collaboration-hub) 
- [Getting Started](#-getting-started)
- [Technical Implementation](#-technical-implementation)
- [Data & Methodology](#-data--methodology)
- [Repository Structure](#-repository-structure)
- [Documentation](#-documentation)

---

## ❌ Problem Statement

Universities generate extensive sustainability-related research, but this work is often fragmented across departments, disciplines, and individuals, leading to:

| Challenge | Impact |
|-----------|--------|
| ❌ Limited visibility into existing sustainability expertise | Missed collaboration opportunities |
| ❌ Difficulty identifying collaborators with complementary skills | Reduced innovation potential |
| ❌ Lack of structured insights into SDG coverage | Inefficient resource allocation |
| ❌ Manual, time-intensive processes for finding partners | Slowed research formation |

**Result**: Opportunities for interdisciplinary collaboration and strategic sustainability initiatives are frequently missed.

---

## 🏗️ Solution Architecture

The platform consists of **5 integrated components** working together to address the fragmentation problem:

```
┌─────────────────────────────────────────────────────────────┐
│         Illinois Sustainability Impact Engine                │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Sustainability│  │   Research   │  │ Collaboration│     │
│  │   Dashboard   │  │   Coverage   │  │     Hub      │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                               │
│  ┌──────────────┐  ┌──────────────┐                         │
│  │   Impact     │  │      AI      │                         │
│  │   Engine     │  │   Prototype  │                         │
│  └──────────────┘  └──────────────┘                         │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## 🧩 Platform Components

### 1. Sustainability Dashboard
**Purpose**: High-level visualization of research activity across all 17 UN SDGs

- Overview of sustainability research coverage and trends
- Quick identification of research strengths and gaps
- Strategic planning support for leadership

**Status**: Integrated in Power BI platform

---

### 2. Research Coverage Analysis
**Purpose**: Detailed analysis of research distribution, gaps, and trends

- Identifies areas of strength and opportunities for growth
- Department-level SDG coverage analysis
- Trend visualization over time

**Status**: Integrated in Power BI platform

---

### 3. Collaboration Hub

**Compatibility scoring tool** that recommends collaborators based on:
- **Topic alignment** (NLP semantic similarity) - 45% weight
- **Method complementarity** (different methods score higher) - 40% weight
- **Career stage fit** (mentorship + peer collaboration) - 15% weight

#### Key Innovation
**Rewards complementary methods** (e.g., Theoretical + Empirical) rather than just similarity. This drives innovation by bringing together different perspectives.

#### Scoring Formula
```
CCS_Total = (Topic × 45%) + (Method × 40%) + (Career × 15%)
```

#### Features
- ✅ Transparent, rule-based scoring (not predictive AI)
- ✅ Explainable recommendations with natural language explanations
- ✅ Streamlit web app with interactive matching
- ✅ Complete methodology documentation

#### Positioning
**Supplementary tool**: The Collaboration Hub is a "nice-to-have" enhancement that adds compatibility scoring to help researchers find collaborators. The Sustainability Dashboard, Research Coverage Analysis, and Impact Engine work independently—the platform functions without the Hub, but it adds value when researchers want to find collaborators.

#### 📚 Complete Documentation
**See `components/collab_hub/README.md`** for:
- **Streamlit app** - Interactive web application
- **Methodology** - NLP formula and CCS scoring
- **Deployment guide** - Streamlit Cloud setup
- **Judge Q&A** - Answers to common questions

---

### 4. Impact Engine
**Purpose**: Research impact metrics and sustainability outcomes visualization

- Quantifies research impact beyond publication count
- Impact score calculation (journal tier, SDG alignment, recency)
- Researcher and department impact comparisons

**Status**: Integrated in Power BI platform

---

### 5. AI Prototype
**Purpose**: Natural language query interface for sustainability research

- Google AI Studio integration
- Ask questions about sustainability research in plain language
- Interactive exploration of research landscape

**Status**: Prototype available

---

## 🚀 Getting Started

### For Judges & Reviewers

1. **Start Here**: Read this README for platform overview
2. **Collaboration Hub**: See `components/collab_hub/README.md` for detailed documentation
3. **Methodology**: Review `components/collab_hub/docs/methodology.md` for step-by-step explanation
4. **Judge Q&A**: Check `components/collab_hub/docs/judge_qa.md` for common questions

### For Developers

1. **Clone the repository**
   ```bash
   git clone https://github.com/meryemrafiq14-hue/sustainability_case_competition.git
   cd sustainability_case_competition
   ```

2. **Run Streamlit App**
   ```bash
   cd components/collab_hub
   pip install -r requirements.txt
   streamlit run app.py
   ```
   - Opens at `http://localhost:8501`
   - Choose your path: Faculty, Student, or Donor

---

## 💻 Technical Implementation

### Technology Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Streamlit app development |
| **Streamlit** | Web application framework |
| **NLP (sentence-transformers)** | Semantic similarity analysis |
| **Pandas/NumPy** | Data manipulation and analysis |

### Collaboration Hub Pipeline

```
Publications CSV (publications.csv)
    ↓
Streamlit App (app.py)
    ├── Load original CSV
    ├── Build researcher profiles on-the-fly
    ├── Perform NLP semantic analysis
    └── Calculate compatibility scores in real-time
    ↓
Interactive Web Interface
    ├── Faculty Path: CCS matching
    ├── Student Path: Opportunity matching
    └── Donor Path: SDG coverage analysis
```

**See `components/collab_hub/README.md`** for detailed documentation.

---

## 📊 Data & Methodology

### Data Source

- **Input**: Publications CSV (`publications.csv`)
- **No external scraping**: All data comes from the provided dataset
- **Fields used**: Author names, departments, publication years, keywords, abstracts, SDG labels

### Data Policy

**We do not publish raw publication data** in this repository. See `DATA_POLICY.md` for details.

| Included | Excluded |
|----------|----------|
| ✅ Documentation of data fields and processing | ❌ Raw publication data (CSV/XLSX) |
| ✅ Methodology and scoring logic | ❌ Power BI `.pbix` files |
| ✅ Streamlit app code | ❌ Large data files |

### Methodology Transparency

- **Rule-based system**: Not predictive AI - every score is explainable
- **Transparent scoring**: Complete methodology documented
- **Real data only**: All matching uses actual publication data
- **NLP semantic analysis**: Uses sentence-transformers on actual keywords and abstracts

---

## 💡 Impact & Insights

### Key Findings

| Finding | Impact |
|--------|--------|
| ✅ Certain SDGs receive significantly more research attention | Identifies funding gaps and opportunities |
| ✅ Collaboration opportunities exist across departments | Enables cross-disciplinary innovation |
| ✅ Early-career researchers benefit from structured discovery | Supports mentorship and career development |
| ✅ Data-driven insights support strategic funding decisions | Improves resource allocation |

### Measurable Impact

- **Visibility**: Improves visibility of sustainability expertise across the institution
- **Efficiency**: Reduces friction in forming interdisciplinary research teams
- **Strategy**: Supports data-driven decision making for leadership and donors
- **Culture**: Moves from passive information access to proactive insight generation

---

## 📁 Repository Structure

```
sustainability_case_competition/
├── README.md                          # This file (platform overview)
├── DATA_POLICY.md                     # Data confidentiality policy
├── publications.csv                   # Original data file
│
└── components/
    └── collab_hub/                   # Collaboration Hub
        ├── README.md                 # Component overview
        ├── app.py                     # Main Streamlit application
        ├── requirements.txt           # Python dependencies
        ├── DEPLOYMENT_GUIDE.md        # Streamlit Cloud deployment
        └── docs/                      # Documentation
            ├── methodology.md        # Complete methodology (NLP, CCS)
            ├── UNDER_THE_HOOD.md     # Technical deep dive
            ├── judge_qa.md           # Answers to judge questions
            ├── limitations.md        # Known limitations
            └── QUICK_START_FOR_JUDGES.md
```

---

## 📚 Documentation

### Collaboration Hub Documentation

**Documentation available in `components/collab_hub/`**:

| Document | Description |
|----------|-------------|
| `README.md` | Component overview and quick start |
| `docs/methodology.md` | Complete step-by-step methodology |
| `docs/UNDER_THE_HOOD.md` | Technical deep dive: How the Streamlit app works |
| `docs/judge_qa.md` | Answers to common judge questions |
| `docs/limitations.md` | Known limitations and future work |
| `docs/QUICK_START_FOR_JUDGES.md` | Quick overview for judges |
| `DEPLOYMENT_GUIDE.md` | Streamlit Cloud deployment guide |

---

## 🎓 Skills Demonstrated

### Technical Skills

- **Web Development**: Streamlit application development
- **NLP**: Semantic similarity analysis using sentence-transformers
- **Data Analysis**: Statistical analysis and pattern recognition
- **Algorithm Design**: Multi-factor scoring system development
- **Python Programming**: Data processing and application development

### Business & Analytical Skills

- **Problem Structuring**: Business analytics lens for complex problems
- **Stakeholder Analysis**: Multi-user persona design
- **Decision Modeling**: Quantitative scoring framework development
- **Sustainability Analytics**: UN SDG mapping and analysis
- **Strategic Thinking**: Institutional impact assessment

---

## 🔮 Future Work

### Planned Enhancements

1. **Data Integration**
   - Live publication and grant databases
   - Real-time data updates
   - Expanded data sources (conferences, patents, etc.)

2. **Advanced Analytics**
   - Domain-specific NLP models
   - Network analysis for research communities
   - Predictive analytics for collaboration success

3. **Platform Features**
   - User profiles and preferences
   - Notification system for new matches
   - Integration between all 5 components

4. **Expansion**
   - Beyond sustainability to other research domains
   - Multi-institutional collaboration
   - Industry partnership matching

---

## ⚖️ Disclaimer

This project is an academic case competition submission.  
No proprietary or confidential data was used.  
All data processing and analysis was performed on publicly available or anonymized university publication metadata.

---

## 📧 Contact & Links

- 📧 **Questions**: Reach out through GitHub Issues
- 🌐 **Streamlit App**: Deployed on Streamlit Cloud (see `components/collab_hub/DEPLOYMENT_GUIDE.md`)

---

<div align="center">

**Built with** ❤️ **for sustainable research collaboration**

_Illinois Sustainability Impact Engine - Case Competition 2025_

</div>
