from sqlalchemy.orm import Session

from app.modules.broker.model import BrokerAccount
from app.modules.trading.model import (
    TradeHistory,
    VirtualOrder,
    VirtualPosition,
    VirtualWallet,
)


def execute_trade(db: Session, user_id: int, data):
    active_broker = db.query(BrokerAccount).filter_by(
        user_id=user_id,
        is_selected=True,
    ).first()

    if not active_broker:
        return {"error": "No active broker selected"}

    if active_broker.broker_name == "algo":
        return place_virtual_order(db, user_id, data)

    if active_broker.broker_name == "angel":
        return {"message": "Angel execution not implemented yet"}

    if active_broker.broker_name == "dhan":
        return {"message": "Dhan execution not implemented yet"}

    return {"error": "Unsupported broker"}


def place_virtual_order(db: Session, user_id: int, data):
    wallet = db.query(VirtualWallet).filter_by(user_id=user_id).first()

    if not wallet:
        return {"error": "Wallet not found"}

    side = data.side.upper()
    cost = data.quantity * data.price

    try:
        if side == "BUY":
            if wallet.balance < cost:
                return {"error": "Insufficient balance"}

            wallet.balance -= cost

            position = db.query(VirtualPosition).filter_by(
                user_id=user_id,
                symbol=data.symbol,
            ).first()

            if position:
                total_qty = position.quantity + data.quantity
                position.avg_price = (
                    (position.avg_price * position.quantity)
                    + (data.price * data.quantity)
                ) / total_qty
                position.quantity = total_qty
            else:
                position = VirtualPosition(
                    user_id=user_id,
                    symbol=data.symbol,
                    quantity=data.quantity,
                    avg_price=data.price,
                )
                db.add(position)

        elif side == "SELL":
            position = db.query(VirtualPosition).filter_by(
                user_id=user_id,
                symbol=data.symbol,
            ).first()

            if not position or position.quantity < data.quantity:
                return {"error": "Not enough quantity to sell"}

            pnl = (data.price - position.avg_price) * data.quantity
            wallet.balance += data.quantity * data.price
            position.quantity -= data.quantity

            trade = TradeHistory(
                user_id=user_id,
                symbol=data.symbol,
                entry_price=position.avg_price,
                exit_price=data.price,
                quantity=data.quantity,
                pnl=pnl,
            )
            db.add(trade)

            if position.quantity == 0:
                db.delete(position)

        else:
            return {"error": "Invalid order side"}

        order = VirtualOrder(
            user_id=user_id,
            symbol=data.symbol,
            side=side,
            quantity=data.quantity,
            price=data.price,
        )
        db.add(order)

        db.commit()
        db.refresh(order)
    except Exception as exc:
        db.rollback()
        print("Order error:", str(exc))
        return {"error": "Order failed"}

    return {
        "message": "Order executed",
        "order_id": order.id,
        "balance": wallet.balance,
    }


def calculate_pnl(entry_price: float, exit_price: float, quantity: int):
    if exit_price is None:
        return 0.0
    return (exit_price - entry_price) * quantity
