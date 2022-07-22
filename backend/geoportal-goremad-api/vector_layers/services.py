import os
from tempfile import NamedTemporaryFile
from typing import List

from sqlalchemy.orm import Session

from shared.exceptions.entity_not_found_exception import EntityNotFoundException
from vector_layers.models import VectorLayer
from vector_layers.schemas import GetVectorLayersResponse, GetVectorLayerResponse, CreateVectorLayerRequest, \
    CreateVectorLayerResponse


def get_vector_layers(db: Session) -> List[GetVectorLayersResponse]:
    vector_layers = db.query(VectorLayer).where(VectorLayer.status).all()
    return [
        GetVectorLayersResponse(
            id=vector_layer.id,
            name=vector_layer.name,
            description=vector_layer.description,
            url=vector_layer.url,
        )
        for vector_layer in vector_layers
    ]


def get_vector_layer(db: Session, vector_layer_id: int) -> GetVectorLayerResponse:
    vector_layer: VectorLayer = db.query(VectorLayer).get(vector_layer_id)
    if not vector_layer or not vector_layer.status:
        raise EntityNotFoundException(type(VectorLayer))
    return GetVectorLayerResponse(
        id=vector_layer.id,

    )


def create_vector_layer(db: Session,
                        vector_layer_request: CreateVectorLayerRequest) -> CreateVectorLayerResponse:
    vector_file = NamedTemporaryFile(delete=False)
    try:
        vector_file.write(vector_layer_request.file)
        print(vector_file.name)
    finally:
        vector_file.close()
        os.unlink(vector_file.name)

    new_vector_layer: VectorLayer = VectorLayer(
        name=vector_layer_request.name,
        title=vector_layer_request.title,
        description=vector_layer_request.description,
        is_public=vector_layer_request.is_public,
    )
    db.add(new_vector_layer)
    db.commit()
    db.refresh(new_vector_layer)

    return CreateVectorLayerResponse(
        name=new_vector_layer.name,
        description=new_vector_layer.description,
        url=new_vector_layer.url,
    )


def delete_vector_layer(db: Session, vector_layer_id: int) -> int:
    vector_layer: VectorLayer = db.query(VectorLayer).get(vector_layer_id)
    if not vector_layer or not vector_layer.status:
        raise EntityNotFoundException(type(VectorLayer))
    vector_layer.status = False
    db.commit()
    return vector_layer_id
