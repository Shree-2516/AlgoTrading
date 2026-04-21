from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text, ForeignKey, Text, Float
from app.db.database import Base


# =========================
# USER TABLE
# =========================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=True)

    is_google_user = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))


# =========================
# BROKER ACCOUNTS TABLE
# =========================
class BrokerAccount(Base):
    __tablename__ = "broker_accounts"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    broker_name = Column(String, nullable=False)
    broker_user_id = Column(String, nullable=False)

    api_key = Column(Text, nullable=False)
    api_secret = Column(Text, nullable=False)

    is_active = Column(Boolean, default=True)
    is_connected = Column(Boolean, default=False)

    # ✅ NEW FIELD (NO BREAKING CHANGE)
    is_selected = Column(Boolean, default=False)


# =========================================================
# 🟢 VIRTUAL WALLET
# =========================================================
class VirtualWallet(Base):
    __tablename__ = "virtual_wallets"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    balance = Column(Float, default=0.0)
    initial_balance = Column(Float, default=0.0)

    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))


# =========================================================
# 🟢 VIRTUAL ORDERS
# =========================================================
class VirtualOrder(Base):
    __tablename__ = "virtual_orders"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    symbol = Column(String, nullable=False)
    side = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    status = Column(String, default="EXECUTED")

    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))


# =========================================================
# 🟡 OPEN POSITIONS
# =========================================================
class VirtualPosition(Base):
    __tablename__ = "virtual_positions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    symbol = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    avg_price = Column(Float, nullable=False)

    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))


# =========================================================
# 🟣 TRADE HISTORY
# =========================================================
class TradeHistory(Base):
    __tablename__ = "trade_history"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    symbol = Column(String, nullable=False)

    entry_price = Column(Float, nullable=False)
    exit_price = Column(Float, nullable=True)

    quantity = Column(Integer, nullable=False)

    pnl = Column(Float, default=0.0)

    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))