import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Ecolang - Video Mesh Viewer",
    layout="wide"
)

# Video pairs configuration
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

# Custom CSS
st.markdown("""
<style>
    .stVideo {
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }

    .video-label {
        background: #262626;
        padding: 12px 16px;
        font-weight: 600;
        font-size: 16px;
        border-radius: 8px;
        margin-bottom: 10px;
        text-align: center;
    }

    .sync-note {
        background: #1a1a1a;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        margin: 20px 0;
        border: 1px solid #3a3a3a;
        color: #888;
    }

    .pulse-dot {
        display: inline-block;
        width: 8px;
        height: 8px;
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

# Sync status
st.markdown("""
<div class="sync-note">
    <span class="pulse-dot"></span>
    Videos are synchronized - left video controls both players
</div>
""", unsafe_allow_html=True)

# Get selected video paths
original_path = VIDEO_PAIRS[selected_pair]["original"]
mesh_path = VIDEO_PAIRS[selected_pair]["mesh"]

# Create two columns for videos
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="video-label">Original Video</div>', unsafe_allow_html=True)
    st.video(original_path, start_time=0)

with col2:
    st.markdown('<div class="video-label">Mesh Render</div>', unsafe_allow_html=True)
    st.video(mesh_path, start_time=0)

# Inject synchronization JavaScript
# This attempts to access parent document's video elements and sync them
sync_script = """
<script>
(function() {
    console.log('Ecolang Video Sync: Initializing...');

    function initSync() {
        try {
            const parentDoc = window.parent.document;
            const videos = parentDoc.querySelectorAll('video');

            if (videos.length >= 2) {
                const video1 = videos[0];
                const video2 = videos[1];

                console.log('Ecolang Video Sync: Found ' + videos.length + ' videos');

                // Check if already initialized
                if (video1.dataset.syncInitialized) {
                    console.log('Ecolang Video Sync: Already initialized');
                    return;
                }
                video1.dataset.syncInitialized = 'true';

                // Synchronization parameters
                const MAX_DRIFT = 0.15;
                let isSyncing = false;

                // Continuous sync monitoring
                function syncVideos() {
                    if (!isSyncing && !video1.paused && !video2.paused) {
                        const timeDiff = Math.abs(video2.currentTime - video1.currentTime);

                        if (timeDiff > MAX_DRIFT) {
                            isSyncing = true;
                            video2.currentTime = video1.currentTime;
                            setTimeout(() => { isSyncing = false; }, 100);
                        }
                    }
                    requestAnimationFrame(syncVideos);
                }

                // Event listeners for video1 (master)
                video1.addEventListener('play', () => {
                    console.log('Ecolang Video Sync: Play event');
                    video2.play().catch(e => console.log('Sync play failed:', e));
                });

                video1.addEventListener('pause', () => {
                    console.log('Ecolang Video Sync: Pause event');
                    video2.pause();
                });

                video1.addEventListener('seeked', () => {
                    console.log('Ecolang Video Sync: Seek event to', video1.currentTime);
                    video2.currentTime = video1.currentTime;
                });

                video1.addEventListener('ratechange', () => {
                    video2.playbackRate = video1.playbackRate;
                });

                video1.addEventListener('volumechange', () => {
                    video2.volume = video1.volume;
                    video2.muted = video1.muted;
                });

                // Start sync loop
                requestAnimationFrame(syncVideos);

                console.log('Ecolang Video Sync: Successfully initialized!');
            } else {
                console.log('Ecolang Video Sync: Waiting for videos... found ' + videos.length);
                // Try again after a delay
                setTimeout(initSync, 500);
            }
        } catch (e) {
            console.log('Ecolang Video Sync: Error -', e.message);
            // Try again after a delay
            setTimeout(initSync, 500);
        }
    }

    // Start initialization after page loads
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => setTimeout(initSync, 1000));
    } else {
        setTimeout(initSync, 1000);
    }
})();
</script>
"""

st.components.v1.html(sync_script, height=0)

# Sidebar
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
        original_size = os.path.getsize(original_path) / (1024 * 1024)
        mesh_size = os.path.getsize(mesh_path) / (1024 * 1024)

        st.markdown("**File Sizes:**")
        st.text(f"Original: {original_size:.1f} MB")
        st.text(f"Mesh: {mesh_size:.1f} MB")
