from fastapi import APIRouter

from shared.database import SessionLocal

auth_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
