from langgraph.graph import StateGraph, END
from app.models.state import ResearchState
from app.agents.planner import planner_agent
from app.agents.search import search_agent
from app.agents.analyst import analyst_agent

def create_workflow():
    workflow = StateGraph(ResearchState)
    
    # Add nodes
    workflow.add_node("planner", planner_agent)
    workflow.add_node("search", search_agent)
    workflow.add_node("analyst", analyst_agent)
    
    # Add edges
    workflow.set_entry_point("planner")
    workflow.add_edge("planner", "search")
    workflow.add_edge("search", "analyst")
    workflow.add_edge("analyst", END)
    
    return workflow.compile()

research_graph = create_workflow()
