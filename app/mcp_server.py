from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.learner import load_learned, save_learned
from app.retriever import retrieve_context
from app.llm_interface import ask_llm
from app.config import load_config
import uvicorn

config = load_config()
app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    learn: bool = True

@app.post("/query")
def query_logs(request: QueryRequest):
    query = request.query
    learned = load_learned()
    
    for entry in learned:
        if query.lower() in entry["query"].lower():
            return {"answer": entry["answer"], "source": "learned"}

    ctx_ids = retrieve_context(query)
    context = "\n".join([f"Context entry {i}" for i in ctx_ids])  # Replace with real text if available
    full_prompt = f"{context}\n\n{query}"
    answer = ask_llm(full_prompt)

    if request.learn and config.get("learning", True):
        save_learned(query, answer)

    return {"answer": answer, "source": "llm"}

@app.get("/")
def root():
    return {"message": "Wireshark RAG Analyst MCP API is running."}

def start_mcp_server():
    uvicorn.run("app.mcp_server:app", host="0.0.0.0", port=8080, reload=False)
