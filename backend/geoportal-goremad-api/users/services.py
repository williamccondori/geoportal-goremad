import os
from datetime import datetime, timedelta

from jwt import encode, decode
from jwt import exceptions


def expire_date(days: int) -> datetime:
    return datetime.now() + timedelta(days=days)


def write_token(data: dict) -> str:
    jwt_secret = os.getenv("JWT_SECRET")
    expired_days = os.getenv("JWT_EXPIRED", 2)
    return encode(payload={**data, "exp": expire_date(expired_days)}, algorithm="HS256", key=jwt_secret)


def validate_token(token: str, output=False) -> str:
    jwt_secret = os.getenv("JWT_SECRET")
    try:
        if output:
            return decode(token, key=jwt_secret, algorithms=["HS256"])
        decode(token, key=jwt_secret, algorithms=["HS256"])
        return "Token válido"
    except exceptions.DecodeError:
        raise Exception("El token es inválido")
    except exceptions.ExpiredSignatureError:
        raise Exception("El token ha expirado")
