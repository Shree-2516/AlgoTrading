from sqlalchemy import Column, Float, ForeignKey, Integer, String, TIMESTAMP, text

from app.db.base import Base


class VirtualWallet(Base):
    __tablename__ = "virtual_wallets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    balance = Column(Float, default=0.0)
    initial_balance = Column(Float, default=0.0)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


class VirtualOrder(Base):
    __tablename__ = "virtual_orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    symbol = Column(String, nullable=False)
    side = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String, default="EXECUTED")
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


class VirtualPosition(Base):
    __tablename__ = "virtual_positions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    symbol = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    avg_price = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


class TradeHistory(Base):
    __tablename__ = "trade_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    symbol = Column(String, nullable=False)
    entry_price = Column(Float, nullable=False)
    exit_price = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=False)
    pnl = Column(Float, default=0.0)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
