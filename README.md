# Ecolang - Video Mesh Viewer

A Streamlit application that displays original videos for the ECOLANG dataset alongside their mesh-rendered counterparts using OSX


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

