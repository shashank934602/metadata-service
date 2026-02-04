from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Metadata Service")

app.include_router(router)
