from datetime import datetime, timedelta
from os import getenv

from fastapi.responses import JSONResponse
from jwt import encode, decode
from jwt import exceptions


def expire_date(days: int) -> datetime:
    return datetime.now() + timedelta(days=days)


def write_token(data: dict) -> str:
    return encode(payload={**data, "exp": expire_date(2)}, algorithm="HS256", key=getenv("JWT_SECRET"))


def validate_token(token: str, output=False) -> JSONResponse:
    try:
        if output:
            return decode(token, key=getenv("JWT_SECRET"), algorithms=["HS256"])
        decode(token, key=getenv("JWT_SECRET"), algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"message": "Invalid token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token expired"}, status_code=401)
