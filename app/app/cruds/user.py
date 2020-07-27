import bcrypt
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserAuthenticate, UserCreate, UserDB


def get_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db:Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = User(name=user.name, email=user.email, password=hashed_password.decode('utf-8'))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user:UserDB, payload: UserDB):
    user = db.query(User).filter(User.id == user.id).first()
    user.name = payload.name
    user.email = payload.email
    db.commit()
    return user

def delete_user(db_session: Session, id: int):
    user = db_session.query(User).filter(User.id == id).first()
    db_session.delete(user)
    db_session.commit()
    return user

def check_user_password(db: Session, user: UserAuthenticate):
    db_user_info: User = get_user_by_email(db, email=user.email)
    return bcrypt.checkpw(user.password.encode('utf-8'), db_user_info.password.encode('utf-8'))