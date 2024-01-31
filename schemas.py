import datetime
from typing import Any
import pydantic

class Basereg(pydantic.BaseModel):
    name: str
    email: str
    date_of_birth: datetime.date

class Registration(Basereg):
    id: int
    date_created: datetime.datetime

    class Config:
        from_attributes = True  

@classmethod
def model_load(cls, obj: Any) -> dict:
    data = {column.name: getattr(obj, column.name) for column in obj.__table__.columns}
    return data

class CreateRegistration(Basereg):
    pass

class Message(pydantic.BaseModel):
    detail: str