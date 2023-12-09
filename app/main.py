import uvicorn
from fastapi import FastAPI
from settings import settings

from app.endpoints.monitoring import monitoring_router

app = FastAPI(title="Beanie demo")
app.include_router(monitoring_router)


@app.on_event("startup")
async def startup_event():
    pass


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=settings.http_port, reload=True)
