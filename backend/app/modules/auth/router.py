from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.response import success
from app.db.database import get_db
from app.modules.auth.service import login_user, login_with_google, register_user
from app.modules.user.schema import UserCreate, UserLogin


router = APIRouter()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    register_user(user, db)
    return success(message="User created")


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return success(login_user(user, db), "Login successful")


@router.post("/google")
def google_login(data: dict, db: Session = Depends(get_db)):
    return success(login_with_google(data, db), "Google login successful")
