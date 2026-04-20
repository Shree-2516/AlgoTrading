from fastapi import APIRouter, Depends, HTTPException
from google.auth.transport import requests
from google.oauth2 import id_token
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.core.config import GOOGLE_CLIENT_ID
from app.core.security import (
    create_access_token,
    get_password_hash,
    verify_password,
)
from app.db.database import SessionLocal
from app.db.models import User
from app.schemas.user import UserCreate, UserLogin

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        db_user = User(
            name=user.name,
            email=user.email,
            password=get_password_hash(user.password),
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except HTTPException:
        raise
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=503, detail="Database connection failed")

    return {"message": "User created"}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    try:
        db_user = db.query(User).filter(User.email == user.email).first()
    except SQLAlchemyError:
        raise HTTPException(status_code=503, detail="Database connection failed")

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not db_user.password or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"sub": db_user.email})

    return {
        "access_token": token,
        "token_type": "bearer",
    }


@router.post("/google")
def google_login(data: dict, db: Session = Depends(get_db)):
    token = data.get("token")

    if not token:
        raise HTTPException(status_code=400, detail="Token missing")

    try:
        idinfo = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            GOOGLE_CLIENT_ID,
        )
        email = idinfo["email"]
        name = idinfo.get("name", "Google User")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid Google token")

    try:
        user = db.query(User).filter(User.email == email).first()

        if not user:
            user = User(
                name=name,
                email=email,
                password="",
                is_google_user=True,
            )
            db.add(user)
            db.commit()
            db.refresh(user)
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=503, detail="Database connection failed")

    access_token = create_access_token({"sub": user.email})

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
