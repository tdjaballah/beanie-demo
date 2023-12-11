import uvicorn
from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from app.endpoints.employee import employee_router
from app.endpoints.salary import salary_router
from app.schemas.client import Client
from app.schemas.employee import Employee
from app.schemas.salary_view import Salary
from settings import settings

from app.endpoints.monitoring import monitoring_router

app = FastAPI(title="Beanie demo")
app.include_router(monitoring_router)
app.include_router(employee_router)
app.include_router(salary_router)


@app.on_event("startup")
async def startup_event():
    client = AsyncIOMotorClient(str(settings.mongodb_url))
    await init_beanie(database=client.beanie_demo, document_models=[Employee, Client, Salary], recreate_views=True)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=settings.http_port, reload=True)
