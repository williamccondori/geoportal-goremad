from uuid import UUID

from pydantic import BaseModel


class GetAllVectorLayersResponse(BaseModel):
    key: UUID
