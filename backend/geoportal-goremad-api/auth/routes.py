from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from auth import services
from auth.schemas import GetCurrentUserResponse, LoginResponse, LoginRequest
from shared.dependencies.get_current_user_information import get_current_user_information
from shared.dependencies.get_database_context import get_database_context
from shared.exceptions.shared.api_exception import ApiException

auth_router = APIRouter()


@auth_router.post("/login", response_model=LoginResponse)
async def login(form_data: OAuth2PasswordRequestForm = Depends(),
                db: Session = Depends(get_database_context)) -> LoginResponse:
    try:
        return services.login(db, LoginRequest(
            username=form_data.username,
            password=form_data.password
        ))
    except ApiException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@auth_router.get("/current-user", response_model=GetCurrentUserResponse)
async def get_current_user(username: str = Depends(get_current_user_information),
                           db: Session = Depends(get_database_context)) -> GetCurrentUserResponse:
    try:
        return services.get_current_user(db, username)
    except ApiException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
