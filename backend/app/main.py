from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import SQLAlchemyError
from app.core.config import ENV_PATH, masked_database_url
from app.api import auth, user   # ✅ import both

app = FastAPI()

print(f"Loaded backend env: {ENV_PATH}")
print(f"Database URL: {masked_database_url()}")

# ✅ ADD THIS BLOCK
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


# ✅ include both routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user.router, prefix="/user", tags=["User"])

@app.get("/")
def home():
    return {"message": "API Running"}
