import asyncio
from langchain_groq import ChatGroq
from app.models.state import ResearchState
from app.config.settings import settings
from app.core.logger import logger

llm = ChatGroq(model=settings.MODEL_NAME, groq_api_key=settings.GROQ_API_KEY)

async def extract_info(result: str, query: str):
    """Extract relevant information from a single search result."""
    logger.info("extractor", f"Extracting from: {result[:50]}...")
    prompt = f"""Extract the most relevant information from the following text related to the query: '{query}'
    
    Text:
    {result}
    
    Extracted relevant information (keep it concise and objective):"""
    
    response = await llm.ainvoke(prompt)
    return response.content

async def extractor_agent(state: ResearchState):
    """Process all search results in parallel to extract relevant insights."""
    search_results = state["search_results"]
    query = state["query"]
    logger.info("extractor", f"Processing {len(search_results)} search results...")
    
    # Process all extractions in parallel
    extraction_tasks = [extract_info(res, query) for res in search_results]
    extracted_data = await asyncio.gather(*extraction_tasks)
    
    logger.info("extractor", "Extraction complete.")
    
    return {
        "extracted_data": extracted_data,
        "logs": [f"Extractor agent processed {len(search_results)} results in parallel."]
    }
