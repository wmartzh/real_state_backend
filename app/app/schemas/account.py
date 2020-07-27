from pydantic import BaseModel
from typing import Optional

from .account_type import AccountTypeDB
from .bank import BankDB


class AccountBase(BaseModel):
    name: str
    balance: float
    account_type_id: int
    bank_id: Optional[int]


class AccountCreate(AccountBase):
    user_id: int


class AccountUpdate(BaseModel):
    name: Optional[str]
    balance: Optional[float]
    account_type_id: Optional[int]
    bank_id: Optional[int]


class AccountDB(AccountCreate):
    id: int

    class Config:
        orm_mode = True

class AccountDBwithRelations(AccountDB):
    account_type: AccountTypeDB
    bank: Optional[BankDB]
