# Gies Impact Command Center

> **AI-powered sustainability research intelligence for the Gies College of Business, University of Illinois Urbana-Champaign**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-agatafietko.github.io-brightgreen?style=flat-square)](https://agatafietko.github.io/sustainability-dashboard/)
[![Built With](https://img.shields.io/badge/Built%20with-React%20%2F%20HTML-orange?style=flat-square)](#)
[![Team](https://img.shields.io/badge/Team-Silly%20Gies-blueviolet?style=flat-square)](#team)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](#license)

---

## Overview

The **Gies Impact Command Center** maps 2,022 Gies College of Business faculty publications (2010–2020) to the United Nations' 17 Sustainable Development Goals, surfacing research gaps, collaboration opportunities, and strategic intelligence for academic leadership, faculty, donors, and institutional partners.

It runs a two-stage AI classification pipeline: LLMs handle relevance detection, and FAISS vector search handles SDG assignment. The frontend makes that output immediately actionable — no 40-page PDF required.

---

## Live Demo

**[agatafietko.github.io/sustainability-dashboard](https://agatafietko.github.io/sustainability-dashboard/)**

---

## Key Findings

- **2,022** total indexed publications · **426** meet sustainability criteria (21.1%)
- **15 of 17 SDGs** covered · SDG 14 and SDG 15 at zero publications
- **+347% growth** in sustainable research output from 2010 to 2020
- **Largest gap:** SDG 14 (Life Below Water) and SDG 15 (Life on Land) vs. ~5.7% global benchmark each
- **Top SDGs:** SDG 3 (141 papers), SDG 10 (105), SDG 8 (87)
- **Top researchers:** Lough (53 papers, SDG 17), Fullerton (35, SDG 13), Ahsen (29, SDG 3)

---

## Features

### Hero Banner
Full-width landing section at the top of the Overview tab, visible immediately on load. Includes the "Moving from Information to Action." headline, a data provenance strip linking all four sources, and an inline AI assistant panel with a pre-surfaced research insight and clickable quick prompts.

### Analytics & Visualization
- **SDG Wheel:** Interactive radial chart mapping institutional coverage across all 17 SDGs with toggle to compare against the UN global benchmark
- **Gap Index:** Identifies the most under-indexed SDGs relative to global averages, surfaced as actionable priority areas
- **Department Breakdown:** Sustainability contribution analysis across Business Administration, Finance, Accountancy, and Gies Affiliates
- **KPI Cards:** Sustainability rate, paper counts, SDG coverage, and largest gap at a glance
- **Publication Trend Chart:** Year-over-year research output tracking from 2010 to 2020

### AI Classification Pipeline
The dataset was processed through a two-stage automated pipeline before appearing in the dashboard.

**Stage 1 (Relevance Detection):** LLM-based binary classification determines whether each publication contributes to any sustainability goal, directly or foundationally.

**Stage 2 (SDG Assignment):** FAISS vector similarity search assigns the top 3 most relevant SDGs per publication. This accounts for interdisciplinary research spanning multiple goals.

All insights labeled "AI-assisted" are deterministic rules-based synthesis, not predictions.

### Research Intelligence Assistant
An inline AI assistant on the Overview tab surfaces key findings without requiring a button click. An auto-surfaced insight highlights the most significant gap in the dataset. Quick-prompt pills let users ask pre-formed questions directly, opening the full chat drawer pre-loaded.

### Faculty Profiles
Click any researcher in the Overview or Network tab to open a full profile modal showing their department, total sustainable paper count, SDG coverage (primary and secondary), research keywords sourced from the dataset, and collaboration pairings they appear in. All data is sourced from the Illinois Experts API — no fabricated bios or titles.

### Collaboration Network
- **Pairings:** Researchers sharing SDG indexing are surfaced as potential collaborators with named pairs, shared SDGs, combined paper counts, and outcome descriptions
- **Methodology transparency:** Pairings are based on bibliometric co-indexing only. No numeric compatibility scores are assigned — predicting collaboration success requires qualitative assessment beyond this data
- **Department nodes:** Click any department to see its suggested pairings

### Collaboration Hub
A dedicated tab connecting Gies research gaps to external funding and partnership opportunities.

- Sustainability Case Competition portal embedded via iframe with full interactivity
- Quick-jump links to Sponsor a Priority, SDG Gaps, Research Partnerships, and Case Competition tracks
- Gap-to-sponsorship mapping: SDGs 14, 15, and 2 (Gies' most under-indexed) surface as open sponsorship tracks
- Context strip explains how the embedded portal connects to the dashboard's own gap analysis

### User Journey Maps
The "Who Uses This" tab contains full visual journey maps for two primary personas: Eleanor (University Donor, age 58) and Marcus (Student Researcher, age 22). Each map includes a before/after comparison showing how the dashboard improves on the status quo, a 5-step journey with emotion labels per stage, features used, time-to-value, and a plain-language improvement summary.

---

## Data Sources

| Source | Role |
|---|---|
| Illinois Experts API (Elsevier) | Faculty profiles and publication metadata |
| Elsevier Scopus | Bibliometric indexing and DOI resolution |
| UN SDG 2023 Report | Global benchmark distribution (normalized) |
| FT50 / UTD24 Journal Lists | Journal quality classification |

Full methodology is accessible via the "Methodology" link in the dashboard footer.

---

## Navigation

| Tab | Contents |
|---|---|
| Overview | Hero banner, data provenance, AI assistant, KPI cards, SDG wheel, gap index, department breakdown, keyword cloud, AI snapshot |
| Network | Collaboration pairings by department, researcher nodes, faculty grid, methodology note |
| Global Impact | World map, geospatial research reach, full SDG coverage by region |
| Collaboration Hub | Embedded Case Competition portal, SDG gap-to-sponsorship mapping, partner links |
| Who Uses This | Visual journey maps for Donor and Student personas |

---

## Technical Stack

| Layer | Technology |
|---|---|
| Frontend | React (single-file, CDN-loaded, no build step) |
| AI Classification | LLM-based binary relevance detection (Stage 1) |
| Vector Search | FAISS — top-3 SDG assignment per publication (Stage 2) |
| Data Pipeline | Python, Illinois Experts API, rate-limited scraping |
| Collaboration Hub | Streamlit iframe embed |
| Deployment | GitHub Pages |

---

## Repository Structure

```
sustainability-dashboard/
├── index.html        # Single-file React dashboard — all components, styles, and logic
└── .gitignore
```

Everything lives in `index.html`. No dependencies, no build process, no npm install.

---

## Getting Started

### View Locally

```bash
git clone https://github.com/agatafietko/sustainability-dashboard.git
cd sustainability-dashboard
open index.html
```

### Deploy to GitHub Pages

1. Go to **Settings > Pages** in your forked repo
2. Set source to `main` branch, `/ (root)`
3. Live at `https://<your-username>.github.io/sustainability-dashboard/`

---

## Team

**Silly Gies** — Gies College of Business, University of Illinois Urbana-Champaign

Agata Fietko · Yuri Chen · Meryem Hassan Rafiq · Yuliia Koreiba · Prateek Verma

---

## Roadmap

- [x] Two-stage AI classification pipeline (LLM + FAISS)
- [x] Interactive SDG wheel with global benchmark toggle
- [x] Hero banner with inline data provenance
- [x] Research Intelligence Assistant with auto-surfaced insights
- [x] Faculty profile modals (verified data only)
- [x] Collaboration Hub with embedded Case Competition portal
- [x] SDG gap-to-sponsorship mapping
- [x] Visual user journey maps (Donor + Student personas)
- [ ] Confidence score display per publication classification
- [ ] Semantic / natural language search
- [ ] Research similarity recommendations
- [ ] Year-over-year growth rate callouts on trend charts
- [ ] Data freshness timestamps and source attribution

---

## Forked From

[prattkk11/sustainability-dashboard](https://github.com/prattkk11/sustainability-dashboard)

---

## License

MIT
