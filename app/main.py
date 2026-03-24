from fastapi import FastAPI
from app.schemas import TextInput, TextAnalysisResponse
from app.analyzer import analyze_text

app = FastAPI(
    title="TextInsight API", description="API to analyze text metrics", version="1.0.0"
)


@app.post("/analyze", response_model=TextAnalysisResponse)
async def post_analyze(data: TextInput):
   """
    Receives text data and returns the analysis results.
    """
    results = analyze_text(data.content)
    return results
