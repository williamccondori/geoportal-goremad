from dotenv import load_dotenv
from fastapi import FastAPI

from companies.routes import company_router

load_dotenv()

app = FastAPI()
app.include_router(company_router, prefix='/companies', tags=['Company'])
