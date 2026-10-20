from fastapi import FastAPI

from app.controllers.irrigation_controller import router as irrigation_router


app = FastAPI(
    title="OzAgriMate Irrigation Management Service"
)

app.include_router(irrigation_router)