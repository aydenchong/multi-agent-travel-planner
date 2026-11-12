from fastapi import FastAPI
from backend.app.core.config import get_settings
from backend.app.schemas.trip import TripRequest
from backend.app.api.chat import router as chat_router

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description="Backend API for the VoyageAI Multi-Agent Travel Planner",
    version="0.1.0",
    debug=settings.debug,
)
app.include_router(chat_router)

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
