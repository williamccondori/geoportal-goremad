from typing import Optional

from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str


class GetCurrentUserResponse(BaseModel):
    username: str
    name: Optional[str]
    last_name: Optional[str]
