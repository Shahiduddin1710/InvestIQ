from pydantic import BaseModel, EmailStr
from typing import Optional


class ForecastRequest(BaseModel):
    ticker: str
    n_days: int
    theme: str = "dark"


class ContactRequest(BaseModel):
    name: str
    email: str
    message: str
