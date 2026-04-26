# 🔬 Autonomous Research Analyst PRO

A production-grade multi-agent research system built with **LangGraph**, **FastAPI**, and **Tavily AI**.

> [!NOTE]
> **Current Status: Phase 4 (Reliability Layer)**
> This version includes parallel execution, advanced source ranking, and a premium Streamlit interface.

## 🚀 Features

1.  **Planner**: Breaks down complex queries into structured research tasks.
2.  **Parallel Search**: Conducts deep web research via **Tavily AI** (Parallelized).
3.  **Smart Extractor**: Asynchronously extracts relevant insights from search results.
4.  **Ranker**: Prioritizes the top findings using LLM-based relevance scoring.
5.  **Analyst**: Synthesizes structured insights from prioritized data.
6.  **Critic**: Self-evaluates the analysis and triggers retries if confidence is < 70%.
7.  **Writer**: Generates a professional, structured Markdown report.

---

## 🛠️ Setup & Installation

### 1. Environment Preparation
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration
Copy `.env.example` to `.env` and add your API keys:
- `GROQ_API_KEY`: For high-speed LLM inference.
- `TAVILY_API_KEY`: For advanced research search.

---

## 🏃 Running the Application

To run the full system, you need to start both the backend and the frontend.

### Step 1: Start the FastAPI Backend
```bash
# From the root directory
uvicorn app.main:app
```
The API will be available at `http://localhost:8000`. You can view the automated docs at `http://localhost:8000/docs`.

### Step 2: Start the Streamlit Frontend
Open a **new terminal** and run:
```bash
# Activate venv if needed
source venv/bin/activate # On Windows: venv\Scripts\activate

# Launch Streamlit
streamlit run frontend/streamlit_app.py
```
The UI will automatically open in your browser (usually at `http://localhost:8501`).

---

## 🧪 API Usage (Optional)
You can interact with the research engine directly via CURL:
```bash
curl -X POST http://localhost:8000/research \
-H "Content-Type: application/json" \
-d '{"query": "Future of quantum computing in 2025"}'
```

---

## 🗺️ Project Roadmap
- [x] Phase 1: Foundation (Planner + Search)
- [x] Phase 2: Orchestration (Analyst + Critic)
- [x] Phase 3: Performance (Parallel Execution + Tavily)
- [x] Phase 4: Reliability (Ranker + Structured Logging)
- [ ] Phase 5: Production (Redis Caching + Streaming)
- [ ] Phase 6: Scaling (Docker + MCP)

Built with ❤️ using LangGraph.
