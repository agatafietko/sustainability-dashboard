# Collaboration Hub - Visual Wireframes
## Detailed UI/UX Specifications for Presentation

---

## 📱 **WIREFRAME 1: SEARCH RESULTS PAGE**

### **Desktop Layout (Full Width)**

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  ILLINOIS SUSTAINABILITY IMPACT ENGINE                    [User Profile] [⚙️] ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  🔍 COLLABORATION HUB                                                       ║
║  Find Research Partners for Interdisciplinary Collaboration                  ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  ┌─────────────────────────────────────────────────────────────────────┐     ║
║  │  🔍 Search by name, topic, keyword, or SDG...                      │     ║
║  └─────────────────────────────────────────────────────────────────────┘     ║
║                                                                               ║
║  Filters: [SDG ▼ All] [Department ▼ All] [Method ▼ All] [Stage ▼ All]      ║
║  Sort by: [Compatibility Score ▼] [Name] [Department] [Recent Activity]     ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  Showing 15 matches sorted by Compatibility Score                          ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  ┌─────────────────────────────────────────────────────────────────────┐     ║
║  │  Rank #1                                                             │     ║
║  │  ┌───────────────────────────────────────────────────────────────┐   │     ║
║  │  │                                                               │   │     ║
║  │  │  ┌──────────┐                                                 │   │     ║
║  │  │  │         │                                                 │   │     ║
║  │  │  │  Photo  │    ╔═══════════════════════════════════════╗   │   │     ║
║  │  │  │         │    ║  COMPATIBILITY SCORE                 ║   │   │     ║
║  │  │  └──────────┘    ║                                       ║   │   │     ║
║  │  │                  ║          ┌─────────┐                 ║   │   │     ║
║  │  │  Dr. Jane Smith  ║          │  87.8   │                 ║   │   │     ║
║  │  │  Associate Professor ║          │  /100  │                 ║   │   │     ║
║  │  │  Business Administration ║          └─────────┘                 ║   │   │     ║
║  │  │                  ║                                       ║   │   │     ║
║  │  │  Research Focus: Machine Learning in Medical Diagnosis   ║   │   │     ║
║  │  │                  ║  Excellent Match                      ║   │   │     ║
║  │  │  [SDG 3: Good Health]                                    ║   │   │     ║
║  │  │                  ╚═══════════════════════════════════╝   │   │     ║
║  │  │                                                               │   │     ║
║  │  │  Method: Empirical/Quantitative | Career: Post-Tenure        │   │     ║
║  │  │                                                               │   │     ║
║  │  │  Recent: 3 publications (2022-2024) | Grants: $500K active   │   │     ║
║  │  │                                                               │   │     ║
║  │  │  ┌─────────────────────────────────────────────────────┐   │   │     ║
║  │  │  │  Score Breakdown (Quick View):                        │   │   │     ║
║  │  │  │                                                       │   │   │     ║
║  │  │  │  Topic Match:    ████████████░░░░  75.6 (50%)        │   │   │     ║
║  │  │  │  Method Match:   ████████████████  100 (35%)         │   │   │     ║
║  │  │  │  Career Stage:  ████████████████  100 (15%)         │   │   │     ║
║  │  │  │                                                       │   │   │     ║
║  │  │  └─────────────────────────────────────────────────────┘   │   │     ║
║  │  │                                                               │   │     ║
║  │  │  [🔍 Why This Score?]  [📧 Contact Researcher]              │   │     ║
║  │  └───────────────────────────────────────────────────────────────┘   │     ║
║  │                                                                       │     ║
║  └─────────────────────────────────────────────────────────────────────┘     ║
║                                                                               ║
║  ┌─────────────────────────────────────────────────────────────────────┐     ║
║  │  Rank #2                                                             │     ║
║  │  ┌───────────────────────────────────────────────────────────────┐   │     ║
║  │  │  [Photo]  Dr. John Doe                                        │   │     ║
║  │  │           Associate Professor | Finance                        │   │     ║
║  │  │                                                               │   │     ║
║  │  │           ╔═══════════════════════════════════╗              │   │     ║
║  │  │           ║  COMPATIBILITY SCORE            ║              │   │     ║
║  │  │           ║          ┌─────────┐            ║              │   │     ║
║  │  │           ║          │  82.3   │            ║              │   │     ║
║  │  │           ║          │  /100   │            ║              │   │     ║
║  │  │           ║          └─────────┘            ║              │   │     ║
║  │  │           ║  Good Match                    ║              │   │     ║
║  │  │           ╚═══════════════════════════════╝              │   │     ║
║  │  │                                                               │   │     ║
║  │  │  Research Focus: Financial Risk Modeling for Healthcare      │   │     ║
║  │  │  [SDG 3: Good Health] [SDG 8: Economic Growth]               │   │     ║
║  │  │                                                               │   │     ║
║  │  │  Method: Quantitative | Career: Post-Tenure                  │   │     ║
║  │  │  Recent: 5 publications | Grants: $750K active              │   │     ║
║  │  │                                                               │   │     ║
║  │  │  Topic: 78.2 (50%) | Method: 85 (35%) | Stage: 100 (15%)    │   │     ║
║  │  │                                                               │   │     ║
║  │  │  [🔍 Why?]  [📧 Contact]                                    │   │     ║
║  │  └───────────────────────────────────────────────────────────────┘   │     ║
║  └─────────────────────────────────────────────────────────────────────┘     ║
║                                                                               ║
║  [Load More Results]                                                          ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### **Key Design Elements**

