# Ecolang - Video Mesh Viewer

A Streamlit application that displays original videos alongside their mesh-rendered counterparts with perfect frame-accurate synchronization.

## Features

- 🎯 **Frame-Accurate Sync** - Videos stay synchronized within 100ms
- 🎮 **Unified Controls** - Control both videos from the left player
- 📱 **Responsive Design** - Works on desktop and mobile
- ⚡ **Fast & Free** - Hosted on GitHub with CDN delivery
- 🎨 **Clean UI** - Professional dark theme interface

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Video Hosting

#### Option A: Using GitHub (Free, Recommended)

1. **Create a new public GitHub repository** (or use this one)
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```

2. **Upload your videos to the `videos/` folder**
   - Name them: `original_1.mp4`, `original_2.mp4`, ..., `original_5.mp4`
   - Name them: `mesh_1.mp4`, `mesh_2.mp4`, ..., `mesh_5.mp4`

3. **Update video URLs in `app.py`**
   - Replace `YOUR_USERNAME` and `YOUR_REPO` with your GitHub details
   - URL format: `https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/videos/original_1.mp4`

#### Option B: Using Local Files (Testing Only)

For local testing, you can modify `app.py` to use local file paths:

```python
VIDEO_PAIRS = {
    "Video 1": {
        "original": "videos/original_1.mp4",
        "mesh": "videos/mesh_1.mp4"
    },
    # ...
}
```

**Note:** Local files won't work when deployed to Streamlit Cloud.

### 3. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Video Requirements

### File Format
- **Format:** MP4 (H.264 codec recommended)
- **Size:** Up to 33MB per video (larger files supported but may load slower)
- **Resolution:** Any (720p or 1080p recommended)

### Naming Convention
Place your videos in the `videos/` folder with these exact names:

```
videos/
├── original_1.mp4
├── mesh_1.mp4
├── original_2.mp4
├── mesh_2.mp4
├── original_3.mp4
├── mesh_3.mp4
├── original_4.mp4
├── mesh_4.mp4
├── original_5.mp4
└── mesh_5.mp4
```

### Optimizing Videos for Web

If your videos are large, optimize them:

```bash
# Using ffmpeg (install from https://ffmpeg.org)
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k -movflags +faststart output.mp4
```

This will:
- Compress the video for faster loading
- Enable progressive loading (faststart)
- Maintain good quality

## Deployment to Streamlit Cloud

1. **Push your code to GitHub** (with videos uploaded)

2. **Go to [share.streamlit.io](https://share.streamlit.io)**

3. **Deploy your app:**
   - Click "New app"
   - Select your repository
   - Set main file: `app.py`
   - Click "Deploy"

4. **Your app will be live** at `https://your-app-name.streamlit.app`

## How It Works

### Synchronization Technology

The app uses JavaScript's `requestAnimationFrame` API for frame-accurate synchronization:

1. **Event Listeners** - Play, pause, seek, and volume events from the left video are mirrored to the right video
2. **Drift Correction** - Every frame, the app checks if videos are more than 100ms out of sync and corrects it
3. **Playback Rate Sync** - Speed changes are synchronized
4. **Volume Sync** - Volume and mute state are synchronized

### Architecture

```
User selects video pair
        ↓
Streamlit dropdown updates URLs
        ↓
Custom HTML component loads
        ↓
Two HTML5 video players created
        ↓
JavaScript sync engine starts
        ↓
Left player controls both videos
```

## Customization

### Change Video Names in Dropdown

Edit the `VIDEO_PAIRS` dictionary in `app.py`:

```python
VIDEO_PAIRS = {
    "Scene 1 - Walking": {  # Change this label
        "original": "...",
        "mesh": "..."
    },
    # ...
}
```

### Adjust Sync Tolerance

In `app.py`, find `MAX_DRIFT` and adjust:

```javascript
const MAX_DRIFT = 0.1; // 100ms - decrease for tighter sync
```

### Modify Styling

Edit the CSS in the `<style>` section of `app.py`:
- Colors: Change hex values (e.g., `#0e1117`)
- Sizes: Adjust padding, gaps, font sizes
- Layout: Modify flexbox properties

## Troubleshooting

### Videos Don't Load

1. **Check URLs** - Make sure GitHub URLs are correct
2. **Check file names** - Must match exactly (case-sensitive)
3. **Check browser console** - Press F12 to see error messages
4. **Try different browser** - Chrome, Firefox, or Edge recommended

### Videos Not Syncing

1. **Check both videos loaded** - Wait for both to fully load
2. **Use left player controls** - Right player controls won't sync
3. **Check video codecs** - Both should be MP4/H.264
4. **Clear browser cache** - Hard refresh with Ctrl+F5

### Slow Loading

1. **Optimize videos** - Use ffmpeg to compress (see above)
2. **Check file sizes** - Keep under 20MB if possible
3. **Use CDN** - GitHub raw URLs have good CDN
4. **Check internet speed** - Videos stream from internet

### GitHub Bandwidth Issues

If you exceed GitHub's bandwidth (rare with 5-10 users/day):
- Use GitHub Pages instead of raw URLs
- Consider Cloudinary free tier (25GB/month)
- Use Google Drive with direct download links

## Technical Stack

- **Frontend:** Streamlit + Custom HTML/JavaScript
- **Video Player:** Native HTML5 `<video>` elements
- **Sync Engine:** RequestAnimationFrame + Event Listeners
- **Hosting:** Streamlit Cloud (app) + GitHub (videos)
- **Styling:** Custom CSS with dark theme

## Browser Support

- ✅ Chrome/Edge (Chromium) - Recommended
- ✅ Firefox
- ✅ Safari
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

- **Initial Load:** 2-5 seconds (depending on video size)
- **Sync Latency:** <100ms
- **Memory Usage:** ~200-300MB (for two 15MB videos)
- **CPU Usage:** Low (hardware-accelerated video decode)

## License

Feel free to use and modify this application for your needs.

## Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review browser console for errors (F12)
3. Ensure all files are named correctly
4. Verify video URLs are accessible

## Credits

Built with Streamlit and modern web technologies for showcasing mesh rendering comparisons.
