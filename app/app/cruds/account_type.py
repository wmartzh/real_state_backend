from sqlalchemy.orm import Session
from app.models.account_type import AccountType
from app.schemas.account_type import AccountTypeBase, AccountTypeDB


def get_account_types(db: Session):
    return db.query(AccountType).all()

def get_account_type(db: Session, account_type_id: int):
    return db.query(AccountType).filter(AccountType.id == account_type_id).first()

def create_account_type(db: Session, account_type: AccountTypeBase):
    db_account_type = AccountType(name=account_type.name)
    db.add(db_account_type)
    db.commit()
    db.refresh(db_account_type)
    return db_account_type

def update_account_type(db: Session, account_type:AccountTypeDB, payload: AccountTypeBase):
    account_type = db.query(AccountType).filter(AccountType.id == account_type.id).first()
    account_type.name = payload.name
    db.commit()
    return account_type

def delete_account_type(db_session: Session, id: int):
    account_type = db_session.query(AccountType).filter(AccountType.id == id).first()
    db_session.delete(account_type)
    db_session.commit()
    return account_type