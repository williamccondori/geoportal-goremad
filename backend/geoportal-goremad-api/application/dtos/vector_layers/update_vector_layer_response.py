from uuid import UUID

from pydantic import BaseModel


class UpdateVectorLayerResponse(BaseModel):
    key: UUID
