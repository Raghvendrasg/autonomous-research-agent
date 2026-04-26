from langchain_groq import ChatGroq
from app.models.state import ResearchState
from app.config.settings import settings

from app.core.logger import logger

llm = ChatGroq(model=settings.MODEL_NAME, groq_api_key=settings.GROQ_API_KEY)

async def analyst_agent(state: ResearchState):
    """Analyze ranked data and generate insights."""
    query = state["query"]
    ranked_sources = state["ranked_sources"]
    
    context = "\n\n".join(ranked_sources)
    prompt = f"""You are a senior research analyst. Based on the following prioritized research findings, provide a comprehensive, deep-dive analysis for the query: '{query}'
    
    Ranked Findings:
    {context}
    
    Provide your analysis in a professional tone, focusing on facts, emerging trends, and synthesized conclusions."""
    
    logger.info("analyst", "Generating deep-dive analysis from ranked sources...")
    response = await llm.ainvoke(prompt)
    
    return {
        "analysis": response.content,
        "logs": ["Analyst agent synthesized research insights from prioritized findings."]
    }
