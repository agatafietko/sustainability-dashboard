# GIES Dashboard - Professional Design Guide

## 🎨 **Design Principles for GIES Dashboard**

### Color Scheme (University of Illinois)
- **Primary Blue**: #13294B (Illinois Blue) or #1E3A8A
- **Orange Accent**: #FF6B35 or #F77F00 (Illinois Orange)
- **White**: #FFFFFF (backgrounds)
- **Light Gray**: #F5F5F5 (subtle backgrounds)
- **Dark Gray**: #333333 (text)

---

## 📊 **Card Visuals - Professional Formatting**

### Step 1: Format All 4 Cards Consistently

**For "Total Publications" Card (Blue):**

1. **Select the card**
2. **Format pane** → **"Effects"** section
   - **Background**: ON
   - **Color**: Illinois Blue (#13294B or similar dark blue)
   - **Transparency**: 0%
3. **Format pane** → **"Visual border"** section
   - **Visual border**: ON
   - **Color**: Lighter blue (#1E3A8A) or white
   - **Width**: 2-3 px
   - **Rounded corners**: 8-10 px
4. **Format pane** → **"Values"** section
   - **Font family**: Arial or Segoe UI
   - **Font size**: 48-56 (large, prominent)
   - **Font color**: White
   - **Font style**: Bold
5. **Format pane** → **"Title"** section
   - **Title**: ON
   - **Title text**: "Total Publications"
   - **Font size**: 14-16
   - **Font color**: White or light gray
   - **Position**: Above value

**For Other 3 Cards (White Background):**

1. **Background**: White or light gray (#F5F5F5)
2. **Visual border**: ON
   - **Color**: Illinois Blue (#13294B)
   - **Width**: 2 px
   - **Rounded corners**: 8 px
3. **Values**:
   - **Font size**: 48-56
   - **Font color**: Dark blue (#13294B) or dark gray
   - **Font style**: Bold
4. **Title**:
   - **Font size**: 14-16
   - **Font color**: Dark gray
   - **Position**: Above value

**For "Sustainable %" Card:**
- Format as percentage (see FORMAT_PERCENTAGE.md)
- Show as **20.90%** or **21%**

---

## 📈 **Line Chart - Professional Formatting**

### Format "Publications by Year" Chart:

1. **Select the line chart**
2. **Format pane** → **"General"** section
   - **Title**: ON
   - **Title text**: "Publications Over Time"
   - **Font size**: 18
   - **Font color**: Dark blue (#13294B)
   - **Position**: Above chart
3. **Format pane** → **"Visual"** → **"Effects"** section
   - **Background**: Light gray (#F5F5F5) or white
   - **Visual border**: ON
   - **Color**: Light gray or blue
   - **Width**: 1 px
   - **Rounded corners**: 4 px
4. **Format pane** → **"Y-axis"** section
   - **Font size**: 12
   - **Font color**: Dark gray
   - **Title**: "Number of Publications"
5. **Format pane** → **"X-axis"** section
   - **Font size**: 12
   - **Font color**: Dark gray
   - **Title**: "Year"
6. **Format pane** → **"Data colors"** section
   - **Line color**: Illinois Blue (#13294B) or Orange (#FF6B35)
   - **Line width**: 3 px
   - **Markers**: ON (optional, for data points)

---

## 📊 **Bar Chart - Professional Formatting**

### Format "Sustainable by Department" Chart:

1. **Select the bar chart**
2. **Format pane** → **"General"** section
   - **Title**: ON
   - **Title text**: "Sustainable Research by Department"
   - **Font size**: 18
   - **Font color**: Dark blue (#13294B)
3. **Format pane** → **"Visual"** → **"Effects"** section
   - **Background**: White or light gray
   - **Visual border**: ON
   - **Color**: Light gray
   - **Width**: 1 px
   - **Rounded corners**: 4 px
4. **Format pane** → **"Data colors"** section
   - **Color**: Illinois Orange (#FF6B35) or Blue (#13294B)
   - **Gradient**: OFF (solid color)
5. **Format pane** → **"Y-axis"** section
   - **Font size**: 12
   - **Font color**: Dark gray
6. **Format pane** → **"X-axis"** section
   - **Font size**: 12
   - **Font color**: Dark gray
   - **Title**: "Number of Publications"
7. **Format pane** → **"Data labels"** section
   - **Data labels**: ON
   - **Position**: End (outside bars)
   - **Font size**: 11
   - **Font color**: Dark gray

---

## 🎯 **Overall Dashboard Layout**

### Recommended Layout:

```
┌─────────────────────────────────────────────────────────┐
│  [Card]      [Card]      [Card]      [Card]           │
│  Total       Sust.       %            Recent           │
│  (Blue)      (White)    (White)      (White)          │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  [Line Chart]              [Bar Chart]                 │
│  Publications Over Time    Sustainable by Department   │
│                                                         │
│  [Slicers]                                              │
│  Department | Year | SDG                               │
└─────────────────────────────────────────────────────────┘
```

### Spacing:
- **Cards**: Even spacing, aligned top row
- **Charts**: Side by side, same height
- **Slicers**: Below charts or left sidebar
- **Padding**: 10-15 px between visuals

---

## 🎨 **Color Palette for GIES Dashboard**

### Primary Colors:
- **Illinois Blue**: #13294B (dark blue)
- **Illinois Orange**: #FF6B35 (accent)
- **White**: #FFFFFF

### Secondary Colors:
- **Light Blue**: #E3F2FD (light backgrounds)
- **Light Orange**: #FFF3E0 (highlights)
- **Dark Gray**: #333333 (text)
- **Light Gray**: #F5F5F5 (subtle backgrounds)

### Usage:
- **Blue**: Primary cards, borders, titles
- **Orange**: Accent bars, highlights, callouts
- **White/Gray**: Backgrounds, subtle elements

---

## ✨ **Professional Touches**

### 1. Consistent Fonts
- **Titles**: Arial Bold, 18-20 pt
- **Card Values**: Arial Bold, 48-56 pt
- **Labels**: Arial Regular, 12 pt
- **Body Text**: Arial Regular, 11-14 pt

### 2. Rounded Corners
- **Cards**: 8-10 px
- **Charts**: 4-6 px
- **Consistent across all visuals**

### 3. Shadows (Optional)
- **Format pane** → **"Effects"** → **"Shadow"**
- **Shadow**: ON
- **Blur**: 5-8 px
- **Transparency**: 20-30%
- **Offset**: 2-3 px
- **Color**: Black or dark gray

### 4. Grid Lines (Charts)
- **Format pane** → **"Gridlines"** section
- **Horizontal**: ON (subtle)
- **Color**: Light gray (#E0E0E0)
- **Width**: 1 px
- **Style**: Dashed (optional)

---

## 📋 **Step-by-Step: Format Your Current Dashboard**

### Step 1: Format Total Publications Card (Blue)

1. **Select** the "Total Publications" card
2. **Format pane** → **"Effects"**:
   - Background: ON, Color: #13294B (dark blue)
3. **Format pane** → **"Values"**:
   - Font size: 56, Color: White, Style: Bold
4. **Format pane** → **"Title"**:
   - Title: ON, Text: "Total Publications", Color: White
5. **Format pane** → **"Visual border"**:
   - Border: ON, Color: White, Width: 2 px, Rounded: 8 px

### Step 2: Format Other 3 Cards (White)

1. **Select** each card (Sustainable Publications, %, Recent)
2. **Format pane** → **"Effects"**:
   - Background: White or #F5F5F5
3. **Format pane** → **"Values"**:
   - Font size: 56, Color: #13294B, Style: Bold
4. **Format pane** → **"Visual border"**:
   - Border: ON, Color: #13294B, Width: 2 px, Rounded: 8 px

### Step 3: Format Line Chart

1. **Select** line chart
2. **Format pane** → **"General"**:
   - Title: ON, Text: "Publications Over Time", Size: 18
3. **Format pane** → **"Data colors"**:
   - Line color: #13294B (blue) or #FF6B35 (orange)
   - Line width: 3 px
4. **Format pane** → **"Effects"**:
   - Background: White, Border: ON, Rounded: 4 px

### Step 4: Format Bar Chart

1. **Select** bar chart
2. **Format pane** → **"General"**:
   - Title: ON, Text: "Sustainable Research by Department", Size: 18
3. **Format pane** → **"Data colors"**:
   - Color: #FF6B35 (orange) or #13294B (blue)
4. **Format pane** → **"Data labels"**:
   - Data labels: ON, Position: End
5. **Format pane** → **"Effects"**:
   - Background: White, Border: ON, Rounded: 4 px

---

## 🎯 **Quick Design Checklist**

- [ ] All cards have consistent styling
- [ ] Total Publications card is blue with white text
- [ ] Other cards are white with blue text/borders
- [ ] All visuals have titles (ON, 18 pt font)
- [ ] Charts have subtle borders (1-2 px, rounded corners)
- [ ] Colors use Illinois Blue (#13294B) and Orange (#FF6B35)
- [ ] Fonts are consistent (Arial, appropriate sizes)
- [ ] Spacing is even between visuals
- [ ] Data labels are readable (if enabled)
- [ ] Dashboard looks clean and professional

---

## 💡 **Pro Tips for GIES Dashboard**

1. **Brand Consistency**: Use Illinois colors throughout
2. **Visual Hierarchy**: Largest numbers (cards) at top, details below
3. **White Space**: Don't overcrowd - leave breathing room
4. **Readability**: Ensure text contrasts well with backgrounds
5. **Professional Look**: Clean lines, consistent spacing, organized layout

---

## 🎨 **Advanced: Add GIES Logo/Header**

If you want to add a header:

1. **Insert** → **"Text box"** or **"Image"**
2. Add GIES logo (if available)
3. Add title: "GIES Business Analytics Dashboard"
4. Format: Dark blue background, white text
5. Position: Top of page

---

**Follow these steps and your GIES dashboard will look professional and polished!** 🎉

The key is consistency - use the same colors, fonts, and styling across all visuals!





