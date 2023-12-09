from fastapi import APIRouter

monitoring_router = APIRouter()


@monitoring_router.get("/status")
def get_status():
    return "OK"
