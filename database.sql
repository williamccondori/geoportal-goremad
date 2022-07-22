-- CREACION DE ESQUEMAS DE LA BASE DE DATOS
CREATE SCHEMA geogoremad_general;
CREATE SCHEMA geogoremad_seguridad;
CREATE SCHEMA geogoremad_geoportal;
CREATE SCHEMA geogoremad_capas;

SET search_path = public,geogoremad_capas;

CREATE EXTENSION postgis WITH SCHEMA geogoremad_capas;

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
  vc_codigo_empresa character varying(15) NOT NULL,
  vc_nombre_empresa character varying(100) NOT NULL,
  vc_descripcion_empresa character varying(255) NOT NULL,
  vc_logo_empresa character varying(255) NULL,
  vc_url_empresa character varying(255) NULL,
  bo_habilitado boolean NOT NULL,
  bo_estado boolean NOT NULL,
  ts_creado timestamp without time zone NOT NULL,
  ts_modificado timestamp without time zone NOT NULL
) WITH (
  OIDS=FALSE
);
-- ALTERACIONES A LOS CAMPOS DE LA TABLA
ALTER TABLE geogoremad_seguridad.empresa ADD CONSTRAINT empresa_pkey PRIMARY KEY (id_empresa);
ALTER TABLE geogoremad_seguridad.empresa ALTER COLUMN bo_habilitado SET DEFAULT true;
ALTER TABLE geogoremad_seguridad.empresa ALTER COLUMN bo_estado SET DEFAULT true;
ALTER TABLE geogoremad_seguridad.empresa ALTER COLUMN ts_creado SET DEFAULT current_timestamp;
ALTER TABLE geogoremad_seguridad.empresa ALTER COLUMN ts_modificado SET DEFAULT current_timestamp;
-- DESCRIPCION DE LOS CAMPOS DE LA TABLA
COMMENT ON TABLE geogoremad_seguridad.empresa IS 'Tabla que contiene los datos de las empresas';
COMMENT ON COLUMN geogoremad_seguridad.empresa.id_empresa IS 'Identificador de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa.vc_codigo_empresa IS 'Codigo de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa.vc_nombre_empresa IS 'Nombre de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa.vc_descripcion_empresa IS 'Descripcion de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa.vc_logo_empresa IS 'Logo de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa.vc_url_empresa IS 'Url de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa.bo_estado IS 'Estado de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa.ts_creado IS 'Fecha de creacion de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa.ts_modificado IS 'Fecha de modificacion de la empresa';

/* ==========================================================================================
AUTOR: WILLIAM CONDORI QUISPE
FECHA: 18-07-2022
NOMBRE DEL OBJETO: geogoremad_seguridad.empresa_configuracion
DESCRIPCION: Tabla que contiene los datos de las configuraciones de las empresas
EJEMPLO DE USO:
========================================================================================== */
-- DEFINICION DE LA TABLA
CREATE TABLE geogoremad_seguridad.empresa_configuracion (
  id_empresa_configuracion serial NOT NULL,
  id_empresa integer NOT NULL,
  vc_clave_configuracion character varying(15) NOT NULL,
  vc_valor_configuracion character varying(255) NOT NULL,
  bo_estado boolean NOT NULL,
  ts_creado timestamp without time zone NOT NULL,
  ts_modificado timestamp without time zone NOT NULL
) WITH (
  OIDS=FALSE
);
-- ALTERACIONES A LOS CAMPOS DE LA TABLA
ALTER TABLE geogoremad_seguridad.empresa_configuracion ADD CONSTRAINT empresa_configuracion_pkey PRIMARY KEY (id_empresa_configuracion);
ALTER TABLE geogoremad_seguridad.empresa_configuracion ADD CONSTRAINT empresa_configuracion_empresa_fkey 
    FOREIGN KEY (id_empresa) REFERENCES geogoremad_seguridad.empresa (id_empresa) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE geogoremad_seguridad.empresa_configuracion ALTER COLUMN bo_estado SET DEFAULT true;
