"""HTTP interface for the existing research report workflow."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from src.main import generate_research_report

app = FastAPI(title="AI Research Assistant API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


class ResearchRequest(BaseModel):
    topic: str = Field(min_length=1, max_length=500)


@app.get("/api/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/research")
def create_research_report(request: ResearchRequest) -> dict:
    topic = request.topic.strip()
    if not topic:
        raise HTTPException(status_code=422, detail="Topic must not be blank.")

    try:
        report = generate_research_report(topic)
        return report.model_dump(mode="json")
    except Exception as exc:
        # Keep implementation details out of the public response. The ASGI server
        # logs the exception for diagnosis.
        raise HTTPException(
            status_code=500,
            detail="Research report generation failed. Check the server logs and API credentials.",
        ) from exc
