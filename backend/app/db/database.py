from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# get DB URL from env
DATABASE_URL = os.getenv("DATABASE_URL")

# engine
engine = create_engine(DATABASE_URL)

# session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base
Base = declarative_base()


# =========================
# ✅ THIS WAS MISSING
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()