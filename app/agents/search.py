from langchain_community.tools import DuckDuckGoSearchRun
from app.models.state import ResearchState

search_tool = DuckDuckGoSearchRun()

def search_agent(state: ResearchState):
    """Execute search tasks."""
    tasks = state["tasks"]
    results = []
    
    for task in tasks:
        search_result = search_tool.run(task)
        results.append(search_result)
    
    return {
        "search_results": results,
        "logs": [f"Search agent performed {len(tasks)} searches."]
    }
