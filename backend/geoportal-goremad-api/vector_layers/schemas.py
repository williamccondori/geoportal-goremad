from pydantic import BaseModel


class GetVectorLayersResponse(BaseModel):
    id: int


class GetVectorLayerResponse(BaseModel):
    id: int


class CreateVectorLayerRequest(BaseModel):
    name: str
    title: str
    description: str
    is_public: bool
    file: bytes
    username: str


class CreateVectorLayerResponse(BaseModel):
    name: str
