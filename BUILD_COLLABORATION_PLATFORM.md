# Step-by-Step: Build Collaboration Platform for Case Competition

## 🎯 **Overview**

This guide walks you through building the "Join Us!" collaboration platform from scratch. We'll use a combination of tools to get it done quickly for your case competition.

---

## 📋 **Phase 1: Create the Survey (30 minutes)**

### **Step 1: Set Up Google Form**

1. **Go to**: https://forms.google.com
2. **Create new form**: Click "+" or "Blank"
3. **Title**: "Find Your Research Match - GIES Collaboration Platform"

### **Step 2: Add Survey Sections**

#### **Section 1: Basic Information**

**Question 1: Name**
- Type: Short answer
- Required: Yes

**Question 2: Email**
- Type: Short answer
- Validation: Email
- Required: Yes

**Question 3: Role**
- Type: Multiple choice
- Options:
  - Undergraduate Student
  - Graduate Student
  - Faculty Member
  - Researcher
  - External Partner
  - Other
- Required: Yes

**Question 4: Department/Program**
- Type: Short answer
- Required: Yes

**Question 5: Year (if student)**
- Type: Dropdown
- Options: Freshman, Sophomore, Junior, Senior, Graduate Year 1, Graduate Year 2, PhD
- Required: No

#### **Section 2: Research Interests**

**Question 6: SDG Focus**
- Type: Checkboxes
- Title: "Which Sustainable Development Goals (SDGs) interest you? (Select all that apply)"
- Options:
  - [ ] SDG 1: No Poverty
  - [ ] SDG 2: Zero Hunger
  - [ ] SDG 3: Good Health & Well-Being
  - [ ] SDG 4: Quality Education
  - [ ] SDG 5: Gender Equality
  - [ ] SDG 6: Clean Water and Sanitation
  - [ ] SDG 7: Affordable and Clean Energy
  - [ ] SDG 8: Decent Work and Economic Growth
  - [ ] SDG 9: Industry, Innovation and Infrastructure
  - [ ] SDG 10: Reduced Inequalities
  - [ ] SDG 11: Sustainable Cities and Communities
  - [ ] SDG 12: Responsible Consumption and Production
  - [ ] SDG 13: Climate Action
  - [ ] SDG 14: Life Below Water
  - [ ] SDG 15: Life on Land
  - [ ] SDG 16: Peace, Justice and Strong Institutions
  - [ ] SDG 17: Partnerships for the Goals
- Required: Yes (at least 1)

**Question 7: Research Areas/Keywords**
- Type: Checkboxes
- Title: "What research topics interest you? (Select all that apply)"
- Options:
  - [ ] Artificial Intelligence
  - [ ] Machine Learning
  - [ ] Healthcare
  - [ ] Sustainability
  - [ ] Finance
  - [ ] Data Analytics
  - [ ] Climate Change
  - [ ] Social Impact
  - [ ] Business Strategy
  - [ ] Public Policy
  - [ ] Education
  - [ ] Technology
  - [ ] Other: ________
- Required: Yes (at least 1)

**Question 8: Additional Keywords**
- Type: Short answer
- Title: "Any other research topics or keywords? (Optional)"
- Required: No

#### **Section 3: Skills & Availability**

**Question 9: Research Skills**
- Type: Checkboxes
- Title: "What skills do you have? (Select all that apply)"
- Options:
  - [ ] Quantitative Analysis
  - [ ] Qualitative Research
  - [ ] Data Science
  - [ ] Literature Review
  - [ ] Statistical Analysis
  - [ ] Programming (Python, R, etc.)
  - [ ] Survey Design
  - [ ] Interviewing
  - [ ] Data Visualization
  - [ ] Writing/Editing
  - [ ] Other: ________
- Required: Yes (at least 1)

**Question 10: Time Commitment**
- Type: Multiple choice
- Title: "How many hours per week can you commit?"
- Options:
  - 1-5 hours/week
  - 5-10 hours/week
  - 10-20 hours/week
  - 20+ hours/week
  - Flexible
- Required: Yes

**Question 11: Duration**
- Type: Multiple choice
- Title: "What duration are you looking for?"
- Options:
  - Short-term (1-3 months)
  - Medium-term (3-6 months)
  - Long-term (6+ months)
  - Ongoing
  - Flexible
