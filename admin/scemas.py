from datetime import datetime, timezone
from pydantic import BaseModel, validator

class Member_to_insert(BaseModel):
    surname: str
    name: str
    patronymic: str
    birth_date: str

class Member_to_delete(BaseModel):
    id: int