from fastapi import FastAPI
from src.core.config import settings
from src.api.routes import router as telemetry_router
from src.api.websockets import router as websocket_router

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(telemetry_router)
app.include_router(websocket_router)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "project": settings.PROJECT_NAME}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
