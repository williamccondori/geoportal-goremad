from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST

from companies import services
from companies.schemas import GetCompaniesResponse, CreateCompanyResponse, CreateCompanyRequest, GetCompanyResponse
from shared.database import SessionLocal

company_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@company_router.patch("/check", response_model=bool)
async def check_companies(db: Session = Depends(get_db)) -> bool:
    try:
        return services.check_companies(db)
    except Exception as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))


@company_router.get("/", response_model=List[GetCompaniesResponse])
async def get_companies(db: Session = Depends(get_db)) -> List[GetCompaniesResponse]:
    try:
        return services.get_companies(db)
    except Exception as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))


@company_router.get("/{company_id}", response_model=GetCompanyResponse)
async def get_company(company_id: int, db: Session = Depends(get_db)) -> GetCompanyResponse:
    try:
        return services.get_company(db, company_id)
    except Exception as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))


@company_router.post("/", response_model=CreateCompanyResponse, status_code=201)
async def create_company(company: CreateCompanyRequest, db: Session = Depends(get_db)) -> CreateCompanyResponse:
    try:
        return services.create_company(db, company)
    except Exception as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))


@company_router.delete("/{company_id}")
async def delete_company(company_id: int, db: Session = Depends(get_db)) -> int:
    try:
        return services.delete_company(db, company_id)
    except Exception as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))
