# Gies Impact Command Center

> **AI-powered sustainability research intelligence for the Gies College of Business, University of Illinois Urbana-Champaign**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-prattkk11.github.io-brightgreen?style=flat-square)](https://prattkk11.github.io/sustainability-dashboard/)
[![HTML](https://img.shields.io/badge/Built%20with-HTML%2FJS-orange?style=flat-square)](#)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](#license)

---

## Overview

The **Gies Impact Command Center** is an analytics dashboard that tracks sustainability research contributions from Gies College of Business faculty. It maps academic publications to the United Nations' 17 Sustainable Development Goals (SDGs) and surfaces insights for academic leadership, faculty, and institutional reporting.

Under the hood, it runs a two-stage AI classification pipeline: LLMs handle relevance detection, and FAISS vector search handles SDG assignment. The frontend makes that output actually readable.

---

## Live Demo

**[prattkk11.github.io/sustainability-dashboard](https://prattkk11.github.io/sustainability-dashboard/)**

---

## Features

### Analytics & Visualization
- **SDG Distribution:** Research alignment across all 17 UN Sustainable Development Goals
- **Department Comparisons:** Sustainability contribution analysis broken down by academic department
- **Publication Trend Analysis:** Year-over-year research output and growth rate tracking
- **Impact KPI Cards:** Quick metrics for sustainability ratios and faculty engagement counts

### AI Classification Pipeline
- **Stage 1 (Relevance Detection):** LLM-based binary classification for whether a publication contributes to any sustainability goal
- **Stage 2 (SDG Identification):** FAISS vector similarity search that assigns the top 3 most relevant SDGs per publication with weighted relevance scores
- Accounts for both direct sustainability work and foundational research that supports SDG progress

### Search & Discovery
- **Advanced Filtering:** Filter by department, year, SDG goal, and journal tier
- **Journal Impact Tracking:** Publications cross-referenced against Financial Times and UT Dallas top-journal lists

### Data Sources
- **Illinois Experts API:** Pulls faculty profiles and publication metadata directly from the university's research database
- **Web Scraping:** Rate-limited scraping for supplemental research metadata
- **Journal Rankings Database:** Classifies publications by academic impact and business domain

---

## Technical Stack

| Layer | Technology |
|---|---|
| Frontend | React (single-file, GitHub Pages hosted) |
| AI Classification | OpenAI GPT models |
| Vector Search | FAISS + Pinecone |
| Data Pipeline | Python |
| Deployment | GitHub Pages |

---

## Data Architecture

The backend pipeline structures data across three layers:

**Faculty Records:** identifiers, department affiliations, active status, research keyword profiles

**Publication Database:** article metadata, DOIs, journal classifications, sustainability scores, SDG mappings

**Sustainability Analytics:** binary sustainability flags, ranked SDG assignments (top 3 per publication), temporal trends, department-level aggregations

---

## Repository Structure

```
sustainability-dashboard/
├── index.html        # Single-file React dashboard (all components, styles, and logic)
└── .gitignore
```

Everything lives in `index.html`. No build step required.

---

## Getting Started

### View Locally

Clone the repo and open `index.html` in a browser:

```bash
git clone https://github.com/agatafietko/sustainability-dashboard.git
cd sustainability-dashboard
open index.html
```

No dependencies, no build process, no npm install.

### Deploy to GitHub Pages

1. Go to **Settings > Pages** in your forked repo
2. Set source to `main` branch, `/ (root)`
3. Your dashboard will be live at `https://<your-username>.github.io/sustainability-dashboard/`

---

## Use Cases

**Academic Leadership:** Insights for sustainability planning, metrics for accreditation reporting, identification of emerging research strengths

**Faculty:** Visibility into SDG contributions and potential collaborators working on related goals

**Institutional Reporting:** Data for sustainability rankings, grant applications, and documenting research impact

---

## Roadmap

- [ ] Faculty-level profiles with individual SDG breakdowns
- [ ] Confidence score display per publication classification
- [ ] Semantic search with natural language query support
- [ ] Research similarity recommendations for collaboration discovery
- [ ] Year-over-year growth rate callouts on trend charts
- [ ] Data freshness timestamps and source attribution

---

## Forked From

[prattkk11/sustainability-dashboard](https://github.com/prattkk11/sustainability-dashboard)

---

## License

MIT
