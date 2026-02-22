# Collaboration Hub Documentation (Judges Two-Pager)

## 1) Purpose and User Need
Universities generate extensive sustainability research, but expertise is fragmented across departments and individuals. The Collaboration Hub is designed to help faculty, students, and leadership identify complementary partners and form interdisciplinary teams aligned to UN SDGs.

## 2) Collaboration Compatibility Score (CCS): Rationale and Formula
The CCS is a weighted, explainable scoring model grounded in stakeholder input to balance topic alignment with complementary research methods and career-stage pairing.

**Weights**
- Topic Match: 45%
- Method Match: 40%
- Career Fit: 15%

**Formula**
```
CCS_Total = ROUND((Topic_Match × 0.45) + (Method_Match × 0.40) + (Career_Fit × 0.15))
```

**Why these weights**
- Topic alignment is primary to ensure relevance.
- Method complementarity increases collaboration value.
- Career fit supports mentorship and balanced teams without dominating the score.

## 3) Scoring Logic (Explainable Components)
**Topic Match (hierarchical SDG alignment)**
1. Exact primary SDG match (highest score)
2. Primary SDG appears in the other’s SDG list
3. Any SDG overlap
4. Adjacent SDGs
5. Same SDG category
6. Default (no overlap)

**Method Match**
- Complementary methods score higher (e.g., Empirical + Theoretical).
- Same or similar methods score lower.

**Career Fit**
- Mentorship pairings score higher (Pre-Tenure + Post-Tenure/Senior).
- Peer pairings score moderate.

This structure makes scores transparent and auditable rather than black-box.

## 4) Data Pipeline and Generation (What We Actually Did)
The demo data was generated using a documented pipeline; the scripts are not included in this public repo, but the logic is fully described.

```
Original CSV (filtered_publications.csv)
   ↓
build_collab_hub_from_scratch.py
   ↓
Researcher_Profiles_For_PowerBI.csv
   ↓
generate_ccs_demo_data.py
   ↓
CCS_Demo_Data.csv (available upon request)
```

**Directly used fields**
- Researcher name, department, SDG labels, keywords, abstract, publication year.

**Derived fields**
- Primary SDG (most frequent SDG)
- Method (keyword inference)
- Career stage (years since first publication)
- Top keywords (frequency ranking)

**Simulated for demo**
- Some user search inputs were varied to show multiple scenarios.
- All CCS scores are computed from the model.
- Explanations are generated from keywords + scoring logic.

## 5) Evidence and Transparency
- Detailed scoring logic and data provenance are documented in:
  - `docs/methodology/CCS_DEMO_DATA_EXPLANATION.md`
  - `docs/methodology/SDG_MATCHING_EXPLANATION.md`
  - `docs/04_scoring_and_metrics.md`

## 6) Validation and Limitations (Current State)
- Prototype-level; not a predictive success model.
- Scores are directional and explainable.
- Demo uses simulated search scenarios for presentation.

## 7) Stakeholder Input and Weighting Justification
- Weighting was informed by stakeholder input, including an interview with Professor Fei.
- Future work: expand interviews across faculty, leadership, and students to refine weights and add calibration with historical collaboration outcomes.

## 8) Judge Feedback → Concrete Improvements
**Feedback: unclear value vs status quo**
- Add a side-by-side slide: current discovery process vs hub (time saved, visibility, structured matching).

**Feedback: “Why 15% career fit?”**
- Add a short rationale and sensitivity note: weights tested for stability; career fit capped to avoid over-weighting hierarchy.

**Feedback: “Who is matched with whom?”**
- Add 2–3 concrete examples (user → match, CCS score, explanation snippet).

**Feedback: “AI accuracy and data source clarity”**
- Add a one-slide methodology summary and data source list.
- Explicitly label limitations and what is simulated.

**Feedback: “Collaboration score is hard to interpret”**
- Add a visual explaining the three score components and how they roll up to CCS.

**Feedback: “Need more about scraped data”**
- Add a data fields table and note that raw CSV is not shared for privacy.

## 9) Next Steps (Validation Plan)
1. Conduct 6–10 stakeholder interviews to re-weight factors.
2. Compare model rankings to known collaborations for face validity.
3. Add qualitative feedback loop for match outcomes.
4. Publish a short methodology appendix in the deck.
