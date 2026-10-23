from fastapi import HTTPException
from app import repository, adapter, event_publisher

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

def add_reading(sensor_id: int, new_reading):
    sensor = repository.get_sensor(sensor_id)
    if sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")

    reading = adapter.standardise_reading(sensor, new_reading)
    saved_reading = repository.save_reading(reading)

    event_publisher.publish_reading_event(saved_reading)

    return {
        "readingId": saved_reading["readingId"],
        "sensorId": saved_reading["sensorId"],
        "farmId": saved_reading["farmId"],
        "message": "Reading recorded successfully",
    }
