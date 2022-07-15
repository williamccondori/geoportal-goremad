from typing import List
from uuid import UUID

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from application.dtos.vector_layers.create_vector_layer_request import CreateVectorLayerRequest
from application.dtos.vector_layers.create_vector_layer_response import CreateVectorLayerResponse
from application.dtos.vector_layers.get_all_vector_layers_response import GetAllVectorLayersResponse
from application.dtos.vector_layers.get_vector_layer_response import GetVectorLayerResponse
from application.dtos.vector_layers.update_vector_layer_request import UpdateVectorLayerRequest
from application.dtos.vector_layers.update_vector_layer_response import UpdateVectorLayerResponse
from application.services.vector_layer_service import VectorLayerService
from routes.base_router import excecute

vector_layer_router = APIRouter()

vector_layer_service = VectorLayerService()


@vector_layer_router.get("/", response_model=List[GetAllVectorLayersResponse])
async def get_all_vector_layers() -> JSONResponse:
    """
    Obtiene todos las capas vectoriales.
    :return: Lista de todas las capas vectoriales.
    """
    return await excecute(vector_layer_service.get_all_vector_layers)


@vector_layer_router.get("/{vector_layer_key}", response_model=List[GetVectorLayerResponse])
async def get_vector_layer(vector_layer_key: UUID) -> JSONResponse:
    """
    Obtiene una capa veectorial por su identificador.
    :param vector_layer_key: Identificador de la capa vectorial.
    :return: Informacion de la capa vectorial.
    """
    return await excecute(vector_layer_service.get_vector_layer, vector_layer_key)


@vector_layer_router.post("/", response_model=CreateVectorLayerResponse)
async def create_vector_layer(create_vector_layer_request: CreateVectorLayerRequest) -> JSONResponse:
    """
    Crea una nueva capa vectorial.
    :param create_vector_layer_request: Datos requeridos para crear la capa vectorial.
    :return: create_vector_layer_response: Datos de la capa vectorial creada.
    """
    return await excecute(vector_layer_service.create_vector_layer, create_vector_layer_request, created=True)


@vector_layer_router.put("/{vector_layer_key}", response_model=UpdateVectorLayerResponse)
async def update_vector_layer(vector_layer_key: UUID,
                              update_vector_layer_request: UpdateVectorLayerRequest) -> JSONResponse:
    """
    Modifica una capa vectorial.
    :param vector_layer_key: Identificador de la capa vectorial.
    :param update_vector_layer_request: Datos requeridos para modificar la capa vectorial.
    :update_vector_layer_response: Datos de la capa vectorial modificada.
    """
    return await excecute(vector_layer_service.update_vector_layer, vector_layer_key, update_vector_layer_request)


@vector_layer_router.delete("/{vector_layer_key}", response_model=UUID)
async def delete_vector_layer(vector_layer_key: UUID) -> JSONResponse:
    """
    Elimina una capa vectorial.
    :param vector_layer_key: Identificador de la capa vectorial.
    :return: id_vector_layer: Identificador de la capa vectorial eliminada.
    """
    return await excecute(vector_layer_service.delete_vector_layer, vector_layer_key)
