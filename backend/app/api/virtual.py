from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import (
    VirtualWallet,
    BrokerAccount,
    VirtualPosition,
    TradeHistory
)
from app.schemas.virtual import WalletCreate, OrderCreate
from app.services.virtual_broker import execute_trade

router = APIRouter(prefix="/virtual", tags=["Virtual Trading"])


# =========================
# 🟢 1. CREATE WALLET + ALGO BROKER
# =========================
@router.post("/wallet", status_code=status.HTTP_201_CREATED)
def create_wallet(data: WalletCreate, db: Session = Depends(get_db)):
    user_id = 1

    print("Received wallet balance:", data.balance)

    existing_wallet = db.query(VirtualWallet).filter_by(user_id=user_id).first()
    if existing_wallet:
        raise HTTPException(status_code=400, detail="Wallet already exists")

    existing_broker = db.query(BrokerAccount).filter_by(
        user_id=user_id,
        broker_name="algo"
    ).first()

    try:
        wallet = VirtualWallet(
            user_id=user_id,
            balance=data.balance,
            initial_balance=data.balance
        )
        db.add(wallet)

        if not existing_broker:
            broker = BrokerAccount(
                user_id=user_id,
                broker_name="algo",
                broker_user_id="virtual",
                api_key="",
                api_secret="",
                is_connected=True,
                is_active=True
            )
            db.add(broker)

        db.commit()
        db.refresh(wallet)

    except Exception as e:
        db.rollback()
        print("Wallet creation error:", str(e))
        raise HTTPException(status_code=500, detail="Failed to create wallet")

    return {
        "message": "Wallet + AlgoTrading broker ready",
        "wallet_id": wallet.id,
        "balance": wallet.balance
    }


# =========================
# 🟢 2. PLACE ORDER
# =========================
@router.post("/order")
def place_virtual_order(data: OrderCreate, db: Session = Depends(get_db)):
    user_id = 1

    result = execute_trade(db, user_id, data)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return result


# =========================
# 🟢 3. GET WALLET
# =========================
@router.get("/wallet")
def get_wallet(db: Session = Depends(get_db)):
    user_id = 1

    wallet = db.query(VirtualWallet).filter_by(user_id=user_id).first()

    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")

    return {
        "id": wallet.id,
        "balance": wallet.balance,
        "initial_balance": wallet.initial_balance
    }


# =========================
# 🟢 4. GET POSITIONS
# =========================
@router.get("/positions")
def get_positions(db: Session = Depends(get_db)):
    user_id = 1

    positions = db.query(VirtualPosition).filter_by(user_id=user_id).all()

    return [
        {
            "symbol": p.symbol,
            "quantity": p.quantity,
            "avg_price": p.avg_price
        }
        for p in positions
    ]


# =========================
# 🟢 5. TRADE HISTORY
# =========================
@router.get("/history")
def get_history(db: Session = Depends(get_db)):
    user_id = 1

    trades = db.query(TradeHistory).filter_by(user_id=user_id).all()

    return [
        {
            "symbol": t.symbol,
            "entry_price": t.entry_price,
            "exit_price": t.exit_price,
            "quantity": t.quantity,
            "pnl": t.pnl
        }
        for t in trades
    ]