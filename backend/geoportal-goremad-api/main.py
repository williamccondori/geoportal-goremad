from fastapi import FastAPI

from auth.routes import auth_router
from companies.routes import company_router

app = FastAPI()

app.include_router(auth_router, prefix='/auth', tags=['Auth'])
app.include_router(company_router, prefix='/companies', tags=['Company'])
# app.include_router(user_router, prefix='/users', tags=['User'])

# Información geográfica
# app.include_router(schema_router, prefix='/schemas', tags=['Schemas'])
# app.include_router(group_layer_router, prefix='group-layers', tags=['Group layers'])
# app.include_router(vector_layer_router, prefix='vector-layers', tags=['Vector layers'])
# app.include_router(raster_layer_router, prefix='raster-layers', tags=['Raster layers'])
