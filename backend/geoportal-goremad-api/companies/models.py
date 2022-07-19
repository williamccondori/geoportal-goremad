from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from shared.database import Base


class Company(Base):
    __tablename__ = 'empresa'
    __table_args__ = {"schema": "geogoremad_seguridad"}
    id = Column('id_empresa', Integer, primary_key=True, index=True)
    code = Column('vc_codigo_empresa', String(15))
    name = Column('vc_nombre_empresa', String(100))
    description = Column('vc_descripcion_empresa', String(255))
    logo = Column('vc_logo_empresa', String(255), nullable=True)
    url = Column('vc_url_empresa', String(255), nullable=True)
    is_enabled = Column('bo_habilitado', Boolean, default=True)
    status = Column('bo_estado', Boolean, default=True)
    created = Column('ts_creado', DateTime, default=datetime.now)
    modified = Column('ts_modificado', DateTime, default=datetime.now)
    settings = relationship('CompanyConfiguration')
    users = relationship('User')


class CompanyConfiguration(Base):
    __tablename__ = 'empresa_configuracion'
    __table_args__ = {"schema": "geogoremad_seguridad"}
    id = Column('id_empresa_configuracion', Integer, primary_key=True, index=True)
    company_id = Column('id_empresa', Integer, ForeignKey("geogoremad_seguridad.empresa.id_empresa"))
    key = Column('vc_clave_configuracion', String(15))
    value = Column('vc_valor_configuracion', String(255))
    status = Column('bo_estado', Boolean, default=True)
    created = Column('ts_creado', DateTime, default=datetime.now)
    modified = Column('ts_modificado', DateTime, default=datetime.now)
