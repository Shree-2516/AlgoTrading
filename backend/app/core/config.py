import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy.engine import make_url

ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(ENV_PATH, override=True)

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

missing = [
    name
    for name, value in {
        "DATABASE_URL": DATABASE_URL,
        "SECRET_KEY": SECRET_KEY,
        "ALGORITHM": ALGORITHM,
        "GOOGLE_CLIENT_ID": GOOGLE_CLIENT_ID,
    }.items()
    if not value
]

if missing:
    raise RuntimeError(f"Missing required environment variables: {', '.join(missing)}")


def masked_database_url():
    url = make_url(DATABASE_URL)
    return str(url.set(password="***"))
