from pydantic import Field

from beanie import View

from app.schemas.employee import Employee


class Salary(View):
    job_title: str = Field(alias="_id")
    total_salary: int

    class Settings:
        source = Employee
        pipeline = [
            {
                "$group": {
                    "_id": "$job_title",
                    "nb_employees": {"$sum": 1},
                }
            },
        ]
