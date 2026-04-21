from pydantic import BaseModel, Field


# =========================
# 🔹 REQUEST SCHEMA
# =========================
class BrokerCreate(BaseModel):
    broker_name: str = Field(..., example="angel")
    broker_user_id: str = Field(..., example="CLIENT123")
    api_key: str = Field(..., min_length=5)
    api_secret: str = Field(..., min_length=5)


# =========================
# 🔹 RESPONSE SCHEMA
# =========================
class BrokerResponse(BaseModel):
    id: int
    broker_name: str
    broker_user_id: str
    is_active: bool
    is_connected: bool

    class Config:
        orm_mode = True


# =========================
# 🔹 OPTIONAL (FUTURE USE)
# =========================
class BrokerVerifyResponse(BaseModel):
    connected: bool