import asyncio
from langchain_groq import ChatGroq
from app.models.state import ResearchState
from app.config.settings import settings
from app.core.logger import logger

llm = ChatGroq(model=settings.MODEL_NAME, groq_api_key=settings.GROQ_API_KEY)

async def ranker_agent(state: ResearchState):
    """Rank extracted data by relevance and eliminate noise."""
    query = state["query"]
    extracted_data = state["extracted_data"]
    
    if not extracted_data:
        return {"ranked_sources": [], "logs": ["Ranker: No data to rank."]}

    # Combine data for ranking
    prompt = f"""You are a research quality controller. Rank the following extracted findings based on their relevance and importance to the research query: '{query}'
    
    Findings:
    {chr(10).join([f"- {item}" for item in extracted_data])}
    
    Select and rank the top 10 most relevant findings. 
    Return them as a numbered list. Do not include any other text."""
    
    try:
        logger.info("ranker", "Ranking extracted information for relevance...")
        response = await llm.ainvoke(prompt)
        ranked_list = [line.strip() for line in response.content.split("\n") if line.strip() and (line[0].isdigit() or line[0] == '-')]
        
        return {
            "ranked_sources": ranked_list,
            "logs": ["Ranker agent prioritized the most relevant sources."]
        }
    except Exception as e:
        logger.error("ranker", f"Ranking failed: {e}")
        # Fallback: just use the extracted data as is
        return {
            "ranked_sources": extracted_data[:10],
            "logs": ["Ranker: Used fallback due to error."]
        }
