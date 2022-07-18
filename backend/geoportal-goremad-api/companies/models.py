from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from shared.database import Base


class Company(Base):
    __tablename__ = 'empresa'
    __table_args__ = {"schema": "geogoremad_seguridad"}

    # Columnas
    id = Column('id_empresa', Integer, primary_key=True)
    code = Column('codigo_empresa', String(15))
    name = Column('nombre_empresa', String(100))
    description = Column('descripcion_empresa', String(255))
    logo = Column('logo_empresa', String(255))
    url = Column('url_empresa', String(255))
    status = Column('estado', Boolean, default=True)
    created = Column('creado', DateTime)
    modified = Column('modificado', DateTime)

    # Relaciones
    settings = relationship("CompanyConfiguration", backref="user")


class CompanyConfiguration(Base):
    __tablename__ = 'configuracion_empresa'
    __table_args__ = {"schema": "geogoremad_seguridad"}

    # Columnas
    company_id = Column('id_empresa', ForeignKey('geogoremad_seguridad.empresa.id_empresa'), primary_key=True)
    key = Column('clave_configuracion', String(15), primary_key=True)
    value = Column('valor_configuracion', String(255))
    status = Column('estado', Boolean, default=True)
    created = Column('creado', DateTime)
    modified = Column('modificado', DateTime)

    # Relaciones
