import os
from tempfile import NamedTemporaryFile
from typing import List

import geopandas
from sqlalchemy.orm import Session

from shared.database import engine
from shared.exceptions.entity_not_found_exception import EntityNotFoundException
from vector_layers.models import VectorLayer
from vector_layers.schemas import GetVectorLayersResponse, GetVectorLayerResponse, CreateVectorLayerRequest, \
    CreateVectorLayerResponse

DEFAULT_CRS = 'EPSG:4326'
SCHEMA_VECTOR_LAYERS = 'geogoremad_capas'


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
    vector_layer_name = vector_layer_request.name.lower()
    if len(vector_layer_name) > 15:
        raise Exception()
    if not vector_layer_name.isalpha():
        raise Exception()

    vector_file = NamedTemporaryFile(delete=False, suffix='.zip')
    try:
        vector_file.write(vector_layer_request.file)
        gdf = geopandas.read_file(vector_file.name)
        gdf.crs = DEFAULT_CRS
        gdf.to_postgis(vector_layer_name, engine, if_exists='replace', schema=SCHEMA_VECTOR_LAYERS)
    finally:
        vector_file.close()
        os.unlink(vector_file.name)

    """
    new_vector_layer: VectorLayer = VectorLayer(
        name=vector_layer_request.name,
        title=vector_layer_request.title,
        description=vector_layer_request.description,
        is_public=vector_layer_request.is_public,
    )
    db.add(new_vector_layer)
    db.commit()
    db.refresh(new_vector_layer)
    """
    return CreateVectorLayerResponse(
    )


def delete_vector_layer(db: Session, vector_layer_id: int) -> int:
    vector_layer: VectorLayer = db.query(VectorLayer).get(vector_layer_id)
    if not vector_layer or not vector_layer.status:
        raise EntityNotFoundException(type(VectorLayer))
    vector_layer.status = False
    db.commit()
    return vector_layer_id