1. **Compatibility Score Box**:
   - Position: Top-right of each card
   - Size: ~120px × 100px
   - Border: 3px solid, color-coded (green for 80+, blue for 60-79, yellow for 40-59)
   - Background: Light blue/white gradient
   - Score: Large, bold (36pt font)
   - Label: "Excellent Match" / "Good Match" / etc.

2. **Quick Breakdown Bar**:
   - Horizontal progress bars
   - Color-coded: Blue (Topic), Orange (Method), Green (Stage)
   - Shows score value and weight percentage

3. **Action Buttons**:
   - "Why This Score?" - Secondary button, opens modal
   - "Contact Researcher" - Primary CTA, Illinois Orange

---

## 🎯 **WIREFRAME 2: TRANSPARENT AI BREAKDOWN MODAL**

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  Compatibility Score Breakdown                                    [X Close]    ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  ┌─────────────────────────────────────────────────────────────────────┐     ║
║  │                                                                       │     ║
║  │                    Overall Compatibility Score                       │     ║
║  │                                                                       │     ║
║  │                    ┌──────────────────┐                              │     ║
║  │                    │                  │                              │     ║
║  │                    │      87.8        │                              │     ║
║  │                    │      /100       │                              │     ║
║  │                    │                  │                              │     ║
║  │                    └──────────────────┘                              │     ║
║  │                                                                       │     ║
║  │              Excellent Match for Interdisciplinary Collaboration    │     ║
║  │                                                                       │     ║
║  └─────────────────────────────────────────────────────────────────────┘     ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  ┌─────────────────────────────────────────────────────────────────────┐     ║
║  │  📊 Topic Match Score: 75.6 (Weight: 50%)                            │     ║
║  │  ─────────────────────────────────────────────────────────────────── │     ║
║  │                                                                       │     ║
║  │  ████████████░░░░░░░░  75.6/100                                     │     ║
║  │                                                                       │     ║
║  │  Breakdown:                                                           │     ║
║  │  • FAISS Semantic Similarity: 94/100 (40% of Topic)                 │     ║
║  │    └─ Your research: "AI for Healthcare"                            │     ║
║  │    └─ Their research: "Machine Learning in Medical Diagnosis"      │     ║
║  │    └─ Similarity: 0.88 (high conceptual alignment)                 │     ║
║  │                                                                       │     ║
║  │  • SDG Alignment: 70/100 (35% of Topic)                              │     ║
║  │    └─ Your SDG Focus: SDG 3 (Good Health)                          │     ║
║  │    └─ Their SDG Focus: SDG 3 (Good Health)                         │     ║
║  │    └─ Relevance Scores: Both >0.7 (high alignment)                 │     ║
║  │                                                                       │     ║
║  │  • Keyword Overlap: 54/100 (25% of Topic)                           │     ║
║  │    └─ Shared Keywords: 7 out of 13 total                            │     ║
║  │    └─ Matching: AI, Healthcare, Machine Learning, Diagnosis...    │     ║
║  │                                                                       │     ║
║  │  Evidence:                                                           │     ║
║  │  📄 3 publications on similar topics                               │     ║
║  │  🎯 Both focus on SDG 3 (Good Health)                               │     ║
║  │  🔗 High semantic similarity in research content                    │     ║
║  │                                                                       │     ║
║  │  Why This Matters:                                                   │     ║
║  │  Shared research interests are the foundation of successful          │     ║
║  │  collaboration. Your work on AI for healthcare aligns strongly      │     ║
║  │  with their machine learning research in medical diagnosis.         │     ║
║  │                                                                       │     ║
║  └─────────────────────────────────────────────────────────────────────┘     ║
║                                                                               ║
║  ┌─────────────────────────────────────────────────────────────────────┐     ║
║  │  🔬 Method Match Score: 100 (Weight: 35%)                            │     ║
║  │  ─────────────────────────────────────────────────────────────────── │     ║
║  │                                                                       │     ║
║  │  ████████████████████  100/100                                      │     ║
║  │                                                                       │     ║
║  │  Breakdown:                                                           │     ║
║  │  • Your Method Profile: Theoretical                                  │     ║
║  │    └─ Mathematical modeling, optimization                           │     ║
║  │    └─ Based on: 5 publications, 2 grants                           │     ║
║  │                                                                       │     ║
║  │  • Their Method Profile: Empirical/Quantitative                      │     ║
║  │    └─ Statistical analysis, field data collection                   │     ║
║  │    └─ Based on: 8 publications, 3 grants                           │     ║
║  │                                                                       │     ║
║  │  • Complementarity Assessment:                                       │     ║
║  │    ✅ Perfect Method Complementarity                                │     ║
║  │    ✅ Theoretical + Empirical = Strong Interdisciplinary            │     ║
║  │    ✅ Skill Diversity: They have programming skills                 │     ║
║  │                                                                       │     ║
║  │  Why This Matters:                                                   │     ║
║  │  Your theoretical models can be validated with their empirical     │     ║
║  │  data, creating a complete research pipeline. This complementary   │     ║
║  │  method pairing is ideal for interdisciplinary collaboration.      │     ║
║  │                                                                       │     ║
║  └─────────────────────────────────────────────────────────────────────┘     ║
║                                                                               ║
║  ┌─────────────────────────────────────────────────────────────────────┐     ║
║  │  👔 Career Stage Match Score: 100 (Weight: 15%)                      │     ║
║  │  ─────────────────────────────────────────────────────────────────── │     ║
║  │                                                                       │     ║
║  │  ████████████████████  100/100                                      │     ║
║  │                                                                       │     ║
║  │  Breakdown:                                                           │     ║
║  │  • Your Career Stage: Pre-Tenure Assistant Professor                  │     ║
║  │    └─ 3 years post-PhD                                              │     ║
║  │                                                                       │     ║
║  │  • Their Career Stage: Post-Tenure Associate Professor              │     ║
║  │    └─ 10 years post-PhD                                             │     ║
║  │                                                                       │     ║
║  │  • Strategic Fit: Optimal Match                                      │     ║
║  │    ✅ Mentorship Opportunity                                         │     ║
║  │    ✅ Established Network Access                                    │     ║
║  │    ✅ Career Development Support                                     │     ║
║  │                                                                       │     ║
║  │  Why This Matters:                                                   │     ║
║  │  This collaboration provides mentorship while you build your         │     ║
║  │  research portfolio, and they gain fresh perspectives from your       │     ║
║  │  theoretical expertise.                                              │     ║
║  │                                                                       │     ║
║  └─────────────────────────────────────────────────────────────────────┘     ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  Recommended Next Steps:                                                      ║
║  • Review their recent publications                                           ║
║  • Explore their active grants                                               ║
║  • Check their collaboration network                                          ║
║                                                                               ║
║  [Close]  [📧 Contact Researcher]                                            ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### **Modal Design Specifications**