- Required: Yes

#### **Section 4: Collaboration Preferences**

**Question 12: Looking For**
- Type: Checkboxes
- Title: "What are you looking for?"
- Options:
  - [ ] Research opportunities to join
  - [ ] Research partners/collaborators
  - [ ] Mentorship
  - [ ] All of the above
- Required: Yes

**Question 13: Preferred Collaboration Type**
- Type: Multiple choice
- Title: "How do you prefer to collaborate?"
- Options:
  - In-person
  - Remote
  - Hybrid
  - Flexible
- Required: Yes

### **Step 3: Configure Form Settings**

1. **Settings** (gear icon):
   - **Collect email addresses**: ON
   - **Limit to 1 response**: ON (optional)
   - **Show progress bar**: ON
   - **Shuffle question order**: OFF

2. **Responses** tab:
   - **Create spreadsheet**: Click "Link to Sheets"
   - This creates a Google Sheet to store responses

3. **Get shareable link**:
   - Click "Send" → Copy link
   - Or get embed code for website

### **Step 4: Test the Form**

1. Fill out the form yourself
2. Check responses in Google Sheets
3. Verify all questions work correctly

---

## 📊 **Phase 2: Create Matching System (1-2 hours)**

### **Step 1: Export Dashboard Data**

**From Power BI, export to CSV:**
1. Go to your Publications table
2. Export data (or use Power BI API)
3. You need:
   - `article_uuid`
   - `title`
   - `name` (researcher)
   - `department`
   - `publication_year`
   - `is_sustain`
   - Related SDG IDs (from SDG_Mappings)
   - Related keywords (from Keywords)

**Or create a combined export:**
- Publications with SDG IDs and keywords included

### **Step 2: Create Matching Script**

**Create Python script: `matching_algorithm.py`**

```python
import pandas as pd
import json

# Load survey responses from Google Sheets (export as CSV)
survey_responses = pd.read_csv('survey_responses.csv')

# Load research opportunities from Power BI export
research_opportunities = pd.read_csv('research_opportunities.csv')

def calculate_match_score(user_row, opportunity_row):
    """
    Calculate match score between user and research opportunity
    Returns score 0-100
    """
    score = 0
    
    # 1. SDG Match (40% weight)
    user_sdgs = set(user_row['SDG_Interests'].split(', '))
    opp_sdgs = set(opportunity_row['SDG_IDs'].split(', '))
    sdg_overlap = len(user_sdgs & opp_sdgs)
    max_sdgs = max(len(user_sdgs), len(opp_sdgs), 1)
    sdg_score = (sdg_overlap / max_sdgs) * 40
    score += sdg_score
    
    # 2. Keyword Match (30% weight)
    user_keywords = set(user_row['Research_Areas'].lower().split(', '))
    opp_keywords = set(opportunity_row['Keywords'].lower().split(', '))
    keyword_overlap = len(user_keywords & opp_keywords)
    max_keywords = max(len(user_keywords), len(opp_keywords), 1)
    keyword_score = (keyword_overlap / max_keywords) * 30
    score += keyword_score
    
    # 3. Department Match (20% weight)
    if user_row['Department'] == opportunity_row['Department']:
        score += 20
    elif are_related_departments(user_row['Department'], opportunity_row['Department']):
        score += 10
    
    # 4. Recency Bonus (10% weight)
    current_year = 2024
    pub_year = opportunity_row['Publication_Year']
    if pub_year >= current_year - 2:
        score += 10
    elif pub_year >= current_year - 5:
        score += 5
    
    return min(score, 100)

def find_matches(user_email):
    """
    Find top matches for a user
    """
    user = survey_responses[survey_responses['Email'] == user_email].iloc[0]
    
    matches = []
    for idx, opp in research_opportunities.iterrows():
        match_score = calculate_match_score(user, opp)
        matches.append({
            'title': opp['Title'],
            'researcher': opp['Name'],
            'department': opp['Department'],
            'sdgs': opp['SDG_IDs'],
            'keywords': opp['Keywords'],
            'year': opp['Publication_Year'],
            'match_score': match_score
        })
    
    # Sort by match score, return top 10
    matches.sort(key=lambda x: x['match_score'], reverse=True)
    return matches[:10]

# Example usage
user_email = "student@illinois.edu"
top_matches = find_matches(user_email)
print(json.dumps(top_matches, indent=2))
```

