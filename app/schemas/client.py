from enum import Enum

from beanie import Document


class BusinessSegment(str, Enum):
    ind = 'Industry'
    ser = 'Service'
    agr = 'Agriculture'


class Client(Document):
    name: str
    business_segment: BusinessSegment

    class Settings:
        name = "clients"

