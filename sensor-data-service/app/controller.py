from fastapi import APIRouter
from app import service, status_tracker
from app.models import LatestSensorReadingsResponse, SensorStatusResponse

router = APIRouter()

# GET /farms/{farmId}/readings/latest
@router.get("/farms/{farmId}/readings/latest", response_model=LatestSensorReadingsResponse)
def get_latest_readings(farmId: int):
    return service.get_latest_readings(farmId)

# GET /sensors/{sensorId}/status
@router.get("/sensors/{sensorId}/status", response_model=SensorStatusResponse)
def get_sensor_status(sensorId: int):
    return status_tracker.get_sensor_status(sensorId)