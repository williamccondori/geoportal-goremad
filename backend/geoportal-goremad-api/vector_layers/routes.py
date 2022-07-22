from typing import List

from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST

from shared.dependencies.get_current_user_information import get_current_user_information
from shared.dependencies.get_database_context import get_database_context
from shared.dependencies.get_zip_file_upload import get_zip_file_upload
from shared.exceptions.shared.api_exception import ApiException
from vector_layers import services
from vector_layers.schemas import GetVectorLayersResponse, GetVectorLayerResponse, CreateVectorLayerResponse, \
    CreateVectorLayerRequest

vector_layer_router = APIRouter()


async def get_vector_layer_request(name: str = Form(...),
                                   title: str = Form(...),
                                   description: str = Form(...),
                                   is_public: bool = Form(...),
                                   file: bytes = Depends(get_zip_file_upload)):
    return CreateVectorLayerRequest(
        name=name,
        title=title,
        description=description,
        is_public=is_public,
        file=file,
        username='faa'
    )


@vector_layer_router.get("/", response_model=List[GetVectorLayersResponse])
async def get_companies(db: Session = Depends(get_database_context),
                        _: str = Depends(get_current_user_information)) -> List[GetVectorLayersResponse]:
    try:
        return services.get_vector_layers(db)
    except Exception as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))


@vector_layer_router.get("/{vector_layer_id}", response_model=GetVectorLayerResponse)
async def get_vector_layer(vector_layer_id: int, db: Session = Depends(get_database_context),
                           _: str = Depends(get_current_user_information)) -> GetVectorLayerResponse:
    try:
        return services.get_vector_layer(db, vector_layer_id)
    except Exception as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))


@vector_layer_router.post("/", response_model=CreateVectorLayerResponse, status_code=201)
async def create_vector_layer(
        vector_layer_request: CreateVectorLayerRequest = Depends(get_vector_layer_request),
        db: Session = Depends(get_database_context)) -> CreateVectorLayerResponse:
    try:
        return services.create_vector_layer(db, vector_layer_request)
    except ApiException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))


@vector_layer_router.delete("/{vector_layer_id}")
async def delete_vector_layer(vector_layer_id: int, db: Session = Depends(get_database_context),
                              _: str = Depends(get_current_user_information)) -> int:
    try:
        return services.delete_vector_layer(db, vector_layer_id)
    except Exception as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))
