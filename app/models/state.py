from typing import TypedDict, List, Annotated
import operator

class ResearchState(TypedDict):
    query: str
    tasks: List[str]
    search_results: Annotated[List[str], operator.add]
    extracted_data: Annotated[List[str], operator.add]
    ranked_sources: List[str]
    analysis: str
    critique: str
    confidence_score: float
    final_report: str
    retries: int
    logs: Annotated[List[str], operator.add]
