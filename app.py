import streamlit as st
import time
from working.agents import app

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Delhi Transit AI",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. CUSTOM CSS (The "AI Vibe")
# ==========================================
st.markdown("""
    <style>
    /* Hide default Streamlit elements for a cleaner web-app feel */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Sleek Gradient Title */
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #00C9FF, #92FE9D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
        padding-top: 2rem;
    }
    .sub-title {
        text-align: center;
        color: #A0A0A0;
        font-size: 1.1rem;
        margin-bottom: 2.5rem;
        font-family: monospace;
    }
    
    /* Premium Button Glow Effect */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%);
        color: #111111 !important;
        font-weight: 700;
        font-size: 1.1rem;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 0;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 8px 20px rgba(0, 201, 255, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. HEADER
# ==========================================
st.markdown('<h1 class="main-title">Transit Intelligence Engine</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Hybrid LangGraph • NetworkX • LLM Architecture</p>', unsafe_allow_html=True)

# ==========================================
# 4. INPUT DASHBOARD
# ==========================================
# Using columns makes it look more like a professional control panel
col1, col2 = st.columns(2)
with col1:
    start = st.text_input("📍 Origin Point", placeholder="e.g., DTU Campus")
with col2:
    end = st.text_input("🏁 Final Destination", placeholder="e.g., Cyber City, Gurgaon")

st.write("") # Quick spacer

# ==========================================
# 5. EXECUTION & AI ANIMATION
# ==========================================
if st.button("Generate Smart Commute Strategy"):
    if not start or not end:
        st.error("⚠️ Please provide both an origin and a destination.")
    else:
        # The st.status creates a cool expanding box showing the "Agents" working
        with st.status("🧠 Initializing Agentic Pipeline...", expanded=True) as status:
            st.write("📡 Agent 1: NLP Translator extracting location tokens...")
            time.sleep(0.5) # Tiny pause for presentation effect
            
            st.write("🗺️ Agent 2: Querying NetworkX graph dataset for shortest path...")
            
            try:
                # Invoke the LangGraph application backend
                result = app.invoke({"origin": start, "destination": end})
                
                st.write("✨ Agent 3: Synthesizing final commute strategy...")
                time.sleep(0.3)
                
                status.update(label="Strategy Generated Successfully!", state="complete", expanded=False)
                
                # --- DISPLAY RESULTS ---
                st.markdown("---")
                
                # Use Streamlit's success banner for a pop of color
                st.success("Optimal Route Secured") 
                
                st.markdown(result['final_plan'])
                
                st.markdown("---")
                # Expose the raw data for the judges to prove it's not just a standard LLM call
                with st.expander("⚙️ Under the Hood: Agentic State Data"):
                    st.json({
                        "NLP_Resolved_Origin": result.get('resolved_origin', 'N/A'),
                        "NLP_Resolved_Destination": result.get('resolved_dest', 'N/A'),
                        "Graph_Nodes_Traversed": result.get('graph_path', [])
                    })
                    
            except Exception as e:
                status.update(label="Agent Pipeline Failed", state="error", expanded=True)
                st.error(f"Critical System Error: {e}")