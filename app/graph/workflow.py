from langgraph.graph import StateGraph, END
from app.models.state import ResearchState
from app.agents.planner import planner_agent
from app.agents.search import search_agent
from app.agents.extractor import extractor_agent
from app.agents.ranker import ranker_agent
from app.agents.analyst import analyst_agent
from app.agents.critic import critic_agent
from app.agents.writer import writer_agent

def critic_router(state: ResearchState):
    """Route to writer or search based on confidence score and retry count."""
    if state.get("confidence_score", 0) < 0.7 and state.get("retries", 0) < 2:
        return "planner" # Retry from planner to refine tasks
    return "writer"

def increment_retries(state: ResearchState):
    """Simple node to increment retries."""
    return {"retries": state.get("retries", 0) + 1}

def create_workflow():
    workflow = StateGraph(ResearchState)
    
    # Add nodes
    workflow.add_node("planner", planner_agent)
    workflow.add_node("search", search_agent)
    workflow.add_node("extractor", extractor_agent)
    workflow.add_node("ranker", ranker_agent)
    workflow.add_node("analyst", analyst_agent)
    workflow.add_node("critic", critic_agent)
    workflow.add_node("writer", writer_agent)
    workflow.add_node("increment_retries", increment_retries)
    
    # Add edges
    workflow.set_entry_point("planner")
    workflow.add_edge("planner", "search")
    workflow.add_edge("search", "extractor")
    workflow.add_edge("extractor", "ranker")
    workflow.add_edge("ranker", "analyst")
    workflow.add_edge("analyst", "critic")
    
    # Conditional routing from critic
    workflow.add_conditional_edges(
        "critic",
        critic_router,
        {
            "planner": "increment_retries",
            "writer": "writer"
        }
    )
    
    workflow.add_edge("increment_retries", "planner")
    workflow.add_edge("writer", END)
    
    return workflow.compile()

research_graph = create_workflow()
