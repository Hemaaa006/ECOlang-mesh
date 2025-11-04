import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Ecolang - Video Mesh Viewer",
    page_icon="🎥",
    layout="wide"
)

# Video pairs configuration
# Replace these URLs with your actual video URLs after uploading to GitHub
VIDEO_PAIRS = {
    "Video 1": {
        "original": "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/videos/original_1.mp4",
        "mesh": "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/videos/mesh_1.mp4"
    },
    "Video 2": {
        "original": "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/videos/original_2.mp4",
        "mesh": "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/videos/mesh_2.mp4"
    },
    "Video 3": {
        "original": "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/videos/original_3.mp4",
        "mesh": "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/videos/mesh_3.mp4"
    },
    "Video 4": {
        "original": "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/videos/original_4.mp4",
        "mesh": "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/videos/mesh_4.mp4"
    },
    "Video 5": {
        "original": "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/videos/original_5.mp4",
        "mesh": "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/videos/mesh_5.mp4"
    }
}

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

# Get selected video URLs
original_url = VIDEO_PAIRS[selected_pair]["original"]
mesh_url = VIDEO_PAIRS[selected_pair]["mesh"]

# Custom HTML component with synchronized video players
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background-color: #0e1117;
            color: #fafafa;
        }}

        .container {{
            padding: 20px;
            max-width: 1400px;
            margin: 0 auto;
        }}

        .video-wrapper {{
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
        }}

        .video-container {{
            flex: 1;
            display: flex;
            flex-direction: column;
            background: #1e1e1e;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        }}

        .video-header {{
            background: #262626;
            padding: 12px 16px;
            font-weight: 600;
            font-size: 16px;
            border-bottom: 2px solid #3a3a3a;
        }}

        .video-container video {{
            width: 100%;
            height: auto;
            display: block;
            background: #000;
        }}

        .sync-status {{
            padding: 10px;
            text-align: center;
            font-size: 12px;
            color: #888;
            background: #1a1a1a;
        }}

        .sync-indicator {{
            display: inline-block;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            margin-right: 6px;
            background: #4CAF50;
            animation: pulse 2s infinite;
        }}

        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
        }}

        .loading {{
            text-align: center;
            padding: 40px;
            color: #888;
        }}

        @media (max-width: 768px) {{
            .video-wrapper {{
                flex-direction: column;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="video-wrapper">
            <div class="video-container">
                <div class="video-header">📹 Original Video</div>
                <video id="video1" controls preload="metadata">
                    <source src="{original_url}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>

            <div class="video-container">
                <div class="video-header">🔷 Mesh Render</div>
                <video id="video2" controls preload="metadata">
                    <source src="{mesh_url}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
        </div>

        <div class="sync-status">
            <span class="sync-indicator"></span>
            Videos are synchronized - controls on the left video will affect both
        </div>
    </div>

    <script>
        // Get video elements
        const video1 = document.getElementById('video1');
        const video2 = document.getElementById('video2');

        // Synchronization parameters
        const MAX_DRIFT = 0.1; // Maximum allowed time difference (100ms)
        let isSyncing = false;

        // Function to sync video2 to video1
        function syncVideos() {{
            if (isSyncing) return;

            const timeDiff = Math.abs(video2.currentTime - video1.currentTime);

            if (timeDiff > MAX_DRIFT) {{
                isSyncing = true;
                video2.currentTime = video1.currentTime;
                setTimeout(() => {{ isSyncing = false; }}, 100);
            }}

            requestAnimationFrame(syncVideos);
        }}

        // Synchronize play event
        video1.addEventListener('play', () => {{
            video2.play().catch(err => {{
                console.log('Play sync failed:', err);
            }});
        }});

        // Synchronize pause event
        video1.addEventListener('pause', () => {{
            video2.pause();
        }});

        // Synchronize seek event
        video1.addEventListener('seeked', () => {{
            video2.currentTime = video1.currentTime;
        }});

        // Synchronize playback rate
        video1.addEventListener('ratechange', () => {{
            video2.playbackRate = video1.playbackRate;
        }});

        // Synchronize volume
        video1.addEventListener('volumechange', () => {{
            video2.volume = video1.volume;
            video2.muted = video1.muted;
        }});

        // Start continuous sync monitoring
        requestAnimationFrame(syncVideos);

        // Handle video loading
        video1.addEventListener('loadedmetadata', () => {{
            console.log('Video 1 loaded');
        }});

        video2.addEventListener('loadedmetadata', () => {{
            console.log('Video 2 loaded');
        }});

        // Error handling
        video1.addEventListener('error', (e) => {{
            console.error('Video 1 error:', e);
        }});

        video2.addEventListener('error', (e) => {{
            console.error('Video 2 error:', e);
        }});

        // Inform Streamlit of component height
        function updateHeight() {{
            const height = document.body.scrollHeight;
            window.parent.postMessage({{
                type: 'streamlit:setComponentValue',
                height: height
            }}, '*');
        }}

        // Update height when videos load
        video1.addEventListener('loadedmetadata', updateHeight);
        video2.addEventListener('loadedmetadata', updateHeight);

        // Initial height update
        setTimeout(updateHeight, 100);
    </script>
</body>
</html>
"""

# Render the synchronized video player
st.components.v1.html(html_code, height=650)

# Footer with instructions
st.markdown("---")
st.markdown("""
### 📖 Instructions:
- Use the dropdown above to select different video pairs
- Control playback using the **left video player** (Original Video)
- Both videos will stay synchronized automatically
- Supported actions: Play, Pause, Seek, Volume, Playback Speed
""")

# Sidebar with additional info
with st.sidebar:
    st.header("About Ecolang")
    st.markdown("""
    This application displays original videos alongside their mesh-rendered counterparts
    in perfect synchronization.

    **Features:**
    - 🎯 Frame-accurate synchronization
    - 🎮 Unified playback controls
    - 📱 Responsive design
    - ⚡ Fast loading with CDN

    **Tips:**
    - Videos sync within 100ms accuracy
    - Use the left player to control both
    - Works on desktop and mobile
    """)

    st.markdown("---")
    st.markdown("**Current Selection:**")
    st.info(f"📹 {selected_pair}")
