from pydantic import BaseModel


class UpdateVectorLayerRequest(BaseModel):
    title: str
