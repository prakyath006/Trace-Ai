import streamlit as st
import requests

# Configure Page
st.set_page_config(
    page_title="TraceAI | Cybernetic Debugging",
    page_icon="�",
    layout="wide",
    initial_sidebar_state="expanded"
)

import os

# Backend URL (FastAPI)
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8001")

# Custom CSS for Premium AI/Futuristic Look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

    /* Deep Space Theme */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0a0b12 0%, #050508 100%);
        font-family: 'Outfit', sans-serif;
        color: #e2e8f0;
    }
    
    /* Sidebar styling - Glassmorphism */
    [data-testid="stSidebar"] {
        background-color: rgba(10, 11, 18, 0.8);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(0, 242, 255, 0.1);
    }
    
    /* Headers - Neon Cyan/Purple Gradient */
    h1 {
        background: linear-gradient(90deg, #00f2ff, #7000ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700 !important;
        font-size: 3rem !important;
        letter-spacing: -0.04em;
        margin-bottom: 0.2rem !important;
        padding-bottom: 0rem !important;
    }
    
    h2 {
        color: #00f2ff !important;
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        margin-bottom: 1.5rem !important;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    h3 {
        color: #94a3b8 !important;
        font-size: 1.1rem !important;
        font-weight: 500 !important;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    
    /* Subtitle */
    .subtitle-text {
        color: #94a3b8;
        font-size: 1.2rem;
        margin-bottom: 2.5rem;
        font-weight: 300;
    }
    
    /* Buttons - Pulse Effect */
    .stButton > button {
        background: linear-gradient(135deg, #00f2ff 0%, #00d1ff 100%);
        color: #050508;
        font-weight: 600;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        text-transform: uppercase;
        letter-spacing: 0.05em;
        width: 100%;
        box-shadow: 0 4px 15px rgba(0, 242, 255, 0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 242, 255, 0.4);
        background: linear-gradient(135deg, #00f2ff 20%, #7000ff 100%);
        color: #ffffff;
    }
    
    /* File Uploader - Cyber Frame */
    [data-testid="stFileUploader"] {
        background-color: rgba(15, 23, 42, 0.5);
        border: 1px solid rgba(0, 242, 255, 0.2);
        border-radius: 12px;
        padding: 2rem;
        transition: border 0.3s ease;
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: #00f2ff;
    }
    
    /* Text Areas - Neo-Brutalism */
    .stTextArea > div > div > textarea {
        background-color: rgba(15, 23, 42, 0.8);
        color: #f1f5f9;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.9rem;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #00f2ff;
        box-shadow: 0 0 0 1px #00f2ff;
    }
    
    /* Result Section - AI/Tech Look */
    .result-section {
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.8) 0%, rgba(10, 11, 18, 0.9) 100%);
        border: 1px solid rgba(0, 242, 255, 0.2);
        border-left: 4px solid #00f2ff;
        padding: 2rem;
        border-radius: 16px;
        margin-top: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }
    
    /* Global Overrides */
    .stSpinner > div {
        border-top-color: #00f2ff !important;
    }
    
    code {
        color: #00f2ff !important;
        background-color: rgba(0, 242, 255, 0.1) !important;
        padding: 2px 4px;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# sidebar header with AI System Icon
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 1rem 0;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">�</div>
            <h2 style="justify-content: center; border: none; margin-bottom: 0;">TraceAI</h2>
            <p style="color: #64748b; font-size: 0.85rem; margin-top: 0;">Automated Diagnostic System v2.0</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### System Status")
    st.markdown("""
        - 🟢 **Core Engine:** Active
        - 🔵 **Vector Database:** Synchronized
        - ⚡ **Latency:** 24ms
    """)
    
    st.markdown("---")
    st.markdown("### System Log")
    st.caption("Waiting for repository uplink...")
    st.caption("AI pathway initialized.")

# Main Header
st.markdown('<h1>TraceAI Diagnostic</h1>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Synthesizing codebase logic through <strong>Advanced Vector Embedding</strong> for precise root-cause isolation.</div>', unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("<h2>📂 Vectorize Repository</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; margin-bottom: 1.5rem;'>Uplink your source architecture (ZIP). Our engine will shard the logic into hyper-dimensional vector space for real-time retrieval.</p>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Drop Repository ZIP", type=["zip"], label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Start Indexing Process", key="index_btn"):
        if uploaded_file:
            with st.spinner("Decoding and Sharding Logic..."):
                try:
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/zip")}
                    response = requests.post(f"{BACKEND_URL}/upload", files=files)
                    if response.status_code == 200:
                        st.success(f"Uplink Established. Vectorized {response.json()['file_count']} code fragments.")
                    else:
                        st.error(f"System Error: {response.json().get('detail', 'System interference detected.')}")
                except Exception as e:
                    st.error(f"Uplink Failed: {e}")
        else:
            st.warning("Please provide a repository ZIP for ingestion.")

with col2:
    st.markdown("<h2>⚡ Analyze Trace</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; margin-bottom: 1.5rem;'>Input the corrupted stack trace. The system will intersect the error signature with the vector database to resolve logic failures.</p>", unsafe_allow_html=True)
    
    error_trace = st.text_area("Stack Trace Input", placeholder="Paste corrupted logs here...", height=200, label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Analyze Trace", key="analyze_btn"):
        if error_trace:
            with st.spinner("Analyzing Logic Remediation..."):
                try:
                    response = requests.post(f"{BACKEND_URL}/analyze", json={"error_trace": error_trace})
                    if response.status_code == 200:
                        st.session_state["analysis_result"] = response.json()["analysis"]
                    else:
                        st.error(f"Analysis Error: {response.json().get('detail', 'Logic intersection failed.')}")
                except Exception as e:
                    st.error(f"Analysis Offline: {e}")
        else:
            st.warning("Input an error trace to begin analysis.")

# Display Results
if "analysis_result" in st.session_state:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h2>🛠 Remediation Blueprint</h2>", unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="result-section">', unsafe_allow_html=True)
        st.markdown(st.session_state["analysis_result"])
        st.markdown('</div>', unsafe_allow_html=True)

