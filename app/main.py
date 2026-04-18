from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.graph.workflow import research_graph

app = FastAPI(title="Autonomous Research Analyst API")

class ResearchRequest(BaseModel):
    query: str

class ResearchResponse(BaseModel):
    query: str
    analysis: str
    logs: list

@app.post("/research", response_model=ResearchResponse)
async def perform_research(request: ResearchRequest):
    try:
        initial_state = {
            "query": request.query,
            "tasks": [],
            "search_results": [],
            "extracted_data": [],
            "analysis": "",
            "confidence_score": 0.0,
            "final_report": "",
            "logs": []
        }
        
        final_state = await research_graph.ainvoke(initial_state)
        
        return ResearchResponse(
            query=final_state["query"],
            analysis=final_state["analysis"],
            logs=final_state["logs"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "Autonomous Research Analyst API is running."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
