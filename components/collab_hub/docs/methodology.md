# Collaboration Hub – Complete Methodology

> **This document explains exactly how the Collaboration Hub works, step-by-step, to address judge questions and ensure transparency.**

---

## 1. Goal

The Collaboration Hub recommends research collaborators to accelerate sustainability impact. It converts publication metadata into researcher profiles, then scores pairwise compatibility using a transparent, rule-based algorithm.

**Key principle**: This is **not predictive AI**. It's a transparent heuristic that decision-makers can understand and validate.

---

## 2. Data Source

### Input Data

- **Source**: Publications CSV provided by the case competition
- **No external scraping**: All data comes from the provided dataset
- **Fields used**:
  - Author names (`name`, `person_uuid`)
  - Departments (`department`)
  - Publication years (`publication_year`)
  - Keywords (`keywords`)
  - Abstracts (`abstract_text` or `abstract`)
  - SDG labels (`top 1`, `top 2`, `top 3`, `is_sustain`)

### Data Processing

1. **Cleaning**: Remove invalid years, clean SDG columns (must be 1-17)
2. **Validation**: Filter to publications between 1900-2026
3. **Aggregation**: Group by `person_uuid` to build researcher profiles

---

## 3. Researcher Profile Construction

For each unique researcher (`person_uuid`), we aggregate their publications:

### Basic Metrics

- **`total_publications`**: Count of all publications for this researcher
- **`sustainable_publications`**: Count where `is_sustain = true`
- **`first_publication_year`**: Earliest publication year
- **`last_publication_year`**: Most recent publication year
- **`years_active`**: `last_year - first_year`
- **`years_since_first`**: Years from first publication to 2025 (current year)

### Career Stage Inference

**Rule-based classification** (not ML):

```python
if years_since_first > 15:
    career_stage = "Senior"
elif years_since_first > 7:
    career_stage = "Post-Tenure"
else:
    career_stage = "Pre-Tenure"
```

**Why this matters**: Career stage affects mentorship opportunities and collaboration dynamics.

### Top Keywords

1. Extract all keywords from all publications (semicolon-separated)
2. Count frequency of each keyword
3. Keep top 10-15 most frequent keywords
4. Store as `top_keywords` (semicolon-separated)

**Used for**: Keyword overlap scoring in compatibility calculation.

### Primary SDG

1. Collect all SDG labels (`top 1`, `top 2`, `top 3`) from all publications
2. Count frequency of each SDG (1-17)
3. **`primary_sdg`**: Most frequent SDG
4. **`sdg_list`**: Top 2-3 SDGs (comma-separated)

**Used for**: SDG alignment scoring in compatibility calculation.

### Primary Method Inference

**Rule-based keyword matching** (not NLP model):

1. Combine all keywords and first 5000 chars of abstracts into one text string
2. Define method keywords:
   - **Theoretical**: 'theoretical', 'model', 'modeling', 'optimization', 'game theory', 'mathematical', 'algorithm', 'framework', 'conceptual'
   - **Empirical**: 'empirical', 'statistical', 'regression', 'analysis', 'data', 'quantitative', 'econometric', 'estimation', 'dataset'
   - **Qualitative**: 'qualitative', 'case study', 'interview', 'ethnography', 'narrative', 'discourse', 'phenomenology'
   - **Fieldwork**: 'field', 'survey', 'experiment', 'observational', 'fieldwork', 'field study', 'field experiment'
   - **Experimental**: 'experiment', 'randomized', 'trial', 'laboratory', 'lab', 'controlled experiment', 'RCT'
   - **Computational**: 'computational', 'simulation', 'machine learning', 'AI', 'artificial intelligence', 'deep learning', 'neural network'

3. Count keyword matches for each method
4. **`primary_method`**: Method with highest count
5. If no matches found, default to "Mixed Methods"

**Limitation**: This is a simple heuristic. It may miss nuanced method distinctions.

---

## 4. Compatibility Scoring Algorithm

For each pair of researchers (A, B), we calculate a compatibility score.

### Formula

```
CCS_Total = (Topic_Score × 0.50) + (Method_Score × 0.35) + (Career_Score × 0.15)
```

**Why these weights?**
- **Topic (50%)**: Research alignment is the strongest predictor of collaboration success
- **Method (35%)**: Complementarity drives innovation (this is our key innovation)
- **Career (15%)**: Mentorship matters, but shouldn't dominate collaboration quality

### Topic Score Calculation (50% weight)

**Sub-components**:
- SDG alignment (70% of topic score)
- Keyword overlap (30% of topic score)

#### SDG Alignment (70% of topic score)

1. Get SDG lists for both researchers (from `sdg_list`)
2. **Exact matches**: Count SDGs that appear in both lists
   - Each exact match = 30 points
3. **Related SDGs**: SDGs in same cluster (1-6 social, 7-12 economic, 13-17 environmental)
   - Each related pair = 0.3 points (capped)
