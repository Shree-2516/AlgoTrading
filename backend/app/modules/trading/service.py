from sqlalchemy.orm import Session

from app.core.engine.execution_engine import execute_for_broker
from app.modules.broker.model import BrokerAccount


def execute_trade(db: Session, user_id: int, data):
    active_broker = db.query(BrokerAccount).filter_by(
        user_id=user_id,
        is_selected=True,
    ).first()

    if not active_broker:
        return {"error": "No active broker selected"}

    return execute_for_broker(db, user_id, data, active_broker)
