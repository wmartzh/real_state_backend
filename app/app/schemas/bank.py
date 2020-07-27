from pydantic import BaseModel
from typing import Optional

class BankBase(BaseModel):
    name: str
    logo: str


class BankUpdate(BaseModel):
    name: Optional[str]
    logo: Optional[str]


class BankDB(BankBase):
    id: int

    class Config:
        orm_mode = True