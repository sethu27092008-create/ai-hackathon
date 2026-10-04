from fastapi import FastAPI, HTTPException
from schemas import SummaryRequest, SummaryResponse
from prompts import summary_prompt
from llm import ask_llm

app = FastAPI(title="AI Summarizer")


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/summarize", response_model=SummaryResponse)
def summarize(req: SummaryRequest):
    try:
        prompt = summary_prompt(req.text, req.style)
        result = ask_llm(prompt)
        return SummaryResponse(summary=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))