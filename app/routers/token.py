from fastapi import HTTPException
from ..config import settings
from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError
from ..database.schemas import TokenData

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.ALGORITHM)

    return encoded_jwt

def verify_token(token: str, credentials_exception: HTTPException):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        return TokenData(email=email)
    except JWTError:
        raise credentials_exception 
