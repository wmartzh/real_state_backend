from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import accounts, account_types, auth, banks, users
from app.models import base
from app.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return "Finance App API"

app.mount("/static", StaticFiles(directory="uploads"), name="static")

app.include_router(accounts.router, prefix='/accounts',tags=['accounts'])
app.include_router(account_types.router, prefix='/account_types',tags=['account_types'])
app.include_router(auth.router, prefix='/authenticate', tags=['authenticate'])
app.include_router(banks.router, prefix='/banks', tags=['banks'])
app.include_router(users.router, prefix='/users', tags=['users'])