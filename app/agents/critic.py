from langchain_groq import ChatGroq
from app.models.state import ResearchState
from app.config.settings import settings
from app.core.logger import logger

llm = ChatGroq(model=settings.MODEL_NAME, groq_api_key=settings.GROQ_API_KEY)

async def critic_agent(state: ResearchState):
    """Detect hallucinations and cross-check claims."""
    query = state["query"]
    analysis = state["analysis"]
    logger.info("critic", "Evaluating research analysis for quality...")
    
    prompt = f"""You are a research critic. Your job is to evaluate the following analysis for accuracy, completeness, and hallucinations.
    
    Original Query: {query}
    Analysis: {analysis}
    
    Evaluate the analysis and provide feedback:
    1. Are there any visible hallucinations?
    2. Is the query fully answered?
    3. What is the confidence score (0.0 to 1.0) for this analysis?
    
    Return your evaluation in the following EXACT format:
    Critique: [Your feedback]
    Score: [0.x]"""
    
    response = await llm.ainvoke(prompt)
    content = response.content
    
    # Extraction logic
    critique = content
    score = 0.8 # Default
    
    if "Score:" in content:
        try:
            import re
            match = re.search(r"Score:\s*([\d\.]+)", content)
            if match:
                score = float(match.group(1))
        except:
            pass
            
    logger.info("critic", f"Critique complete. Confidence Score: {score}")
    
    return {
        "critique": critique,
        "confidence_score": score,
        "logs": [f"Critic agent evaluated the analysis with a confidence score of {score}."]
    }
