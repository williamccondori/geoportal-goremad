from typing import List

from sqlalchemy.orm import Session

from companies import models
from companies.schemas import GetCompaniesResponse, GetCompanyResponse, CreateCompanyRequest, CreateCompanyResponse


def get_companies(db: Session) -> List[GetCompaniesResponse]:
    return db.query(models.Company).all()


def get_company(db: Session, company_id: int) -> GetCompanyResponse:
    return db.query(models.Company).get(company_id)


def create_company(db: Session, company: CreateCompanyRequest) -> CreateCompanyResponse:
    db_company = models.Company(
        name=company.name,
        description=company.description,
        logo=company.logo
    )
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def delete_company(db: Session, company_id: int) -> int:
    db_company = db.query(models.Company).get(company_id)
    db.delete(db_company)
    db.commit()
    return company_id