### **Step 3: Process Survey Responses**

**Create script to process Google Sheets data:**

```python
import pandas as pd

# Read Google Sheets export
responses = pd.read_csv('form_responses.csv')

# Clean and structure data
processed_responses = []
for idx, row in responses.iterrows():
    # Extract SDG interests (convert from form response format)
    sdg_interests = []
    for i in range(1, 18):  # SDG 1-17
        if pd.notna(row.get(f'SDG_{i}')):
            sdg_interests.append(i)
    
    processed_responses.append({
        'email': row['Email'],
        'name': row['Name'],
        'role': row['Role'],
        'department': row['Department'],
        'sdg_interests': ', '.join(map(str, sdg_interests)),
        'research_areas': row['Research_Areas'],
        'skills': row['Skills'],
        'time_commitment': row['Time_Commitment'],
        'duration': row['Duration']
    })

# Save processed data
pd.DataFrame(processed_responses).to_csv('processed_responses.csv', index=False)
```

---

## 💻 **Phase 3: Build Website Components (2-3 hours)**

### **Step 1: Create Landing Page Section**

**HTML Structure:**

```html
<section class="join-us-hero">
  <div class="container">
    <h1>Find Your Research Match</h1>
    <p class="subheadline">Connect with researchers working on sustainability challenges. 
    Find projects that match your interests. Make an impact.</p>
    <div class="cta-buttons">
      <a href="#survey" class="btn-primary">Find Opportunities</a>
      <a href="#researcher" class="btn-secondary">Join as Researcher</a>
    </div>
  </div>
</section>
```

**CSS Styling:**

```css
.join-us-hero {
  background: linear-gradient(135deg, #13294B 0%, #FF6B35 100%);
  color: white;
  padding: 80px 20px;
  text-align: center;
}

.join-us-hero h1 {
  font-size: 48px;
  font-weight: bold;
  margin-bottom: 20px;
}

.subheadline {
  font-size: 20px;
  margin-bottom: 40px;
  opacity: 0.9;
}

.cta-buttons {
  display: flex;
  gap: 20px;
  justify-content: center;
}

.btn-primary {
  background: #FF6B35;
  color: white;
  padding: 15px 40px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: bold;
  font-size: 18px;
}

.btn-secondary {
  background: white;
  color: #13294B;
  padding: 15px 40px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: bold;
  font-size: 18px;
}
```

### **Step 2: Embed Google Form**

**Option A: Direct Embed**

```html
<section id="survey" class="survey-section">
  <div class="container">
    <h2>Take Our Survey</h2>
    <p>Help us match you with the perfect research opportunity</p>
    <iframe 
      src="YOUR_GOOGLE_FORM_EMBED_URL" 
      width="100%" 
      height="800" 
      frameborder="0" 
      marginheight="0" 
      marginwidth="0">
      Loading…
    </iframe>
  </div>
</section>
```

**To get embed URL:**
1. Open your Google Form
2. Click "Send" (top right)
3. Click "</>" (embed icon)
4. Copy the iframe code
5. Paste into your website

**Option B: Link to Form**

```html
<section id="survey" class="survey-section">
  <div class="container">
    <h2>Find Your Research Match</h2>
    <p>Take our quick survey to discover research opportunities that align with your interests</p>
    <a href="YOUR_GOOGLE_FORM_LINK" target="_blank" class="btn-primary">
      Start Survey →
    </a>
  </div>
</section>
```

### **Step 3: Create Opportunity Board**

**HTML Structure:**

```html
<section class="opportunities-section">
  <div class="container">
    <h2>Research Opportunities</h2>
    
    <!-- Filters -->
    <div class="filters">
      <input type="text" id="search" placeholder="Search opportunities...">
      <select id="sdg-filter">
        <option value="">All SDGs</option>
        <option value="1">SDG 1: No Poverty</option>
        <option value="2">SDG 2: Zero Hunger</option>
        <!-- Add all 17 SDGs -->
      </select>
      <select id="dept-filter">
        <option value="">All Departments</option>
        <option value="Business Administration">Business Administration</option>
        <option value="Finance">Finance</option>
        <!-- Add all departments -->
      </select>
    </div>
    
    <!-- Opportunity Cards -->
    <div class="opportunities-grid" id="opportunities-grid">
      <!-- Cards will be populated by JavaScript -->
    </div>
  </div>
</section>
```

