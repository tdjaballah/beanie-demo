from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException

from app.schemas.employee import Employee, EmployeeCreate

employee_router = APIRouter(prefix="/employee", tags=["Employee"])


@employee_router.post("/")
async def add(employee: EmployeeCreate) -> Employee:
    employee = await Employee(**employee.model_dump()).insert()
    return employee


@employee_router.get("/{employee_id}")
async def get(employee_id: PydanticObjectId) -> Employee:
    if (employee := await Employee.get(employee_id)) is not None:
        return employee
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Employee with id: {employee_id} not found!"
        )


@employee_router.get("/")
async def get_all() -> List[Employee]:
    employees = await Employee.find_all().to_list()
    return employees


@employee_router.delete("/{employee_id}")
async def delete(employee_id: PydanticObjectId) -> Employee:
    if (employee := await Employee.get(employee_id)) is not None:
        await employee.delete()
        return employee
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Employee with id: {employee_id} not found!"
        )


@employee_router.delete("/")
async def delete_all() -> None:
    await Employee.delete_all()
    return None
