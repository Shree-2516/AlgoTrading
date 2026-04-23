from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.modules.auth.service import login_user, login_with_google, register_user
from app.modules.user.schema import UserCreate, UserLogin


router = APIRouter()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(user, db)


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(user, db)


@router.post("/google")
def google_login(data: dict, db: Session = Depends(get_db)):
    return login_with_google(data, db)
