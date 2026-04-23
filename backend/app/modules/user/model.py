from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import relationship

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=True)

    is_google_user = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    brokers = relationship("BrokerAccount", back_populates="user")
    strategies = relationship("Strategy", back_populates="user")
    virtual_wallets = relationship("VirtualWallet", back_populates="user")
    virtual_orders = relationship("VirtualOrder", back_populates="user")
    virtual_positions = relationship("VirtualPosition", back_populates="user")
    trades = relationship("TradeHistory", back_populates="user")
