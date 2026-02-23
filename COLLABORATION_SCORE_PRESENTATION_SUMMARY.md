# Collaboration Compatibility Score - Presentation Summary
## Quick Reference for Case Competition Presentation

---

## 🎯 **THE INNOVATION**

**Collaboration Compatibility Score (0-100)**: A quantified metric that proactively suggests interdisciplinary research partners based on three stakeholder-validated dimensions.

---

## 📐 **THE ALGORITHM**

### **Formula**
$$\text{Score} = (0.50 \times S_{\text{Topic}}) + (0.35 \times S_{\text{Method}}) + (0.15 \times S_{\text{Stage}})$$

### **Weights (Justified by Professor's Feedback)**

| Component | Weight | Why |
|-----------|--------|-----|
| **Topic Match** | **50%** | Primary factor - shared research interests are foundational |
| **Method Match** | **35%** | Critical - professor emphasized seeking **complementary** (different) methods |
| **Career Stage** | **15%** | Strategic enabler - important but secondary to research alignment |

---

## 🔍 **SUB-SCORE LOGIC**

### **1. Topic Match (0-100)**
**Data Sources**: FAISS vector database, SDG Relevance Scores, NLP keywords

**Calculation**:
- **FAISS Similarity (40%)**: Semantic search on research content
- **SDG Alignment (35%)**: Matching SDG focus areas with relevance scores
- **Keyword Overlap (25%)**: Jaccard similarity of publication keywords

**Example**: User (AI for Healthcare) + Collaborator (ML in Medical Diagnosis) = **75.6/100**

---

### **2. Method Match (0-100)**
**CRITICAL INNOVATION**: Rewards **DIFFERENT/complementary** methods, not identical methods.

**Method Categories**:
- Theoretical ↔ Empirical/Quantitative
- Qualitative ↔ Quantitative
- Fieldwork ↔ Computational
- Experimental ↔ Theoretical

**Scoring**:
- Perfect Complementarity (different categories) = **100**
- Same category = **0-25** (low score)

**Example**: User (Theoretical) + Collaborator (Empirical) = **100/100**

**Why**: Interdisciplinary collaboration thrives on method diversity.

---

### **3. Career Stage Match (0-100)**
**Data Sources**: Faculty records, tenure status, years post-PhD

**Optimal Matches**:
- Pre-Tenure ↔ Post-Tenure (mentorship opportunity) = **100**
- Post-Tenure ↔ Senior (strategic partnership) = **100**

**Example**: User (Pre-Tenure) + Collaborator (Post-Tenure) = **100/100**

---

## 🎨 **UX DELIVERABLES**

### **1. Search Results Wireframe**
**Key Elements**:
- **Compatibility Score** prominently displayed (top-right, 87.8/100)
- **Quick Breakdown** inline (Topic: 75.6, Method: 100, Stage: 100)
- **Ranking** by score (Rank #1, #2, etc.)
- **Action Buttons**: "Why?" (transparency) + "Contact" (CTA)

**Visual Hierarchy**: Score is the primary ranking tool, always visible.

---

### **2. Transparent AI Breakdown Modal**
**Purpose**: Build trust through explainability.

**Content**:
- Overall score with interpretation
- Detailed breakdown of each sub-score:
  - Component-level explanation (FAISS, SDG, Keywords)
  - Evidence citations (publications, grants)
  - "Why This Matters" section
- Recommended next steps

**Design**: Expandable sections, progress bars, color-coded scores.

---

### **3. Network Graph Integration**
**Visual Encoding**:
- **Edge Thickness**: Thicker = Higher score (5px for 80-100, 1px for 0-39)
- **Edge Color/Brightness**: Brighter = Higher score (Orange/Green for 80+, Gray for low)
- **Edge Opacity**: More opaque = Higher score (100% for 80+, 20% for low)

**Result**: Interdisciplinary opportunities are **instantly visible** - thick, bright edges show best matches.

**Interactive**: Hover for score, click for breakdown, filter by minimum score.

---

## 💡 **KEY TALKING POINTS**

### **For Judges**

1. **Visionary & Grounded**:
   - ✅ Algorithm based on stakeholder research (professor interview)
   - ✅ Uses existing platform capabilities (FAISS, SDG Scores)
   - ✅ Clear path to implementation

2. **Innovation**:
   - ✅ Proactive suggestion (not just search)
   - ✅ Quantified compatibility (not subjective)
   - ✅ Method complementarity (rewards different methods)

3. **Transparency**:
   - ✅ Full score breakdown with evidence
   - ✅ Explainable AI (not black box)
   - ✅ Data sources cited

4. **User Experience**:
   - ✅ Score is primary ranking mechanism
   - ✅ Network graph makes opportunities visible
   - ✅ Seamless integration across views

---

## 📊 **EXAMPLE SCENARIO**

**User Profile**:
- Research: AI for Healthcare (SDG 3)
- Method: Theoretical
- Stage: Pre-Tenure

**Top Match - Collaborator A**:
- Research: ML in Medical Diagnosis (SDG 3)
- Method: Empirical/Quantitative
- Stage: Post-Tenure

**Score Calculation**:
- Topic: 75.6 (FAISS: 94, SDG: 70, Keywords: 54)
- Method: 100 (Perfect complementarity: Theoretical + Empirical)
- Stage: 100 (Optimal: Pre-Tenure + Post-Tenure)

**Final Score**: **87.8/100** - Excellent match for interdisciplinary collaboration.

---

## ✅ **IMPLEMENTATION STATUS**

**Algorithm**: ✅ Finalized with weights and sub-score logic  
**UX Design**: ✅ Wireframes and specifications complete  
**Presentation**: ✅ Ready for case competition  

---

**This summary provides quick reference for the presentation. Full details in `COLLABORATION_COMPATIBILITY_SCORE_FINAL.md`.**


