from fastapi import HTTPException
from app import repository

def get_latest_readings(farm_id: int):
    sensors = repository.get_sensors_by_farm(farm_id)
    if not sensors:
        raise HTTPException(status_code=404, detail="Farm not found")

    latest_readings = []
    for sensor in sensors:
        reading = repository.get_latest_reading(sensor["sensorId"])
        if reading is not None:
            latest_readings.append({
                "sensorId": reading["sensorId"],
                "readingType": reading["readingType"],
                "value": reading["value"],
                "unit": reading["unit"],
                "recordedAt": reading["recordedAt"],
            })

    return {
        "farmId": farm_id,
        "readings": latest_readings,
    }