from fastapi import APIRouter
from fastapi.responses import Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

user_router = APIRouter()


@user_router.get("/")
async def get_all_users() -> Response:
    return Response(content={"users": []}, status_code=HTTP_200_OK)


@user_router.get("/{user_id}")
async def get_user(user_id: int) -> Response:
    return Response(content={"user": {"id": user_id, "name": "John Doe"}}, status_code=HTTP_201_CREATED)


@user_router.post("/")
async def create_user() -> Response:
    return Response(content={"user": {"id": 1, "name": "John Doe"}}, status_code=HTTP_200_OK)


@user_router.put("/{user_id}")
async def update_user(user_id: int) -> Response:
    return Response(content={"user": {"id": user_id, "name": "John Doe"}}, status_code=HTTP_200_OK)


@user_router.delete("/{user_id}")
async def delete_user(user_id: int) -> Response:
    return Response(content={"user": {"id": user_id, "name": "John Doe"}}, status_code=HTTP_200_OK)
