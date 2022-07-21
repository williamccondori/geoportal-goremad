import os
from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from auth.schemas import GetCurrentUserResponse, LoginRequest, LoginResponse
from shared.exceptions.unauthorized_exception import UnauthorizedException
from shared.exceptions.user_not_enabled_exception import UserNotEnabledException
from users.models import User
from users.services import get_user_by_username

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode: dict = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(db: Session, username: str) -> GetCurrentUserResponse:
    user = get_user_by_username(db, username)
    return GetCurrentUserResponse(
        username=user.username,
        name=user.name,
        last_name=user.last_name
    )


def login(db: Session, login_request: LoginRequest) -> LoginResponse:
    user: User = get_user_by_username(db, login_request.username)
    if not user:
        raise UnauthorizedException()
    if not user.is_enabled:
        raise UserNotEnabledException()
    if not verify_password(login_request.password, user.password):
        raise UnauthorizedException()
    access_token_expires: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return LoginResponse(
        access_token=create_access_token(
            data={"sub": user.username},
            expires_delta=access_token_expires
        ),
        token_type="bearer"
    )
