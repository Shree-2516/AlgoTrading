from pydantic import BaseModel, Field, validator


# =========================
# 🟢 WALLET SCHEMA
# =========================
class WalletCreate(BaseModel):
    balance: float = Field(..., gt=0, example=10000)


# =========================
# 🟢 ORDER SCHEMA
# =========================
class OrderCreate(BaseModel):
    symbol: str = Field(..., min_length=2, example="BTCUSD")
    side: str = Field(..., example="BUY")  # BUY / SELL
    quantity: int = Field(..., gt=0, example=1)
    price: float = Field(..., gt=0, example=50000)

    # ✅ enforce BUY/SELL only
    @validator("side")
    def validate_side(cls, value):
        value = value.upper()
        if value not in ["BUY", "SELL"]:
            raise ValueError("side must be BUY or SELL")
        return value