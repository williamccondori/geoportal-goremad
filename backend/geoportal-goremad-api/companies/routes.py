from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK

from companies import services
from companies.schemas import GetCompaniesResponse, CreateCompanyResponse, CreateCompanyRequest
from shared.database import SessionLocal

company_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@company_router.get("/", response_model=List[GetCompaniesResponse])
async def get_companies(db: Session = Depends(get_db)) -> JSONResponse:
    db_company = services.get_companies(db)
    return JSONResponse(content=db_company, status_code=HTTP_200_OK)


@company_router.get("/{company_id}", response_model=GetCompaniesResponse)
async def get_company(company_id: int, db: Session = Depends(get_db)) -> JSONResponse:
    db_company = services.get_company(db, company_id)
    return JSONResponse(content=db_company, status_code=HTTP_200_OK)


@company_router.post("/", response_model=CreateCompanyResponse)
async def create_company(company: CreateCompanyRequest, db: Session = Depends(get_db)) -> JSONResponse:
    db_company = services.create_company(db, company)
    return JSONResponse(content=db_company, status_code=HTTP_200_OK)


@company_router.delete("/{company_id}")
async def delete_company(company_id: int, db: Session = Depends(get_db)) -> JSONResponse:
    db_company_id = services.delete_company(db, company_id)
    return JSONResponse(content=db_company_id, status_code=HTTP_200_OK)
