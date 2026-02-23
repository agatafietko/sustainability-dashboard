# Phase 2 Implementation Guide - Medium Effort Features

## 🎯 **Phase 2 Features to Build**

1. **Predictive Trends Dashboard**
2. **Actionable Insights Panel**
3. **Real-Time Activity Feed**

---

## 📈 **Feature 1: Predictive Trends Dashboard**

### **Purpose**: Forecast future research directions and trends

### **Step 1: Create Trend Analysis Measures**

**Measure 1: Year-over-Year Growth**
```DAX
YoY Growth = 
VAR CurrentYear = SELECTEDVALUE(Publications[publication_year])
VAR PreviousYear = CurrentYear - 1
VAR CurrentCount = 
    CALCULATE(
        [Total Publications],
        Publications[publication_year] = CurrentYear
    )
VAR PreviousCount = 
    CALCULATE(
        [Total Publications],
        Publications[publication_year] = PreviousYear
    )
RETURN
IF(
    PreviousCount > 0,
    DIVIDE(CurrentCount - PreviousCount, PreviousCount, 0) * 100,
    BLANK()
)
```

**Measure 2: Average Growth Rate**
```DAX
Average Growth Rate = 
VAR Years = DISTINCTCOUNT(Publications[publication_year])
VAR FirstYear = MIN(Publications[publication_year])
VAR LastYear = MAX(Publications[publication_year])
VAR FirstYearCount = 
    CALCULATE(
        [Total Publications],
        Publications[publication_year] = FirstYear
    )
VAR LastYearCount = 
    CALCULATE(
        [Total Publications],
        Publications[publication_year] = LastYear
    )
RETURN
IF(
    FirstYearCount > 0 && Years > 1,
    POWER(
        DIVIDE(LastYearCount, FirstYearCount, 1),
        DIVIDE(1, Years - 1, 1)
    ) - 1,
    BLANK()
) * 100
```

**Measure 3: Forecasted Publications (Next 3 Years)**
```DAX
Forecasted Publications = 
VAR AvgGrowth = [Average Growth Rate] / 100
VAR LastYear = MAX(Publications[publication_year])
VAR LastYearCount = 
    CALCULATE(
        [Total Publications],
        Publications[publication_year] = LastYear
    )
VAR YearsAhead = 3
RETURN
LastYearCount * POWER(1 + AvgGrowth, YearsAhead)
```

### **Step 2: Create Forecast Line Chart**

1. **Click Line chart visual**
2. **X-axis**: Drag `publication_year`
3. **Y-axis**: 
   - `Total Publications` measure (historical)
   - `Forecasted Publications` measure (forecast)

4. **Add Analytics (Forecast)**:
   - **Format pane** → **"Analytics"** section
   - **Forecast**: ON
   - **Forecast length**: 3 years
   - **Confidence interval**: 95%
   - **Style**: Dashed line for forecast

