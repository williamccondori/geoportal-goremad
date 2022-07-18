from pydantic import BaseModel


class GetCompaniesResponse(BaseModel):
    id: int
    name: str
    description: str
    logo: str


class GetCompanyResponse(BaseModel):
    id: int
    name: str
    description: str
    logo: str


class CreateCompanyRequest(BaseModel):
    name: str
    description: str
    logo: str


class CreateCompanyResponse(GetCompanyResponse):
    pass
