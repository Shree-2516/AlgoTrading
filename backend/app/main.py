from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from app.core.config import ENV_PATH, masked_database_url
from app.modules.auth.router import router as auth_router
from app.modules.broker.router import router as broker_router
from app.modules.trading.router import router as trading_router
from app.modules.user.router import router as user_router


app = FastAPI()

print(f"Loaded backend env: {ENV_PATH}")
print(f"Database URL: {masked_database_url()}")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(SQLAlchemyError)
def sqlalchemy_exception_handler(request, exc):
    return JSONResponse(
        status_code=503,
        content={"detail": "Database connection failed"},
    )


app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(broker_router, prefix="/broker", tags=["Broker"])
app.include_router(trading_router, prefix="/virtual", tags=["Virtual Trading"])


@app.get("/")
def home():
    return {"message": "API Running"}


from app.db.database import Base, engine
from app.modules.broker import model as broker_model
from app.modules.trading import model as trading_model
from app.modules.user import model as user_model

Base.metadata.create_all(bind=engine)
