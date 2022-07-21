import os

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from shared.dependencies.get_database_context import get_database_context
from shared.exceptions.unauthorized_exception import UnauthorizedException
from shared.exceptions.user_not_enabled_exception import UserNotEnabledException
from users.services import get_user_by_username

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login", scheme_name="JWT")


def get_current_user_information(token: str = Depends(oauth2_scheme),
                                 db: Session = Depends(get_database_context)) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise UnauthorizedException()
    except JWTError:
        raise UnauthorizedException()
    user = get_user_by_username(db, username)
    if not user:
        raise UnauthorizedException()
    if not user.is_enabled:
        raise UserNotEnabledException()
    return user.username
