import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Ecolang - Video Mesh Viewer",
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
st.title("Ecolang - Video Mesh Viewer")
st.markdown("---")

# Video selector
st.markdown("### Select a video to view:")
selected_pair = st.selectbox(
    "Choose video",
    list(VIDEO_PAIRS.keys()),
    label_visibility="collapsed"
)

st.markdown("---")

# Get selected video paths
original_path = VIDEO_PAIRS[selected_pair]["original"]
mesh_path = VIDEO_PAIRS[selected_pair]["mesh"]

# Create synchronized video player using custom HTML component
# This approach works on Streamlit Cloud by embedding videos with sync JavaScript
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
            background-color: transparent;
            color: #fafafa;
        }}

        .container {{
            padding: 0px;
            max-width: 100%;
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
            padding: 12px;
            text-align: center;
            font-size: 13px;
            color: #888;
            background: #1a1a1a;
            border-radius: 8px;
            border: 1px solid #3a3a3a;
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

        @media (max-width: 768px) {{
            .video-wrapper {{
                flex-direction: column;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="sync-status">
            <span class="sync-indicator"></span>
            Videos are synchronized - left video controls both players
        </div>
        <br>
        <div class="video-wrapper">
            <div class="video-container">
                <div class="video-header">Original Video</div>
                <video id="video1" controls preload="auto">
                    <source src="{original_path}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>

            <div class="video-container">
                <div class="video-header">Mesh Render</div>
                <video id="video2" controls preload="auto">
                    <source src="{mesh_path}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
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
            if (isSyncing) {{
                requestAnimationFrame(syncVideos);
                return;
            }}

            // Only sync when both videos are playing
            if (!video1.paused && !video2.paused) {{
                const timeDiff = Math.abs(video2.currentTime - video1.currentTime);

                if (timeDiff > MAX_DRIFT) {{
                    isSyncing = true;
                    video2.currentTime = video1.currentTime;
                    setTimeout(() => {{ isSyncing = false; }}, 100);
                }}
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
            console.log('Video 1 loaded successfully');
        }});

        video2.addEventListener('loadedmetadata', () => {{
            console.log('Video 2 loaded successfully');
        }});

        // Error handling
        video1.addEventListener('error', (e) => {{
            console.error('Video 1 error:', video1.error);
        }});

        video2.addEventListener('error', (e) => {{
            console.error('Video 2 error:', video2.error);
        }});
    </script>
</body>
</html>
"""

# Render the synchronized video player
st.components.v1.html(html_code, height=700, scrolling=False)


# Sidebar with additional info
with st.sidebar:
    st.header("About Ecolang")
    st.markdown("""
    This application displays original videos alongside their mesh-rendered counterparts
    for easy comparison.
    """)

    st.markdown("---")
    st.markdown("**Current Selection:**")
    st.info(f"{selected_pair}")

    # Show video file info
    import os
    if os.path.exists(original_path) and os.path.exists(mesh_path):
        original_size = os.path.getsize(original_path) / (1024 * 1024)  # MB
        mesh_size = os.path.getsize(mesh_path) / (1024 * 1024)  # MB

        st.markdown("**File Sizes:**")
        st.text(f"Original: {original_size:.1f} MB")
        st.text(f"Mesh: {mesh_size:.1f} MB")
