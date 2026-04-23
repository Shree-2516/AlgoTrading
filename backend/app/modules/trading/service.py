from sqlalchemy.orm import Session

from app.core.engine.execution.execution_engine import execute_for_broker
from app.core.logger import get_logger
from app.modules.broker.model import BrokerAccount
from app.modules.trading.model import TradeHistory, VirtualPosition, VirtualWallet


logger = get_logger(__name__)


def create_virtual_wallet(data, db: Session, user_id: int = 1):
    existing_wallet = db.query(VirtualWallet).filter_by(user_id=user_id).first()
    if existing_wallet:
        return {"error": "Wallet already exists"}

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
        logger.exception("Wallet creation failed: %s", exc)
        return {"error": "Failed to create wallet"}

    return {
        "wallet_id": wallet.id,
        "balance": wallet.balance,
    }


def execute_trade(db: Session, user_id: int, data):
    active_broker = db.query(BrokerAccount).filter_by(
        user_id=user_id,
        is_selected=True,
    ).first()

    if not active_broker:
        return {"error": "No active broker selected"}

    return execute_for_broker(db, user_id, data, active_broker)


def get_virtual_wallet(db: Session, user_id: int = 1):
    wallet = db.query(VirtualWallet).filter_by(user_id=user_id).first()

    if not wallet:
        return {"error": "Wallet not found"}

    return {
        "id": wallet.id,
        "balance": wallet.balance,
        "initial_balance": wallet.initial_balance,
    }


def list_positions(db: Session, user_id: int = 1):
    positions = db.query(VirtualPosition).filter_by(user_id=user_id).all()

    return [
        {
            "symbol": position.symbol,
            "quantity": position.quantity,
            "avg_price": position.avg_price,
        }
        for position in positions
    ]


def list_trade_history(db: Session, user_id: int = 1):
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
