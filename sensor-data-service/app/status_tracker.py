from app import repository
from fastapi import HTTPException
from datetime import datetime

def get_sensor_status(sensor_id: int):
    sensor = repository.get_sensor(sensor_id)

    if sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")

    last_reading = repository.get_latest_reading(sensor_id)
    if last_reading is None:
        raise HTTPException(status_code=404, detail="No readings recorded for this sensor")

    now = datetime.now().astimezone().replace(microsecond=0)
    time_since_last_reading = now - last_reading["recordedAt"]

    # Offline if there has been no reading for 24 hours
    if time_since_last_reading.days >= 1:
        status = "offline"
        offline_for_hours = int(time_since_last_reading.total_seconds() // 3600)
    else:
        status = "online"
        offline_for_hours = 0

    return {
        "sensorId": sensor["sensorId"],
        "farmId": sensor["farmId"],
        "status": status,
        "lastReadingAt": last_reading["recordedAt"],
        "offlineForHours": offline_for_hours,
    }