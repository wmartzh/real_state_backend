from sqlalchemy import Column,Integer, String
from app.db import Base


class AccountType(Base):
  __tablename__ = "account_types"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)