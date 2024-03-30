from starlette import status
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from models import Users
from database import  SessionLocal
from .auth import get_current_user


router = APIRouter(
    prefix='/users',
    tags=['users']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency =  Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get('/', status_code=status.HTTP_200_OK)
async def read_data(user: user_dependency,
                   db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='authentication failed')
    return db.query(Users).filter(Users.id == user.get('id')).first()