from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status, Request
import fastapi.security as _security
from typing import Optional
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from datetime import timedelta, datetime
from app.utils.userHelper import get_user_by_username
from app.schemas.userSchema import TokenDataSchema
from app.models.userModel import User
from app.db.session import get_db
from app.config.settings import settings



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM

oauth2_scheme = _security.OAuth2PasswordBearer(tokenUrl="/auth/login")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


async def authenticate_user(db:Session, username: str, password: str):
    user = await get_user_by_username(db, username)

    if not user or not verify_password(password, user.hash_password):
        return False
    return user


async def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt
    
    
def get_current_user(token: str = Depends(oauth2_scheme)):
    print("extracted token",token)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        print("decoding token")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("payload")
        username: str = payload.get("sub")
        role: str = payload.get("role")
        print(username, role)

        if username is None or role is None:
            raise credentials_exception
        return {"username": username, "role": role}
    except JWTError:
        raise credentials_exception