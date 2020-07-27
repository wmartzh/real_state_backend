from sqlalchemy.orm import Session
from app.models.bank import Bank
from app.schemas.bank import BankBase, BankDB, BankUpdate


def get_banks(db: Session):
    return db.query(Bank).all()

def get_bank(db: Session, bank_id: int):
    return db.query(Bank).filter(Bank.id == bank_id).first()

def create_bank(db: Session, bank: BankBase):
    db_bank = Bank(name=bank.name, logo=bank.logo)
    db.add(db_bank)
    db.commit()
    db.refresh(db_bank)
    return db_bank

def update_bank(db: Session, bank:BankDB, payload: BankUpdate):
    bank = db.query(Bank).filter(Bank.id == bank.id).first()
    if payload.name:
        bank.name = payload.name
    if payload.logo:
        bank.logo = payload.logo
    db.commit()
    return bank

def delete_bank(db_session: Session, id: int):
    bank = db_session.query(Bank).filter(Bank.id == id).first()
    db_session.delete(bank)
    db_session.commit()
    return bank