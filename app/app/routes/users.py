from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.user import User
from app.schemas.user import UserDB, UserCreate
from app.cruds import user as UserOperations
from app.connection import get_db

router = APIRouter()

@router.post("/", response_model=UserDB)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserOperations.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return UserOperations.create_user(db=db, user=user)


@router.get("/", response_model=List[UserDB])
def get_users(db: Session = Depends(get_db)):
    return UserOperations.get_users(db)


@router.get("/{id}", response_model=UserDB)
def get_user(id: int, db: Session = Depends(get_db)):
    user = UserOperations.get_user(db, id)
    if not user:
        raise HTTPException(404, "User not found.")
    return user


@router.put("/{id}", response_model=UserDB)
def update_user(id: int, payload: UserDB, db: Session = Depends(get_db)):
    user = UserOperations.get_user(db, id)
    updated_user = UserOperations.update_user(db, user, payload)
    return updated_user


@router.delete("/{id}", response_model=UserDB)
def delete_user(id: int, db: Session = Depends(get_db)):
    user = UserOperations.delete_user(db, id)
    return user
