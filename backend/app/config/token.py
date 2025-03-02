from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from pydantic import EmailStr
from uuid import UUID
from datetime import timedelta, datetime, timezone
from jose import jwt, JWTError
from jose.exceptions import ExpiredSignatureError
from typing import Annotated
from ..schemas import UserPrivate, UserNotFound
from .config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_DAYS
from .database import get_db
# from ..services import user_service

oauth2_scheme = HTTPBearer()

token_dependency = Annotated[HTTPAuthorizationCredentials, Depends(oauth2_scheme)]

def create_access_token(data: dict, expire_date: timedelta | None = None):
    data["id"] = str(data["id"]) # convert UUID to string first 
    to_encode = data.copy()
    if expire_date is None:
        expire_date = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.now(timezone.utc) + expire_date
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def create_refresh_token(data: dict, expire_date: timedelta | None = None):
    data["id"] = str(data["id"]) # convert UUID to string first 
    to_encode = data.copy()
    if expire_date is None:
        expire_date = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    expire = datetime.now(timezone.utc) + expire_date
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

async def get_current_user(credentials: token_dependency, db: Session = Depends(get_db)) -> UserPrivate:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )    
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: EmailStr = payload.get("email")
        user_id: UUID = UUID(payload.get("id"))
        username: str = payload.get("username")
        if not email or not user_id or not username :
            raise credentials_exception
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except JWTError:
        raise credentials_exception
    try:
        user = user_service.get_user_by_id(user_id=user_id, db=db)
    except UserNotFound:
        raise credentials_exception
    return user

def refresh_tokens(refresh_token: str, db: Session):
    refresh_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate refresh token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        email: EmailStr = payload.get("email")
        user_id: UUID = UUID(payload.get("id"))
        username: str = payload.get("username")
        if not email or not user_id or not username:
            raise refresh_exception
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except JWTError:
        raise refresh_exception
    try:
        user = user_service.get_user_by_id(user_id=user_id, db=db)
    except UserNotFound:
        raise refresh_exception
    
    user_data = user.model_dump()
    new_access_token = create_access_token(data=user_data)
    new_refresh_token = create_refresh_token(data=user_data)
    return {"access_token": new_access_token, "refresh_token": new_refresh_token, "token_type": "bearer"}
