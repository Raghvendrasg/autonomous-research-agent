from langchain_groq import ChatGroq
from app.models.state import ResearchState
from app.config.settings import settings

llm = ChatGroq(model=settings.MODEL_NAME, groq_api_key=settings.GROQ_API_KEY)

def analyst_agent(state: ResearchState):
    """Analyze search results and generate insights."""
    query = state["query"]
    search_results = state["search_results"]
    
    context = "\n\n".join(search_results)
    prompt = f"""You are a research analyst. Based on the following search results, provide a comprehensive analysis for the query: '{query}'
    
    Search Results:
    {context}
    
    Detailed Analysis:"""
    
    response = llm.invoke(prompt)
    
    return {
        "analysis": response.content,
        "logs": ["Analyst agent generated research insights."]
    }