4. **SDG score**: `min(100, exact_matches × 30 + related_score × 10)`

#### Keyword Overlap (30% of topic score)

1. Get keyword sets for both researchers (from `top_keywords`)
2. Calculate Jaccard similarity: `intersection / union`
3. **Keyword score**: `jaccard × 100`

#### Combined Topic Score

```
Topic_Score = (SDG_Score × 0.7) + (Keyword_Score × 0.3)
```

**Range**: 0-100

### Method Score Calculation (35% weight)

**Key innovation**: Rewards **complementary methods**, not similarity.

#### Complementarity Matrix

High scores for complementary pairs:
- Theoretical + Empirical = **100**
- Theoretical + Fieldwork = **100**
- Empirical + Qualitative = **85**
- Fieldwork + Computational = **85**

Low scores for same methods:
- Theoretical + Theoretical = **25**
- Empirical + Empirical = **25**
- Mixed Methods + Mixed Methods = **50**

Moderate scores for different but not explicitly complementary:
- Default = **50**

**Why this matters**: Different methods bring different perspectives, leading to more innovative research.

### Career Stage Score Calculation (15% weight)

**Optimal pairs** (mentorship opportunities) = **100**:
- Pre-Tenure + Post-Tenure
- Pre-Tenure + Senior
- Post-Tenure + Senior

**Good pairs** (peer collaboration) = **60-75**:
- Same stage (Post-Tenure + Post-Tenure = 75)
- Same stage (Pre-Tenure + Pre-Tenure = 60)

**Other combinations** = **50**

**Why 15%?**: Career stage matters for mentorship, but topic and method alignment are more important for research success.

---

## 5. Output Generation

### Main Pipeline Outputs

1. **`Researcher_Profiles_For_PowerBI.csv`**
   - One row per researcher
   - All aggregated metrics (publications, career stage, method, SDG, keywords)

2. **`Collab_Matches_For_PowerBI.csv`**
   - One row per researcher pair
   - All scores (Total, Topic, Method, Career)
   - Explanations and reasons
   - Match quality labels

3. **`network_graph_data.csv`**
   - Network edges for visualization
   - Only high-quality matches (score ≥ 70)

### Demo Data Generation

**`CCS_Demo_Data.csv`** is created separately for presentation:

1. Selects 15 diverse researchers (mix of career stages)
2. Generates 2-3 matches per researcher
3. **Adds small randomized variation** to SDG/method inputs to show diverse scenarios
4. Uses same scoring formula as main pipeline

**Important**: Demo data is **synthetic** (with randomization) for presentation clarity. It's not a predictive model.

---

## 6. Explainability

Every match includes:

1. **Total score** and **sub-scores** (Topic, Method, Career)
2. **Text explanation**:
   - Top keywords from match
   - Method complementarity description
   - Career pairing description
3. **Reasons**:
   - `Topic_Reason`: SDG alignment summary
   - `Method_Reason`: Method pairing and complementarity
   - `Stage_Reason`: Career stage pairing and opportunity type

**Example explanation**:
> "Expertise in Machine Learning and Data Analytics. Highly complementary methods (Computational + Empirical) create exceptional research synergy. Strong mentorship pairing: Post-Tenure and Pre-Tenure researchers."

---

## 7. Validation

### Method Complementarity Validation

The algorithm correctly:
- ✅ Scores Theoretical + Empirical = ~100 (high complementarity)
- ✅ Scores Theoretical + Theoretical = ~25 (low complementarity)
- ✅ Scores mentorship pairs (Pre-Tenure + Senior) = ~100

### Score Ranges

- **Excellent matches**: 85-100
- **Good matches**: 70-84
- **Moderate matches**: 55-69
- **Low matches**: <55

---

## 8. Limitations

See `limitations.md` for detailed limitations. Key points:

1. **Rule-based, not AI**: This is a transparent heuristic, not a predictive ML model
2. **Method inference**: Simple keyword matching may miss nuance
3. **SDG assignment**: Relies on provided labels (may be sparse)
4. **Demo data**: Includes randomization for presentation clarity

---

## 9. Reproducibility

### To Reproduce Results

1. Place the publications CSV in the expected location
2. Run `build_collab_hub_from_scratch.py`
3. Review outputs in `Researcher_Profiles_For_PowerBI.csv` and `Collab_Matches_For_PowerBI.csv`

### To Generate Demo Data

1. First run `build_collab_hub_from_scratch.py` (to create researcher profiles)
2. Then run `generate_ccs_demo_data.py`
3. Review `CCS_Demo_Data.csv`

---

## Summary

The Collaboration Hub is a **transparent, rule-based system** that:
- Converts publication metadata into researcher profiles
- Scores pairwise compatibility using topic, method, and career factors
- Rewards complementary methods (key innovation)
- Provides explainable recommendations

**It is not predictive AI**—it's a decision support tool that makes collaboration opportunities visible and actionable.
