from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST

from companies import services
from companies.schemas import GetCompaniesResponse, CreateCompanyResponse, CreateCompanyRequest, GetCompanyResponse
from shared.dependencies.get_current_user_information import get_current_user_information
from shared.dependencies.get_database_context import get_database_context

company_router = APIRouter()


@company_router.patch("/check", response_model=bool)
async def check_companies(db: Session = Depends(get_database_context)) -> bool:
    try:
        return services.check_companies(db)
    except Exception as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))


@company_router.get("/", response_model=List[GetCompaniesResponse])
async def get_companies(db: Session = Depends(get_database_context),
                        _: str = Depends(get_current_user_information)) -> List[GetCompaniesResponse]:
    try:
        return services.get_companies(db)
    except Exception as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))


@company_router.get("/{company_id}", response_model=GetCompanyResponse)
async def get_company(company_id: int, db: Session = Depends(get_database_context),
                      _: str = Depends(get_current_user_information)) -> GetCompanyResponse:
    try:
        return services.get_company(db, company_id)
    except Exception as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))


@company_router.post("/", response_model=CreateCompanyResponse, status_code=201)
async def create_company(company: CreateCompanyRequest, db: Session = Depends(get_database_context),
                         _: str = Depends(get_current_user_information)) -> CreateCompanyResponse:
    try:
        return services.create_company(db, company)
    except Exception as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))


@company_router.delete("/{company_id}")
async def delete_company(company_id: int, db: Session = Depends(get_database_context),
                         _: str = Depends(get_current_user_information)) -> int:
    try:
        return services.delete_company(db, company_id)
    except Exception as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))