**JavaScript to Populate Cards:**

```javascript
// Load opportunities from your data source
const opportunities = [
  {
    title: "AI for Cancer Diagnosis",
    researcher: "Dr. Jane Smith",
    department: "Business Administration",
    sdgs: [3],
    keywords: ["AI", "Healthcare", "Machine Learning"],
    year: 2019,
    matchScore: 85
  },
  // Add more opportunities from your Power BI data
];

function createOpportunityCard(opp) {
  const sdgBadges = opp.sdgs.map(sdg => 
    `<span class="sdg-badge sdg-${sdg}">SDG ${sdg}</span>`
  ).join('');
  
  const keywordTags = opp.keywords.map(kw => 
    `<span class="keyword-tag">${kw}</span>`
  ).join('');
  
  return `
    <div class="opportunity-card">
      <div class="sdg-badges">${sdgBadges}</div>
      <h3>${opp.title}</h3>
      <p class="researcher">${opp.researcher} • ${opp.department}</p>
      <div class="keywords">${keywordTags}</div>
      <div class="meta">
        <span>Year: ${opp.year}</span>
        ${opp.matchScore ? `<span class="match-score">Match: ${opp.matchScore}%</span>` : ''}
      </div>
      <div class="actions">
        <button class="btn-learn-more">Learn More</button>
        <button class="btn-contact">Contact Researcher</button>
      </div>
    </div>
  `;
}

function displayOpportunities() {
  const grid = document.getElementById('opportunities-grid');
  grid.innerHTML = opportunities.map(opp => createOpportunityCard(opp)).join('');
}

// Filter functionality
document.getElementById('search').addEventListener('input', filterOpportunities);
document.getElementById('sdg-filter').addEventListener('change', filterOpportunities);
document.getElementById('dept-filter').addEventListener('change', filterOpportunities);

function filterOpportunities() {
  const search = document.getElementById('search').value.toLowerCase();
  const sdg = document.getElementById('sdg-filter').value;
  const dept = document.getElementById('dept-filter').value;
  
  const filtered = opportunities.filter(opp => {
    const matchesSearch = opp.title.toLowerCase().includes(search) ||
                         opp.researcher.toLowerCase().includes(search) ||
                         opp.keywords.some(kw => kw.toLowerCase().includes(search));
    const matchesSDG = !sdg || opp.sdgs.includes(parseInt(sdg));
    const matchesDept = !dept || opp.department === dept;
    
    return matchesSearch && matchesSDG && matchesDept;
  });
  
  document.getElementById('opportunities-grid').innerHTML = 
    filtered.map(opp => createOpportunityCard(opp)).join('');
}

// Initialize
displayOpportunities();
```

**CSS for Cards:**

```css
.opportunities-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 30px;
}

.opportunity-card {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: transform 0.2s, box-shadow 0.2s;
}

.opportunity-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.sdg-badge {
  display: inline-block;
  background: #13294B;
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  margin-right: 5px;
}

.keyword-tag {
  display: inline-block;
  background: #f5f5f5;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  margin-right: 5px;
  margin-top: 5px;
}

.match-score {
  color: #FF6B35;
  font-weight: bold;
}

.btn-learn-more, .btn-contact {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-right: 10px;
  margin-top: 10px;
}

.btn-learn-more {
  background: #13294B;
  color: white;
}

.btn-contact {
  background: #FF6B35;
  color: white;
}
```

### **Step 4: Add Dashboard Integration**

**Embed Power BI Dashboard:**

```html
<section class="dashboard-section">
  <div class="container">
    <h2>Live Research Statistics</h2>
    <div class="dashboard-embed">
      <iframe 
        src="YOUR_POWER_BI_EMBED_URL" 
        width="100%" 
        height="600" 
        frameborder="0">
      </iframe>
    </div>
  </div>
</section>
```

**Or Create Custom Stats Widget:**

