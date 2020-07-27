from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.routes.auth import get_current_user
from app.models.account_type import AccountType
from app.schemas.account_type import AccountTypeBase, AccountTypeDB
from app.schemas.user import UserDB
from app.cruds import account_type as AccountTypeOperations
from app.connection import get_db

router = APIRouter()

@router.post("/", response_model=AccountTypeDB, status_code=201)
def create_account_type(account_type: AccountTypeBase, db: Session = Depends(get_db)):
    return AccountTypeOperations.create_account_type(db=db, account_type=account_type)


@router.get("/", response_model=List[AccountTypeDB])
def get_account_types(db: Session = Depends(get_db)):
    return AccountTypeOperations.get_account_types(db)


@router.get("/{id}", response_model=AccountTypeDB)
def get_account_type(id: int, db: Session = Depends(get_db)):
    account_type = AccountTypeOperations.get_account_type(db, id)
    if not account_type:
        raise HTTPException(404, "Account Type not found.")
    return account_type


@router.put("/{id}", response_model=AccountTypeDB)
def update_account_type(id: int, payload: AccountTypeBase, db: Session = Depends(get_db)):
    account_type = AccountTypeOperations.get_account_type(db, id)
    updated_account_type = AccountTypeOperations.update_account_type(db, account_type, payload)
    return updated_account_type


@router.delete("/{id}", response_model=AccountTypeDB)
def delete_account_type(id: int, db: Session = Depends(get_db)):
    account_type = AccountTypeOperations.delete_account_type(db, id)
    return account_type
