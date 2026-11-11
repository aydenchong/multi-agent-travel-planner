
from fastapi import FastAPI

app = FastAPI(
    title="VoyageAI API",
    description="Backend API for the VoyageAI Multi-Agent Travel Planner",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "voyageai-api"
    }
