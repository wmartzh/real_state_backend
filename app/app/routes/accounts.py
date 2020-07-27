from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.routes.auth import get_current_user
from app.models.account import Account
from app.schemas.account import AccountBase, AccountDB, AccountCreate, AccountUpdate
from app.schemas.user import UserDB
from app.cruds import account as AccountOperations
from app.connection import get_db

router = APIRouter()

@router.post("/", response_model=AccountDB, status_code=201)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    return AccountOperations.create_account(db=db, account=account)


@router.get("/", response_model=List[AccountDB])
def get_accounts(db: Session = Depends(get_db)):
    return AccountOperations.get_accounts(db)


@router.get("/{id}", response_model=AccountDB)
def get_account(id: int, db: Session = Depends(get_db)):
    account = AccountOperations.get_account(db, id)
    if not account:
        raise HTTPException(404, "Account not found.")
    return account


@router.put("/{id}", response_model=AccountDB)
def update_account(id: int, payload: AccountUpdate, db: Session = Depends(get_db)):
    account = AccountOperations.get_account(db, id)
    if not account:
        raise HTTPException(404, "Account not found.")
    updated_account = AccountOperations.update_account(db, account, payload)
    return updated_account


@router.delete("/{id}", response_model=AccountDB)
def delete_account(id: int, db: Session = Depends(get_db)):
    account = AccountOperations.get_account(db, id)
    if not account:
        raise HTTPException(404, "Account not found.")
    account = AccountOperations.delete_account(db, id)
    return account