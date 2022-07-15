from dotenv import load_dotenv
from fastapi import FastAPI

from routes.auth import auth_routes
from routes.user_routes import user_router
from routes.vector_layer_routes import vector_layer_router

load_dotenv()

app = FastAPI()
app.include_router(user_router, prefix='/users', tags=['Users'])
app.include_router(vector_layer_router, prefix='/vector-layers', tags=['Vector layers'])
app.include_router(auth_routes, prefix="/api")
