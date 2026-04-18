from langchain_groq import ChatGroq
from app.models.state import ResearchState
from app.config.settings import settings

llm = ChatGroq(model=settings.MODEL_NAME, groq_api_key=settings.GROQ_API_KEY)

def planner_agent(state: ResearchState):
    """Convert vague query into structured tasks."""
    query = state["query"]
    prompt = f"""You are a research planner. Break down the following research query into 3-5 specific, actionable research tasks.
    Query: {query}
    
    Return the tasks as a list of strings."""
    
    response = llm.invoke(prompt)
    # Simple parsing for Phase 1
    tasks = [line.strip("- ").strip() for line in response.content.split("\n") if line.strip()]
    
    return {
        "tasks": tasks,
        "logs": [f"Planner created {len(tasks)} tasks."]
    }
