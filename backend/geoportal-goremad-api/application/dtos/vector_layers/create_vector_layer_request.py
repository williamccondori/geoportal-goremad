from pydantic import BaseModel


class CreateVectorLayerRequest(BaseModel):
    name: str
    title: str
