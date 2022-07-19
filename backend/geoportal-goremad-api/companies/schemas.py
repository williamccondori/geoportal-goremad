from typing import Optional

from pydantic import BaseModel


class GetCompaniesResponse(BaseModel):
    id: int
    code: str
    name: str
    description: str
    logo: Optional[str]
    url: Optional[str]


class GetCompanyResponse(BaseModel):
    id: int
    code: str
    name: str
    description: str
    logo: Optional[str]
    url: Optional[str]


class CreateCompanyRequest(BaseModel):
    code: str
    name: str
    password: str
    description: str
    logo: Optional[str]
    url: Optional[str]


class CreateCompanyResponse(GetCompanyResponse):
    pass
