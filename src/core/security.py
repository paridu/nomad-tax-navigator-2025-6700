import os
from cryptography.fernet import Fernet
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional

# Security Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "unsecure_default_change_me_in_prod")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
FIELD_ENCRYPTION_KEY = os.getenv("FIELD_ENCRYPTION_KEY") # AES-256 Key

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
cipher_suite = Fernet(FIELD_ENCRYPTION_KEY) if FIELD_ENCRYPTION_KEY else None

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def encrypt_sensitive_data(data: str) -> str:
    """Encrypts Tier 1 data (Tax IDs, Income) before DB storage."""
    if not cipher_suite:
        raise ValueError("Encryption key not configured")
    return cipher_suite.encrypt(data.encode()).decode()

def decrypt_sensitive_data(token: str) -> str:
    """Decrypts Tier 1 data for processing."""
    if not cipher_suite:
        raise ValueError("Encryption key not configured")
    return cipher_suite.decrypt(token.encode()).decode()

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)