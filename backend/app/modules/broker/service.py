from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.engine.execution.broker_engine import verify_angel, verify_dhan
from app.core.security import decrypt_data, encrypt_data
from app.modules.broker.model import BrokerAccount


def add_broker_account(data, db: Session, user_id: int = 1):
    existing = db.query(BrokerAccount).filter(
        BrokerAccount.user_id == user_id,
        BrokerAccount.broker_name == data.broker_name,
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Broker already added")

    broker = BrokerAccount(
        user_id=user_id,
        broker_name=data.broker_name,
        broker_user_id=data.broker_user_id,
        api_key=encrypt_data(data.api_key),
        api_secret=encrypt_data(data.api_secret),
        is_connected=False,
        is_active=True,
        is_selected=False,
    )

    db.add(broker)
    db.commit()
    db.refresh(broker)

    return {
        "broker_id": broker.id,
    }


def verify_broker_account(broker_id: int, db: Session):
    broker = _get_broker_or_404(db, broker_id)

    try:
        api_key = decrypt_data(broker.api_key)
        api_secret = decrypt_data(broker.api_secret)
        broker_name = broker.broker_name.lower()

        if broker_name == "angel":
            broker.is_connected = verify_angel(api_key, api_secret, broker.broker_user_id)
        elif broker_name == "dhan":
            broker.is_connected = verify_dhan(api_key)
        else:
            broker.is_connected = False
    except Exception:
        broker.is_connected = False

    db.commit()
    return {"connected": broker.is_connected}


def toggle_broker_account(broker_id: int, db: Session):
    broker = _get_broker_or_404(db, broker_id)
    broker.is_active = not broker.is_active
    db.commit()

    return {"is_active": broker.is_active}


def select_broker_account(broker_id: int, db: Session, user_id: int = 1):
    brokers = db.query(BrokerAccount).filter_by(user_id=user_id).all()

    if not brokers:
        raise HTTPException(status_code=404, detail="No brokers found")

    for broker in brokers:
        broker.is_selected = False

    broker = _get_broker_or_404(db, broker_id)
    broker.is_selected = True
    db.commit()

    return {"broker_id": broker.id}


def get_active_broker_account(db: Session, user_id: int = 1):
    broker = db.query(BrokerAccount).filter_by(
        user_id=user_id,
        is_selected=True,
    ).first()

    if not broker:
        return None

    return {
        "id": broker.id,
        "broker_name": broker.broker_name,
    }


def list_broker_accounts(db: Session, user_id: int = 1):
    brokers = db.query(BrokerAccount).filter(BrokerAccount.user_id == user_id).all()

    return [
        {
            "id": broker.id,
            "broker_name": broker.broker_name,
            "broker_user_id": broker.broker_user_id,
            "is_active": broker.is_active,
            "is_connected": broker.is_connected,
            "is_selected": broker.is_selected,
        }
        for broker in brokers
    ]


def _get_broker_or_404(db: Session, broker_id: int):
    broker = db.query(BrokerAccount).filter(BrokerAccount.id == broker_id).first()

    if not broker:
        raise HTTPException(status_code=404, detail="Broker not found")

    return broker
