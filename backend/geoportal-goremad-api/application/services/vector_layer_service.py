from typing import List
from uuid import uuid4, UUID

from application.dtos.vector_layers.create_vector_layer_request import CreateVectorLayerRequest
from application.dtos.vector_layers.create_vector_layer_response import CreateVectorLayerResponse
from application.dtos.vector_layers.get_all_vector_layers_response import GetAllVectorLayersResponse
from application.dtos.vector_layers.get_vector_layer_response import GetVectorLayerResponse
from application.dtos.vector_layers.update_vector_layer_request import UpdateVectorLayerRequest
from application.dtos.vector_layers.update_vector_layer_response import UpdateVectorLayerResponse
import models


class VectorLayerService:

    async def get_all_vector_layers(self) -> List[GetAllVectorLayersResponse]:
        return db.query(models.VectorLayer).all()
        return [
            GetAllVectorLayersResponse(key=uuid4()),
        ]
    
    async def get_vector_layer(self, vector_layer_key: UUID) -> GetVectorLayerResponse:
        return GetVectorLayerResponse(key=vector_layer_key)

    async def create_vector_layer(self,
                                  create_vector_layer_request: CreateVectorLayerRequest) -> CreateVectorLayerResponse:
        return CreateVectorLayerResponse(key=uuid4(), name=create_vector_layer_request.name,
                                         title=create_vector_layer_request.title)

    async def update_vector_layer(self, vector_layer_key: UUID,
                                  update_vector_layer_request: UpdateVectorLayerRequest) -> UpdateVectorLayerResponse:
        print(vector_layer_key)
        print(update_vector_layer_request)
        return UpdateVectorLayerResponse(key=vector_layer_key)

    async def delete_vector_layer(self, vector_layer_key: UUID) -> UUID:
        return vector_layer_key
