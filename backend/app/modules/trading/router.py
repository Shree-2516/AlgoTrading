from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.response import success
from app.db.database import get_db
from app.modules.trading.schema import OrderCreate, WalletCreate
from app.modules.trading.service import (
    create_virtual_wallet,
    execute_trade,
    get_virtual_wallet,
    list_positions,
    list_trade_history,
)


router = APIRouter()


@router.post("/wallet", status_code=status.HTTP_201_CREATED)
def create_wallet(data: WalletCreate, db: Session = Depends(get_db)):
    result = create_virtual_wallet(data, db)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return success(result, "Wallet + AlgoTrading broker ready")


@router.post("/order")
def place_virtual_order(data: OrderCreate, db: Session = Depends(get_db)):
    user_id = 1
    result = execute_trade(db, user_id, data)

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return success(result, result.get("message", "Order executed"))


@router.get("/wallet")
def get_wallet(db: Session = Depends(get_db)):
    result = get_virtual_wallet(db)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return success(result, "Wallet fetched")


@router.get("/positions")
def get_positions(db: Session = Depends(get_db)):
    return success(list_positions(db), "Positions fetched")


@router.get("/history")
def get_history(db: Session = Depends(get_db)):
    return success(list_trade_history(db), "Trade history fetched")
