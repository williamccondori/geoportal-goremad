-- CREACION DE ESQUEMAS DE LA BASE DE DATOS
CREATE SCHEMA geogoremad_general;
CREATE SCHEMA geogoremad_seguridad;
CREATE SCHEMA geogoremad_geoportal;

/* ==========================================================================================
AUTOR: WILLIAM CONDORI QUISPE
FECHA: 18-07-2022
NOMBRE DEL OBJETO: geogoremad_seguridad.empresa
DESCRIPCION: Tabla que contiene los datos de las empresas
EJEMPLO DE USO:
========================================================================================== */
-- DEFINICION DE LA TABLA
CREATE TABLE geogoremad_seguridad.empresa (
  id_empresa serial NOT NULL,
  codigo_empresa character varying(15) NOT NULL,
  nombre_empresa character varying(100) NOT NULL,
  descripcion_empresa character varying(255) NOT NULL,
  logo_empresa character varying(255) NOT NULL,
  url_empresa character varying(255) NOT NULL,
  estado boolean NOT NULL,
  creado timestamp without time zone NOT NULL,
  modificado timestamp without time zone NOT NULL
) WITH (
  OIDS=FALSE
);
-- ALTERACIONES A LOS CAMPOS DE LA TABLA
ALTER TABLE geogoremad_seguridad.empresa ADD CONSTRAINT empresa_id_empresa_pkey PRIMARY KEY (id_empresa);
ALTER TABLE geogoremad_seguridad.empresa ADD CONSTRAINT empresa_codigo_empresa_key UNIQUE (codigo_empresa);
ALTER TABLE geogoremad_seguridad.empresa ALTER COLUMN estado SET DEFAULT true;
ALTER TABLE geogoremad_seguridad.empresa ALTER COLUMN creado SET DEFAULT current_timestamp;
ALTER TABLE geogoremad_seguridad.empresa ALTER COLUMN modificado SET DEFAULT current_timestamp;
-- DESCRIPCION DE LOS CAMPOS DE LA TABLA
COMMENT ON TABLE geogoremad_seguridad.empresa IS 'Tabla que contiene los datos de las empresas';
COMMENT ON COLUMN geogoremad_seguridad.empresa.id_empresa IS 'Identificador de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa.codigo_empresa IS 'Codigo de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa.nombre_empresa IS 'Nombre de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa.descripcion_empresa IS 'Descripcion de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa.logo_empresa IS 'Logo de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa.url_empresa IS 'Url de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa.estado IS 'Estado de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa.creado IS 'Fecha de creacion de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa.modificado IS 'Fecha de modificacion de la empresa';

/* ==========================================================================================
AUTOR: WILLIAM CONDORI QUISPE
FECHA: 18-07-2022
NOMBRE DEL OBJETO: geogoremad_seguridad.empresa_configuracion
DESCRIPCION: Tabla que contiene los datos de las configuraciones de las empresas
EJEMPLO DE USO:
========================================================================================== */
-- DEFINICION DE LA TABLA
CREATE TABLE geogoremad_seguridad.empresa_configuracion (
  id_empresa integer NOT NULL,
  clave_configuracion character varying(15) NOT NULL,
  valor_configuracion character varying(255) NOT NULL,
  estado boolean NOT NULL,
  creado timestamp without time zone NOT NULL,
  modificado timestamp without time zone NOT NULL
) WITH (
  OIDS=FALSE
);
-- ALTERACIONES A LOS CAMPOS DE LA TABLA
ALTER TABLE geogoremad_seguridad.empresa_configuracion ADD CONSTRAINT empresa_configuracion_id_empresa_clave_configuracion_pkey PRIMARY KEY (id_empresa, clave_configuracion);
ALTER TABLE geogoremad_seguridad.empresa_configuracion ADD CONSTRAINT empresa_configuracion_empresa_fkey 
    FOREIGN KEY (id_empresa) REFERENCES geogoremad_seguridad.empresa (id_empresa) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE geogoremad_seguridad.empresa_configuracion ALTER COLUMN estado SET DEFAULT true;
ALTER TABLE geogoremad_seguridad.empresa_configuracion ALTER COLUMN creado SET DEFAULT current_timestamp;
ALTER TABLE geogoremad_seguridad.empresa_configuracion ALTER COLUMN modificado SET DEFAULT current_timestamp;
-- DESCRIPCION DE LOS CAMPOS DE LA TABLA
COMMENT ON TABLE geogoremad_seguridad.empresa_configuracion IS 'Tabla que contiene los datos de las configuraciones de las empresas';
COMMENT ON COLUMN geogoremad_seguridad.empresa_configuracion.id_empresa IS 'Identificador de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa_configuracion.clave_configuracion IS 'Clave de la configuracion de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa_configuracion.valor_configuracion IS 'Valor de la configuracion de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa_configuracion.estado IS 'Estado de la configuracion de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa_configuracion.creado IS 'Fecha de creacion de la configuracion de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa_configuracion.modificado IS 'Fecha de modificacion de la configuracion de la empresa';

