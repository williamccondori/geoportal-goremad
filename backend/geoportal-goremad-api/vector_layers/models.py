from datetime import datetime

from sqlalchemy import Column, Integer, Boolean, DateTime, String

from shared.database import Base


class VectorLayer(Base):
    __tablename__ = 'capa_vectorial'
    __table_args__ = {"schema": "geogoremad_geoportal"}
    id = Column('id_capa_vectorial', Integer, primary_key=True, index=True)
    name = Column('vc_nombre', String(100))
    title = Column('vc_titulo', String(100))
    description = Column('vc_descripcion', String(255), nullable=True)
    is_public = Column('bo_publico', Boolean, default=False)
    is_enabled = Column('bo_habilitado', Boolean, default=True)
    status = Column('bo_estado', Boolean, default=True)
    created = Column('ts_creado', DateTime, default=datetime.now)
    modified = Column('ts_modificado', DateTime, default=datetime.now)
    created_by = Column('vc_usuario_creador', String(100))
    modified_by = Column('vc_usuario_modificador', String(100))