```html
<section class="stats-section">
  <div class="container">
    <h2>Research Impact at a Glance</h2>
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-number" id="total-pubs">1,899</div>
        <div class="stat-label">Total Publications</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" id="sustainable-pubs">397</div>
        <div class="stat-label">Sustainable Research</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" id="sustainable-pct">21%</div>
        <div class="stat-label">Sustainable %</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" id="sdgs-covered">15</div>
        <div class="stat-label">SDGs Covered</div>
      </div>
    </div>
  </div>
</section>
```

**Fetch data from Power BI API or update manually:**

```javascript
// Update stats (you can fetch from Power BI API or update manually)
async function updateStats() {
  // If using Power BI API:
  // const data = await fetchPowerBIData();
  // document.getElementById('total-pubs').textContent = data.totalPublications;
  
  // Or update manually from your dashboard:
  document.getElementById('total-pubs').textContent = '1,899';
  document.getElementById('sustainable-pubs').textContent = '397';
  document.getElementById('sustainable-pct').textContent = '21%';
  document.getElementById('sdgs-covered').textContent = '15';
}
```

---

## 🔗 **Phase 4: Connect Everything (1 hour)**

### **Step 1: Link Survey to Matching**

**After user submits Google Form:**

1. **Set up Google Apps Script** (optional, for automation):
   - Go to Google Sheets → Extensions → Apps Script
   - Create script to process new responses
   - Run matching algorithm
   - Email results to user

**Or Manual Process:**
1. Export Google Sheets responses to CSV
2. Run matching script
3. Generate match results
4. Display on website or email to user

### **Step 2: Create Results Page**

**After survey submission, redirect to results:**

```html
<!-- results.html -->
<section class="results-section">
  <div class="container">
    <h2>Your Research Matches</h2>
    <p>Based on your interests, here are the top opportunities for you:</p>
    
    <div class="matches-grid" id="matches-grid">
      <!-- Matches populated by JavaScript -->
    </div>
    
    <div class="actions">
      <a href="opportunities.html" class="btn-primary">Browse All Opportunities</a>
      <a href="survey.html" class="btn-secondary">Update My Preferences</a>
    </div>
  </div>
</section>
```

**JavaScript to show matches:**

```javascript
// Get user email from URL parameter or session
const userEmail = new URLSearchParams(window.location.search).get('email');

// Fetch matches (from your backend or local data)
async function loadMatches(email) {
  // Call your matching API or load from file
  const matches = await fetchMatches(email);
  
  const grid = document.getElementById('matches-grid');
  grid.innerHTML = matches.map(opp => createOpportunityCard(opp)).join('');
}

loadMatches(userEmail);
```

### **Step 3: Add Contact Form**

**Create contact modal/form:**

```html
<!-- Contact Modal -->
<div id="contact-modal" class="modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <h2>Contact Researcher</h2>
    <form id="contact-form">
      <input type="text" name="name" placeholder="Your Name" required>
      <input type="email" name="email" placeholder="Your Email" required>
      <input type="text" name="role" placeholder="Your Role" required>
      <textarea name="message" placeholder="Why are you interested? What can you contribute?" required></textarea>
      <button type="submit" class="btn-primary">Send Message</button>
    </form>
  </div>
</div>
```

**JavaScript for contact form:**

```javascript
document.getElementById('contact-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData);
  
  // Send to backend or email service
  // For demo, you can use EmailJS or Formspree
  await sendContactEmail(data);
  
  alert('Message sent! The researcher will contact you soon.');
  document.getElementById('contact-modal').style.display = 'none';
});
```

---

## 📦 **Phase 5: Complete Website Structure**

