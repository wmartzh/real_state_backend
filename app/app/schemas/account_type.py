from pydantic import BaseModel


class AccountTypeBase(BaseModel):
    name: str


class AccountTypeDB(AccountTypeBase):
    id: int

    class Config:
      orm_mode = True