from fastapi import APIRouter, Depends

from app.modules.auth.dependencies import get_current_user
from app.modules.user.model import User


router = APIRouter()


@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
    }
