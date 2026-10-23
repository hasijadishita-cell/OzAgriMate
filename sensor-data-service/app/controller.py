from fastapi import APIRouter
from app import service, status_tracker
from app.models import LatestSensorReadingsResponse, SensorStatusResponse, AddSensorReadingRequest,AddSensorReadingResponse;

router = APIRouter()

# GET /farms/{farmId}/readings/latest
@router.get("/farms/{farmId}/readings/latest", response_model=LatestSensorReadingsResponse)
def get_latest_readings(farmId: int):
    return service.get_latest_readings(farmId)

# GET /sensors/{sensorId}/status
@router.get("/sensors/{sensorId}/status", response_model=SensorStatusResponse)
def get_sensor_status(sensorId: int):
    return status_tracker.get_sensor_status(sensorId)

# POST /sensors/{sensorId}/readings
@router.post("/sensors/{sensorId}/readings", status_code=201, response_model=AddSensorReadingResponse)
def add_reading(sensorId: int, reading: AddSensorReadingRequest):
    return service.add_reading(sensorId, reading)