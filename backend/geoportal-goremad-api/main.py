from fastapi import FastAPI

from companies.routes import company_router

app = FastAPI()
app.include_router(company_router, prefix='/companies', tags=['Company'])