/* ==========================================================================================
AUTOR: WILLIAM CONDORI QUISPE
FECHA: 18-07-2022
NOMBRE DEL OBJETO: geogoremad_seguridad.usuario
DESCRIPCION: Tabla que contiene los datos de los usuarios
EJEMPLO DE USO:
========================================================================================== */
-- DEFINICION DE LA TABLA
CREATE TABLE geogoremad_seguridad.usuario (
  id_usuario serial NOT NULL,
  id_empresa integer NOT NULL,
  nombre_usuario character varying(100) NOT NULL,
  apellido_usuario character varying(100) NOT NULL,
  codigo_usuario character varying(15) NOT NULL,
  contrasenia_usuario character varying(255) NOT NULL,
  email_usuario character varying(100) NOT NULL,
  estado boolean NOT NULL,
  creado timestamp without time zone NOT NULL,
  modificado timestamp without time zone NOT NULL
) WITH (
  OIDS=FALSE
);
-- ALTERACIONES A LOS CAMPOS DE LA TABLA
ALTER TABLE geogoremad_seguridad.usuario ADD CONSTRAINT usuario_id_usuario_pkey PRIMARY KEY (id_usuario);
ALTER TABLE geogoremad_seguridad.usuario ADD CONSTRAINT usuario_empresa_fkey 
    FOREIGN KEY (id_empresa) REFERENCES geogoremad_seguridad.empresa (id_empresa) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE geogoremad_seguridad.usuario ADD CONSTRAINT usuario_codigo_usuario_key UNIQUE (codigo_usuario);
ALTER TABLE geogoremad_seguridad.usuario ALTER COLUMN estado SET DEFAULT true;
ALTER TABLE geogoremad_seguridad.usuario ALTER COLUMN creado SET DEFAULT current_timestamp;
ALTER TABLE geogoremad_seguridad.usuario ALTER COLUMN modificado SET DEFAULT current_timestamp;
-- DESCRIPCION DE LOS CAMPOS DE LA TABLA
COMMENT ON TABLE geogoremad_seguridad.usuario IS 'Tabla que contiene los datos de los usuarios';
COMMENT ON COLUMN geogoremad_seguridad.usuario.id_usuario IS 'Identificador del usuario';
COMMENT ON COLUMN geogoremad_seguridad.usuario.id_empresa IS 'Identificador de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.usuario.nombre_usuario IS 'Nombre del usuario';
COMMENT ON COLUMN geogoremad_seguridad.usuario.apellido_usuario IS 'Apellido del usuario';
COMMENT ON COLUMN geogoremad_seguridad.usuario.codigo_usuario IS 'Codigo del usuario (para el inicio de sesion)';
COMMENT ON COLUMN geogoremad_seguridad.usuario.contrasenia_usuario IS 'Contrasenia del usuario';
COMMENT ON COLUMN geogoremad_seguridad.usuario.email_usuario IS 'Email del usuario';
COMMENT ON COLUMN geogoremad_seguridad.usuario.estado IS 'Estado del usuario';
COMMENT ON COLUMN geogoremad_seguridad.usuario.creado IS 'Fecha de creacion del usuario';
COMMENT ON COLUMN geogoremad_seguridad.usuario.modificado IS 'Fecha de modificacion del usuario';

/* ==========================================================================================
AUTOR: WILLIAM CONDORI QUISPE
FECHA: 18-07-2022
NOMBRE DEL OBJETO: geogoremad_seguridad.usuario_configuracion
DESCRIPCION: Tabla que contiene los datos de las configuraciones de los usuarios
EJEMPLO DE USO:
========================================================================================== */
-- DEFINICION DE LA TABLA
CREATE TABLE geogoremad_seguridad.usuario_configuracion (
  id_usuario integer NOT NULL,
  clave_configuracion character varying(100) NOT NULL,
  valor_configuracion character varying(255) NOT NULL,
  estado boolean NOT NULL,
  creado timestamp without time zone NOT NULL,
  modificado timestamp without time zone NOT NULL
) WITH (
  OIDS=FALSE
);
-- ALTERACIONES A LOS CAMPOS DE LA TABLA
ALTER TABLE geogoremad_seguridad.usuario_configuracion ADD CONSTRAINT usuario_configuracion_id_usuario_clave_configuracion_pkey PRIMARY KEY (id_usuario, clave_configuracion);
ALTER TABLE geogoremad_seguridad.usuario_configuracion ADD CONSTRAINT usuario_configuracion_usuario_fkey 
    FOREIGN KEY (id_usuario) REFERENCES geogoremad_seguridad.usuario (id_usuario) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE geogoremad_seguridad.usuario_configuracion ALTER COLUMN estado SET DEFAULT true;
ALTER TABLE geogoremad_seguridad.usuario_configuracion ALTER COLUMN creado SET DEFAULT current_timestamp;
ALTER TABLE geogoremad_seguridad.usuario_configuracion ALTER COLUMN modificado SET DEFAULT current_timestamp;
-- DESCRIPCION DE LOS CAMPOS DE LA TABLA
COMMENT ON TABLE geogoremad_seguridad.usuario_configuracion IS 'Tabla que contiene las configuraciones de los usuarios';
COMMENT ON COLUMN geogoremad_seguridad.usuario_configuracion.id_usuario IS 'Identificador del usuario';
COMMENT ON COLUMN geogoremad_seguridad.usuario_configuracion.clave_configuracion IS 'Clave de la configuracion';
COMMENT ON COLUMN geogoremad_seguridad.usuario_configuracion.valor_configuracion IS 'Valor de la configuracion';
COMMENT ON COLUMN geogoremad_seguridad.usuario_configuracion.estado IS 'Estado de la configuracion';
COMMENT ON COLUMN geogoremad_seguridad.usuario_configuracion.creado IS 'Fecha de creacion de la configuracion';
COMMENT ON COLUMN geogoremad_seguridad.usuario_configuracion.modificado IS 'Fecha de modificacion de la configuracion';
