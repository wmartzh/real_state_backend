from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    account_type_id = Column(Integer, ForeignKey("account_types.id"))
    bank_id = Column(Integer, ForeignKey("banks.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    balance = Column(Float)

    account_type = relationship("AccountType", backref="account_type")
    bank = relationship("Bank", backref="user")