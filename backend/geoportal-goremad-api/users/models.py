from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from shared.database import Base


class User(Base):
    __tablename__ = 'usuario'
    __table_args__ = {"schema": "geogoremad_seguridad"}
    id = Column('id_usuario', Integer, primary_key=True, index=True)
    company_id = Column('id_empresa', Integer, ForeignKey("geogoremad_seguridad.empresa.id_empresa"))
    name = Column('vc_nombre_usuario', String(100), nullable=True)
    last_name = Column('vc_apellido_usuario', String(100), nullable=True)
    username = Column('vc_codigo_usuario', String(15))
    password = Column('vc_contrasenia_usuario', String(255))
    email = Column('vc_email_usuario', String(100))
    is_enabled = Column('bo_habilitado', Boolean, default=True)
    status = Column('bo_estado', Boolean, default=True)
    created = Column('ts_creado', DateTime, default=datetime.now)
    modified = Column('ts_modificado', DateTime, default=datetime.now)
    settings = relationship('UserConfiguration')


class UserConfiguration(Base):
    __tablename__ = 'usuario_configuracion'
    __table_args__ = {"schema": "geogoremad_seguridad"}
    id = Column('id_usuario_configuracion', Integer, primary_key=True, index=True)
    user_id = Column('id_usuario', Integer, ForeignKey("geogoremad_seguridad.usuario.id_usuario"))
    key = Column('vc_clave_configuracion', String(15))
    value = Column('vc_valor_configuracion', String(255))
    status = Column('bo_estado', Boolean, default=True)
    created = Column('ts_creado', DateTime, default=datetime.now)
    modified = Column('ts_modificado', DateTime, default=datetime.now)
