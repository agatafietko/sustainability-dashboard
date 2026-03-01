# Deployment Guide: Streamlit Community Cloud

Step-by-step instructions to deploy the Sustainability Research Discovery Hub to Streamlit Community Cloud (free).

---

## Prerequisites

1. **GitHub Account** (free)
2. **Streamlit Community Cloud Account** (free, sign up at https://streamlit.io/cloud)
3. **Original CSV file**: `for distribution case competition filtered_publications.csv`

## GitHub Repository

**Repository URL**: `https://github.com/meryemrafiq14-hue/sustainability_case_competition.git`

The app is located in: `components/collab_hub/app.py`

---

## Step 1: Prepare Your Repository

### 1.1 Verify Repository Structure

Your GitHub repository should have this structure:

```
sustainability_case_competition/
├── components/
│   └── collab_hub/
│       ├── app.py                    # Streamlit app
│       ├── requirements.txt          # Dependencies
│       └── ... (other files)
└── for distribution case competition filtered_publications.csv  # Original data
```

**Note**: The app loads the original CSV from the repository root. Ensure the CSV file is committed to the repo.

### 1.2 Verify Files Are Committed

```bash
cd "/Users/meryem/Documents/Collab hub/Case Competition"
git status
# Should show all files committed
```

---

## Step 2: Verify App Files

The app needs:
- `components/collab_hub/app.py` - Main Streamlit application
- `components/collab_hub/requirements.txt` - Dependencies
- `for distribution case competition filtered_publications.csv` - Original data (in repo root)

**Verify files are committed:**
```bash
git status
# Should show "nothing to commit, working tree clean"
```

---

## Step 3: Deploy to Streamlit Cloud

### 3.1 Sign Up / Log In

1. Go to https://share.streamlit.io/
2. Click **"Sign up"** or **"Log in"**
3. Sign in with your GitHub account

### 3.2 Create New App

1. Click **"New app"** button
2. Fill in the form:
   - **Repository**: Select `meryemrafiq14-hue/sustainability_case_competition`
   - **Branch**: `main`
   - **Main file path**: `components/collab_hub/app.py`
   - **App URL**: Choose a custom URL (e.g., `sustainability-research-hub`)

3. Click **"Deploy"**

### 3.3 Configure Secrets (If Needed)

If you're using Streamlit Secrets for confidential data:

1. In your app dashboard, click **"⋮"** (three dots) → **"Settings"**
2. Scroll to **"Secrets"**
3. Paste your secrets in TOML format:
   ```toml
   [data]
   csv_path = "your/path/here"
   ```
4. Click **"Save"** - the app will automatically redeploy

---

## Step 4: Wait for Deployment

1. Streamlit Cloud will:
   - Install dependencies from `requirements.txt`
   - Run `app.py`
   - Show deployment progress in the dashboard

2. **First deployment takes 2-5 minutes** (downloading models, installing packages)

3. You'll see logs in real-time. Watch for:
   - ✅ "Successfully installed..."
   - ✅ "You can now view your Streamlit app..."

---

## Step 5: Access Your Live App

Once deployed, you'll get a public URL like:
```
https://sustainability-research-hub.streamlit.app
```

**Share this URL with judges!**

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'sentence_transformers'"

**Solution**: Make sure `requirements.txt` includes `sentence-transformers>=2.2.0`

### Issue: "FileNotFoundError: for distribution case competition filtered_publications.csv"

**Solution**: 
- Ensure the original CSV file is in the repository root
- The app searches multiple paths automatically
- Check the file path in the error message and verify it exists in the repo

### Issue: "App is taking too long to load"

**Solution**: 
- First load downloads the NLP model (~80MB) - this is normal
- Subsequent loads are cached and faster
- Consider using `@st.cache_resource` (already in code)

### Issue: "Deployment failed"

**Solution**:
1. Check the logs in Streamlit Cloud dashboard
2. Verify `requirements.txt` syntax is correct
3. Make sure Python version is compatible (Streamlit Cloud uses Python 3.9+)

---

## Updating Your App

After making changes:

```bash
git add .
git commit -m "Update app"
git push origin main
```

Streamlit Cloud **automatically redeploys** when you push to the main branch.

---

## Optional: Custom Domain

Streamlit Cloud free tier includes:
- ✅ Public URL (your-app.streamlit.app)
- ✅ Automatic HTTPS
- ✅ Auto-deploy on git push

For custom domain, you'd need Streamlit Cloud Team plan.

---

## Security Notes

1. **Public repositories**: Your code and data are public
2. **Secrets**: Use Streamlit Secrets for sensitive data
3. **Data privacy**: Ensure CSV doesn't contain confidential information
4. **Rate limiting**: Free tier has usage limits (reasonable for demos)

---

## Success Checklist

- [ ] GitHub repository created and code pushed
- [ ] `requirements.txt` includes all dependencies
- [ ] `Researcher_Profiles_For_PowerBI.csv` is accessible (in repo or via secrets)
- [ ] Streamlit Cloud app deployed successfully
- [ ] App loads and shows the persona selection
- [ ] Matching works when form is submitted
- [ ] Public URL is accessible

---

**Need help?** Check Streamlit Community Cloud docs: https://docs.streamlit.io/streamlit-community-cloud
