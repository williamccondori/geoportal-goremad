import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
__db_host = os.environ.get("POSTGRES_HOST")
__db_port = os.environ.get("POSTGRES_PORT", 5432)
__db_user = os.environ.get("POSTGRES_USER")
__db_pass = os.environ.get("POSTGRES_PASS")
__db_name = os.environ.get("POSTGRES_DBNAME")

SQLALCHEMY_DATABASE_URL = f"postgresql://{__db_user}:{__db_pass}@{__db_host}:{__db_port}/{__db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
