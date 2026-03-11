# Gies Impact Command Center

**Built by Team Silly Gies** — Agata Fietko, Yuri Chen, Meryem Hassan Rafiq, Yuliia Koreiba, Prateek Verma

Gies College of Business, University of Illinois Urbana-Champaign

Forked from [prattkk11/sustainability-dashboard](https://github.com/prattkk11/sustainability-dashboard) and extended for the Gies Sustainability Case Competition.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-agatafietko.github.io-brightgreen?style=flat-square)](https://agatafietko.github.io/sustainability-dashboard/)
[![Built With](https://img.shields.io/badge/Built%20with-React%20%2F%20HTML-orange?style=flat-square)](#)
[![Team](https://img.shields.io/badge/Team-Silly%20Gies-blueviolet?style=flat-square)](#team)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](#license)

---

## What This Is

The Gies Impact Command Center maps 2,022 Gies College of Business faculty publications (2010 to 2020) to the UN's 17 Sustainable Development Goals. The goal was simple: take a dataset that would otherwise live in a spreadsheet and make it actually useful for donors, faculty, students, and institutional leadership.

A two-stage AI pipeline processes the raw data. LLMs handle relevance detection first, then FAISS vector search assigns SDGs. The dashboard puts that output in front of people who need it, without a 40-page PDF.

**[agatafietko.github.io/sustainability-dashboard](https://agatafietko.github.io/sustainability-dashboard/)**

---

## Key Numbers

- **2,022** total indexed publications, **426** meet sustainability criteria (21.1%)
- **15 of 17 SDGs** covered; SDG 14 and SDG 15 sit at zero publications
- **+347% growth** in sustainable research output from 2010 to 2020
- Largest gaps: SDG 14 (Life Below Water) and SDG 15 (Life on Land), both at 0 vs. a ~5.7% global benchmark
- Top SDGs: SDG 3 at 141 papers, SDG 10 at 105, SDG 8 at 87
- Top researchers: Lough (53 papers, SDG 17), Fullerton (35, SDG 13), Ahsen (29, SDG 3)
- Departments: Business Admin 250 papers, Finance 121, Accountancy 34, Gies Affiliates 21

---

## Features

### Hero Banner
The first thing you see when the dashboard loads. "Moving from Information to Action." sits at the top alongside a data provenance strip showing all four sources inline and the Research Intelligence Assistant panel. Key findings surface automatically without clicking anything.

### Analytics and Visualization
- **SDG Wheel:** Interactive radial chart showing institutional coverage across all 17 SDGs, with a toggle to overlay the UN global benchmark
- **Gap Index:** Under-indexed SDGs relative to global averages, surfaced as priority areas
- **Department Breakdown:** Coverage across Business Administration, Finance, Accountancy, and Gies Affiliates
- **KPI Cards:** Sustainability rate, paper counts, SDG coverage, and largest gap, updated live when SDGs are filtered
- **Publication Trend Chart:** Year-over-year output from 2010 to 2020
- **Keyword Cloud:** Research topic frequency mapped to SDGs

### AI Classification Pipeline
The full dataset was processed through a two-stage pipeline before anything shows up in the dashboard.

**Stage 1 (Relevance Detection):** LLM-based binary classification determines whether each publication contributes to any sustainability goal, directly or foundationally.

**Stage 2 (SDG Assignment):** FAISS vector similarity search assigns the top 3 most relevant SDGs per publication with weighted relevance scores, accounting for interdisciplinary work.

Everything labeled "AI-assisted" in the dashboard is deterministic rules-based synthesis of the dataset, not generative predictions.

### Research Intelligence Assistant
The assistant is visible inline on the Overview tab before you click anything. An auto-surfaced insight highlights the most significant finding in the current view. Four quick-prompt pills let users ask pre-formed questions that open the full chat drawer pre-loaded. The full assistant handles natural language questions about SDG gaps, researchers, departments, collaboration opportunities, and strategy.

### Faculty Profile Modals
Click any researcher card in the Overview or Network tab to open a profile. Each one shows department, total sustainable paper count, SDG coverage with official SDG colors, research keywords from the dataset, and any collaboration pairings the researcher appears in. All data comes directly from the Illinois Experts API. No fabricated titles, bios, or publication lists.

### Collaboration Network
- Named pairings: researchers sharing SDG indexing are surfaced as potential collaborators, with both names, shared SDGs, combined paper counts, and a concrete outcome description
- Methodology note: pairings are based on bibliometric co-indexing only. No numeric compatibility scores are assigned, since predicting collaboration success requires qualitative assessment beyond this data
- Clickable department nodes surface pairings with sourced rationale

### Collaboration Hub
A tab that connects Gies research gaps directly to external funding and partnership opportunities.

- Sustainability Case Competition portal embedded via iframe with full interactivity
- Quick-jump links to Sponsor a Priority, SDG Gaps, Research Partnerships, and Case Competition tracks
- Gap-to-sponsorship mapping: SDGs 14, 15, and 2 (Gies' most under-indexed goals) surface as open sponsorship tracks in the portal

### User Journey Maps
The "Who Uses This" tab has full visual journey maps for two personas. Each one includes a before/after comparison showing how the dashboard changes the experience, a 5-step journey with emotion labels, features used, time-to-value, and a plain-language improvement summary.

**Eleanor, 58 — University Donor.** Before: calls the development office, gets a 40-page PDF, defers her decision. With the dashboard: filters SDG 13, reads Fullerton's work in the AI snapshot, renews her pledge in under 3 minutes.

**Marcus, 22 — Student Researcher.** Before: emails the department, waits days, cold-emails 10 professors. With the dashboard: filters by keyword, finds Fullerton in the Network tab, emails with context in under 5 minutes.

---

## Data Sources

| Source | Role |
|---|---|
| Illinois Experts API (Elsevier) | Faculty profiles and publication metadata |
| Elsevier Scopus | Bibliometric indexing and DOI resolution |
| UN SDG 2023 Report | Global benchmark distribution (normalized) |
| FT50 / UTD24 Journal Lists | Journal quality classification |

Full methodology is in the dashboard footer and the provenance strip on the Overview tab.

---

## Design Decisions Worth Noting

**No fabricated researcher data.** Faculty profiles only show what is actually in the dataset: name, department, paper count, SDG assignments, and keywords. Titles, bios, and publication lists were removed.

**AI transparency.** "AI-assisted" labels refer to deterministic rules-based synthesis only. The assistant does not generate predictions beyond what the data supports.

---

## Navigation

| Tab | Contents |
|---|---|
| Overview | Hero banner, data provenance, AI assistant, KPI cards, SDG wheel, gap index, department breakdown, keyword cloud |
| Network | Collaboration pairings by department, researcher nodes, faculty profile grid |
| Global Impact | World map, geospatial research reach, SDG coverage by region |
| Collaboration Hub | Embedded Case Competition portal, gap-to-sponsorship mapping, partner links |
| Who Uses This | Visual journey maps for Donor and Student personas with before/after comparison |

---

## Technical Stack

| Layer | Technology |
|---|---|
| Frontend | React (single-file, CDN-loaded, no build step) |
| AI Classification | LLM-based binary relevance detection (Stage 1) |
| Vector Search | FAISS, top-3 SDG assignment per publication (Stage 2) |
| Data Pipeline | Python, Illinois Experts API, rate-limited scraping |
| Collaboration Hub | Streamlit iframe embed |
| Deployment | GitHub Pages |

---

## Repository Structure

```
sustainability-dashboard/
├── index.html        # Single-file React dashboard, all components and logic in one file
└── .gitignore
```

Everything lives in `index.html`. No dependencies, no build process, no npm install.

---

## Getting Started

```bash
git clone https://github.com/agatafietko/sustainability-dashboard.git
cd sustainability-dashboard
open index.html
```

To deploy your own fork: go to **Settings > Pages**, set source to `main` branch at `/ (root)`, and it will be live at `https://<your-username>.github.io/sustainability-dashboard/`.

---

## Changelog

| Version | Changes |
|---|---|
| v1.0 | Initial fork from prattkk11 |
| v1.1 | Collaboration Hub tab with Streamlit embed and gap-to-sponsorship mapping |
| v1.2 | Hero banner ("Moving from Information to Action.") |
| v1.3 | Faculty profile modals with verified dataset-only data |
| v1.4 | Data provenance strip, inline AI assistant panel, quick-prompt pills |
| v1.5 | Full visual user journey maps with before/after comparison |
| v1.5.1 | Removed numeric compatibility scores, added methodology disclaimer |
| v1.5.2 | Fixed AI chatbot responses to remove fabricated statistics |

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
- [ ] Semantic / natural language publication search
- [ ] Research similarity recommendations
- [ ] Year-over-year growth rate callouts on trend charts
- [ ] Data freshness timestamps and source attribution

---

## License

MIT
