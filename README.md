One Delhi: Agentic Transit Journey Simulator
One Delhi is an agentic transit journey simulator for the Delhi NCR region. By utilizing a LangGraph-orchestrated multi-agent pipeline, this project bridges the gap between deterministic graph-based transit routing (NetworkX) and the contextual reasoning capabilities of Large Language Models (OpenAI).

🚇 Project Overview
Traditional transit apps are rigid and break when data is missing. One Delhi solves this by simulating how humans navigate—using AI to reason through transit networks, suggest precise station exits, and calculate dynamic last-mile fare estimates in real-time.

🛠 Tech Stack
Language: Python 3.14

Orchestration: LangGraph, LangChain

LLM Backend: OpenAI (GPT-4o/GPT-4o-mini)

Graph Engine: NetworkX (Dijkstra’s Algorithm)

Frontend: Streamlit

Deployment: Streamlit Community Cloud

🤖 The 4-Agent Workflow
The application processes transit requests through a robust, state-managed pipeline:

Agent 1 (NLP Translator): Standardizes chaotic user inputs into clean location tokens.

Agent 2 (Graph Router): Queries a local .gpickle transit graph, utilizing a multi-property fuzzy matcher and shortest-path algorithms.

Agent 3 (Last-Mile Engine): Calculates dynamic last-mile fares based on time-of-day and regional Delhi NCR rates.

Agent 4 (Strategy Formatter): Compiles the complex state into a polished, markdown-formatted commuter itinerary.

📂 Project Structure
Plaintext
One-Delhi-Deploy/
├── app.py                # Main Streamlit frontend
├── requirements.txt      # Project dependencies
├── .gitignore            # Excludes venv, .env, and large data files
├── working/
│   ├── agents.py         # 4-agent logic & LangGraph state machine
│   ├── state.py          # State definitions
│   ├── config.py         # LLM & environment configuration
│   └── combined_network.gpickle  # Serialized Delhi Metro graph
└── .streamlit/
    └── secrets.toml      # Secure storage for API keys
🚀 How to Run Locally
Clone the repository:

Bash
git clone https://github.com/dominatingspirit/One-Delhi-Deploy.git
cd One-Delhi-Deploy
Install dependencies:

Bash
pip install -r requirements.txt
Set your API Key:
Create a .env file in the root folder and add:

Plaintext
OPENAI_API_KEY=your_key_here
Launch the app:

Bash
streamlit run app.py
📜 Credits
Developed by Krishna Anand (CSE, DTU) as a dynamic, software-only transit optimization solution for the Delhi NCR region
