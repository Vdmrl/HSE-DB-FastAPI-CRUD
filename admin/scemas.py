from datetime import datetime, timezone
from pydantic import BaseModel, validator

class Member(BaseModel):
    surname: str
    name: str
    patronymic: str
    birth_date: str