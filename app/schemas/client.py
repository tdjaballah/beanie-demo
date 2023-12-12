from enum import Enum

from beanie import Document
from pydantic import BaseModel


class BusinessSegment(str, Enum):
    ind = 'Industry'
    ser = 'Services'


class ClientCreate(BaseModel):
    name: str
    business_segment: BusinessSegment


class Client(Document, ClientCreate):
    class Settings:
        name = "clients"

