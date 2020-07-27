from typing import List, Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    name: Optional[str]


class UserCreate(UserBase):
    password: str


class UserAuthenticate(BaseModel):
    email: str
    password: str


class UserDB(UserBase):
    id: int
    class Config:
        orm_mode = True