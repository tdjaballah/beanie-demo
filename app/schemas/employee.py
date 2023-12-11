from __future__ import annotations

from enum import Enum
from typing import Optional

import pymongo
from beanie import Document, Link
from pydantic import BaseModel, Field

from app.schemas.client import Client


class JobTitle(str, Enum):
    ceo = 'CEO'
    cto = 'CTO'
    dev = 'Business developer'


class Address(BaseModel):
    zipcode: int
    country: str


class EmployeeSummary(BaseModel):
    name: str
    job_title: JobTitle


class EmployeeCreate(EmployeeSummary):
    salary: Optional[int] = None
    address: Address
    client: list[Link[Client]] = Field(default_factory=list)
    reports_to: Optional[EmployeeCreate] = None


EmployeeCreate.model_rebuild()


class Employee(Document, EmployeeCreate):
    reports_to: Optional[Link[Employee]]

    class Settings:
        name = "employees"
        indexes = [
            "job_title",
            [
                ("job_title", pymongo.HASHED),
            ],
        ]


Employee.model_rebuild()
