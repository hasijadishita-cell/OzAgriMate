from fastapi import FastAPI, HTTPException
from app.controller import router

app= FastAPI(title="OzAgriMate Farm Management Service")
app.include_router(router)