ALTER TABLE geogoremad_seguridad.empresa_configuracion ALTER COLUMN ts_creado SET DEFAULT current_timestamp;
ALTER TABLE geogoremad_seguridad.empresa_configuracion ALTER COLUMN ts_modificado SET DEFAULT current_timestamp;
-- DESCRIPCION DE LOS CAMPOS DE LA TABLA
COMMENT ON TABLE geogoremad_seguridad.empresa_configuracion IS 'Tabla que contiene los datos de las configuraciones de las empresas';
COMMENT ON COLUMN geogoremad_seguridad.empresa_configuracion.id_empresa_configuracion IS 'Identificador de la configuracion de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa_configuracion.id_empresa IS 'Identificador de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa_configuracion.vc_clave_configuracion IS 'Clave de la configuracion de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa_configuracion.vc_valor_configuracion IS 'Valor de la configuracion de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa_configuracion.bo_estado IS 'Estado de la configuracion de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa_configuracion.ts_creado IS 'Fecha de creacion de la configuracion de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.empresa_configuracion.ts_modificado IS 'Fecha de modificacion de la configuracion de la empresa';

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
  vc_nombre_usuario character varying(100) NULL,
  vc_apellido_usuario character varying(100) NULL,
  vc_codigo_usuario character varying(15) NOT NULL,
  vc_contrasenia_usuario character varying(255) NOT NULL,
  vc_email_usuario character varying(100) NOT NULL,
  bo_habilitado boolean NOT NULL,
  bo_estado boolean NOT NULL,
  ts_creado timestamp without time zone NOT NULL,
  ts_modificado timestamp without time zone NOT NULL
) WITH (
  OIDS=FALSE
);
-- ALTERACIONES A LOS CAMPOS DE LA TABLA
ALTER TABLE geogoremad_seguridad.usuario ADD CONSTRAINT usuario_pkey PRIMARY KEY (id_usuario);
ALTER TABLE geogoremad_seguridad.usuario ADD CONSTRAINT usuario_empresa_fkey 
    FOREIGN KEY (id_empresa) REFERENCES geogoremad_seguridad.empresa (id_empresa) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE geogoremad_seguridad.usuario ALTER COLUMN bo_habilitado SET DEFAULT true;
ALTER TABLE geogoremad_seguridad.usuario ALTER COLUMN bo_estado SET DEFAULT true;
ALTER TABLE geogoremad_seguridad.usuario ALTER COLUMN ts_creado SET DEFAULT current_timestamp;
ALTER TABLE geogoremad_seguridad.usuario ALTER COLUMN ts_modificado SET DEFAULT current_timestamp;
-- DESCRIPCION DE LOS CAMPOS DE LA TABLA
COMMENT ON TABLE geogoremad_seguridad.usuario IS 'Tabla que contiene los datos de los usuarios';
COMMENT ON COLUMN geogoremad_seguridad.usuario.id_usuario IS 'Identificador del usuario';
COMMENT ON COLUMN geogoremad_seguridad.usuario.id_empresa IS 'Identificador de la empresa';
COMMENT ON COLUMN geogoremad_seguridad.usuario.vc_nombre_usuario IS 'Nombre del usuario';
COMMENT ON COLUMN geogoremad_seguridad.usuario.vc_apellido_usuario IS 'Apellido del usuario';
COMMENT ON COLUMN geogoremad_seguridad.usuario.vc_codigo_usuario IS 'Codigo del usuario (para el inicio de sesion)';
COMMENT ON COLUMN geogoremad_seguridad.usuario.vc_contrasenia_usuario IS 'Contrasenia del usuario';
COMMENT ON COLUMN geogoremad_seguridad.usuario.vc_email_usuario IS 'Email del usuario';
COMMENT ON COLUMN geogoremad_seguridad.usuario.bo_estado IS 'Estado del usuario';
COMMENT ON COLUMN geogoremad_seguridad.usuario.ts_creado IS 'Fecha de creacion del usuario';
COMMENT ON COLUMN geogoremad_seguridad.usuario.ts_modificado IS 'Fecha de modificacion del usuario';

/* ==========================================================================================
AUTOR: WILLIAM CONDORI QUISPE
FECHA: 18-07-2022
NOMBRE DEL OBJETO: geogoremad_seguridad.usuario_configuracion
DESCRIPCION: Tabla que contiene los datos de las configuraciones de los usuarios
EJEMPLO DE USO:
========================================================================================== */
-- DEFINICION DE LA TABLA
CREATE TABLE geogoremad_seguridad.usuario_configuracion (
  id_usuario_configuracion serial NOT NULL,
  id_usuario integer NOT NULL,
  vc_clave_configuracion character varying(100) NOT NULL,
  vc_valor_configuracion character varying(255) NOT NULL,
  bo_estado boolean NOT NULL,
  ts_creado timestamp without time zone NOT NULL,
  ts_modificado timestamp without time zone NOT NULL
) WITH (
  OIDS=FALSE
);
-- ALTERACIONES A LOS CAMPOS DE LA TABLA
ALTER TABLE geogoremad_seguridad.usuario_configuracion ADD CONSTRAINT usuario_configuracion_pkey PRIMARY KEY (id_usuario_configuracion);
ALTER TABLE geogoremad_seguridad.usuario_configuracion ADD CONSTRAINT usuario_configuracion_usuario_fkey 
    FOREIGN KEY (id_usuario) REFERENCES geogoremad_seguridad.usuario (id_usuario) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE geogoremad_seguridad.usuario_configuracion ALTER COLUMN bo_estado SET DEFAULT true;
