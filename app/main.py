import uvicorn
from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from app.endpoints.employee import employee_router
from app.schemas.employee import Employee
from settings import settings


app = FastAPI(title="Beanie demo")
app.include_router(employee_router)


@app.on_event("startup")
async def startup_event():
    client = AsyncIOMotorClient(str(settings.mongodb_url))
    await init_beanie(database=client.beanie_demo, document_models=[Employee], recreate_views=True)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", reload=True)
