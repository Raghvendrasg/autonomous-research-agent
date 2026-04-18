# 🧠 Autonomous Research Analyst

A production-grade multi-agent research system built with LangGraph and FastAPI.

## 🚀 Phase 1: Foundation
This version includes the initial multi-agent workflow:
1. **Planner**: Breaks down complex queries into research tasks.
2. **Search**: Conducts web research via DuckDuckGo.
3. **Analyst**: Processes findings into a detailed analysis.

## 🛠️ Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   Copy `.env.example` to `.env` and add your API keys.

4. Run the API:
   ```bash
   python app/main.py
   ```

## 🧪 Testing
Send a POST request to `http://localhost:8000/research` with a JSON body:
```json
{
  "query": "What are the latest breakthroughs in fusion energy as of 2024?"
}
```
