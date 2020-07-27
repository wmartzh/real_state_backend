from fastapi import APIRouter, Depends, HTTPException, File, Form, UploadFile
from sqlalchemy.orm import Session
from typing import List

from app.routes.auth import get_current_user
from app.models.bank import Bank
from app.schemas.bank import BankBase, BankDB, BankUpdate
from app.schemas.user import UserDB
from app.cruds import bank as BankOperations
from app.connection import get_db
from app.utils.file import save_uploaded_file, delete_file

router = APIRouter()

@router.post("/", status_code=201)
def create_bank(name: str = Form(...), logo: UploadFile = File(...), db: Session = Depends(get_db)):
    url = save_uploaded_file(logo)
    bank = BankBase(name=name, logo=url)
    return BankOperations.create_bank(db=db, bank=bank)


@router.get("/", response_model=List[BankDB])
def get_banks(db: Session = Depends(get_db)):
    return BankOperations.get_banks(db)


@router.get("/{id}", response_model=BankDB)
def get_bank(id: int, db: Session = Depends(get_db)):
    bank = BankOperations.get_bank(db, id)
    if not bank:
        raise HTTPException(404, "Bank not found.")
    return bank


@router.put("/{id}", response_model=BankDB)
def update_bank(id: int, name: str = Form(None), logo: UploadFile = File(None), db: Session = Depends(get_db)):
    bank = BankOperations.get_bank(db, id)
    payload = BankUpdate(name=name)
    if not bank:
        raise HTTPException(404, "Bank not found.")
    if logo:
        url = save_uploaded_file(logo)
        payload.logo = url
        delete_file(bank.logo)
    updated_bank = BankOperations.update_bank(db, bank, payload)
    return updated_bank


@router.delete("/{id}", response_model=BankDB)
def delete_bank(id: int, db: Session = Depends(get_db)):
    bank = BankOperations.get_bank(db, id)
    if not bank:
        raise HTTPException(404, "Bank not found.")
    bank = BankOperations.delete_bank(db, id)
    delete_file(bank.logo)
    return bank
