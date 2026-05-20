from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from executor import run_pipeline

app = FastAPI(title="Mini SQL Agent API")

class QueryRequest(BaseModel):
    question: str

class AgentResponse(BaseModel):
    sql: str
    result: list | int | float | None
    summary: str
    status: str
    
def generate_summary(result_data, question):
    """
    Very basic heuristic summary generator.
    In a real app, this would be an LLM call.
    """
    if not result_data:
        return "I could not find any results for your query."
    
    if isinstance(result_data, list) and len(result_data) == 1:
        row = result_data[0]
        if len(row) == 1:
            val = list(row.values())[0]
            if "count" in question.lower() or "how many" in question.lower():
                return f"There are {val} items matching your request."
            elif "sum" in question.lower() or "total" in question.lower():
                return f"The total is {val}."
            return f"The answer is {val}."
            
    return f"I found {len(result_data)} records matching your request."

@app.post("/agent/sql", response_model=AgentResponse)
async def handle_sql_agent(req: QueryRequest):
    # Task 4 specifies max 3 retries
    res = run_pipeline(req.question, max_retries=3)
    
    if res["status"] == "failed":
        return AgentResponse(
            sql=res["sql"],
            result=None,
            summary="Failed to execute query after retries.",
            status="failed"
        )
        
    summary = generate_summary(res["result"], req.question)
    
    # If the result is a single value, try to unpack it to match the expected example format
    final_result = res["result"]
    if isinstance(final_result, list) and len(final_result) == 1 and len(final_result[0]) == 1:
        final_result = list(final_result[0].values())[0]
        
    return AgentResponse(
        sql=res["sql"],
        result=final_result,
        summary=summary,
        status="success"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
