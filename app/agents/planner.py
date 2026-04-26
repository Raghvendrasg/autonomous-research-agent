from langchain_groq import ChatGroq
from app.models.state import ResearchState
from app.config.settings import settings

from app.core.logger import logger

llm = ChatGroq(model=settings.MODEL_NAME, groq_api_key=settings.GROQ_API_KEY)

async def planner_agent(state: ResearchState):
    """Convert vague query into structured tasks."""
    query = state["query"]
    logger.info("planner", f"Planning research for query: {query}")
    
    prompt = f"""You are a research planner. Break down the following research query into 3-5 specific, actionable research tasks.
    Query: {query}
    
    Return the tasks as a list of strings. Do not include introductory text, just the list."""
    
    response = await llm.ainvoke(prompt)
    tasks = [line.strip("- ").strip("123456789. ") for line in response.content.split("\n") if line.strip() and len(line) > 10]
    
    logger.info("planner", f"Created {len(tasks)} tasks.")
    
    return {
        "tasks": tasks[:5],
        "logs": [f"Planner created {len(tasks[:5])} research tasks."]
    }
