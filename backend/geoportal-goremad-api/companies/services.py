from typing import List

import bcrypt
from sqlalchemy.orm import Session

from companies.models import Company, CompanyConfiguration
from companies.schemas import GetCompaniesResponse, GetCompanyResponse, CreateCompanyRequest, CreateCompanyResponse
from users.models import User, UserConfiguration


def __get_company_by_code(db: Session, code: str) -> Company:
    return db.query(Company).where(Company.code == code, Company.status).first()


def check_company(db: Session, company_id: int) -> bool:
    return db.query(Company).where(Company.id == company_id, Company.status).count() > 0


def check_companies(db: Session) -> bool:
    return db.query(Company).where(Company.status).count() > 0


def get_companies(db: Session) -> List[GetCompaniesResponse]:
    companies = db.query(Company).where(Company.status).all()
    return [
        GetCompaniesResponse(
            id=company.id,
            code=company.code,
            name=company.name,
            description=company.description,
            logo=company.logo,
            url=company.url
        ) for company in companies
    ]


def get_company(db: Session, company_id: int) -> GetCompanyResponse:
    company_existss = check_company(db, company_id)
    if not company_existss:
        raise Exception("La empresa con código {} no existe".format(company_id))

    company = db.query(Company).get(company_id)
    return GetCompanyResponse(
        id=company.id,
        code=company.code,
        name=company.name,
        description=company.description,
        logo=company.logo,
        url=company.url
    )


def create_company(db: Session, company: CreateCompanyRequest) -> CreateCompanyResponse:
    company_exists = __get_company_by_code(db, company.code)
    if company_exists:
        raise Exception("La empresa con código {} ya existe".format(company.code))

    # Validacion de contrasenia
    user_default_password = company.password
    if len(user_default_password) < 8:  # Si la contrasenia es menor a 8 caracteres
        raise Exception("La contraseña debe tener al menos 8 caracteres")
    if user_default_password.isalpha():  # Si solo tiene letras
        raise Exception("La contraseña debe tener al menos un caracter numérico")
    if user_default_password.isnumeric():  # Si solo tiene numeros
        raise Exception("La contraseña debe tener al menos un caracter alfabético")

    # Validacion de codigo
    company_code = company.code.lower()
    if len(company_code) > 15:  # Si el codigo es mayor a 15 caracteres
        raise Exception("El código debe tener menos de 15 caracteres")
    if not company_code.isalpha():  # Si solo tiene letras
        # Si el codigo tiene espacios o numeros
        raise Exception("El código debe tener solo caracteres alfabéticos")

    # CONFIGURACION DE LA EMPRESA
    initial_zoom = CompanyConfiguration(key="zoom_inicial", value="13")
    db.add(initial_zoom)

    # USUARIOS

    # CONFIGURACION DEL USUARIO
    user_initial_zoom = UserConfiguration(key="zoom_inicial", value="13")
    db.add(user_initial_zoom)

    hashed_password = bcrypt.hashpw(user_default_password.encode("utf-8"), bcrypt.gensalt())
    user_default = User(
        username="administrador",
        password=hashed_password.decode("utf-8"),
        email=f"administrador@{company.code}.com",
    )
    user_default.settings = [user_initial_zoom]
    db.add(user_default)

    # EMPRESA
    new_company = Company(
        code=company_code,
        name=company.name,
        description=company.description,
        logo=company.logo,
        url=company.url
    )
    new_company.settings = [initial_zoom]
    new_company.users = [user_default]

    db.add(new_company)
    db.commit()

    db.refresh(new_company)

    return CreateCompanyResponse(
        id=new_company.id,
        code=new_company.code,
        name=new_company.name,
        description=new_company.description,
        logo=new_company.logo,
        url=new_company.url
    )


def delete_company(db: Session, company_id: int) -> int:
    company_existss = check_company(db, company_id)
    if not company_existss:
        raise Exception("La empresa con código {} no existe".format(company_id))

    company = db.query(Company).get(company_id)
    company.status = False

    # Eliminar configuraciones
    settings = db.query(CompanyConfiguration).where(CompanyConfiguration.company_id == company_id).all()
    for setting in settings:
        setting.status = False

    # Eliminar usuarios
    users = db.query(User).where(User.company_id == company_id).all()
    for user in users:
        user.status = False

    db.commit()

    return company_id
