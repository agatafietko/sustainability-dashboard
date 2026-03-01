# The Illinois Sustainability Impact Engine

> **An AI-powered decision-support platform for discovering sustainability research expertise and facilitating interdisciplinary collaboration across university departments.**

---

## 🎯 Quick Overview

The **Illinois Sustainability Impact Engine** is a comprehensive platform that transforms fragmented sustainability research into actionable insights. It enables researchers, faculty, and leadership to discover expertise, identify collaboration opportunities, and make data-driven decisions aligned with the UN Sustainable Development Goals (SDGs).

### ✨ What Makes This Different

- **🔍 Discovery**: Instantly identify sustainability research expertise across all 17 UN SDGs
- **🤝 Smart Matching**: AI-powered collaboration recommendations based on complementary methods, not just similarity
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
- [Impact & Insights](#-impact--insights)
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
- **Topic alignment** (SDG + keyword overlap) - 50% weight
- **Method complementarity** (different methods score higher) - 35% weight
- **Career stage fit** (mentorship + peer collaboration) - 15% weight

#### Key Innovation
**Rewards complementary methods** (e.g., Theoretical + Empirical) rather than just similarity. This drives innovation by bringing together different perspectives.

#### Scoring Formula
```
CCS_Total = (Topic × 50%) + (Method × 35%) + (Career × 15%)
```

#### Features
- ✅ Transparent, rule-based scoring (not predictive AI)
- ✅ Explainable recommendations with natural language explanations
- ✅ Power BI dashboard with interactive filtering
- ✅ Complete methodology documentation

#### Positioning
**Supplementary tool**: The Collaboration Hub is a "nice-to-have" enhancement that adds compatibility scoring to help researchers find collaborators. The Sustainability Dashboard, Research Coverage Analysis, and Impact Engine work independently—the platform functions without the Hub, but it adds value when researchers want to find collaborators.

#### 📚 Complete Documentation
**See `components/collab_hub/README.md`** for:
- **End-to-end pipeline** - Complete data journey from CSV to Power BI
- **Value proposition** - How to sell the idea and positioning
- Step-by-step methodology
- Script documentation
- Power BI setup guide
- Judge Q&A answers

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
   git clone [repository-url]
   cd sustainability_case_competition
   ```

2. **Set up environment**
   ```bash
   pip install pandas numpy
   ```

3. **Run Collaboration Hub pipeline** (requires publications CSV)
   ```bash
   cd components/collab_hub/scripts
   python build_collab_hub_from_scratch.py
   ```

4. **Generate demo data**
   ```bash
   python generate_ccs_demo_data.py
   ```

5. **Load into Power BI**
   - Import `CCS_Demo_Data.csv` or `Collab_Matches_For_PowerBI.csv`
   - See `components/collab_hub/powerbi/README.md` for setup

---

## 💻 Technical Implementation

### Technology Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Data processing and transformation |
| **Power BI** | Dashboard visualization (4 integrated components) |
| **Google AI Studio** | Natural language query interface |
| **Pandas/NumPy** | Data manipulation and analysis |

### Data Pipeline

```
Publications CSV
    ↓
Data Processing Scripts
    ↓
Researcher Profiles
    ↓
Component-Specific Processing
    ↓
Power BI Dashboards
```

### Collaboration Hub Pipeline (Detailed)

```
Publications CSV
    ↓
build_collab_hub_from_scratch.py
    ├── Extract researcher profiles
    ├── Infer career stages
    ├── Identify primary methods
    └── Calculate SDG alignment
    ↓
Researcher_Profiles_For_PowerBI.csv
    ↓
generate_ccs_demo_data.py (for demo)
    ├── Select diverse researchers
    ├── Generate matches
    └── Calculate compatibility scores
    ↓
Streamlit App → Interactive matching interface
```

**See `components/collab_hub/scripts/README.md`** for detailed script documentation.

---

## 📊 Data & Methodology

### Data Source

- **Input**: Publications CSV provided by the case competition
- **No external scraping**: All data comes from the provided dataset
- **Fields used**: Author names, departments, publication years, keywords, abstracts, SDG labels

### Data Policy

**We do not publish raw publication data** in this repository. See `DATA_POLICY.md` for details.

| Included | Excluded |
|----------|----------|
| ✅ Documentation of data fields and processing | ❌ Raw publication data (CSV/XLSX) |
| ✅ Methodology and scoring logic | ❌ Power BI `.pbix` files |
| ✅ Scripts that generate outputs | ❌ Large Excel files |

### Methodology Transparency

- **Rule-based system**: Not predictive AI - every score is explainable
- **Transparent scoring**: Complete methodology documented
- **Reproducible**: Scripts available for validation
- **Real data only**: All matching uses actual publication data

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
│
├── components/                        # Platform components
│   ├── collab_hub/                   # Collaboration Hub
│   │   ├── README.md                 # Component overview
│   │   ├── scripts/                   # Python scripts
│   │   │   ├── README.md             # Script documentation
│   │   │   ├── build_collab_hub_from_scratch.py
│   │   │   └── generate_ccs_demo_data.py
│   │   ├── docs/                      # Methodology & submission docs
│   │   │   ├── methodology.md        # Complete step-by-step methodology
│   │   │   ├── limitations.md        # Known limitations
│   │   │   ├── judge_qa.md           # Answers to judge questions
│   │   │   ├── cover_letter_template.md
│   │   │   └── slides_outline.md
│   │   ├── powerbi/                   # Power BI setup
│   │   │   └── README.md
│   │   ├── data/                      # Data policy
│   │   │   └── README.md
│   │   └── outputs/                   # Output descriptions
│   │       └── README.md
│   ├── sustainability_dashboard/      # (component folder)
│   ├── research_coverage/            # (component folder)
│   ├── impact_engine/                # (component folder)
│   └── ai_prototype/                 # (component folder)
│
├── docs/                              # Main project documentation
├── scripts/                           # Shared scripts (if any)
├── presentation/                      # Competition presentation
└── screenshots/                      # Dashboard screenshots
```

---

## 📚 Documentation

### Main Documentation

### Collaboration Hub Documentation

**Documentation available in `components/collab_hub/`**:

| Document | Description |
|----------|-------------|
| `README.md` | Component overview and quick start |
| `docs/methodology.md` | Complete step-by-step methodology |
| `docs/judge_qa.md` | Answers to common judge questions |
| `docs/limitations.md` | Known limitations and future work |
| `scripts/README.md` | Script documentation and usage |

---

## 🎓 Skills Demonstrated

### Technical Skills

- **Data Engineering**: ETL pipeline design and implementation
- **Data Analysis**: Statistical analysis and pattern recognition
- **Algorithm Design**: Multi-factor scoring system development
- **Data Visualization**: Power BI dashboard creation (4 integrated components)
- **Python Programming**: Data processing and transformation scripts
- **AI/ML Integration**: Google AI Studio prototype development

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
   - NLP topic modeling for better method inference
   - Predictive analytics for collaboration success
   - Network analysis for research communities

3. **Platform Features**
   - Dynamic KPI tracking over time
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
- 🌐 **Streamlit App**: Deployed on Streamlit Cloud (see DEPLOYMENT_GUIDE.md)
- 📄 **Presentation**: Available in `/presentation` folder
- 🤖 **AI Prototype**: Try the AI Prototype

---

<div align="center">

**Built with** ❤️ **for sustainable research collaboration**

_Illinois Sustainability Impact Engine - Case Competition 2025_

</div>
