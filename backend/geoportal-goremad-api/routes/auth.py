from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr

from functions_jwt import write_token, validate_token

auth_routes = APIRouter()


class User(BaseModel):
    username: str
    email: EmailStr


@auth_routes.post("/login")
async def login(user: User) -> JSONResponse:
    if user.username == "WCONDORI":
        return JSONResponse(content={"token": write_token({"username": user.username})}, status_code=200)
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)


@auth_routes.post("/verify/token")
async def verify_token(authorization: str = Header(None)) -> JSONResponse:
    token = authorization.split(" ")[1]
    return validate_token(token, output=True)
