from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.response import success
from app.db.database import get_db
from app.modules.broker.schema import BrokerCreate
from app.modules.broker.service import (
    add_broker_account,
    get_active_broker_account,
    list_broker_accounts,
    select_broker_account,
    toggle_broker_account,
    verify_broker_account,
)


router = APIRouter()


@router.post("/add", status_code=status.HTTP_201_CREATED)
def add_broker(data: BrokerCreate, db: Session = Depends(get_db)):
    return success(add_broker_account(data, db), "Broker added")


@router.post("/verify/{broker_id}")
def verify_broker(broker_id: int, db: Session = Depends(get_db)):
    return success(verify_broker_account(broker_id, db), "Broker verified")


@router.post("/toggle/{broker_id}")
def toggle_broker(broker_id: int, db: Session = Depends(get_db)):
    return success(toggle_broker_account(broker_id, db), "Broker status updated")


@router.post("/select/{broker_id}")
def select_broker(broker_id: int, db: Session = Depends(get_db)):
    return success(select_broker_account(broker_id, db), "Active broker updated")


@router.get("/active")
def get_active_broker(db: Session = Depends(get_db)):
    return success(get_active_broker_account(db), "Active broker fetched")


@router.get("/list")
def get_brokers(db: Session = Depends(get_db)):
    return success(list_broker_accounts(db), "Brokers fetched")
