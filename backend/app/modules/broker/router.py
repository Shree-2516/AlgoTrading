from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import decrypt_data, encrypt_data
from app.db.database import get_db
from app.modules.broker.model import BrokerAccount
from app.modules.broker.schema import BrokerCreate
from app.modules.broker.service import verify_angel, verify_dhan


router = APIRouter()


@router.post("/add", status_code=status.HTTP_201_CREATED)
def add_broker(data: BrokerCreate, db: Session = Depends(get_db)):
    user_id = 1

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
        "message": "Broker added",
        "broker_id": broker.id,
    }


@router.post("/verify/{broker_id}")
def verify_broker(broker_id: int, db: Session = Depends(get_db)):
    broker = db.query(BrokerAccount).filter(BrokerAccount.id == broker_id).first()

    if not broker:
        raise HTTPException(status_code=404, detail="Broker not found")

    try:
        api_key = decrypt_data(broker.api_key)
        api_secret = decrypt_data(broker.api_secret)

        if broker.broker_name.lower() == "angel":
            status_check = verify_angel(api_key, api_secret, broker.broker_user_id)
        elif broker.broker_name.lower() == "dhan":
            status_check = verify_dhan(api_key)
        else:
            status_check = False

        broker.is_connected = status_check
    except Exception:
        broker.is_connected = False

    db.commit()

    return {"connected": broker.is_connected}


@router.post("/toggle/{broker_id}")
def toggle_broker(broker_id: int, db: Session = Depends(get_db)):
    broker = db.query(BrokerAccount).filter(BrokerAccount.id == broker_id).first()

    if not broker:
        raise HTTPException(status_code=404, detail="Broker not found")

    broker.is_active = not broker.is_active
    db.commit()

    return {"is_active": broker.is_active}


@router.post("/select/{broker_id}")
def select_broker(broker_id: int, db: Session = Depends(get_db)):
    user_id = 1
    brokers = db.query(BrokerAccount).filter_by(user_id=user_id).all()

    if not brokers:
        raise HTTPException(status_code=404, detail="No brokers found")

    for broker in brokers:
        broker.is_selected = False

    broker = db.query(BrokerAccount).filter_by(id=broker_id).first()

    if not broker:
        raise HTTPException(status_code=404, detail="Broker not found")

    broker.is_selected = True
    db.commit()

    return {"message": "Active broker updated"}


@router.get("/active")
def get_active_broker(db: Session = Depends(get_db)):
    user_id = 1
    broker = db.query(BrokerAccount).filter_by(
        user_id=user_id,
        is_selected=True,
    ).first()

    if not broker:
        return {"message": "No active broker"}

    return {
        "id": broker.id,
        "broker_name": broker.broker_name,
    }


@router.get("/list")
def get_brokers(db: Session = Depends(get_db)):
    user_id = 1
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
