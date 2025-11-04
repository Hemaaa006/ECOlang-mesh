# Ecolang Setup Guide

## Step-by-Step Instructions

### Step 1: Upload Your Videos to GitHub

Since your videos are on Google Drive, follow these steps:

#### 1.1 Download Videos from Google Drive
- Download all 10 videos (5 original + 5 mesh renders) to your local machine

#### 1.2 Rename Videos
Rename them according to this convention:
```
original_1.mp4, original_2.mp4, original_3.mp4, original_4.mp4, original_5.mp4
mesh_1.mp4, mesh_2.mp4, mesh_3.mp4, mesh_4.mp4, mesh_5.mp4
```

#### 1.3 Move Videos to the Videos Folder
Copy all renamed videos to: `C:\Users\dell\Desktop\ecolang\videos\`

### Step 2: Create GitHub Repository

#### 2.1 Initialize Git Repository
```bash
cd C:\Users\dell\Desktop\ecolang
git init
git add .
git commit -m "Initial commit: Ecolang video viewer"
```

#### 2.2 Create GitHub Repository
1. Go to https://github.com/new
2. Create a new **public** repository named "ecolang" (or any name you prefer)
3. **Do NOT** initialize with README (we already have files)

#### 2.3 Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/ecolang.git
git branch -M main
git push -u origin main
```

**Note:** If your videos are larger than 25MB each, you may need to use Git LFS:
```bash
git lfs install
git lfs track "*.mp4"
git add .gitattributes
git commit -m "Configure Git LFS for videos"
```

### Step 3: Update Video URLs in app.py

1. Open `app.py` in a text editor
2. Find the `VIDEO_PAIRS` dictionary (around line 12)
3. Replace `YOUR_USERNAME` and `YOUR_REPO` with your actual GitHub username and repository name

Example:
```python
VIDEO_PAIRS = {
    "Video 1": {
        "original": "https://raw.githubusercontent.com/johnsmith/ecolang/main/videos/original_1.mp4",
        "mesh": "https://raw.githubusercontent.com/johnsmith/ecolang/main/videos/mesh_1.mp4"
    },
    # ... rest of the pairs
}
```

### Step 4: Test Locally (Optional but Recommended)

Before deploying, test locally:

```bash
cd C:\Users\dell\Desktop\ecolang
streamlit run app.py
```

The app will open at http://localhost:8501

**For local testing:** You can temporarily use local file paths:
```python
"original": "videos/original_1.mp4",
```

### Step 5: Deploy to Streamlit Cloud (Optional)

1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select your repository: `YOUR_USERNAME/ecolang`
5. Main file path: `app.py`
6. Click "Deploy!"

Your app will be live at: `https://ecolang-YOUR_USERNAME.streamlit.app`

## Alternative: Using Google Drive Direct Links

If you prefer to keep videos on Google Drive (not recommended for sync quality):

### Option A: Google Drive Public Links

1. Make each video publicly accessible
2. Get the shareable link: `https://drive.google.com/file/d/FILE_ID/view`
3. Convert to direct download link: `https://drive.google.com/uc?export=download&id=FILE_ID`
4. Update `VIDEO_PAIRS` in `app.py` with these links

**Limitations:**
- May hit bandwidth limits
- Slower loading
- Less reliable synchronization

## Troubleshooting

### Git Push Fails (File Too Large)
If videos are >100MB, use Git LFS:
```bash
git lfs install
git lfs track "*.mp4"
git add .gitattributes
git add videos/
git commit -m "Add videos with Git LFS"
git push
```

### Videos Don't Play Locally
- Streamlit's file serving works better with URLs
- For local testing, use a local web server or test with GitHub URLs after pushing

### Sync Issues
- Ensure both videos have the same frame rate
- Use the same codec (H.264) for both videos
- Videos should ideally be the same length

## Quick Commands Reference

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Locally
```bash
streamlit run app.py
```

### Git Commands
```bash
git status                          # Check what files are staged
git add .                          # Stage all files
git commit -m "Your message"       # Commit changes
git push                           # Push to GitHub
```

### Check Streamlit Version
```bash
streamlit --version
```

## Next Steps

1. ✅ Download and rename your videos
2. ✅ Move videos to the `videos/` folder
3. ✅ Create GitHub repository and push code
4. ✅ Update URLs in `app.py`
5. ✅ Test locally
6. ✅ Deploy to Streamlit Cloud (optional)

You're all set! Your Ecolang video viewer is ready to go. 🎉
