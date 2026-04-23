from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.modules.broker.model import BrokerAccount
from app.modules.trading.model import TradeHistory, VirtualPosition, VirtualWallet
from app.modules.trading.schema import OrderCreate, WalletCreate
from app.modules.trading.service import execute_trade


router = APIRouter()


@router.post("/wallet", status_code=status.HTTP_201_CREATED)
def create_wallet(data: WalletCreate, db: Session = Depends(get_db)):
    user_id = 1

    existing_wallet = db.query(VirtualWallet).filter_by(user_id=user_id).first()
    if existing_wallet:
        raise HTTPException(status_code=400, detail="Wallet already exists")

    existing_broker = db.query(BrokerAccount).filter_by(
        user_id=user_id,
        broker_name="algo",
    ).first()

    try:
        wallet = VirtualWallet(
            user_id=user_id,
            balance=data.balance,
            initial_balance=data.balance,
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
                is_active=True,
            )
            db.add(broker)

        db.commit()
        db.refresh(wallet)
    except Exception as exc:
        db.rollback()
        print("Wallet creation error:", str(exc))
        raise HTTPException(status_code=500, detail="Failed to create wallet")

    return {
        "message": "Wallet + AlgoTrading broker ready",
        "wallet_id": wallet.id,
        "balance": wallet.balance,
    }


@router.post("/order")
def place_virtual_order(data: OrderCreate, db: Session = Depends(get_db)):
    user_id = 1
    result = execute_trade(db, user_id, data)

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return result


@router.get("/wallet")
def get_wallet(db: Session = Depends(get_db)):
    user_id = 1
    wallet = db.query(VirtualWallet).filter_by(user_id=user_id).first()

    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")

    return {
        "id": wallet.id,
        "balance": wallet.balance,
        "initial_balance": wallet.initial_balance,
    }


@router.get("/positions")
def get_positions(db: Session = Depends(get_db)):
    user_id = 1
    positions = db.query(VirtualPosition).filter_by(user_id=user_id).all()

    return [
        {
            "symbol": position.symbol,
            "quantity": position.quantity,
            "avg_price": position.avg_price,
        }
        for position in positions
    ]


@router.get("/history")
def get_history(db: Session = Depends(get_db)):
    user_id = 1
    trades = db.query(TradeHistory).filter_by(user_id=user_id).all()

    return [
        {
            "symbol": trade.symbol,
            "entry_price": trade.entry_price,
            "exit_price": trade.exit_price,
            "quantity": trade.quantity,
            "pnl": trade.pnl,
        }
        for trade in trades
    ]
