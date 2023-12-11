from typing import List

from fastapi import APIRouter

from app.schemas.salary_view import Salary

salary_router = APIRouter(prefix="/salary", tags=["Salary"])


@salary_router.get("/")
async def get_all() -> List[Salary]:
    salaries = await Salary.find_all().to_list()
    return salaries
