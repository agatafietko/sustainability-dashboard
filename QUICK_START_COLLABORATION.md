# Quick Start: Build Collaboration Platform (3-4 Hours)

## 🚀 **Fast Track for Case Competition**

### **Step 1: Create Google Form (30 min)**

1. Go to https://forms.google.com
2. Create new form: "Find Your Research Match"
3. Add these sections:
   - **Basic Info**: Name, Email, Role, Department
   - **SDG Interests**: Checkboxes for all 17 SDGs
   - **Research Areas**: Checkboxes (AI, Healthcare, Sustainability, etc.)
   - **Skills**: Checkboxes (Quantitative, Programming, etc.)
   - **Time Commitment**: Multiple choice
4. Get embed code: Send → </> → Copy iframe code

---

### **Step 2: Use Website Template (1 hour)**

1. **Open `website_templates.html`** (I just created it)
2. **Replace** `YOUR_GOOGLE_FORM_EMBED_URL_HERE` with your Google Form embed URL
3. **Add your opportunities data**:
   - Export from Power BI: Publications with SDG and keyword info
   - Update the `opportunities` array in the JavaScript section
4. **Customize**:
   - Update stats (total pubs, sustainable %, etc.)
   - Add more opportunities from your data
   - Adjust colors if needed

---

### **Step 3: Add Your Data (1 hour)**

**Export from Power BI:**
1. Go to your Publications table
2. Export to CSV (or use Power BI API)
3. Include: title, name, department, publication_year, SDG IDs, keywords

**Create opportunities.json:**
```json
[
  {
    "id": 1,
    "title": "Your Publication Title",
    "researcher": "Researcher Name",
    "department": "Department Name",
    "email": "email@illinois.edu",
    "sdgs": [3, 8],
    "keywords": ["AI", "Healthcare"],
    "year": 2019
  }
]
```

**Update JavaScript:**
- Replace sample opportunities with your data
- Add at least 10-20 opportunities for demo

---

### **Step 4: Deploy Website (30 min)**

**Option A: GitHub Pages (Free)**
1. Create GitHub repository
2. Upload your HTML file
3. Enable GitHub Pages
4. Get live URL

**Option B: Vercel (Free, Recommended)**
1. Go to https://vercel.com
2. Sign up/login
3. Import your project
4. Deploy (takes 2 minutes)

**Option C: Netlify (Free)**
1. Go to https://netlify.com
2. Drag and drop your HTML file
3. Get instant URL

---

### **Step 5: Connect Form to Matching (Optional, 1 hour)**

**Simple Matching (No Backend):**
- Users fill form
- You export responses from Google Sheets
- Run matching script (Python or JavaScript)
- Manually update opportunities with match scores
- Or: Show all opportunities, let users filter

**Advanced Matching (With Backend):**
- Set up simple backend (Node.js/Python)
- Process form responses automatically
- Calculate matches
- Display results page

---

## ✅ **Minimum Viable Product Checklist**

**Must Have:**
- [ ] Landing page with "Join Us!" section
- [ ] Google Form embedded
- [ ] Opportunity board (10-20 opportunities)
- [ ] Basic filters (SDG, Department)
- [ ] Contact form/modal
- [ ] Stats section (from dashboard)
- [ ] Mobile responsive

**Nice to Have:**
- [ ] Matching algorithm
- [ ] Results page after survey
- [ ] Email notifications
- [ ] Power BI dashboard embedded
- [ ] Search functionality

---

## 🎯 **What You'll Have**

✅ **Professional website** with:
- Engaging "Join Us!" hero section
- Embedded survey form
- Interactive opportunity board
- Live research statistics
- Contact system
- Modern, responsive design

✅ **Ready for case competition** in 3-4 hours!

---

## 💡 **Pro Tips**

1. **Start Simple**: Get basic version working first
2. **Use Template**: `website_templates.html` has everything you need
3. **Add Real Data**: Export 20-30 opportunities from Power BI
4. **Test Mobile**: Make sure it looks good on phone
5. **Polish Later**: Get it working, then make it pretty

---

## 📝 **Next Steps**

1. **Create Google Form** (30 min)
2. **Use website template** (1 hour)
3. **Add your data** (1 hour)
4. **Deploy** (30 min)
5. **Test & polish** (30 min)

**Total: ~3-4 hours for working MVP!**

---

**The template file `website_templates.html` is ready to use - just add your Google Form URL and data!** 🎉

Need help with any specific step? Let me know!



