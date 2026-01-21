from fastapi import FastAPI
from src.api.routes import profiles, compliance, travel
from src.database.session import engine
from src.database.base import Base

# Initialize Database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Global Compliance Compass API",
    description="Core backend services for automated cross-border tax logic and digital nomad profiles.",
    version="1.0.0"
)

# Include Routers
app.include_router(profiles.router, prefix="/api/v1/profiles", tags=["Profiles"])
app.include_router(travel.router, prefix="/api/v1/travel", tags=["Travel History"])
app.include_router(compliance.router, prefix="/api/v1/compliance", tags=["Compliance Engine"])

@app.get("/health")
async def health_check():
    return {"status": "active", "service": "compass-core-api"}