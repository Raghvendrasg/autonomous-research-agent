import streamlit as st
import requests
import json
import time

# --- Page Config ---
st.set_page_config(
    page_title="Autonomous Research Analyst PRO",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Premium CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: radial-gradient(circle at top right, #1a1c24, #0e1117);
    }
    
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }
    
    .log-entry {
        font-family: 'Fira Code', monospace;
        font-size: 0.85rem;
        padding: 5px 10px;
        border-left: 3px solid #4b6cb7;
        margin-bottom: 5px;
        background: rgba(75, 108, 183, 0.05);
    }
    
    .metric-card {
        text-align: center;
        padding: 15px;
        background: rgba(75, 108, 183, 0.1);
        border-radius: 10px;
        border: 1px solid rgba(75, 108, 183, 0.3);
    }
    
    .source-tag {
        display: inline-block;
        padding: 2px 8px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 4px;
        font-size: 0.75rem;
        margin-bottom: 4px;
        color: #aaa;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=80)
    st.markdown("### Research Control")
    st.info("System Level: Phase 4 (Reliability Layer)")
    st.markdown("---")
    backend_url = st.text_input("API Gateway", value="http://localhost:8000/research")
    st.markdown("---")
    st.markdown("#### Engine Capabilities")
    st.checkbox("Tavily AI Search", value=True, disabled=True)
    st.checkbox("Parallel Extraction", value=True, disabled=True)
    st.checkbox("Auto-Ranking", value=True, disabled=True)
    st.checkbox("Self-Critique Loop", value=True, disabled=True)

# --- Main UI ---
st.markdown("<h1 class='main-header'>Autonomous Research Analyst</h1>", unsafe_allow_html=True)
st.markdown("Generate high-fidelity, peer-reviewed research reports using multi-agent orchestration.")

query = st.text_input("What would you like to research today?", placeholder="e.g., Deep dive into the economic impact of Room-Temperature Superconductors")

if st.button("🚀 Begin Research Pipeline"):
    if not query:
        st.warning("Please specify a research topic.")
    else:
        with st.status("Initializing Multi-Agent Workflow...", expanded=True) as status:
            try:
                start_time = time.time()
                status.write("📡 Connecting to Research Engine...")
                response = requests.post(backend_url, json={"query": query})
                
                if response.status_code == 200:
                    data = response.json()
                    duration = time.time() - start_time
                    
                    status.update(label=f"Analysis Complete in {duration:.1f}s", state="complete", expanded=False)
                    
                    # --- Layout ---
                    col_main, col_stats = st.columns([2.5, 1])
                    
                    with col_main:
                        st.markdown("### 📄 Final Research Report")
                        st.markdown(f"<div class='card'>{data['final_report']}</div>", unsafe_allow_html=True)
                        
                        st.download_button(
                            label="Export Report (Markdown)",
                            data=data['final_report'],
                            file_name=f"research_{int(time.time())}.md",
                            mime="text/markdown"
                        )
                    
                    with col_stats:
                        st.markdown("### 📊 Metrics")
                        m_col1, m_col2 = st.columns(2)
                        with m_col1:
                            st.markdown(f"<div class='metric-card'><small>Confidence</small><br/><b>{data['confidence_score']*100:.0f}%</b></div>", unsafe_allow_html=True)
                        with m_col2:
                            st.markdown(f"<div class='metric-card'><small>Sources</small><br/><b>{len(data.get('ranked_sources', []))}</b></div>", unsafe_allow_html=True)
                        
                        st.markdown("---")
                        st.markdown("#### 🛠️ Execution Trace")
                        log_container = st.container(height=300)
                        for log in data['logs']:
                            log_container.markdown(f"<div class='log-entry'>{log}</div>", unsafe_allow_html=True)
                        
                        with st.expander("Show Ranked Sources"):
                            for source in data.get('ranked_sources', []):
                                st.markdown(f"<div class='source-tag'>{source}</div>", unsafe_allow_html=True)
                else:
                    status.update(label="System Error", state="error")
                    st.error(f"Engine Exception: {response.text}")
            except Exception as e:
                status.update(label="Gateway Timeout", state="error")
                st.error(f"Communication Failure: {e}")

st.markdown("---")
st.caption("Powered by LangGraph, FastAPI, and Tavily AI. Built for Phase 4 Reliability.")
