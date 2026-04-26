from langchain_groq import ChatGroq
from app.models.state import ResearchState
from app.config.settings import settings
from app.core.logger import logger

llm = ChatGroq(model=settings.MODEL_NAME, groq_api_key=settings.GROQ_API_KEY)

async def writer_agent(state: ResearchState):
    """Generate final structured report."""
    query = state["query"]
    analysis = state["analysis"]
    critique = state["critique"]
    logger.info("writer", "Generating final research report...")
    
    prompt = f"""You are a professional report writer. Generate a final structured research report based on the following analysis and critique.
    
    Original Query: {query}
    Analysis: {analysis}
    Critique: {critique}
    
    The report should include:
    - Executive Summary
    - Key Insights
    - Detailed Findings
    - Risks and Limitations
    - Conclusion
    
    IMPORTANT: Format the report in BEAUTIFUL Markdown. Use headers, bold text, and lists for readability."""
    
    response = await llm.ainvoke(prompt)
    logger.info("writer", "Final report generated.")
    
    return {
        "final_report": response.content,
        "logs": ["Writer agent generated the final report asynchronously."]
    }
