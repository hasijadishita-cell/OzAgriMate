from pydantic import BaseModel
from datetime import datetime
from typing import List

# POST  ||  /sensors/{sensorId}/readings
class AddSensorReadingRequest(BaseModel):
    readingType: str
    value: float
    unit: str
    recordedAt: datetime


class AddSensorReadingResponse(BaseModel):
    readingId: int
    sensorId: int
    farmId: int
    message: str


# GET  ||  /farms/{farmId}/readings/latest
class SensorReading(BaseModel):
    sensorId: int
    readingType: str
    value: float
    unit: str
    recordedAt: datetime


class LatestSensorReadingsResponse(BaseModel):
    farmId: int
    readings: List[SensorReading]

# GET  ||  /sensors/{sensorId}/status
class SensorStatusResponse(BaseModel):
    sensorId: int
    farmId: int
    status: str  # "online" or "offline"
    lastReadingAt: datetime
    offlineForHours: int