ALTER TABLE geogoremad_seguridad.usuario_configuracion ALTER COLUMN ts_creado SET DEFAULT current_timestamp;
ALTER TABLE geogoremad_seguridad.usuario_configuracion ALTER COLUMN ts_modificado SET DEFAULT current_timestamp;
-- DESCRIPCION DE LOS CAMPOS DE LA TABLA
COMMENT ON TABLE geogoremad_seguridad.usuario_configuracion IS 'Tabla que contiene las configuraciones de los usuarios';
COMMENT ON COLUMN geogoremad_seguridad.usuario_configuracion.id_usuario_configuracion IS 'Identificador de la configuracion del usuario';
COMMENT ON COLUMN geogoremad_seguridad.usuario_configuracion.id_usuario IS 'Identificador del usuario';
COMMENT ON COLUMN geogoremad_seguridad.usuario_configuracion.vc_clave_configuracion IS 'Clave de la configuracion';
COMMENT ON COLUMN geogoremad_seguridad.usuario_configuracion.vc_valor_configuracion IS 'Valor de la configuracion';
COMMENT ON COLUMN geogoremad_seguridad.usuario_configuracion.bo_estado IS 'Estado de la configuracion';
COMMENT ON COLUMN geogoremad_seguridad.usuario_configuracion.ts_creado IS 'Fecha de creacion de la configuracion';
COMMENT ON COLUMN geogoremad_seguridad.usuario_configuracion.ts_modificado IS 'Fecha de modificacion de la configuracion';


/* ==========================================================================================
AUTOR: WILLIAM CONDORI QUISPE
FECHA: 18-07-2022
NOMBRE DEL OBJETO: geogoremad_geoportal.capa_vectorial
DESCRIPCION: Tabla que contiene los datos de las capas vectoriales
EJEMPLO DE USO:
========================================================================================== */
-- DEFINICION DE LA TABLA
CREATE TABLE geogoremad_geoportal.capa_vectorial (
  id_capa_vectorial serial NOT NULL,
  vc_nombre character varying(100) NOT NULL,
  vc_titulo character varying(100) NOT NULL,
  vc_descripcion character varying(255) NULL,
  bo_publico boolean NOT NULL,
  bo_habilitado boolean NOT NULL,
  bo_estado boolean NOT NULL,
  ts_creado timestamp without time zone NOT NULL,
  ts_modificado timestamp without time zone NOT NULL,
  vc_usuario_creador character varying(100) NOT NULL,
  vc_usuario_modificador character varying(100) NOT NULL,
) WITH (
  OIDS=FALSE
);
-- ALTERACIONES A LOS CAMPOS DE LA TABLA
ALTER TABLE geogoremad_geoportal.capa_vectorial ADD CONSTRAINT capa_vectorial_pkey PRIMARY KEY (id_capa_vectorial);
ALTER TABLE geogoremad_geoportal.capa_vectorial ALTER COLUMN bo_publico SET DEFAULT false;
ALTER TABLE geogoremad_geoportal.capa_vectorial ALTER COLUMN bo_habilitado SET DEFAULT true;
ALTER TABLE geogoremad_geoportal.capa_vectorial ALTER COLUMN bo_estado SET DEFAULT true;
ALTER TABLE geogoremad_geoportal.capa_vectorial ALTER COLUMN ts_creado SET DEFAULT current_timestamp;
ALTER TABLE geogoremad_geoportal.capa_vectorial ALTER COLUMN ts_modificado SET DEFAULT current_timestamp;
-- DESCRIPCION DE LOS CAMPOS DE LA TABLA
COMMENT ON TABLE geogoremad_geoportal.capa_vectorial IS 'Tabla que contiene las capas vectoriales';
COMMENT ON COLUMN geogoremad_geoportal.capa_vectorial.id_capa_vectorial IS 'Identificador de la capa vectorial';
COMMENT ON COLUMN geogoremad_geoportal.capa_vectorial.vc_nombre IS 'Nombre de la capa vectorial';
COMMENT ON COLUMN geogoremad_geoportal.capa_vectorial.vc_titulo IS 'Titulo de la capa vectorial';
COMMENT ON COLUMN geogoremad_geoportal.capa_vectorial.vc_descripcion IS 'Descripcion de la capa vectorial';
COMMENT ON COLUMN geogoremad_geoportal.capa_vectorial.bo_publico IS 'Indica si la capa vectorial es publica';
COMMENT ON COLUMN geogoremad_geoportal.capa_vectorial.bo_habilitado IS 'Indica si la capa vectorial esta habilitada';
COMMENT ON COLUMN geogoremad_geoportal.capa_vectorial.bo_estado IS 'Indica si la capa vectorial esta activa';
COMMENT ON COLUMN geogoremad_geoportal.capa_vectorial.ts_creado IS 'Fecha de creacion de la capa vectorial';
COMMENT ON COLUMN geogoremad_geoportal.capa_vectorial.ts_modificado IS 'Fecha de modificacion de la capa vectorial';
COMMENT ON COLUMN geogoremad_geoportal.capa_vectorial.vc_usuario_creador IS 'Usuario que creo la capa vectorial';
COMMENT ON COLUMN geogoremad_geoportal.capa_vectorial.vc_usuario_modificador IS 'Usuario que modifico la capa vectorial';