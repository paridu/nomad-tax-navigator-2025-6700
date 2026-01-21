from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date

class UserBase(BaseModel):
    email: EmailStr
    home_country_code: str

class UserCreate(UserBase):
    password: str

class TravelEntryCreate(BaseModel):
    country_code: str
    entry_date: date
    exit_date: Optional[date] = None
    purpose: str = "Digital Nomad Work"

class UserProfileResponse(UserBase):
    id: int
    class Config:
        from_attributes = True