5. **Format Chart**:
   - **Title**: "Research Trends & 3-Year Forecast"
   - **Font size**: 18
   - **Historical line**: Solid, Blue (#13294B)
   - **Forecast line**: Dashed, Orange (#FF6B35)
   - **Confidence band**: Light gray, semi-transparent

### **Step 3: Create SDG Trend Forecast**

**Measure: Forecast by SDG**
```DAX
Forecast by SDG = 
VAR SelectedSDG = SELECTEDVALUE('sdg_lookup'[SDG ID])
VAR SDGData = 
    FILTER(
        ALL(Publications[publication_year]),
        CALCULATE(
            COUNTROWS('SDG_Mappings'),
            'SDG_Mappings'[SDG ID] = SelectedSDG
        ) > 0
    )
VAR AvgGrowth = [Average Growth Rate] / 100
VAR LastYear = MAX(Publications[publication_year])
VAR LastYearCount = 
    CALCULATE(
        COUNTROWS('SDG_Mappings'),
        'SDG_Mappings'[SDG ID] = SelectedSDG,
        Publications[publication_year] = LastYear
    )
VAR YearsAhead = 3
RETURN
IF(
    NOT ISBLANK(SelectedSDG),
    LastYearCount * POWER(1 + AvgGrowth, YearsAhead),
    BLANK()
)
```

**Create Streamgraph/Area Chart:**

1. **Click Area chart** (or install Streamgraph custom visual)
2. **X-axis**: `publication_year`
3. **Legend**: `SDG Name` (from sdg_lookup)
4. **Values**: `Total Publications` (filtered by SDG)
5. **Add forecast**: Extend to future years with forecasted values

6. **Format**:
   - **Title**: "SDG Research Trends & Forecast"
   - **Colors**: Different color for each SDG
   - **Forecast area**: Semi-transparent, different pattern

### **Step 4: Create Emerging Trends Detection**

**Measure: Emerging Trend Indicator**
```DAX
Emerging Trend = 
VAR CurrentYear = MAX(Publications[publication_year])
VAR Recent3Years = 
    CALCULATE(
        [Total Publications],
        Publications[publication_year] >= CurrentYear - 2
    )
VAR Previous3Years = 
    CALCULATE(
        [Total Publications],
        Publications[publication_year] >= CurrentYear - 5 &&
        Publications[publication_year] < CurrentYear - 2
    )
VAR GrowthRate = DIVIDE(Recent3Years - Previous3Years, Previous3Years, 0)
RETURN
SWITCH(
    TRUE(),
    GrowthRate > 0.3, "Rapidly Growing",
    GrowthRate > 0.15, "Growing",
    GrowthRate > 0, "Stable Growth",
    "Declining"
)
```

**Create Emerging Trends Table:**

1. **Click Table visual**
2. **Columns**:
   - `SDG Name`
   - `Emerging Trend` measure
   - `YoY Growth` measure
   - `Forecast by SDG` measure

3. **Format**:
   - **Conditional formatting** for Emerging Trend column:
     - "Rapidly Growing": Green
     - "Growing": Light green
     - "Stable Growth": Yellow
     - "Declining": Red
   - **Sort**: By YoY Growth (descending)

4. **Title**: "Emerging Research Trends by SDG"

### **Step 5: Create Forecast Summary Cards**

**Create cards showing:**
- **3-Year Forecast**: Total publications predicted
- **Growth Rate**: Average annual growth
- **Top Growing SDG**: SDG with highest growth
- **Trend Direction**: Overall trend (up/down)

---

## 💡 **Feature 2: Actionable Insights Panel**

### **Purpose**: AI-generated recommendations based on data analysis

### **Step 1: Create Insight Generation Measures**

**Insight 1: SDG Opportunity**
```DAX
SDG Opportunity Insight = 
VAR LowCoverageSDGs = 
    CALCULATE(
        COUNTROWS('sdg_lookup'),
        FILTER(
            ALL('sdg_lookup'),
            [SDG Coverage by SDG] < 5
        )
    )
RETURN
IF(
    LowCoverageSDGs > 0,
    "Opportunity: " & LowCoverageSDGs & " SDGs have low coverage. Consider strategic investment in these areas.",
    "All SDGs have adequate coverage."
)
```

**Insight 2: Department Growth**
```DAX
Department Growth Insight = 
VAR TopDept = 
    TOPN(
        1,
        VALUES(Publications[department]),
        [Sustainable by Department],
        DESC
    )
VAR TopDeptName = SELECTEDVALUE(Publications[department])
VAR TopDeptCount = [Sustainable by Department]
RETURN
"Top Performer: " & TopDeptName & " leads with " & TopDeptCount & " sustainable publications. Consider replicating their success model."
```

**Insight 3: Collaboration Opportunity**
```DAX
Collaboration Insight = 
VAR IsolatedDepts = 
    CALCULATE(
        COUNTROWS(DISTINCT(Publications[department])),
        FILTER(
            ALL(Publications),
            [Department Connectivity] < 3
        )
    )
RETURN
IF(
    IsolatedDepts > 0,
    "Collaboration Opportunity: " & IsolatedDepts & " departments have limited SDG connections. Encourage cross-department collaboration.",
    "Strong collaboration network across departments."
)
```

**Insight 4: Trend Alert**
```DAX
Trend Alert Insight = 
VAR RecentGrowth = 
    CALCULATE(
        [YoY Growth],
        Publications[publication_year] = MAX(Publications[publication_year])
    )
RETURN
IF(
    RecentGrowth > 15,
    "Strong Growth: Publications increased " & FORMAT(RecentGrowth, "0.0") & "% last year. Maintain momentum.",
    IF(
        RecentGrowth < 0,
        "Attention Needed: Publications declined " & FORMAT(ABS(RecentGrowth), "0.0") & "% last year. Review strategy.",
        "Stable Growth: Maintain current research output."
    )
)
```

**Insight 5: Impact Score Alert**
```DAX
Impact Score Insight = 
VAR AvgImpact = AVERAGEX(Publications, [Research Impact Score])
RETURN
IF(
    AvgImpact < 50,
    "Improvement Opportunity: Average impact score is " & FORMAT(AvgImpact, "0.0") & ". Focus on top-tier journals and SDG alignment.",
    "Strong Impact: Average impact score is " & FORMAT(AvgImpact, "0.0") & ". Maintain quality standards."
)
```

### **Step 2: Create Insights Panel Visual**

**Option A: Card-Based Insights**

1. **Create multiple Card visuals** (one for each insight)
2. **Each card shows**:
   - Insight title (e.g., "SDG Opportunity")
   - Insight text (from measure)
   - Priority indicator (color-coded)

3. **Format cards**:
   - **Background**: Light blue or light orange
   - **Border**: Colored based on priority
   - **Font**: Readable, 12-14pt
   - **Layout**: Stacked vertically or in grid

**Option B: Table-Based Insights**

1. **Click Table visual**
2. **Columns**:
   - **Priority** (calculated column: High/Medium/Low)
   - **Category** (SDG, Department, Collaboration, etc.)
   - **Insight Text** (from measures)
   - **Action** (suggested action)

3. **Format**:
   - **Conditional formatting** for Priority
   - **Sort**: By Priority (High first)
   - **Filter**: Show top 5-10 insights

4. **Title**: "Actionable Insights & Recommendations"

### **Step 3: Create Dynamic Insights**

**Create measure that combines all insights:**
```DAX
All Insights = 
VAR SDGInsight = [SDG Opportunity Insight]
VAR DeptInsight = [Department Growth Insight]
VAR CollabInsight = [Collaboration Insight]
VAR TrendInsight = [Trend Alert Insight]
VAR ImpactInsight = [Impact Score Insight]
RETURN
SDGInsight & UNICHAR(10) & UNICHAR(10) &
DeptInsight & UNICHAR(10) & UNICHAR(10) &
CollabInsight & UNICHAR(10) & UNICHAR(10) &
TrendInsight & UNICHAR(10) & UNICHAR(10) &
ImpactInsight
```

**Use in a large text box or card**

### **Step 4: Create Priority-Based Insights**

**Create priority scoring:**
```DAX
Insight Priority = 
VAR SDGCoverage = [SDG Coverage by SDG]
VAR Growth = [YoY Growth]
VAR Impact = [Research Impact Score]
RETURN
SWITCH(
    TRUE(),
    SDGCoverage < 2 || Growth < -10 || Impact < 40, "High",
    SDGCoverage < 5 || Growth < 0 || Impact < 50, "Medium",
    "Low"
)
```

**Format insights by priority:**
- **High Priority**: Red border, bold text
- **Medium Priority**: Yellow border, regular text
- **Low Priority**: Green border, light text

---

## 📱 **Feature 3: Real-Time Activity Feed**

### **Purpose**: Show live updates on research activity

### **Step 1: Create Activity Measures**

**Measure: Recent Activity Count**
```DAX
Recent Activity = 
CALCULATE(
    [Total Publications],
    Publications[publication_year] >= YEAR(TODAY()) - 1
)
```

**Measure: New This Month** (if you have date data)
```DAX
New This Month = 
CALCULATE(
    [Total Publications],
    FILTER(
        ALL(Publications),
        YEAR(Publications[publication_year]) = YEAR(TODAY()) &&
        MONTH(Publications[publication_year]) = MONTH(TODAY())
    )
)
```

**Measure: Activity Status**
```DAX
Activity Status = 
VAR Recent = [Recent Activity]
VAR Total = [Total Publications]
VAR PercentRecent = DIVIDE(Recent, Total, 0) * 100
RETURN
SWITCH(
    TRUE(),
    PercentRecent > 20, "Highly Active",
    PercentRecent > 10, "Active",
    "Moderate Activity"
)
```

### **Step 2: Create Activity Feed Table**

1. **Click Table visual**
2. **Columns**:
   - `publication_year`
   - `title`
   - `name` (author)
   - `department`
   - `SDG Name` (from relationship)
   - `is_sustain` (as icon)

3. **Filter**:
   - Show only recent publications (last 2-3 years)
   - Sort by year (newest first)

4. **Format**:
   - **Conditional formatting** for is_sustain (green icon if sustainable)
   - **Compact layout**
   - **Row highlighting** on hover

5. **Title**: "Recent Research Activity"

### **Step 3: Create Activity Summary Cards**

**Create cards showing:**
- **Recent Publications**: Count from last year
- **New This Year**: Count from current year
- **Activity Status**: Text indicator
- **Last Updated**: Timestamp (if available)

### **Step 4: Create Activity Timeline**

1. **Click Line chart or Area chart**
2. **X-axis**: `publication_year`
3. **Y-axis**: `Total Publications` (cumulative or by year)
4. **Format**:
   - **Title**: "Research Activity Timeline"
   - **Markers**: ON (show data points)
   - **Highlight**: Recent years in different color

### **Step 5: Create Activity Notifications**

**Create measure for notifications:**
```DAX
Activity Notification = 
VAR RecentCount = [Recent Activity]
VAR AvgPerYear = DIVIDE([Total Publications], DISTINCTCOUNT(Publications[publication_year]), 0)
RETURN
IF(
    RecentCount > AvgPerYear * 1.2,
    "📈 Above Average Activity: " & RecentCount & " publications in last year",
    IF(
        RecentCount < AvgPerYear * 0.8,
        "📉 Below Average Activity: " & RecentCount & " publications in last year",
        "✅ Normal Activity: " & RecentCount & " publications in last year"
    )
)
```

**Display in a card or text box**

### **Step 6: Create Milestone Alerts**

**Create measures for milestones:**
```DAX
Milestone Alert = 
VAR Total = [Total Publications]
VAR Sustainable = [Sustainable Publications]
RETURN
SWITCH(
    TRUE(),
    Total >= 2000, "🎉 Milestone: Reached 2,000 total publications!",
    Total >= 1500, "Approaching milestone: " & 2000 - Total & " publications until 2,000",
    Sustainable >= 400, "🎉 Milestone: Reached 400 sustainable publications!",
    Sustainable >= 350, "Approaching milestone: " & 400 - Sustainable & " until 400 sustainable",
    "Continue building research portfolio"
)
```

**Display in prominent card or banner**

---

## 📋 **Complete Phase 2 Dashboard Structure**

### **New Page: "Predictive Analytics & Insights"**

**Layout:**

```
Row 1: [Forecast Summary Cards]
       3-Year Forecast | Growth Rate | Top Growing SDG

Row 2: [Trend Forecast Chart - Full Width]
       Historical + Forecasted trends

Row 3: [SDG Trend Streamgraph - Full Width]
       SDG trends over time with forecast

Row 4: [Emerging Trends Table]
       Top growing/declining SDGs

Row 5: [Actionable Insights Panel - Full Width]
       Card-based or table-based insights

Row 6: [Activity Feed Section]
       Recent Activity Cards | Activity Timeline

Row 7: [Activity Feed Table]
       Recent publications list
```

---

## ✅ **Phase 2 Implementation Checklist**

### **Predictive Trends Dashboard:**
- [ ] Created YoY Growth measure
- [ ] Created Average Growth Rate measure
- [ ] Created Forecasted Publications measure
- [ ] Created forecast line chart with analytics
- [ ] Created SDG trend forecast
- [ ] Created streamgraph/area chart with forecast
- [ ] Created Emerging Trend indicator measure
- [ ] Created emerging trends table
- [ ] Created forecast summary cards
- [ ] Formatted all visuals with titles

### **Actionable Insights Panel:**
- [ ] Created SDG Opportunity Insight measure
- [ ] Created Department Growth Insight measure
- [ ] Created Collaboration Insight measure
- [ ] Created Trend Alert Insight measure
- [ ] Created Impact Score Insight measure
- [ ] Created All Insights combined measure
- [ ] Created Insight Priority measure
- [ ] Created insights panel (cards or table)
- [ ] Applied priority-based formatting
- [ ] Tested insights update with filters

### **Real-Time Activity Feed:**
- [ ] Created Recent Activity measure
- [ ] Created Activity Status measure
- [ ] Created Activity Notification measure
- [ ] Created Milestone Alert measure
- [ ] Created activity feed table
- [ ] Created activity summary cards
- [ ] Created activity timeline chart
- [ ] Added milestone alerts
- [ ] Formatted all activity visuals

### **Overall:**
- [ ] Created new page "Predictive Analytics & Insights"
- [ ] Arranged all visuals in logical layout
- [ ] Applied consistent formatting
- [ ] Tested all measures calculate correctly
- [ ] Verified forecasts display properly
- [ ] Tested insights update dynamically

---

## 🎯 **Quick Start Steps**

1. **Create new page**: Click "+" → Rename to "Predictive Analytics & Insights"
2. **Start with Forecasts**: Build trend forecast chart first
3. **Add Insights**: Create insight measures, build insights panel
4. **Build Activity Feed**: Create activity table and cards
5. **Format everything**: Add titles, colors, consistent styling
6. **Test**: Verify forecasts work, insights update, activity shows correctly

---

## 💡 **Pro Tips**

1. **Forecast Accuracy**: Use historical data (at least 3-5 years) for better forecasts
2. **Insight Refresh**: Insights should update when filters change
3. **Activity Timing**: If you have actual dates, use them; otherwise use publication_year
4. **Visual Hierarchy**: Make high-priority insights more prominent
5. **Testing**: Test with different filter combinations to ensure insights are relevant

---

## 🔧 **Advanced Enhancements**

### **For Forecasts:**
- Add confidence intervals
- Show multiple scenarios (optimistic, realistic, pessimistic)
- Compare forecast to actual when new data arrives

### **For Insights:**
- Add "Dismiss" functionality (if building custom)
- Categorize insights (Strategic, Operational, Tactical)
- Link insights to specific actions/dashboards

### **For Activity:**
- Add real-time updates (if data source supports it)
- Show activity by department/SDG
- Add activity trends (increasing/decreasing)

---

**Follow these steps to build all Phase 2 features! Start with Predictive Trends, then Insights, then Activity Feed.** 🎉

Need help with any specific step? Let me know which feature you're working on!




