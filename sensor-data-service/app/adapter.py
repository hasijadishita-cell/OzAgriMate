from fastapi import HTTPException

# Reject impossible soil moisture readings
def validate_reading(reading):
    if reading.readingType == "soilMoisture":
        if reading.value < 0 or reading.value > 100:
            raise HTTPException(
                status_code=400,
                detail="soilMoisture must be between 0 and 100 %",
            )

# Check the reading, then convert it into the OzAgriMate format for saving
def standardise_reading(sensor: dict, reading):
    validate_reading(reading)

    return {
        "sensorId": sensor["sensorId"],
        "farmId": sensor["farmId"],
        "readingType": reading.readingType,
        "value": reading.value,
        "unit": reading.unit,
        "recordedAt": reading.recordedAt,
    }