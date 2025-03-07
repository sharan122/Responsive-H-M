# mutations/add_user.py

import datetime
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate
from fastapi import HTTPException

def add_user(db: Session, user: UserCreate):
    db_user = User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        created_at=datetime.datetime.utcnow()
    )
    
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Username or email already exists.")