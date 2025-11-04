import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Ecolang - Video Mesh Viewer",
    page_icon="🎥",
    layout="wide"
)

# Video pairs configuration - using local file paths
# Streamlit Cloud will serve these files directly from the repo
VIDEO_PAIRS = {
    "Video 1 - Ch07 Speakerview 016": {
        "original": "videos/original_1.mp4",
        "mesh": "videos/mesh_1.mp4"
    },
    "Video 2 - Ch09 Speakerview 007": {
        "original": "videos/original_2.mp4",
        "mesh": "videos/mesh_2.mp4"
    },
    "Video 3 - Ch11 Speakerview 002": {
        "original": "videos/original_3.mp4",
        "mesh": "videos/mesh_3.mp4"
    },
    "Video 4 - Ch12 Speakerview 006": {
        "original": "videos/original_4.mp4",
        "mesh": "videos/mesh_4.mp4"
    },
    "Video 5 - Ch17 Speakerview 011": {
        "original": "videos/original_5.mp4",
        "mesh": "videos/mesh_5.mp4"
    }
}

# Custom CSS for styling
st.markdown("""
<style>
    /* Video container styling */
    .stVideo {
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }

    /* Header styling */
    .video-header {
        background: #262626;
        padding: 12px 16px;
        font-weight: 600;
        font-size: 18px;
        border-radius: 8px;
        margin-bottom: 10px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    /* Sync info box */
    .sync-info {
        background: #1a1a1a;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        margin: 20px 0;
        border: 1px solid #3a3a3a;
    }

    .sync-indicator {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #4CAF50;
        margin-right: 8px;
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
</style>
""", unsafe_allow_html=True)

# App header
st.title("🎥 Ecolang - Video Mesh Viewer")
st.markdown("---")

# Video selector
st.markdown("### Select a video pair to view:")
selected_pair = st.selectbox(
    "Choose video",
    list(VIDEO_PAIRS.keys()),
    label_visibility="collapsed"
)

st.markdown("---")

# Get selected video paths
original_path = VIDEO_PAIRS[selected_pair]["original"]
mesh_path = VIDEO_PAIRS[selected_pair]["mesh"]

# Info message about synchronization
st.markdown("""
<div class="sync-info">
    <span class="sync-indicator"></span>
    <strong>Note:</strong> Use the play/pause buttons on both videos to keep them synchronized
</div>
""", unsafe_allow_html=True)

# Create two columns for side-by-side video display
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="video-header">📹 Original Video</div>', unsafe_allow_html=True)
    st.video(original_path)

with col2:
    st.markdown('<div class="video-header">🔷 Mesh Render</div>', unsafe_allow_html=True)
    st.video(mesh_path)

# Footer with instructions
st.markdown("---")
st.markdown("""
### 📖 Instructions:
- Use the dropdown above to select different video pairs
- Play both videos manually to view them side-by-side
- Both videos have independent controls for flexible viewing
- For best synchronization, start both videos at the same time

### ⚡ Pro Tip:
Open your browser's developer console (F12) and use this script for automatic synchronization:
```javascript
// Get all video elements
const videos = document.querySelectorAll('video');
if (videos.length >= 2) {
    const v1 = videos[0];
    const v2 = videos[1];

    // Sync play/pause
    v1.addEventListener('play', () => v2.play());
    v1.addEventListener('pause', () => v2.pause());
    v1.addEventListener('seeked', () => { v2.currentTime = v1.currentTime; });
}
```
""")

# Sidebar with additional info
with st.sidebar:
    st.header("About Ecolang")
    st.markdown("""
    This application displays original videos alongside their mesh-rendered counterparts
    for easy comparison.

    **Features:**
    - 🎮 Side-by-side video comparison
    - 📱 Responsive design
    - ⚡ Fast loading from repository
    - 🎯 High-quality video playback

    **Tips:**
    - Videos are served directly from the repository
    - Use fullscreen mode for better viewing
    - Works on desktop and mobile browsers
    """)

    st.markdown("---")
    st.markdown("**Current Selection:**")
    st.info(f"📹 {selected_pair}")

    # Show video file info
    import os
    if os.path.exists(original_path) and os.path.exists(mesh_path):
        original_size = os.path.getsize(original_path) / (1024 * 1024)  # MB
        mesh_size = os.path.getsize(mesh_path) / (1024 * 1024)  # MB

        st.markdown("**File Sizes:**")
        st.text(f"Original: {original_size:.1f} MB")
        st.text(f"Mesh: {mesh_size:.1f} MB")
