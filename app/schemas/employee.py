from enum import Enum
from typing import Optional

from beanie import Document
from pydantic import BaseModel


class JobTitle(str, Enum):
    sd = 'Software Developer'
    ml = 'Machine Learning Engineer'
    de = 'Data Engineer'


class Address(BaseModel):
    zipcode: int
    country: str


class EmployeeCreate(BaseModel):
    name: str
    job_title: JobTitle
    salary: Optional[int] = None
    address: Address


class Employee(Document, EmployeeCreate):
    class Settings:
        name = "employees"