- **Width**: 800px (desktop), 95% (mobile)
- **Height**: Scrollable, max-height 90vh
- **Background**: White with subtle shadow
- **Sections**: Expandable/collapsible for each sub-score
- **Colors**: 
  - Topic: Blue (#13294B)
  - Method: Orange (#FF6B35)
  - Stage: Green (#4CAF50)

---

## 🕸️ **WIREFRAME 3: NETWORK GRAPH VIEW**

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  Collaboration Network Graph                                    [View Options] ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  Filters: [Min Score: 70 ▼] [SDG: All ▼] [Department: All ▼]                  ║
║                                                                               ║
║  ┌─────────────────────────────────────────────────────────────────────┐     ║
║  │                                                                       │     ║
║  │                    [SDG 3 Node]                                      │     ║
║  │                         │                                             │     ║
║  │                         │ ═══════════ (thick, bright)                │     ║
║  │                         │                                             │     ║
║  │                    ┌────┴────┐                                        │     ║
║  │                    │         │                                        │     ║
║  │                    │  Dr.    │                                        │     ║
║  │                    │  Jane   │                                        │     ║
║  │                    │  Smith  │                                        │     ║
║  │                    │ (87.8)  │                                        │     ║
║  │                    └────┬────┘                                        │     ║
║  │                         │ ═══════════ (thick, bright)                │     ║
║  │                         │                                             │     ║
║  │                    ┌───┴────┐                                        │     ║
║  │                    │  YOU   │                                        │     ║
║  │                    │ (User) │                                        │     ║
║  │                    └───┬────┘                                        │     ║
║  │                        │                                              │     ║
║  │                        │ ═══════ (medium, blue)                      │     ║
║  │                        │                                              │     ║
║  │                    ┌───┴────┐                                        │     ║
║  │                    │  Dr.  │                                        │     ║
║  │                    │  John │                                        │     ║
║  │                    │  Doe  │                                        │     ║
║  │                    │(82.3) │                                        │     ║
║  │                    └───┬────┘                                        │     ║
║  │                        │                                              │     ║
║  │                        │ ─── (thin, gray)                            │     ║
║  │                        │                                              │     ║
║  │                    ┌───┴────┐                                        │     ║
║  │                    │  Dr.  │                                        │     ║
║  │                    │  Mary │                                        │     ║
║  │                    │  Lee  │                                        │     ║
║  │                    │(65.1) │                                        │     ║
║  │                    └───────┘                                        │     ║
║  │                                                                       │     ║
║  │                                                                       │     ║
║  │  Legend:                                                              │     ║
║  │  ═══════  Excellent (80-100) - Thick, Bright Orange/Green           │     ║
║  │  ════     Good (60-79) - Medium, Blue                                │     ║
║  │  ───      Moderate (40-59) - Thin, Light Gray                       │     ║
║  │                                                                       │     ║
║  └─────────────────────────────────────────────────────────────────────┘     ║
║                                                                               ║
║  Hover over any edge to see Compatibility Score                              ║
║  Click edge for detailed breakdown | Click node for profile                  ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### **Network Graph Specifications**

**Node Design**:
- **User Node**: 40px, Illinois Blue, 3px white border, centered
- **Collaborator Nodes**: 30px, Illinois Orange, 2px white border
- **SDG Nodes** (optional): 25px, SDG color, 1px border

**Edge Design**:
- **Thickness Scale**:
  - 80-100: 5px (thickest)
  - 60-79: 3px (medium)
  - 40-59: 2px (thin)
  - 0-39: 1px (very thin)
- **Color Scale**:
  - 80-100: Bright Orange (#FF6B35) or Green (#4CAF50)
  - 60-79: Illinois Blue (#13294B)
  - 40-59: Light Gray (#CCCCCC)
  - 0-39: Very Light Gray (#E0E0E0)
- **Opacity Scale**:
  - 80-100: 100% opacity
  - 60-79: 70% opacity
  - 40-59: 40% opacity
  - 0-39: 20% opacity

**Interactions**:
- **Hover on Edge**: Tooltip shows score
- **Click on Edge**: Opens breakdown modal
- **Click on Node**: Navigate to profile
- **Filter Slider**: Dynamically updates graph

---

## 📱 **MOBILE RESPONSIVE LAYOUT**

### **Search Results (Mobile)**

```
╔═══════════════════════════════════════════════════════════════════╗
║  [☰] COLLABORATION HUB                              [🔍] [Profile] ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  ┌─────────────────────────────────────────────────────────┐     ║
║  │  🔍 Search...                                            │     ║
║  └─────────────────────────────────────────────────────────┘     ║
║                                                                   ║
║  [Filters ▼]                                                    ║
║                                                                   ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  ┌─────────────────────────────────────────────────────────┐     ║
║  │  Rank #1                                                 │     ║
║  │                                                           │     ║
║  │  ┌──────┐                                                │     ║
║  │  │Photo │  Dr. Jane Smith                                │     ║
║  │  └──────┘  Associate Professor                            │     ║
║  │                                                           │     ║
║  │  ╔═══════════════════════════════╗                        │     ║
║  │  ║  COMPATIBILITY SCORE         ║                        │     ║
║  │  ║        87.8/100               ║                        │     ║
║  │  ║  Excellent Match              ║                        │     ║
║  │  ╚═══════════════════════════════╝                        │     ║
║  │                                                           │     ║
║  │  Research: ML in Medical Diagnosis                        │     ║
║  │  [SDG 3]                                                  │     ║
║  │                                                           │     ║
║  │  Topic: 75.6 | Method: 100 | Stage: 100                 │     ║
║  │                                                           │     ║
║  │  [🔍 Why?]  [📧 Contact]                                 │     ║
║  └─────────────────────────────────────────────────────────┘     ║
║                                                                   ║
║  [Load More]                                                      ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

**Mobile Adaptations**:
- Single column layout
- Score box full width
- Quick breakdown collapsed by default
- Touch-friendly button sizes (min 44px)
- Simplified filters (dropdown menus)

---

## 🎨 **COLOR PALETTE**

### **Primary Colors**
- **Illinois Blue**: #13294B (primary text, headers)
- **Illinois Orange**: #FF6B35 (CTAs, highlights)

### **Score Colors**
- **Excellent (80-100)**: Green (#4CAF50) or Orange (#FF6B35)
- **Good (60-79)**: Blue (#13294B)
- **Moderate (40-59)**: Yellow (#FFC107)
- **Low (0-39)**: Gray (#9E9E9E)

### **Sub-Score Colors**
- **Topic Match**: Blue (#13294B)
- **Method Match**: Orange (#FF6B35)
- **Career Stage**: Green (#4CAF50)

---

## ✅ **IMPLEMENTATION NOTES**

### **Accessibility**
- Color-blind friendly: Use both color and thickness/pattern
- Keyboard navigation support
- Screen reader labels for all interactive elements
- Minimum touch target: 44px × 44px

### **Performance**
- Lazy load network graph (load on demand)
- Virtual scrolling for long result lists
- Debounce search input (300ms delay)
- Cache score calculations

### **Responsive Breakpoints**
- **Desktop**: >1024px (3-column grid)
- **Tablet**: 768px-1024px (2-column grid)
- **Mobile**: <768px (single column)

---

**These wireframes provide complete visual specifications for implementation and presentation.**


