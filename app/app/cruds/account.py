from sqlalchemy.orm import Session
from app.models.account import Account
from app.schemas.account import AccountBase, AccountCreate, AccountDB, AccountUpdate


def get_accounts(db: Session):
    return db.query(Account).all()

def get_account(db: Session, account_id: int):
    return db.query(Account).filter(Account.id == account_id).first()

def create_account(db: Session, account: AccountCreate):
    db_account_type = Account(
      name=account.name,
      balance=account.balance,
      account_type_id=account.account_type_id,
      bank_id=account.bank_id,
      user_id=account.user_id
    )
    db.add(db_account_type)
    db.commit()
    db.refresh(db_account_type)
    return db_account_type

def update_account(db: Session, account_type: AccountDB, payload: AccountUpdate):
    account = db.query(Account).filter(Account.id == account_type.id).first()
    if payload.name:
        account.name = payload.name
    if payload.balance:
        account.balance = payload.balance
    if payload.account_type_id:
        account.account_type_id = payload.account_type_id
    if payload.bank_id:
        account.bank_id = payload.bank_id
    db.commit()
    return account_type

def delete_account(db_session: Session, id: int):
    account = db_session.query(Account).filter(Account.id == id).first()
    db_session.delete(account)
    db_session.commit()
    return account