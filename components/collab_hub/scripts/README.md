# Collaboration Hub Scripts

This folder contains the Python scripts that generate researcher profiles and collaboration matches.

## Core Scripts

### `build_collab_hub_from_scratch.py`
**Purpose**: Main pipeline that builds the complete collaboration matching system

**What it does**:
1. Loads the publications CSV
2. Aggregates publications into researcher profiles
3. Calculates pairwise compatibility scores
4. Generates Power BI-ready outputs

**Input**: `for distribution case competition filtered_publications.csv`

**Outputs**:
- `Researcher_Profiles_For_PowerBI.csv` - One row per researcher with aggregated metrics
- `Collab_Matches_For_PowerBI.csv` - All pairwise matches with scores
- `faculty_matches.csv` - Same as above, different format
- `best_faculty_match.csv` - Top 50 matches
- `network_graph_data.csv` - Network visualization edges

**Usage**:
```bash
python build_collab_hub_from_scratch.py
```

### `generate_ccs_demo_data.py`
**Purpose**: Creates demo dataset for Power BI presentation

**What it does**:
1. Loads researcher profiles
2. Selects diverse researchers (by career stage)
3. Generates 2-3 matches per researcher
4. Adds small randomized variation for presentation clarity
5. Calculates CCS scores using the same formula

**Input**: `Researcher_Profiles_For_PowerBI.csv` (from build_collab_hub_from_scratch.py)

**Output**: `CCS_Demo_Data.csv` - Demo matches for dashboard

**Usage**:
```bash
python generate_ccs_demo_data.py
```

**Important**: This is **demo data** with randomized variation. It's designed to show how the scoring works, not to predict real collaborations.

### `build_ccs_demo_from_original.py`
**Purpose**: Alternative demo data generator (if needed)

### `add_exceptional_matches.py`
**Purpose**: Utility script to add specific high-quality matches to demo data

## Dependencies

Install required packages:
```bash
pip install pandas numpy
```

## Data Flow

```
Publications CSV
    ↓
build_collab_hub_from_scratch.py
    ↓
Researcher_Profiles_For_PowerBI.csv
    ↓
generate_ccs_demo_data.py
    ↓
CCS_Demo_Data.csv (for Power BI)
```

## Scoring Formula

All scripts use the same compatibility scoring:

```
CCS_Total = (Topic_Score × 0.50) + (Method_Score × 0.35) + (Career_Score × 0.15)
```

Where:
- **Topic_Score**: SDG alignment (70%) + keyword overlap (30%)
- **Method_Score**: Rewards complementary methods (Theoretical + Empirical = high)
- **Career_Score**: Rewards mentorship pairings (Pre-Tenure + Senior = high)

See `../docs/methodology.md` for detailed explanation.
