from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from app.core.config import ENV_PATH, masked_database_url
from app.core.logger import get_logger
from app.core.response import error, success
from app.modules.auth.router import router as auth_router
from app.modules.broker.router import router as broker_router
from app.modules.trading.router import router as trading_router
from app.modules.user.router import router as user_router


app = FastAPI()
logger = get_logger(__name__)

logger.info("Loaded backend env: %s", ENV_PATH)
logger.info("Database URL: %s", masked_database_url())

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
    logger.exception("Database error: %s", exc)
    return JSONResponse(
        status_code=503,
        content=error("Database connection failed"),
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=error(str(exc.detail)),
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled error: %s", exc)
    return JSONResponse(
        status_code=500,
        content=error(str(exc)),
    )


API_V1_PREFIX = "/api/v1"

app.include_router(auth_router, prefix=f"{API_V1_PREFIX}/auth", tags=["Auth"])
app.include_router(user_router, prefix=f"{API_V1_PREFIX}/user", tags=["User"])
app.include_router(broker_router, prefix=f"{API_V1_PREFIX}/broker", tags=["Broker"])
app.include_router(trading_router, prefix=f"{API_V1_PREFIX}/virtual", tags=["Virtual Trading"])


@app.get("/")
def home():
    return success(message="API Running")


from app.db.database import Base, engine
from app.modules.backtest import model as backtest_model
from app.modules.broker import model as broker_model
from app.modules.strategy import model as strategy_model
from app.modules.trading import model as trading_model
from app.modules.user import model as user_model

Base.metadata.create_all(bind=engine)