### **Full Page Structure:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GIES Research Collaboration Platform</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header -->
  <header>
    <nav>
      <div class="logo">GIES Research</div>
      <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#opportunities">Opportunities</a></li>
        <li><a href="#dashboard">Dashboard</a></li>
        <li><a href="#about">About</a></li>
      </ul>
    </nav>
  </header>

  <!-- Hero Section -->
  <section id="home" class="join-us-hero">
    <!-- Hero content from Step 1 -->
  </section>

  <!-- How It Works -->
  <section class="how-it-works">
    <div class="container">
      <h2>How It Works</h2>
      <div class="steps">
        <div class="step">
          <div class="step-number">1</div>
          <h3>Take Survey</h3>
          <p>Tell us about your research interests and skills</p>
        </div>
        <div class="step">
          <div class="step-number">2</div>
          <h3>Get Matched</h3>
          <p>Our algorithm finds opportunities that match your profile</p>
        </div>
        <div class="step">
          <div class="step-number">3</div>
          <h3>Connect</h3>
          <p>Reach out to researchers and start collaborating</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Survey Section -->
  <section id="survey" class="survey-section">
    <!-- Survey embed from Step 2 -->
  </section>

  <!-- Opportunities Section -->
  <section id="opportunities" class="opportunities-section">
    <!-- Opportunity board from Step 3 -->
  </section>

  <!-- Dashboard Section -->
  <section id="dashboard" class="dashboard-section">
    <!-- Dashboard embed from Step 4 -->
  </section>

  <!-- Footer -->
  <footer>
    <p>&copy; 2024 GIES Business School - University of Illinois</p>
  </footer>

  <script src="script.js"></script>
</body>
</html>
```

---

## 🚀 **Quick Start Checklist**

### **Day 1: Setup (2 hours)**
- [ ] Create Google Form with all questions
- [ ] Test form and get shareable link
- [ ] Export Power BI data to CSV
- [ ] Set up basic website structure

### **Day 2: Build Components (3 hours)**
- [ ] Create landing page/hero section
- [ ] Embed Google Form
- [ ] Build opportunity board (HTML/CSS/JS)
- [ ] Add filters and search

### **Day 3: Integration (2 hours)**
- [ ] Create matching script
- [ ] Connect form to matching
- [ ] Build results page
- [ ] Add contact form

### **Day 4: Polish (2 hours)**
- [ ] Add dashboard integration
- [ ] Style everything consistently
- [ ] Test user flows
- [ ] Mobile responsiveness

---

## 💡 **Quick Implementation Tips**

### **For Case Competition (Fast Track):**

1. **Use Google Forms** (don't build custom form)
2. **Simple matching** (SDG + keyword overlap, no complex algorithm)
3. **Static opportunity data** (export from Power BI, hardcode in website)
4. **Basic contact form** (use Formspree or EmailJS - free)
5. **Embed Power BI** (don't build custom dashboard)

### **Minimum Viable Product:**

- ✅ Landing page with "Join Us!" section
- ✅ Google Form embedded
- ✅ Opportunity board (10-20 opportunities from your data)
- ✅ Basic filters (SDG, Department)
- ✅ Contact form
- ✅ Dashboard embed

---

## 📝 **Sample Data Structure**

**Create `opportunities.json` from your Power BI data:**

```json
[
  {
    "id": 1,
    "title": "AI for Cancer Diagnosis",
    "researcher": "Dr. Mehmet Ahsen",
    "department": "Business Administration",
    "email": "ahsen@illinois.edu",
    "sdgs": [3],
    "keywords": ["AI", "Healthcare", "Machine Learning", "Breast Cancer"],
    "year": 2019,
    "doi": "https://doi.org/10.1287/isre.2018.0789",
    "abstract": "Bias-aware algorithm for breast cancer diagnosis..."
  },
  {
    "id": 2,
    "title": "CEO Risk Preference and R&D Investment",
    "researcher": "Dr. A. Rashad Abdel-Khalik",
    "department": "Accountancy",
    "email": "rashad@illinois.edu",
    "sdgs": [8],
    "keywords": ["Finance", "Risk Management", "R&D", "Corporate Governance"],
    "year": 2014,
    "doi": "https://doi.org/10.1111/abac.12029",
    "abstract": "CEO risk tolerance and investment in risky projects..."
  }
  // Add more from your Publications data
]
```

---

## ✅ **Final Checklist**

- [ ] Google Form created and tested
- [ ] Website landing page designed
- [ ] Opportunity board built
- [ ] Matching algorithm created (or simple version)
- [ ] Contact form added
- [ ] Dashboard integrated
- [ ] Mobile responsive
- [ ] Tested all user flows
- [ ] Ready for case competition!

---

**Follow these steps and you'll have a working collaboration platform!** 🎉

Need help with any specific step? Let me know which part you're working on!



