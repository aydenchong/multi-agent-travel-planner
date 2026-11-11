from fastapi import FastAPI

from backend.app.schemas.trip import TripRequest


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


@app.post("/api/v1/trips/validate")
def validate_trip(request: TripRequest):
    return {
        "valid": True,
        "message": "Trip request validated successfully",
        "trip": request.model_dump(mode="json")
    }
