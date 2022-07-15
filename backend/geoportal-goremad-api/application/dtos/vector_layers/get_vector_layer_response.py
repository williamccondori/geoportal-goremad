from uuid import UUID

from pydantic import BaseModel


class GetVectorLayerResponse(BaseModel):
    key: UUID
