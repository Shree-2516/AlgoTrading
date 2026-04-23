from sqlalchemy import Column, Float, ForeignKey, Integer, TIMESTAMP, text
from sqlalchemy.orm import relationship

from app.db.base import Base


class Backtest(Base):
    __tablename__ = "backtests"

    id = Column(Integer, primary_key=True, index=True)
    strategy_id = Column(Integer, ForeignKey("strategies.id"), nullable=False)
    total_trades = Column(Integer, default=0)
    net_pnl = Column(Float, default=0.0)
    win_rate = Column(Float, default=0.0)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    strategy = relationship("Strategy", back_populates="backtests")
