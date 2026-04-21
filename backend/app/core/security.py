from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

# 🔐 NEW: Encryption imports
from cryptography.fernet import Fernet
import os

# JWT config
from app.core.config import SECRET_KEY, ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


# =========================================================
# 🔐 ENCRYPTION LAYER (NEW - SAFE ADDITION)
# =========================================================

# ⚠️ MUST be stored in .env (important)
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")

if not ENCRYPTION_KEY:
    # fallback (only for dev, not production)
    ENCRYPTION_KEY = Fernet.generate_key()
    print("⚠️ WARNING: ENCRYPTION_KEY not found in .env, using temporary key")

# Ensure bytes
if isinstance(ENCRYPTION_KEY, str):
    ENCRYPTION_KEY = ENCRYPTION_KEY.encode()

fernet = Fernet(ENCRYPTION_KEY)


def encrypt_data(data: str) -> str:
    if not data:
        return data
    return fernet.encrypt(data.encode()).decode()


def decrypt_data(data: str) -> str:
    if not data:
        return data
    return fernet.decrypt(data.encode()).decode()


# =========================================================
# 🔑 PASSWORD FUNCTIONS (EXISTING - UNCHANGED)
# =========================================================

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)


def get_password_hash(password):
    return pwd_context.hash(password)


# =========================================================
# 🔐 JWT TOKEN (EXISTING - UNCHANGED)
# =========================================================

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)