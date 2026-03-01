# Streamlit Cloud Deployment

## GitHub Repository

**Repository URL**: `https://github.com/meryemrafiq14-hue/sustainability_case_competition.git`

**App Location**: `components/collab_hub/app.py`

---

## Quick Deployment Steps

1. **Go to Streamlit Cloud**: https://share.streamlit.io/
2. **Sign in** with your GitHub account
3. **Click "New app"**
4. **Fill in**:
   - **Repository**: `meryemrafiq14-hue/sustainability_case_competition`
   - **Branch**: `main`
   - **Main file path**: `components/collab_hub/app.py`
   - **App URL**: Choose a custom name (e.g., `sustainability-research-hub`)
5. **Click "Deploy"**

---

## Requirements

- The original CSV file (`for distribution case competition filtered_publications.csv`) must be in the repository root
- All dependencies are in `components/collab_hub/requirements.txt`
- First deployment takes 2-5 minutes (downloads NLP model)

---

## Your App URL

After deployment, your app will be available at:
```
https://[your-app-name].streamlit.app
```

Example: `https://sustainability-research-hub.streamlit.app`

---

## Troubleshooting

**Issue**: "FileNotFoundError: for distribution case competition filtered_publications.csv"
- **Solution**: Ensure the CSV file is committed to the repository root

**Issue**: "ModuleNotFoundError"
- **Solution**: Verify `requirements.txt` includes all dependencies

**Issue**: Slow first load
- **Expected**: First load downloads NLP model (~80MB). Subsequent loads are cached and fast.

---

For detailed deployment instructions, see `DEPLOYMENT_GUIDE.md`
