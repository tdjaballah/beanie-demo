import pymongo
from beanie import Document, iterative_migration
from pydantic import ConfigDict, Extra


class Employee(Document):
    model_config = ConfigDict(extra=Extra.allow)

    salary: int

    class Settings:
        name = "employees"
        indexes = [
            "job_title",
            [
                ("job_title", pymongo.HASHED),
            ],
        ]


usd_eur = 1.2


class Forward:
    @iterative_migration()
    async def from_eur_to_usd(self, input_document: Employee, output_document: Employee):
        if input_document.salary is not None:
            output_document.salary = int(input_document.salary * usd_eur)


class Backward:
    @iterative_migration()
    async def from_usd_to_eur(self, input_document: Employee, output_document: Employee):
        if input_document.salary is not None:
            output_document.salary = input_document.salary / usd_eur
