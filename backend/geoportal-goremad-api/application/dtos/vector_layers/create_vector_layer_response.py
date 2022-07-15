from uuid import UUID

from pydantic import BaseModel


class CreateVectorLayerResponse(BaseModel):
    key: UUID
    name: str
    title: str
