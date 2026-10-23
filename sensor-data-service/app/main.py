from fastapi import FastAPI
from app.controller import router

app = FastAPI(title="Sensor Data Service")
app.include_router(router)