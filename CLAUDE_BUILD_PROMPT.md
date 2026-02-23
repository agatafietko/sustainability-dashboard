# Claude Build Prompt - Collaboration Platform Website

## 🎯 **Copy this entire prompt and give it to Claude**

---

# Build a Research Collaboration Platform Website

I need you to build a modern, professional website for a research collaboration platform called "Join Us!" for the GIES Business School at University of Illinois. This will be used in a case competition.

## **Website Requirements:**

### **1. Landing Page / Hero Section**

Create an engaging hero section with:
- **Headline**: "Find Your Research Match" or "Connect. Collaborate. Impact."
- **Subheadline**: "Connect with researchers working on sustainability challenges. Find projects that match your interests. Make an impact."
- **Two CTA buttons**: 
  - Primary: "Find Opportunities" (Orange #FF6B35)
  - Secondary: "Join as Researcher" (White with blue text)
- **Design**: Modern gradient background using Illinois Blue (#13294B) and Orange (#FF6B35)
- **Style**: Clean, professional, engaging

### **2. "How It Works" Section**

Create a 3-step visual guide:
- **Step 1**: Take Survey (icon/number: 1)
- **Step 2**: Get Matched (icon/number: 2)
- **Step 3**: Connect (icon/number: 3)
- Each step has: Number badge, title, brief description
- Layout: 3 columns, responsive grid

### **3. Survey Section**

- **Title**: "Find Your Research Match"
- **Embed Google Form**: Placeholder for iframe embed
- **Instructions**: "Take our quick survey to discover research opportunities that align with your interests"
- Design: Centered, clean, professional

### **4. Research Opportunity Board**

Create an interactive opportunity board with:

**Features:**
- **Search bar**: Full-text search
- **Filters**: 
  - SDG dropdown (all 17 SDGs)
  - Department dropdown (Business Administration, Finance, Accountancy, Gies Affiliates)
- **Opportunity cards** (grid layout):
  - SDG badges (visual icons/badges)
  - Research title
  - Researcher name and department
  - Keyword tags
  - Publication year
  - Match score (if available)
  - Two buttons: "Learn More" and "Contact Researcher"

**Sample Data Structure** (use this format):
```javascript
const opportunities = [
  {
    id: 1,
    title: "AI for Cancer Diagnosis: Bias-Aware Classification",
    researcher: "Dr. Mehmet Ahsen",
    department: "Business Administration",
    email: "ahsen@illinois.edu",
    sdgs: [3],
    keywords: ["AI", "Healthcare", "Machine Learning", "Breast Cancer"],
    year: 2019,
    matchScore: 85
  },
  {
    id: 2,
    title: "CEO Risk Preference and R&D Investment",
    researcher: "Dr. A. Rashad Abdel-Khalik",
    department: "Accountancy",
    email: "rashad@illinois.edu",
    sdgs: [8],
    keywords: ["Finance", "Risk Management", "R&D", "Corporate Governance"],
    year: 2014,
    matchScore: null
  }
  // Add 10-15 more sample opportunities
];
```

**Card Design:**
- White background, subtle shadow
- Hover effect (lift up slightly)
- SDG badges: Small, colored badges (blue/orange theme)
- Keyword tags: Light gray background, rounded
- Match score: Orange color, bold
- Buttons: Blue for "Learn More", Orange for "Contact"

**Functionality:**
- Search filters cards in real-time
- SDG filter filters by SDG number
- Department filter filters by department
- Cards update dynamically

### **5. Statistics Section**

Create a stats dashboard showing:
- **4 KPI cards** in a grid:
  - Total Publications: 1,899
  - Sustainable Research: 397
  - Sustainable %: 21%
  - SDGs Covered: 15
- **Design**: Dark blue gradient cards, large numbers, clean labels
- **Style**: Professional, prominent

### **6. Contact Modal**

Create a modal that opens when "Contact Researcher" is clicked:
- **Form fields**:
  - Name (text input)
  - Email (email input)
  - Role (text input: Student/Faculty/etc.)
  - Message (textarea)
- **Buttons**: "Send Message" (primary) and close (X)
- **Functionality**: 
  - Opens when contact button clicked
  - Closes when X clicked or outside modal clicked
  - Form submission shows alert (demo mode)

### **7. Header Navigation**

- **Logo**: "GIES Research" or similar
- **Navigation links**: Home, Opportunities, Dashboard, About
- **Style**: Sticky header, Illinois Blue background, white text

### **8. Footer**

- Simple footer with copyright: "© 2024 GIES Business School - University of Illinois"
- Illinois Blue background, white text

## **Design Specifications:**

### **Color Palette:**
- **Primary Blue**: #13294B (Illinois Blue)
- **Orange Accent**: #FF6B35 (Illinois Orange)
- **White**: #FFFFFF
- **Light Gray**: #F5F5F5
- **Dark Gray**: #333333 (text)

### **Typography:**
- **Font Family**: Arial, sans-serif (or system fonts)
- **Headings**: Bold, large (36-56px)
- **Body**: Regular, readable (16-18px)

### **Layout:**
- **Max width**: 1200px
- **Padding**: 20px on mobile, auto margins on desktop
- **Grid**: Responsive grid for cards (3 columns desktop, 2 tablet, 1 mobile)
- **Spacing**: Generous white space

### **Responsive Design:**
- **Desktop**: Full layout, 3-column grids
- **Tablet**: 2-column grids, adjusted spacing
- **Mobile**: Single column, stacked layout, touch-friendly buttons

## **Technical Requirements:**

1. **HTML**: Semantic, clean structure
2. **CSS**: Modern, responsive, use CSS Grid/Flexbox
3. **JavaScript**: 
   - Filter/search functionality
   - Modal open/close
   - Dynamic card generation
   - Smooth scrolling
4. **No external dependencies**: Use vanilla JavaScript (no frameworks required)
5. **Performance**: Fast loading, optimized

## **Features to Implement:**

✅ Search bar filters opportunities  
✅ SDG dropdown filter  
✅ Department dropdown filter  
✅ Opportunity cards display with all info  
✅ Contact modal opens/closes  
✅ Smooth scrolling navigation  
✅ Mobile responsive  
✅ Hover effects on cards  
✅ Professional styling

## **Sample Opportunities to Include:**

Add at least 15-20 sample opportunities from research publications. Include variety:
- Different departments
- Different SDGs (focus on SDG 3, 8, 10, 16 which are strong in the data)
- Different years (2010-2020)
- Various keywords (AI, Healthcare, Finance, Sustainability, etc.)

## **Additional Notes:**

- Make it look modern and professional (better than typical university sites)
- Use smooth transitions and hover effects
- Ensure accessibility (good contrast, readable fonts)
- Test all functionality works
- Make sure it's polished and ready for case competition presentation

## **Output Requirements:**

Provide:
1. Complete HTML file (single file with embedded CSS and JavaScript, or separate files)
2. Instructions on how to:
   - Replace Google Form embed URL
   - Update opportunity data
   - Customize colors/content
   - Deploy to hosting

---

**Build this website with all the features above. Make it production-ready and professional!**



