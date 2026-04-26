import asyncio
from tavily import TavilyClient
from app.models.state import ResearchState
from app.config.settings import settings
from app.core.logger import logger

tavily = TavilyClient(api_key=settings.TAVILY_API_KEY)

async def search_query(query: str):
    """Perform a single search query using Tavily."""
    logger.info("search", f"Running search for: {query}")
    response = await asyncio.to_thread(
        tavily.search, 
        query=query, 
        search_depth="advanced", 
        max_results=3
    )
    return response

async def search_agent(state: ResearchState):
    """Execute search tasks in parallel."""
    tasks = state["tasks"]
    logger.info("search", f"Executing {len(tasks)} parallel tasks...")
    
    # Execute all search tasks in parallel
    search_tasks = [search_query(task) for task in tasks]
    search_results = await asyncio.gather(*search_tasks)
    
    # Flatten and format results for the extractor
    formatted_results = []
    for res in search_results:
        for item in res.get("results", []):
            formatted_results.append(f"Source: {item['url']}\nContent: {item['content']}")
    
    logger.info("search", f"Found {len(formatted_results)} search results.")
    
    return {
        "search_results": formatted_results,
        "logs": [f"Search agent performed {len(tasks)} parallel searches via Tavily."]
    }
